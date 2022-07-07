---
author: ''
category: Tools
date: '2022-07-05'
summary: ''
title: What is MQTT?
---

## What is MQTT?

* Open-source
* Pub-sub messaging
* No queues
* designed for resource constrained devices (low bandwidth and high latency - satellite and dial up)
* unreliable networks
* Security: TLS
* created from the Tech Industry
* Not layered: extensions require new implementations of clients and servers
* QOS (Quality of Service): At most once (0), at least once (1) and Exactly once (2)

## What is AMQP?

* open-source
* Security: TLS and SASL (Simple Authentication Security Layer)
* created from the Finance Industry
* Layered: extensions are backward compatible
* QOS (Quality of Service): At most once (0), at least once (1) and Exactly once (2)



## Sources

* [MQTT vs AMQP](https://stackoverflow.com/questions/39615697/cloud-connectivity-for-mqtt-and-amqp)
* [AMQP vs MQTT: Comparing Instant Messaging Protocols](https://www.cometchat.com/blog/amqp-vs-mqtt-comparing-instant-messaging-protocols)