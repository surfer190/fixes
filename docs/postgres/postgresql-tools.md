---
author: ''
category: postgres
date: '2022-11-25'
summary: ''
title: Postgres - Cool and Useful Postgresql Tools
---

## Cool and Useful PostgreSQL tools

### Visualisers

* [PEV2 - Postgresql EXPLAIN Visualizer](https://github.com/dalibo/pev2) - a vuejs html file - just put the result of `EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) <your query>` in the input.

### Log Analyser

* [pgbadger](https://github.com/darold/pgbadger) - a perl based command line aggregator of a static log file

### Performance

* [Connection Pooler for PostgreSQL](https://www.pgbouncer.org/) - useful for a large number of connections and load (not response time)
* [pgbench](https://www.postgresql.org/docs/current/pgbench.html) - run a benchmark test on PostgreSQL

### Development

#### Python

* [aiosql](https://github.com/nackjicholson/aiosql) - Using SQL as code (no ORM)

#### Regression Testing

* [Regression testing of SQL code](https://github.com/dimitri/regresql)
