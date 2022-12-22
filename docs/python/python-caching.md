---
author: ''
category: Python
date: '2022-11-30'
summary: ''
title: Python Caching
---

## Python Caching

Some methods (patterns) of caching and planning decisions have been described by [aws caching best practices](https://aws.amazon.com/caching/best-practices/)

### Deciding on whether to cache data:

* Is it safe to use a cached value? Different contexts hae different requirements - stock level at checkout vs stock level at cart time.
* Is caching effective for the data? sweeping through key space of data that changes frequently - keeping cache up-to-date offsets any advantage caching could offer
* Is the data stuctured well for caching? is data combined and then cached

> Simply caching a database record can often be enough to offer significant performance advantages

> Caches are simple key-value stores

### Methods of Caching

* Lazy caching
* Write-through
* Time-to-live
* Evictions
* The thundering herd

#### Lazy Caching

* Also called lazy population or cache-aside
* populate the cache only when an object is actually requested by the application

Basic flow:

1. Receive request for top 10 items
2. check cache to see if object is in cache
3. if in cache (a cache hit) the object is returned
4. If not in cache (a cache miss) the database is queried from the database, the cache is updated and the object returned

Advantages:

* The cache only contains objects that the application actually requests, which helps keep the cache size manageable - evict only the least accessed keys
* Cache expiration is easily handled by simply deleting the cached object. A new object will be fetched from the database the next time it is requested.
* Lazy caching is widely understood, and many web and app frameworks include support out of the box.

Eg.

    def get_user(user_id):
    
        record = cache.get(user_id)

        if record is None:
            record = db.query("select * from users where id = ?",user_id)
            cache.set(user_id, record)

        return record

    user = get_user(17)

> You should apply a lazy caching strategy anywhere in your app where you have data that is going to be read often, but written infrequently.

#### Write-through

In a write-through cache, the cache is updated in real time when the database is updated.

* proactive to avoid unnecessary cache misses
* good for data that you absolutely know is going to be accessed
*  A good example is any type of aggregate, such as a top 100 game leaderboard, or the top 10 most popular news stories, or even recommendations.

Eg.

    def save_user(user_id, values):
        record = db.query("update users ... where id = ?", user_id, values)

        cache.set(user_id, record)

        return record

    user = save_user(17, {"name": "Nate Dogg"})

Advantages:

* Avoids cache misses
* It simplifies cache expiration. The cache is always up-to-date.

Disadvantages:

* The cache can be filled with unnecessary objects that aren't actually being accessed - Not only could this consume extra memory, but unused items can evict more useful items out of the cache.
* Lots of cache churn if certain records are updated repeatedly.
* When cache nodes fail, those objects will no longer be in the cache. You need some way to repopulate the cache of missing objects, for example by lazy population.

#### Time-to-live

Previous examples, we were only operating on a single user record. In a real app, a given page or screen often caches a whole bunch of different stuff at once.
Cache expiration can get really complex really quickly.

No silver bullet, but a few simple strategies:

* Always apply a time to live (TTL) to all of your cache keys, except those you are updating by write-through caching. You can use a long time, say hours or even days. This approach catches application bugs, where you forget to update or delete a given cache key when updating the underlying record. Eventually, the cache key will auto-expire and get refreshed.
* For rapidly changing data such as comments, leaderboards, or activity streams, rather than adding write-through caching or complex expiration logic, just set a short TTL of a few seconds. If you have a database query that is getting hammered in production, it's just a few lines of code to add a cache key with a 5 second TTL around the query. This code can be a wonderful Band-Aid to keep your application up and running while you evaluate more elegant solutions.
* Russian doll caching, has come out of work done by the Ruby on Rails team. In this pattern, nested records are managed with their own cache keys, and then the top-level resource is a collection of those cache keys. Say you have a news webpage that contains users, stories, and comments. In this approach, each of those is its own cache key, and the page queries each of those keys respectively.
* When in doubt, just delete a cache key if you're not sure whether it's affected by a given database update or not. Your lazy caching foundation will refresh the key when needed. In the meantime, your database will be no worse off than it was without caching.

#### Evictions

* Evictions occur when memory is over filled or greater than maxmemory setting in the cache
* Default elasticache policy selects the least recently used keys that have an expiration (TTL) value set

options:

* allkeys-lfu: The cache evicts the least frequently used (LFU) keys regardless of TTL set
* allkeys-lru: The cache evicts the least recently used (LRU) regardless of TTL set
* volatile-lfu: The cache evicts the least frequently used (LFU) keys from those that have a TTL set
* volatile-lru: The cache evicts the least recently used (LRU) from those that have a TTL set
* volatile-ttl: The cache evicts the keys with shortest TTL set
* volatile-random: The cache randomly evicts keys with a TTL set
* allkeys-random: The cache randomly evicts keys regardless of TTL set
* no-eviction: The cache doesn’t evict keys at all. This blocks future writes until memory frees up.

> if you are experiencing evictions with your cluster, it is usually a sign that you need to scale up (use a node that has a larger memory footprint) or scale out (add additional nodes to the cluster) in order to accommodate the additional data

#### The thundering herd

* When many different application processes simultaneously request a cache key, get a cache miss, and then each hits the same database query in parallel
* The more expensive this query is, the bigger impact it has on the database.
* Problem with TTLs - a popular persons cache will still be evicted

When adding a new cache node you want to pre warm:

1. Write a script that performs the same requests that your application will
2. If your app is set up for lazy caching, cache misses will result in cache keys being populated, and the new cache node will fill up.
3. When you add new cache nodes, run your script before you attach the new node to your application. Because your application needs to be reconfigured to add a new node to the consistent hashing ring, insert this script as a step before triggering the app reconfiguration.

> If you use the same TTL length (say 60 minutes) consistently, then many of your cache keys might expire within the same time window, even after prewarming your cache.

### Caching in Practice

> In practice, in-memory caching is widely useful, because it is much faster to retrieve a flat cache key from memory than to perform even the most highly optimized database query or remote API call.

In-memory cache allow:

* speed - querying is fast to a key-value store, in-memory not disk
* simplicity

> Popular technologies that are used for caching like Memcached and Redis will automatically evict the less frequently used cache keys to free up memory if you set an eviction policy.

### Where does the Cache Live

If you have many pods - a write-through cache will only work is the cache lives outside of the pod.

Popular in-memory caches:

* memcached
* redis

### What Flask says about Caching

What does a cache do? Say you have a function that takes some time to complete but the results would still be good enough if they were 5 minutes old. So then the idea is that you actually put the result of that calculation into a cache for some time.

Then a link to [flask-caching](https://flask-caching.readthedocs.io/en/latest/) is given and they dive straight in...no discussion of concepts or overview.

### What Django says about Caching

> A fundamental trade-off in dynamic websites is, well, they’re dynamic

* Each time a user requests a page, the web server makes all sorts of calculations – from database queries to template rendering to business logic – to create the page that your site’s visitor sees.
* This is a lot more expensive, from a processing-overhead perspective, than your standard read-a-file-off-the-filesystem server arrangement (like a standard html file)
* For most web applications, this overhead isn’t a big deal.
* For high-traffic sites, it’s essential to cut as much overhead as possible.

> To cache something is to save the result of an expensive calculation so that you don’t have to perform the calculation next time.

Pseudocode example:

    given a URL, try finding that page in the cache
    if the page is in the cache:
        return the cached page
    else:
        generate the page
        save the generated page in the cache (for next time)
        return the generated page

Django comes with a robust cache system that lets you save dynamic pages so they don’t have to be calculated for each request.

Different levels of cache granularity:

* cache output of specific views
* cache only the pieces that are difficult to produce
* cache your entire site

Django also works well with “downstream” caches, such as [Squid](http://www.squid-cache.org/) and browser-based caches.
These are caches you don't directly control but can give hints via HTTP headers.

The [django cache framework design philosophy](https://docs.djangoproject.com/en/4.1/misc/design-philosophies/#cache-design-philosophy):

* Less code - to keep fast as possible
* Consistency - consistent api across cache backends
* Extensibility - extensible at application level

More info in [django docs: setting up the cache](https://docs.djangoproject.com/en/4.1/topics/cache/#setting-up-the-cache)

## All the tools

### The core

> Core tools used for caching

* [Squid](http://www.squid-cache.org/) - web caching proxy
* [Memcached](https://memcached.org) - Free & open source distributed memory object caching system
* [Redis](https://redis.io/) - The open source, in-memory data store

### The bindings

> A binding is a language specific API or SDK for a tool - not 100% on this

* [pymemcache](https://pypi.org/project/pymemcache/) - memcached python binding
* [pylibmc](https://pypi.org/project/pylibmc/) - memcached python binding
* [redis-py](https://pypi.org/project/redis/) - redis python binding
* [hiredis](https://pypi.org/project/hiredis/) - speeds up bulk parsing

### Python

* [Cachetools](https://cachetools.readthedocs.io/en/latest/) - Extensible memoizing collections and decorators. Variants of standard libraries `@lru_cache`
* [Python standard lib: functools cache](https://docs.python.org/3/library/functools.html)
* [ExpiringDict](https://github.com/mailgun/expiringdict)












### Questions?

1. What types of Caching are there?

* In-process caching - shares memory with application
* Local cache - on the same node but using its own memory space - cannot degrade main applciation performance
* Remote and distributed caching - to service distributed horizontally scaled workloads

2. Is `expiringdict` and `lrucache` and `cachetools` per process cache?

* These use local in-process memory - only available to the process inside vm (or container) it is on.
* Processes do not share memory but threads do.
* per-process (or in-process) caching prevents other processes from using the same cache
* When a process restarts - the cache is lost
* Good for a single process or node app.
* Degrade the performance of the main application because of the same memory usage and can also cause out of memory errors
* Cache will not persist across processes

lrucache, cachetools and expiringdict are all using a python dict behind the scenes.

redis-simple-cache - schedules storing in redis db

Must use memcached or redis.

> Performant is not a good word. Rather get the metrics on a base line performance and improve it based on what your customer wants.

Aspects to improve application performance:

* Speed up code.
* Speed up hardware.
* Lower network latency.
* Add caching to remove lookup latency.
* Remove caching to reduce memory usage.
* Add a server to the pool to increase throughput.
* Remove a server from the pool to decrease costs.

> Web users have very specific complaints about performance: slow page loads and content that shifts around

Trigger cache rebuild when catalogue rebuild completes.
Rebuild removes existing cache?

product data can be cached 11000 products

stock data cached 11000 * 170 = 1870000 - hash

article_number and uom and store code

categories cache

Methods:

* https://github.com/mailgun/expiringdict
* Memcached


## Sources

* [AWS Caching Best Practices](https://aws.amazon.com/caching/best-practices/)
* [Django Cache Framework](https://docs.djangoproject.com/en/4.1/topics/cache/)
* [Stackoverflow: Performant](https://stackoverflow.blog/2022/11/17/performant-is-nonsense-but-performance-can-still-matter/?cb=1)
* [Caching in Action](https://medium.com/@sandeep4.verma/caching-in-action-2127b6ed4a69)
* [Youtube: Jack of Some - cache vs redis](https://www.youtube.com/watch?v=mHJoq4aK4lk)