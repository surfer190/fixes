---
author: ''
category: postgres
date: '2022-11-29'
summary: ''
title: The Art of Postgresql
---

# The Art of Postgresql

Postgresql is not about storage, it is about concurrency and isloation.

RDBMS - Relational database management systems - provide ACID gaurantees.

## A - Atomic

* Many actions in a transaction can use a `rollback` to return to the original state
* If the systems runs out of storage, tranasctions will all rollback
* Transactions for DDL's (Data Description Language) - adding columns or index - if filesystem fills before end of script.

## C - Consistenency

* Scheme, data types, constraints, relations
* postgres will error out when trying to do things inconsistent with the schema

> Relations are the central concept of SQL. Relations is a mathemtaical concept - sets that share common properties - attribute domains.

## I - Isolation

* While you do select read queries, while other operations and transactions are happeneing.
* Using `pg_dump` while other people are doing changes - so it typically uses an isolation mode. This is called `repeatable read` isolation. The default is `read commited`. More on [postgres isolation](./transaction-isolation.md).
* Isolation is hard to implement at the application level

## D - Durable

* Write a client to do inserts, check the commits on the client. Then check commits on server. Pull the plug out of the system intermittently. If there is a mismatch in counts of commits - then there is no durability.

### PostgreSQL for Developers

* Transactions - means compliance with ACID
* SQL
* Object oriented
* Extensions
* Rich Data types
* Data processing
* Advanced Indexing
* Arrays, XML and JSON

> Some systems are calling themselves databases - NoSQL systems, but they are not databases. They are not ACID compliant.

### How do you know what postgresql is doing?

Use `EXPLAIN`.

The favourite version from the author is `explain (analyse, verbose, buffers)`:

* The most information
* `analyse` will run the query

## Sources

* [Youtube: PostgresOpen 2019 The Art Of PostgreSQL](https://www.youtube.com/watch?v=q9IXCdy_mtY)
