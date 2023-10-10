---
author: ''
category: Postgres
date: '2023-02-10'
summary: ''
title: DBA General Health Tasks
---

# Postgres DBA General Health Tasks

## Set a statement timeout

Long running queries should be offloaded to other systems or read replicas. Transactional systems should have queries finishing execution within milliseconds.

Check the existing setting:

    psql
    \c <my_db>
    show statement_timeout;
    show idle_in_transaction_session_timeout;

Set the max:

    ALTER DATABASE <my_db> SET statement_timeout = '60s';
    ALTER DATABASE <my_db> SET idle_in_transaction_session_timeout = '600s';

## Query stats

Enable `pg_stat_statements`:

    CREATE extension pg_stat_statements;

> On all environments - especially production.

## Log slow running queries

    psql
    \c <my_db>
    show log_min_duration_statement;

Change the setting:

    ALTER DATABASE <my_db> SET log_min_duration_statement = '500ms';
    
> Can be set globally in `postgres.conf`

This will only log queries 500ms or slower

    log_statement = none
    log_min_duration_statement = 500
    
## Consider Server Side Connection pooling

Check:

    SELECT count(*),
        state
    FROM pg_stat_activity
    GROUP BY 2;

> Consider pgBouncer

## Cancel or terminate a session

    SELECT pg_cancel_backend(<pid>);

    SELECT pg_terminate_backend(<pid>);

### Source

* [Five Tips For a Healthier Postgres Database](https://www.crunchydata.com/blog/five-tips-for-a-healthier-postgres-database-in-the-new-year)
* [postgresqlco.nf: Idle in transaction](https://postgresqlco.nf/doc/en/param/idle_in_transaction_session_timeout/)
* [postgresqlco.nf: Statement timeout](https://postgresqlco.nf/doc/en/param/statement_timeout/)
* [postgresqlco.nf: Log min duration statement](https://postgresqlco.nf/doc/en/param/log_min_duration_statement/)
