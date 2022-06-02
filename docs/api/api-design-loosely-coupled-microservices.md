
---
author: ''
category: API
date: '2022-05-31'
summary: ''
title: API Design - Loosely Coupled Microservices
---

Independence it vital for independent scaling - horizontally scaling or deprecating just the service needed based on usage.

If they are too dependent on each other (or closely coupled) - a break or change in one microservice will affect the others.

### Creating Loosely Coupled Services

* Association coupling - microservices may be independent but they work together as part of the system - manage dependencies and permissions
* Use Schemas - Control the data you consume with a schema for internal and external services
* Alternate couplings - Build fail safes and prioritise response time with REST
* Use APIs to share data - each service has its own database typically - data is shared via the api preventing bad data from ever being entered and gives the service the ability to change architecture without the calling service from knowing
* Keep dependencies to a minimum - Keeping shared libraries to a minimum - can allow services to be language agnostic
* Asynchronous Communication - callers expecting a response in a specific amount of time - it needs to be monitored and have a circuit breaker to prevent resource pile up or consumption. Look to use async messaging like kafka.
* Independent Testing Environments - To prevent cascading failures - independent deployments and independent testing environments.
* Avoid downstream testing - mock responses from remote services
* Avoid domain creep - there should be flow and permissions between services - do not just share information with all services - lest you expose unnecessary info.

- Synchronous APIs: immediate return of data - clients requests and waits for a response
- Asynchronous APIs: supply a callback to the client (requestor) - when the resource is ready.

Returning a `202 Accepted` and a link to poll for status or results would be a Asynchronous API implemented synchronously.

### Larger Organisations

The enterprise service bus (ESB) is less focused on just HTTP and supports JMS, AMQP and others - so focused on both synchronous and asynchronous apis.

> Here you may find a service that accepts client communications over HTTP, but then has a persistent runtime connected to a backed queue hosted on RabbitMQ, or consuming a topic hosted on Kafka. You may find an integration with a custom trigger looking for updates or inserts in a given table. On every change to that table the system may grab that event and emit a new event in the form of message sent to the queue or a topic: thereby translating the DB world to the Message world and offering systems that don’t need to understand DB logic the ability to simply subscribe to the topic instead.

* Transaction Integrity - example bank transaction - cannot debit until credit completed successfully - rollback if not. Stateless HTTP and API gateways is not the correct place to handle these transactions.
* Exception handling - building systems with a backoff function - that retries less frequently - can't be handled in the request-response cycle of an HTTP request.

> Asynchronous systems are often solving integration problems, translating between protocols, handling stateful sockets and more. Those systems are built to cater for those specific needs. API Management systems and APIs in general are built to make it as easy as possible for developers to find and use those APIs. Moreover, those APIs are usually stateless, RESTful APIs that are only using a single protocol: http. Complex architectures require both types of platforms and understanding when and how one uses each of these is crucial for an elegant system design

## Source

* [Nordic APIs: Loosely coupled microservices](https://nordicapis.com/how-to-design-loosely-coupled-microservices/)
* [Synchronous vs Asynchronous APIs](https://www.techtarget.com/whatis/definition/synchronous-asynchronous-API)
* [Difference between synchronous and asynchronous APIs](https://cloud.google.com/blog/topics/developers-practitioners/differences-between-synchronous-web-apis-and-asynchronous-stateful-apis)

