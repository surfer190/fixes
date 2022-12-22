---
author: ''
category: postgres
date: '2022-12-11'
summary: ''
title: Extension Must be Loaded via Shared Preload Libraries
---

## Pg_stat_statements Must be Loaded via Shared Preload Libraries

Recently wanted to `SELECT` some stats from the `pg_stat_statements` extension and received this:

    postgres=# SELECT * FROM pg_stat_statements LIMIT 1;
    ERROR:  pg_stat_statements must be loaded via shared_preload_libraries

The extension was activated with:

    CREATE EXTENSION pg_stat_statments;

and the extension was visible in psql:

    postgres=> \dx
                                        List of installed extensions
            Name        | Version |   Schema   |                        Description                        
    --------------------+---------+------------+-----------------------------------------------------------
    pg_stat_statements | 1.10    | public     | track execution statistics of all SQL statements executed
    plpgsql            | 1.0     | pg_catalog | PL/pgSQL procedural language
    (2 rows)

However it appears that you must manually edit the configuration to enable that extension.

> On AWS RDS one would not need to do this - `pg_stat_statements` is enabled by default

## The Fix

1. Find where your config file is:

    postgres=# SHOW config_file;
                config_file               
    -----------------------------------------
    /etc/postgresql/15/main/postgresql.conf

2. Edit the config file:

    sudo vim /etc/postgresql/15/main/postgresql.conf

3. Set:

    shared_preload_libraries = 'pg_stat_statements'

4. Restart postgres:

    sudo systemctl restart postgresql@15-main

## Sources

* [DB Stackexchange: PG Stat Statements preload Libraries](https://dba.stackexchange.com/questions/124054/pg-stat-statements-not-found-even-with-shared-preload-libraries-pg-stat-stat)
* [Stackoverflow: pg-stat-statements must be loaded by shared preload](https://stackoverflow.com/questions/28147037/pghero-on-postgresapp-pg-stat-statements-must-be-loaded-via-shared-preload-libra)
