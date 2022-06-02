---
author: ''
category: Book Summaries
date: '2022-04-26'
summary: ''
title: Software Architecture - The Hard Parts
---

## Software Architecture - The Hard Parts

> There is no single development, in either technology or management technique, which by itself promises even one order of magnitude (tenfold) improvement within a decade in productivity, in reliability, in simplicity. - Fred Brooks from “No Silver Bullet

> Don’t try to find the best design in software architecture; instead, strive for the least worst combination of trade-offs.

For many in architecture, data is everything. Every enterprise building any system must deal with data, as it tends to live much longer than systems or architecture, requiring diligent thought and design

10 years ago - the architecture pattern was orchestration-driven - service oriented infrastructure.
Open source operating systems became commercially free and operationally free - using ansible along with emerging tools like kubernetes.

Microservices:

* domain-driven design
* limiting scope to a single function
* single model
* distributed system

### The Importance of Data Architecture

* Operational data (OLTP) - used frequently for transactions
* Analytical data (OLAP) - used for analysis, strategy and predictions

### Architectural Decision Records

ADR's - architectural design records - describe an architectural decision

* ADR: A short noun phrase containing the architecture decision
* Context: In this section of the ADR we will add a short one- or two-sentence description of the problem, and list the alternative solutions.
* Decision: In this section we will state the architecture decision and provide a detailed justification of the decision.
* Consequences: In this section of the ADR we will describe any consequences after the decision is applied, and also discuss the trade-offs that were considered.

### Architecture Fitness Functions

Architectural governance - ensure implemented solution abides by design.
Devops spawned - automating manual chores - automation and feedback
Continuous integration makes integration phase of code faster - the bigger the project the more painful the integration
Linux, open source and virtual machines.
Code reviews.

> Security needs to be part of the deployment pipeline

Architects should not form a cabal and retreat to an ivory tower to build an impossibly complex, interlocking set of fitness functions that merely frustrate developers and teams.

A checklist before deploying code.

### Architecture vs Design: Keeping Definitions Simple

* service - collection of functionality deployed as a single executable
* coupling - two artifacts are coupled if a change in one requires a change in another
* component - building block of application with a certain function
* synchronous communication - called must wait for response before proceeding
* asynchoronous communication - caller does not wait - the caller can be notified by another channel
* orchestrated coordination - a service has primary responsibility to coordinate workflow
* choreographed coordination - lacks an orchestrator - services coordinate
* Atomicity - A consistent state at all times opposite to eventual consistency
* Contract - Interface between 2 software parts

### Introducing the SysOps Saga




## Source

* [“Software Architecture: The Hard Parts” - Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)
