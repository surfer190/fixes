---
author: ''
category: Python
date: '2022-07-22'
summary: ''
title: Sqlalchemy - Alembic Migrations
---

# SQLAlchemy: Alembic Migrations

Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python

> Alembic - A chemical apparatus to purify substances by distillation

## Basic Info

* Repository: [Alembic at Github](https://github.com/sqlalchemy/alembic)
* Package: [Alembic at Pypi](https://pypi.org/project/alembic/)

## Installation

> Alembic uses SQLAlchemy and database drivers

    python -m pip install alembic

* Alembic supports Python versions 3.7 and above

## Tutorial

> Alembic provides for the creation, management, and invocation of change management scripts for a relational database, using SQLAlchemy as the underlying engine

Ideally you want it installed in your virtual environment so that when you run `alembic` it has access to your models.

### The Migration Environment

* Starting point
* A directory of scripts specific to the application
* Created once and kept with applciation source code

To initialise and call the folder `alembic`:

    alembic init alembic

Example directory:

    yourproject/
        alembic/
            env.py
            README
            script.py.mako
            versions/
                3512b954651e_add_account.py
                2b1ae634e5cd_add_order_id.py
                3adcc9a56557_rename_username_field.py

* `alembic` - this directory lives within your application’s source tree and is the home of the migration environment. It can be named anything, and a project that uses multiple databases may even have more than one.
* `env.py` - script run when the mgiration tool is invoked - mostly how to connect to the db
* `script.py.mako` - the mako template used to generate migration scripts - creates the files with `/version`
* `versions/` - holds version scripts - numbering does not ascend - it uses `guid` that refer to each other. Versions from different branches can be _spliced_ by hand

Alembic has other templates based on project setup:

    alembic list_templates

### Editing the Alembic.ini File

Alembic placed a file `alembic.ini` into the current directory

The file is read using Python’s `ConfigParser.SafeConfigParser` object

* `file_template` - this is the naming scheme used to generate new migration files. Uncomment the presented value if you would like the migration files to be prepended with date and time, so that they are listed in chronological order.
    - `%%(rev)s` - revision id
    - `%%(slug)s` - a truncated string derived from the revision message
    - `%%(epoch)s` - epoch timestamp based on the create date; this makes use of the Python datetime.timestamp() method to produce an epoch value.
    - `%%(year)d`, `%%(month).2d`, `%%(day).2d`, `%%(hour).2d`, `%%(minute).2d`, `%%(second).2d` - components of the create date, by default `datetime.datetime.now()` unless the timezone configuration option is also used.
* `sqlalchemy.url` - A URL to connect to the database via SQLAlchemy.

For a single database, starting up all that is needed is:

    sqlalchemy.url = postgresql://scott:tiger@localhost/test

### Create a Migration Script

    alembic revision -m "create product table"

A new file is generated:

    """create product table

    Revision ID: 5a5a17843e58
    Revises: 
    Create Date: 2022-09-15 16:39:28.057474

    """
    from alembic import op
    import sqlalchemy as sa


    # revision identifiers, used by Alembic.
    revision = '5a5a17843e58'
    down_revision = None
    branch_labels = None
    depends_on = None


    def upgrade() -> None:
        pass


    def downgrade() -> None:
        pass

* Our job here is to populate the `upgrade()` and `downgrade()` functions with directives that will apply a set of changes to our database.
* `upgrade()` is required while `downgrade()` is only needed if down-revision capability is desired


We add:

    def upgrade():
        op.create_table(
            'product',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(50), nullable=False),
            sa.Column('description', sa.Unicode(200)),
        )

    def downgrade():
        op.drop_table('product')

* [`create_table()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.create_table) and [`drop_table()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.drop_table) are Alembic directives

### Run the Migration

Run to the most recent migration:

    alembic upgrade head

Run to a specific version:

    alembic upgrade 5a5a17843e58

* It checks if the `alembic_version` table exists - if not it creates it
* It runs upgrade in each file until it reaches the given revision

### Running the Second Migration

    alembic revision -m "Add a column"

And edit:

    def upgrade() -> None:
        op.add_column('product', sa.Column('last_modified_date', sa.DateTime))


    def downgrade() -> None:
        op.drop_column('product', 'last_modified_date')

Run the migration:

    alembic upgrade 86f

> A partial number can be used as long as the portion of the hash is unique

You can also give relative identifiers:

    alembic upgrade +2 # move 2 versions up

    alembic downgrade -1 # move 1 version down

    alembic upgrade ae10+2 # move to ae10 + 2 versions

### Getting Info

Get the current hash:

    alembic current

    INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
    INFO  [alembic.runtime.migration] Will assume transactional DDL.
    86f384da7285 (head)

Get alembic history:

    alembic history
    5a5a17843e58 -> 86f384da7285 (head), Add a column
    <base> -> 5a5a17843e58, create product table

Can also run it verbosely:

    alembic history --verbose

### Downgrade

To downgrade back to the beginning:

    alembic downgrade base

Back up again:

    alembic upgrade head

## Auto Generating Migrations

Alembic can view the status of the database and compare against the table metadata in the application, generating the “obvious” migrations based on a comparison.

Using:

    alembic revision --autogenerate

> This creates _candidate_ migrations that can be reviewed manually

In `env.py` you should add your model's metadata object

    # add your model's MetaData object here
    # for 'autogenerate' support
    # from myapp import mymodel
    # target_metadata = mymodel.Base.metadata
    target_metadata = None

changed to:

    from myapp.mymodel import Base
    target_metadata = Base.metadata

> I tried the above and it did not work. I had to import the base model but then also import all the models afterwards which is made clear by this [stackoverflow answer](https://stackoverflow.com/questions/48053955/alembic-migrations-on-multiple-models)

This is sent into the `run_migrations_online()` function

Then we can run autogeneration - and it will check the MetaData against the database and create migraitons based on it.

    alembic revision --autogenerate -m "Add existing tables"

Always look at the candidate migrations...first before applying.

    alembic upgrade head

## What does Autogenerate Detect (and not Detect)?

Autogenerate is not perfect. One must always manually review the candidate migration.

Autogenerate will detect:

* Table additions and removals
* Column additions and removals
* Change of nullable status on columns
* Changes in indexes and named unique constraints
* Changes in foreign key constraints

Autogenerate will optionally detect:

* Change of column type. [EnvironmentContext.configure.compare_type](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.compare_type) should be set to `True`
* Change of server default. [EnvironmentContext.configure.compare_server_default](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.compare_server_default) should be set to `True`

Autogenerate cannot detect:

* Changes of table name - these will come out as an add/drop of two different tables, and should be hand-edited into a name change instead.
* Changes of column name - these are detected as a column add/drop pair, which is not at all the same as a name change
* Anonymously named constraints (remember to give constraints a name)
* Special SQLAlchemy types such as `Enum` when generated on a backend which doesn’t support ENUM directly

### Controlling what is Autogenerated

Continue with [Controlling what is Autogenerated](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#controlling-what-to-be-autogenerated)

### How to Start Afresh

If you want to start from scratch again.

Remove all db tables and truncate the `alembic_version` table.
Remove the migration files in `versions`/
Run the migration autogeneration if needed.
Run the migrations.

## Source

* [Alembic Docs](https://alembic.sqlalchemy.org/en/latest/)
* [Alembic meaining: Wiktionary](https://en.wiktionary.org/wiki/alembic)
* [Stackoverflow: Alembic automatic migrations import all models](https://stackoverflow.com/questions/48053955/alembic-migrations-on-multiple-models)
