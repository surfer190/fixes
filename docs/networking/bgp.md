---
author: ''
category: Networking
date: '2020-11-25'
summary: ''
title: BGP
---
# BGP Basics

## BGP

* Border Gateway Protocol - routing protocol to exchange information between networks
* The AS (Autonomous System) is the cornerstone of BGP - uniquely identifies networks with a common routing policy
* widely used for the internet backbone

## Path Vector Protocol

* BGP is a _path vector_ routing protocol - a route is a pairing between a destination and attributes of the path to that destination

Eg.

    12.6.126.0/24 207.126.96.43  1021  0 6461 7018 6337 11268 i
    
    AS PATH: 0 6461 7018 6337 11268 i

## Definitions

* Transit - Paying to carry traffic across a network
* Peering - Exchanging routing information and traffic
* Default - Where to send traffic when there is no explicit match in the routing table

## Autonomous System

* Collection of Networks with the same routing policy
* Single routing protocol
* Under single ownership / administrative control
* Identified by an ASN (Autonomous System Number)

## Autonomous System Number

* 0 - 65535: original 16-bit range
* 65535 - 4294967295: 32-bit range

Usage:

* 0 and 65535: reserved
* 1 - 64495: public internet
* 64496-64511: documentation
* 64512-65534: Private use
* 23456: 32-bit range in 16-bit world
* 65536-65551: documentation
* 65552-4294967295: public internet

* Distributed by regional internet registry
* [Check who assigned ASN](http://www.iana.org/assignments/as-numbers/as-numbers.xhtml)

## BGP Basics

* Runs over TCP port 179
* Learns paths but internal and external BGP speakers
* Picks the best path and installs it in the routing table (RIB)
* Best path is sent to external neighbours
* Policy is applied to choose best path

## eBGP - External BGP Peering

* Between BGP speakers in different AS
* Should be directly connected

## iBGP - Internal BGP Peering

* BGP peer within the same AS
* Do not need to be directly connected
* Must be fully meshed


    
## Source

* [African Union European Luxembourg BGP Paper](https://au.int/sites/default/files/documents/31363-doc-session_4-1-_bgp_intro.pdf)