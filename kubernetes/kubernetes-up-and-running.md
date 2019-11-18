# Notes on Kubernetes Up and Running

## 1. Intro

Kubernetes is a Container orchestration APIs.

* Open source
* Developed by Google
* Introduced in 2014
* Proven infrastructure for realiable and scalable distributed systems

### Distributed System

More and more API's are delivered through various pieces or machines behind the scenes.
These API's are relied upon heavily and therefore should be highly reliable.
They should be highly available even during software rollout and maintenance.
They should also scale rapidly as more devices are connected.

The benfits of kubernetes:
* Velocity
* Scaling
* Abstracting your Infrastructure
* Efficiency

### Velocity

Speed to develop and deploy while maintaining a relaiable service

Achieved with:

* Immutability
* Declarative configuration
* Online self-healing system

#### Immutability

* Once an artifact is in the system it cannot change by user modification

With mutable systems changes are applied as incremental updates to an existing system. For example a package manager with `apt`, they are set of changes over time to a system.
These changes are often performed by many different people and have not been recorded.

An immutable system is an entirely new image - an update replaces the entire image.
There are no incremental changes.

Building a new image also allows for **rollback**, whereas shipping a new binary may make rollback impossible.

> Immutable container images are at the core of everything you build in Kubernetes

#### Declarative Configuration

Describing your application to kubernetes.

> Everything in kubernetes is a declarative configuration object representing the desired state of the system

Kubernetes job is to ensure the actual state matches the desired state

Declarative configuration is the opposite of imperitive configuration - where execution is based on a series of instructions.

> Declarative configuration can be understood before it is executed, it is far less error prone.

It can also use software development tools: source control, code review and unit testing.
Storing declarative config in source control is infrastructure as code.

**Rollback** is once again made easier, as you have a prior version of the running config. Impossible with imperitive instructions describing how to get from point A to point B, they rarely tell how to go the reverse way.

#### Self-Headling Systems

* Conitnuously takes action to ensure the current state matches the desired state.
* It will fight to maintain reliability
* Traditional repair - imperitive repair - requiring human intervention is expensive and slower.

For example asserting a desired state of 3 replicas, if you create a fourth replica. Hubernetes will destroy it.

Online self-healing systems improve developer velocity - time spent in operations and maintenance is spent on testing and development.

### Scaling

As your product grows - you need to scale your software and your team.

#### Decoupling

* Each component seperated by defined API's and load balancers
* Makes it easy to scale as increasing the size can be done without adjusting or reconfiguring any other layer of the system
* Decoupling allows development teams to focus on a small service
* Limit cross team communication overhead for deploying services

#### Easy Scaling

Containers are immutable and number of replicas is merely a number in declarative config.
Scaling can be done by simply changing this number or enabling autoscaling.

> Sometimes you need to scale up the cluster itself. Which is simply a task of adding a new machine of the same class and joining it to the cluster.

You can forecast growth on the aggregate of the services.
Teams can also share the underlying machines.

#### Scaling Development Teams with Microservices

* The ideal team size is a 2-pizza team (6 - 8 people)
    * Good knowledge sharing
    * Fast decision making
    * Common sense of purpose
* Larger teams suffer from
    * Issues of hierachy
    * Poor visibility
    * Infighting

Kubernetes provides the abstractions to build these microservice architecture:
* Pods - groups of containers
* Services - Load balancing and discovery isolating microservices from eachother
* Namespaces - isolation and access control
* Ingress - easy-to-use frontend that combine microservices into a single externalised API service area

#### Seperating Concerns for Consistency and Scaling

Seperating application operator from the cluster orchestration operator

The cluster orchestration operator concerns herself with the SLA (service level agreement) without worrying about the applications running on top of it.
The application operator concerns herself with the application running on top of the SLA, not how the SLA is achieved.

The OS is also decoupled from the container - so a small team of OS experts can scale to thousands of clusters.

> Devoting even a small team to managing an OS is beyond the scale of many organizations. In these environments, a managed Kubernetes-as-a-Service (KaaS) provided by a public cloud provider is a great option - Brendan Burns, “Kubernetes: Up and Running.”

There is a thriving ecosystem of companies and projects that help to install and manage Kubernetes - from doing it the hard way to fully managed kubernetes.

KaaS (Kubernetes as a Service) - lets small companies focus their energy on building software to support their work.
A larger organisation may want to manage the k8s cluster themselves for greater flexibility and cost saving

### Abstracting your Infrastrcuture

Too many cloud API's mirror the infrastructure that IT expects not the concepts - so VM's instead of applications.

Developers are consuming a high level API that Machines and need not concern themselves with individual machines.
This also lets us move to different providers as the api is common.

> Kubernetes has a number of plug-ins that can abstract you from a particular cloud

You also use `PersistentVolumes` and `PersistentVolumeClaims` to abstract yourself from certain storage implementations.

To achieve this portability you need to **avoid** cloud managed services:
* Amazons DynamoDB
* Azure's CosmosDB
* Google Cloud Spanner

Meaning you will need to deploy your and manage an openource solution like Cassandra, MySQL or MongoDB.

### Efficiency

Developers no longer need to think about machines, their applications can be colocated on the same machines without affecting the applications themselves.
Tasks can be packed tighter.

    Efficiency = useful work by machine / energy spent doing work

There are 2 costs: human cost and infrastructure cost.

Running a server incurs a cost: power usage, cooling, space and compute power. Idle CPU time is wasted.
The system administrator should ensure usage is at acceptable levels.
Kubernetes can ensure a high degree of usage across nodes.

A developer's development or staging environment can be quickly and cheaply created as a set of containers in a personal view of a kubernetes cluster - a namespace.

Every commit can also be tested on containers instead of VM's.

## 2. Creating and Running Containers

The applications that kuberentes manages ultimately accept input, manipulate data and return results.

We must first consider how to build the _container images_ that contain these programs.

Applications are made up of:
* language runtime
* libraries
* source code

In many cases your application relies on shared libraries `libc` or `libssl`.

These shared libraries cause issues when they are not on the production OS.

These shared libraries cause needless complexity between teams.

> Too often the state of the art for deployment involves running imperative scripts, which inevitably have twisty and byzantine failure cases

The container image provides immutability.

> Docker, the default container runtime engine, makes it easy to package an executable and push it to a remote registry where it can later be pulled by others

You can also run your own registry using open source or commercial systems

> Container images bundle a program and its dependencies into a single artifact under a root filesystem

Docker is the most popular image format, standardised by the Open Container Initiative as the OCI image format.
Kubernetes supports docker and OCI compatible images.














