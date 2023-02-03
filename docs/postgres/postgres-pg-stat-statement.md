---
author: ''
category: postgres
date: '2022-12-14'
summary: ''
title: Postgres - Querying the pg_stats_statements view
---

    SELECT 
        QUERY,
        CALLS,
        TOTAL_EXEC_TIME,
        MIN_EXEC_TIME,
        MAX_EXEC_TIME,
        MEAN_EXEC_TIME,
        STDDEV_EXEC_TIME,
        ROWS,
        SHARED_BLKS_HIT,
        SHARED_BLKS_READ,
        SHARED_BLKS_DIRTIED,
        SHARED_BLKS_WRITTEN,
        TEMP_BLKS_READ,
        TEMP_BLKS_WRITTEN,
        BLK_READ_TIME
    FROM PG_STAT_STATEMENTS
    ORDER BY CALLS DESC
    LIMIT 100;

Index stats:

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

Find common called with slow exec time:

    SELECT 
        QUERY,
        CALLS,
        TOTAL_EXEC_TIME,
        MIN_EXEC_TIME,
        MAX_EXEC_TIME,
        MEAN_EXEC_TIME,
        STDDEV_EXEC_TIME,
        ROWS,
        SHARED_BLKS_HIT,
        SHARED_BLKS_READ,
        SHARED_BLKS_DIRTIED,
        SHARED_BLKS_WRITTEN,
        TEMP_BLKS_READ,
        TEMP_BLKS_WRITTEN,
        BLK_READ_TIME
    FROM PG_STAT_STATEMENTS
    WHERE calls > 50 AND mean_exec_time > 0.5
    ORDER BY calls DESC
    LIMIT 50;

Analyse queries from a specific database:

    SELECT QUERY,
        CALLS,
        TOTAL_EXEC_TIME,
        MIN_EXEC_TIME,
        MAX_EXEC_TIME,
        MEAN_EXEC_TIME,
        STDDEV_EXEC_TIME,
        ROWS,
        SHARED_BLKS_HIT,
        SHARED_BLKS_READ,
        SHARED_BLKS_DIRTIED,
        SHARED_BLKS_WRITTEN,
        TEMP_BLKS_READ,
        TEMP_BLKS_WRITTEN,
        BLK_READ_TIME
    FROM PG_STAT_STATEMENTS,
        PG_DATABASE
    WHERE PG_DATABASE.OID = PG_STAT_STATEMENTS.DBID
        AND CALLS > 50
        AND DATNAME = '<my_db_name>'
    ORDER BY CALLS DESC;