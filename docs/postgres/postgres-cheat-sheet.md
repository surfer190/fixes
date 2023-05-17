---
author: ''
category: Postgres
date: '2020-08-13'
summary: ''
title: Postgres Cheat Sheet
---
# Postgres Cheatsheet 

A quick reference for  quick and dirty postgres commands

### Change databases

When you connect to postgres it is always on a specific db

to change databases, close the old connection and reconnect on the new database:

    \c name_database

[Copy data from table in one schema to another](https://stackoverflow.com/questions/39890502/how-to-copy-certain-tables-from-one-schema-to-another-within-same-db-in-postgres)

    insert into schema2.the_table
    select * 
    from schema1.the_table;

View the size of a database:

    \l+ <database_name>

View schemas in a db

    select nspname from pg_catalog.pg_namespace;

[Alter or change  the public schema name](https://stackoverflow.com/questions/24080832/postgres-best-way-to-move-data-from-public-schema-of-one-db-to-new-schema-of-an)

    alter schema public rename to original_public;
    create schema public;

[Add superuser privilege to a user](https://stackoverflow.com/questions/10757431/postgres-upgrade-a-user-to-be-a-superuser)

In psql:

    ALTER USER my_user WITH SUPERUSER;

[List all databases](https://dba.stackexchange.com/questions/1285/how-do-i-list-all-databases-and-tables-using-psql)

In psql:

    \l

[View the users and roles of a postgres instance](https://unix.stackexchange.com/questions/201666/command-to-list-postgresql-user-accounts)

In psql:

    \du 

[View the schemas in a postgres database](https://dba.stackexchange.com/questions/40045/how-do-i-list-all-schemas-in-postgresql/40051)

In psql:

    \dn

[Reset a postgres user password](https://stackoverflow.com/questions/12720967/how-to-change-postgresql-user-password)

In psql:

    ALTER USER user_name WITH PASSWORD 'new_password';

[Postgres connection strings](https://stackoverflow.com/questions/3582552/postgresql-connection-url)

    postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]

## Dump (Backup) and Restore

Dump a remote database

    pg_dump -U {username} -h {ip} -p 5432 {database_name} > {backup_name}.bak

> ensure your pg_dump version matches or you might get something like:

    pg_dump: error: server version: 14.5; pg_dump version: 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
    pg_dump: error: aborting because of server version mismatch

Create a database and user for access to it:

    sudo -u postgres psql
    create database {db_name};
    create user {username} with encrypted password '{password}';
    grant all privileges on database {db_name} to {username};

Restore the database:

    sudo -u postgres psql {db_name} < {backup_name}.bak

## PSQL Cheatsheet

Select a database

    \c <db_name>

list tables (and owners)

    \dt

## Get the version

    postgres=# SELECT version();
    PostgreSQL 10.21 (Ubuntu 10.21-0ubuntu0.18.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0, 64-bit
    (1 row)

## Trouble shooting ownership

Ever get this:

    psycopg2.errors.InsufficientPrivilege: must be owner of table section
    peewee.ProgrammingError: must be owner of table section

then the owner of the table is not the current user - so it cannot drop that table.

Check table ownership with:

    \dt+

## Delete a database

    DROP database <mydbname>;

## Create a user and grant access to a db

    create user pali_canon with encrypted password 'pali_canon';
    grant all privileges on database pali_canon to pali_canon;

## How to Query an Array Field

Check if an array field contains a value

    select * from mytable where 'Journal'=ANY(array_test_types);

An array field is seen as `int[]` or `bigint[]` in PG Admin.

## Difference Between Double Quotes and Single Quotes in Postgres SQL

> There is a difference between single quotes and double quotes in PostgreSQL. Unlike python.

* Double quotes are for names of tables or fields.
* The single quotes are for string constants

## Enable Extension

    CREATE EXTENSION <extension name>;

eg. `CREATE EXTENSION pg_stat_statements;`

## Disable Extension

    DROP EXTENSION IF EXISTS <extension_name>;

eg. `DROP EXTENSION IF EXISTS pg_stat_statements;`

## Reset PgStatStatement

    select pg_stat_statements_reset();

## Check if extension is enabled

From `psql`:

    \dx

or in plain old SQL:

    SELECT * FROM pg_extension;

## View indexes on a table

From `psql`:

    \d+ <table_name>

## Checking Table Sizes

    \d+

## Check available extensions

    SELECT name FROM pg_available_extensions;

## Drop index

    DROP INDEX CONCURRENTLY <index_name>

[Postgres docs: Drop index](https://www.postgresql.org/docs/current/sql-dropindex.html)

## Check the size of an index

In psql:

    \di+

## Check Index Stats

    SELECT
        relname,
        indexrelname,
        idx_scan,
        idx_tup_read,
        idx_tup_fetch,
        pg_size_pretty(pg_relation_size(indexrelname::regclass)) as size
    FROM
        pg_stat_all_indexes
    WHERE
        schemaname = 'public'
        AND indexrelname NOT LIKE 'pg_toast_%'
    ORDER BY
        pg_relation_size(indexrelname::regclass) DESC;

## Check Table Stats (Shows Index vs Sequential scans)

    SELECT pg_stat_user_tables.schemaname,
        pg_stat_user_tables.relname,
        pg_stat_user_tables.seq_scan,
        pg_stat_user_tables.seq_tup_read,
        pg_stat_user_tables.idx_scan,
        pg_stat_user_tables.idx_tup_fetch
        FROM pg_stat_user_tables;

## Get size of a specific table

    SELECT pg_size_pretty (pg_relation_size('table_name'));

eg:

    SELECT pg_size_pretty (pg_relation_size('products'));

## Check when Last the Stats Database has been Reset

    SELECT datname, stats_reset FROM pg_stat_database;

## Reset Stats for a Database

    SELECT pg_stat_reset();

> Only resets stats on db of connected session

## Drop a table

    DROP TABLE <table_name>

[Postgres docs: Drop table](https://www.postgresql.org/docs/current/sql-droptable.html)

## Create a multi-column index

Do the index types have to be the same?

    CREATE INDEX CONCURRENTLY test2_mm_idx ON test2 (major, minor);

[Postgres docs: Create a multicolumn index](https://www.postgresql.org/docs/9.6/indexes-multicolumn.html)

## Reindex an index

REINDEX INDEX CONCURRENTLY <table_name>

## View active connections

    select *
    from pg_stat_activity
    where datname = 'mydatabasename';

## Sources

* [Postgres: Check if array field contains a value](https://stackoverflow.com/questions/39643454/postgres-check-if-array-field-contains-value)
* [Postgres docs: String constants](https://www.postgresql.org/docs/9.4/sql-syntax-lexical.html)
* [Install and Configure postgres 14 on ubuntu 20.04](https://www.atlantic.net/dedicated-server-hosting/how-to-install-and-configure-postgres-14-on-ubuntu-20-04/)
* [Postgres: list installed extensions](https://stackoverflow.com/questions/21799956/using-psql-how-do-i-list-extensions-installed-in-a-database/21799995)
