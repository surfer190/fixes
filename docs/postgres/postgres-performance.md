---
author: ''
category: Postgres
date: '2022-10-25'
summary: ''
title: Postgres Performance
---

# Postgres Performance

> For many application developers their database is a black box

## Understanding your Cache and its Hit Rate

The typical rule for most applications is that only a fraction of its data is regularly accessed.
20% of your data can account for 80% of the reads.

Generally you want your cache hit rate to be at 99%

You can check it with:

    SELECT 
        sum(heap_blks_read) as heap_read,
        sum(heap_blks_hit)  as heap_hit,
        sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio
    FROM 
        pg_statio_user_tables;

> If you find yourself with a ratio significantly lower than 99% then you likely want to consider increasing the cache available to your database, you can do this on Heroku Postgres by performing a fast database changeover or on something like EC2 by performing a dump/restore to a larger instance size.

## Understanding Index Usage

> Several frameworks will add indexes on your primary keys, though if you’re searching on other fields or joining heavily you may need to manually add such indexes.

Indexes are most valuable across large tables as well. While accessing data from cache is faster than disk, even data within memory can be slow if Postgres must parse through hundreds of thousands of rows to identify if they meet a certain condition

To generate a list of tables and the percentage of time they use an index:

    SELECT 
        relname, 
        100 * idx_scan / (seq_scan + idx_scan) percent_of_times_index_used, 
        n_live_tup rows_in_table
    FROM 
        pg_stat_user_tables
    WHERE 
        seq_scan + idx_scan > 0 
    ORDER BY 
        n_live_tup DESC;

> While there is no perfect answer, if you’re not somewhere around 99% on any table over 10,000 rows you may want to consider adding an index

When examining where to add an index you should look at what kind of queries you’re running. Generally you’ll want to add indexes where you’re looking up by some `other id` or on values that you’re commonly **filtering** on such as `created_at` fields.

You can view the execution plan of a query with `EXPLAIN`:

    EXPLAIN ANALYZE SELECT * FROM events WHERE app_info_id = 7559;

    Seq Scan on events  (cost=0.00..63749.03 rows=38 width=688) (actual time=2.538..660.785 rows=89 loops=1)
      Filter: (app_info_id = 7559)
        Total runtime: 660.885 ms

Add the index:

    CREATE INDEX CONCURRENTLY idx_events_app_info_id ON events(app_info_id);

Then check the query plan:

    EXPLAIN ANALYZE SELECT * FROM events WHERE app_info_id = 7559;

    Index Scan using idx_events_app_info_id on events  (cost=0.00..23.40 rows=38 width=688) (actual time=0.021..0.115 rows=89 loops=1)
      Index Cond: (app_info_id = 7559)
        Total runtime: 0.200 ms

You can then check the amount of time spent in the database with a tool like datadog or newrelic.

## Index Cache Hit Rate

To check how much of the indexes are within your cache:

    SELECT 
        sum(idx_blks_read) as idx_read,
        sum(idx_blks_hit)  as idx_hit,
        (sum(idx_blks_hit) - sum(idx_blks_read)) / sum(idx_blks_hit) as ratio
    FROM 
        pg_statio_user_indexes;

> Generally, you should also expect this to be in the 99% similar to your regular cache hit rate.

## PG Stat Statements

Keeps a normalized record of when queries are run

Enable it:

    CREATE extension pg_stat_statements;

Queries are that are similar are recorded in a normalised form.

In postgres > 11 you can run:

    SELECT MEAN_EXEC_TIME, CALLS, QUERY
    FROM PG_STAT_STATEMENTS
    ORDER BY MEAN_EXEC_TIME DESC
    LIMIT 100;

### What to optimize

A query that returns 1 or a small set of records should happen in less than 1ms (better to be less than 5ms)

So find queries and then `EXPLAIN ANALYSE` them.


## Source

* [Understanding Postgres Performance](https://www.craigkerstiens.com/2012/10/01/understanding-postgres-performance/)
* [More on Postgres Performance](https://www.craigkerstiens.com/2013/01/10/more-on-postgres-performance/)
