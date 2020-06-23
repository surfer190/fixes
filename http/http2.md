# Learning HTTP/2

HTTP/2 (`h2`) is the major revision of the network protocol used by the world wide web - **meant to improve the perceived performance of loading web content**

HTTP/1.1 was approved in 1999 - since then nothing has changed.
Even slight delays make web users lose interest.

Apparently `h2` powers google, facebook, twitter and wikipedia.

### Foreward

In 2009, HTTP/1.1 was a decade old.

> Now loading a single web page often involved making hundreds of requests, slowing down the web

Many alternative protocols were introduced:
* Roy Fielding's WAKA
* HTTP over SCTP 
* Google's SPDY - making use of Chrome browser

In 2012: firefox , nginx and akamai implemented the protocol

In October 2012, the HTTP working group charted `HTTP/2` using `SPDY` as a starting point.

> ...in a few cases it was agreed that moving forward was more important than one person’s argument carrying the day, so we made decisions by flipping a coin. While this might seem like madness to some, to me it demonstrates maturity and perspective that’s rare

In December 2014, `HTTP/2` was submitted to the Internet Engineering Steering Council.

- Mark Nottingham

## 1. Evolution of HTTP

* In 1930's, Vannevar Bush, introduced the idea of linking data together contextually - _memex_
* `Hypertext` was coined in 1963 by Ted Nelson - a body of information interconnected in a complex way not conveniently represented or presented on paper. - _docuverse_ or _xanadu_
* In 1989, `HTTP` was introduced by Tim Berners-Lee - he embraces hypertext: human readable information linked together in an unconstrained way and hypermedia: linking not bound to text.

### HTTP/0.9 and HTTP/1.0

`HTTP/0.9`:

* has a single method: `GET`
* No headers
* Could only fetch text - html

In 1996, RFC 1945, codified `HTTP/1.0`:

* Headers
* Response Codes
* Redirects
* Errors
* Conditional Requests
* Content Encoding (Compression)
* More request methods: `POST`, `PUT`, `DELETE`

Flaws:

* Inability to keep a connection open between requests
* Lack of a mandatory Host header
* Bare bones options for caching

`HTTP/1.1`:

* The protocol that has lived for 20 years
* Fixed the above `HTTP/1.0` issues
* The mandatory `Host` header made virtual hosting possible - serving multiple sites form a single IP
* No longer needed to reestablish the TCP connection on every request
* Extenstion to Caching headers
* An `OPTIONS` method
* The Upgrade Header
* Range requests
* compression with transfer-encoding
* pipelining - allows client to send all requests at once but server had to respond in order - so it was a "mess up"

### Beyond 1.1

* An ecommerce site went far beyond the vision of the interwoven docuverse
* `SPDY` introduced: multiplexing, framing and header compression

### HTTP/2

* Enhance user _perceived_ latency
* Address the _head of line blocking_ problem
* Not require multiple connections to a server
* Retain the semantics (names of things) of `HTTP/1.1`

## 2. HTTP/2 Quickstart

Getting an `h2` server up and running:

* Get and install a webserver that speaks h2
* Get and install a TLS certificate

### Getting a certificate

> A self-signed cert is not signed by a CA, it will generate warnings in a web browser

#### Using an Online Generator

Use an [online cert generator at sslchecker](https://www.sslchecker.com/csr/self_signed) - becasue the private key is not generated in a secure environment you control they should only used for experimentation.

#### Self-signed

Use OpenSSL.

    openssl genrsa -out key.pem 2048
    openssl req -new -x509 -sha256 -key privkey.pem -out cert.pem -days 365 \
    -subj "/CN=fake.example.org

#### Letsencrypt

* Easy automated and free Certificate Authority
* Use `certbot`

    wget https://dl.eff.org/certbot-auto
    chmod a+x certbot-auto
    ./certbot-auto certonly --webroot -w <your web root> -d <your domain>

This creates:

* Your certificate’s private key: `/etc/letsencrypt/live/<your domain>/privkey.pem`
* Your new certificate: `/etc/letsencrypt/live/<your domain>/cert.pem`
* The Let’s Encrypt CA chain: `/etc/letsencrypt/live/<your domain>/chain.pem`
* Your new cert and the chain all in one: `/etc/letsencrypt/live/<your domain>/fullchain.pem`

### Running your Server

[`nghttp2`](https://nghttp2.org/) is a useful tool for working with and debugging `h2`.

    sudo apt-get install nghttp2
    ./nghttpd -v -d <webroot> <port> <key> <cert>
    
eg.

    ./nghttpd -v -d /usr/local/www 8443 \
            /etc/letsencrypt/live/yoursite.com/privkey.pem \
            /etc/letsencrypt/live/yoursite.com/cert.pem

### Adding HTTP/2 to your Existing Webserver running Nginx

There is a [good tutorial at digitalocean on setting up http/2](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-with-http-2-support-on-ubuntu-18-04).

The gist of it is to change:

    listen 443 ssl;

to 

    listen 443 ssl http2;

## 3. How and Why we Hack the Web

Performance challenges:

* Hundreds of objects per page
* Variability in networks
* Wide range of devices using the site

A consistent and fast web experience is a challenge

### The Anotomy of a web page request

2 parts: fetching and rendering

Fetching:

1. Put URL in the queue to fetch
2. Resolve the ip address of the hostname of the URL
3. Open a TCP connection to the Host
4. If HTTPS, intiiate and finish a TLS handshake
5. Send the request for the page URL

Rendering:

1. Receive response
2. Parse Base HTML then trigger fetches for objects on the page
3. If the critical objects on the page have been received - start rendering
4. As additional objects are received - continue to parse and render until done

The above processes need to be done for every click - straining the network and devices.

#### Critical performance

Challenges on the network

* Latency - how long it takes for an ip packet to get from one point to another
* Round trip time (RTT) - double the latency
* bandwidth - Amount of data a connection can handle at a time
* DNS lookup - The internets phonebook - only needs to lookup once per hostname
* Connection time - three way TCP handshake. SYN -> SYN, ACK -> ACK
* TSL Negotation time - More round trips and processing time

Challenges on the server

* Time to First Byte (TTFB) - Time from when a browser sends a request to acquiring the first byte
* Content download time - Time to last byte (TTLB)
* Start Render Time - How quickly a client can put something on the screen for the user
* Document Complete (Page Load Time) - Time a page is considered `done` by the client

Internet movement to more:

* More bytes
* More objects
* More complexity
* More hostnames
* More TCP sockets

#### The problems with HTTP/1

* Head of line blocking - a browser usually wants many objects from a particular host. Each asset needs its own connection - it doesn't use a single connection. If any of those requests or responses have a problem - subsequent requests are blocked. Modern browsers open up to 6 connections per host.
* Inefficient use of TCP - built in congestion avoidance mechanisms. It is not the fastest but it is the most reliable. Central to this is the _congestion window_ - the number of tcp packets a client can send before being acknowledged by the receiver.

> An internet protocol packet is a series of bytes encapsulated in a dataframe. The most data one packet can transmit is 1460 bytes.

Sending one packet at a time is not terribly efficient. TCP has a _slow start_ to feel out the network first to not congest it. The window size will be calculated during the _slow start_.

> Modern operating systems commonly use an initial congestion window size between 4 and 10 packets, meaning only 5840 bytes can be sent before needing an acknowledgement.

Todays webpages average 2MB - 9 round trips are needed.

When packet loss occurs the congestion window is decreased.

* Fat message headers - no way to compress the message headers. Headers make up the majority of the bytes on a request. The median request header is 460 bytes. A page with 140 objects - that is 63 KB.
* Limited priorities

### Web Performance Techniques

* Steve Souders, in early 2000's wrote _High Performance Websites_ and _Even faster websites_
* In 2010, Google added web performance as a criteria in ranking

> Majority of time is spent fetching assets and rendering the page - rather than the inital load. 

### Best Practices for Web Performance

* Optimise DNS Lookups
* Optimise TCP Connections
* Avoid redirects
* Cache on the client
* Cache at the edge
* Conditional caching
* Compression and minification
* Avoid blocking CSS/JS
* Optimise Images

#### Optimise DNS Lookups

* Limit unique hostnames
* Understand DNS resolution
* Leverage DNS prefetch eg. `<link rel="dns-prefetch" href="//ajax.googleapis.com">`

#### Optimise TCP Connections

* Leverage preconnect: `<link rel="preconnect" href="//fonts.example.com" crossorigin>` - establishes a connection before it is needed
* Use early termination - leverage a CDN (Content Delivery Network)
* Use TLS best practices for optimising HTTPS

#### Avoid redirects

* Redirects trigger connections to additional hostnames
* Use rewrite rules if it is the same host
* Redirects are used in the dark art of SEO - sometimes tearing the bandaid off in one go is the best solution

#### Cache on the client

- Nothing is faster than retrieving an asset from local cache
- It is also cheaper
- TTL (Time to live) - specifies the time to keep resources
- Static content like images and versioned content can be cached forever
- For CSS, JS and personalised objects cache twice the median session time

Client caching can be set through the `Cache control`, `max-age` and `Expires` headers.

#### Cache at the Edge

- Take strain off server infrastucture
- Only sharable assets should be cached at the edge. Not personalised items.
- Assets that are time sensitive should also be avoided

#### Conditional caching

* Only give me the new asset if it has changed
* Use the `Last-Modified-Since` Header
* Include an `Etag`

#### Compression and minification

* All textual context can be compressed
* Comments and space is removed
* Compression reduces size with `gzip` and `deflate`

#### Avoid blocking CSS/JS

* CSS tells the browser where to render content - clients therefore download it before rendering.
* It is good to place CSS resources early in the `<head>` of html
* jS by default is fetched and prcoessed at the point in the HTML
* If JS order is not critical and it must run before `onload` then mafe use of:

    <script async src=”/js/myfile.js”>

* If execution order is important but scripts can run after the DOM is loaded

    <script defer src="/js/myjs.js">

* If JS is not critical to the view, then only fetch after `onload` fires

> If all this sounds a tad complicated, that’s because it is

#### Optimise Images

* Fewest bytes to achieve a given visual quality
* Image metadata should be removed before sending to clients [Oreilly High Performance Images](https://www.oreilly.com/library/view/high-performance-images/9781491925799/)

### AntiPatterns

> HTTP/2 will only open a single connection per hostname, some HTTP/1.1 best practices are turning into anti-patterns for h2

* Spriting and resource consolidation inlining - In HTTP/2 a given request is no longer blocking.
* Embedding JS into HTML is no longer cacheable.
* sharding leverages browsers ability to open multiple connections per hostname
* Cookie-less domain

## 4. Transition to HTTP/2




### Sources

* [Learning HTTP/2 - Stephen Ludin and Javier Garza](https://www.oreilly.com/library/view/learning-http2/9781491962435/)