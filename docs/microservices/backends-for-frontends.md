---
author: ''
category: Microservices
date: '2022-07-14'
summary: ''
title: Backend for Frontend - API Pattern
---

## Backend for Frontend - The BFF Pattern

The scenario: You may have microservices for Customers, Orders, Products, Shopping carts, etc. The microservices expose APIs to be used by the frontend.

The problem: The data returned to the frontend by the Microservices may not be formatted or filtered according to the exact way the frontend needs to represent them

**Backend for Frontend is an alternative to GraphQL**

Formatting it on the client - slows down the client and responsiveness.

The BFF (Backend for Frontend) is used to shift the formatting work to the intermediate layer.
The frontend will request from the BFF.

> Also called an Edge service

A BFF is not a microservice - it does not have a bounded context and it scatter and gathers from other services.
It is usually stateless.

The BFF will:

* Call the other microservices (aggregation of service calls)
* Format the data based on the frontend representation
* Send the formatted data to the frontend

Less work and logic needed for the frontend. Less tests.
More tests and management for the Backend for frontend team.

Eg.

    Browser -> BFF  -> Order Service
                    -> USer Service
                    -> Menu Service
                    -> Cart Service
                    -> Product Service

> Ideally, the front-end team will be responsible for managing the BFF as well - but they don't seem to.

The latency added by the BFF is supposed to be much lower than that of the client or browser.

> If your application is a simple monolithic app, a BFF is unnecessary

> if your application depends on microservices and consumes many external APIs and other services, it is better to use a BFF to streamline the data flow and introduce a lot of efficiency to your application.

You can have multiple BFFs specific for specific clients. Instead of A single api for all clients.

> More Layers

Traditional apps might just have a single api gateway for all clients - The General-Purpose API Backend. These can become a bottleneck or single source of failure. Now the general purpose API is now managed by the "API Team" - another layer.

> The BFF eliminates any direct calls outside of the perimeter to the downstream services

### Advantages of a BFF

* Separation of concerns (autonomy) - frontend requirements seperated from backend concerns. Frontend can work on the BFF along with the app.
* Easier to maintain and modify APIs - client application knows less about the api structure - more resistant to change
* Better error handling in the frontend - BFF can add better client errors from service errors that mean nothing to the end user
* Better security - sensitive and unnecesary data can be hidden
* Shared team ownership of components - Frontend teams get to enjoy ownership of both their client application and its underlying resource consumption layer (higher dev velocities apparently)

### Disaadvantages

* Pushes more fan out - a single call to the BFF API - makes multiple downstream calls to different services. If any of those calls are slow it slows down the BFF response. If any of those calls break or fail, it breaks the API call. The BFF should communicate asynchronously with downstream services on message queues (not HTTP apis).
* Duplication and lower reuse: if the BFFs do similar things
* More components

### Best Practices

* Avoid implementing a BFF with self-contained all-inclusive API - Don't implement service level APIs in the BFF (formating/presentation/consumption/translation layer)
* Avoid BFF logic duplication - a single BFF should cater to a specific user experience, not a device type (mobile devices will share teh same experience)
* Avoid over-relying on BFFs - It should mainly be about formatting - don't use it for security etc.

> The BFF is tightly coupled to a specific user experience. The BFF is tightly focused on a single UI, and just that UI. That allows it to be focused, and will therefore be smaller. (Supposedly)

The organisation structure will determine which style of BFF is used - BFF per experience of client or BFF per client OS (Android, iOS or Web)

> Any organization that designs a system will produce a design whose structure is a copy of the organization's communication structure — Melvin E. Conway (Conway's Law)

> One experience, one BFF

### Other Things

The BFF can also make multiple calls in parallel to downstream services. Then return a single response to clients.

> When you are generating a larger portion of the web UI on the server-side (e.g using server-side templating), a BFF is the obvious place where this can be done

It can also simplify caching somewhat as you can place a reverse proxy in front of the BFF, allowing you to cache the results of aggregated calls (although you have to make sure you set your cache controls accordingly to ensure that the aggregated content's expiry is as short as the freshest piece of content in the aggregation needs it to be).

Also a BFF is good for an external party experience. If they use the general purpose API you might have to keep it around long term for a small subset of functionality.

> Typically microservices should be developed according to business verticals - catering for a specific industry.

Teams can use more server side changes and avoid the app store review process with a BFF.

perimeter concerns such as authentication/authorisation or request logging - should maybe be handled at an upstream layer.

> Backends For Frontends solve a pressing concern for mobile development when using microservices

The simple act of limiting the number of consumers they support makes them much easier to work with and change, and helps teams developing customer-facing applications retain more autonomy.

> Concentrate on your feature and specific usecases, before thinking about generic usage. No premature optimisation.

### The Problem with Frontend Developers writing Backend Code

The backend team has to develop a lightweight library which enabled writing the 'edge services' more easily, taking care of:

* alerting
* monitoring
* telemetry
* authentication
* rate limiting
* cleaning the incoming requests

## Sources

* [Sam Newman - Pattern: Backends For Frontends](https://samnewman.io/patterns/architectural/bff/)
* [The BFF Pattern](https://blog.bitsrc.io/bff-pattern-backend-for-frontend-an-introduction-e4fa965128bf)
* [BFF: Soundcloud](https://www.thoughtworks.com/insights/blog/bff-soundcloud)
* [AKF partners: Backend of Frontend](https://akfpartners.com/growth-blog/backend-for-frontend)
