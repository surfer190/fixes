---
author: ''
category: Postgres
date: '2022-10-24'
summary: ''
title: Postgres - Finding Missing Indexes
---

# Postgres: Finding Missing Indexes

A bit of serialisation work was underway. Serialisation is changing objects to different representations. In this case a JSON file was being imported into a Postgres database.
From that imported data a materialized view and another table were joined and used to insert into a final `catalogue` table.

This process is called _data loading_ in this case.

There are 4 environments:

* Production
* Pre-production
* Quality Assurance
* Development

These 4 environments all were linked to seperate databases.

During the data load of the development environment - it ran fairly quick. The logs showed each stores catalogue was build in less than 5 seconds.
A strange thing happened when running the _data load_ in the quality assurance (QA) environment:

* The stores would take 5 minutes each to build (as opposed to 5 seconds on Development)
* The CPU usage of the Postgres RDS instance would go up to 60% and sit there while under way.

## Initial Naive Process

The question was asked: 

> "Have you ever experienced a _data load_ going super slow?"

The answer was: bear in mind that the db is a lot less powerful than production and pre-production. This is true, the development database was a `db.t3.medium` while the pre-production RDS instance was a `db.r5.xlarge`.

This was a naive approach....thinking throwing more resources will solve a problem with the approach taken.

This is also proved false - as the development instance is running on the same `db.t3.medium` and experiencing no slowness.

The source of the slowness was not identified or examined.

## Identifying the Problem

In this case identification that there is indeed a problem arose from the fact that a process took 5 seconds in one case and 5 minutes (300 seconds) in another.
That is a **60 times slower**.

How would you identify a problem is there was only a 2 or 3 time factor slower?

* Postgres Analyse
* Postgres Explain

### Cool Tools to Look At

* [pghero](https://github.com/ankane/pghero) - index recommendations
* [hypopg](https://hypopg.readthedocs.io/en/rel1_stable/) - adding hypothetical queries
* [dexter](https://github.com/ankane/dexter) - index recommender

### A Note on Indexes

Why do we add indexes?

To increase read performance - speed up our queries. This comes at the expense of write performance (INSERTS are slower) and indexes take up space on disk and in memory.

> Every index you add to your Postgres database will slow down your write throughput for the table it exists on

A cool thing about Postgres, though, is that it will track all sorts of interesting data on when indexes are used and not.

You always want the database to do less work.

> Using an index typically only makes sense for returning a small fraction of all rows

### Pg_Stat_Statements

`pg_stat_statements` keeps track of the most time consuming queries on your database. Similar to the `slow_query_log` in mysql. However the slo query log functionality in postgres also uses log file and a `log_min_statement_duration` setting.

You need to turn it on though:

    CREATE extension pg_stat_statements;

Then make sure to restart. If you get this when selecting from the `pg_stat_statements` table:

    ERROR:  pg_stat_statements must be loaded via shared_preload_libraries

You need to edit you `postgres.conf` and set:

    shared_preload_libraries = 'pg_stat_statements'

Then check the calls and total time:

    SELECT mean_exec_time, calls, query 
    FROM pg_stat_statements 
    ORDER BY mean_time DESC 
    LIMIT 100;

> The fields change for different version. The above works for postgres 12.

[An explanation of the `pg_stat_statements` fields](https://www.postgresql.org/docs/current/pgstatstatements.html)

* A average execution time of 0.5 ms - means the query executes very quickly. Adding an index will not help here. Probably best to reduce the number of calls.
* An average time of 100ms (with less calls) - a good candidate for an index.

To disable `pg_stat_statements`:

    DROP EXTENSION IF EXISTS pg_stat_statements;

### Checking Indexes

To check whether an index is used on a specific query you run, use:

A [Postgres Explain](https://www.postgresql.org/docs/current/sql-explain.html) - which shows the query place. See [using EXPLAIN](https://www.postgresql.org/docs/9.6/using-explain.html):

    EXPLAIN SELECT * FROM foo;

There are 4 types of scans in postgres:

* Sequential scan: not using index
* Index scan: Searches on index then table
* Index only scan: searches on index only
* bitmap heap scan

To check the indexes on a table:

    SELECT * FROM pg_indexes WHERE tablename = 'table_name';

Or view all indexes and extra info (disk space needed for the index):

    my_db_=> \di+

                                                                    List of relations
 Schema |                              Name                               | Type  |  Owner   |       Table       | Persistence |    Size    | Description 
--------+-----------------------------------------------------------------+-------+----------+-------------------+-------------+------------+-------------
 public | table_name_x_y_z_idx | index | postgres | latest_price_view | permanent   | 9816 kB    | 

See a list of indexes sorted by size and if they are unused:

    SELECT
    schemaname || '.' || relname AS table,
    indexrelname AS index,
    pg_size_pretty(pg_relation_size(i.indexrelid)) AS index_size,
    idx_scan as index_scans
    FROM pg_stat_user_indexes ui
    JOIN pg_index i ON ui.indexrelid = i.indexrelid
    WHERE NOT indisunique AND idx_scan < 50 AND pg_relation_size(relid) > 5 * 8192
    ORDER BY pg_relation_size(i.indexrelid) / nullif(idx_scan, 0) DESC NULLS FIRST,
    pg_relation_size(i.indexrelid) DESC;

Another [query to find unused indexes](https://gist.github.com/jberkus/6b1bcaf7724dfc2a54f3)...make sure to run it on read replicas as well.

### Sequential Scans vs Index Scans

Another good query to use is:

    SELECT pg_stat_user_tables.schemaname,
    pg_stat_user_tables.relname,
    pg_stat_user_tables.seq_scan,
    pg_stat_user_tables.seq_tup_read,
    pg_stat_user_tables.idx_scan,
    pg_stat_user_tables.idx_tup_fetch
    FROM pg_stat_user_tables;

If the `seq_scan` is high but `idx_scan` is low - it indicates the potential need for an index.

## Inconsistency Between Environments

Inconsistency between the environments is a problem.
Perhaps a good problem as comparing the speed of the _data load_ on different environments allowed us to realise that there is a problem.

However, using a migration tool to keep schema changes would ensure and gaurantee the consistency between the environments.

See [sqlalchemy alembic](https://alembic.sqlalchemy.org/en/latest/) and [django migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/).

## Examining the Root Cause

## Adding an Index to a Production Table

Here may be dragons.

Sometimes adding an INDEX to a database - locks the entire table for the duration of the index build.
Depending on the size of the table this can cause data loss and failures.

Postgres has a handy options that enables the _concurrent_ building of indexes without locking up the database.
This is called `online` mode in some other database systems.

    CREATE INDEX CONCURRENTLY idx_my_table_x_y ON public.my_table USING btree (x, y, z)

[Create Index Concurrently was added in postgres 8.2](https://www.postgresql.org/docs/9.1/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY)

The advantages: no downtime and dataloss.
The disadvantages: the index build will take several times longer, Extra CPU and I/O load is imposed, it must wait for existing transactions to complete.

## How to Test and Verify that the Speed has Increased

?

### When to Create an Index

As an aside, it is worth noting that if you are loading data into a fresh table. It is more efficient to load the data first and then create the index.

> Index updates during inserts are expensive.

## Sources

* [List Columns with Indexes Postgresql](https://stackoverflow.com/questions/2204058/list-columns-with-indexes-in-postgresql)
* [Indexing Large Database Tables](https://semaphoreci.com/blog/2017/06/21/faster-rails-indexing-large-database-tables.html)
* [Most Efficient Way to Create an Index in Postgres](https://stackoverflow.com/questions/18580448/most-efficient-way-to-create-an-index-in-postgres)
* [Citus data: Index all the things in postgres](https://www.citusdata.com/blog/2017/10/11/index-all-the-things-in-postgres/)
* [Video: How Postgres could Index Itself](https://www.youtube.com/watch?v=Mni_1yTaNbE)
* [More on Postgres Performance](https://www.craigkerstiens.com/2013/01/10/more-on-postgres-performance/)
* [How do I know if any index is used in a query](https://stackoverflow.com/questions/53662948/how-do-i-know-if-any-index-is-used-in-a-query-postgresql-11)
* [New Finding Unused Indexes Query ](https://www.databasesoup.com/2014/05/new-finding-unused-indexes-query.html)
* [How to find which tables require a postgres index?](https://www.postgresql.org/message-id/CAA8OQ6_Sk7MFDNt5O4QpfYSovqhD8bbZikQmLv8L0Avaa=OkLQ@mail.gmail.com)
