---
author: ''
category: SQLite
date: '2022-09-01'
summary: ''
title: Fundamentals of SQlite
---

## SQLite

SQLite is a library, providing an in-process relational database for efficient storage of small-to-medium-sized data sets.
It could also be called an embedded SQL database.

SQLite requires zero configuration (or server setup) to get up and running since the SQL logic is run in the host process, and the database consists of only two files you can easily copy or move around.

SQLite is configured by executing special queries of the form `PRAGMA <setting> = <value>`.

### The Toy Database

It is sometimes portrayed as a toy database or one that should never be used in production.

* You can connect to and query the same database concurrently with multiple processes, though only one write operation can happen at the same time.
* You can scale a SQLite database to multiple GByte in size and many concurrent readers while maintaining high performance by applying the below optimizations

### SQLite Quickstart

[sqlite quickstart](https://www.sqlite.org/quickstart.html)

Check the sqlite cli binary is availabe:

    $ sqlite3 -version
    3.40.1 2022-12-28 14:03:47 df5c253c0b3dd24916e4ec7cf77d3db5294cc9fd45ae7b9c5e82ad8197f38a24

Create a test db:

    sqlite3 test.db

> This also puts you into the sqlite3 shell

View help:

    .help

Quit:

    .quit

### Some Commands to Run on Every Connection for High Performance

    pragma journal_mode = WAL;

Journal mode - Instead of writing directly to the file write to the write ahead log that periodically writes back to the file. This allows multiple concurrent readers even during an open write transaction can significantly improve performance.

    pragma synchronous = normal;
    pragma synchronous = off;

Synchronous commit - teh default of `full` means that every update must wait for `FSYNC`. This greatly improves commit performance at the cost of corruption of the db on a crash.

    pragma mmap_size = 30000000000;

Enable memory mapping - Uses memory mapping instead of read/write calls when the database is < mmap_size in bytes. Less syscalls, and pages and caches will be managed by the OS, so the performance of this depends on your operating system.

    pragma page_size = 32768;

Increase the page size - useful for when storing large blobs of data.

### DBA Tasks

Periodic maintenance should be run on the db:

    pragma vacuum;

completely rewrites teh db (removed dead cells)

    pragma optimize;

improve query performance

## Sources

* [SQLite Performance Tuning](https://phiresky.github.io/blog/2020/sqlite-performance-tuning/)
* [SQLite documentation](https://www.sqlite.org/docs.html)
* [SQLite Pragma synchronous](https://www.sqlite.org/pragma.html#pragma_synchronous)
* [SQLite Pragme optimise](https://www.sqlite.org/pragma.html#pragma_optimize)
