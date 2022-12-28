---
author: ''
category: postgres
date: '2022-12-12'
summary: ''
title: Postgres - DBA Tasks
---

# Postgres Database Administrator Tasks

## Finding Unused Indexes

To find indexes that were not scanned or fetched since the last time the statistics were reset:

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
        AND idx_scan = 0
        AND idx_tup_read = 0
        AND idx_tup_fetch = 0
    ORDER BY
        pg_relation_size(indexrelname::regclass) DESC;

It is good to reset the statistics when you are done:

    -- Find table oid by name
    SELECT oid FROM pg_class c WHERE relname = 'table_name';
    -- Reset counts for all indexes of table
    SELECT pg_stat_reset_single_table_counters(14662536);

    ?

## Index and Table Bloat

> When you update rows in a table, PostgreSQL marks the tuple as dead and adds the updated tuple in the next available space.

Methods of checking bloat:

* [Postgres wiki: Show database bloat](https://wiki.postgresql.org/wiki/Show_database_bloat)
* [Github: postgres table bloat estimation](https://github.com/ioguix/pgsql-bloat-estimation/blob/master/table/table_bloat.sql)
* [Github: Btree bloat](https://github.com/ioguix/pgsql-bloat-estimation/blob/master/btree/btree_bloat.sql)

### Clearing Bloat in Indexes

1. Recreate the index
2. Rebuild the index (instead of dropping and recreating yourself), this will obtain a lock on the table and prevent it from being changed while the operation is in progress.

    REINDEX INDEX index_name;

3. Rebuild the index concurrently (without locking):

    REINDEX INDEX CONCURRENTLY index_name;

> When using REINDEX CONCURRENTLY, PostgreSQL creates a new index with a name suffixed with `_ccnew`

Invalid indexes can be found with:

    SELECT
        c.relname as index_name,
        pg_size_pretty(pg_relation_size(c.oid))
    FROM
        pg_index i
        JOIN pg_class c ON i.indexrelid = c.oid
    WHERE
        -- New index built using REINDEX CONCURRENTLY
        c.relname LIKE  '%_ccnew'
        -- In INVALID state
        AND NOT indisvalid
    LIMIT 10;

### Index De-duplication

In PostgreSQL 13 index deduplication in enabled by default.

If you are migrating from PostgreSQL versions prior to 13, you need to rebuild the indexes using the REINDEX command in order to get the full benefits of index de-deduplication.

### Clearing Bloat in Tables

Ways:

1. Re-create the table
2. Vacuum the table (`VACUUM FULL <table_name>`) - Vacuum full requires a lock on the table, and is not an ideal solution for tables that need to be available while being vacuumed
3. Using `pg_repack` - an extension.

        CREATE EXTENSION pg_repack;
    
    To repack a table with indexes:

        pg_repack -k --table table_name db_name

### Postgres Indexes and Nulls

In postgresql NULL values are indexes

Better to index on values that are not NULL:

Initially:

    CREATE INDEX transaction_cancelled_by_ix ON transactions(cancelled_by_user_id);

To fix:

    DROP INDEX transaction_cancelled_by_ix;

    CREATE INDEX transaction_cancelled_by_part_ix ON transactions(cancelled_by_user_id)
    WHERE cancelled_by_user_id IS NOT NULL;

### Utilizing Partial Indexes

Finding good candiates for indexes with a high amount of `NULL` values:

    SELECT
        c.oid,
        c.relname AS index,
        pg_size_pretty(pg_relation_size(c.oid)) AS index_size,
        i.indisunique AS unique,
        a.attname AS indexed_column,
        CASE s.null_frac
            WHEN 0 THEN ''
            ELSE to_char(s.null_frac * 100, '999.00%')
        END AS null_frac,
        pg_size_pretty((pg_relation_size(c.oid) * s.null_frac)::bigint) AS expected_saving
        -- Uncomment to include the index definition
        --, ixs.indexdef
    FROM
        pg_class c
        JOIN pg_index i ON i.indexrelid = c.oid
        JOIN pg_attribute a ON a.attrelid = c.oid
        JOIN pg_class c_table ON c_table.oid = i.indrelid
        JOIN pg_indexes ixs ON c.relname = ixs.indexname
        LEFT JOIN pg_stats s ON s.tablename = c_table.relname AND a.attname = s.attname
    WHERE
        -- Primary key cannot be partial
        NOT i.indisprimary

        -- Exclude already partial indexes
        AND i.indpred IS NULL

        -- Exclude composite indexes
        AND array_length(i.indkey, 1) = 1

        -- Larger than 10MB
        AND pg_relation_size(c.oid) > 10 * 1024 ^ 2

    ORDER BY
        pg_relation_size(c.oid) * s.null_frac DESC;


* `tx_cancelled_by_ix` is a large index with many null values: great potential here!
* `tx_op_1_ix` is a large index with few null values: there's not much potential
* `tx_token_ix` is a small index with few null values: I wouldn't bother with this index
* `tx_op_name_ix` is a large index with no null values: nothing to do here

Indexes are also dropped from replications.
When you release 10GB from your primary database, you also release roughly the same amount of storage from each replica.

## Check dead tuples

    select n_live_tup, n_dead_tup, relname from pg_stat_all_tables;

## Killing Postgres Sessions

    SELECT pg_cancel_backend(pid) FROM pg_stat_activity WHERE state = 'active' and pid <> pg_backend_pid();

or:

    SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state = 'active' and pid <> pg_backend_pid();

## Sources

* [Hakibenita: Unused Indexes](https://hakibenita.com/postgresql-unused-index-size)
* [Killing postgres sessions](https://www.sqlprostudio.com/blog/8-killing-cancelling-a-long-running-postgres-query)