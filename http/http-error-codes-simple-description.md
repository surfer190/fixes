## HTTP Status Codes in a Nutshell

1xx: hold on
2xx: here you go
3xx: go away
4xx: you fucked up
5xx: I fucked up

[Twitter Source][https://twitter.com/nixcraft/status/548494265727188992]

### Non-Rude Version

2xx: Good - action taken with no errors
3xx: Redirect - ok, but resource is somewhere else
4xx: Error by the client - not found (Largest block)
5xx: Error on server - less descriptive, best to give better responses for clients logs

## All Status Code

A [wikipedia list of all status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

## All Headers

A [wikipedia list of all HTTP Headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Response_fields)

## Availability and Caching

Nothing worse than an API that can't handle requests

Cache runs in memory that keeps newly created calls
Sometimes a response takes a long time with multiple calls to multiple databases, that take a long time.
Putting that response into cache, means that the next few lookups won't need to do the heavy lifting again.

Available caching:
* [Varnish](https://varnish-cache.org/)
* [Hazel](https://hazelcast.org/)
* [Memcached](http://www.memcached.org/)

    


### Rate limiting

Even cache won't stop a huge amount of requests.
Each user has a certain number of requests in a given time period.
Prevents users flooding you with attacks and Denial of Service (DDOS)
Needs some form of authnetication to be successful

## Authentication

* API tokens - used when making requests - like a username and password
* Cross realm authentication
* HTTP Digest

**A lot of the above depends on framework, language and tools of choice**