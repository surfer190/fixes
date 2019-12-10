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

6. Labels and Annotations

