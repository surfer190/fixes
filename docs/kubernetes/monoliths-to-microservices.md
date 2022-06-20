---
author: ''
category: Kubernetes
date: '2020-01-06'
summary: ''
title: Monoliths To Microservices
---
## Monoliths to Microservices

# 1. Just Enough Microservices

## What are Microservices?

* Independently deployable services modeled around a business domain
* A microservice architecture is a network of communicating microservices
* They are a type of SOA (Service oriented Architecture)
* Technology agnostic
* expose business capabilities via network endpoints
* Databases are hidden - encapsulate data storage and retrieval via well defined interfaces

### Independently Deployable

* Deploy to production on it's own

> Get into the habit of releasing changes to a single microservice without having to deploy anything else

To allow for independent deployablility the services need to be _loosely coupled_

We need explicit, well-defined and stable contracts between services

Sharing of databases is especially problematic

### Modelled around a Business Domain

Making changes across the process boundary is expensive - make them as infrequently as possible.

> If you need to make a change to two services to roll out a feature, and orchestrate the deployment of these two changes, that takes more work than making the same change inside a single service (or, for that matter, a monolith)

A traditional 3-tiered architecture MVC - Model (Database), Controller (Backend) and View (Presentaiton) layer.
Each layer is managed by a different team.

For a single change all teams need to make changes an they need to be deployed in the correct order.

> Any organization that designs a system…will inevitably produce a design whose structure is a copy of the organization’s communication structure - Conway's Law

People are grouped on their core competencies.
We need to group poly-skilled teams - to reduce hand-offs and silos.

High cohesion of related technology, but low cohesion of business functionality.

Another architecutre is around the service offered: Customer, Catalog and Recommendation service

All 3 tiers are in the single service - a bit of application logic, some data storage and UI.

So our teams are organised around the business domain.

### Own their Data

Microservices should not share databases.
Internal implementations can change for arbitrary reasons - the public facing contract is more stable.

Hiding the database ensures reduced coupling.

### What Advantages can Microservices Bring?

* Independence allows for improved scale and robustness.
* More developers, without getting in eachothers way
* Easier for developers to know their part of the system - process isolation
* Flexibility

### What Problems do they Create

> Service-oriented architecture became a thing partly because computers got cheaper, so we had more of them. Rather than deploy systems on single, giant mainframes, it made more sense to make use of multiple cheaper machines

* Communication over a network is not isntantaneous - latency of microservices.
* These latencies are unpredictable
* (DB) Transactions become difficult
* Services can and will fail
* Wealth of microservice friendly technology which can easily be used badly 

All systems we classify as monoliths are also _distributed systems_

> Microservices buy you options - they have costs - are those costs worth it

Our User Interfaces should also be broken up into micro services

> Adopting any new technology will have a cost

> There is far too much technical snobbery out there toward some technology stacks that can unfortunately border on contempt for people who work with particular tools. Don’t be part of the problem!”

Size - have as small an interface as possible

True technology companies combine the business and IT silo's

> Product owners now work directly as part delivery teams, with these teams being aligned around customer-facing product lines, rather than around arbitrary technical groupings

Microservices make this shift easier.

> Reducing services that are shared across multiple teams is key to minimizing delivery contention

## The Monolith




