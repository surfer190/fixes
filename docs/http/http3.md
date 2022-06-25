---
author: ''
category: Http
date: '2022-06-23'
summary: ''
title: Http3
---

# HTTP/3

> TCP is the main protocol that provides crucial services such as reliability and in-order delivery to other protocols higher up on the OSI model such as HTTP.

A HTTP Request uses a stack of protocols: HTTP on TLS on TCP on IP.

* HTTP deals with URLs and data interpretation
* TLS secures the connection with encryption
* TCP enables reliable in order delivery
* IP routes packets between machines

A new protocol was introduced called `QUIC`.
`HTTP/2` requires changes to work on `QUIC`.

TCP (Transmission Control Protocol) focuses on reliability over efficiency - requiring a full handshake and a round trip for requests.
TCP is large and complex and has many implementations and extensions.

HTTP/3 is essential HTTP/2 over QUIC

Main features coming from QUIC:

* Faster connection set-up
* Less HoL blocking
* Connection migration

Importantly - many other protocols can run over QUIC: `DNS`, `SSH`, `SMB`, `RTP` etc.

The reason QUIC runs on UDP (User Datagram Protocol) - is due to the difficulty in updating all the hardware and software of the internet. A full independent transport layer - would require all devices on the internet to be upgraded.

> UDP is bare bones. ONly supports port numbers. Good for live traffic, low-up front delay requirements (like DNS) and for single round trip requirements.

So reasons UDP is used is for easy deployment.

QUIC implements most TCP features:

* reliable (with acknowledgements and retransmissions)
* connection setup with a handshake
* flow-control and congestion-control

> Re-implemented in a more performant way

Newer versions of TLS (1.3 and up) only require a single round trip.

There is no clear text version of QUIC. Encryption is ingrained into QUIC.
Most packet headers are also encrypted.

Cons of QUIC:

* Network providers hesitate to allow QUIC: as the headers encrypt metrics they use to block
* QUIC encrypts each individual packet - TLS-over-TCP can encrypt several at a time
* Centralisation - Originally introduced by Google - the IETF QUIC proposal was created by many big companies: facebook, cloudflare, google and big CDNs - most likely leading to more centralisation.

> For HTTP/1.1, the resource-loading process is quite simple, because each file is given its own TCP connection and downloaded in full.

> TCP was never designed to transport multiple, independent files over a single connection. Because that is exactly what web browsing requires, this has led to many inefficiencies over the years. QUIC solves this by making multiple byte streams a core concept at the transport layer and handling packet loss on a per-stream basis.

### Connection Migrations

> For TCP, In practice every network change means that existing TCP connections can no longer be used.

Quick introduces the `connection identifier (CID)` - a common list of (randomly generated) CIDs mapping to a single connection.

It does not change when chainging networks - unlike TCP that uses the 4 tuple (client IP address + client port + server IP address + server port)

> QUIC changes the CID every time a new network is used - to prevent privacy issues? But its encrypted right?

QUIC Implementations are currently done in user-space not kernel-space yet.

QUIC can evolve: `QUIC uses individual frames to send meta data, instead of a large fixed packet header.`

## Performance Improvements

[HTTP/3: Performance Improvements](https://www.smashingmagazine.com/2021/08/http3-performance-improvements-part2/)




## Source

* [Smashing Magazine HTTP3 Core Concepts](https://www.smashingmagazine.com/2021/08/http3-core-concepts-part1/)