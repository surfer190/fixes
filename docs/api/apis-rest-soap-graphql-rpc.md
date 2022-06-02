---
author: ''
category: API
date: '2022-05-30'
summary: ''
title: Api's - Rest vs Soap vs RPC vs GraphQL
---

## API's: Rest vs Soap vs RPC vs GraphQL

### RPC

* Local clients sends commands to a remote server
* Stubs convert client and server requests and responses
* xml-rpc and json-rpc - google made general purpose rpc (gRPC)
* Apache Thrift and twitter twirp use gRPC for internal microservices communication
* RPC - short lightweight messages go easy on the network
* Used verbs to manipulate the service, eg. getCustomerAccount

### SOAP

* Simple Object Access Protocol
* Microsoft created in 1999
* Every soap message has an envelope, header and body (and a fault when it fails)
* Soap `ws-security` - encrypts messages
* Soap can chain messages - for complex transactions with multiple parties
* Soap very complex and verbose
* Used verbs to manipulate the service, eg. getCustomerAccount

### REST

* Representational State Transfer
* Resource based
* Keeps verbs to a minimum: HTTP methods
* Client-server autonomy: as long as the api interface does not change the client and server can change the database it uses or anything
* Uniform interface: 1 naming convention or end-point format (endpoint is uri with http method)
* Layered system architecture: client knows nothing of server architecture - intermediary or end server
* Stateless interactions: each request is taken as new (opposite of soap but soap allows both)
* HTTP caching
* Code on demand
* Can be chatty - getting too much info for the client
* Shallow learning curve

### GraphQL

* In 2015 - Facebook got tired of REST overfetching data
* Single request - returns all inclusive reply
* Single endpoint
* client can customise what is returned with a schema
* Steep learning curve

> Event driven architecture - subscribing to events instead of polling of request-response. Event producers and consumers don't directly depend on each other. They act asynchronously and execute operations when needed.






## Sources

* [Comparing API Architectural Styles: SOAP vs REST vs GraphQL vs RPC](https://www.altexsoft.com/blog/soap-vs-rest-vs-graphql-vs-rpc/)