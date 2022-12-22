---
author: ''
category: django
date: '2022-11-26'
summary: ''
title: Django Cache
---

## Django Cache

The cache system requires a small amount of setup - you must tell it where to store the cache

* database
* filesystem
* memory

> An important decision that affects your cache’s performance

It goes in the [CACHE](https://docs.djangoproject.com/en/4.1/ref/settings/#caches) setting

### Memcached

[Memcached](https://memcached.org/) is an entirely memory-based cache server.

> Used to reduce database access and dramatically increase site performance

After installing Memcached itself, you’ll need to install a Memcached binding.

There are several Python Memcached bindings available; the two supported by Django are [pylibmc](https://pypi.org/project/pylibmc/) and [pymemcache](https://pypi.org/project/pymemcache/)

Settings:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

or using a socket:

> Unix sockets are a form of communication between two processes that appears as a file on disk.

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
            'LOCATION': 'unix:/tmp/memcached.sock',
        }
    }

> One excellent feature of Memcached is its ability to share a cache over multiple servers - this means you can run Memcached daemons on multiple machines, and the program will treat the group of machines as a single cache - without needing to duplicate the cache values

Example below uses shared cache

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
            'LOCATION': [
                '172.19.26.240:11211',
                '172.19.26.242:11211',
            ]
        }
    }

Memory-based caching has a **disadvantage**: because the cached data is stored in memory, the data will be lost if your server crashes

> Without a doubt, none of the Django caching backends should be used for permanent storage

### Redis

[Redis](https://redis.io/) is an in-memory database that can be used for caching

> To begin you’ll need a Redis server running either locally or on a remote machine.

The python binding for redis: [redis-py](https://pypi.org/project/redis/) is required and [hiredis](https://pypi.org/project/hiredis/) is recommended.

Settings:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379',
        }
    }

with auth:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': 'redis://username:password@127.0.0.1:6379',
        }
    }

servers setup in replication mode, write operations are done on the first server read operations are performed on the others at random:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': [
                'redis://127.0.0.1:6379', # leader
                'redis://127.0.0.1:6378', # read-replica 1
                'redis://127.0.0.1:6377', # read-replica 2
            ],
        }
    }

### Database caching

> Django can store its cached data in your database

This works best if you’ve got a fast, well-indexed database server.

Settings:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'my_cache_table',
        }
    }

> Unlike other cache backends, the database cache does not support automatic culling of expired entries at the database level. Instead, expired cache entries are culled each time `add()`, `set()`, or `touch()` is called.

#### Creating the cache table

    python manage.py createcachetable

> Like `migrate`, `createcachetable` won’t touch an existing table. It will only create missing tables.

### Filesystem caching

> The file-based backend serializes and stores each cache value as a separate file

Settings:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/django_cache',
        }
    }

> `LOCATION` should be absolute path

Make sure the cache is readable and writable by the server process.

### Local-memory caching

> The default cache

This cache is per-process and thread safe

> Thread safe means the code will work as expected even though being run simultaneously by multiple threads. Remember threads share memory and the data structures within.

Settings:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }

> The cache `LOCATION` is used to identify individual memory stores. If you only have one locmem cache, you can omit the `LOCATION`

* The cache uses a least-recently-used (LRU) culling strategy
* Note that each process will have its own private cache instance, which means no cross-process caching is possible.
* This also means the local memory cache isn’t particularly memory-efficient
* Probably not a good choice for production environments.
* Nice for development.

### Dummy Caching

Doesn't actually cache - just implements the caching interface without doing anything

This is useful if you have a production site that uses heavy-duty caching in various places but a development/test environment where you don’t want to cache and don’t want to have to change your code to special-case the latter.

Settings:

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

## Cache Arguments

Additional keys in cache settings:

* `TIMEOUT`: default timeout in seconds. Defaults to 300 seconds (5 mins). `None` for not expire. `0` for no cache/don't cache.
* `OPTIONS`:
    * `MAX_ENTRIES`: Max entries before old entries deleted. defaults to 300.
    * `CULL_FREQUENCY`: Fractions of entries removed when `MAX_ENTRIES` reached. Defaults to 3. So `1/3` is culled each time. Value of `0` means the entire cache is dumped.
* `KEY_PREFIX`: string prepended to all keys
* `VERSION`: default version number for cache keys
* `KEY_FUNCTION `: dotted path for function to create final cache key

Eg. Memcache

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
            'LOCATION': '127.0.0.1:11211',
            'OPTIONS': {
                'binary': True,
                'username': 'user',
                'password': 'pass',
                'behaviors': {
                    'ketama': True,
                }
            }
        }
    }

Eg. Redis

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379',
            'OPTIONS': {
                'db': '10',
                'parser_class': 'redis.connection.PythonParser',
                'pool_class': 'redis.BlockingConnectionPool',
            }
        }
    }

### The Per Site Cache

The simplest way to cache is to cache the entire site

Add `UpdateCacheMiddleware` and `FetchFromCacheMiddleware`:

    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    ]

Then add required settings:

* `CACHE_MIDDLEWARE_ALIAS` – The cache alias to use for storage.
* `CACHE_MIDDLEWARE_SECONDS` – The number of seconds each page should be cached.
* `CACHE_MIDDLEWARE_KEY_PREFIX` – If the cache is shared across multiple sites using the same Django installation, set this to the name of the site, or some other string that is unique to this Django instance, to prevent key collisions. Use an empty string if you don’t care.

`FetchFromCacheMiddleware`:

* caches GET and HEAD responses with status 200
* Responses to requests for the same URL with different query parameters are considered to be unique pages and are cached separately
* This middleware expects that a HEAD request is answered with the same response headers as the corresponding GET request; in which case it can return a cached GET response for HEAD request.

`UpdateCacheMiddleware` sets:

* `Expires` to the current datetime plus `CACHE_MIDDLEWARE_SECONDS`
* `Cache-Control` to give a max age for the page

Cache keys:

* If `USE_I18N` is set to True then the generated cache key will include the name of the active language.
* Cache keys also include the current time zone when USE_TZ is set to True.

### The per-view cache

    django.views.decorators.cache.cache_page(timeout, *, cache=None, key_prefix=None)

Caching the output of individual views

Example:

    from django.views.decorators.cache import cache_page

    @cache_page(900)
    def my_view(request):
        ...

> 900 seconds

The cache timeout set by cache_page takes precedence over the `max-age` directive from the `Cache-Control` header

The per-view cache, like the per-site cache, is keyed off of the URL. If multiple URLs point at the same view, each URL will be cached separately,

Example:

    urlpatterns = [
        path('foo/<int:code>/', my_view),
    ]

Cached seperately:

* `/foo/1/`
* `/foo/23/`

Direct to use a specific cache:

    @cache_page(60 * 15, cache="special_cache")
    def my_view(request):
        ...

Override cache prefix (of `CACHE_MIDDLEWARE_KEY_PREFIX`):

    @cache_page(60 * 15, key_prefix="site1")
    def my_view(request):
        ...

`cache_page` automatically sets `Cache-Control` and `Expires` headers in the response

#### Per-view cache with UrlConf

    from django.views.decorators.cache import cache_page

    urlpatterns = [
        path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
    ]

### Template fragment caching

More control and granularity

    {% load cache %}

Eg.

    {% load cache %}
    {% cache 500 sidebar %}
        .. sidebar ..
    {% endcache %}

Caching per-user or per some other paramter

    {% load cache %}
    {% cache 500 sidebar request.user.username %}
        .. sidebar for logged in user ..
    {% endcache %}

Language specific

    {% load i18n %}
    {% load cache %}

    {% get_current_language as LANGUAGE_CODE %}

    {% cache 600 welcome LANGUAGE_CODE %}
        {% translate "Welcome to example.com" %}
    {% endcache %}

## The low-level cache API

Your site includes a view whose results depend on several expensive queries -  the results of which change at different intervals

The per site, page or fragment cache would not work well as the data still changes enough to affect the business but not often enough that it needs to query the database every time - slowing down the responses.

You can use this API to store objects in the cache with any level of granularity you like

You can cache any Python object that can be pickled safely: strings, dictionaries, lists of model objects, and so forth.

Access the cache:

    from django.core.cache import caches
    cache1 = caches['myalias']

> Repeated requests will access the same object

To provide thread-safety, a different instance of the cache backend will be returned for each thread

Default cache:

    from django.core.cache import cache
    # equivalent to: caches['default'].

### Basic Usage

    # cache.set(key, value, timeout=DEFAULT_TIMEOUT, version=None)
    cache.set('my_key', 'hello, world!', 30)

    # cache.get(key, default=None, version=None)
    cache.get('my_key')

The timeout argument is optional and defaults to the timeout argument of the appropriate backend in the `CACHES` setting

If an object does not exist `None` is returned.

If you need to determine whether the object exists in the cache and you have stored a literal value None, use a _sentinel_ object as the default

    sentinel = object()
    cache.get('my_key', sentinel) is sentinel

> sentinel value (flag, signal value) - condition for termination - [wikipedia](https://en.wikipedia.org/wiki/Sentinel_value)

Default argument:

    cache.get('my_key', 'has expired')

Add (will not attempt update):

    cache.add('add_key', 'New value')

> Return value is True or False whether it did add

Get or set:

    cache.get_or_set('my_new_key', 'my new value', 100)

Any callable can be used as a default value:

    >>> import datetime
    >>> cache.get_or_set('some-timestamp-key', datetime.datetime.now)

Get many:

    >>> cache.set('a', 1)
    >>> cache.set('b', 2)
    >>> cache.set('c', 3)
    >>> cache.get_many(['a', 'b', 'c'])
    {'a': 1, 'b': 2, 'c': 3}

Set many:

    >>> cache.set_many({'a': 1, 'b': 2, 'c': 3})

Delete cache:

    cache.delete('a')

Delete many:

    cache.delete_many(['a', 'b', 'c'])

Remove everything in your cache (even stuff not set from your application):

    cache.clear()

Set a new expiration for a key:

    cache.touch('a', 10)

> `touch()` returns True if the key was successfully touched, False otherwise.

Increment and decrement:

    >>> cache.set('num', 1)
    >>> cache.incr('num')
    2
    >>> cache.incr('num', 10)
    12
    >>> cache.decr('num')
    11
    >>> cache.decr('num', 5)
    6

> `incr()`/`decr()` methods are not guaranteed to be atomic. On those backends that support atomic increment/decrement (most notably, the memcached backend), increment and decrement operations will be atomic

Close the connection:

    cache.close()

> The async variants of base methods are prefixed with a, e.g. `cache.aadd()` or `cache.adelete_many()`

[Information on async support of cache](https://docs.djangoproject.com/en/4.1/topics/cache/#id14)

#### Cache key prefixing

If you are sharing a cache instance between servers, or between your production and development environments, it’s possible for data cached by one server to be used by another server.

> Django will automatically prefix the cache key with the value of the `KEY_PREFIX` cache setting

#### Cache versioning

When you change running code that uses cached values, you may need to purge any existing cached values.

Easiest way is to flush the entire cache - but this can lead to the loss of cache values that are still valid and useful.
There is a system-wide identifier: `VERSION`

> The value of this setting is automatically combined with the cache prefix and the user-provided cache key to obtain the final cache key.

Primitive (basic building block) cache functions accept the version parameter:

    cache.set('my_key', 'hello world!', version=2)

#### Cache key transformation

Give a dotted path to a function called `make_key()` in the `KEY_FUNCTION` setting.

    def make_key(key, key_prefix, version):
        return '%s:%s:%s' % (key_prefix, version, key)

#### Cache key warnings

Memcached does not allow cache keys longer than 250 characters or containing whitespace or control characters, and using such keys will cause an exception.

Silence warnings with:

    import warnings

    from django.core.cache import CacheKeyWarning

    warnings.simplefilter("ignore", CacheKeyWarning)

## Source

* [Django Docs: Cache Framework](https://docs.djangoproject.com/en/4.1/topics/cache/#setting-up-the-cache)
* [Stackoverflow: What is the meaning of "Thread safe"?](https://stackoverflow.com/questions/261683/what-is-the-meaning-of-the-term-thread-safe)
