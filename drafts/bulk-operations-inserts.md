---
author: ''
category: sqlalchemy
date: '2022-12-01'
summary: ''
title: Sqlalchemy - Performance Inserting Records
---


There is a project where there needs to be some processing then a inserting of a few million records.

The constraints are an RDS instance t3.medium....

* [sqlalchemy peristence techniques bulk operations](https://docs.sqlalchemy.org/en/14/orm/persistence_techniques.html#bulk-operations)
* [sqlalchemy profiling and adding 400k records really slow](https://docs.sqlalchemy.org/en/13/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow)



[stackoverflow: reduce memory usage of bulk insert](https://stackoverflow.com/questions/61964803/how-to-reduce-the-memory-usage-in-bulk-insert)


[patshaughnessy: is your postgres starved for memory](https://patshaughnessy.net/2016/1/22/is-your-postgres-query-starved-for-memory)

[cybertec-postgresql: postgres bulk loading large amounts of data](https://www.cybertec-postgresql.com/en/postgresql-bulk-loading-huge-amounts-of-data/)

[stackoverlow: large postgresqlt transaction runs out of memory](https://stackoverflow.com/questions/6238404/large-sql-transaction-runs-out-of-memory-on-postgresql-yet-works-on-sql-server)

