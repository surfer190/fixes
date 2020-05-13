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

## Container Images

Container Image - a binary package that encapsulates all the files necessary to run a program inside an OS container

You will either build a container image form your local filesystem or download an existing image from a container registry.

### Docker Image Format

* Most popular and widespread image format
* Uses layers: each layer adds, removes or modifies files on from the preceding layer - example of an overlay filesystem
* Convert implementations of overlay are: `aufs`, `overlay` and `overlay2`

Docker began standardising the image format with the OCI (Open Container Initiative) achieving 1.0 in mid 2017.

Container images are combined with a container configuration file - containing the instructions to set up the container and the application entry point

The container configuration contains:
* information on networking setup
* namespace isolation
* resource constraints (cgroups)
* `syscall` restrictions

The container root file system and configuration file are bundled using the Docker Image format.

There are 2 types of containers:
* System Containers
* Application containers

System containers mimic VM's (virtual machines) - often running a full boot process. They contain system services like: `ssh`, `cron` and `syslog`.

When docker was new these containers were common - _I think we are talking LXC here_

> Application containers can commonly run a single program

Running a single program (or process) per container might seem like a constraint, it really provides the granularity for composing scalable applications. A design philosophy leveraged heavily by pods.

Linux Containers (LXC) are System containers, while docker is a process-based application container.

### Building Application Images with Docker

Container orchestration systems (like kubernetes) are focused on building and deploying distributed systems made up of application containers.

#### Dockerfiles

A dockerfile can be used to automate the creation of a docker image.

For example a node.js application (any other dynamic language like python or ruby would work the same)

The simplest nodejs applications contain a `package.json` and a `server.js` file.

**package.json**

    {
        "name": "simple-node",
        "version": "1.0.0",
        "description": "A sample simple application for Kubernetes Up & Running",
        "main": "server.js",
        "scripts": {
            "start": "node server.js"
        },
        "author": ""
    }

**server.js**

    var express = require('express');

    var app = express();
    app.get('/', function (req, res) {
        res.send('Hello World!');
    });
    app.listen(3000, function () {
        console.log('Listening on port 3000!');
        console.log('  http://localhost:3000');
    });

Run `npm install express --save`

We also need a `Dockerfile` the recipe for how to build a container image and a `.dockerignore` a list of files and folders to ignore when copying files to an image.

**.dockerignore**

    node_modules

**Dockerfile**

    #Start from a Node.js 10 (LTS) image 
    FROM node:10

    # Specify the directory inside the image in which all commands will run 
    WORKDIR /usr/src/app

    # Copy package files and install dependencies 
    COPY package*.json ./
    RUN npm install

    # Copy all of the app files into the image 
    COPY . .

    # The default command to run when starting the container 
    CMD [ "npm", "start" ]

* Every Dockerfile builds on a `base image` in this case `node:10` available on dockerhub
* We need to initialise the dependencies for the application
* Copy the program files across
* We also need to specify the entry point...the command for the process based container to run

Create (Build) the image with:

    docker build -t simple-node .

This makes `simple-node` live in our local docker registry, the true power of docker comes from sharing images across the community

When you want to run the image (create a container):

    docker run --rm -p 3000:3000 simple-node


#### Optimising Image Sizes

**Layer Deletions**

There are some gotchas that lead to images that are too large.

It is important to remember that files removed by subsequent layers are still present but inaccessible.

    └── layer A: contains a large file named 'BigFile'
        └── layer B: removes 'BigFile'
            └── layer C: builds on B by adding a static binary

The problem is that `BigFile` still exists and will still move around the network when pulling and pushing images

**Changes early on in Dockerfile**

Another pitfall is image caching and building

> Every layer is an independent delta (change) from the layer below it

So every change you make, changes the layers below it.

    └── layer A: contains a base OS
        └── layer B: adds source code server.js
            └── layer C: installs the 'node' package

vs

    └── layer A: contains a base OS
        └── layer B: installs the 'node' package
            └── layer C: adds source code server.js

Both of these images will work the same on first pull, however changing `server.js` will result in only that change being pushed or pulled in the second case.

In the first case both layers need to be pushed and pulled.

> You want to order your layers from least likely to change to most likely to change in order to optimize the image size for pushing and pulling

#### Image Security

* Don't build containers with passwords baked in - on any layer
* Secrets and images should never be mixed

### Multistage Image Builds

Doing compilation as part of the construction of the container image.
It feels natural and is easy, but it leaves unnecessary dev tools inside your image - slowing down deployments.

With multistage builds, a Dockerfile can produce multiple images.
Each image is a stage.
Artifacts can be copied from preceding stages to the current stage.

Lets us look at `kuard` a react.js frontend and go backend.

**Single stage**

Dockerfile produces a container image containing a static executable, go dev tools, source code of the application and react js code.
Total size: _500MB_

    FROM golang:1.11-alpine

    # Install node and npm
    RUN apk update && apk upgrade && apk add --no-cache git nodejs bash npm

    # Get dependencies or go part of the build
    RUN go get -u github.com/jteewen/go-bindata/...
    RUN go get github.com/tools/godep

    WORKDIR /go/src/github.com/kubernetes-up-and-running/kuard

    # copy all sources in
    COPY . .

    # Set of variables the build script expects
    ENV VERBOSE=0
    ENV PKG=github.com/kubernetes-up-and-running/kuard
    ENV ARCH=amd64
    ENV VERSION=test

    # Do the build. The script is part of incoming sources.
    RUN build/build.sh

    CMD [ "/go/bin/kuard" ]

**Multistage**

This dockerfile produces 2 images. The first is the build image containing go compiler, react.js and source code. The second is the deployment image containing the compiled binary.
Multistage builds:
* decrease container side
* speed up deployments

Total size: _20MB_

    # Stage 1: Build
    FROM golang:1.11-alpine as build

    # Install Node and NPM
    RUN apk update && apk upgrade && apk add --no-cache git nodejs bash npm

    # Get dependencies for go as part of the build
    RUN go get -u github.com/jteeuwen/go-bindata/...
    RUN go get github.com/tools/godep

    WORKDIR /go/src/github.com/kubernetes-up-and-running/kuard

    # Copy source
    COPY . .

    # Set of variables
    ENV VERBOSE=0
    ENV PKG=github.com/kubernetes-up-and-running/kuard
    ENV ARCH=amd64
    ENV VERSION=test

    # Do the build
    RUN build/build.sh

    # Stage 2: Deployment
    FROM alpine

    USER nobody:nobody

    COPY --from=build /go/bin/kuard /kuard

    CMD [ "/kuard"]

You can build and run the image with:

    docker build -t kuard .
    docker run --rm -p 8080:8080 kuard

### Storing Images in a Remote Repo

* k8s relies on images in the pod manifest are available to every machine in a cluster
* Store docker images in a remote repository
* Choose public or private registry

Authenticate to the registry with:

    docker login

You can tag the image with the target docker registry and give another identifier after the `:`

    docker tag kuard gcr.io/kuar-demo/kuard-amd64:blue

Once tagged you can push the image to the remote

    docker push gcr.io/kuar-demo/kuard-amd64:blue

### The Docker Container Runtime

Kubernetes provides an API for describing an application deployment but relies on a container runtime to setup an application container that work on the target OS.

On linux that means configuring `cgroups` and `namespaces`

The interface to the runtime is the `Container Runtime Interface` (CRI), it is implemented by a number of programs:

* `containerd-cri` build by Docker
* `cri-o` build by Red Hat

> Kubernetes containers are launched by a daemon on each node called the _kubelet_

It is easier to use `docker` cli however:

    docker run -d --name kuard --publish 8080:8080 gcr.io/kuar-demo/kuard-amd64:blue

`-p` published the port from the container to the host
`-d` means detach or run as a daemon

Docker Allows us to limit the amount of resources used by an application by exposing the underlying `cgroup` tech of the linux kernel

    docker run -d --name kuard --publish 8080:8080 kuard-multistage

Containers allow us to restrict resource utilisation - ensuring fair usage

Stop and remove the container

    docker stop kuard
    docker rm kuard

#### Limiting Memory Usage

You can limit resource usage with `--memory` and `--memory-swap` flags

    docker run -d --name kuard --publish 8080:8080 --memory 200m --memory-swap 1G  kuard-multistage

> If the program in the container uses too much memory, it will be terminated

#### Limiting CPU Usage

Use the `--cpu-shares` flag

    docker run -d --name kuard --publish 8080:8080 --memory 200m --memory-swap 1G --cpu-shares 1024 kuard-multistage

### Clean Up

You can delete an image with

    docker rmi <image_name>

> Unless you explicitly delete an image it will live on your system forever, even if you build a new image with an identical name

Perform a general cleanup (use with care):

    docker system prune

Another way is to run a garbage collector [docker-gc](https://github.com/spotify/docker-gc) on cron

Containers:

* clean abstractions applications become easier to build, deploy and distribute (not test?)
* Isolation between containers on same machine - avoiding dependency conflict (virtualenv's do this)

# 3. Deploying a Kubernetes Cluster

Transform your container into a complete, reliable and scalable distributed system.

For that you need a kubernetes cluster.

Better to let the clouds manage kubernetes for you. If not, use `minikube`.
It only creates a single node cluster.

## Azure: Deploying a k8s cluster

Using **AKS** - [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough)

Create the resource group:

    az group create --name=kuar --location=westus

Create the cluster:

    az aks create --resource-group=kuar --name=kuar-cluster --node-vm-size=Standard_D1  --generate-ssh-key

Get credentials for the cluster:

    az aks get-credentials --resource-group=kuar --name=kuar-cluster

## GCP: Deploying a k8s cluster

Using **GKE** - [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster)

You need the `gcloud` tool

Set the default zone:

    gcloud config set compute/zone us-west1-a

Create the cluster:

    gcloud container clusters create kuar-cluster

When the cluster is ready, get the credentials:

    gcloud auth application-default login

## AWS: Deploying a k8s cluster

Using **EKS** - Elastic Kubernetes Service

Use the [`eksctl` tool](https://eksctl.io)

Create a cluster

    eksctl create cluster --name kuar-cluster

## Installing Kubernetes Locally using Minikube

For development only as is a single node, does not provide reliability.

    minikube start

This creates a local vm, provisions kubernetes and creates a local `kubectl` configuration that points to the cluster

When you are done you can stop and delete the vm with:

    minikube stop
    minikube delete

## Running Kubernetes in Docker

You can simulate a kubernetes cluster with [kind: kubernetes in docker](https://kind.sigs.k8s.io/)

## The Kubernetes Client

The official kubernetes client is `kubectl`

`kubectl` can manage: pods, replicasets and services. You can also explore the overall health of a cluster.

### Checking Cluster Status

Get version

    kubectl version

    Client Version: version.Info{Major:"1", Minor:"16", GitVersion:"v1.16.2", GitCommit:"c97fe5036ef3df2967d086711e6c0c405941e14b", GitTreeState:"clean", BuildDate:"2019-10-15T23:43:08Z", GoVersion:"go1.12.10", Compiler:"gc", Platform:"darwin/amd64"}
    Server Version: version.Info{Major:"1", Minor:"16", GitVersion:"v1.16.2", GitCommit:"c97fe5036ef3df2967d086711e6c0c405941e14b", GitTreeState:"clean", BuildDate:"2019-10-15T19:09:08Z", GoVersion:"go1.12.10", Compiler:"gc", Platform:"linux/amd64"}

Tells you the client and server version. They can be different versions as long as they are within 2 major versions.

Get componentstatuses:

    kubectl get componentstatuses

    NAME                 AGE
    scheduler            <unknown>
    controller-manager   <unknown>
    etcd-0               <unknown>

* `controller-manager` - regulates behaviour ensures components are healthy
* `scheduler` - places different pods on different nodes
* `etcd` server - storage for api objects

### List Worker Nodes

    kubectl get nodes

    NAME       STATUS   ROLES    AGE   VERSION
    minikube   Ready    <none>   30m   v1.16.2

* `master` nodes contain the API server and scheduler
* `worker` nodes are where your container run

Get info about a specific node:

    kubectl describe nodes <nodename>
    kubectl describe nodes minikube

Get the:
* Operations
* Disk and Memory Space
* Software info: Docker, kubernetes and Linux Kernel versions
* Pod Information - You can get name, CPU and memory of each pod - requests and limits also tracked

## Cluster Components

Many of the components that make up the kubernetes cluster are deployed using kubernetes itself.
They run in the `kube-system` namespace

### Kubernetes Proxy

* Responsible for routing traffic to load balanced services
* Must be present on every node (uses `Daemonset` for this)

View the proxies:

    kubectl get daemonSets --namespace=kube-system kube-proxy

### Kubernetes DNS

* Naming and discovery for services
* DNS service is run as a `deployment`

Get the DNS deployment:

    kubectl get deployments --namespace=kube-system coredns

Get service that load balances dns:

    kubectl get services --namespace=kube-system kube-dns
    
    NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
    kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   28h

> It might be `core-dns`, `coredns` or `kube-dns` on other systems. Kubernetes 1.12 moved from `kube-dns` to `core-dns`

If you check a container in a cluster the cluster ip `10.96.0.10` will be in `/etc/resolv.conf`

## Kubernetes UI

The final component is the GUI. A single replica managed by kubernetes.

You can see it with:

    kubectl get deployments --namespace=kube-system kubernetes-dashboard

> On `minikube version: v1.5.0` it is in its own namespace

    kubectl get deployments --namespace=kubernetes-dashboard kubernetes-dashboard

and

    kubectl get services --namespace=kube-system kubernetes-dashboard

You can use `kubectl proxy` to access the UI

You can then access the service at: [http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/)

# 4. Common Kubectl Commands

## Namespaces

* A folder to organise objects
* By default uses the `default` namespace
* Can specify a namespace with `--namespace=xxx`
* Interacting with all namespaces use `--all-namespaces`

## Contexts

* Used to change the default namespace more permanently
* Recorded in `kubectl` file

### Kubectl File

* Stored in `$HOME/.kube/config`
* Stores location and how to authenticate to cluster

Create a context with a different namespace:

    kubectl config set-context my-context --namespace=mystuff

To use this context:

    kubectl config use-context my-context

> Contexts can also be used to manage different clusters or different users on clusters Use the `--users` or `--clusters` flag with `set-context`

## Viewing Kubernetes API Objects

Everything in kubernetes is a Restful resource - _kubernetes objects_

Each object exists at a unique path: eg. `https://your-k8s.com/api/v1/namespaces/default/pods/my-pod`

`kubectl` uses this api

### Get

You get a resource with:

    kubectl get <resource-name> <obj-name>

Get more details with `-o wide`

To view the complete resource as json `-o json`

To use `awk` to manipulate the output use the `--no-headers` flag

You can also use the [`jsonPATH` (JSON XPath)](https://restfulapi.net/json-jsonpath/) query language to get specific elements:

    kubectl get pods kubernetes-dashboard-57f4cb4545-9m2mx -o jsonpath --template={.status.podIP} --namespace=kubernetes-dashboard

### Describe

To get more details info

    kubectl describe pods kubernetes-dashboard-57f4cb4545-9m2mx --namespace=kubernetes-dashboard

## Creating, Updating and Destroying Kubernetes Objects

Objects in kubernetes are represented as `yaml` or `json`

For example a simple object in `obj.yaml` you can create the object with:

    kubectl apply -f obj.yaml

You use the same command to update:

    kubectl apply -f obj.yaml

If an object is unchanged, nothing happens.
See what will happen in a `--dry-run`

You can do interactive edits (not infrastructure as code) with:

    kubectl edit <resource-name> <object-name>

The `apply` command records history:
* edit-last-applied
* set-last-applied
* view-last-applied

    kubectl apply -f myobj.yaml view-last-applied

When you want to delete an object:

    kubectl delete -f obj.yaml

you can also delete with:

    kubectl delete <resource-name> <obj-name>

## Labeling and Annotating Objects

Add a label to a pod:

    kubectl label pods bar color=red

Remove a label from a pod:

    kubectl label pods bar color-

## Debugging Commands

View the logs for a container:

    kubectl logs <pod-name>

If you have mulitple containers in your pod use the `-c` flag. If you want to follow:

    kubectl logs <pod-name> -f

To `exec` commands in a running container:

    kubectl exec -it <pod-name> -- bash

If you don't have a terminal in the running container, you can attach to the running process:

    kubectl attach -it <pod_name>

`attach` is similar to `kubectl logs` except you can send to input to the running process

Copy files from within  container:

    kubectl cp <pod-name>:</path/to/file> <path/to/local>

To access your pod via the network, you can use the `port-forward` command to forward your local traffic to the pod. If it isn't availabel publicly.

    kubectl port-forward <pod-name> 8080:80

> Forwards traffic on local machine `8080` to remote container on port `80`

You can also port forward service:

    kubectl port-forward services/<service-name> 8080:80

> A forwarded service only goes to a single pod ever - they will not go through the service load balancer

See cluster use of resources:

    kubectl top nodes

or

    kubectl top pods

## Command Autocompletion

Install autocompletion with:

    brew install bash-completion

Activate it temporarily with:

    source <(kubectl completion bash)

activate it permanently with by putting that command in `~/.bashprofile`

## Getting Help

    kubectl help

or specific:

    kubectl help <command>
    kubectl help get

## Visual Code Extensions

There is also a visual studio code extension

# 5. Pods

Colocate multiple applications into a single atomic unit on a single machine.

An example is 2 pods - 1 web server and 1 git sync using the same filesystem

It first it might seem tempting to wrap everything in a single container - but that would be a bad choice:
* they have different requirements for resource usage - web server is user facing, git synchronizer is not.
* Isolation: if git synchronizer has a memory leak

It makes sense however to keep them together.

> A "Pod" is a group of whales

## Pods in Kubernetes

A pod represents a collection of application containers and volumes running in the same execution environment.

Pods are the smallest deployable artifact in k8s.

All the containers in a pod always land on the same machine.
Each container has its own `cgroup` but share a number of linux namespaces.

Applications in the same pod:
* share the same ip address and port space
* have the same hostname
* can communicate over native interprocess communication - system V IPC or posix message queues

Containers not in the same pod are isolated from each other - different ips and different hostnames.

> Containers on the same node and different pods may as well be on different servers

## Thinking with Pods

What should I put in a pod?

Symbiotic things. Things that scale together.

Wordpress and a MySQL Database are not symbiotic. If wordpress and the database land up on different machines they can still communicate over a network connection.
You also wouldn't scale wordpress and the database together.
Wordpress is mostly stateless - so scaling it is easy.
Scaling a MySQL database is much harder - you would most likely dedicate more resources to a single pod.
Their scaling strategies are incompatible.

The question to ask yourself is:

> Will these containers work correctly if they land on different machines

If the answer is *no*, a pod is the correct grouping for the containers.

When containers interact via a filesystem it is impossible for them to operate on different machines.

### Pod Manifest

A pod manifest is a text file representation of the kubernetes API object.

> Kubernetes strongly uses _declarative configuration_

Meaning you write down your desired state and a service ensure it gets the actual state to equal the desired state

The kubernetes API accepts the pod manifests and stored them persistently in `etcd`

The scheduler ensures the pods are deployed on a node and distributed amongst nodes.
Once scheduled to a node pods don't move - they must explicitly be destroyed and rescheduled.

`ReplicaSets` are better suited to running multiple instances of a pod.

#### Creating a Pod

    kubectl run kuard --generator=run-pod/v1 --image=gcr.io/kuar-demo/kuard-amd64:blue
    pod/kuard created

Get the pod status with:

    kubectl get pods
    NAME    READY   STATUS    RESTARTS   AGE
    kuard   1/1     Running   0          2m7s

Delete the pod

    kubectl delete pods/kuard

#### Creating a Pod Manifest

* Can be written in JSON or Yaml
* Yaml preferred as easier to read and you can add comments
* Should be treated the same way as source code

* `metadata` describes the pod
* `spec` describes the volumes and containers that will run in the pod

**kuard-pod.yaml**

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard
    spec:
      containers:
        - image: gcr.io/kuar-demo/kuard-amd64:blue
          name: kuard
          ports:
            - containerPort: 8080
              name: http
              protocol: TCP

to launch a single instance run:

    kubectl apply -f kuard-pod.yaml

Kubernetes will schedule that pod to run on a healthy node in the cluster, where it is monitored by the `kubelet` daemon process.

#### Listing Pods

    kubectl get pods
    NAME    READY   STATUS    RESTARTS   AGE
    kuard   1/1     Running   0          24m

A `Pending` status indicates that a pod has been submitted but hasn't been scheduled

#### Pod Details

    kubectl describe pods kuard
    
Basic info:

    Name:         kuard
    Namespace:    default
    Priority:     0
    Node:         minikube/192.168.64.3
    Start Time:   Fri, 06 Dec 2019 06:05:50 +0200
    Labels:       run=kuard
    Annotations:  <none>
    Status:       Running
    IP:           172.17.0.6
    IPs:
        IP:  172.17.0.6

Containers:

    Containers:
      kuard:
        Container ID:   docker://d44acd72e40d0f0cbfae5a734493417e15b09a28aae0b67a46355cdfb3e98605
        Image:          gcr.io/kuar-demo/kuard-amd64:blue
        Image ID:       docker-pullable://gcr.io/kuar-demo/kuard-amd64@sha256:1ecc9fb2c871302fdb57a25e0c076311b7b352b0a9246d442940ca8fb4efe229
        Port:           <none>
        Host Port:      <none>
        State:          Running
          Started:      Fri, 06 Dec 2019 06:06:05 +0200
        Ready:          True
        Restart Count:  0
        Environment:    <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from default-token-mbn5b (ro)

Conditions:

    Conditions:
      Type              Status
      Initialized       True 
      Ready             True 
      ContainersReady   True 
      PodScheduled      True 

Volumes:

    Volumes:
      default-token-mbn5b:
        Type:        Secret (a volume populated by a Secret)
        SecretName:  default-token-mbn5b
        Optional:    false

Events:

    Events:
      Type    Reason     Age        From               Message
      ----    ------     ----       ----               -------
      Normal  Scheduled  <unknown>  default-scheduler  Successfully assigned default/kuard to minikube
      Normal  Pulling    3d8h       kubelet, minikube  Pulling image "gcr.io/kuar-demo/kuard-amd64:blue"
      Normal  Pulled     3d8h       kubelet, minikube  Successfully pulled image "gcr.io/kuar-demo/kuard-amd64:blue"
      Normal  Created    3d8h       kubelet, minikube  Created container kuard
      Normal  Started    3d8h       kubelet, minikube  Started container kuard

#### Deleting a Pod

    kubectl delete pods/kuard

or using the file

    kubectl delete -f kuard-pod.yaml

A pod is not immediately killed, the pod is put in a `Terminating` state.
The _grace period_ is 30 seconds. 

> Important to note that when you delete a pod, any data stored in the containers associated with that pod will be deleted. If you want to persist data across multiple instances of a pod you need to use `PersistentVolumes`

### Accessing your Pod

**Using port forwarding**

    kubectl port-forward kuard 8080:8080

A secure tunnel is created from your local machine to the kubernetes master to the pod running on worker nodes.

You can then access the pod via web interface a:

    localhost:8080

**Getting logs**

    kubectl logs kuard

or follow with:

    kubectl logs kuard -f

Get logs for the previous instance of a container if it is restarting always:

    kubectl logs kuard --previous

> In production it is better to use log aggregation like `fluentd` and `elasticsearch`

**Running commands in your container**

    kubectl exec kuard date

or get an interactive session:

    kubectl exec -it kuard ash

**Copying files to and from containers**

Copy from pod to local

    kubectl cp <pod-name>:/captures/capture3.txt ./capture3.txt

Copy from local to pod

    kubectl cp $HOME/config.txt <pod-name>:/config.txt

> You really should treat the contents of a container as immutable

### Health Checks

> A process in kubernetes is automatically kept alive with a _process health check_

This ensures your main process is always running

A simple process check is insufficient in the case of a deadlocked process- which cannot server requests.
To address this Kubernetes has a healthcheck for application _liveness_ - application specific logic - like loading a webpage.

Liveness healthchecks are defined in your pod manifest.

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard
    spec:
      containers:
        - image: gcr.io/kuar-demo/kuard-amd64:blue
          name: kuard
          livenessProbe:
            httpGet:
              path: /healthy
              port: 8080
            initialDelaySeconds: 5
            timeoutSeconds: 1
            periodSeconds: 10
            failureThreshold: 3
          ports:
            - containerPort: 8080
              name: http
              protocol: TCP

An `httpGet` probe is used to do a `HTTP GET` to `/healthy` on port `8080`:
* `initialDelaySeconds: 5` - starts 5 seconds after the container starts
* `timeoutSeconds: 1` - probe must respond within 1 second
* `periodSeconds: 10` - test is performed every 10 seconds
* a status code equal to or greater than 200 and less than 400 to be considered successful

> Default response to a failed liveness probe check restarts the pod. The pods `restartPolicy` can be `Always`, `OnFailure`(restart only on liveness failure or non-zero process exit) or `Never`

**Readiness probe**

Liveness determines if an application is running properly.
Readiness determines if an application is ready to serve user requests

Containers that fail readiness are removed from service load balancers

#### Types of Health Checks

* HTTP checks
* TCP Socket: `tcpSocker` - databases, non-HTTP api's
* `exec` probes - only if a non-zero exit is received does it fail

### Resource Management

Kubernetes provide improvements to image packaging and reliable deployment

Equally important is increasing the overall utilisation of nodes in a cluster

The cost of a machine is constant whether idle or fully loaded.

Ensuring machines are at high levels of usage increases the efficient of every dollar.

Based on utilization = amount of resources being used / amount of resources purchased

With kubernetes you can push your utilisation to greater than 50%.
Let kubernetes find your optimal packing.

* Resource requests specify the minimum amount of a resource required to run the application
* Resource limits specify the maximum amount of a resource that an application can consume

#### Resource Requests

Kubernetes guarantees these resources

For example to ensure the container lands on a machine with half a CPU and gets 128Mb RAM:

Use the `resources` flag

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard
    spec:
      containers:
        - image: gcr.io/kuar-demo/kuard-amd64:blue
          name: kuard
          resources:
            requests:
              cpu: "500m"
              memory: "128Mi"
            limits:
              cpu: "1000m"
              memory: "256Mi”
          ports:
            - containerPort: 8080
              name: http
              protocol: TCP

> Resources are requested per container, not per pod. 

Scheduler will ensure sum of all requests of all pods on a node does not exceed the apacity of the node

* As long as it is the only Pod on the machine, it will consume all 2.0 of the available cores, despite only requesting 0.5 CPU
* If a second Pod with the same container and the same request of 0.5 CPU lands on the machine, then each Pod will receive 1.0 cores
* If a third identical Pod is scheduled, each Pod will receive 0.66 cores. Finally, if a fourth identical Pod is scheduled, each Pod will receive the 0.5 core it requested, and the node will be at capacity.

The `kubelet` terminates containers whose memory usage is greater than requested memory when the node runs out of memory.

Resource `limits` can also be set - they ensure that usage does not exceed these limits.

> Limits are hard limits

### Persisting Data with Volumes

When a pod is deleted or a container restarts all the data on the container's filesystem is deleted.

> Usually a good thing as you don't want to leave cruft around from your stateless web app.

In other cases persistent disk storage is an important part of a healthy application

#### Using Volumes with Pods

* `spec.volumes` - array that defines the volumes that may be accessed by containers in the pod manifest
* `volumeMounts` - array that defines the volumes that are mounted to a particular container and the path where the volume should be mounted

> Not all containers are required to mount all volumes defined in the pod

> Two different container can mount the same volume at different mount points

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard
    spec:
      volumes:
        - name: "kuard-data"
          hostPath:
            path: "/var/lib/kuard"
      containers:
        - image: gcr.io/kuar-demo/kuard-amd64:blue
          name: kuard
          volumeMounts:
            - mountPath: "/data"
              name: "kuard-data"
          ports:
            - containerPort: 8080
              name: http
              protocol: TCP

A single volume `kuard-data` is mounted to `/data`

#### Patterns for Using Data in your Application

* Communication / synchronization - sharing a git repo between containers - `emptyDir` works well
* Cache - prerendered thumbnails that survive restarts - `emptyDir` works well
* Persistent data - data independent of the lifespan of the pod and should move between nodes if nodes fail or a pod is moved. Kubernetes supports a variety of remote storage volumes and protocols like NFS, iSCSI as well as cloud provider storage Amazon Elastic Block Store, Azure's files and Disk Storage and Google's Persistent Disk.
* Mounting the host filesystem - Applications need the underlying host filesystem, but don't need a persistent volume. For example they need `/dev`- for this Kubernetes supports `hostPath` volume that mounts paths on worked node to the container.

### Persisting data using remote disks

Often you want the data to stay with the pod even when restarted on a new host.
To achieve this you mount a `remote network storage volume` into your pod.
With network-based storage Kubernetes automatically mounts and unmounts the appropriate storage.

An example using an NFS server:

    volumes:
        - name: "kuard-data"
          nfs:
            server: my.nfs.server.local
            path: "/exports

**Persistent volumes are a deep topic**

### Putting it all Together

Many applications are stateful and we must preserve any data and ensure access to underlying storage volume.

A persistent volume backed by network attached storage.

> Through a combination of persistent volumes, readiness and liveness probes, and resource restrictions, Kubernetes provides everything needed to run stateful applications reliably.

A full example: `kuard-pod-full.yaml`

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard
    spec:
      volumes:
        - name: "kuard-data"
          nfs:
            server: my.nfs.server.local
            path: "/exports"
      containers:
        - image: gcr.io/kuar-demo/kuard-amd64:blue
          name: kuard
          ports:
            - containerPort: 8080
              name: http
              protocol: TCP
          resources:
            requests:
              cpu: "500m"
              memory: "128Mi"
            limits:
              cpu: "1000m"
              memory: "256Mi"
          volumeMounts:
            - mountPath: "/data"
              name: "kuard-data"
          livenessProbe:
            httpGet:
              path: /healthy
              port: 8080
            initialDelaySeconds: 5
            timeoutSeconds: 1
            periodSeconds: 10
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 30
            timeoutSeconds: 1
            periodSeconds: 10
            failureThreshold: 3

# 6. Labels and Annotations

Kubernetes was made to grow as your application grows in scale and complexity

Labels and annotation lets you work  in they way _you_ built the app - assuming the dev knows best? But google decided on this.

Labels are key-value pairs that can be attached to kubernetes objects, they are important in grouping objects.
Annotations are key-value pairs designed to hold non-identifying info that can be leveraged by tools and libraries.

## Labels

* keys: an optional prefix and a name, separated by a slash, prefix must be a DNS subdomain.
* values: strings with max of 63 characters

Example:

    acme.com/app-version => 1.0.0
    appVersion => 1.0.0
    app.version => 1.0.0
    kubernetes.io/cluster-service => true

### Applying Labels

Create deployments (array of pods)

Run kuard version 1 in a production environment (2 replicas):

    kubectl run alpaca-prod --image=gcr.io/kuar-demo/kuard-amd64:blue --replicas=2 --labels="ver=1,app=alpaca,env=prod"

Run kuard version 2 in a test environment:

    kubectl run alpaca-test --image=gcr.io/kuar-demo/kuard-amd64:green --replicas=1 --labels="ver=2,app=alpaca,env=test"

Run bandicoot version 2 in production environment (2 replicas):

    kubectl run bandicoot-prod --image=gcr.io/kuar-demo/kuard-amd64:green --replicas=2 --labels="ver=2,app=bandicoot,env=prod"

Run bandicoot version 2 in a staging environment:

    kubectl run bandicoot-staging --image=gcr.io/kuar-demo/kuard-amd64:green --replicas=1 --labels="ver=2,app=bandicoot,env=staging"

If we get deployments:

    kubectl get deployments --show-labels
    NAME                READY   UP-TO-DATE   AVAILABLE   AGE     LABELS
    alpaca-prod         2/2     2            2           5m26s   app=alpaca,env=prod,ver=1
    alpaca-test         1/1     1            1           3m49s   app=alpaca,env=test,ver=2
    bandicoot-prod      2/2     2            2           66s     app=bandicoot,env=prod,ver=2
    bandicoot-staging   1/1     1            1           62s     app=bandicoot,env=staging,ver=2

### Modifying Labels

    kubectl label deployments alpaca-test "canary=true"

> This will only change the label on the deployment, not the `replicaSet` or `pods`

    kubectl get pods --show-labels
    NAME                                 READY   STATUS    RESTARTS   AGE     LABELS
    alpaca-prod-85cdbc664-gkq5j          1/1     Running   0          8m50s   app=alpaca,env=prod,pod-template-hash=85cdbc664,ver=1
    alpaca-prod-85cdbc664-gs4t5          1/1     Running   0          8m50s   app=alpaca,env=prod,pod-template-hash=85cdbc664,ver=1
    alpaca-test-776d476d-khv6p           1/1     Running   0          7m13s   app=alpaca,env=test,pod-template-hash=776d476d,ver=2
    bandicoot-prod-589dc468c6-5ssc6      1/1     Running   0          4m30s   app=bandicoot,env=prod,pod-template-hash=589dc468c6,ver=2
    bandicoot-prod-589dc468c6-8vm2x      1/1     Running   0          4m30s   app=bandicoot,env=prod,pod-template-hash=589dc468c6,ver=2
    bandicoot-staging-77f4467bb8-5w9xz   1/1     Running   0          4m26s   app=bandicoot,env=staging,pod-template-hash=77f4467bb8,ver=2

To show a label value as a column

    kubectl get deployments -L canary

Remove a label with

    kubectl label deployments alpaca-test "canary-"

### Label Selectors

> Each deployment (via a ReplicaSet) creates a set of Pods using the labels specified in the template embedded in the deployment

What was that?

`pod-template-hash` is a label applied by the deployment so it can keep track of which pods were generated from which template version

Select pods that are only version 2:

    kubectl get pods --selector="ver=2"

A logical `AND` with multiple selectors:

    kubectl get pods --selector="app=bandicoot,ver=2"

One of (`IN` operator):

    kubectl get pods --selector="app in (alpaca,bandicoot)"

Get where a key is set:

    kubectl get deployments --selector="canary"

There are negatives of the above too:

* `key=value`
* `key!=value`
* `key in (value1, value2)`
* `key notin (value1, value2)`
* `key` - key is set
* `!key` - key is not set

`-l` is the short flag of `--selector`:

    kubectl get pods -l 'ver=2,!canary'

### Label Selectors in API Objects

Selector of: `“app=alpaca,ver in (1, 2)”`

Would be converted to:

    selector:
      matchLabels:
        app: alpaca
      matchExpressions:
        - {key: ver, operator: In, values: [1, 2]}
        
Seelctor: `app=alpaca,ver=1`

Would be converted to:

    selector:
        app: alpaca
        ver: 1

### Labels in Kubernetes Architecture

Labels link related kubernetes objects

> Kubernetes is a purposely decoupled system - there is no hierachy and all components operate independently

Labels are the powerful and ubiquitous glue that holds Kubernetes together.

## Annotations

Metadata with the sole purpose of assisting tools and libraries
They are a way for other tools driving kubernetes by API to store data

There is overlap of annotations and labels - when in doubt use annotations and promote to labels.

Annotations are used to:
* Keep track of a reason for the latest update on an object
* Communicate a specialised scheduling policy
* Extend data about the last tool and date of an update
* Attach build, release or image information (git hash, timestamp, PR number )
* Enable the deployment object to keep track of replicaSets
* Data to enhance the UI - base64 encoded image or logo

The primary use case is **rolling deployments** - so rollbacks to previous state can happen.

### Defining Annotations

Annotations are defined in the same way as labels.
The `namespace` part of the annotation is more important.

> It is not uncommon for a JSON document to be encoded as a string and stored in an annotation

kubernetes has no knowledge of the format of an annotation and no validation

Annotations are defined in the `metadata` section in every Kubernetes object:

    metadata:
      annotations:
        example.com/icon-url: "https://example.com/icon.png"

## Cleanup

Lets remove the deployments we created

    kubectl delete deployments --all

# 7. Service Discovery

Kubernetes is very dynamic - pods and nodes are scheduled and autoscaled.

> The API-driven nature of the system encourages others to create higher and higher levels of automation

The problem is _finding all the things_

## What is Service Discovery

What processes are listening at which address for which service.
Good service discovery ensures low latency and reliable info.

DNS - Domain Name System - is the traditional system of service discovery on the internet.

> DNS is designed for relatively stable name resolution with wide and efficient caching

It is a great system for the internet but Kubernetes is too dynamic

Unfortunately many systems (like java) look up a name in DNS directly and never re-resolve.
Leading to stale mappings - even with short TTL's and well behaved clients.
There are limits to the amount and type of information that can be returned by a DNS query.
Things start to break past 20-30 A records on a DNS query of a single name.

`SRV` records solve that issue but are hard to use.

Usually client's handle multiple IP's by just taking the first IP address and rely on the DNS server to randomise or round-robin the order of results.

## The Service Object

Service discovery in k8s starts with the service object

We use `kubectl expose` to create a service.

    kubectl run alpaca-prod --image=gcr.io/kuar-demo/kuard-amd64:blue --replicas=3 --port=8080 --labels="ver=1,app=alpaca,env=prod"

    kubectl expose deployment alpaca-prod

    kubectl run bandicoot-prod --image=gcr.io/kuar-demo/kuard-amd64:green --replicas=2 --port=8080 --labels="ver=2,app=bandicoot,env=prod"
    
    kubectl expose deployment bandicoot-prod
    
    $ kubectl get services -o wide
    NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE   SELECTOR
    alpaca-prod      ClusterIP   10.102.127.103   <none>        8080/TCP   88s   app=alpaca,env=prod,ver=1
    bandicoot-prod   ClusterIP   10.108.246.138   <none>        8080/TCP   4s    app=bandicoot,env=prod,ver=2
    kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP    8d    <none>

The `kubernetes` service is created automatically so you can speak to the kubernetes API from within the app

`kubectl expose` will pull the label selector and the relevant ports from the deployment definition

The service is also assigned a virtual IP called the _cluster IP_ - a special ip that will load balance across all the pods

To interact with a service we need to port forward to a pod:

    ALPACA_POD=$(kubectl get pods -l app=alpaca -o jsonpath='{.items[0].metadata.name}')
    kubectl port-forward $ALPACA_POD 48858:8080

### Service DNS

The cluster ip is virtual - and therefore stable - so it is appropriate to give it a DNS address.
Issues around clients caching DNS results will no longer apply.

Kubernetes provides a DNS service exposed to pods running in the cluster.
The DNS service is installed as a system component when the cluster is created.
It is k8s building on k8s.

If you query `alpaca-prod` from within a container, you get:

    ;; ANSWER SECTION:
    alpaca-prod.default.svc.cluster.local.	30	IN	A	10.102.127.103

* `alpaca-prod` - name of the service
* `default` - namespace of the service
* `svc` - recognise as service
* `cluster.local.` - base domain name for the cluster

In it's own namespace you can refer to just the name of the service `alpaca-prod`

### Readiness Checks

Lets add a readiness check:

    kubectl edit deployment/alpaca-prod

add a readiness probe:

    name: alpaca-prod
      readinessProbe:
        httpGet:
           path: /ready
           port: 8080
        periodSeconds: 2
        initialDelaySeconds: 0
        failureThreshold: 3
        successThreshold: 1

This will delete and recreate the pods

But we need to restart the port forwarder

    kubectl port-forward $ALPACA_POD 48858:8080

You can now use a `watch` command to find what service are sending traffic to a service

    kubectl get endpoints alpaca-prod --watch

## Looking Beyond the Cluster

At some point you want the pod reachable outside the cluster.

The most portable way of doing this is with `NodePorts`

In addition to the cluster IP the system picks a port and every node in the cluster forwards traffic from that port to the service.

If you can reach any node, you can reach the service.

    kubectl edit service alpaca-prod

Change `spec.type` to `NodePort` (from `ClusterIp`)

or you can specify this when creating the service

    kubectl expose --type=NodePort

> This can be intergrated with hardware or software load balancers

View the port assigned to the pod:

    $ kubectl describe service alpaca-prod
    Name:                     alpaca-prod
    Namespace:                default
    Labels:                   app=alpaca
                            env=prod
                            ver=1
    Annotations:              <none>
    Selector:                 app=alpaca,env=prod,ver=1
    Type:                     NodePort
    IP:                       10.102.127.103
    Port:                     <unset>  8080/TCP
    TargetPort:               8080/TCP
    NodePort:                 <unset>  30442/TCP
    Endpoints:                172.17.0.11:8080,172.17.0.7:8080,172.17.0.8:8080
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:                   <none>

In this case `30442` was assigned. 

    ssh <node> -L 8080:localhost:32711

Apparently locally you can access it directly

## Cloud Integration

You can set the `spec.type` as `LoadBalancer`

A public address will be assigned by your public cloud.

Describe the service to find the ip:

    kubectl describe service alpaca-prod

> The way a load balancer is configured is specific to each cloud

## Advanced Details

### Endpoints

Some applications want to access services without using the cluster IP

For this we use `endpoints`

    $ kubectl describe endpoints alpaca-prod
    Name:         alpaca-prod
    Namespace:    default
    Labels:       app=alpaca
                env=prod
                ver=1
    Annotations:  endpoints.kubernetes.io/last-change-trigger-time: 2019-12-12T16:44:01Z
    Subsets:
    Addresses:          172.17.0.11,172.17.0.7,172.17.0.8
    NotReadyAddresses:  <none>
    Ports:
        Name     Port  Protocol
        ----     ----  --------
        <unset>  8080  TCP

    Events:  <none>

we can watch the endpoint:

    kubectl get endpoints alpaca-prod --watch

now lets delete and recreate:

    kubectl delete deployment alpaca-prod
    kubectl run alpaca-prod --image=gcr.io/kuar-demo/kuard-amd64:blue --replicas=3 --port=8080 --labels="ver=1,app=alpaca,env=prod"

as you do this:

    alpaca-prod   172.17.0.11:8080,172.17.0.7:8080,172.17.0.8:8080   153m
    alpaca-prod   172.17.0.8:8080                                    154m
    alpaca-prod   <none>                                             154m
    alpaca-prod   172.17.0.8:8080                                    154m
    alpaca-prod   172.17.0.6:8080,172.17.0.8:8080                    154m
    alpaca-prod   172.17.0.6:8080,172.17.0.7:8080,172.17.0.8:8080    154m

that happens

> However many old services expect a plain old ip address

### Manual Service Discovery

You can use the kubernetes API for rudimentary service discovery

    $ kubectl get pods -o wide --selector=app=alpaca,env=prod
    NAME                           READY   STATUS    RESTARTS   AGE     IP           NODE       NOMINATED NODE   READINESS GATES
    alpaca-prod-65bf8ccb57-5vdcl   1/1     Running   0          3m57s   172.17.0.8   minikube   <none>           <none>
    alpaca-prod-65bf8ccb57-fhds9   1/1     Running   0          3m57s   172.17.0.7   minikube   <none>           <none>
    alpaca-prod-65bf8ccb57-nf8pv   1/1     Running   0          3m57s   172.17.0.6   minikube   <none>           <none>

that is the basics of service discovery

### kube-proxy and ClusterIPs

Cluster IPs are stable virtual IPs that load-balance traffic across all of the endpoints in a service.
It is done by a component running on every node in a cluster called `kube-proxy`.

`kube-proxy` is updating `iptables` to redirect traffic.

### Cluster IP Environment Variables

You should use DNS to find cluster ips, however you can also use environment variables.

    ALPACA_PROD_SERVICE_HOST	10.102.127.103
    ALPACA_PROD_SERVICE_PORT	8080

The environment variables approach requires resources to be created in a specific order.

Connecting external resources to kubernetes is difficult, you could create an internal load balancer in your VPN.
That delivers traffic from a fixed ip into the cluster. Then use traditional DNS.

Or run `kube-proxy` on the external resource - difficult to setup only for on-premise.

> cleanup the containers with `kubectl delete services,deployments -l app`

# 8. HTTP Load Balancing with Ingress

Getting network traffic to and from an application is critical

The `service` operates at layer 4 (according to the OSI model) - the transport layer - it only forwards TCP and UDP and does not look inside those connections.

That is why applications on a cluster use many different exposed service. In this case they are of `type: NodePort`.
You have to have clients connecting to a unique port per service.

If the services are of `type: LoadBalancer` you allocate expensive cloud resources for each service.

For HTTP (layer 7) based services, we can do better.

Solving this problem in non-Kubernetes situations - users often turn to _virtual hosting_.
A mechanism to host many HTTP sites on a single IP.

Typically the user uses a load balancer to accept connections on port 80 and 443.
The program parses the HTTP connection based on the `Host` header and the URL path. It then proxies the HTTP call to some other program.

The load balancer or reverse proxy plays traffic cop for directing the incoming connection to the right upstream server.

Kubernetes calls its HTTP-based load-balancing system _Ingress_.

> Ingress is kubernetes native virtual-hosting

A complex part of the pattern is the user must manage the load balancer configuration file - a dynamic environment with many virtual hosts.

Kubernetes simplifies this by:
* standardizing the configuration
* moving to a standard kubernetes object
* merging multiple ingress objects into a single config for the load balancer

## Ingress Spec vs Ingress Controllers

Ingress differs from every other kubernetes resource.

There is no "standard" ingress controller built into kubernetes.

There is no code to act on the objects, the user (or distribution) must install and manage the outside controller.
The controller is _pluggable_.

* there is no single http load balancer that can be universally used
* there are also cloud provided load balancers and hardware load balancers
* ingress was added before common extensability was added

## Installing Contour

Contour is a controller used to configure the open source load balancer called Envoy.
Envoy is built to be configured via API.
Contour translates ingress objects into something envoy can understand.

[Coutours Github Page](https://github.com/projectcontour/contour)

    kubectl apply -f https://projectcontour.io/quickstart/contour.yaml

It creates all this shit:

    namespace/projectcontour created
    serviceaccount/contour created
    configmap/contour created
    customresourcedefinition.apiextensions.k8s.io/ingressroutes.contour.heptio.com created
    customresourcedefinition.apiextensions.k8s.io/tlscertificatedelegations.contour.heptio.com created
    customresourcedefinition.apiextensions.k8s.io/httpproxies.projectcontour.io created
    customresourcedefinition.apiextensions.k8s.io/tlscertificatedelegations.projectcontour.io created
    serviceaccount/contour-certgen created
    rolebinding.rbac.authorization.k8s.io/contour created
    role.rbac.authorization.k8s.io/contour-certgen created
    job.batch/contour-certgen created
    clusterrolebinding.rbac.authorization.k8s.io/contour created
    clusterrole.rbac.authorization.k8s.io/contour created
    role.rbac.authorization.k8s.io/contour-leaderelection created
    rolebinding.rbac.authorization.k8s.io/contour-leaderelection created
    service/contour created
    service/envoy created
    deployment.apps/contour created
    daemonset.apps/envoy created

You can get the external address of contour with:

    $ kubectl get -n projectcontour service contour -o wide
    NAME      TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE    SELECTOR
    contour   ClusterIP   10.103.81.4   <none>        8001/TCP   100s   app=contour

> With minikube `EXTERNAL-IP` will be `<none>`, you need to assign ips to each service of `type: LoadBalacer` with `minikube tunnel` (It takes a while)

**The above did not work**

### Configuring DNS

Configure DNS entries to the external address of your load balancer

You can map multiple hostnames to a single external endpoint.
For an ip address use `A records` for a hsotname use `CNAME records`.

## Configurating local DNS

Using `/etc/hosts`.

On mac you might need to `sudo killall -HUP mDNSResponder` after changing the file.

Eg.

    192.168.0.101 alpaca.example.com bandicoot.example.com

## Using Ingress

    kubectl run be-default --image=gcr.io/kuar-demo/kuard-amd64:blue --replicas=3 --port=8080
    kubectl expose deployment be-default
    kubectl run alpaca --image=gcr.io/kuar-demo/kuard-amd64:green --replicas=3 --port=8080
    kubectl expose deployment alpaca
    kubectl run bandicoot --image=gcr.io/kuar-demo/kuard-amd64:purple --replicas=3 --port=8080
    kubectl expose deployment bandicoot

View the services

    $ kubectl get services -o wide
    NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE     SELECTOR
    alpaca       ClusterIP   10.109.108.131   <none>        8080/TCP   2m48s   run=alpaca
    bandicoot    ClusterIP   10.111.63.119    <none>        8080/TCP   18s     run=bandicoot
    be-default   ClusterIP   10.103.30.58     <none>        8080/TCP   4m3s    run=be-default
    kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    8d      <none>

### Simplest Usage

Pass everything it sees to the upstream service.

`simple-ingress.yml`:

    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
      name: simple-ingress
    spec:
      backend:
        serviceName: alpaca
        servicePort: 8080

    kubectl apply -f simple-ingress.yaml
    
Verify it was setup correctly with:

    $ kubectl get ingress
    NAME             HOSTS   ADDRESS   PORTS   AGE
    simple-ingress   *                 80      27s

and

    $ kubectl describe ingress simple-ingress
    Name:             simple-ingress
    Namespace:        default
    Address:          
    Default backend:  alpaca:8080 (172.17.0.12:8080,172.17.0.13:8080,172.17.0.14:8080)
    Rules:
    Host  Path  Backends
    ----  ----  --------
    *     *     alpaca:8080 (172.17.0.12:8080,172.17.0.13:8080,172.17.0.14:8080)
    Annotations:
    kubectl.kubernetes.io/last-applied-configuration:  {"apiVersion":"extensions/v1beta1","kind":"Ingress","metadata":{"annotations":{},"name":"simple-ingress","namespace":"default"},"spec":{"backend":{"serviceName":"alpaca","servicePort":8080}}}

    Events:  <none>

**This ensures anything hitting the Ingress controller is forwarded to the `alpaca` service**

### Using Hostnames

**host-ingress.yml**

    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
      name: host-ingress
    spec:
      rules:
      - host: alpaca.example.com
        http:
          paths:
          - backend:
              serviceName: alpaca
              servicePort: 8080
      - host: bandicoot.example.com
        http:
          paths:
            - backend:
                serviceName: bandicoot
                servicePort: 8080

Directing traffic based on the properties of the request.

    $ kubectl get ingress
    NAME             HOSTS                                      ADDRESS   PORTS   AGE
    host-ingress     alpaca.example.com,bandicoot.example.com             80      4m22s
    simple-ingress   *                                                    80      4d11h

    $ kubectl describe ingress host-ingress
    Name:             host-ingress
    Namespace:        default
    Address:          
    Default backend:  default-http-backend:80 (<none>)
    Rules:
    Host                   Path  Backends
    ----                   ----  --------
    alpaca.example.com     
                                alpaca:8080 (172.17.0.5:8080,172.17.0.6:8080,172.17.0.7:8080)
    bandicoot.example.com  
                                bandicoot:8080 (172.17.0.10:8080,172.17.0.2:8080,172.17.0.9:8080)
    Annotations:
    kubectl.kubernetes.io/last-applied-configuration:  {"apiVersion":"extensions/v1beta1","kind":"Ingress","metadata":{"annotations":{},"name":"host-ingress","namespace":"default"},"spec":{"rules":[{"host":"alpaca.example.com","http":{"paths":[{"backend":{"serviceName":"alpaca","servicePort":8080}}]}},{"host":"bandicoot.example.com","http":{"paths":[{"backend":{"serviceName":"bandicoot","servicePort":8080}}]}}]}}

    Events:  <none>

There is a reference to the `default-http-backend:80` - some ingress controllers 

You can then go to `alpaca.example.com` or `bandicoot.example.com`

### Using Paths

Directing traffic based on path, you can set in the `paths` entry.

**path-ingress.yml**:

    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
      name: path-ingress
    spec:
      rules:
      - host: bandicoot.example.com
        http:
          paths:
          - path: "/"
            backend:
              serviceName: bandicoot
              servicePort: 8080
          - path: "/a/"
            backend:
              serviceName: alpaca
              servicePort: 8080

Now `bandicoot.example.com` goes to bandicoot and `bandicoot.example.com/a/` goes to `alpaca`.

### Clean Up

    kubectl delete ingress host-ingress path-ingress simple-ingress
    kubectl delete service alpaca bandicoot be-default
    kubectl delete deployment alpaca bandicoot be-default

## Advanced Ingress Topics and Gotchas

Features supported depend on the Ingress Controller implementations.

### Running Multiple Ingress Controllers

* Specify which ingress object is meant for which ingress controller with: `kubernetes.io/ingress.class` annotation
* If it is not set - multiple controllers will fight to satisfy the ingress and write to the `status` field

### Multiple Ingress Objects

* Ingress controllers should read them all and try merge them

### Ingress and Namespaces

* An ingress object can only refer to an upstream service in the same namespace - security reasons
* However, multiple Ingress objects in different namespaces can specify subpaths for the same host - they are merged.
* No restrictions on Ingress controller access to host and path

### Path Rewriting

* Some ingress controllers support this.
* This modifies the HTTP request as it is processed

With an `nginx ingress controller`: the annotation `nginx.ingress.kubernetes.io/rewrite-target: /` can reqrite path and supports regex.

> Path rewriting isn’t a silver bullet, though, and can often lead to bugs

> Better to avoid subpaths

### Serving TLS

Ingress and INgress controllers (what is the difference?) support this.

Create a secret with kubectl:

    kubectl create secret tls <secret-name> --cert <certificate-pem-file> --key <private-key-pem-file>

**tls-secret.yml**:

    apiVersion: v1
    kind: Secret
    metadata:
      creationTimestamp: null
      name: tls-secret-name
    type: kubernetes.io/tls
    data:
      tls.crt: <base64 encoded certificate>
      tls.key: <base64 encoded private key>

Once the certificate is uploaded you can reference an Ingress Object.

**tls-ingress.yml**

    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
      name: tls-ingress
    spec:
      tls:
      - hosts:
        - alpaca.example.com
        secretName: tls-secret-name
      rules:
      - host: alpaca.example.com
        http:
          paths:
          - backend:
              serviceName: alpaca
              servicePort: 8080

> Uploading and managing TLS secrets can be difficult

It is recommended to use [`cert-manager`](https://github.com/jetstack/cert-manager) that links up directly with `lets-encrypt` 

## Alternate Ingress Implementations

Each cloud provider has an Ingress implementation that exposes the layer 7 load balancer.
Instead of configuring a software load balancer running in a pod, these controllers take ingresses and use them to configure the cloud based load balancers.

The most popular ingress is the [Nginx Ingress Controller](https://github.com/kubernetes/ingress-nginx/)
The open source version reads ingress objects and merges them into an Nginx config file.

Other options:
* [Ambassador](https://github.com/datawire/ambassador)
* [Gloo](https://github.com/solo-io/gloo)
* [Traefik](https://containo.us/traefik/) - go reverse=proxy that also acts as an ingress

## The Future of Ingress

The ingress object provides a useful abstraction for configuring L7 load balancers

> It is easy to misconfigure ingress

Ingress was created before the idea of service mesh - the intersection of ingress and service mesh is still being defined.

* Istio has a gateway that overlaps with an ingress
* Contour introduced an `IngressRoute` 

## Summary

* Ingress is unique to Kubernetes
* Critical for exposing services in a practical and cost-effective way

# 9. ReplicaSets

Pods are essentially one-off singletons. More often than not you want multiple replicas of a container running at a time.

* Redundancy - multiple instances mean a failure can be tolerated
* Scale - more requests can be handled
* Sharding - different parts of computation can be handled in parrallel

A user defines a replicated set of pods as a single entity - a replica set.

A replicaset is a cluster wide pod manager - ensuring the right types and number of pods are running.

Building blocks of common application deployment and unerpin self healing infrastructure.

It is a cookie cutter and a desired number of cookies.
Managing replicated pods is an example of a reconciliation loop.

> The decision to embed a pod in a replicaset, should rather have been a reference to a pod.

## Reconcilliation Loops

* Desired state vs observed/current state
* reconcilliation loop is constantly running
* goal-driven, slef-healing system

## Relating Pods and ReplicaSets

* Kubernetes is built decoupled - modular - swappable and replacable.
* ReplicaSets that create pods and services that load balance them are totally seperate API objects.

Reasons:
* ReplicaSets can adopt existing pods
* Leave the pod alive for debugging purposes but remove from replica set and service

## Designing with ReplicaSets

Replicasets are designed to be a single, scalable microservice
Everypod created from a replicaset is the same
A k8s service load balancer spreads teh traffic across the pods
Designed for stateless services

## ReplicaSet Spec

Like all objects in `k8s` they are defined by a spec.
All replicasets must have a unique name: `metadata.name`, the number of replicas to run and a pod template.

**kuard-rs.yaml**

    apiVersion: apps/v1
    kind: ReplicaSet
    metadata:
      name: kuard
      labels:
        app: kuard
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: kuard
      template:
        metadata:
          labels:
            app: kuard
            version: "2"
        spec:
          containers:
            - name: kuard
              image: "gcr.io/kuar-demo/kuard-amd64:green"

### Pod Templates

The pods created by the replciate set are created using the api.

The reconcilliation loop discovers pods with **labels**

    template:
      metadata:
        labels:
          app: helloworld
          version: v1
      spec:
        containers:
          - name: helloworld
            image: kelseyhightower/helloworld:v1
            ports:
              - containerPort: 80

## Creating a ReplicaSet

    kubectl apply -f kuard-rs.yml

the replicaset will see no pod and request it is created:

    $ kubectl get pods
    NAME          READY   STATUS    RESTARTS   AGE
    kuard-2qmn2   1/1     Running   0          2m22s

## Inspecting a ReplicaSet

    $ kubectl get rs
    NAME    DESIRED   CURRENT   READY   AGE
    kuard   1         1         1       3m21s

inspect the rs:

    $ kubectl describe rs kuard
    Name:         kuard
    Namespace:    default
    Selector:     app=kuard
    Labels:       app=kuard
    Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                    {"apiVersion":"apps/v1","kind":"ReplicaSet","metadata":{"annotations":{},"labels":{"app":"kuard"},"name":"kuard","namespace":"default"},"s...
    Replicas:     1 current / 1 desired
    Pods Status:  1 Running / 0 Waiting / 0 Succeeded / 0 Failed
    Pod Template:
    Labels:  app=kuard
            version=2
    Containers:
    kuard:
        Image:        gcr.io/kuar-demo/kuard-amd64:green
        Port:         <none>
        Host Port:    <none>
        Environment:  <none>
        Mounts:       <none>
    Volumes:        <none>
    Events:
    Type    Reason            Age    From                   Message
    ----    ------            ----   ----                   -------
    Normal  SuccessfulCreate  3m46s  replicaset-controller  Created pod: kuard-2qmn2

### Finding a Replicaset from a pod

Sometimes you want to find if a pod is being managed by a replicaset

The key is to check the `kubernetes.io/created-by` annotation.

    $ kubectl get pods kuard-2qmn2 -o yaml
    apiVersion: v1
    kind: Pod
    metadata:
    creationTimestamp: "2019-12-17T13:58:41Z"
    generateName: kuard-
    labels:
        app: kuard
        version: "2"
    name: kuard-2qmn2
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
        blockOwnerDeletion: true
        controller: true
        kind: ReplicaSet
        name: kuard
        uid: 00d2a2f5-5d3e-4260-bae7-4e19aa5df6df
    resourceVersion: "292844"
    selfLink: /api/v1/namespaces/default/pods/kuard-2qmn2
    uid: a89f3fc9-e5f0-46dc-beea-40872120d42a
    spec:
    containers:
    - image: gcr.io/kuar-demo/kuard-amd64:green
        imagePullPolicy: IfNotPresent
        name: kuard
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: default-token-mbn5b
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
        key: node.kubernetes.io/not-ready
        operator: Exists
        tolerationSeconds: 300
    - effect: NoExecute
        key: node.kubernetes.io/unreachable
        operator: Exists
        tolerationSeconds: 300
    volumes:
    - name: default-token-mbn5b
        secret:
        defaultMode: 420
        secretName: default-token-mbn5b
    status:
    conditions:
    - lastProbeTime: null
        lastTransitionTime: "2019-12-17T13:58:41Z"
        status: "True"
        type: Initialized
    - lastProbeTime: null
        lastTransitionTime: "2019-12-17T13:58:44Z"
        status: "True"
        type: Ready
    - lastProbeTime: null
        lastTransitionTime: "2019-12-17T13:58:44Z"
        status: "True"
        type: ContainersReady
    - lastProbeTime: null
        lastTransitionTime: "2019-12-17T13:58:41Z"
        status: "True"
        type: PodScheduled
    containerStatuses:
    - containerID: docker://ea0a3131df253e9f1edc0a81018631e8ba0028c1d398cabd08932b4a4ab1bbd5
        image: gcr.io/kuar-demo/kuard-amd64:green
        imageID: docker-pullable://gcr.io/kuar-demo/kuard-amd64@sha256:b45e6382fef12c72da3abbf226cb339438810aae18928bd2a811134b50398141
        lastState: {}
        name: kuard
        ready: true
        restartCount: 0
        started: true
        state:
        running:
            startedAt: "2019-12-17T13:58:43Z"
    hostIP: 192.168.64.3
    phase: Running
    podIP: 172.17.0.18
    podIPs:
    - ip: 172.17.0.18
    qosClass: BestEffort
    startTime: "2019-12-17T13:58:41Z"

> Yet again the book fails as with minikube this doesn't show anything for `created-by`

### Finding a Set of Pods for the ReplicaSet

    $ kubectl get pods -l app=kuard,version=2
    NAME          READY   STATUS    RESTARTS   AGE
    kuard-2qmn2   1/1     Running   0          19m

## Scaling Replicasets

Replicasets are scaled up or down with `spec.replicas`

### imperitive Scaling

    kubectl scale replicasets kuard --replicas=4

> Remmeber to also update the tet files replicas

there needs to be a declarative change for the imperitive change

### Declaratively scaling out kubectl apply

    spec:
        replicas: 5

then:

    kubectl apply -f kuard-rs.yml

### Autoscaling a Replicaset

Sometimes you just want enough.

A webserver like nginx you may want to scale for CPU usage.
For an in-memory cache like redis, you may want to scale for memory usage.
In some cases you may want to scale on custom app metrics.

The HPA (Horizontal Pod Autoscaler) handles these scenarios.

> HPA requires the presence of the heapster Pod on your cluster. heapster keeps track of metrics and provides an API for consuming metrics that HPA uses when making scaling decisions

To check if `heapster` exists, use (and check for heapster):

    kubectl get pods --namespace=kube-system

It is horizontal scaling - adding more replicas of a pod.
Vertical scaling is adding more CPU and RAM to the pod.

There is also `cluster autoscaling` - the number of machines in a cluster are scaled in response to resource needs.

### Autoscaling based on CPU

Useful for request based system - that consume CPU proportionally to requests with relatively static memory usage.

    kubectl autoscale rs kuard --min=2 --max=5 --cpu-percent=80

This creates an autoscaler that scales from 2 to 5 pods with a CPU threshold of 80%

Get autoscalers with:

    kubectl get hpa

> Be careful of imperitive declarations of replicas - manually setting the number of replicas when there is a autoscaler present.

## Deleting ReplicaSets

Delete a replicaSet with:

    kubectl delete rs kuard

Delete a replicaset without deleting the pods:

    kubectl delete rs kuard --cascade=false

# 10. Deployments

* The Deployment object exists to manage the release of new versions.
* They represent deployed applications (transcending version)
* Enable easy movement from one version to the next

It uses health checks and stops deployment if there are issues.

> You can simply and reliably roll out new software versions without downtime or errors

The deployment controller - controls the deployment.

> Another key win for kubernetes is the ability to do a rolling update - without downtime or losing a single request.

## First Deployment

`kuard-deployment.yml`:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: kuard
    spec:
      selector:
        matchLabels:
          run: kuard
      replicas: 1
      template:
        metadata:
          labels:
            run: kuard
        spec:
          containers:
          - name: kuard
            image: gcr.io/kuar-demo/kuard-amd64:blue

Create the deployment:

    kubectl create -f kuard-deployment.yaml

### Deployment Internals

Deployments manage ReplicaSets, as ReplicaSets manage Pods.
View the label selector of the deployment:

    kubectl get deployments kuard -o jsonpath --template {.spec.selector.matchLabels}
    map[run:kuard]

Get all replicasets

    kubectl get replicasets --selector=run=kuard

Resize the deployment

    kubectl scale deployments kuard --replicas=2
    
    $ kubectl get replicasets --selector=run=kuard
    NAME              DESIRED   CURRENT   READY   AGE
    kuard-5897df564   2         2         1       7m25s

Scale back

    kubectl scale rs kuard-5897df564 --replicas=1

Yet it still has 2 desired:

    $ kubectl get replicasets --selector=run=kuard
    NAME              DESIRED   CURRENT   READY   AGE
    kuard-5897df564   2         2         2       13m

Remember adjusting the number of replicas with the replicaset won't work as it is the deployment that manages the number of replicas and will reset that replicaset to 2.

## Creating Deployments

Get the deployment as a yaml file

    kubectl get deployments kuard --export -o yaml > kuard-deployment.yml
    kubectl replace -f kuard-deployment.yaml --save-config

The `--save-config` part ensures k8s will remember the history of the deployment

The deployment also has a strategy object:

    strategy:
      rollingUpdate:
        maxSurge: 1
        maxUnavailable: 1
      type: RollingUpdate”

There are 2 types `Recreate` and `RollingUpdate`

## Managing Deployments

    $ kubectl describe deployments kuard
    Name:                   kuard
    Namespace:              default
    CreationTimestamp:      Tue, 17 Dec 2019 18:49:33 +0200
    Labels:                 <none>
    Annotations:            deployment.kubernetes.io/revision: 1
                            kubectl.kubernetes.io/last-applied-configuration:
                            {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{"deployment.kubernetes.io/revision":"1"},"creationTimestamp":null,"...
    Selector:               run=kuard
    Replicas:               2 desired | 2 updated | 2 total | 2 available | 0 unavailable
    StrategyType:           RollingUpdate
    MinReadySeconds:        0
    RollingUpdateStrategy:  25% max unavailable, 25% max surge
    Pod Template:
    Labels:  run=kuard
    Containers:
    kuard:
        Image:        gcr.io/kuar-demo/kuard-amd64:blue
        Port:         <none>
        Host Port:    <none>
        Environment:  <none>
        Mounts:       <none>
    Volumes:        <none>
    Conditions:
    Type           Status  Reason
    ----           ------  ------
    Progressing    True    NewReplicaSetAvailable
    Available      True    MinimumReplicasAvailable
    OldReplicaSets:  <none>
    NewReplicaSet:   kuard-5897df564 (2/2 replicas created)
    Events:
    Type    Reason             Age                From                   Message
    ----    ------             ----               ----                   -------
    Normal  ScalingReplicaSet  15h                deployment-controller  Scaled up replica set kuard-5897df564 to 1
    Normal  ScalingReplicaSet  15h (x3 over 15h)  deployment-controller  Scaled up replica set kuard-5897df564 to 2

* `OldReplicaSets` and `NewReplicaSet` are important, they point to the replicaset the deployment is currently managing. If in the middle of a rollout, both fields will be set. If rollout is complete `OldReplicaSet` will be set to `<none>`

* `kubectl rollout history` - gets the history of a rollout
* `kubectl rollout status` - gets the status of a rollout

## Updating Deployments

### Scaling a Deployment

Increase number of replicas in the `yaml` and apply:

    kubectl apply -f kuard-deployment.yaml

### Updating a Container Image

Edit the deployment yaml

    containers:
    - image: gcr.io/kuar-demo/kuard-amd64:green
      imagePullPolicy: Always

You can also annotate to give info about the deployment:

    spec:
      ...
      template:
        metadata:
          annotations:
            kubernetes.io/change-cause: "Update to green kuard"

> Remember to annotate the template and not the deployment. ONly use it for significant updates.

    kubectl apply -f kuard-deployment.yaml

That will trigger a rollout

    kubectl rollout status deployments kuard

Both old and new replicasets are kept, incase you want to rollback:

    kubectl get replicasets -o wide
    
    NAME               DESIRED   CURRENT   READY   AGE     CONTAINERS   IMAGES                               SELECTOR
    kuard              3         3         3       3h51m   kuard        gcr.io/kuar-demo/kuard-amd64:green   app=kuard
    kuard-5897df564    0         0         0       60m     kuard        gcr.io/kuar-demo/kuard-amd64:blue    pod-template-hash=5897df564,run=kuard
    kuard-6dd979cc6f   2         2         2       31s     kuard        gcr.io/kuar-demo/kuard-amd64:green   pod-template-hash=6dd979cc6f,run=kuard

You can pause a deployment

    kubectl rollout pause deployments kuard

and resume

    kubectl rollout resume deployments kuard

### Rollout History

See deployment history with:

    $ kubectl rollout history deployment kuard
    deployment.apps/kuard 
    REVISION  CHANGE-CAUSE
    1         <none>
    2         Update to green kuard

Get more details of the revision

    $ kubectl rollout history deployment kuard --revision=2
    deployment.apps/kuard with revision #2
    Pod Template:
    Labels:       pod-template-hash=6dd979cc6f
            run=kuard
    Annotations:  kubernetes.io/change-cause: Update to green kuard
    Containers:
    kuard:
        Image:      gcr.io/kuar-demo/kuard-amd64:green
        Port:       <none>
        Host Port:  <none>
        Environment:        <none>
        Mounts:     <none>
    Volumes:      <none>

Change the version and annotation back to blue and apply.

    $ kubectl rollout history deployment kuard
    deployment.apps/kuard 
    REVISION  CHANGE-CAUSE
    1         <none>
    2         Update to green kuard
    3         Update to blue kuard

To rollback to the green kuard:

    kubectl rollout undo deployments kuard

    $ kubectl get rs -o wide
    NAME               DESIRED   CURRENT   READY   AGE     CONTAINERS   IMAGES                               SELECTOR
    kuard              3         3         3       3h57m   kuard        gcr.io/kuar-demo/kuard-amd64:green   app=kuard
    kuard-5897df564    0         0         0       66m     kuard        gcr.io/kuar-demo/kuard-amd64:blue    pod-template-hash=5897df564,run=kuard
    kuard-65c78f8d5f   0         0         0       3m41s   kuard        gcr.io/kuar-demo/kuard-amd64:blue    pod-template-hash=65c78f8d5f,run=kuard
    kuard-6dd979cc6f   2         2         2       6m37s   kuard        gcr.io/kuar-demo/kuard-amd64:green   pod-template-hash=6dd979cc6f,run=kuard

> Ensure that delcarative files match what is running in production 

Running `kubectl rollout undo` does not change source code, the better way to revert is with yaml.

Rollback to a specific version in history

    kubectl rollout undo deployments kuard --to-revision=3

It creates a new revision `5`:

    kubectl rollout history deployment kuard

The history can build up so might be wise to only keep a few revisions, use `revisionHistoryLimit`:

    ...
    spec:
    # We do daily rollouts, limit the revision history to two weeks of
    # releases as we don't expect to roll back beyond that.
    revisionHistoryLimit: 14
    ...

## Delpoyment Strategies

### Recreate Strategy

* simpler and faster
* terminates all pods and then re-creates all pods
* certainly results in downtime
* test deployment for non-user facing applications

### RollingUpdate Strategy

* preferred for user-facing applications
* Incrementally updates pods
* No downtime

### Managing Multiple Versions of your Service

> What about the scenario that during a deployment rollout a javascript asset is downloaded from the old replicaset that has been changed in the new replicaset. It now calls the old api which has subsequently dissapeared.

You always had this problem though, it is all about maintaining forward and backward compatability.


> You need to decouple your service from applications that depend on your service

Like a frontend decoupled from a backend via an API contract and a load balancer.

#### Configuring a Rolling Update

A `RollingUpdate` has:
* `maxUnavailable` - max number of pods that can be unavailable during a rolling update (can be number or percentage). Affects speed of update and availability. Used in cases where you can drop apacity like websites at night.
* `maxSurge` - Used when you don't want to drop below 100% capacity. Can be a number or percentage - defines how many extra resources can be applied during a rollout.

Set `maxUnavailable` to `0` and `maxSurge` to `20%` - ith a service with 10 replicas.
2 new Replica are created, then the oldReplica set is dropped to 8/10 - this continues to gaurentee at least 100% usage.

> Setting `maxSurge` to 100% is equivalent to blue/green deployment.

### Slowing Rollouts to ensure Service Health

The deployment controller relies on a pod's readiness check - without the checks your deployment controller is blind.
You can use `minReadySeconds` to specify seconds before updating the next pod.

    spec:
      minReadySeconds: 60

Sometimes the pod may never become healthy in that case you should set a `progressDeadlineSeconds` (actually in all cases) so that you are notifed when a pod is stuck:

    spec:
      progressDeadlineSeconds: 600

This sets it to 10 minutes - then the deployment is marked as failed.

## Deleting a Deployment

    kubectl delete deployments kuard

or using the declarative yaml file we created earlier:

    kubectl delete -f kuard-deployment.yaml

Deleting the deployment deletes all replicasets and pods.

## Monitoring a Deployment

When a deployment fails to make progress for some time, the deployment will timeout.
The state will turn to `failed`

    status.conditions
    Condition: Progressing
    Status: False

# 11. DaemonSets

Deployments and replicasets are generally about creating a service.
But that is not the only reason for replicating a set of pods, another reason is to schedule a pod per node in a cluster.

The kubernetes resource responsible for this is a `DaemonSet`

They are used to deploy system daemons such as log aggregators and monitoring agents.

Daemonsets share functionality with Replicasets - they create pods for long running services and ensure that current state matches the desired state.

ReplicaSets should be used when the **application is completely decoupled from the node**

DaemonSets should be used when a **single copy of your applications should run on every node in a cluster**.

You may want to run intrusion detection on nodes exposed to the edge network.

They are needed for he requirements of an enterprise IT department requirements.

## Daemonset Scheduler

A daemonset will create a pod on every node unless a node selector is used.
They are ignored by the kubernetes scheduler, the daemonset controller is in charge of state management.

THe decoupled nature mean that pods in a daemonset or a replicaset can be inspected the same way.

    kubectl logs <pod-name>

## Creating DaemonSets

Lets create a `fluentd` logging agent on every node in a cluster.

`fluentd.yaml`:

    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: fluentd
      labels:
        app: fluentd
    spec:
      selector:
        matchLabels:
          app: fluentd
      template:
        metadata:
          labels:
            app: fluentd
        spec:
          containers:
          - name: fluentd
            image: fluent/fluentd:v0.14.10
            resources:
              limits:
                memory: 200Mi
              requests:
                cpu: 100m
                memory: 200Mi
            volumeMounts:
            - name: varlog
              mountPath: /var/log
            - name: varlibdockercontainers
              mountPath: /var/lib/docker/containers
              readOnly: true
          terminationGracePeriodSeconds: 30
          volumes:
          - name: varlog
            hostPath:
              path: /var/log
          - name: varlibdockercontainers
            hostPath:
              path: /var/lib/docker/containers

Daemonsets require a unique name across all daemonsets in a k8s namespace.

Get daemonsets

    $ kubectl get daemonset
    NAME      DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
    fluentd   1         1         1       1            1           <none>          109s

Describe daemonset

    $ kubectl describe ds fluentd
    Name:           fluentd
    Selector:       app=fluentd
    Node-Selector:  <none>
    Labels:         app=fluentd
    Annotations:    deprecated.daemonset.template.generation: 1
                    kubectl.kubernetes.io/last-applied-configuration:
                    {"apiVersion":"apps/v1","kind":"DaemonSet","metadata":{"annotations":{},"labels":{"app":"fluentd"},"name":"fluentd","namespace":"default"}...
    Desired Number of Nodes Scheduled: 1
    Current Number of Nodes Scheduled: 1
    Number of Nodes Scheduled with Up-to-date Pods: 1
    Number of Nodes Scheduled with Available Pods: 1
    Number of Nodes Misscheduled: 0
    Pods Status:  1 Running / 0 Waiting / 0 Succeeded / 0 Failed
    Pod Template:
    Labels:  app=fluentd
    Containers:
    fluentd:
        Image:      fluent/fluentd:v0.14.10
        Port:       <none>
        Host Port:  <none>
        Limits:
        memory:  200Mi
        Requests:
        cpu:        100m
        memory:     200Mi
        Environment:  <none>
        Mounts:
        /var/lib/docker/containers from varlibdockercontainers (ro)
        /var/log from varlog (rw)
    Volumes:
    varlog:
        Type:          HostPath (bare host directory volume)
        Path:          /var/log
        HostPathType:  
    varlibdockercontainers:
        Type:          HostPath (bare host directory volume)
        Path:          /var/lib/docker/containers
        HostPathType:  
    Events:
    Type    Reason            Age   From                  Message
    ----    ------            ----  ----                  -------
    Normal  SuccessfulCreate  15h   daemonset-controller  Created pod: fluentd-wxpx6

Showing it was deployed to the single node of `minikube`

Get the relevant pods:

    $ kubectl get pods -o wide --selector="app=fluentd"
    NAME            READY   STATUS    RESTARTS   AGE     IP           NODE       NOMINATED NODE   READINESS GATES
    fluentd-wxpx6   1/1     Running   0          3m50s   172.17.0.6   minikube   <none>           <none>

Adding a new node will automatically add the pod to that node.

## Limiting DaemonSets to a Specific Node

Suppose you want to deploy a pod to a subset of notes - ones that have a GPU or faster access to storage.
In this case node labels can tag specific nodes that meet the workload requirements.

### Adding Labels to Nodes

For example add a `ssd=true` to a single node

    $ kubectl get nodes
    NAME       STATUS   ROLES    AGE   VERSION
    minikube   Ready    <none>   13d   v1.16.2

    kubectl label nodes minikube ssd=true

Select the nodes matching that label

    $ kubectl get nodes --selector ssd=true
    NAME       STATUS   ROLES    AGE   VERSION
    minikube   Ready    <none>   13d   v1.16.2

### Node Selectors

Node selectors can be used to limit what nodes a pod can run on a given k8s cluster

For example a DaemonSet configuration to limit nginx to running only on nodes with `ssd=true`

**nginx-fast-storage.yaml**

    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      labels:
        app: nginx
        ssd: "true"
      name: nginx-fast-storage
    spec:
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
            ssd: "true"
        spec:
          nodeSelector:
            ssd: "true"
          containers:
            - name: nginx
              image: nginx:1.10.0

Adding the `ssd=true` label to a node means that the daemonset will automatically deploy to that node.
The inverse is also true, if a label is deleted.

## Updating a DaemonSet

Prior to k8s 1.6, the only way to update pods managed by the daemonset was to update the daemonset and manually delete each pod so the daemonset recreates it.

In 1.6, Daemonsets gained the equivalent of a deployment object.

### Rolling Update of a Daemonset

The `RollingUpdate` strategy can be used.

* `spec.updateStrategy.type: RollingUpdate`
* Any change to `spec.template` will initiate a rolling update

2 parameters control the rolling update:
* `spec.minReadySeconds` - how long a pod must be ready before rolling update proceeds
* `spec.updateStrategy.rollingUpdate.maxUnavailable` - how many pods can be simultaneously updated

Likely want to set `spec.minReadySeconds` to `30-60 seconds`

`spec.updateStrategy.rollingUpdate.maxUnavailable` is application dependant - setting to 1 increases the time of rollout. Increasing this increases the speed of rollout but increases the blast radius.

Check status with:

    kubectl rollout status daemonSets my-daemon-set

## Deleting a Daemonset

Use:

    kubectl delete -f fluentd.yaml

> Deleting the daemonset will delete all the pods, set `--cascade=False` to ensure only the daemonset is deleted and not the pods

# 12. Jobs

So far we have looked at long running processes such as db's or web applications.
These workloads run until they are upgraded or the service is no longer needed.

There is often a need for short-lived one-off tasks - the `Job` object is made for handling these types of tasks.

A job creates a pod that runs until successful termination (exit with 0).
Whereas a regular pod will continually restart regardless of the exit code.

Jobs are useful for things you only want to do once - like a db migration or batch job.

## The Job Object

Responsible for creating and managing pods defined in a template in a job spec.
These pods generally run until completion.

There is a chance your job will not execute if the required resources are not found by the scheduler.
Also a small chance that duplicate podswill be created.

## Job Patterns

Jobs are designed to manage batch-like workloads where work items are processed by one or more pods.
Each job runs a single pod until successful termination.

* One shot: Run once until completion (database migration) - `completions=1`, `parrallelism=1`
* One or more pods running one or more times until a completion point - `completions=+1`, `parrallelism=1+`
* One or more pods running until successful termination - `completitions=1`, `parrallelism=2+`

A pod template must be defined in the job configuration. Once a job is up and running - the pod backing the job must be monitored for successful termination.
The job controller is responsible for recreating a pod until successful termination.

    kubectl run -i oneshot --image=gcr.io/kuar-demo/kuard-amd64:blue --restart=OnFailure -- --keygen-enable --keygen-exit-on-complete --keygen-num-to-gen 10

* `-i` indicates an interactive command so it waits until the job is running and then shows the log output
* `--restart=OnFailure` tells kubectl to create a job object
* All options after `--` are command-line arguments to the container image.

I think the job failed for me:

    $ kubectl get jobs
    NAME      COMPLETIONS   DURATION   AGE
    oneshot   0/1           24m        24m

> After the job has completed, the Job object and related Pod are still around. This is so that you can inspect the log output.

    kubectl delete jobs oneshot

**job-oneshot.yaml**:

    apiVersion: batch/v1
    kind: Job
    metadata:
      name: oneshot
    spec:
      template:
        spec:
          containers:
          - name: kuard
            image: gcr.io/kuar-demo/kuard-amd64:blue
            imagePullPolicy: Always
            args:
            - "--keygen-enable"
            - "--keygen-exit-on-complete"
            - "--keygen-num-to-gen=10"
          restartPolicy: OnFailure

Create with:

    kubectl apply -f job-oneshot.yaml

Describe the job with:

    $ kubectl describe jobs/oneshot
    Name:           oneshot
    Namespace:      default
    Selector:       controller-uid=3f05b1a2-39ae-4fef-98ed-f53b193aef75
    Labels:         controller-uid=3f05b1a2-39ae-4fef-98ed-f53b193aef75
                    job-name=oneshot
    Annotations:    kubectl.kubernetes.io/last-applied-configuration:
                    {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"name":"oneshot","namespace":"default"},"spec":{"template":{"spec":{"co...
    Parallelism:    1
    Completions:    1
    Start Time:     Wed, 18 Dec 2019 03:12:37 +0200
    Pods Statuses:  0 Running / 0 Succeeded / 1 Failed
    Pod Template:
    Labels:  controller-uid=3f05b1a2-39ae-4fef-98ed-f53b193aef75
            job-name=oneshot
    Containers:
    kuard:
        Image:      gcr.io/kuar-demo/kuard-amd64:blue
        Port:       <none>
        Host Port:  <none>
        Args:
        --keygen-enable
        --keygen-exit-on-complete
        --keygen-num-to-gen=10
        Environment:  <none>
        Mounts:       <none>
    Volumes:        <none>
    Events:
    Type     Reason                Age   From            Message
    ----     ------                ----  ----            -------
    Normal   SuccessfulCreate      31h   job-controller  Created pod: oneshot-6f9bx
    Normal   SuccessfulDelete      31h   job-controller  Deleted pod: oneshot-6f9bx
    Warning  BackoffLimitExceeded  31h   job-controller  Job has reached the specified backoff limit

**It failed!**

> Jobs have a finite beginning and end - users create many of them. That is why labels are automatically assigned to pods. 

### Pod Failure

Sometimes a pod has a bug in the code and the pod enters a `CrashLoopBackOff`.

K8s will wait a bit before restarting the pod, to prevent excess resource usage on the node.

If you set `restartPolicy: Never` you are telling k8s to not restart the pod on failure, but rather declare the pod as failed. This creates alot of junk.

Delete the jobs with:

    kubectl delete jobs oneshot

You can use liveness probes with jobs, if a liveness policy determines a pod is dead it'll be restarted and replaced for you.

### Parallelism

Generating keys can be slow.

Set `completions=10` and `paralelism=5`

**job-parallel.yaml**

    apiVersion: batch/v1
    kind: Job
    metadata:
      name: parallel
      labels:
        chapter: jobs
    spec:
      parallelism: 5
      completions: 10
      template:
        metadata:
          labels:
            chapter: jobs
        spec:
          containers:
          - name: kuard
            image: gcr.io/kuar-demo/kuard-amd64:blue
            imagePullPolicy: Always
            command: ["/kuard"]
            args:
            - "--keygen-enable"
            - "--keygen-exit-on-complete"
            - "--keygen-num-to-gen=10"
          restartPolicy: OnFailure

It did not work out as expected for me, I watched the pods:

    $ kubectl get pods -w
    NAME                       READY   STATUS              RESTARTS   AGE
    nginx-fast-storage-wknfz   1/1     Running             0          128m
    parallel-kcvxt             0/1     ContainerCreating   0          10s
    parallel-lpttv             0/1     ContainerCreating   0          10s
    parallel-ng5xd             0/1     RunContainerError   0          10s
    parallel-pjwdz             0/1     ContainerCreating   0          10s
    parallel-vnskl             0/1     ContainerCreating   0          10s
    parallel-pjwdz             0/1     RunContainerError   0          11s
    parallel-lpttv             0/1     RunContainerError   0          13s
    parallel-vnskl             0/1     RunContainerError   0          16s
    parallel-kcvxt             0/1     RunContainerError   0          19s
    parallel-ng5xd             0/1     RunContainerError   1          22s
    parallel-pjwdz             0/1     RunContainerError   1          25s
    parallel-lpttv             0/1     RunContainerError   1          28s
    parallel-vnskl             0/1     RunContainerError   1          31s
    parallel-kcvxt             0/1     RunContainerError   1          35s
    parallel-ng5xd             0/1     CrashLoopBackOff    1          36s
    parallel-pjwdz             0/1     CrashLoopBackOff    1          38s
    parallel-vnskl             0/1     CrashLoopBackOff    1          43s
    parallel-lpttv             0/1     CrashLoopBackOff    1          43s
    parallel-pjwdz             0/1     RunContainerError   2          45s
    parallel-kcvxt             0/1     Terminating         1          45s
    parallel-vnskl             0/1     Terminating         1          45s
    parallel-lpttv             0/1     Terminating         1          45s
    parallel-pjwdz             0/1     Terminating         2          45s
    parallel-ng5xd             0/1     Terminating         1          45s
    parallel-kcvxt             0/1     Terminating         1          45s
    parallel-vnskl             0/1     Terminating         1          45s
    parallel-ng5xd             0/1     Terminating         2          45s
    parallel-lpttv             0/1     Terminating         1          45s
    parallel-pjwdz             0/1     Terminating         2          45s
    parallel-ng5xd             0/1     Terminating         2          46s
    parallel-kcvxt             0/1     Terminating         1          48s
    parallel-kcvxt             0/1     Terminating         1          48s
    parallel-pjwdz             0/1     Terminating         2          48s
    parallel-pjwdz             0/1     Terminating         2          48s
    parallel-vnskl             0/1     Terminating         1          49s
    parallel-vnskl             0/1     Terminating         1          49s
    parallel-ng5xd             0/1     Terminating         2          50s
    parallel-ng5xd             0/1     Terminating         2          50s
    parallel-lpttv             0/1     Terminating         1          50s
    parallel-lpttv             0/1     Terminating         1          50s

You can get the events causing the error:

    kubectl get events --sort-by=.metadata.creationTimestamp

That said the error:

    41m         Normal    Created                pod/parallel-ng5xd   Created container kuard
    41m         Warning   Failed                 pod/parallel-ng5xd   Error: failed to start container "kuard": Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "exec: \"--keygen-enable\": executable file not found in $PATH": unknown

[Source of the above answer](https://stackoverflow.com/questions/41604499/my-kubernetes-pods-keep-crashing-with-crashloopbackoff-but-i-cant-find-any-lo)

The problem was no command: `command: ["/kuard"]` which I added to the container spec.

    $ kubectl get pods -w
    NAME                       READY   STATUS              RESTARTS   AGE
    nginx-fast-storage-wknfz   1/1     Running             0          157m
    parallel-gfb4m             0/1     ContainerCreating   0          2s
    parallel-ll5fz             0/1     ContainerCreating   0          2s
    parallel-qjtgd             0/1     ContainerCreating   0          2s
    parallel-qlwbs             0/1     ContainerCreating   0          2s
    parallel-srq8z             0/1     ContainerCreating   0          2s
    parallel-qlwbs             1/1     Running             0          5s
    parallel-srq8z             1/1     Running             0          8s
    parallel-qjtgd             1/1     Running             0          11s
    parallel-ll5fz             1/1     Running             0          15s
    parallel-gfb4m             1/1     Running             0          18s
    parallel-qlwbs             0/1     Completed           0          102s
    parallel-ltbvb             0/1     Pending             0          0s
    parallel-ltbvb             0/1     Pending             0          0s
    parallel-ltbvb             0/1     ContainerCreating   0          0s
    parallel-ltbvb             1/1     Running             0          7s
    parallel-srq8z             0/1     Completed           0          112s
    parallel-k725g             0/1     Pending             0          0s
    parallel-k725g             0/1     Pending             0          0s
    parallel-k725g             0/1     ContainerCreating   0          0s
    parallel-qjtgd             0/1     Completed           0          115s
    parallel-xt5tk             0/1     Pending             0          0s
    parallel-xt5tk             0/1     Pending             0          0s
    parallel-xt5tk             0/1     ContainerCreating   0          0s
    parallel-ll5fz             0/1     Completed           0          118s
    parallel-zw49p             0/1     Pending             0          0s
    parallel-zw49p             0/1     Pending             0          0s
    parallel-k725g             1/1     Running             0          6s
    parallel-zw49p             0/1     ContainerCreating   0          0s
    parallel-xt5tk             1/1     Running             0          6s
    parallel-zw49p             1/1     Running             0          6s
    parallel-gfb4m             0/1     Completed           0          2m48s
    parallel-92fw6             0/1     Pending             0          0s
    parallel-92fw6             0/1     Pending             0          0s
    parallel-92fw6             0/1     ContainerCreating   0          0s
    parallel-92fw6             1/1     Running             0          6s
    parallel-zw49p             0/1     Completed           0          66s
    parallel-ltbvb             0/1     Completed           0          83s
    parallel-xt5tk             0/1     Completed           0          104s
    parallel-k725g             0/1     Completed           0          110s

To view the keys, check the job:

    $ kubectl describe job parallel
    Name:           parallel
    Namespace:      default
    Selector:       controller-uid=967166ca-3480-4e7c-88d7-87dcfff0507c
    Labels:         chapter=jobs
    Annotations:    kubectl.kubernetes.io/last-applied-configuration:
                    {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"chapter":"jobs"},"name":"parallel","namespace":"default"},"s...
    Parallelism:    5
    Completions:    10
    Start Time:     Wed, 18 Dec 2019 04:39:11 +0200
    Completed At:   Wed, 18 Dec 2019 04:43:04 +0200
    Duration:       3m53s
    Pods Statuses:  0 Running / 10 Succeeded / 0 Failed
    Pod Template:
    Labels:  chapter=jobs
            controller-uid=967166ca-3480-4e7c-88d7-87dcfff0507c
            job-name=parallel
    Containers:
    kuard:
        Image:      gcr.io/kuar-demo/kuard-amd64:blue
        Port:       <none>
        Host Port:  <none>
        Command:
        /kuard
        --keygen-enable
        --keygen-exit-on-complete
        --keygen-num-to-gen=10
        Environment:  <none>
        Mounts:       <none>
    Volumes:        <none>
    Events:
    Type    Reason            Age   From            Message
    ----    ------            ----  ----            -------
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-qlwbs
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-srq8z
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-qjtgd
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-gfb4m
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-ll5fz
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-ltbvb
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-k725g
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-xt5tk
    Normal  SuccessfulCreate  31h   job-controller  Created pod: parallel-zw49p
    Normal  SuccessfulCreate  31h   job-controller  (combined from similar events): Created pod: parallel-92fw6

Then get the logs of the pod to view the keys generated:

    kubectl logs parallel-qlwbs

    ...
    2019/12/18 02:39:16 Serving on HTTP on :8080
    2019/12/18 02:39:27 (ID 0 1/10) Item done: SHA256:1s0bwfuxiEmal1NoYVSlYgoyz3V3I9hjO0dHJ/YD0UM
    2019/12/18 02:39:29 (ID 0 2/10) Item done: SHA256:NgjpYmiHa5/V+Zme+bcAM0tWZsEJbkXxpgHzdY0BNmQ
    2019/12/18 02:39:37 (ID 0 3/10) Item done: SHA256:h0eZaM5Cq7Pxs6Rj9CbLFCadyN1JOiNu4p4MbIq2JpY
    2019/12/18 02:39:37 (ID 0 4/10) Item done: SHA256:4CMGwCKTCxvTxK5cVQ69Bm0S4XpjdfbKJ8AW5zYJbhs
    2019/12/18 02:39:54 (ID 0 5/10) Item done: SHA256:1ZgtS+9Wnw9qVCPOtpuvWw7/egpOyMupW3lTe//q/oA
    2019/12/18 02:40:10 (ID 0 6/10) Item done: SHA256:YmAIHf55NNh/wk1kIzueqFbc0o/qLj2g4gsEQiWU468
    2019/12/18 02:40:17 (ID 0 7/10) Item done: SHA256:1BeE92jMTr6p9Y7lh2hRytU/Fv5myxQmcr/5kSL22zU
    2019/12/18 02:40:27 (ID 0 8/10) Item done: SHA256:40b+yqosWRV1SlP4JvT/k6IaLeusBuRe7P7HYdjrIAc
    2019/12/18 02:40:32 (ID 0 9/10) Item done: SHA256:reu+UWnFO+GNCll8O/xNf8JEV/pZivImUYLKdzUixS0
    2019/12/18 02:40:52 (ID 0 10/10) Item done: SHA256:GfLpuGv696ce3fboMyHHWlcdAbeXSFX4jXzO0WnB8dY
    2019/12/18 02:40:52 (ID 0) Workload exiting
    ...

### Work Queues

A common case is for jobs to process work from a work queue.
1 task creates a number of work items and publishes them to a work queue.
A worker job can be run to process each work item until the work queue is empty.

    Producer -> Work Queue -> Consumer

We start by launching a centralised work queue service.

> we create a simple ReplicaSet to manage a singleton work queue daemon

`rs-queue.yaml`:

    apiVersion: apps/v1
    kind: ReplicaSet
    metadata:
      labels:
        app: work-queue
        component: queue
        chapter: jobs
      name: queue
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: work-queue
      template:
        metadata:
          labels:
            app: work-queue
            component: queue
            chapter: jobs
        spec:
          containers:
          - name: queue
            image: "gcr.io/kuar-demo/kuard-amd64:blue"
            imagePullPolicy: Always

Set the queue pod:

    QUEUE_POD=$(kubectl get pods -l app=work-queue,component=queue -o jsonpath='{.items[0].metadata.name}')

Forward to the port:

    kubectl port-forward $QUEUE_POD 8080:8080

Let us expose it as a service to make it easy for producers and consumers to locate the work queue via DNS.

**service-queue.yaml**

    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: work-queue
        component: queue
        chapter: jobs
      name: queue
    spec:
      ports:
      - port: 8080
        protocol: TCP
        targetPort: 8080
      selector:
        app: work-queue
        component: queue

Create a queue:

    http PUT localhost:8080/memq/server/queues/keygen

put this in `load-queue.sh`:

    for i in work-item-{0..99}; do
    curl -X POST localhost:8080/memq/server/queues/keygen/enqueue \
        -d "$i"
    done

### Now the Consumer

    apiVersion: batch/v1
    kind: Job
    metadata:
      labels:
        app: message-queue
        component: consumer
        chapter: jobs
      name: consumers
    spec:
      parallelism: 5
      template:
        metadata:
          labels:
            app: message-queue
            component: consumer
            chapter: jobs
        spec:
          containers:
          - name: worker
            image: "gcr.io/kuar-demo/kuard-amd64:blue"
            imagePullPolicy: Always
            command: ["/kuard"]
            args:
            - "--keygen-enable"
            - "--keygen-exit-on-complete"
            - "--keygen-memq-server=http://queue:8080/memq/server"
            - "--keygen-memq-queue=keygen"
          restartPolicy: OnFailure

There are now 5 pods:

    $ kubectl get pods -w
    NAME                       READY   STATUS      RESTARTS   AGE
    consumers-2schk            1/1     Running     0          21s
    consumers-5ktf8            1/1     Running     0          21s
    consumers-fh8m7            1/1     Running     0          21s
    consumers-jlwsn            1/1     Running     0          21s
    consumers-qcvwz            1/1     Running     0          21s

these will continue to work until the queue is empty

### Cleanup

    kubectl delete rs,svc,job -l chapter=jobs

### Cron Jobs

Sheduling a job. A `Cronjob` is responsible for creating a new Job object at particular intervals.

    apiVersion: batch/v1beta1
    kind: CronJob
    metadata:
      name: example-cron
    spec:
      # Run every fifth hour
      schedule: "0 */5 * * *"
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - name: batch-job
                image: my-batch-image
              restartPolicy: OnFailure

* `spec.schedule` is the standard cron format

Get details with:

    $ kubectl describe cronjob.batch/example-cron
    Name:                          example-cron
    Namespace:                     default
    Labels:                        <none>
    Annotations:                   kubectl.kubernetes.io/last-applied-configuration:
                                    {"apiVersion":"batch/v1beta1","kind":"CronJob","metadata":{"annotations":{},"name":"example-cron","namespace":"default"},"spec":{"jobTempl...
    Schedule:                      0 */5 * * *
    Concurrency Policy:            Allow
    Suspend:                       False
    Successful Job History Limit:  3
    Failed Job History Limit:      1
    Starting Deadline Seconds:     <unset>
    Selector:                      <unset>
    Parallelism:                   <unset>
    Completions:                   <unset>
    Pod Template:
      Labels:  <none>
      Containers:
      batch-job:
        Image:           my-batch-image
        Port:            <none>
        Host Port:       <none>
        Environment:     <none>
        Mounts:          <none>
      Volumes:           <none>
    Last Schedule Time:  <unset>
    Active Jobs:         <none>
    Events:              <none>

# 13. ConfigMaps and Secrets

> It is good practice to make container images as reusable as possible

The same image should be used for development, staging and production

Testing and versioning gets difficult if the image needs to be recreated for each environment

How do we specialise he use of the image t runtime?

We use `ConfigMap` and `secrets`

ConfigMaps - provide config information for workloads
Secrets - provide config information of a sensitive nature (crednetials or TLS certificates)

## ConfigMaps

* Think of it as a small filesystem
* They are used to define the environment

The ConfigMap is combined with the pod right before it is run.
This means the container image and pod defintion can be reused across apps by just changing the `ConfigMap` used

### Creating ConfigMaps

You can create these imperitively or declaratively.

Create a config file: `my-config.txt`

    parameter1 = value1
    parameter2 = value2

then create a `ConfigMap` from it:

    kubectl create configmap my-config --from-file=my-config.txt --from-literal=extra-param=extra-value --from-literal=another-param=another-value

the equivalent yaml is:

    $ kubectl get configmaps my-config -o yaml
    apiVersion: v1
    data:
      exta-param: extra-value
      my-config.txt: |
        parameter1 = value1
        parameter2 = value2
    kind: ConfigMap
    metadata:
      creationTimestamp: "2019-12-18T08:31:03Z"
      name: my-config
      namespace: default
      resourceVersion: "408037"
      selfLink: /api/v1/namespaces/default/configmaps/my-config
      uid: c8d227af-1932-424d-acd4-88bff381d26b

A configMap is basically key-value pairs stored, the interesting happens when you try use a ConfigMap.

## Using a ConfigMap

3 ways:
* filesystem - mount a configmap into a pod - a file is created for each entry
* environment variable - dynamically set the value of an environment variable
* command-line argument - k8s supports dynamically creating the command line for a container from ConfigMap values

For filesystem we create a new volume and give it the name `config-volume`. 
We define this volume to be a `ConfigMap` volume and point at the `ConfigMap` to mount.
We specify where this is mounted in the container with a `volumeMount` - most cases we mount at `/config`

Environment variables are specified with the `valueFrom` member - that refernces the configmap with `configMapKeyRef`

Commandline arguments build on environment variables with the special `$(env-var-name)` syntax - as a command in the yaml.

Eg. `kuard-config.yaml`

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard-config
    spec:
      containers:
        - name: test-container
          image: gcr.io/kuar-demo/kuard-amd64:blue
          imagePullPolicy: Always
          command:
            - "/kuard"
            - "$(EXTRA_PARAM)"
          env:
            - name: ANOTHER_PARAM
              valueFrom:
                configMapKeyRef:
                  name: my-config
                  key: another-param
            - name: EXTRA_PARAM
              valueFrom:
                configMapKeyRef:
                  name: my-config
                  key: extra-param
          volumeMounts:
            - name: config-volume
              mountPath: /config
      volumes:
        - name: config-volume
          configMap:
            name: my-config
      restartPolicy: Never

In my case I get a `CreateContainerConfigError` on the pod, because I didn't specify `another-param`. I got this error with `kubectl get events`:

    $ kubectl get events
    LAST SEEN   TYPE      REASON      OBJECT             MESSAGE
    <unknown>   Normal    Scheduled   pod/kuard-config   Successfully assigned default/kuard-config to minikube
    41s         Normal    Pulling     pod/kuard-config   Pulling image "gcr.io/kuar-demo/kuard-amd64:blue"
    52s         Normal    Pulled      pod/kuard-config   Successfully pulled image "gcr.io/kuar-demo/kuard-amd64:blue"
    52s         Warning   Failed      pod/kuard-config   Error: couldn't find key another-param in ConfigMap default/my-config

Something was up and I changed something.

If we port forward to that container we can view the server env:

    kubectl port-forward kuard-config 8080

In the filesystem browser - you can see the config files and values in `/config` and the config file `my-config.txt`

## Secrets

Certain data is sensitive - password, security tokens or other types of private keys

Secrets enable contianer images to be created without bundling sensitive data.
Allowing containers to be portable across environments.

> By default kubernetes secrets are stored in plain text in `etcd` storage. Anyone who has cluster admin can read all the secrets in a cluster. Most cloud key stores have integration with Kubernetes flexible volumes, enabling you to skip Kubernetes secrets entirely

### Creating Secrets

> Container images should not bundle TLS ceritficates or keys so they can remain portable and distributable through public docker registries

Obtain the rax data we want to store

    curl -o kuard.crt  https://storage.googleapis.com/kuar-demo/kuard.crt
    curl -o kuard.key https://storage.googleapis.com/kuar-demo/kuard.key

Create the secret with:

    kubectl create secret generic kuard-tls --from-file=kuard.crt --from-file=kuard.key

The secret was created with two data elements.
Get the details with:

    $ kubectl describe secrets kuard-tls
    Name:         kuard-tls
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>

    Type:  Opaque

    Data
    ====
    kuard.crt:  1050 bytes
    kuard.key:  1679 bytes

We consume the secrets with a secrets volume.

### Consuming Secrets

They can be consumed using the k8s rest api

However to keep the pplicaiton protable - ie. requiring no modification to acquire the secrets we use a secrets volume.

#### Secrets Volume

Secrets are exposed to pods using the secrets volume type.
Secrets volumes are managed by the `kubelet` and are created at pod creation time.
Secrets are stored on `tmpfs` volumes and are not written to disk on nodes.

Each data element of a secret is stored in a seperate file under the target mount point.
The `kuard-tls` secret container `kuard.crt` and `kuard.key`

Mounting the `kuard-tls` secrets to `/tls` results in:

    /tls/kuard.crt
    /tls/kuard.key

Delcare a secret with

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard-tls
    spec:
      containers:
        - name: kuard-tls
          image: gcr.io/kuar-demo/kuard-amd64:blue
          imagePullPolicy: Always
          volumeMounts:
          - name: tls-certs
            mountPath: "/tls"
            readOnly: true
      volumes:
        - name: tls-certs
          secret:
            secretName: kuard-tls

After apply, port forward to https port and check it out:

    kubectl port-forward kuard-tls 8443:8443

then go to: https://localhost:8443/

## Private Docker Registries

A special use case is to store access credentials to private docker registries.

`Image pull secrets` leverage the secrets API to automate the ditribution of private registry credentials.

They are just like regular secrets but except they are consumed through `spec.imagePullSecrets`

Create an image pull secret:

    kubectl create secret docker-registry my-image-pull-secret --docker-username=<docker-username> --docker-password=<password> --docker-email=<email-address>

You then give access to the pod (for the imagepull secret) with:

`kuard-registry.yaml`:

    apiVersion: v1
    kind: Pod
    metadata:
      name: kuard-tls
    spec:
      containers:
        - name: kuard-tls
          image: gcr.io/kuar-demo/kuard-amd64:blue
          imagePullPolicy: Always
          volumeMounts:
          - name: tls-certs
            mountPath: "/tls"
            readOnly: true
      imagePullSecrets:
      - name:  my-image-pull-secret
      volumes:
        - name: tls-certs
          secret:
            secretName: kuard-tls

> If you are repeatedly pulling from the same registry, you can add the secrets to the default service account associated with each Pod to avoid having to specify the secrets in every Pod you create

## Naming Constraints

Valid key names:
* `.auth_token`
* `Key.pem`
* `config_file`

Invalid key names:
* `Token..properties`
* `auth file.json`
* `_password.txt`

Configmaps are `UTF-8` text. They are unable to store binary but can store base64.
THe maximum size of a ConfigMap or Secret is 1MB.

## Managing ConfigMaps and Secrets

The usual `create`, `delete`, `get` and `decscribe` commands work.

### Listing

    kubectl get secrets

    kubectl get configmaps

    $ kubectl describe cm my-config
    Name:         my-config
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>

    Data
    ====
    another-param:
    ----
    another-value
    extra-param:
    ----
    extra-value
    my-config.txt:
    ----
    parameter1 = value1
    parameter2 = value2

    Events:  <none>

You can view raw data with:

    $ kubectl get cm my-config -o yaml
    apiVersion: v1
    data:
      another-param: another-value
      extra-param: extra-value
      my-config.txt: |
        parameter1 = value1
        parameter2 = value2
    kind: ConfigMap
    metadata:
      creationTimestamp: "2019-12-18T08:55:40Z"
      name: my-config
      namespace: default
      resourceVersion: "410659"
      selfLink: /api/v1/namespaces/default/configmaps/my-config
      uid: a21d5265-e699-40a6-b351-0d18945a0bef

or get a secret with:

    kubectl get secret kuard-tls -o yaml

### Creating

    kubectl create secret generic

or

    kubectl create configmap

with:
* `--from-file=<filename>`
* `--from-file=<key>=<filename>`
* `--from-file=<directory>`
* `--from-literal=<key>=<value>`

### Updating

#### Update from file

Just update the ConfigMap or secret and run:

    kubectl replace -f <filename>

or

    kubectl apply -f <filename>

> Oftentimes the manifests are checked into source control

**It is a bad idea to check secret yaml files into source control**

#### Recreate and Update

If you store the inputs as seperate files on the disk you can use:

    kubectl create secret generic kuard-tls \
    --from-file=kuard.crt --from-file=kuard.key \
    --dry-run -o yaml | kubectl replace -f -

Here to tell kubectl to just dump the `yaml` it would send to the API server and pipe that to `kubectl replace ...`

#### Edit Current Version

    kubectl edit configmap my-config

#### Live Updates

When a configmap or secret is updated via API, it is automatically pushed to the volumes.
So you can update the config of applications without restarting them. 
It is up to the applcation to update to new settings.

# 14. RBAC (Role Based Access Control) for k8s

Introduced in version 1.5 and becoming generally available in 1.8.

RBAC restricts access to actions on the kubernetes API.
It is critical to hardening access to a k8s cluster, to prevent one person in a namespace taking out a production cluster.

Multitenant security is complex and multifaceted.

> In a hostile security environment do not beleive that RBAC by itself is enough to protect you. In this case isolation should be done with a hypervisor.

Authentication - Getting the identity, it should integrate with a pluggable identity provider - k8s does not have a built in identity store.
Authorization - Once identified, authorization determines whether the identity is allowed to perform an action of access a resource.

## RBAC

Every request in k8s is associated with an identity. Even a request with no identity is associated with `system:unauthenticated`. 

k8s uses a generic interface for authentication provider - each provider supplies a username and set of groups a user belongs to.

K8s supports:
* HTTP basic auth (deprecated)
* x509 client certificates
* Static token files on the host
* Cloud auth providers (Azure active directory or AWS IAM) - or Open Source Single-sign On Identity providers (like keycloak)
* Authentication webhooks

### Understanding Roles and Role Bindings

To determine authorization roles and role bindings are used.

* `role` - set of abstract capabilities. Eg. `appdev` can create pods and services.
* `role binding` - assignment of one or more roles to an identity. Eg. binding `appdev` role to the `alice` user.

### Roles and Role Bindings in K8s

Two types:
* Namespaces - `Role` and `RoleBinding`
* Across cluster - `ClusterRole` and `ClusterRoleBinding`

`Role` and `RoleBinding` only work within a specific namespace

This role gives ability to create pods and services

    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      namespace: default
      name: pod-and-services
    rules:
    - apiGroups: [""]
      resources: ["pods", "services"]
      verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]

To bind this role to `alice` we create a `RoleBinding`

    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      namespace: default
      name: pods-and-services
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: alice
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: mydevs
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: pod-and-services

For limiting access to cluster level resources use `ClusterRole` and `ClusterRoleBinding`

### K8s Verbs

* `create`
* `delete`
* `get`
* `list`
* `patch`
* `update`
* `watch`
* `proxy`

### Built-in Roles

    kubectl get clusterroles

Most of the roles are for system utilities: `system`

There are 4 types of user roles:
* `cluster-admin` - complete access to the entire cluster
* `admin` - access to the complete namespace
* `edit` - allow you to modify a namespace
* `view` - read only access to a namespace

> Any built-in cluster role, those modifications are transient. Whenever the API server is restarted (e.g., for an upgrade) your changes will be overwritten.

To preventt this you need to set gthe annotation:

    rbac.authorization.kubernetes.io/autoupdate: False

> By default k8s allows `system:unauthenticated` to the API discovery endpoint - in hostile environments (zero trust) you should ensure `--anonymous-auth=false`

## Techniques for managing RBAC

### Can-I Tool

    kubectl auth can-i create pods

Can also test subresources

    kubectl auth can-i get pods --subresource=logs

### Managing RBAC in Source COntrol

Like everything in k9s there is a `json` or `yaml` representation

To reconcile roles and role bindings to the current state of the cluster use:

    kubectl auth reconcile -f some-rbac-config.yaml

Add `--dry-run` to print out but not run the changes

## Advanced Topics

### Aggregating Cluster Roles

Cloning clusterroles to others is error prone and time consuming.

> Kubernetes RBAC supports the usage of an aggregation rule to combine multiple roles together in a new role

Some more info in the book...


# 15. Intergrating Storage Solutions and Kubernetes

Decoupling state from applications and building your microservices to be as statless as possible result in maximally reliable, manageable systems.

Integrating data with containers and container orchestrators is often the most complicated aspect of building a complex system.

The move also involves:

* decoupling
* immutable architecture
* declarative application development

Cloud native storage like cassandra or mongodb involve some imperitive steps.

Eg. Setting up a `ReplicaSet` in Mongodb involves deploying the the Mondo daemon and identifying the leader.

Most containerized systems are usually adapted from existing systems deployed into vm's - where data needs to be imported or migrated.

Storage is often an externalised cloud service - it can never really exist inside of the k8s cluster.

Variety of approaches of intergrating storage:

* Importing External services (cloud or vm)
* Reliable singletons running in k8s
* StatefulSets in k8s

## Importing External Services

An existing machine in your network running a database.
In this case you don't want to immediately move the data to k8s.
It could be run by a different team, a gradual move or moving it is just more trouble than it is worth.

**This db will never be in k8s**

It is still worthwhile to represent the server in k8s - to get built in naming, service discovery primitives and makes it look like the database is a k8s service.

Making it easy to replace the service.

Eg. You rely on db in production running on a machine but for testing you deploy the db to transient containers.
Data persistence is not important in this case.

Representing both db's as a k8s service enables you to maintain the same config  - maintaining high fidelity.
So a service will look the same but the `namespace` will differ:

    kind: Service
    metadata:
      name: my-database
      namespace: test

in production:

    kind: Service
    metadata:
      name: my-database
      namespace: prod

When deploying a pod in `test` namespace and look for a pod called `my-database`, it receives a pointer to `my-database.test.svc.cluster.internal` which points to the test db.
When a pod in `prod` looks up `my-database` it will point to the prod db.

### Services without Selectors

With external services there are no labels - instead you have a DNS name to point to the specific server running the database.
Let's say the db is called `database.company.com`

To import this database into k8s, we create a service without a pod selector that references the DNS name of the server:

`dns-service.yaml`

    kind: Service
    apiVersion: v1
    metadata:
      name: external-database
    spec:
      type: ExternalName
      externalName: database.company.com

When a typical k8s service is created - an ip address and DNS record is created.
When you create a service of type `ExternalName`, the k8s dns is populated with a `CNAME` record that points to the external name.

When a lookup is done to `external-database.svc.default.cluster` by a k8s pod, DNS aliases that to `database.company.com`

Cloud providers would also provide you a hostname eg. `my-database.databases.cloudprovider.com`

Sometimes you don't have a DNS address, just an `ip`, in this case it is a bit diffferent.

1. Create a service without a label selector but also without the `ExternalName`
2. Create an endpoint

**external-ip-service.yaml**

    kind: Service
    apiVersion: v1
    metadata:
      name: external-ip-database

K8s will allocate a virtual ip for the service and populate an `A` record for it.

Because there is no selector for the service, there will be no endpoints populated for the load balancer to redirect traffic to.

The user is responsible for populating the endpoints manually:

**external-ip-endpoints.yaml**

    kind: Endpoints
    apiVersion: v1
    metadata:
      name: external-ip-database
    subsets:
      - addresses:
        - ip: 192.168.0.1
        ports:
        - port: 3306

### Limitations of External Services: Health Checking

External services in k8s do not perform health checking - the user is responsible for the realiability of the service.

## Running Reliable Singletons

Challenge of running storage in K8s is that often primitives like `replicaSet` expect every container to be identical and replacable - for most storage solutions that is not the case.

One solution is running a single pod that runs the database or other storage solution.
There is no replication.

> This may seem counter to the principles of reliable distributed systems but it is no more unreliable than running your own database or storage on a single vm.

For smaller systems the downtime tradeoff for upgrades might be worth it.

### Running a MySQL Singleton

You need 3 basic objects:

* A `persistent volume` to manage the lifespan of the disk storage independently from the lifespan of the MySQL application
* A MySQL `pod` that will run the MySQL application
* A `service` that will expose this pod to other containers

Persistent volumes independence is important - should the container database application crash the storage will persist.

We use `NFS` for maximum portability - but you can use something else:
Instead of using `nfs` use `azure`, `awsElasticBlockStore` or `gcePersistentDisk`

**nfs-volume.yaml**

    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: database
      labels:
        volume: my-volume
    spec:
      accessModes:
      - ReadWriteMany
      capacity:
        storage: 1Gi
      nfs:
        server: 192.168.0.1
        path: "/exports"

This defines an NFS `PersistentVolume` object with 1GB of storage.

Once the persisten volume has been created we need to claim the persistent volume for our pod:

**nfs-volume-claim.yaml**

    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: database
    spec:
      accessModes:
      - ReadWriteMany
      resources:
        requests:
          storage: 1Gi
      selector:
        matchLabels:
          volume: my-volume

The reason for this indirection is to isolate the pod defintion from the storage definition.

You can declare a volume in a pod specification, but that locks the pod to a particular volume provider.

A volume claim keeps your pod spec cloud agnostic.

> Furthermore, in many cases, the persistent volume controller will actually automatically create a volume for you

Now we claimed the persistent volume, we can use a `ReplicaSet` to construct our singleton pod.

May be weird to use a `ReplicaSet` to manage a single pod, but it is necessary for reliablity.
Once scheduled to a machine, a bare pod is bound to that machine forever.
If the machine fails, any pods associated to that machine fail as well - and are not rescheduled elsewhere.
If we use a `ReplicaSet` they will be rescheduled.

**mysql-replicaset.yaml**

    apiVersion: apps/v1
    kind: ReplicaSet
    metadata:
      name: mysql
      # labels so that we can bind a Service to this Pod
      labels:
        app: mysql
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: mysql
      template:
        metadata:
          labels:
            app: mysql
        spec:
          containers:
          - name: database
            image: mysql
            resources:
              requests:
                cpu: 1
                memory: 2Gi
            env:
            # Environment variables are not a best practice for security,
            # but we're using them here for brevity in the example.
            # See Chapter 11 for better options.
            - name: MYSQL_ROOT_PASSWORD
              value: some-password-here
            livenessProbe:
              tcpSocket:
                port: 3306
            ports:
            - containerPort: 3306
            volumeMounts:
              - name: database
                # /var/lib/mysql is where MySQL stores its databases
                mountPath: "/var/lib/mysql"
          volumes:
          - name: database
            persistentVolumeClaim:
              claimName: database

The replicaset creates a pod running MySQL using the persistent disk we just created.

Now expose as a service:

**mysql-service.yaml**

    apiVersion: v1
    kind: Service
    metadata:
      name: mysql
    spec:
      ports:
      - port: 3306
        protocol: TCP
      selector:
        app: mysql

We now have a reliable singleton MySQL instance running and exposed as `mysql`
Which we can access with `mysql.svc.default.cluster`

### Dynamic Volume Provisioning

Cluster operator creates one or more `StorageClass` objects - for example on Azure:

**storageclass.yaml**

    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: default
      annotations:
        storageclass.beta.kubernetes.io/is-default-class: "true"
      labels:
        kubernetes.io/cluster-service: "true"
    provisioner: kubernetes.io/azure-disk

Once the storage class is created you can refer to it in your persistent volume claim.

When the dynamic provisioner sees the storage claim - it uses the appropriate volume driver.

**dynamic-volume-claim.yaml**

    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: my-claim
      annotations:
        volume.beta.kubernetes.io/storage-class: default
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi

The `volume.beta.kubernetes.io/storage-class: default` is what links the claim to the storage class

> Automatic provisioning of a persistent volume is a great feature that makes it significantly easier to build and manage stateful applications in Kubernetes - however the lifespan of the persistent volume is determined by the reclaimation policy - which is usually bound to the pod by default. So if you delete the pod the data is deleted.

Persistent volumes are great for traditional applications that require storage.
For highly available scalable storage - you need `StatefulSets`

## Kubernetes-Native Storage with StatefulSets

When k8s started there has an emphasis for replicas being exactly the same in a replicaset.

No replica had an individual identity or configurtion - this approach was good for isolation required for orchestration - it made developing stateful applications difficult.

### Properties of Stateful Sets

They are replicated groups of pods similar to ReplicaSets, with a few differences:

* Each replica gets a persistent hostname with a unique index (`database-0`, `database-1`)
* Each replica is created from lowest to highest index, creation will block until the previous index is healthy and available
* When deleted, each pod is deleted from highest to lowest

This simple solution makes it much easier to deploy storage apps on k8s

The stable hostnames means all replicas (other than the first) can reference the first one reliably - `database-0`

### Manually Replicated MongoDB with StatefulSets

A 3 replica stateful set of Mongo db:

    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: mongo
    spec:
      serviceName: "mongo"
      replicas: 3
      selector:
        matchLabels:
          app: mongo
      template:
        metadata:
          labels:
            app: mongo
        spec:
          containers:
          - name: mongodb
            image: mongo:3.4.1
            command:
            - mongod
            - --replSet
            - rs0
            ports:
            - containerPort: 27017
              name: peer

Getting the pods:

    $ kubectl get pods
    NAME          READY   STATUS    RESTARTS   AGE
    mongo-0       1/1     Running   0          109s
    mongo-1       1/1     Running   0          15s
    mongo-2       1/1     Running   0          12s

Each pod has a numeric index as a suffix

Now we need a headless service to manage the DNS entries for the stateful set

A service is `headless` if it doesn't have a cluster virtual ip

Since in stateful sets each pod has a unique identity it doesn't make sense to have a load-balancing ip address.
You create headless with `clusterIP: None`

**mongo-service.yaml**

    apiVersion: v1
    kind: Service
    metadata:
      name: mongo
    spec:
      ports:
      - port: 27017
        name: peer
      clusterIP: None
      selector:
        app: mongo

There are usually 4 dns entries populated:

    mongo.default.svc.cluster.local
    0⁠.mongo⁠.default⁠.svc⁠.cluster​.local
    mongo-1.mongo 
    mongo-2.mongo

Thus you get well defined stateful names.
You can test out the dns resolution with:

    kubectl run -it --rm --image busybox busybox ping mongo-1.mongo

Now we need to manually setup pod replication

    kubectl exec -it mongo-0 mongo
    > rs.initiate({_id:"rs0", members: [{_id:0, host:"mongo-0.mongo:27017"}]});
    { "ok" : 1 }

This tells `mongodb` to intiate the ReplicaSet `rs0` with `mongo-0.mongo`

> The `rs0` name is arbitrary

Add the other replicas

    rs0:OTHER> rs.add("mongo-1.mongo:27017")
    { "ok" : 1 }
    rs0:PRIMARY> rs.add("mongo-2.mongo:27017")
    { "ok" : 1 }

Now we have a replicated Mongo db instance

### Automating Mongo DB Cluster Creations

More in the book for this - makes use of an `init` script

### Persistent Volumes and Stateful Sets

> because the StatefulSet replicates more than one Pod you cannot simply reference a persistent volume claim. Instead, you need to add a persistent volume claim template

### StateFul Set

Get Stateful sets

    $ kubectl get sts
    NAME    READY   AGE
    mongo   3/3     38m

Delete a stateful set

    $ kubectl delete sts mongo
    statefulset.apps "mongo" deleted

# 16. Extending Kubernetes

More info in the book, seems a deep topic that I will look at later...I also want to learn `go` a bit before

# 17. Deploying Real-World Applications

Using k8s in the real world

## Jupyter

Jupyter is a web0based interactive scientific notebook for explorationa dn experimentation

1. Create a namespace for the application

    kubectl create namespace jupyter

2. Create a deployment

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        run: jupyter
      name: jupyter
      namespace: jupyter
    spec:
      replicas: 1
      selector:
        matchLabels:
          run: jupyter
      template:
        metadata:
          labels:
            run: jupyter
        spec:
          containers:
          - image: jupyter/scipy-notebook:abdb27a6dfbb
            name: jupyter
          dnsPolicy: ClusterFirst
          restartPolicy: Always

3. Watch the pod (it takes a while to create)

    watch kubectl get pods -n jupyter
    
    NAME                       READY   STATUS    RESTARTS   AGE
    jupyter-5bf5d6c5bd-txdmf   1/1     Running   0          14m

4. Get the intial login token

    pod_name=$(kubectl get pods --namespace jupyter --no-headers | awk '{print $1}')
    kubectl logs --namespace jupyter ${pod_name}

5. Port forward

    kubectl port-forward ${pod_name} 8888:8888 -n jupyter
    
6. Visit the site

    http://localhost:8888/login?token=xxx

## Parse

Parse server is a cloud API dedicated to providing easy-to-use storage for mobile applications.
Facebook bought it in 2013 and shut it down.

Parse uses Mongo Db for storage - so we assume you have that 3 node statefulset up.

The open source `parse-server` comes with a `Dcokerfile` for easy containerisation.

If you want to build your own image:

    git clone git@github.com:parse-community/parse-server.git
    cd parse
    docker build -t ${DOCKER_USER}/parse-server .
    # Push to dockerhub
    docker push ${DOCKER_USER}/parse-server

### Deploying Parse

You need:

* `PARSE_SERVER_APPLICATION_ID` - identifier for your app
* `PARSE_SERVER_MASTER_KEY` - an identifier that authorizes the master user
* `PARSE_SERVER_DATABASE_URI` - URI for your mongodb cluster

Lets use the existing image on dockerhub:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: parse-server
      namespace: default
    spec:
      replicas: 1
      selector:
        matchLabels:
          run: parse-server
      template:
        metadata:
          labels:
            run: parse-server
        spec:
          containers:
          - name: parse-server
            image: parseplatform/parse-server
            env:
            - name: PARSE_SERVER_DATABASE_URI
              value: "mongodb://mongo-0.mongo:27017,\
                mongo-1.mongo:27017,mongo-2.mongo\
                :27017/dev?replicaSet=rs0"
            - name: PARSE_SERVER_APP_ID
              value: my-app-id
            - name: PARSE_SERVER_MASTER_KEY
              value: my-master-key

I was getting an issue:

    $ kubectl get pods
    NAME                            READY   STATUS             RESTARTS   AGE
    mongo-0                         1/1     Running            0          14m
    mongo-1                         1/1     Running            0          14m
    mongo-2                         1/1     Running            0          14m
    parse-server-555dcf844c-2f8x5   0/1     CrashLoopBackOff   3          3m3s

so I got the logs for it:

    kubectl logs parse-server-555dcf844c-2f8x5

in the logs I moticed in red:

    ERROR: appId and masterKey are required

Apparently the environment variable needed now is `PARSE_SERVER_APPLICATION_ID` and not `PARSE_SERVER_APP_ID`

Create the service to test parse:

    apiVersion: v1
    kind: Service
    metadata:
      name: parse-server
      namespace: default
    spec:
      ports:
      - port: 1337
        protocol: TCP
        targetPort: 1337
      selector:
        run: parse-server

Now all is working:

    $ kubectl get pods
    NAME                           READY   STATUS    RESTARTS   AGE
    mongo-0                        1/1     Running   0          21m
    mongo-1                        1/1     Running   0          21m
    mongo-2                        1/1     Running   0          21m
    parse-server-fff856db6-mbt95   1/1     Running   0          98s

To access the api do you need to port formard?

    $ kubectl get svc
    NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
    parse-server   ClusterIP   10.103.26.80    <none>        1337/TCP    2m46s

    kubectl port-forward parse-server-fff856db6-mbt95 1337:1337

Add some data to parse:

    $ http post localhost:1337/parse/classes/scores X-Parse-Application-Id:my-app-id score=1337 player_name:stephen
    HTTP/1.1 201 Created
    Access-Control-Allow-Headers: X-Parse-Master-Key, X-Parse-REST-API-Key, X-Parse-Javascript-Key, X-Parse-Application-Id, X-Parse-Client-Version, X-Parse-Session-Token, X-Requested-With, X-Parse-Revocable-Session, Content-Type, Pragma, Cache-Control
    Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
    Access-Control-Allow-Origin: *
    Access-Control-Expose-Headers: X-Parse-Job-Status-Id, X-Parse-Push-Status-Id
    Connection: keep-alive
    Content-Length: 64
    Content-Type: application/json; charset=utf-8
    Date: Wed, 18 Dec 2019 20:42:16 GMT
    ETag: W/"40-eOAuPeKPi5lRZ/W6/wevSA0q/tk"
    Location: http://localhost:1337/parse/classes/scores/U93JjLNaQp
    X-Powered-By: Express

    {
        "createdAt": "2019-12-18T20:42:16.122Z",
        "objectId": "U93JjLNaQp"
    }

Get all scores with:

    $ http localhost:1337/parse/classes/scores X-Parse-Application-Id:my-app-id
    HTTP/1.1 200 OK
    Access-Control-Allow-Headers: X-Parse-Master-Key, X-Parse-REST-API-Key, X-Parse-Javascript-Key, X-Parse-Application-Id, X-Parse-Client-Version, X-Parse-Session-Token, X-Requested-With, X-Parse-Revocable-Session, Content-Type, Pragma, Cache-Control
    Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
    Access-Control-Allow-Origin: *
    Access-Control-Expose-Headers: X-Parse-Job-Status-Id, X-Parse-Push-Status-Id
    Connection: keep-alive
    Content-Length: 132
    Content-Type: application/json; charset=utf-8
    Date: Wed, 18 Dec 2019 20:44:13 GMT
    ETag: W/"84-8vrU48X7zjC1oY6AE8rxZ+EiksM"
    X-Powered-By: Express

    {
        "results": [
            {
                "createdAt": "2019-12-18T20:42:16.122Z",
                "objectId": "U93JjLNaQp",
                "score": "1337",
                "updatedAt": "2019-12-18T20:42:16.122Z"
            }
        ]
    }

## Ghost

A popular blogging engine with a clean interface written in javascript - can use SQLite or MySQL.

### Configuring Ghost

Configured with `js`

**ghost-config.js**

    var path = require('path'),
        config;

    config = {
        development: {
            url: 'http://localhost:2368',
            database: {
                client: 'sqlite3',
                connection: {
                    filename: path.join(process.env.GHOST_CONTENT,
                                        '/data/ghost-dev.db')
                },
                debug: false
            },
            server: {
                host: '0.0.0.0',
                port: '2368'
            },
            paths: {
                contentPath: path.join(process.env.GHOST_CONTENT, '/')
            }
        }
    };

    module.exports = config;

Now create a k8s configmap

    kubectl create cm --from-file ghost-config.js ghost-config

Creating a config called `ghost-config`, we mount this config as a volume in our container.

**ghost.yaml**:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: ghost
    spec:
      replicas: 1
      selector:
        matchLabels:
          run: ghost
      template:
        metadata:
          labels:
            run: ghost
        spec:
          containers:
          - image: ghost
            name: ghost
            command:
            - sh
            - -c
            - cp /ghost-config/ghost-config.js /var/lib/ghost/config.js && /usr/local/bin/docker-entrypoint.sh node current/index.js
            volumeMounts:
            - mountPath: /ghost-config
              name: config
          volumes:
          - name: config
            configMap:
              defaultMode: 420
              name: ghost-config

We copy `config.js` to a place where ghost expects it. ConfigMap can only mount directories - not individual files
We can't just mount to `/var/lib/ghost` as ghost expects other files.

Expose it as a service with:

    kubectl expose deployments ghost --port=2368

Now it is a service:

    $ kubectl get svc
    NAME           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)     AGE
    ghost          ClusterIP   10.110.230.119   <none>        2368/TCP    78s

View ghost with:

    kubectl proxy
    
    Go to: http://localhost:8001/api/v1/namespaces/default/services/ghost/proxy/

#### Ghost and MySQL

A more scalable way of deploying the app is to use MySQL

Update config.js:

        database: {
            client: 'mysql',
            connection: {
                host     : 'mysql',
                user     : 'root',
                password : 'root',
                database : 'ghost_db',
                charset  : 'utf8'
            }
        },

Create the new configmap:

    kubectl create configmap ghost-config-mysql --from-file ghost-config.js

Update the deployment configMap to point to `ghost-config-mysql`

Deploy a MySQL cluster like we did with mongodb previously.
Create the database with MySQL:

    kubectl exec -it mysql-xyz -- mysql -u root -p 

    create database ghost_db;

Apply:

    kubectl apply -f ghost.yaml

Now you can scale up cause your applciation is decoupled from the data.

## Redis

Redis is a popular in memory key/value store. A reliable redis instance is made of 2 parts: `redis-server` and `redis-sentinel` - which implements health checking and failover.

In a replicated way there is a single master used for both reads and writes.
There are replicas that duplicate data and are used for load balancing.
Any replica can failover to become a master.

The failover is performed by the `redis-failover`

### Configuring Redis

We are going to use configmaps to configure redis

It needs seperate configurations for master and slave replicas.

**master.conf**

    bind 0.0.0.0
    port 6379

    dir /redis-data

**slave.conf**

    bind 0.0.0.0
    port 6379

    dir .

    slaveof redis-0.redis 6379

**sentinel.conf**

    bind 0.0.0.0
    port 26379

    sentinel monitor redis redis-0.redis 6379 2
    sentinel parallel-syncs redis 1
    sentinel down-after-milliseconds redis 10000
    sentinel failover-timeout redis 20000

We need a few wrapper scripts for our stateful set:

The first one checks if it is a master or slave - based on the hostname - and starts it up:

**init.sh**

    #!/bin/bash
    if [[ ${HOSTNAME} == 'redis-0' ]]; then
      redis-server /redis-config/master.conf
    else
      redis-server /redis-config/slave.conf
    fi

**sentinel.sh**

    #!/bin/bash
    cp /redis-config-src/*.* /redis-config

    while ! ping -c 1 redis-0.redis; do
      echo 'Waiting for server'
      sleep 1
    done

    redis-sentinel /redis-config/sentinel.conf

Now we pack all this up into a configmap:

    kubectl create configmap \
    --from-file=slave.conf=./slave.conf \
    --from-file=master.conf=./master.conf \
    --from-file=sentinel.conf=./sentinel.conf \
    --from-file=init.sh=./init.sh \
    --from-file=sentinel.sh=./sentinel.sh \
    redis-config

### Creating a Redis Service

Create a k8s service that provides naming and discovery for redis replicas `redis-0.redis`

**redis-service.yaml**

    apiVersion: v1
    kind: Service
    metadata:
      name: redis
    spec:
      ports:
      - port: 6379
        name: peer
      clusterIP: None
      selector:
        app: redis

> Kubernetes doesn't care that the pods are not created yet - it will add the right names when the pods are created

### Deploying Redis

We are going to deploy with a stateful set:

**redis.yaml**

    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: redis
    spec:
      replicas: 3
      serviceName: redis
      selector:
        matchLabels:
          app: redis
      template:
        metadata:
          labels:
            app: redis
        spec:
          containers:
          - command: [sh, -c, source /redis-config/init.sh ]
            image: redis:3.2.7-alpine
            name: redis
            ports:
            - containerPort: 6379
              name: redis
            volumeMounts:
            - mountPath: /redis-config
              name: config
            - mountPath: /redis-data
              name: data
          - command: [sh, -c, source /redis-config/sentinel.sh]
            image: redis:3.2.7-alpine
            name: sentinel
            volumeMounts:
            - mountPath: /redis-config
              name: config
          volumes:
          - configMap:
              defaultMode: 420
              name: redis-config
            name: config
          - emptyDir:
            name: data

There are 2 containers, one runs `init.sh` the other runs `sentinel.sh`

There are also 2 volumes: 1 for our ConfigMap the other is `emptyDir` to hold data that survives a restart.
For more reliable installation - this could be a network attached disk.

To get logs from a specific container within a pod use:

    kubectl logs redis-0 redis
    kubectl logs redis-0 sentinel

There was an error in sentinel:

    *** FATAL CONFIG FILE ERROR ***
    Reading the configuration file, at line 4
    >>> 'sentinel monitor redis redis-0.redis 6379 2'
    Can't resolve master instance hostname.

Eventually it sorted itself out

### Playing with redis

We can check which sentinel believes it is the master

    $ kubectl exec redis-2 -c redis -- redis-cli -p 26379
    Could not connect to Redis at 127.0.0.1:26379: Connection refused
    Could not connect to Redis at 127.0.0.1:26379: Connection refused

Get the value `foo`:

    kubectl exec redis-2 -c redis -- redis-cli -p 6379 get foo

Write to from slave:

    kubectl exec redis-2 -c redis -- redis-cli -p 6379 set foo 10

Try from a master:

    kubectl exec redis-0 -c redis -- redis-cli -p 6379 set foo 10

Now read again:

    kubectl exec redis-2 -c redis -- redis-cli -p 6379 get foo

**Something sketchy is happeneing**

    redis-0                        1/2     CrashLoopBackOff   5          11m
    redis-1                        1/2     CrashLoopBackOff   5          11m
    redis-2                        2/2     Running            4          9m16s

# 18. Organising your Application

How to layout, manage, share and update various configurations that make up your applciation.

## Principles

* Filesystems as source of truth
* Code reviews to ensure the quality of the changes
* Feature flags for staged roll forward and roll back

### Filesystems as source of truth

In a true productionised application the data in `etcd` is the source of truth.
The `yaml` or `json`.

It allows you to treat your cluster as `immutable infrastructure`

> If your cluster is a snowflake made up by the ad-hoc application of various random YAML files downloaded from the internet, it is as dangerous as a virtual machine that has been built from imperative bash scripts

Managing via filesystems also makes it more collaborative with the aid of source control

### The role of code review

Code review and config review.
A few people should look at the configuration of a critical deployment.

> In our experience, most service outages are self-inflicted via unexpected consequences, typos, or other simple mistakes

### Feature Gates and Guards

> Should you use the same repository for application source code as well as configuration? This can work for small projects, but in larger projects it often makes sense to separate the source code from the configuration to provide for a separation of concerns

So development is done behind a feature flag or gate that can be turned on or off

> There are a variety of benefits to this approach. First, it enables the committing of code to the production branch long before the feature is ready to ship

So development is much closer to the `HEAD` of a repo

Enabling or disabling a feature becaome a much simpler task.

## Managing your Application in Source Control

### Filesystem Layout

First cardinality: `frontend`, `backend` or `queue` - this sets the stage for team scaling.

For an application using 2 services:
* `/frontend`
* `/service-1`
* `/service-2`

Within each directory the config for the application is stored - yaml files represent the state of the cluster.

Include both the `service name` and `object type` within the same file.

> It is an antipattern to create multiple objects in the same file

    /frontend
        frontend-deployment.yaml
        frontend-service.yaml
        frontend-ingress.yaml
    /service-1
        service-1-deployment.yaml
        service-1-service.yaml
        service-1-ingress.yaml
    /service-2
        service-2-deployment.yaml
        service-2-service.yaml
        service-2-ingress.yaml

### Managing Periodic Versions

Use `tags, branches, and source-control features` or `clone into different directories for different versions`

#### Versioning with Branches and Tags

Tag a release `git tag v1.0`

#### Versioning with Directories

    /frontend
        /v1
            frontend-deployment.yaml
            frontend-service.yaml
            frontend-ingress.yaml
        /current
            frontend-deployment.yaml
            frontend-service.yaml
            frontend-ingress.yaml
    ...

New configurations are added to the `current` directory
Old configs are copied to their versioned directory `/v1`

## Securing your Application for Development, Testing and Deployment

In addition to release cadence you want to strucutre your app for:
* agile development
* quality testing
* safe deployment

Each developer should be able to develop new features of the application
In a microservices archiecture that feature might be dependent on many others - it is essential developers can work in their own environment.

Important to test your application as well.

### Progression of a Release

* `HEAD` - Bleeding edge - latest changes
* `Development` - Largely stable but not ready for deployment
* `Staging` - Unlikely to change unless problems found
* `Canary` - First release to users for real-world problem
* `Release` - Current Production release

#### Mapping of Revision and Stages

    frontend/
        canary/ -> v2/
        release/ -> v1/
        v1/
            frontend-deployment.yaml

You can use symbolic links to map a stage name to a release, or an additional tag in the source control management

## Parametering your Application with Templates

> Variance and drift between different environments produces snowflakes and systems that are hard to reason about

### Parameterizing with Helm and Templates

There are different languages for creating parameterised configurations - they all divide the files into a `template` file - containing the bulk of the configuration and the `parameters` file - combined with the template to create the complete config.

Most languages allow default values if none are set

Helm is a package manager for kubernetes.

> Despite what devotees of various languages may say, all parameterization languages are largely equivalent, and as with programming langauges, which one you prefer is largely a matter of personal or team style

Helm uses mustache syntax

    metadata:
      name: {{ .Release.Name }}-deployment

`Release.Name` should be interpolated into the deployment

To pass a parameter to a deployment:

`values.yaml`:

    Release:
      Name: my-release

### Filesystem Layout for Paramterisation

    frontend/
        staging/
            templates -> ../v2
            staging-parameters.yaml
        production/
            templates -> ../v1
            production-parameters.yaml
        v1/
            frontend-deployment.yaml
            frontend-service.yaml
        v2/
            frontend-deployment.yaml
            frontend-service.yaml

In a source controlled version:

    frontend/
        staging-parameters.yaml
        templates/
            frontend-deployment.YAML

## Deploying your Application around the World

> In the world of the cloud, where an entire region can fail, deploying to multiple regions (and managing that deployment) is the only way to achieve sufficient uptime for demanding users

### Architectures for World-wide Deployment

Each k8s cluster is intended to run in a single region
Each k8s cluster is expected to contain a single complete deployment of your application

A regions configuration is conceptually equivalent to the deployment lifecycle:

Production is just split into `East US`, `West US`, `UK`, `Asia`

    frontend/
        staging/
            templates -> ../v3/
            parameters.yaml
        eastus/
            templates -> ../v1/
            parameters.yaml
        westus/
            templates -> ../v2/
            parameters.yaml

or:

    frontend/
        staging-parameters.yaml
        eastus-parameters.yaml
        westus-parameters.yaml
        templates/
            frontend-deployment.yaml

### implementing Worldwide Deployment

* Ensure very high reliability and uptime
* Key is to limit the `blast radius`
* Begin rollout to low traffic regions
* Once validated on low-traffic, deploy to high traffic regions


### Dashboard and Monitoring Worldwide

* Different versions of an app in different regions
* It is essential to develop a dashboard which tell you at first glance and alerting that fires when too many of the same app is deployed
* Best practice to limit the number of active versions to 3 - one testing, one rolling out and one being replaced

# Appendix A. Building a Raspberry Pi k8s Cluster

* A rewarding experience
* See how k8s automatically reacts to removing a node

## Parts List

* 4 Raspberry Pi Boards
* 4 SDHC Memory Cards
* 4 x 12 inch Cat 6 Ethernet Cables
* 4 x 12 Inch USB A Micro USB
* 1 x 5 port 10/100 Fast Ethernet Switch
* 1 x 5 Port USB Charger
* 1 x Raspberry Pi stackable case
* 1 x USB-to-barrel plug

## Flashing the Images

Raspbian supports docker, but [Hypriot](https://blog.hypriot.com/downloads/) comes with docker pre-installed.
It also has good instructions on how to flash the card.

## First Boot: Master

Insert memory card, HDMI cable and plug in a keyboard, attach power and boot up.

> Change the default password

### Setting Up Networking

Edit `/boot/user-data` - add the SSID and password.
Reboot with `sudo reboot`

Next step is to setup a static IP for your cluster's internal network, edit `/etc/network/interfaces.d/etho0`:

    allow-hotplug eth0
    iface eth0 inet static
        address 10.0.0.1
        netmask 255.255.255.0
        broadcast 10.0.0.255
        gateway 10.0.0.1

This sets the main ethernet interface to be allocated to `10.0.0.1`

Reboot the machine.

Next we need to install DHCP on the master, so it allocates addresses to the worker nodes.

    sudo apt-get install isc-dhcp-server

Then set `/etc/dhcp/dhcpd.conf` to be:

    # Set a domain name, can basically be anything
    option domain-name "cluster.home";

    # Use Google DNS by default, you can substitute ISP-supplied values here
    option domain-name-servers 8.8.8.8, 8.8.4.4;

    # We'll use 10.0.0.X for our subnet
    subnet 10.0.0.0 netmask 255.255.255.0 {
        range 10.0.0.1 10.0.0.10;

        option subnet-mask 255.255.255.0;
        option broadcast-address 10.0.0.255;
        option routers 10.0.0.1;
    }
    default-lease-time 600;
    max-lease-time 7200;
    authoritative;

You might also need to edit `/etc/defaults/isc-dhcp-server` to set `INTERFACES` to `eth0`

More info in the book

#### Enhancing Pod Functionality by Bundling Supporting Containers

What types of containers should be bundled in a single pod?

* The primary container fulfils the core function of the pod

3 design patterns for packaging containers into a pod

* sidecar - secondary container enhances and extend's primary containers core functionality
* ambassador - supplemental container to abstract remote resources from the main container - primary container does not need to know the actual deployment environment
* adaptor - translate the primary containers data, protocols and interfaces to align with those expected by outside parties.

## Source

* Brendan Burns, Joe Beda & Kelsey Hightower “Kubernetes: Up and Running.”
* [Patterns of architecting kubernetes](https://www.digitalocean.com/community/tutorials/architecting-applications-for-kubernetes)
