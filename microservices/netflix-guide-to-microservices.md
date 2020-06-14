## What Microservices are Not

### Monolithic code base

* Everyone contributes to a single codebase
* Changes and errors were difficult to diagnose
* A Week troubleshooting memory leaks

### Monolithic Database

* On epeice of hardware running 1 big database
* When it went down, everything went down
* Looking for bigger hardware to vertically scale the application
* Adding a column to a table was a big cross functional process

## What is a Microservice

Developing a single application as a suite of small services, each running in its own process.
Communicating with lightweight mechanisms often an HTTP resource API. - Martin Fowler

* Seperation of concerns
* scalability - lend themselves to horizontal scaling and workload partitioning
* Virtualisation and elasticity - automated operations and on demand provisioning

### Edge Services

ELB (Elastic Load Balancer) -> Zuul Proxy layer (dynamic routing) -> Core API

### Middle Tier and Platform Services

* AB testing service
* Subscriber service
* Recommendation service
* Platform services: Routing, configuration and crypto
* Persistence: Cache and DB

Data is typically stored in your persistence layer

The microservice is an abstraction - containing all these things:

* Service client
* Persistence
* Cache client

It is not just the stateless application

## Challenges and Solutions

* Dependency
* Scale
* Variance
* Change

## Dependency

### Intra-service requests

* Network or latency issues
* service you are calling is not fast and efficient

> A single service failing could cascade issues

To prevent this netflix created hysterix:

* structured way for handling timeouts and retries
* fallback to show some data
* isolated thread pools

Service should function even when dependencies go away

### Persistence

[CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem) says it is impossible for a distributed datastore to simultaneously provide 2 of these:

* Consistency - every read receives the most recent write or error
* Availability - every read receives a response
* Partition Tolerance - System continues to operate despite arbitrary number of dropped messages

Netflix chose Cassandra and wanted *eventual consistency*

### Infrastructure

> Everything fails

Don't put all your eggs in one basket

3 Regions were used

## Scales

Stateless service
* no cache, no database
* frequently accessed metadata
* No instance affinity - a customer will use various instances
* Loss of a node is a non-event (ephemeral)
* Recovery is very quick

Autoscaling: Min, max and metric to use when scaling your group

Advantages of autoscaling:

* compute efficiency (using on-demand capacity)
* Node failures are not big deals
* Traffic spikes, DDOS or performance bug allows you to absord that change and figure out what happened

Surviving instance failure - chaos monkey

Stateful service
* Database and caches
* Avoid storing business logic and state within one application
* Loss of a node is a notable event

Redundancy is fundamental - 2 kidneys, 2 lungs

EVCache - relying on it at 800k - 1M Request Per Second

## Variance

Variety in your architecture

The more variance you have the greater your challenges - increases complexity

### Operational Drift

Unintentional:

* Alert thresholds
* timeouts, retries and fallbacks
* throughput (RPS)

Autonomic nervous system - body just takes care of - don't need to think about breathing or how to digest food.
Make these processes subconscious.

Use continuous learning and automation - this is how knowledge becomes code.

    Incident -> Resolution -> Review -> Remediation -> Analysis -> Best Practice -> Automation -> Adoption

Production ready checklist (automation and continuous improvement behind it):

* Alerts
* autoscaling
* chaos
* consistent naming
* ELB config
* Healthcheck
* Immutable machine images
* Squeeze testing
* timeouts, retries and fallbacks

### Polyglot and Containers

Intentional - people adding new programming languages into the microservices architecture

The paved road (best of breed tech that worked best) - automation and integration baked in - so developers could be agile.
Then there was the rocky road new tech and docker.

Cost of variance:

* productivity tooling
* different tooling for memory and cpu on containers
* Base image fragmentation - more specialised
* learning curve - things break in interesting and new ways


Key points:

* Raise the awareness of costs
* prioritise by impact
* seek reusable solutions

Integrated delivery:

* Test out the code changes with some real traffic and determine if the code is better
* Staged deployments - 1 region at a time


Conway's Law

> Organisations which design systems are constrained to produce designs which  are copies of the communication structures of these organisations

Any piece of software reflects the organisational structure that produced it

This is not solutions first, it was organisation first.

Organisation should be refactored based on the value or way we deliver value.




