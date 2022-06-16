---
author: ''
category: Book Summaries
date: '2022-05-06'
summary: ''
title: Fundamentals of Software Architecture
---

# Fundamentals of Software Architecture - An Engineering Approach

1. The industry does not have a good definition of a software architect
2. The scope and responsibility of a software architect is always expanding
3. The definition is ever changing as the software development ecosystem evolves

### Defining Software Architecture

* Architecture Decisions - conditions or constraints set by the architecture review board or chief architect
* Architecture Characteristics - availability, reliability, scalability, security, testability, learnability, etc.
* Design Principles - guidelines
* Structure - microservices, layered, micro kernel

### Expectations of an Architect

* Make architectural decisions - guide the team / department - do not make the choice
* Continually analyse the architecture
* Keep current with trends - developers keep up to date with the technology
* Ensure compliance - documented, communicated, 
* Diverse Exposure and Experience - Different technologies, frameworks, platforms and environments
* Business Domain Knowledge - solving a real world problem
* Interpersonal skills - strong leadership, mentor and effectively communicate ideas and architecture principles
* Navigate politics - almost every decision made will be challenged - product owners, project managers, business stakeholders and developers.

### Intersection of Architecture and...

Relationship between architecture and operations was formal and bureacratic.
Most companies outsourced to third parties with service level agreements (SLA), scale, responsiveness etc.

**Case study** Pets.com: money was spent on marketing and not infrastructure - the website was very slow. What was needed was elastic scale - the ability to quickly create more resources.

* Software architecture lacks the features of more mature engineering disciplines
* Estimation is bad - doesn't account for exploration and unknown unknowns

The architect must carefully consider the environment:

> For example, a microservices architecture assumes automated machine provisioning, automated testing and deployment, and a raft of other assumptions. Trying to build one of these architectures with an antiquated operations group, manual processes and little testing creates tremendous friction and challenges to success.

Architectural fitness functions: an objective integrity assessment of some architectural characteristic - iteratively improving on the solution leads to evolutionary computing.

#### Operations / DevOps

Many architectures assumed that architects could not control operations.
The design can be simplified if operations and architects work together.

#### Process

The process of software development has a bearing on the architecture. Software developed iteratively can have a fasted feedback loop. Allowing for more aggressive experimentation from architects.

A team started with a monolithic architecture because it was easy and fast to bootstrap, but now they need to move it to a more modern architecture - agile processes support this migration rather than heavy planning.

#### Data

Code and data are symbiotic.
How the application accesses the data has a great affect on noSQL database design.

### Laws of Software Architecture

1. Everything is Software Architecture is a Trade Off - If you think there isn't you probably haven't discovered it yet
2. Why is more important than how - ADR (Architecture Decision Records)

## 2. Architectural Thinking

The architectural viewpoint is different from the developers / engineers.

* Architecture vs design - collaboration of teams
* Wide breadth of technical knowledge - as well as depth
* Analysing and reconciling tradeoffs
* Understanding business drivers and translating to architectural concerns

### Architecture vs Design

* Architecture id done on whiteboards and development is done in practice a one way flow
* It is important to ensure it is 2 directional - a tight collaboration

### Technical Breadth

* An architects technical breadth is broader than a develop

All info can be seperated into:

- stuff you know: technologies, frameworks and languages (python, django, fastapi, dbs)
- stuff you know you don't know: stuff you have heard about with little expertise in (clojure)
- stuff you don't know you don't know - tech, frameworks and languages that are the perfect solution but you don't know about them

A developers early career focusses on stuff you know - the ideal place for hands on experience.
In also expands the middle section.
You have to maintain the stuff you know - you can become an expert and lose it.

As the career advances into an architecture role the technical breadth of knowledge is important.

Transitioning can cause disfunctions:

* An architect tries to maintain expertise in a wide area, succeeding in non and running themselves ragged.
* stale expertise - thinking your outdated information is still cutting edge

Frozen caveman antipattern - Generally, this anti-pattern manifests in architects who have been burned in the past by a poor decision or unexpected occurrence, making them particularly cautious in the future. While risk assessment is important, it should be realistic as well. Understanding the difference between genuine versus perceived technical risk is part of the ongoing learning process for architects.

### Analysing Tradeoffs

> Architecture is the stuff you can’t Google

The answer to every architecture problem is: _it depends_

Example: Using `publish-subscribe (topics) - kafka` vs `point-to-point (message queue) - rabbitmq`. Adding new consumers is easier with pub - sub, the producer is more decoupled (a change in it is not required in order for the new service to work)

> Programmers know the benefits of everything and the trade-offs of nothing. Architects need to understand both. - Rick Hickey

The downside of teh pub-sub is that anyone can now access the topic - data access, governance and security. If a rogue service did listen on a queue - a notification would be sent out about the loss of data. Also perhaps some services required different data - a different data contract.
Queues also know the volume of messages in a topic and can independently scale.

### Understanding Business Drivers

Understanding the business drivers of success and translating them into architecture requirements.

Every architect should be able to code and maintain technical breadth.
Beware the bottleneck trap - where an architect takes ownership of a critical path - since the architect is more theory and attending meetings - it becomes a bottleneck.

You need to delegate the critical path - to others on the team - and focus on something 3 iterations down the road.

Benefits:

1. Architect gets hands-on
2. Critical path is distributed
3. Architect can identify pain points

How to stay up to date for an architect:

1. Do POC's (proof of concepts) - compare results put architecture to the test - write the best production-quality code they can (it becomes reference for other team members) - gets practice writing quality well structured code
2. tackle low priorty - technical debt stories
3. Creating simple CLI tools to help the team - automated source code validation
4. Do code reviews

## 3. Modularity

Different platforms offer different reuse methods.
All support some way of grouping code together with modules.

Software systems module complex systems that move towards entropy (disorder).
Energy must be added to preserve order.

Sustainable code bases require order and consistency.

Mechanisms:

* java: package eg. `com.mycompany.customer` relates to customer
* .NET: namespace

In 1968, Edsger Dijkstr wrote a letter: "GOTO statement considered harmful" - non-linear leaping around code made it hard to debug.
This ushered in the era of structured programming languages

> Lumping a large number of classes together in a monolithic application may make sense from a convenience standpoint. However, when it comes time to restructure the architecture, the coupling encouraged by loose partitioning becomes an impediment to breaking the monolith apart

Matching package namespaces to folders in a filesystem prevented clashes.

### Measuring Modularity

#### Cohesion

> how related the parts are to one another

* functional cohesion - module contains everything it needs to function
* sequential cohesion - two modules interact - output of one should be input to another
* communication cohesion - two modules form a communication chain - add a record and send an email
* procedural cohesion - two modules must execute code in order
* temporal cohesion - modules related based on timing - startup
* logical cohesion - related logically not functionally eg. module that work on strings
* coincedental cohesion - unrelated modules but in the same source file (the most negative form)

Example:

class CustomerMaintenance:
    def add_customer():
    def update_customer():
    def get_customer():
    def notify_customer():
    def get_customer_orders():
    def cancel_customer_orders():

or separate into 2 classes?

class CustomerMaintenance:
    def add_customer():
    def update_customer():
    def get_customer():
    def notify_customer():

class OrderMaintenance:
    def get_customer_orders():
    def cancel_customer_orders():

* Is CustomerMaintenance expected to grow?
* Does OrderMaintenance require so much info about the customer that seperating the two modules would require a high degree of coupling?

The measures of cohesion focus on what fields are used by what functions.

A low `LCOM` score means high cohesion. A function only using a single field can be extracted along with the field into its own class.

#### Coupling

* Afferent coupling - measures the number of incoming connections to a code artifact
* Efferent coupling - measures the outgoing connections to other code artifacts

Abstractness is the ratio of abstract artifacts (abstract classes, interfaces, and so on) to concrete artifacts (implementation).

No abstractions - would be a single `main()` method

The flip side is too many abstractions for example: `AbstractSingletonProxyFactoryBean`

5000 lines of code in a `main()` method yields abstractness of almost `0`

Instability is the ratio of efferent coupling to the sum of both efferent and afferent coupling.

A class that calls many other classes - delegating work - the calling class has a high chance of breaking if one or more of the called methods break.

Distance from the main sequence = Abstractness (A) + Instability (I) - 1

> Always gives a ratio of 0 to 1

The main sequence can be graphed - the closer to the line the better balanced the class.

* Too far in the upper right: `one of uselessness` - code too abstract and difficult to use
* Lower left had corner: `zone of pain` - too much implementation and not enough abstraction becomes brittle and hard to maintain

Analysing code basis:

* unfamiliarity
* migration
* technical debt assessment

All code level metrics require interpretation

#### Connascence

> Two components are connascent if a change in one would require the other to be modified in order to maintain the overall correctness of the system

Static connascence - source-code level coupling. 

* Connascence of name - multiple components must agree on the name (system wide name changes)
* Connascence of type - agree on type
* Connascence of meaning / convention - True = 1 and False = 0
* Connascence of position - position in function signature
* Connascence of algorithm - agreeing on a hashing algorithm for example

Dynamic connascence - analyses calls at runtime

* Connascence of Timing - race conditions affecting the outcome
* Connascence of Values - values relating on one another. The more common and problematic case involves transactions, especially in distributed systems. When an architect designs a system with separate databases, yet needs to update a single value across all of the databases, all the values must change together or not at all.
* Connascence of Identity - The common example of this type of connascence involves two independent components that must share and update a common data structure, such as a distributed queue.


Architects should refactor from dynamic to static (strong to weak) - as there are modern tools to fix static connascence.

    Identity -> value -> timing -> execution -> position -> algorithm -> meaning -> type -> name

* strength
* locality - less damaging the closer the connescence is together - strong connescence within the same module represent less code problems
* degree - size of impact - break systems into pieces, minimise connescence across boundaries, maximise within

## 4. Architecture Characteristics Defined

An Architect must take many factors into account when designing a software solution:

* auditability
* performance
* security
* requirements
* data
* legality
* scalability

An architect contributes to the business requirements but also everything not related to the requirements in order to build the solution. Sometimes refered to as non-functional requirements.

Operational characteristics:

* availability
* continuity - disaster recovery
* performance - stress testing, response times, peak analysis, frequency of functions
* recoverability - business continuity
* reliability/safety - will it cost lives
* robustness - handling error and boundary conditions
* scalability - perform and operate with an increased number of requests

Structural Architectural Charcteristics:

* Configurability - Ability of end users to change aspects of software
* Extensibility
* Installability
* Leveragability - Reuse
* Localisation - support for mulitple languages
* Maintainability - ease to make changes and enhance
* Portability
* Supportability - level of logging and debugging
* Upgradability

Cross-cutting architecture characteristics:

* Accessibility - to all users even those with disabilties
* Archivability - customer accounts to be deleted
* Authentication - are they who they say they are
* Authorization - what a user can do
* Legal - POPIA, GDPR
* Privacy - Hide transactions from internal employees even (encrypted transactions)
* Security
* Supportability
* Usability/Achievability - training required for user to achieve goals

ISO (International Organisation of Standards):

* Performance efficiency
* Compatability
* Usability
* Reliability
* Security
* Maintainability
* Portability

Tradeoffs:

Improvements in security often lead to a negative impact on performance

> Never shoot for the best - always go for the least worst

If you can make changes to the architecture more easily, you can stress less about discovering the exact correct thing in the first attempt.



















## Source

* [Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/)