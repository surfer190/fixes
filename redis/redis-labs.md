# Redis

Remote Dictionary Server

Database for the instant experience

In memory open source database

Redis Enterprise is the product - backups, replication and clustering.

Redis is for ephemeral data 

Data structures:
* Strings
* Bitmaps
* Hashes
* Lists
* Sets
* Sorted Sets
* Geospacial Data, etc
* Hyperloglog
* Streams

Redis does not let you nest data easily - the reason is speed - reduces performance.
Rational choices made.

Twitter: 0.5 - 1 PB 
booking.com: 10 - 20TB
Snapchat: 40TB

* Written in C 
* Data entitely served from memory - no buffering
* Single-threaded and lock free

## Testing

Linear scaling

1 node 5.3M ops per second
40 nodes 201M ops per second

## Redis Data Structures

### Use Cases

* Cache
* Message brokers/queues
* User sessions
* Real-time recommendations
* Leaderboards

#### Strings: simple cache

db overload or bad respense tme - strings are perfect for this.
These commands below only work with strings.

    SET 
    GET 

strings are byte-safe your data will not be corrupted by redis - store images etc.

* All keys have an expiry - very useful for caching
* Register to listen for changes on keys and operations - pubsub (no persistence)

It is good practice to use a `:` to namespace keys

    SET keyname value

    SET userid:1 "8754"
    OK

Response will be `OK`

    GET keyname
    GET userid:1
    "8754"

Expiring keys

    EXPIRE keyname seconds
    EXPIRE userid:1 60

Delete a key

`UNLINK`

    UNLINK keyname
    UNLINK userid:1

UNLINK will asynchronously reclaim memory - from moment you send the command the key will not be available
DEL will stop server for brief amount of time and reclaim the memory

`EXPIRE`

    EXPIRE foo 10

Will have access afterwards gone

eviction?

#### Hashes: user sessions

Hashes - hash maps. Essentially dictionaries.

You cannot nest values

Problem:
* Maintain session state across multiple sessions
* Mulitple session variables
* Want sticky state
* High speed and low latency

State must be saved on redis not on the application

eCommerce good - show cart state on every page

* `HSET` to save session variables as key/value pairs
* `HMGET` to retrieve values
* `HINCRBY` - incremeent any field in hash structure

Same user logged in from different devices might have seperate user session

    HSET keyname field value field value field value
    
    HSET usrses:1 userid 8754 name Dave ip 10.20.104.31 hits 1
    4 # number of fields

Get the dictionary

    HMGET usrses:1

Change a field value

    HSET keyname field value
    HSET usrses:1 lastpage homepage

Delete

    HDEL keyname field
    HDEL usrses:1 lastpage

Increment a numeric field in a hash

    HINCBY keyname field value
    HINCBY usrses:1 hits 1

Example:

    127.0.0.1:6379> HSET usersess:02 userid 8675309 firstname John lastname Smith ip 127.0.0.1 lastvisit "home"
    (integer) 5
    127.0.0.1:6379> HGETALL usersess:02
    1) "userid"
    2) "8675309"
    3) "firstname"
    4) "John"
    5) "lastname"
    6) "Smith"
    7) "ip"
    8) "127.0.0.1"
    9) "lastvisit"
    10) "home"
    127.0.0.1:6379> HINCRBY usersess:02 hits 1
    (integer) 1
    127.0.0.1:6379> HMGET userid firstname hits
    1) (nil)
    2) (nil)
    127.0.0.1:6379> HMGET usersess:02 userid firstname hits
    1) "8675309"
    2) "John"
    3) "1"
    127.0.0.1:6379> HSET usersess:02 ip 198.1.1.0
    (integer) 0
    127.0.0.1:6379> HMGET usersess:02 ip
    1) "198.1.1.0"
    127.0.0.1:6379> HDEL usersess:02 lastname
    (integer) 1

### Lists: Message Queues

Problem:
* Tasks need to be worked on asynchronously to reduce block/wait times
* Lots of times to be worked on
* Assign items to worker process and remove from queue at the same time
* Buffering high speed data-ingestion


Lists in redis are linked lists: O(1)

LPUSH: push item from left end of queue
RPUSH: push add values at the right of the queue
RPOPLPUSH: pops an item on one queue and pushes it on the left side of another - either in one of the lists even during failures

    LPUSH key value
    LPUSH queue 1 orange

    RPUSH queue1 green
    
    RPOPLPUSH key key
    RPOPLPUSH queue1 queue2

    LPOP key
    LPOP Foo

    127.0.0.1:6379> lpush pizzas margherita mrinara capricciosa
    (integer) 3
    127.0.0.1:6379> rpoplpush pizzas processing
    "margherita"
    127.0.0.1:6379> lrange pizzas 0 3
    1) "capricciosa"
    2) "mrinara"
    127.0.0.1:6379> lrange processing 0 3
    1) "margherita"
    127.0.0.1:6379> lpop processing
    "margherita"
    127.0.0.1:6379> lrange processing 0 3
    (empty list or set)

Better to do it atomicaly

### Sets: Real-time recommendation engine

> People that read this article also like

* Recommend similar purchases
* Identify fraud

`SETS` are unique collections of strings
`SADD` add tags to articke
`SISMEMBER` check an article has a given tag

    SET key member member member 
    SET colours orange blue white red green

Create a set

    SADD tag1 one two three

Find members of a set

    SMEMBERS tag3

Intersection of all sets

    SINTER tag1 tag2 tag3

Example:

    127.0.0.1:6379> SADD colors:all red orange yellow green blue indigo violet
    (integer) 7
    127.0.0.1:6379> SADD colors:friends yellow pink
    (integer) 2
    127.0.0.1:6379> SADD colors:myfavs blue black red
    (integer) 3
    127.0.0.1:6379> SINTER colors:all colors:friends colors:myfavs
    (empty list or set)
    127.0.0.1:6379> SINTER colors:all colors:friends
    1) "yellow"
    127.0.0.1:6379> SINTER colors:all colors:myfavs
    1) "red"
    2) "blue"

Also can get the union with:

    127.0.0.1:6379> SUNION color:myfavs colors:friends
    1) "yellow"
    2) "pink"

### Sorted Sets: Game Leaderboards

Problem:
* Many users playing a game collect points
* Display a real-time leaderboard
* Who is your nearest competition
* Dask-based bd is too slow

Sorted list automatically keeps list of users sorted by score

Add to a sorted set

    ZADD key score member score member
    ZADD game:1 10000 id:2 21000 id:1

> Score must be a number - needs to be sorted

Increment member

    ZINCRBY key incremeber member
    ZINCRBY game:1 10000 id:3

Get a range

    ZREVRANGE key start stop
    ZREVRANGE game:1 0 0

    127.0.0.1:6379> ZADD members:1 22 sw 26 cw 53 eh 32 ch 28 sh
    (integer) 5
    127.0.0.1:6379> ZREVRANGE members:1 0 0
    1) "eh"
    127.0.0.1:6379> ZREVRANGE members:1 4 4
    1) "sw"
    127.0.0.1:6379> ZREVRANGE members:1 -1 -1
    1) "sw"
    127.0.0.1:6379> ZRANGE members:1 0 0 WITHSCORES
    1) "sw"
    2) "22"

### GeoSet: Search By Location

Give me all the pharmacies in a 2km radius

Behind the scenes geosets are sorted sets that you can intersect with another set

> How far am I from the hospital?

GEORADIUS 

#### Hyperloglog Datastructure


#### Translating Redis-CLI into your Language

Python

    redisClient.zadd("game:1", 10000, "id:1")

#### Complexity

Redis will give you the big O notation

### Redis Modules

Extensions to redis

* JSON
* RedisAI
* Search
* Graph
* RedisBloom
* RedisTimeSeries
* RedisGraph

### Persistance

2 persistence mechanism, which aare the same as most other database:
* Snapshots - whole dataset persisted periodically
* Writeahead log - Append only file

You can turn persistence mechanisms off - eg. cache

### Clients

* [redis-py](https://github.com/andymccurdy/redis-py)

Redis will return a byte-string, you can specify `decode_responses=True` to not get byte strings back.

    redis = Redis(host=os.environ.get("REDIS_HOST", "localhost"),
                port=os.environ.get("REDIS_PORT", 6379),
                db=0, decode_responses=True)
              
however that will break images stored as string

### Manage Distributed State

Redis Streams - Data processing pipeline and are time directed.






### Sources

* [Redis.io](https://redis.io/documentation)



## Why Redis?

IoT, eCommerce, Personalizaton, Search...

Telecoms Billing: CDR's and SDR's





### Connect

Start the redis CLI

    redis-cli

Quoting to set values to a specific key, you need to use quoting when value has spaces

    SET somekey "this is a test"

