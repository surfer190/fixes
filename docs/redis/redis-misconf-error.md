---
author: ''
category: Redis
date: '2022-12-10'
summary: ''
title: Redis - MISCONF Redis is configured to save RDB snapshots
---

Every receive this error?

    127.0.0.1:6379> ping
    (error) MISCONF Redis is configured to save RDB snapshots, but it is currently not able to persist on disk. Commands that may modify the data set are disabled, because this instance is configured to report errors during writes if RDB snapshotting fails (stop-writes-on-bgsave-error option). Please check the Redis logs for details about the RDB error.

Solve with:

    127.0.0.1:6379> config set stop-writes-on-bgsave-error no
    OK

## Source

* [Stackoverflow: misconf redis is configured to save rdb snapshots](https://stackoverflow.com/questions/19581059/misconf-redis-is-configured-to-save-rdb-snapshots)
