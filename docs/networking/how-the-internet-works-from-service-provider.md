---
author: ''
category: Networking
date: '2020-10-05'
summary: ''
title: How does a Subscriber's Internet travel from Service Provider Perspective
---

# How does a Subscriber's Internet travel from Service Provider Perspective

## How does a packet travel Through a Service Provider

As with everything it depends on the solution provided - Fibre, Adsl and Wireless technology like 3g, 4g and LTE

Looking from a Fibre perspective the flow is bassically:

    ONT -> OLT -> ENNI -> RADIUS -> BNG -> PACKET INTROSPECTIN - P ROUTER - PEERING/IP TRANSIT

So let us go through what the above are:

* ONT (Optical Network Terminal) - device at subscriber's home that converts optical signals into electrical signals
* OLT (Optical Line Terminal) - convert, frame, and transmit signals for the PON network and to coordinate the optical network terminals multiplexing for the shared upstream transmission
* ENNI (External Network-to-Network Interface) - The boundary between 2 operators. Layer 2 Vlan is handed off.
* Radius - Speaks to the BNG to authenticate subscribers
* BNG (Broadband Network Gateway) - the access point for customers to connect to the broadband network
* PACKET INTROSPECTION - Inspects all traffic and stores amount of traffic used for subscribers
* P ROUTER (Provider Router) - Provide reachability between Provider Edge devices
* PEERING / IP TRANSIT - IP transit is when one entity pays another for the right to transit its upstream network (One entity is higher than the other on the chain). IP peering is a mutual exchange of data between two ISPs.



## Sources

* [What is a BNG?](https://netelastic.com/what-is-bng-and-which-one-is-right-for-your-network/)
* [What is a ONT?](https://www.otelco.com/faq/ont-optical-network-terminal/)
* [What is an OLT?](https://searchnetworking.techtarget.com/definition/Optical-line-terminal-OLT)
* [What is an ENNI?](https://wiki.mef.net/pages/viewpage.action?pageId=54762782)
* [What is Deep Packet Introspection?](https://digitalguardian.com/blog/what-deep-packet-inspection-how-it-works-use-cases-dpi-and-more)
* [What is a P Router?](https://orhanergun.net/what-does-p-router-mean-in-mpls/)
* [What is Peering and IP Transit?](https://blog.equinix.com/blog/2018/12/10/networking-for-nerds-do-you-know-the-difference-between-ip-peering-vs-ip-transit-for-enterprise-internet-interconnection/)