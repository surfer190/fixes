---
author: ''
category: http
date: '2022-11-09'
summary: ''
title: HTTP Caching
---

## HTTP Caching

> The HTTP cache stores a response associated with a request and reuses the stored response for subsequent requests.

* No need to deliver the request to the origin server, closer the client and cache, the faster the response
* The typical example: browser itself stores a cache for browser requests
* The origin server does not need to parse and route the request, restore the session based on the cookie, query the DB for results, or render the template engine - reduces the load on the server.

> Proper operation of the cache is critical to the health of the system.

### Types of Caches

The [IETF HTTP working group RFC (Request for Comments) on HTTP Caching](https://httpwg.org/specs/rfc9111.html) states 2 types of caches:

* Private caches
* Shared caches

#### Private Caches

* cache tied to a specific client - typically the browser
* not shared so can store a personalised response
* May cause information leakage if shared
* Personalized contents are usually controlled by cookies

Must specify:

    Cache-Control: private

> Note: if the response has an `Authorization` header, it cannot be stored in the private cache (or a shared cache, unless public is specified)

#### Shared Cache

> The shared cache is located between the client and the server and can store responses that can be shared among users

2 types:

* proxy caches
* managed caches

##### Proxy caches

* Reduce traffic outside the network
* Not managed by service developer - controlled by HTTP headers
* Some proxies are old and do not respect headers

Kitchen sink headers:

    Cache-Control: no-store, no-cache, max-age=0, must-revalidate, proxy-revalidate

> In recent years, as HTTPS has become more common and client/server communication has become encrypted, proxy caches in the path can only tunnel a response and can't behave as a cache, in many cases. In this case there is no need to worry about outdated proxy cache.

On the other hand, if a TLS bridge proxy decrypts all communications in a person-in-the-middle manner by installing a certificate from a CA (certificate authority) managed by the organization on the PC, and performs access control, etc. — it is possible to see the contents of the response and cache it.

##### Managed caches

Managed caches are explicitly deployed by service developers to offload the origin server and to deliver content efficiently

Example:

* reverse proxies
* CDNs
* service workers with Cache API

In most cases they are managed with the `Cache-Control` header

To opt out of private or proxy cache:

    Cache-Control: no-store

Example:

* Varnish Cache uses VCL (Varnish Configuration Language, a type of DSL) logic to handle cache storage
* Service workers and Cache API allow for control with javascript

### Heuristic caching

Automatic caching for certain characteristics

Example - a response that ahs not been updated in a long while:

    HTTP/1.1 200 OK
    Content-Type: text/html
    Content-Length: 1024
    Date: Tue, 22 Feb 2022 22:22:22 GMT
    Last-Modified: Tue, 22 Feb 2021 22:22:22 GMT

Despite no `max-age` header the heuristics will determine it to be cached.

More interesting info in [MDN: HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

* The `ETag`
* Cache Busting for CSS and JS

## Sources

* [MDN web docs: HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
