---
author: ''
category: Python
date: '2022-11-30'
summary: ''
title: Python Redis Cache
---

## Python Redis Cache

Fast in-memory database

> The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker. - [redis official site](https://redis.io/)

Go to python client library: [redis-py](https://github.com/redis/redis-py)

Redis makes a good cache as it has a simple api and is fast.
It is more suitable in containerised workloads as pods can connect to a centralised redis instance to retrieve cache instead of waisting local memory with an in process cache like python's `lru_cache` or `cachetools`.

Expiry can also be set on keys.

### Install from Source

Go to [redis downloads](https://redis.io/download/)

    cd /opt
    sudo wget https://download.redis.io/releases/redis-6.2.7.tar.gz
    sudo tar xzf redis-6.2.7.tar.gz
    cd redis-6.2.7/
    cat README.md
    sudo make
    sudo make install

Confirm redis is on the `$PATH` and the version is right:

    redis-cli --version

Create basic server config:

    # /etc/redis/6379.conf

    port              6379
    daemonize         yes
    save              60 1
    bind              127.0.0.1
    tcp-keepalive     300
    dbfilename        dump.rdb
    dir               ./
    rdbcompression    yes

## Fundamentals

* Redis has a client-server architecture
* uses a request-response model
* Redis stands for **Remote Dictionary Service**
* clients connect to a Redis server through TCP connection, on port 6379 by default
* You request an action: get, set etc. and receive a response
* The cli in `redis-cli` stands for command line interface
* The server in `redis-server` is for running a server

Start the server:

    redis-server /etc/redis/6379.conf

It runs in the background as a daemon

Enter the cli:

    redis-cli

Test connectivity:

    $ redis-cli
    127.0.0.1:6379> PING
    PONG

> redis commands are case sensitive but the python commands/functions are not

Shutdown the service with:

    pgrep redis-server
    pkill redis-server

of

    redis-cli shutdown

### Redis as a Python Dictionary

There are many parrallels between a python dictionary (hash table) and redis:

* Redis database holds key:value pairs and supports commands such as GET, SET, and DEL
* Redis keys are always strings
* Redis values may be a number of different data types: string, list, hashes, sets
* Many Redis commands operate in constant O(1) time, just like retrieving a value from a Python dict or any hash table

### Exercise: Mapping country to Capital

Set and get

    127.0.0.1:6379> SET Bahamas Nassau
    OK
    127.0.0.1:6379>  SET South_Africa Pretoria
    OK
    127.0.0.1:6379> SET Croatia Zagreb
    OK
    127.0.0.1:6379> GET South_Africa
    "Pretoria"
    127.0.0.1:6379> GET Bahamas
    "Nassau"
    127.0.0.1:6379> GET Japan
    (nil)

Set and get multiple

    127.0.0.1:6379> MSET Lebanon Beirut Norway Oslo France Paris
    OK
    127.0.0.1:6379> MGET Lebanon Norway Bahamas
    1) "Beirut"
    2) "Oslo"
    3) "Nassau"

Check existence of key

    127.0.0.1:6379> EXISTS Norway
    (integer) 1
    127.0.0.1:6379> EXISTS Sweden
    (integer) 0

Hash - A hash is a mapping of string:string, called field-value pairs, that sits under one top-level key

    127.0.0.1:6379> HSET fixes.co.za url "https://fixes.co.za/"
    (integer) 1
    127.0.0.1:6379> HSET fixes.co.za github fixes
    (integer) 1
    127.0.0.1:6379> HSET fixes.co.za fullname "fixes"
    (integer) 1
    127.0.0.1:6379> HGETALL fixes.co.za
    1) "url"
    2) "https://fixes.co.za/"
    3) "github"
    4) "fixes"
    5) "fullname"
    6) "fixes"
    127.0.0.1:6379> HMSET pypa url "https://www.pypa.io/" github pypa fullname "Python Packaging Authority"
    OK
    127.0.0.1:6379> HGETALL pypa
    1) "url"
    2) "https://www.pypa.io/"
    3) "github"
    4) "pypa"
    5) "fullname"
    6) "Python Packaging Authority"
    127.0.0.1:6379> HGET fixes.co.za url
    "https://fixes.co.za/"

### Commands

Sets:

`SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP, SRANDMEMBER, SREM, SSCAN, SUNION, SUNIONSTORE`

Hashes:

`HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HLEN, HMGET, HMSET, HSCAN, HSET, HSETNX, HSTRLEN, HVALS`

Lists:

`BLPOP, BRPOP, BRPOPLPUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSH, LPUSHX, LRANGE, LREM, LSET, LTRIM, RPOP, RPOPLPUSH, RPUSH, RPUSHX`

Strings:

`APPEND, BITCOUNT, BITFIELD, BITOP, BITPOS, DECR, DECRBY, GET, GETBIT, GETRANGE, GETSET, INCR, INCRBY, INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN`

### Clearing DB

    127.0.0.1:6379> FLUSHDB
    OK
    127.0.0.1:6379> exit

## Python Redis client library: redis-py

* It encapsulates an actual TCP connection to a Redis server and sends raw commands, as bytes serialized using the REdis Serialization Protocol (RESP), to the server
* It then takes the raw reply and parses it back into a Python object such as bytes, int, or even datetime.datetime.

Install:

    python -m pip install redis

usage:

    >>> import redis
    >>> r = redis.Redis()
    >>> r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    True
    >>> r.get("Bahamas")
    b'Nassau'
    >>> r.get("Bahamas").decode("utf-8")
    'Nassau'

> Note: `bytes` is the common return type so using `r.get("Bahamas").decode("utf-8")` may be required

* Most of the commands look the same: eg. `r.ping()` and `r.hgetall()`
* One thing that’s worth knowing is that redis-py requires that you pass it keys that are `bytes`, `str`, `int`, or `float`.
* Redis itself only allows strings as keys

### Example: Pipelining (Crazy Hats Store)

There is a way to insert many values into the redis db without round trips.
It is called [pipelining](https://redis.io/docs/manual/pipelining/)

    import random

    random.seed(444)
    hats = {f"hat:{random.getrandbits(32)}": i for i in (
        {
            "color": "black",
            "price": 49.99,
            "style": "fitted",
            "quantity": 1000,
            "npurchased": 0,
        },
        {
            "color": "maroon",
            "price": 59.99,
            "style": "hipster",
            "quantity": 500,
            "npurchased": 0,
        },
        {
            "color": "green",
            "price": 99.99,
            "style": "baseball",
            "quantity": 200,
            "npurchased": 0,
        })
    }

    r = redis.Redis(db=1)
    with r.pipeline() as pipe:
        for h_id, hat in hats.items():
            pipe.hmset(h_id, hat)

         pipe.execute()
    r.bgsave()

> Now lets check the keys and see if the data is there

    r.keys()  # Careful on a big DB. keys() is O(N)
    
    pprint(r.hgetall("hat:56854717"))

Check all the keys on redis-cli:

    KEYS *




## Sources

* [Realpython: python-redis](https://realpython.com/python-redis/)
