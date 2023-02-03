---
author: ''
category: Tools
date: '2022-12-20'
summary: ''
title: Varnish Cache
---

## 1. What is Varnish?

* a _reverse caching proxy_: a proxy server that speaks HTTP that
you put in front of your web servers. Varnish heavily reduces the load and the latency of your web servers.
* serving client requests with content that is cached in memory, eliminating the need to send each client request to the web servers
* when the content for a request is not available in cache, Varnish will connect
to web servers to retrieve the requested content,

tiers:

* the origin: your web servers prone to high load and latency
* the edge: outer tier - where client interacts with your platform

> Varnish speaks HTTP and sits in front of the web servers, it seemingly assumes the role of the web server. The HTTP client that connects to the platform has no idea that Varnish is actually a proxy.

2 versions:

* open source - Varnish Cache (the project)
* enterprise version - Varnish Enterprise (the product)

In default mode: Varnish respects `Cache-Control` headers.

### What is VCL?

* Varnish Configuration Language
* Domain specific language to control handling, routing and caching

> When `varnishd` process is started, the VCL file is processed, VCL code is translated into C, the C is compiled to a shared object and that object is linked to the server process

DNS resolution of the hostname is done when the VCL configuration is loaded and not on every backend connection








## Source

* [Varnish 6 by Example](https://info.varnish-software.com/the-varnish-book)
