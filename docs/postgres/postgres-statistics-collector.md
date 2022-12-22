---
author: ''
category: postgres
date: '2022-12-01'
summary: ''
title: Postgresql - Statistics Collector
---

# Postgres Statistics Collector

As always - use the [source postgres docs](https://www.postgresql.org/docs/14/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW) over these notes.

## View all available Stat Views

    SELECT viewname
    FROM pg_views
    WHERE viewname LIKE 'pg_stat%';

## Check when last stats were reset

    SELECT * FROM pg_stat_database;

## Reset All Stat Counters

    SELECT pg_stat_reset();

> Resets all statistics counters for the current database to zero

This needs to be run on each database you are connected to. The same as enabling extensions.

### Reset PG_STAT_STATEMENT

pg_stat_statement is part of an extensions/module and not pg core.

If `pg_stat_statement` is enabled:

    CREATE extension pg_stat_statements;

Stats can be refreshed with:

    select pg_stat_statements_reset();

### Dynamic Statistics Views

Instantaneous views

    -- current activity - active connections, queries being run, ip addresses
    SELECT * FROM pg_stat_activity;

    -- replications to connected standby server
    SELECT * FROM pg_stat_replication;

    -- WAL receiver from that receiver's connected server (does not work)
    SELECT * FROM pg_stat_wal_receiver;

    -- information about the subscription workers (no records)
    SELECT * FROM pg_stat_subscription;

    -- information about SSL used on this connection
    SELECT * FROM pg_stat_ssl;

    -- information about GSSAPI authentication and encryption used on this connection
    SELECT * FROM pg_stat_gssapi;

    -- backends running ANALYZE, showing current progress
    SELECT * FROM pg_stat_progress_analyze;

    -- backends running CREATE INDEX or REINDEX, showing current progress
    SELECT * FROM pg_stat_progress_create_index;

    -- current progress of vacuums
    SELECT * FROM pg_stat_progress_vacuum;

    -- CLUSTER or VACUUM FULL progress
    SELECT * FROM pg_stat_progress_cluster;

    -- WAL sender process streaming a base backup
    SELECT * FROM pg_stat_progress_basebackup;

    -- Running COPY progress
    SELECT * FROM pg_stat_progress_copy;

## Collected Statistics Views

    -- WAL archiver process's activity
    SELECT * FROM pg_stat_archiver;

    -- background writer process's activity
    SELECT * FROM pg_stat_bgwriter;

    -- WAL Activity
    SELECT * FROM pg_stat_wal;
    -- ERROR:  Function pg_stat_get_wal() is currently not supported for Aurora

    -- database-wide statistics - last stats reset, number of tuples inserter, read etc
    SELECT * FROM pg_stat_database;

    -- query cancels due to conflict with recovery on standby servers
    SELECT * FROM pg_stat_database_conflicts;

    -- one row of stats per table in the cluster - all tables shown
    SELECT * FROM pg_stat_all_tables ORDER BY seq_tup_read DESC;

    -- only system tables are shown
    SELECT * FROM pg_stat_sys_tables;

    -- Only user tables shown
    SELECT * FROM pg_stat_user_tables ORDER BY n_dead_tup DESC;

    -- counts actions taken so far within the current transaction
    -- pg_stat_xact_sys_tables
    -- pg_stat_xact_user_tables
    SELECT * FROM pg_stat_xact_all_tables;

    -- showing statistics about accesses to that specific index
    -- pg_stat_sys_indexes
    -- pg_stat_user_indexes
    SELECT * FROM pg_stat_all_indexes;


    -- showing statistics about I/O on that specific index
    -- pg_statio_sys_indexes
    -- pg_statio_user_indexes
    SELECT * FROM pg_statio_all_indexes ORDER BY idx_blks_read DESC;

    -- showing statistics about I/O on that specific table
    -- pg_statio_sys_tables
    -- pg_statio_user_tables
    SELECT * FROM pg_statio_all_tables

    --  showing statistics about I/O on that specific sequence
    -- pg_statio_sys_sequences
    -- pg_statio_user_sequences
    SELECT * FROM pg_statio_all_sequences;

    -- statistics about executions of that function
    SELECT * FROM pg_stat_user_functions;

    -- statistics about functions in transactions
    SELECT * FROM pg_stat_xact_user_functions;

    -- stats about simple least-recently-used
    SELECT * FROM pg_stat_slru;

    -- stats about the replication slot's usage
    SELECT * FROM pg_stat_replication_slots;

## PG_Locks

[`pg_locks` view][https://www.postgresql.org/docs/current/view-pg-locks.html]

    SELECT * FROM pg_locks;

> pg_locks contains one row per active lockable object, requested lock mode, and relevant process

## Sources

* [Postgres Docs: Monitoring Stats Collector](https://www.postgresql.org/docs/14/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW)
* [Postgres Docs: pg_stat_statements](https://www.postgresql.org/docs/14/pgstatstatements.html)
