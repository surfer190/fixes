---
author: ''
category: Http
date: '2020-07-29'
summary: ''
title: Http2
---
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

* Head of line blocking
    - a browser usually wants many objects from a particular host.
    - Each asset needs its own connection - it doesn't use a single connection.
    - If any of those requests or responses have a problem - subsequent requests are blocked.
    - Modern browsers open up to 6 connections per host.
* Inefficient use of TCP
    - built in congestion avoidance mechanisms.
    - It is not the fastest but it is the most reliable.
    - Central to this is the _congestion window_ - the number of tcp packets a client can send before being acknowledged by the receiver.

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

> in order to support HTTP/2 all you need to do is upgrade to a web server that speaks h2

Considerations:

* browser support for `h2`
* Move to serving over TLS
* Tuning your website for h2
* Third parties on your site

### Browser Support

Any browser not supporting H2 will just fall back

### Moving to TLS

* Most browsers only access H2 over TLS
* TLS 1.2 is required

### Undoing H1.1 and tuning for H2

* concatenation - request overhead is not much in bytes and time is not much bigger.
* minification - keep doing in `h2`
* sharding - HTTP/2 uses a single socket - sharding breaks that goal
* cookie-less domains - seperate domains should be avoided

### third Parties

* Can be a major drag on the performance gains of http2

## 5. The HTTP/2 Protocol

### Layers of HTTP/2

* Framing layer - core to multiplexing
* Data/HTTP layer - traditional HTTP

Aspects of the protocol:

* Binary protocol - Binary protocol - 1's and 0's are transmitted over the wire
* Header compression - headers are compressed (less bytes over the wire)
* Multiplexed - requests and responses are interwoven within a single TCP connection
* Encrypted - Data on the wire is encrypted

#### Connection

* The base element of the HTTP/2 session is the TCP/IP socket connection
* `h1.1` is stateless, `h2` has connection level settings and a header table.

#### Frames

HTTP/2 is framed, HTTP/1.1 is text delimited

Parsing HTTP/1.1 is slow and error prone.

HTTP/2 frame headers:

* `Length` (3 bytes) Length of the frame payload
* `Type` (1 byte) Type of Frame
* `Flags` (1 byte) Flags specific to frame type
* `R` (1 bit) A reserved bit
* `Stream Identifier` (31 bits) A unique identifier of teh stream
* `Frame Payload` (variable) The actual frame content

Everything is deterministic, so parsing it is easier than non-deterministic text

Because of framing h2's requests can be interwover / multiplexed - no waiting for to send or receive the full request / response before sending another. No head of line blocking.

HTTP/2 Frame types:

* `DATA` - Core content
* `HEADERS` - HTTP headers and priorities
* `PRIORITY` - Priority (changes / stream priority)
* `RST_STREAM` - Allows endpoint to end a stream
* `SETTINGS` - Communicates connection level parameters
* `PUSH_PROMISE` - Indicates a server is about to send something
* `PING` - Tests connectivity and measures RTT (Round Trip Time)
* `GOAWAY` - Tells an endpoint a peer is done accepting new streams
* `WINDOW_UPDATE` - Communicates how many bytes an endpoing is willing to receive
* `CONTINUATION` - Used to extend header blocks

#### Streams

Stream - Independent, bidirection sequence of frames exchanged between the client and server within an HTTP/2 connection.

Requests and responses happen on the same stream.

#### Messages

Message - Generic term for an HTTP request or response

A stream transmits a pair of request/response messages.

At a minimum a message consists of a:

* `HEADERS` frame

H1 headers and responses are split into message headers and the message body.
An H2 request/response is split into HEADERS and DATA frames.

Differences between H1 and H2 messages:

**Everything in H2 is a header**

H1 request and response:

    GET / HTTP/1.1
    Host: www.example.com
    User-agent: Next-Great-h2-browser-1.0.0
    Accept-Encoding: compress, gzip

    HTTP/1.1 200 OK
    Content-type: text/plain
    Content-length: 2

H2 request and response:

    :scheme: https
    :method: GET
    :path: /
    :authority: www.example.com
    User-agent: Next-Great-h2-browser-1.0.0
    Accept-Encoding: compress, gzip

    :status: 200
    content-type: text/plain

> This h2 representation is not what goes over the wire

**No chunked encoding**

Since we know the length of the frame ahead of time - using frames there is no need for chunking.

**No more 101 responses**

Switching protocols response is for upgrading a websockets connection.
ALPN provides more explicit protocol negotiation paths with less round trip overhead.

#### Flow Control

The client or server can pace the delivery of data.
Reason for slowing the stream is to ensure it does not choke out others.
Client might also have bandwidth and memory issues.

Setting the maximum value of `2^31-1` effectively disables it.

Flow control information is indicated in `WINDOW_UPDATE` frames.

#### Priority

Once the browser has the HTML - it needs other things like CSS and JS to render the page.
Without multiplexing it needs to wait for a response before asking for a new one.

With h2 the browser can send all resource requests at the same time.
The problem is that priority is lost.

Using `HEADERS` and `PRIORITY` the client can communicate the order that the responses are needed.

A depenecy tree is built with prorities and weights (by the browser)

### Server Push

The best way to improve performance for a particular object - it to have it in the browsers cache before it is even asked for.

This is H2's **server push** feature - sending an object to a client because it knows the client will need it in the future.

**More info in the book**

### Header Compression (HPACK)

The average webpage requires 140 requests
The median size of requests is 460 bytes

On a congested network the crime is the very few unique bytes

> Why not just use GZIP for header compression instead of HPACK? It would be a lot less work, for certain. Unfortunately the CRIME attack showed that it would also be vulnerable leakage of encrypted information. CRIME works by the attackers adding data to a request and then observing whether the resultant compressed and encrypted payload is smaller. If it is smaller they know that their inserted text overlaps with something else in the request such as a secret session cookie. In a relatively small amount of time the entire secret payload can be extracted in this manner. Thus, off-the-shelf compression schemes were out, and HPACK was invented.

For example:

request 1:

    :authority: www.akamai.com
    :method: GET
    :path: /
    :scheme: https
    accept: text/html,application/xhtml+xml
    accept-language: en-US,en;q=0.8
    cookie: last_page=286A7F3DE
    upgrade-insecure-requests: 1
    user-agent: Awesome H2/1.0

request 2:

    :authority: www.akamai.com
    :method: GET
    :path: /style.css
    :scheme: https
    accept: text/html,application/xhtml+xml
    accept-language: en-US,en;q=0.8
    cookie: last_page=*398AB8E8F
    upgrade-insecure-requests: 1
    user-agent: Awesome H2/1.0

The first request is 220bytes and the second is 230 bytes.
But only 36 bytes are unique. Only sending the 36 unique bytes will mean an **85%** saving.

**More info in the book**

### On the Wire

h2 on the wire in in binary and compressed

HTTP/2 GET Request

    :authority: www.akamai.com
    :method: GET
    :path: /
    :scheme: https
    accept: text/html,application/xhtml+xml,...
    accept-language: en-US,en;q=0.8
    cookie: sidebar_collapsed=0; _mkto_trk=...
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh;...

HTTP/2 GET Response (Headers)

    :status: 200
    cache-control: max-age=600
    content-encoding: gzip
    content-type: text/html;charset=UTF-8
    date: Tue, 31 May 2016 23:38:47 GMT
    etag: "08c024491eb772547850bf157abb6c430-gzip"
    expires: Tue, 31 May 2016 23:48:47 GMT
    link: <https://c.go-mpulse.net>;rel=preconnect
    set-cookie: ak_bmsc=8DEA673F92AC...
    vary: Accept-Encoding, User-Agent
    x-akamai-transformed: 9c 237807 0 pmb=mRUM,1
    x-frame-options: SAMEORIGIN

    <DATA Frames follow here>

* Status code: 200 (Success)
* a cookie is set
* Content is gzipped (content-encoding)

To see what actually happens over the wire use [nghttp](https://github.com/nghttp2/nghttp2/)

## 6. HTTP/2 Performance

> Browsers all have different implementations - so there can be considerable differences between them

Looking at single requests means the only improvements can be:

* header compression
* connection reuse
* avoidance of head of line blocking

Not measuring:

* multiplexing
* server push

### Latency

* Time it takes for a packet of data to get from one point to another
* The Round trip time measured in `ms`

2 main factors are:

1. distance between 2 points
2. speed of the transmission medium (radio waves, vd fibre vs copper)

The speed of light in optical fiber is about 2/3 the speed of light in a vacuum or around 200,000,000 meters per second

However this is theoretical as fibre is never laid in a straight line and gateway, routers, switches and the server itself can hinder this.

> Mike Belshe wrote a paper called “More Bandwidth Doesn’t Matter (Much)” - saying that once you his 5 - 8Mbps in bandwidth a webpage speed hits a limit. On the other hand Page load time goes down exponentially with latency. Hence using fibre is more important than a high bandwidth copper line.

> Decreasing latency always makes websites faster

You can use `ping` to measure latency

    $ ping -c 4 fixes.co.za
    PING fixes.co.za (37.139.28.74): 56 data bytes
    64 bytes from 37.139.28.74: icmp_seq=0 ttl=50 time=249.768 ms
    64 bytes from 37.139.28.74: icmp_seq=1 ttl=50 time=271.186 ms
    64 bytes from 37.139.28.74: icmp_seq=2 ttl=50 time=294.646 ms
    64 bytes from 37.139.28.74: icmp_seq=3 ttl=50 time=332.131 ms

### Packet Loss

* When packets travelling across a computer network fail to reach their destination.
* Usually caused by network congestion
* Determental to h2 as it opens a single TCP connection and reduces the TCP window size when there is congestion

### Server Push

**More in the book**

### Time to First Byte (TTFB)

Measurement of the responsiveness of a web server

Contains:
* socket connection time
* time taken to send the HTTP request
* time taken to get the first byte of the page

HTTP/2 does a lot more work teh H1:

* Adjusting window sizes
* Building the dependency tree
* Maintaining static and dynamic tables of header info
* Compressing and decompressing headers
* Adjusting priorities
* Pushing streams not yet requested (server push)

### Third Parties

Analytics, tracking, social and advertising
These can slow down your site and even make it fail

Affects h2 because:

* a third party request is delivered over a different hostname
* a different hostname means cannot beneifit from: server push, dependencies and priorities
* Can't control the third party (unless you use self hosted analytics like matomo)

You can clearly see that opening multiple connections on H1 added significant connection time and SSL handshake time
On h2, only the first connection does this. The rest are sent over the same connection.

### HTTP/2 Antipatterns

* Domain sharding - many small objects on different domains to trick into sending in parrallel (6 TCP connections per hostname - therefor 30 over 5 hostnames)
* Inlining - inline style and JS into HTML with the aim of saving connections and round trips. With this you lose valuable features like caching.
* Concatenating - consolidating many small files into a big one
* Cookie-less domains - some servers use cookies that exceed the size of a TCP packet. In h2 headers are compressed using HPACK. they also use additional host names.
* Spriting - a matrix of smaller images
* Prefetch - hints to the browser to fetch a cacheable item. H2 has _server push_

Prefetch example:

    <link rel="prefetch" href="/important.css">

#### Studies in the book

* Facebook improved perceived performance by `33%`, `1.5s` earlier than h1
* Yahoo.com: h1 displays in `5.5s`, h2 displays in `4s`

## 7. HTTP/2 Implementations

Read the book for support among desktop and mobile browsers...

## 8. Debugging H2

* Chrome developer tools
* `chrome://net-internals`
* Firefox developer tools
* [WebPageTest](https://www.webpagetest.org/)
* openssl
* [nghttp2](https://nghttp2.org)
* `curl`

    curl -v --http2 https://fixes.co.za/vim/undo-and-redo-in-vim/

* h2i
* wireshark

## 9. What is Next?

### TCP vs UDP

TCP is an IP datagram–based protocol that provides an agreed concept of a connection, reliability, and congestion control.

UDP (User Datagram Protocol), on the other hand, is much more basic. In this protocol datagrams (packets) are individual with no relation to any other UDP packet. There is no “connection,” no guarantee of delivery, and no ability to adapt to different network conditions

UDP is perfect for small individual queries - DNS.

Moving TCP out of kernel space into userspace for control

### QUIC

> TCP connections are stuck in the cage of TCP slow start, congestion avoidance, and irrational reaction to missing packets

* QUIC - Quick UDP Internet Connection - developed by Google.
* Takes HTTP/2 and places it atop a user space resident UDP-based transport protocol

Potencial Features:

* Out of order packet processing - in h2 if one packet is lost the entire connection stalls
* Flexible congestion control
* Low connection estbalishment overhead - goal is for 0-RTT - todays tech TCP and tLS1.2 has 3 round trips minimum
* Authentication of transport details - QUIC will authenticate the packet header
* Connection migration - IP Addresses may change in long lived connections

### TLS 1.3

* 1-RTT for new connections as opposed to 3 for TLS1.2


### Sources

* [Learning HTTP/2 - Stephen Ludin and Javier Garza](https://www.oreilly.com/library/view/learning-http2/9781491962435/)