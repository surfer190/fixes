---
author: ''
category: postgres
date: '2022-12-14'
summary: ''
title: Pgbench
---

## Create the test db

    sudo su postgres
    psql
    CREATE DATABASE pgbench_test;

## Initialise the tables

    pgbench -p 5432 -i pgbench_test

> Can scale it with `-s` but that will have storage requirements

    pgbench -U postgres -p 5432 -i -s 50 pgbench_test

## Establish a baseline

Set:

* Number of clients
* Number of threads
* Number of transactions

    pgbench -p 5432 -c 10 -j 2 -t 10000 pgbench_test

### Setting over max clients

Will blow up with too many clients set:

    postgres@web:/home/staging$ pgbench -p 5432 -c 100 -j 4 -t 100 pgbench_test
    pgbench (15.1 (Ubuntu 15.1-1.pgdg20.04+1))
    starting vacuum...end.
    pgbench: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  sorry, too many clients already

### Example results

Postgres direct:

    postgres@web:/home/staging$ pgbench -p 5432 -c 50 -j 4 -t 100 pgbench_test
    pgbench (15.1 (Ubuntu 15.1-1.pgdg20.04+1))
    starting vacuum...end.
    transaction type: <builtin: TPC-B (sort of)>
    scaling factor: 1
    query mode: simple
    number of clients: 50
    number of threads: 4
    maximum number of tries: 1
    number of transactions per client: 100
    number of transactions actually processed: 5000/5000
    number of failed transactions: 0 (0.000%)
    latency average = 65.068 ms
    initial connection time = 53.936 ms
    tps = 768.424869 (without initial connection time)

Postgres via pgbouncer:

    staging@web:~$ pgbench -U local -h 127.0.0.1 -p 6432 -c 50 -j 4 -t 100 pgbench_test
    Password: 
    pgbench (15.1 (Ubuntu 15.1-1.pgdg20.04+1))
    starting vacuum...WARNING:  skipping "pgbench_branches" --- only table or database owner can vacuum it
    WARNING:  skipping "pgbench_tellers" --- only table or database owner can vacuum it
    end.
    transaction type: <builtin: TPC-B (sort of)>
    scaling factor: 1
    query mode: simple
    number of clients: 50
    number of threads: 4
    maximum number of tries: 1
    number of transactions per client: 100
    number of transactions actually processed: 5000/5000
    number of failed transactions: 0 (0.000%)
    latency average = 81.775 ms
    initial connection time = 149.511 ms
    tps = 611.435233 (without initial connection time)

Increasing `max_client_conn = 300` on pgbouncer:

    staging@web:~$ pgbench -U local -h 127.0.0.1 -p 6432 -c 100 -j 4 -t 100 pgbench_test
    Password: 
    pgbench (15.1 (Ubuntu 15.1-1.pgdg20.04+1))
    starting vacuum...WARNING:  skipping "pgbench_branches" --- only table or database owner can vacuum it
    WARNING:  skipping "pgbench_tellers" --- only table or database owner can vacuum it
    end.
    transaction type: <builtin: TPC-B (sort of)>
    scaling factor: 1
    query mode: simple
    number of clients: 100
    number of threads: 4
    maximum number of tries: 1
    number of transactions per client: 100
    number of transactions actually processed: 10000/10000
    number of failed transactions: 0 (0.000%)
    latency average = 187.221 ms
    initial connection time = 284.280 ms
    tps = 534.126975 (without initial connection time)

## Sources

https://www.dba-ninja.com/2019/11/how-to-use-pgbench-for-postgresql-benchmark-testing.html

https://www.postgresql.org/docs/current/pgbench.html