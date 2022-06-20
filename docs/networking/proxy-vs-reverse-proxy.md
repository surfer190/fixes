---
author: ''
category: Networking
date: '2022-06-15'
summary: ''
title: Proxy vs Reverse Proxy
---

[Proxy definition](https://en.wiktionary.org/wiki/proxy)

> To act or substitute an authorised act for another

## Proxy Server

A proxy server is a networking device or application that is positioned between the default gateway and the internet / external network.
Its primary use is in corporate to decrease the amount of internet traffic. If someone else had downloaded a file - the file would be cached on the proxy server so no external network request was required.
It also prevented certain protocols like SSH, could mask IP addresses and act as a firewall.

    Client -> Default gateway router -> Proxy -> Internet -> Destination Server

The client only communicates with the proxy.
The heavy lifting was done on the client side in this traditional proxy server.
The purpose of a proxy server is to protect clients.

## Reverse proxy

A reverse proxy is a networking device or application is position before the default gateway and is the only device an internet client speaks to.
The reverse proxy serves requests and contacts multiple upstream servers based on the request.
For example: a reverse proxy receiving a request for a static asset file may serve the file but when a request for json or html is received - is may send that request to an upstream web server for processing.

    Client -> Internet -> Default gateway router -> Reverse Proxy (Nginx) -> Destination Server (gunicorn)

* The client only communicates with the reverse proxy.
* Heavy lifting done on the server side.
* The purpose of a reverse proxy is to protect servers.

### Source

* [Difference between proxy and reverse proxy](https://www.strongdm.com/blog/difference-between-proxy-and-reverse-proxy)
