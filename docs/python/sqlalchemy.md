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

Continue from

[https://docs.sqlalchemy.org/en/14/tutorial/metadata.html](https://docs.sqlalchemy.org/en/14/tutorial/metadata.html)




## Source

* [SQLALchemy Overview](https://docs.sqlalchemy.org/en/14/intro.html)


