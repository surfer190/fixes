---
author: ''
category: Python
date: '2022-07-22'
summary: ''
title: Sqlalchemy
---
# SQLAlchemy: Fundamentals

SQLALchemy is a comprehensive set of tools for working with databases and Python

It consists of:

* Object Relational Mapper (ORM + Session) - domain-centric view
* the Core (SQL Expression Language, Schema and Types, Engine, Connection Pooling and Dialect) - schema-centric view

## Installation and checking version

    pip install sqlalchemy

Check version:

    >>> import sqlalchemy
    >>> sqlalchemy.__version__ 
    '1.4.39'

## Establishing Connectivity - the Engine

Starts with the `Engine`: central source of connections and a holding space for connections called a connection pool

> The engine is typically a global object created just once for a particular database server - configured with a url string

The engine is created with `create_engine()`

    from sqlalchemy import create_engine
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

> This uses a in-memory sqlite db

The connection string (`"sqlite+pysqlite:///:memory:"`) indicates:

* The kind of database (`sqlite`) - a dialect linked to a database driver or DB-API
* The DB-API we are using (`pysqlite`) - the third-party driver in this case the `sqlite` standard library
* How to locate the database (`/:memory`) - an in-memory database

> Lazy initialization - the connection is only established when it is first used

We used `echo=True` a shortcut to setup python logging

## Working with Transactions and the DBAPI

The `Engine`s primary endpoints are `Connection` and `Result` - the facade (front facing interface hiding the internals) is `Session`.

You can always run pure SQL with `text()`

    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("select 'hello world'"))
        print(result.all())

Running it gives:

    2022-07-22 10:31:35,068 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2022-07-22 10:31:35,068 INFO sqlalchemy.engine.Engine select 'hello world'
    2022-07-22 10:31:35,068 INFO sqlalchemy.engine.Engine [generated in 0.00015s] ()
    [('hello world',)]
    2022-07-22 10:31:35,068 INFO sqlalchemy.engine.Engine ROLLBACK

* the context manager provided for a database connection
* framed the operation inside of a transaction
* The default behavior of the Python DBAPI - a transaction is always in progress - when scope is released a `ROLLBACK` is emitted to end the transaction
* **The transaction is not committed automatically** - you need to run `Connection.commit()` - `autocommit` is only for special cases

Here is an example commiting the data:

    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
        )
        conn.commit()

You can have multiple `commit()`s in that context manager - called **commit-as-you-go**

Another style is with an automatic commit at the end within the transaction:

    with engine.begin() as conn:
        conn.execute(
            sqlalchemy.text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
        )

> This is the **begin once** style

#### Quick Terms

* DDL: Data Definition Language - configure tables, constraints, and other permanent objects within a database schema.
* DML: Data Manipulation Language - use to modify the data in tables (CRUD - create, read, update and delete)

## Basics of Statement Execution

Fetching rows

    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM some_table"))
        for row in result:
            print(f"x: {row.x}  y: {row.y}")

What does result look like:

    <sqlalchemy.engine.cursor.CursorResult object at 0x10219eaf0>

It has a few operations you can do on it:

    ipdb> dir(result)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_allrows', '_assert_no_memoizations', '_attributes', '_column_slices', '_cursor_metadata', '_cursor_strategy_cls', '_echo', '_fetchall_impl', '_fetchiter_impl', '_fetchmany_impl', '_fetchone_impl', '_generate', '_generate_rows', '_getter', '_init_metadata', '_is_cursor', '_iter_impl', '_iterator_getter', '_manyrow_getter', '_memoized_keys', '_metadata', '_next_impl', '_no_result_metadata', '_onerow_getter', '_only_one_row', '_post_creational_filter', '_process_row', '_raw_all_rows', '_raw_row_iterator', '_real_result', '_reset_memoizations', '_row_getter', '_row_logging_fn', '_set_memoized_attribute', '_soft_close', '_soft_closed', '_source_supports_scalars', '_tuple_getter', '_unique_filter_state', '_unique_strategy', '_yield_per', 'all', 'close', 'closed', 'columns', 'connection', 'context', 'cursor', 'cursor_strategy', 'dialect', 'fetchall', 'fetchmany', 'fetchone', 'first', 'freeze', 'inserted_primary_key', 'inserted_primary_key_rows', 'is_insert', 'keys', 'last_inserted_params', 'last_updated_params', 'lastrow_has_defaults', 'lastrowid', 'mappings', 'memoized_attribute', 'memoized_instancemethod', 'merge', 'one', 'one_or_none', 'out_parameters', 'partitions', 'postfetch_cols', 'prefetch_cols', 'returned_defaults', 'returned_defaults_rows', 'returns_rows', 'rowcount', 'scalar', 'scalar_one', 'scalar_one_or_none', 'scalars', 'supports_sane_multi_rowcount', 'supports_sane_rowcount', 'unique', 'yield_per']

It has a `.all()` which returns results as a list or we can iterate overit because it implements python's iterator interface.

The Row object:

    ipdb> type(row)
    <class 'sqlalchemy.engine.row.Row'>

Rows can be used with `.` notation for the attribute name:

    ipdb> row.x
    1
    ipdb> row.y
    1

or win many other ways...

### Sending parameters

To send parameters, in the SQL you refer to the variable name and prepend with `:`...eg. `:my_var` and then you send in a dict with `{'my_var': 40}`.
This allows sqlalchemy to sanitise the data.

> Bound parameters (seperating the query from the parameters) should always be used - to avoid SQL Injection

We can run a list of inserts (provided the statement does not have a return) - it is really using `executemany()` behind the scenes.

    >>> with engine.connect() as conn:
            conn.execute(
                text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
                [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
            )
            conn.commit()

You can also bundle paramters into a statement:

    stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
    with engine.connect() as conn:
        result = conn.execute(stmt)

## Executing with an ORM Session

> The fundamental transactional / database interactive object when using the ORM is called the Session.

    from sqlalchemy.orm import Session

    stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
    with Session(engine) as session:
        result = session.execute(stmt)
        for row in result:
            print(f"x: {row.x}  y: {row.y}")

> The `Session` doesn’t actually hold onto the `Connection` object after it ends the transaction. It gets a new Connection from the Engine when executing SQL against the database is next needed.

[More info on Session](https://docs.sqlalchemy.org/en/14/orm/session_basics.html)

## Working with Database Metadata

[Metadata](https://docs.sqlalchemy.org/en/14/tutorial/metadata.html)

> Metadata is objects that represent database concepts like tables and columns

The most common foundational objects are: MetaData, Table, and Column

1. we will want to have `Table` objects constructed that represent all of the database tables we are interested in working with.
2. Each Table may be **declared**, meaning we explicitly spell out in source code what the table looks like, or may be **reflected** - we generate the object based on what’s already present in a particular database.

Start with a collection known as a `MetaData` object - a facade around a python dictionary storing a series of tables keyed to their string name.

Constructing the metadata object:

    from sqlalchemy import MetaData
    metadata_obj = MetaData()

> Having a single MetaData object for an entire application is the most common case

Once we have a MetaData object, we can declare some Table objects:

    from sqlalchemy import Table, Column, Integer, String

    user_table = Table(
        "user_account",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("fullname", String),
    )

* `Table` - represents a database table and assigns itself to a metadata collection
* `Column` - represents a column in a database table, and assigns itself to a `Table` object. The Column usually includes a string name and a type object.
* `String` and `Integer` - SQL data types

    >>> user_table.c.name
    Column('name', String(length=30), table=<user_account>)

    >>> user_table.c.keys()
    ['id', 'name', 'fullname']

Primary key is usally declared implicitly:

    >>> user_table.primary_key
    PrimaryKeyConstraint(Column('id', Integer(), table=<user_account>, primary_key=True, nullable=False))

Foreign keys are usually declared explicity using the `ForeignKey` object

    >>> from sqlalchemy import ForeignKey
    >>> address_table = Table(
    ...     "address",
    ...     metadata_obj,
    ...     Column("id", Integer, primary_key=True),
    ...     Column("user_id", ForeignKey("user_account.id"), nullable=False),
    ...     Column("email_address", String, nullable=False),
    ... )

> When using the ForeignKey object within a Column definition, we can omit the datatype for that Column; it is automatically inferred from that of the related column

### Emitting DDL to the Database

DDL - Data definition language, or emitting `CREATE TABLE...` statement

    metadata_obj.create_all(engine)

There is also a:

    MetaData.drop_all()

> Overall, the `CREATE / DROP` feature of MetaData is useful for test suites, small and/or new applications, and applications that use short-lived databases. For management over the long term a schema management tool like alembic is preferable.

### Defining Table Metadata with the ORM

Declaring tables is done with mapped python classes

When using the ORM, the MetaData collection remains present, however it itself is contained within an ORM-only object known as the `registry`

    from sqlalchemy.orm import registry
    mapper_registry = registry()

The registry includes a metadata object:

    mapper_registry.metadata

Each mapped class descends from a common base class called the **Delcarative Base**. We get the declarative base from the registry:

    Base = mapper_registry.generate_base()

The above can be combined into a shorter:

    from sqlalchemy.orm import declarative_base
    Base = declarative_base()

#### Declaring Mapped Classes

    from sqlalchemy.orm import relationship

    class User(Base):
        __tablename__ = "user_account"

        id = Column(Integer, primary_key=True)
        name = Column(String(30))
        fullname = Column(String)
        addresses = relationship("Address", back_populates="user")

        def __repr__(self):
            return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

    class Address(Base):
        __tablename__ = "address"

        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey("user_account.id"))

        user = relationship("User", back_populates="addresses")

        def __repr__(self):
            return f"Address(id={self.id!r}, email_address={self.email_address!r})"

These declarative tables also include `Table` objects - equivalent to those seen in table metadata.

    >>> User.__table__
    Table('user_account', MetaData(),
        Column('id', Integer(), table=<user_account>, primary_key=True, nullable=False),
        Column('name', String(length=30), table=<user_account>),
        Column('fullname', String(), table=<user_account>), schema=None)

> The decalarative process will name the fields automatically based on the attribute name

* the classes have an automatically generated `__init__()` method, so instances can be created:

    sandy = User(name="sandy", fullname="Sandy Cheeks")

* we provided a optional `__repr__()` method
* we also included a bidirectional relationship - this is another fully optional construct, where we made use of an ORM construct called `relationship()` on both classes, which indicates to the ORM that these `User` and `Address` classes refer to each other in a one to many / many to one relationship

#### Emitting the DDL to the database

    mapper_registry.metadata.create_all(engine)

    # the identical MetaData object is also present on the
    # declarative base
    Base.metadata.create_all(engine)

### Combining Core Table Declarations with ORM Declarative

You can have a hybrid approach of declarative tables and metadata table objects.
A hybrid table where the `__table__` is assigned instead of it being acquired automatically using the `__tablename__`.

Eg.

    mapper_registry = registry()
    Base = mapper_registry.generate_base()


    class User(Base):
        __table__ = user_table

        addresses = relationship("Address", back_populates="user")

        def __repr__(self):
            return f"User({self.name!r}, {self.fullname!r})"


    class Address(Base):
        __table__ = address_table

        user = relationship("User", back_populates="addresses")

        def __repr__(self):
            return f"Address({self.email_address!r})"

> In general one would choose a single approach

### Table Reflection

Generating Table and related objects by reading the current state of a database.

    some_table = Table("some_table", metadata_obj, autoload_with=engine)

`Column` and `Constraint` objects, pass it the target `Engine` using the `Table.autoload_with`

    >>> some_table
    Table('some_table', MetaData(),
        Column('x', INTEGER(), table=<some_table>),
        Column('y', INTEGER(), table=<some_table>),
        schema=None)

More on:

* [Reflecting Database Objects](https://docs.sqlalchemy.org/en/14/core/reflection.html)
* [Mapping Declaratively with Reflected Tables](https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html#orm-declarative-reflected)

## Working with Data

> Our interaction with the database is always in terms of a transaction, even if we’ve set our database driver to use autocommit behind the scenes

### Selecting Rows with Core or ORM

The `select()` function generates a Select construct which is used for all SELECT queries.

Passed to methods:

* `Connection.execute()` in `Core`
* `Session.execute()` in `ORM`

#### The select() SQL Expression Construct

A select in sqlalchemy core:

    from sqlalchemy import select

    stmt = select(user_table).where(user_table.c.name == "spongebob")
    print(stmt)

    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)

A select with sqlalchemy ORM:

    from sqlalchemy import select

    stmt = select(User).where(User.name == "spongebob")
    pritn(stmt)

    with Session(engine) as session:
        for row in session.execute(stmt):
            print(row)

### A Quick Word on Session and SessionMaker

* `sessionmaker` acts as a factory for `Session` objects
* `Engine` acts as a factory for `Connection` objects

[Session and SessionMaker](https://docs.sqlalchemy.org/en/14/orm/session_api.html#session-and-sessionmaker)

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # an Engine, which the Session will use for connection
    # resources
    engine = create_engine('postgresql://scott:tiger@localhost/')

    Session = sessionmaker(engine)

    with Session() as session:
        session.add(some_object)
        session.add(some_other_object)
        session.commit()

or use with a try...finally:

    session = Session()
    try:
        session.add(some_object)
        session.add(some_other_object)
        session.commit()
    finally:
        session.close()

To open and automatically commit a transaction use `Session.begin()`:

    Session = sessionmaker(engine)

    with Session.begin() as session:
        session.add(some_object)
        session.add(some_other_object)

### Setting the COLUMNS and FROM clause

Using the sqlalchemy core approach:

    print(select(user_table.c.name, user_table.c.fullname))

When using the full entity `User` and using `session.execute()` - the entity itself is returned as a single element within each row.
What is returned is row objects - having a single `User` element.

    row = session.execute(select(User)).first()

To get just the instance of the User class:

    user = session.scalars(select(User)).first()

> ie. this will return a User instance, not a tuple where the first element is a User instance

You can also select individual columns:

    print(select(User.name, User.fullname))

With `session.execute()` the items have individual elements:

    >>> row = session.execute(select(User.name, User.fullname)).first()
    >>> row
    ('spongebob', 'Spongebob Squarepants')

Selecting from multiple tables:

    session.execute(
        select(User.name, Address).where(User.id == Address.user_id).order_by(Address.id)
    ).all()

### The WHERE clause

An expression is created:

    print(user_table.c.name == "squidward")

Then applied:

    print(select(user_table).where(user_table.c.name == "squidward"))

multiple where clauses:

    print(
        select(address_table.c.email_address).where(
            user_table.c.name == "squidward", address_table.c.user_id == user_table.c.id
        )
    )

this generates:

    SELECT address.email_address
    FROM address, user_account
    WHERE user_account.name = :name_1 AND address.user_id = user_account.id

or use `_and` and `_or`:

    from sqlalchemy import and_, or_
    print(
            select(Address.email_address).where(
                and_(
                    or_(User.name == "squidward", User.name == "sandy"),
                    Address.user_id == User.id,
                )
            )
        )

For simple equality comparisons use `filter_by`:

    print(select(User).filter_by(name="spongebob", fullname="Spongebob Squarepants"))

### Explicit FROM clauses and JOINs

Selecting columns from a specific table - puts it in the from clause automatically

    >>> print(select(user_table.c.name, address_table.c.email_address))

gives:

    SELECT user_account.name, address.email_address
    FROM user_account, address

To join, you can use `join_from` which lets you set the left and right sides of the join explicitly:

    print(
        select(user_table.c.name, address_table.c.email_address).join_from(
            user_table, address_table
        )
    )

gives:

    SELECT user_account.name, address.email_address
    FROM user_account JOIN address ON user_account.id = address.user_id

or you can use `join()` to set the right side of the join, the left side is inferred:

    print(select(user_table.c.name, address_table.c.email_address).join(address_table))

gives:

    SELECT user_account.name, address.email_address
    FROM user_account JOIN address ON user_account.id = address.user_id

> The `ON` clause is inferred

Add a from clause fi it is not inferred how it is required `select_from(user_table)`:

    print(select(address_table.c.email_address).select_from(user_table).join(address_table))

Also if the columns clause does not have enough info:

    from sqlalchemy import func
    print(select(func.count("*")).select_from(user_table))

### Setting the On Clause

> When there is a `ForeignKeyConstraint` the `ON` clause can be created automatically, if not you can set it explicitly

    print(
        select(address_table.c.email_address).select_from(user_table).join(
            address_table, user_table.c.id == address_table.c.user_id
        )
    )

> You only need to use `<table>.c.<column_name>` when using sqlalchemy code - inferred table. A declarative table doesn't need the `c`.

### Outer and Full Joins

> Both the `Select.join()` and `Select.join_from()` methods accept keyword arguments `Select.join.isouter` and `Select.join.full` which will render `LEFT OUTER JOIN` and `FULL OUTER JOIN`, respectively.

Left outer join - left table shown - match and unmatched rows on right

    >>> print(select(user_table).join(address_table, isouter=True))

    SELECT user_account.id, user_account.name, user_account.fullname
    FROM user_account LEFT OUTER JOIN address ON user_account.id = address.user_id

Full outer join - all matched and unmatch rows are shown:

    >>> print(select(user_table).join(address_table, full=True))
    SELECT user_account.id, user_account.name, user_account.fullname
    FROM user_account FULL OUTER JOIN address ON user_account.id = address.user_id

### ORDER BY, GROUP BY, HAVING

#### ORDER BY

The `Select.order_by()` method accepts one or more positional expressions

    select(user_table).order_by(user_table.c.name)

Use `Column.desc()` or `Column.asc()`:

    select(User).order_by(User.fullname.desc())

#### Aggregate functions with GROUP BY / HAVING

Multiple rows can be aggregates with a : Count, Average, Min and Max.

SQLAlchemy provides for SQL functions in an open-ended way using a namespace known as `func`

    from sqlalchemy import func
    count_fn = func.count(user_table.c.id)
    print(count_fn)

Example:

    >>> with engine.connect() as conn:
        result = conn.execute(
            select(User.name, func.count(Address.id).label("count"))
            .join(Address)
            .group_by(User.name)
            .having(func.count(Address.id) > 1)
        )
        print(result.all())

#### Ordering or Grouping by a Label

To order or group by an expression in the columns clause.

    from sqlalchemy import func, desc
    stmt = (
        select(Address.user_id, func.count(Address.id).label("num_addresses"))
        .group_by("user_id")
        .order_by("user_id", desc("num_addresses"))
    )
    print(stmt)

#### Aliases

Whenever you use `AS` in raw SQL you are using an alias.

For table entities of sqlalchemy core:

    user_alias_1 = user_table.alias()
    user_alias_2 = user_table.alias()

The ORM equivalent is:

    from sqlalchemy.orm import aliased
    address_alias_1 = aliased(Address)
    address_alias_2 = aliased(Address)

#### Subqueries and 

SQLAlchemy uses the `Subquery` object to represent a subquery. It is obtained from the `Select.subquery()` method.

    subq = (
        select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
        .group_by(address_table.c.user_id)
        .subquery()
    )

The `Subquery` object behaves like any other FROM object such as a `Table`

The columns can be referenced from the `SubQuery.c` namespace, eg:

    print(select(subq.c.user_id, subq.c.count))

Joining to a subquery:

    stmt = select(user_table.c.name, user_table.c.fullname, subq.c.count).join_from(
        user_table, subq
    )

Results in:

    SELECT user_account.name, user_account.fullname, anon_1.count
    FROM user_account JOIN (SELECT count(address.id) AS count, address.user_id AS user_id
    FROM address GROUP BY address.user_id) AS anon_1 ON user_account.id = anon_1.user_id

#### CTEs

CTE - Common table expression

The CTE is obtained from the `Select.cte()` method.

    subq = (
        select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
        .group_by(address_table.c.user_id)
        .cte()
    )

    stmt = select(user_table.c.name, user_table.c.fullname, subq.c.count).join_from(
        user_table, subq
    )

    print(stmt)

Results in:

    WITH anon_1 AS
    (SELECT count(address.id) AS count, address.user_id AS user_id
    FROM address GROUP BY address.user_id)
    SELECT user_account.name, user_account.fullname, anon_1.count
    FROM user_account JOIN anon_1 ON user_account.id = anon_1.user_id

It may in more elaborate cases be composed from the `RETURNING` clause of an `INSERT`, `UPDATE` or `DELETE` statement

> In both cases, the subquery and CTE were named at the SQL level using an “anonymous” name (`anon`). In the Python code, we don’t need to provide these names at all. The object identity of the Subquery or CTE instances serves as the syntactical identity of the object when rendered. A name that will be rendered in the SQL can be provided by passing it as the first argument of the `Select.subquery()` or `Select.cte()` methods.

#### ORM Entity Subqueries/CTEs

Using the sqlalchemy core aliases above, mean that the resultant data will include the rows in a tuple.
If you want to get an ORM object use the ORM alias for the Subquery - telling sqlalchemy the model to use.

    address_subq = aliased(Address, subq)

> This can also be used with the CTE's

#### More in the Docs on:

* [Scalar and Correlated Subqueries](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#scalar-and-correlated-subqueries)
* [UNION, UNION ALL and other set operations](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#union-union-all-and-other-set-operations)
* [EXISTS subqueries](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#exists-subqueries)
* [Working with SQL Functions](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#working-with-sql-functions)
* [Data Casts and Type Coercion](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#data-casts-and-type-coercion)

## Data Manipulation with the ORM

### Inserting Rows with the ORM

The Session object is responsible for creating inserts and emitting them.

The ORM class represents the row.

Example initialising an ORM class:

    squidward = User(name="squidward", fullname="Squidward Tentacles")
    krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")

> We are able to construct these objects using the names of the mapped columns as keyword arguments in the constructor - which go to the autogenerated `__init__` constructor.

A primary key is not included, since we would like to make use of the auto-incrementing primary key

SQLAlchemy-mapped attributes always return a value in Python and don’t raise `AttributeError` if they’re missing. So if `squidward.id` is interpreted, the result will be `None`.

The objects are transient and have not been persisted to the database.

Adding objects to a session:

    session = Session(engine)
    session.add(squidward)
    session.add(krabs)

The objects are now in a pending state - you can view the pending items with `session.new`

#### Flushing

The session makes use of `unit of work` - a list of changes are kept and periodically flushed to the database.
It accumulates changes one at a time but does not communicate them until needed.

When it does emit SQL - it is known as a flush.

You can manually flush with `session.flush()`

The transaction now remains open until we call any of the `Session.commit()`, `Session.rollback()`, or `Session.close()` methods of Session.

Not needed to manually flush, the system with autoflush.

> Why are seperate `INSERT` statements sent - and not a `executemany`? It needs the primary key. If we know the pk before hand this will be optimised . Some database backends such as `psycopg2` can also INSERT many rows at once while still being able to retrieve the primary key values.

#### Identity Map

The identity map is an in-memory store that links all objects currently loaded in memory to their primary key identity

We can get the object without emitting a `SELECT`:

    some_squidward = session.get(User, 4)

It maps to the same object:

    >>> some_squidward is squidward
    True

#### Commiting

At the end, you commit:

    session.commit()

### Updating ORM Objcts

Get a row:

    sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()

The python object is a proxy for a row in the db

    >>> sandy
    User(id=2, name='sandy', fullname='Sandy Cheeks')

If the record is altered:

    >>> sandy.fullname = "Sandy Squirrel"

The object is indicated as `dirty`:

    sandy in session.dirty
    True

As mentioned previously, a flush occurs automatically before we emit any SELECT, using a behavior known as autoflush

    sandy in session.dirty
    False

#### TroubleShooting

If you are adding related records with related fields you may get:

    sqlalchemy.exc.ProgrammingError: (psycopg2.ProgrammingError) can't adapt type 'MyModel'

This happens when the related records have not been commited (and have a primary key). Also when you use the instance and not the primary key if it was defined that way in the models.

Given the fields for the `CatalogueVersion` model:

    product_file_id  = Column(BigInteger, ForeignKey(ProductFile.id))
    taxonomy_file_id = Column(BigInteger, ForeignKey(TaxonomyFile.id))

When createing the `CatalogueVersion` it is expecting the id - not the instance:

    catalogue_version = CatalogueVersion(
        product_file_id=product_file,
        taxonomy_file_id=category_file
    )

vs:

    catalogue_version = CatalogueVersion(
        product_file_id=product_file.id,
        taxonomy_file_id=category_file.id
    )

#### Handling IntegrityError

How do you handle `sqlalchemy.exc.IntegrityError`?

Since a large number of inserts are happening - in bulk - how would you handle the individual case?

> The Integrity Error isn't thrown until the session is flushed to the db



### ORM-Enabled Updates

Similar to SQL UPDATE

    session.execute(
        update(User)
        .where(User.name == "sandy")
        .values(fullname="Sandy Squirrel Extraordinaire")
    )

### Deleting ORM Objects



## SQLAlchemy Query get raw SQL query

    from sqlalchemy.dialects import postgresql
    >>> print(str(query.statement.compile(dialect=postgresql.dialect())))

## Source

* [SQLALchemy Overview](https://docs.sqlalchemy.org/en/14/intro.html)
* [How do I get a raw, compiled SQL query from a SQLAlchemy expression](https://stackoverflow.com/questions/4617291/how-do-i-get-a-raw-compiled-sql-query-from-a-sqlalchemy-expression)
* [Reflect a PostgreSQL view in SQLAlchemy](https://hultner.se/quickbits/2017-10-23-postgresql-reflection-views-python-sqlalchemy.html)
