---
author: ''
category: Postgres
date: '2022-11-08'
summary: ''
title: Postgres  Terminology
---

# Postgres  Terminology

## Cluster

A full instance running the Postgres process is a cluster.

Calling it a database may lead to confusion.

A running postgres cluster has:

* a base backup
* associate WAL (write-ahead-log)

## Database

Connections are made to a database - not to a cluster.

Eg: `postgres://fixes.MyPassWord@xyz.db.postgresbridge.com:5432/mydatabase`

* connector: `postgres`
* user: `fixes`
* password: `MyPassWord`
* host: `xyz.db.postgresbridge.com`
* port: `5432`
* db: `mydatabase`

> The database portion can be postgres which is the default Postgres database

When you do a `pg_dump` against a Postgres database it is only that database, where-as the base backup and WAL is for all of the databases contained within a cluster.

## Schema

> Most of the time when you talk about schema you mean the tables and columns you create inside your database

A folder in your database.

However, postgres's schemas are logically separated by a **namespace** within the database

By default you're mostly working with the `public` schema which you get by default.

In postgres you have something called a `search_path`:

    show search_path;
    "$user", public

> You can update your search path to search across multiple schemas, it will search them in order for matching table names.

You can also execute fully qualified queries:

    SELECT *
    FROM orders;

    SELECT *
    FROM public.orders;

View all schemas;

    SELECT * FROM pg_namespace

## Tuple

A row in a table.
A number of attributes: a name, value and data type

tuple set - a set of rows (a queryset?)

## Record and Row

Mean the same as a tuple however they are also postgres SQL keywords. Tuple is not a postgres SQL keyword.

The `record` keyword is most frequently used as a return type in server side functions that return composite types.

    CREATE FUNCTION onerow(pk integer)
        RETURNS record AS
        $$
            SELECT * FROM mytable WHERE mytable.pk = pk
        $$
    LANGUAGE 'sql';

The `row` keyword is used to construct composite (tuple valued) types within SQL.

    INSERT INTO on_hand VALUES (ROW('fuzzy dice', 42, 1.99), 1000);

## Array

A list of values that are all the same type

    SELECT ARRAY[1,2,3,4];

Arrays can be multi-dimensional:

    SELECT ARRAY[[1,2,3],[4,5,6]];

Not restricted to built-in types, they can be any type:

    CREATE TYPE person AS (name text, age integer);
    SELECT ('Peter',45)::person;
    SELECT ARRAY[('Peter',45),('Paul',35)]::person[];

## Relation

* a "relation" is a collection of tuples
* a single tuple is a "unary relation"
* two tuples are a "binary relation"

We usually call relations "tables"

Views are also relations.

Relations are the results of queries.

See all relations with:

    SELECT relname, relkind FROM pg_class

You will also see indexes, views, sequences, materialized views, and foreign tables.

## Target List and Restrictions

Parts of a SQL query

    SELECT <target list>
    FROM mytable
    WHERE <restrictions>

## Page

Down at the level of the disk, database tables reside in files, one file per table.

Rather than one tightly stuffed file of data, the database internally divides the table file into regularly spaced "pages", and only partially fills each page with tuples.

Now, when the database needs to update a tuple, to perhaps add more data, only the page of interest needs to be re-written, and the rest of the file can remain untouched.

The "page" is in many ways the fundamental unit of the underlying database engine. You don't see it when writing SQL, but things like the "page cache" (a piece of RAM where frequently read pages are placed for high-speed access) and the "random page cost" (a tuning parameter that expresses how expensive random access within files is) testify to the centrality of the "page" in the system design of the database.

**PostgreSQL pages are fixed at exactly 8192 bytes.**

That is also the default size of memory “blocks” in areas like the WAL.
Some block sizes can be increased; pages, never.

## TOAST

[The Oversized Attribute Storage Technique](https://www.postgresql.org/docs/current/storage-toast.html)

When a page grows bigger than 8kb.

When an incoming attribute is too large to fit into a page, Postgres slices it into smaller pieces that do fit inside a page, and puts those pieces into a special "TOAST table" associated with the main table.

Then, when you go to retrieve that tuple, the database goes to the TOAST table, gets the pieces and glues them back together again before returning them to you.

Find a toast table linked to an original:

    SELECT a.relname, b.relname AS toast_relname
    FROM pg_class a
    JOIN pg_class b
    ON a.reltoastrelid = b.oid
    WHERE a.relname = 'mytablename';

This tuple re-construction time is the main point of visibility of the TOAST system: retrieving a batch of TOASTed tuples will take longer than retrieving a similar batch of smaller tuples!

* there is just more data in the TOASTed records
* gluing together the TOASTed pieces takes a non-zero amount of computational time.






## Sources

* [Crunchydata: Databases and SChemas](https://www.crunchydata.com/blog/postgres-databases-and-schemas)
* [Crunchdata: Postgres Insider Terminology](https://www.crunchydata.com/blog/challenging-postgres-terminology)
