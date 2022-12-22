---
author: ''
category: redis
date: '2022-12-10'
summary: ''
title: Redis Sysadmin Tasks
---

## Check Memory usage

    127.0.0.1:6379> info memory
    # Memory
    used_memory:1030528
    used_memory_human:1006.38K
    used_memory_rss:1241088
    used_memory_rss_human:1.18M
    used_memory_peak:1031952
    used_memory_peak_human:1007.77K
    used_memory_peak_perc:99.86%
    used_memory_overhead:1029976
    used_memory_startup:963376
    used_memory_dataset:552
    used_memory_dataset_perc:0.82%
    total_system_memory:8589934592
    total_system_memory_human:8.00G
    used_memory_lua:37888
    used_memory_lua_human:37.00K
    maxmemory:0
    maxmemory_human:0B
    maxmemory_policy:noeviction
    mem_fragmentation_ratio:1.20
    mem_allocator:libc
    active_defrag_running:0
    lazyfree_pending_objects:0

## Memory stats

    127.0.0.1:6379> memory stats
    1) "peak.allocated"
    2) (integer) 1031952
    3) "total.allocated"
    4) (integer) 1030496
    5) "startup.allocated"
    6) (integer) 963376
    7) "replication.backlog"
    8) (integer) 0
    9) "clients.slaves"
    10) (integer) 0
    11) "clients.normal"
    12) (integer) 66488
    13) "aof.buffer"
    14) (integer) 0
    15) "db.0"
    16) 1) "overhead.hashtable.main"
        2) (integer) 112
        3) "overhead.hashtable.expires"
        4) (integer) 0
    17) "overhead.total"
    18) (integer) 1029976
    19) "keys.count"
    20) (integer) 2
    21) "keys.bytes-per-key"
    22) (integer) 33560
    23) "dataset.bytes"
    24) (integer) 520
    25) "dataset.percentage"
    26) "0.77473181486129761"
    27) "peak.percentage"
    28) "99.858909606933594"
    29) "fragmentation"
    30) "1.1207501888275146"

## Keyspace Info

    127.0.0.1:6379> info keyspace
    # Keyspace
    db0:keys=2,expires=0,avg_ttl=0

## List all keys

    127.0.0.1:6379> KEYS *
    1) "Bahamas"
    2) "Croatia"

## Check size a specific key takes up

    127.0.0.1:6379> MEMORY USAGE Bahamas
    (integer) 57

> Result is in bytes

## Redis benchmark

    redis-benchmark

## Sources

* [Educaba: Redis Memory Usage](https://www.educba.com/redis-memory-usage/)
