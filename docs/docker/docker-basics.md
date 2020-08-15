---
author: ''
category: Docker
date: '2020-06-14'
summary: ''
title: Docker Basics
---
# Docker Basics

## What is docker?

It is an open platform to build, ship and run distributed applications. It was introduced in 2013 by Soloman Hykes. However Linux containers have been around since 2008.

How does Docker help:

* Packaging software in a way the leverages skills developers have
* A way to bundle dependencies
* Using some artifact to test and deliver - accelerates development cycles
* Less resource intensive than VM's - reduces infrastructure costs
* Helps onboard new developers more quickly
* Lowers the wall between development and operations teams

> Understanding docker is essential to build and operate cloud-native applications - scalable, highly available, and run on managed cloud infrastructures

Eventually container orchestration technologies like kubernetes will be required

Ultimately it reduces complexity of communication between development and infrastructure teams.
Letting companies ship better software faster.
As teams get bigger the burden of communication becomes harder.
No need for developers to request a package version installed on a production server.
Provides a layer of isolation.
Nature of throw-away containers prevent relying on old artifacts.
Also allows for better reliability and scalability.

Many Parts:

* Docker engine: powers docker locally - a portable, lightweight runtime and packaging tool
* Docker hub: cloud service to share images 
* docker compose: mechanism to define and run multi-container applications
* docker swarm: container orchestration for production
* docker registry: server side application that stores and lets you distribute Docker images
* docker machine: tool that lets you install Docker Engine on virtual hosts and manage hosts

> However when people are talking docker they are usually talking `docker engine`

### What Docker is Not

* Enterprise Virtualization (VMWare, KVM): Complete OS on hypervisor - docker is process based and lightweight
* Cloud platform (Openstack, cloudstack): docker does not allow for creating of new host systems, object stores, block storage
* Configuration management (Chef, Ansible and Puppet) - docker can lesson the load but does not maange state
* Deployment framework (capistrano, fabric)
* Workload management (Mesos, Kubernetes, Swarm)
* VM manager / Development environemnt (vagrant) - a virtual machine manager

> Atomic host - Small finely tuned image like CoreOS

## Serverless vs Docker vs VM's

They are not competing - they should be used together for maximum benefit.

The `Dockerfile` and `docker-compose.yml` can take the role of an operating manual.
In years past, getting a development environment running was often a multiday task.

Nowadays it is:

1. Install docker
2. Clone the repo
3. `docker-compose up`

Always learn the fundamentals first - mastering the basics will give you greater success later on.
The most important piece of your project, the `Dockerfile`

> You’ll learn that any application code can be packaged in a container image, regardless of age, framework, language, or architectural pattern.

## The Docker Landscape

### Process Simplification

> Our experience has shown that when you are following traditional processes, deploying a brand new application into production can take the better part of a week for a complex new system.

DevOps can help but also requires arguably more time, effort and communication.

This time wasted can limit the kinds of innovation that development teams will undertake in the future.

> If deploying software is hard, time-consuming, and dependent on resources from another team, then developers may just build everything into the existing application in order to avoid suffering the new deployment penalty.

An updated deploy may be:

1. Development team build image and ship to registry
2. Operations engineers provide config details and provision resources
3. Developers trigger deployment

Clearer division of responsibilities

### Broad Support

Docker is well supported by large public cloud providers.
* AWS: Elastic Container Service (ECS), EKS (ECS for Kubernetes), Fargate and Elastic Beanstalk.
* Google AppEngine and Google Kubernetes Engine
* Red Hat OpenShift
* IBM Cloud
* Microsoft Azure Container Service
* Rackspace Cloud
* Docker Cloud

> At DockerCon 2014, Google’s Eric Brewer announced that Google would be supporting Docker as its primary internal container format

A lot of money is backing the success and stability of the platform.

Docker has traditionally been developed on the Ubuntu Linux distribution. Also RedHat has gone all-in on containers and all of their platforms have first-class support for Docker.

Red Hat’s CoreOS, which is built entirely on top of Docker containers, either running on Docker itself or under their own `rkt` runtime

> In the first years after Docker’s release, a set of competitors and service providers voiced concerns about Docker’s proprietary image format. Containers on Linux did not have a standard image format, so Docker, Inc., created their own according to the needs of their business.

The OCI (Open Container Initiative) is a spec for images/runtimes, these claim to implement:

* `runc`- part of docker
* `railcar` - oracle
* `kata containers` - intel and openstack
* `gVisor` - google - implemented in userspace

### Architecture

Its fundamental user-facing structure is indeed a simple client/server model via API

> The docker command-line tool and `dockerd` daemon talk to each other over network sockets

Ports:

* `TCP 2375` for unencrypted
* `TCP 2376` for encrypted

`docker swarm` was an oler, now deprecated project that was a standalone application. There is now a newer built-in version called `swarm mode`.

Docker also has it's own toolset: Compose, Machine and Swarm. However Docker's offering in the production orchestration space have been overshadowed by Google's Kubernetes and Apache Mesos.

#### Container Networking

* Most people run their containers in the default configuration, called *bridge* mode.
* A bridge is just a network device that repeats traffic from one side to another
* The Docker server acts as a virtual bridge and the containers are clients behind it
* Docker lets you bind and expose individual or groups of ports on the host to the container so that the outside world can reach your container on those ports

#### Getting the Most out of Docker

> Docker’s architecture aims it squarely at applications that are either stateless or where the state is externalized into data stores like databases or caches. Those are the easiest to containerize.

Putting a database engine inside Docker is a bit like swimming against the current - this is not the most obvious use case for Docker.

> Some good applications for beginning with Docker include web frontends, backend APIs, and short-running tasks like maintenance scripts that might normally be handled by cron.

#### Containers are not Virtual Machines

* Think of docker containers not as virtual machines but as very lightweight wrappers around a single Unix process (they are process based)
* Containers are also **ephemeral**: they may come and go much more readily than a traditional virtual machine
* if you run Docker on a Mac or Windows system you are leveraging a Linux virtual machine to run `dockerd`, the Docker server. However, on Linux `dockerd` can be run natively and therefore there is no need for a virtual machine to be run anywhere on the system
* There is limited isolation. The default container configuration just has them all sharing CPU and memory on the host system - this means that unless you constrain them, containers can compete for resources on your production machines
* Containers are lightweight - just reference to a layered filesystem

> You probably wouldn’t, for instance, spin up an entire virtual machine to run a `curl` command to a website from a remote location, but you might spin up a new container for this purpose

Warning: Many types of security vulnerabilities or simple misconfiguration can give the container’s root user unauthorized access to the host’s system resources, files, and processes.

#### Immutable Infrastructure

An immutable infrastructure, where components are replaced entirely rather than being changed in place.
The difficulty of creating an idempotent configuration management codebase has given rise to popularity of immutable infrastructure.

CoreOS can entirely update itself and switch to the updated OS - without requiring decommissioning.

Many container-based production systems are now using tools such as _HashiCorp’s Packer_ to build cloud virtual server images and then leveraging Docker to nearly or entirely avoid configuration management systems

#### Stateless Applications

> A good example of the kind of application that containerizes well is a web application that keeps its state in a database

* Stateless applications are normally designed to immediately answer a single self-contained request, and have no need to track information between requests from one or more clients

Local state relies on configuration files - this limits reusability and makes it harder to deploy.
In many cases, you move configuration state into environment variables that can be passed to your application from the container.

> Rather than baking the configuration into the container, you apply the configuration to the container at deployment time

This allows you to easily do things like use the same container to run in either production or staging environments

#### Externalising State

* Configuration is best passed by environment variables
* Applications that need to store files, however, face some challenges. Storing things to the container’s filesystem will not perform well, will be extremely limited by space, and will not preserve state across a container lifecycle
* It’s best to design a solution where the state can be stored in a centralized location that could be accessed regardless of which host a container runs on - Amazon S3, EBS volumes, HDFS, Openstack swift, a local block store or even mounting EBS volumes.

In short avoid containerising applications that make extensive use of the filesystem.

### The Docker Workflow

#### Revision Control

* Filesystem layers - Docker will use as many base layers as it can so that only the layers affected by the code change are rebuilt
* Image tags - image tagging at deployment time - which can be standardised across applications

Also makes communication between teams and tooling simpler.

> Note on `latest`: It is a bad idea to use `latest` in production workflows. As dependedncies can be updated without your knowledge. Rolling back is also an issue as what tag will you use.

#### Building

Building an application is a dark art in most corporates - only a few know how to do it for different applications.
Docker doesn’t solve all the problems, but it does provide a standardized tool configuration and toolset for builds

To consume a `Dockerfile` and produce a Docker image:

    docker build

Each command in a Dockerfile generates a new layer in the image.

Modern multistage Docker builds also allow you to define the build environment separately from the final artifact image - that is why environment variables must not be baked into the dockerfile?

#### Testing

* By design, containers include all of their dependencies, tests run on containers are very reliable
* Docker containers can be a real lifeline to developers or QA engineers who need to wade into the swamp of inter-microservice API calls.
* Integration tests are easier

#### Packaging and Deployment

* Docker tools only use one thing - the container - the docker image.
* Docker has one line to build and run on a host
* Standard docker client handles deploying to a single host at a time.

#### Orchestration

* Mass deployment tools: [New Relic Centurion](https://github.com/newrelic/centurion), [Spotify's Helios](https://github.com/spotify/helios) or [Ansible Docker tooling](https://docs.ansible.com/ansible/latest/scenario_guides/guide_docker.html)
* Fully automated schedulers:
    * [Apache Mesos](http://mesos.apache.org/)
    * [Googles' Kubernetes](https://kubernetes.io/)
    * Others: Hashicorp's nomad, CoreOS's Techtonic, Mesosphere DC/OS and Rancher

#### Atomic Hosts

* Traditionally, servers and virtual machines are systems that an organization will carefully assemble, configure, and maintain to provide a wide variety of functionality that supports a broad range of usage patterns
* Updates must often be applied via nonatomic operations

#### Additional Tools

* Rancher’s Convoy plug-in for managing persistent volumes on Amazon EBS volumes or over NFS mounts
* Weaveworks’ Weave Net network overlay
* Microsoft’s Azure File Service plug-in

## Installing Docker

A lot of seemingly complex setup info in the book, I just installed MacOS docker desktop

### Testing Docker

Open a shell sessions on alpine linux:

    docker run --rm -ti alpine:latest /bin/sh

`alpine` is the image name and `latest` is the image tag

#### Docker Server

Running the docker daemon manually is as simple as:

    sudo dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375

> won't work on window or mac

If you ever have a need to access the underlying VM:

    docker run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh

    / # cat /etc/os-release
    PRETTY_NAME="Docker Desktop"
    / # ps | grep dockerd
    1382 root      8:14 /usr/local/bin/dockerd -H unix:///var/run/docker.sock --config-file /run/config/docker/daemon.json --swarm-default-advertise-addr=eth0 --userland-proxy-path /usr/bin/vpnkit-expose-port
    15267 root      0:00 grep dockerd

## Working with docker images

* Every Docker container is based on an image
* Images are the underlying definition of what gets reconstituted into a running container, much like a virtual disk becomes a virtual machine when you start it up
* Every Docker image consists of one or more filesystem layers that generally have a direct one-to-one mapping to each individual build step used to create that image

Images make up everything you do with docker:

* building images
* uploading (pushing) images to an image registry
* Downloading (pulling) images to an image registry
* Creating and running containers from an image

### Anatomy of a Dockerfile

* This file describes all the steps that are required to create an image.
* would usually be contained within the root directory of the source code repository for your application

Example for a nodeJS application:

    # The Base Image locked to specific release
    FROM node:0.10

    # Key-value pairs to search and identify images/containers
    LABEL "maintainer"="anna@example.com"
    LABEL "rating"="Five Stars" "class"="First Class"

    # Set the user to run processes on the container
    USER root

    # Set Shell environment variables
    ENV AP /data/app
    ENV SCPATH /etc/supervisor/conf.d

    RUN apt-get -y update

    # Run CLI instructions
    # The daemons
    RUN apt-get -y install supervisor
    RUN mkdir -p /var/log/supervisor

    # Copy files from either the local filesystem or a remote URL into your image
    # Supervisor Configuration
    ADD ./supervisord/conf.d/* $SCPATH/

    # Application Code
    ADD *.js* $AP/

    # Change the working directory for the remaining build instructions
    WORKDIR $AP

    RUN npm install

    # Defines the process you want to run within the container
    CMD ["supervisord", "-n"]

* Each line in a Dockerfile creates a new image layer that is stored by Docker
* This means that when you build new images, Docker will only need to build layers that deviate from previous builds - you can reuse all the layers that haven't changed
* You could build a Node instance from a plain, base Linux image
* The Node.js community maintains a series of Docker images
* You could lock the image to a specific point release of node: `node:0.10.33`


* You can check image meta data with: `docker inspect <image-tag>`
* `MAINTAINER` is a deprecated field in the Dockerfile specification
* By default, Docker runs all processes as `root` within the container
* It is not recommended that you run commands like `apt-get -y update` or `yum -y update` in your application’s `Dockerfile` - requires crawling the repository index each time you run a build - not repeatable
* `ADD` actually copies the files to the image - so once the image is built you don't need access to them.
* Remember that every instruction creates a new Docker image layer, so it often makes sense to combine a few logically grouped commands onto a single line
* The order of commands in a Dockerfile can have a very significant impact on ongoing build times. You should try to order commands so that things that change between every single build are closer to the bottom
* When you rebuild an image, every single layer after the first introduced change will need to be rebuilt.
* It is generally considered a best practice to try to run only a single process within a container
* A container should provide a single function so that it remains easy to horizontally scale individual functions

> Due to potential security risks, production containers should almost always be run under the context of a nonprivileged user

### Building an Image

When cloning a repo you will get something like this:

    $ tree -a -I .git
    .
    ├── .dockerignore
    ├── .gitignore
    ├── Dockerfile
    ├── Makefile
    ├── README.md
    ├── Vagrantfile
    ├── index.js
    ├── package.json
    └── supervisord
        └── conf.d
            ├── node.conf
            └── supervisord.conf

    2 directories, 10 files

* `.dockerignore` file defines what you don't want to upload to the docker host when building the image.
* `package.json` defines the nodejs app and lists dependencies.
* `index.js` is the main source code of the application
* The `supervisord` directory contains the configuration files for `supervisord` to start and monitor.

To build the image:

    docker build -t example/docker-node-hello:latest .

This builds the image:

    Successfully built d9dff15d5b87
    Successfully tagged example/docker-node-hello:latest

To improve the speed of builds, Docker will use a local cache when it thinks it is safe. This can sometimes lead to unexpected issues because it doesn’t always notice that something changed in a lower layer. In the preceding output you will notice lines like `---> Running in 0c2dc15cab8d`. If instead you see `---> Using cache`, you know that Docker decided to use the cache.

You can disable the cache for a build by using the `--no-cache` argument to the docker build command.

#### Troubleshooting Broken Builds

We hope that things just work, but in reality that is rarely the case.

If we change `apt-get -y update` to `apt-get -y update-all`, you get:

    Step 7/14 : RUN apt-get -y update-all
    ---> Running in 06cd2cf607a0
    E: Invalid operation update-all
    The command '/bin/sh -c apt-get -y update-all' returned a non-zero code: 100

`Running in 06cd2cf607a0` gives us the container id. Sometimes you will just get an image id: `---> 8a773166616c`.
In that case, you can run an interactive container to determine why the build is not working:

    docker run --rm -ti 8a773166616c /bin/bash

Fix the error.

#### Running your Image

Once you have built your image, you can run it on your docker host with:

    docker run -d -p 8080:8080 example/docker-node-hello:latest

Which means create a running container in the background from the image with `example/docker-node-hello:latest` tag and port `8080` in the container mapped to port `8080` on the host.

You can verify it is running with:

    docker ps
    docker container list

If you are running docker locally you can go to: `http://127.0.0.1:8080`

Otherwise check the docker host ip with `echo $DOCKER_HOST` or `docker-machine ip`.

To send environment variables to the container:

Stop it first

    docker ps
    docker stop 85fc21edaad9 

You can then update the `$WHO` environment variable with:

    docker run -d -p 8080:8080 -e WHO="Stephen" \
    example/docker-node-hello:latest

This will update the application.

#### Custom Base Images

These are the lowest level images that other docker images are based on.
Most are minimal installs of linux distributions: `ubuntu`, `fedora`, `centOS` and `Alpine Linux`.

> However, there are times when it is more preferable to build your own base images rather than using an image created by someone else

Sometimes you want to get the image size down. `Alpine Linux` is designed to be small and is popular for docker.
Alpine is based around `musl libc` not `gnu libc`.

> It has the largest impact on Java-based applications and DNS resolution

It is widely used in production but ships with `/bin/sh` and not `/bin/bash`.

## Storing Images

* You don’t normally build the images on a production server and then run them
* Ordinarily, deployment is the process of pulling an image from a repository and running it on one or more Docker servers.

#### Public Registries

* [Docker hub](https://hub.docker.com/)
* [quay.io](quay.io)

This is probably the right first step if you’re getting serious about Docker but are not yet shipping enough code to need an internally hosted solution.
One of the downsides is that every layer of every deployment might need to be dragged across the internet in order to deploy an application.

#### Private Registries

* [Docker Distribution](https://github.com/docker/distribution)

You can auth with `docker login` - this logs into docker hub.
It writes a dotfile to `cat ~/.docker/config.json`.

You can logout to remove cached credentials:

    docker logout

You might be able to log into a different registry:

    docker login someregistry.example.com

You can change the repo of your image with:

    docker tag example/docker-node-hello:latest \
    ${<myuser>}/docker-node-hello:latest

Check if the image exists on the server:

    docker image ls ${<myuser>}/docker-node-hello

Upload to the repo (push):

    docker push ${<myuser>}/docker-node-hello:latest

> If this image was uploaded to a public repository, anyone in the world can now easily download it by running the docker pull command.

Pull the image:

    docker pull ${<myuser>}/docker-node-hello:latest

#### Running a pirvate registry

More info in the book about creating and running a private registry

### Advanced Building Techniques

> Keeping your image sizes small and your build times fast can be very beneficial in decreasing the time required to build and deploy new versions of your software into production

A 1Gb Image that needs to be installed on 100 nodes becomes a problem - a scaling problem. When you deploy new releases multiple times a day it becomes a bigger problem.

Most times a minimal linux distribution is not even required.

For example, `go` is a compiled programming language producing static binary files.

    docker run -d -p 8080:8080 adejonge/helloworld

Then get the info of the last container you created:

    docker container ls -l

You can export the files in the container returned to a tarball

    docker export a6f328e6eda1 -o web-app.tar

You can examine the contents of the tarball with:

    $ tar -tvf web-app.tar
    -rwxr-xr-x  0 root   0           0 Sep 25 15:16 .dockerenv
    drwxr-xr-x  0 root   0           0 Sep 25 15:16 dev/
    -rwxr-xr-x  0 root   0           0 Sep 25 15:16 dev/console
    drwxr-xr-x  0 root   0           0 Sep 25 15:16 dev/pts/
    drwxr-xr-x  0 root   0           0 Sep 25 15:16 dev/shm/
    drwxr-xr-x  0 root   0           0 Sep 25 15:16 etc/
    -rwxr-xr-x  0 root   0           0 Sep 25 15:16 etc/hostname
    -rwxr-xr-x  0 root   0           0 Sep 25 15:16 etc/hosts
    lrwxrwxrwx  0 root   0           0 Sep 25 15:16 etc/mtab -> /proc/mounts
    -rwxr-xr-x  0 root   0           0 Sep 25 15:16 etc/resolv.conf
    -rwxr-xr-x  0 root   0     3604416 Jul  2  2014 helloworld
    drwxr-xr-x  0 root   0           0 Sep 25 15:16 proc/
    drwxr-xr-x  0 root   0           0 Sep 25 15:16 sys/

Almost all the files are `0` bytes in length. These files are required to exist in every linux container and are automatically bind-mounted from the host into the container when it is first created.

The only thing with size is the `helloworld` binary.

> Containers are only required to contain exactly what they need to run on the underlying kernel

Sometimes a shell is good for troubleshooting so people compromise with a lightweight linux distribution.

We can poke around in alpine linux with:

    docker run -ti alpine:latest /bin/sh

We cannot do this with the go image above, because it does not contain a shell or `ssh`.
We can't use `ssh`, `nsenter` or `docker exec` to examine it.

How do we examine a containers filesystem? We need to inspect the image to find where the files are stored:

    docker image inspect alpine:latest

    "Id": "sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1",
    "RepoTags": [
        "alpine:latest"
    ],
    "RepoDigests": [
        "alpine@sha256:769fddc7cc2f0a1c35abb2f91432e8beecf83916c421420e6a6da9f8975464b6"
    ],
    "GraphDriver": {
        "Data": {
            "MergedDir": "/var/lib/docker/overlay2/33cd56da7058828f2bbc3f162beaf8e611d6a44b96ff15dd76d0b9f6927e11be/merged",
            "UpperDir": "/var/lib/docker/overlay2/33cd56da7058828f2bbc3f162beaf8e611d6a44b96ff15dd76d0b9f6927e11be/diff",
            "WorkDir": "/var/lib/docker/overlay2/33cd56da7058828f2bbc3f162beaf8e611d6a44b96ff15dd76d0b9f6927e11be/work"
        },
        "Name": "overlay2"
    },

and on the go application container:

    docker image inspect adejonge/helloworld:latest

    "Id": "sha256:4fa84a96f0d641a79ad7574fd75eabee71e93095fb35af9c30e9b59e3269206d",
    "RepoTags": [
        "adejonge/helloworld:latest"
    ],
    "RepoDigests": [
        "adejonge/helloworld@sha256:46d95092b73dccbcc12cdec910a3673e41cd7c4fabc7bf7413dfb12f709e2a1d"
    ],
    "GraphDriver": {
    "Data": {
        "LowerDir": "/var/lib/docker/overlay2/86f86888c7eb97264dfab3308d46be90c05b2cc39f8290491aabf080579d9ef1/diff:/var/lib/docker/overlay2/157089801bf8d5c0ba8944a9b50b52d7239ec68d3ac231b2ef5e8f8785925401/diff",
        "MergedDir": "/var/lib/docker/overlay2/26103927669ab87c80f1d03e5de4823ec239b4428b3e3c08afafc9180aaa4cef/merged",
        "UpperDir": "/var/lib/docker/overlay2/26103927669ab87c80f1d03e5de4823ec239b4428b3e3c08afafc9180aaa4cef/diff",
        "WorkDir": "/var/lib/docker/overlay2/26103927669ab87c80f1d03e5de4823ec239b4428b3e3c08afafc9180aaa4cef/work"
    },
    "Name": "overlay2"

On linux we need to use this command to explore the host machine:

    docker run -it --privileged --pid=host debian nsenter -t 1  -m -u -n -i sh

If you go to the `diff` folder of the `MergedDir` you can see the files.

The size of alpine is:

    du -sh /var/lib/docker/overlay2/33cd56da7058828f2bbc3f162beaf8e611d6a44b96ff15dd76d0b9f6927e11be/diff/
    5.8 M

In the go case check the lowerDir:

    ls -lh /var/lib/docker/overlay2/86f86888c7eb97264df
    ab3308d46be90c05b2cc39f8290491aabf080579d9ef1/diff
    total 3520
    -rwxr-xr-x    1 root     root        3.4M Jul  2  2014 helloworld

You can even run this file directly from the docker server - driving how useful statically compiled applications can be

#### Multistage Builds

    # Build container
    FROM golang:alpine as builder
    RUN apk update && \
        apk add git && \
        CGO_ENABLED=0 go get -a -ldflags '-s' github.com/adriaandejonge/helloworld

    # Production container
    FROM scratch
    COPY --from=builder /go/bin/helloworld /helloworld
    EXPOSE 8080
    CMD ["/helloworld"]

Base your build on the golang image and will be referring to this build image/stage

More relevant stuff in the book

#### Layers are Additive

The filesystem layers that make up images are additive in nature.
In other words you cannot make your image smaller by deleting files that were generated in earlier steps.

Example:

    FROM fedora
    RUN dnf install -y httpd
    CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

Just docker build:

    docker build .

    ...
    Successfully built 2f96aac9e094

Lets tag that build, to refer to it easier:

    docker tag 2f96aac9e094 size1

Now lets look at the image layers with:

    docker history size1

    IMAGE               CREATED              CREATED BY                                      SIZE                COMMENT
    2f96aac9e094        About a minute ago   /bin/sh -c #(nop)  CMD ["/usr/sbin/httpd" "-…   0B                  
    2c0ecaeaa083        About a minute ago   /bin/sh -c dnf install -y httpd                 223MB               
    e9ed59d2baf7        4 weeks ago          /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
    <missing>           4 weeks ago          /bin/sh -c #(nop) ADD file:22abad47ea7363005…   246MB               
    <missing>           8 months ago         /bin/sh -c #(nop)  ENV DISTTAG=f30container …   0B                  
    <missing>           8 months ago         /bin/sh -c #(nop)  LABEL maintainer=Clement …   0B

Notice 4 layers added no size to our final image, but 2 of them added a great deal of size. The Fedora image that includes a minimal Linux distribution at 246MB. However the 182MB is surprising - apache shouldn't be that big.

Package managers like `apk`, `apt`, `dnf` or `yum` rely on cache which takes a large amount of space and is useless once the package has been installed. The obvious next step is to delete the cache.

    FROM fedora
    RUN dnf install -y httpd
    RUN dnf clean all
    CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

Then build, tag and view the history again:

    IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
    3203a6f67417        14 seconds ago      /bin/sh -c #(nop)  CMD ["/usr/sbin/httpd" "-…   0B                  
    a71a22f17812        14 seconds ago      /bin/sh -c dnf clean all                        1.73MB              
    2c0ecaeaa083        9 minutes ago       /bin/sh -c dnf install -y httpd                 223MB               
    e9ed59d2baf7        4 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
    <missing>           4 weeks ago         /bin/sh -c #(nop) ADD file:22abad47ea7363005…   246MB               
    <missing>           8 months ago        /bin/sh -c #(nop)  ENV DISTTAG=f30container …   0B                  
    <missing>           8 months ago        /bin/sh -c #(nop)  LABEL maintainer=Clement …   0B  

Now the image is 1.73MB **greater** than it was.

Showing the additive nature. The only way to make a layer smaller is to remove file before saving the layer.

> The most common way to deal with this is by stringing commands together on a single Dockerfile line. You can do this very easily by taking advantage of the && operator

So rewrite the file like:

    FROM fedora
    RUN dnf install -y httpd && \
        dnf clean all
    CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

That drops the file size significantly:

    IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
    21eff7fc3868        3 minutes ago       /bin/sh -c #(nop)  CMD ["/usr/sbin/httpd" "-…   0B                  
    8eaa03cfcd9d        3 minutes ago       /bin/sh -c dnf install -y httpd && dnf clean…   19.8MB              
    e9ed59d2baf7        4 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
    <missing>           4 weeks ago         /bin/sh -c #(nop) ADD file:22abad47ea7363005…   246MB               
    <missing>           8 months ago        /bin/sh -c #(nop)  ENV DISTTAG=f30container …   0B                  
    <missing>           8 months ago        /bin/sh -c #(nop)  LABEL maintainer=Clement …   0B                  

Boom - massive saving in space.

#### Optimising for Cache

We want to keep builds as fast as possible. Keeping feedback loops tight.

> Docker uses a layer cache to try to avoid rebuilding any image layers that it has already built

Therefore, the order in which you do things inside your Dockerfile can have a dramatic impact on how long your builds take on average.

let's customise the previous dockerfile:

    FROM fedora
    RUN dnf install -y httpd && \
        dnf clean all
    RUN mkdir /var/www && \
        mkdir /var/www/html
    ADD index.html /var/www/html
    CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

Now we add the `index.html`:

    <html>
        <head>
            <title>My custom Web Site</title>
        </head>
        <body>
            <p>Welcome to my custom Web Site</p>
        </body>
    </html>

Time the build process:

    time docker build --no-cache .
    
    ...
    real	2m3.571s
    user	0m0.085s
    sys	0m0.185s

Building straight after:

    time docker build 

    real	0m0.635s
    user	0m0.075s
    sys	0m0.171s

Update the `index.html` file:

    # Most items will use cache

    real	0m1.255s
    user	0m0.075s
    sys	0m0.172s

> Long story short: order matters. The files that change frequently should be lower down in the `Dockerfile` as cache will be invalidated for less tasks. Stable time consuming tasks should be higher up.

## Working with Containers

### What are Containers?

Virtualization - KVM or VmWare let you run a complete linux kernel on a virtualised layer called a `hypervisor`.
Provides strong isolation between workloads - each virtual machine has its own kernel in a seperate memory space.

Container share a single kernel.
Isolation between workloads happens in one kernel.
Operating system virtualization.
Provides resource efficiency - one less layer between the task and hardware underneath. A vm call has to go through vm's kernel then through the hypervisor kernel.

Downside is you can only run containers that are compatible with the underlying kernel. Containers are therefore an OS-specific technology. You can't run a windows or BSD container on a linux kernel. You need to use KVM or VMWare in that instance.

### History of Containers

* Containers are not a new idea.
* Seeds for today’s containers were planted in 1979 with the addition of the `chroot` system call to Version 7 Unix.
* `chroot` restricts a process’s view of the underlying filesystem to a single subtree
* It was used to protect the OS from untrusted processes like `FTP, BIND and Sendmail`
* `Sidewinder firewall built on top of BSDI Unix` created tightly controlled domains on a single kernel - not compatible with many unix installations.
* In 2000, FreeBSD released the `jail` command - which allowed shared environments in hosting providers. Between customers and internal users.
* `jail` added restrictions and expanded on `chroot`.
* In 2004, Sun released Solaris 10 which included Solaris containers. - evolving into Solaris zones. The first major commerical container implementations.
* 2005 - OpenVZ for linux
* 2007 - HP secure resource partitions - HP-UX containers
* 2008 - Linux containers (LXC)

Only in 2013 did the LXC growth start proper with the inclusion of user namespaces in `3.8`.

### Creating a Container

So far we've used `docker run`. This does 2 things:
1. `docker create` - create a container from the underlying image
2. `docker start` - execute the container

You can use `-p` to map network ports or `-e` to pass environment variables to the container.

#### Basic Configuration

> Settings in the Dockerfile are always used as defaults, but can be overriden at container creation time

**Container name**: by default docker randomly names your container, if you want to give a name use:

    docker create --name="awesome-service" ubuntu:latest sleep 120

You can start the container with:

    docker start awesome-service

It will automatically exit after 120 seconds, but you could stop it manually with:

    docker stop awesome-service

**Labels**: Key-value pairs that can be applied to images and containers. New containers automatically inherit the labels from the parent image.

You can also add labels to a container with `-l`:

    docker run -d --name has-some-labels -l deployer=Ahmed -l tester=Asako  ubuntu:latest sleep 1000

You can then search for containers on this metadata:

    docker ps -a -f label=deployer=Ahmed

You can use `docker inspect <container-id>` to see all the labels a container has.

**hostname**: docker copies certain files on the host `/etc/hostname` and others, into the container's configuration directory on the host. It then uses a bind mount to link that file into the container.

We can launch a default container like this:

    docker run --rm -ti ubuntu:latest /bin/bash

The argument `--rm` tells docker to delete the container when it exits.
The `-t` argument tells docker to allocate a pseudo-TTY, `-i` tells docker that it is going to be an interactive session and we want to keep `STDIN` open.

On the docker container run: `mount`, you will see:

    /dev/sda1 on /etc/resolv.conf type ext4 (rw,relatime,data=ordered)
    /dev/sda1 on /etc/hostname type ext4 (rw,relatime,data=ordered)
    /dev/sda1 on /etc/hosts type ext4 (rw,relatime,data=ordered)

You can check the hostname with `hostname -f`, it will not be fully qualified.

To set the hostname specifically, we can use the `--hostname` argument to pass in a more specific value.

    docker run --rm -ti --hostname="mycontainer.example.com" ubuntu:latest /bin/bash

**domain name service (dns)**: 

`resolv.conf` is also managed via bind mount between the host and container.

By default it is an exact copy of the docker host's `resolv.conf`. You can override this with `--dns` and `--dns-search` arguments.

    docker run --rm -ti --dns=8.8.8.8 --dns=8.8.4.4 --dns-search=example1.com \
    --dns-search=example2.com ubuntu:latest /bin/bash

    root@117e9a8ed06a:/# more /etc/resolv.conf
    search example1.com example2.com
    nameserver 8.8.8.8
    nameserver 8.8.4.4

**mac address**: more in the book on this

**storage volumes**: Sometimes you need storage that will persist between container deployments.

> Mounting storage from the Docker host is not generally advisable because it ties your container to a particular Docker host for its persistent state. But for cases like temporary cache files or other semi-ephemeral states, it can make sense.

You can use `-v` to mount directories and individual files from the host server into the container.
This mounts `/mnt/session_data` to `/data` within the container:

    docker run --rm -ti -v /mnt/session_data:/data ubuntu:latest /bin/bash

By default it is read/write, you can change to read only with:

    docker run --rm -ti -v /mnt/session_data:/data:ro ubuntu:latest /bin/bash

None of the mount points need to pre-exist.

If the container application is designed to write into `/data`, then this data will be visible on the host filesystem in `/mnt/session_data` and will remain available when this container stops and a new container starts with the same volume mounted.

> It is possible to tell Docker that the root volume of your container should be mounted read-only so that processes within the container cannot write anything to the root filesystem. This prevents things like logfiles, which a developer may be unaware of, from filling up the container’s allocated disk in production.

We can accomplish this by using `--read-only=true`

    docker run --rm -ti --read-only=true -v /mnt/session_data:/data ubuntu:latest /bin/bash

In this case the root filesystem will be read only, the `/data` dir will be read/write.

To make `/tmp` writable use the `--tmpfs` argument with `docker run`

> Containers should be designed to be stateless whenever possible. Managing storage creates undesirable dependencies and can easily make deployment scenarios much more complicated.

#### SELinux and volume mounts

* You might get a `Permission Denied` error when trying to mount a volume to your container.
* You can use a `z` option to the docker command - more in the book

#### Resource Quotas

Other applications on the same physical system can have a noticable impact on performance and resource availability.

Virtual Machines have the advantage that you can easily and tightly control the CPU, memory allocated. In docker you must leverage `cgroup` to control resources.
`docker create` and `docker run` allow you to configure CPU, swap, memory and storage I/O restrictions.

You can also use `docker container update` to adjust at runtime.

If your kernel does not support these things, when you do `docker info`...you will get warnings.

#### CPU Shares

The computing power of all CPU cores in a system is considered the full pool of shares.
Docker assigns `1024` to represent the full pool.

If you want the container to use at most half of the computing power, you would allocate `512`.
This value is used for scheduling time for CPU usage, not actual limiting.

Use the `stress` program container:

    docker run --rm -ti progrium/stress --cpu 2 --io 1 --vm 2 --vm-bytes 128M --timeout 120s

then you can see how the system is being affected:

    top -bn1 | head -n 15

then half the number of shares assigned with:

    docker run --rm -ti --cpu-shares 512 progrium/stress --cpu 2 --io 1 --vm 2 --vm-bytes 128M --timeout 120s

> Docker's `cgroup` limits are not hard limits, they are relative. Similar to the `nice` command.

#### CPU Pinning

You can assign a container to a specific core or cores.
You pin it with `--cpuset=0`...remember this command is 0 indexed.

Using the `CPU CFS (Completely Fair Scheduler)`, you can alter the CPU quota for a given container setting the `--cpu-quota` flag.

#### Simplifying CPU quotas

You can now simplify tell docker the amount of compute you want available to your container.
Use the `--cpus` command, a number between `0.01` and the number of cores on your machine.

    docker run -d --cpus="40.25" progrium/stress --cpu 2 --io 1 --vm 2 --vm-bytes 128M --timeout 60s

If it is too high you get an error:

    docker: Error response from daemon: Range of CPUs is from 0.01 to 2.00, as there are only 2 CPUs available.

You could update the resource limits of more than one container with:

    docker update --cpus="1.5" <container_id> <container_id>

### Memory

Important: The memory limit is a hard limit.
You can also allocate more memory than the host has - in that case the container will use swap.

You use the `--memory` option:

    docker run --rm -ti --memory 512m progrium/stress --cpu 2 --io 1 --vm 2 --vm-bytes 128M --timeout 120s

This sets 512MB as the RAM constraint and 512MB as the additional swap space.

Docker supports `b`, `k`, `m`, or `g` representing bytes, kilobytes, megabytes, or gigabytes.

To set or disable swap you would use: `--memory-swap`

This commands sets the amount of memory to 512MB and amount of swap to 256MB:

    docker run --rm -ti --memory 512m --memory-swap=768m progrium/stress --cpu 2 --io 1 --vm 2 --vm-bytes 128M --timeout 120s

Setting `--memory-swap=-1` disables swap entirely

> Again, unlike CPU shares, memory is a hard limit! This is good, because the constraint doesn’t suddenly have a noticeable effect on the container when another container is deployed to the system. But it does mean that you need to be careful that the limit closely matches your container’s needs because there is no wiggle room. An out-of-memory container causes the kernel to behave just like it would if the system were out of memory. It will try to find a process to kill in order to free up space. This is a common failure case where containers have their memory limits set too low. The telltale sign of this issue is a container exit code of 137 and kernel out-of-memory (OOM) messages in the dmesg output.

More stuff in the book about running out of memory

Most on IO and ulimits in the book.

### Starting a Container

`docker create` - creates the docker container configuration but not the running process.

Let's say we needed to run a copy of redis, a common key/value store. It is a lightweight, long-lives process and serves as an example of something we might do in a real environment.

Create the container:

    docker create -p 6379:6379 redis:5.0

This creates the container and gives you the hash.

You can list all containers on your system (including not started ones) with:

`docker ps -a` or `docker container list -a`

Start the redis container with:

    docker start b8990dd4b1b0

There it is:

    docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
    b8990dd4b1b0        redis:5.0           "docker-entrypoint.s…"   About a minute ago   Up 48 seconds       0.0.0.0:6379->6379/tcp   inspiring_ritchie

### Autorestarting a Container

For production applications you want your containers up at all times. Sometimes a sheduler can do this for you.

You can tell docker to handle restarts for you with `--restart` argument. It takes 4 values:

* `no` - Never restart if it exits
* `always` - Always restarts when exits
* `on-failure` - Restarts on a nonzero exit code - `on-filure:3` restarts 3 times then gives up.
* `unless-stopped` - Restart unless intentionally stopped with something like `docker stop`

    docker run -ti --restart=on-failure:3 redis:5.0

### Stopping a container

To stop and start:

    docker stop b8990dd4b1b0
    docker start b8990dd4b1b0

As long as a container has not been deleted, you can restart it without needing to recreate it (build it).

> Containers are just a tree of processes that interact with the system in essentially the same way as any other process on the server

Important as we can send unix signals to our processes.
We sent `SIGTERM` to the container.

If you want to ensure that a container is killed if it hasn't stopped in a certain time:

    docker stop -t 25 b8990dd4b1b

This sends a `SIGKILL` after 25 seconds.

### Killing a Container

    docker kill b8990dd4b1b

> Use `man signal` for more info on signals

More on signals in the book, like `HUP` and `USR1`

### Pausing a Container

If you want to pause and unpause a container:

    docker pause b8990dd4b1b0
    docker unpause b8990dd4b1b0

Reasons for pausing:

* leave resources allocated
* leave entries in the process table
* Taking a snapshot
* Freeing CPU time

Pausing uses `cgroups` [freezer](https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt), pausing does not send any information to the containers about a state change.

### Cleaning up containers and images

We have accumulated a lot of image layers and container folders on our system.

> We must stop all containers that are using an image before removing the image itself

There are times, especially during development cycles, when it makes sense to completely purge all the images or containers from your system

This can be done with:

    docker system prune

To remove only unused images use:

    docker system prune -a

To remove all containers on your docker host:

    docker rm $(docker ps -a -q)

Delete all images on your docker host:

    docker rmi $(docker images -q)

Remove all untagged images:

    docker rmi $(docker images -q -f "dangling=true")

### Windows Containers

Check the book

## 6. Exploring Docker

### Docker version

    $ docker version
    Client: Docker Engine - Community
    Version:           19.03.2
    API version:       1.40
    Go version:        go1.12.8
    Git commit:        6a30dfc
    Built:             Thu Aug 29 05:26:49 2019
    OS/Arch:           darwin/amd64
    Experimental:      false

    Server: Docker Engine - Community
    Engine:
    Version:          19.03.2
    API version:      1.40 (minimum version 1.12)
    Go version:       go1.12.8
    Git commit:       6a30dfc
    Built:            Thu Aug 29 05:32:21 2019
    OS/Arch:          linux/amd64
    Experimental:     false
    containerd:
    Version:          v1.2.6
    GitCommit:        894b81a4b802e4eb2a91d1ce216b8817763c29fb
    runc:
    Version:          1.0.0-rc8
    GitCommit:        425e105d5a03fabd737a126ad93d62a9eeede87f
    docker-init:
    Version:          0.18.0
    GitCommit:        fec3683

### Server Info

Use `docker info`:

    $ docker info
    Client:
    Debug Mode: false

    Server:
        Containers: 6
        Running: 3
        Paused: 0
        Stopped: 3
    Images: 149
    Server Version: 19.03.2
    Storage Driver: overlay2
        Backing Filesystem: extfs
        Supports d_type: true
        Native Overlay Diff: true
    Logging Driver: json-file
    Cgroup Driver: cgroupfs
    Plugins:
        Volume: local
        Network: bridge host ipvlan macvlan null overlay
        Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
    Swarm: inactive
    Runtimes: runc
    Default Runtime: runc
    Init Binary: docker-init
    containerd version: 894b81a4b802e4eb2a91d1ce216b8817763c29fb
    runc version: 425e105d5a03fabd737a126ad93d62a9eeede87f
    init version: fec3683
    Security Options:
    seccomp
    Profile: default
    Kernel Version: 4.9.184-linuxkit
    Operating System: Docker Desktop
    OSType: linux
    Architecture: x86_64
    CPUs: 2
    Total Memory: 1.952GiB
    Name: docker-desktop
    ID: WU2A:7GJU:3UUY:HP3R:P4WD:DSCE:YBRN:TZMM:UAY2:CMA5:3HJH:FTEM
    Docker Root Dir: /var/lib/docker
    Debug Mode: true
    File Descriptors: 54
    Goroutines: 67
    System Time: 2019-09-30T10:26:31.5423907Z
    EventsListeners: 2
    HTTP Proxy: gateway.docker.internal:3128
    HTTPS Proxy: gateway.docker.internal:3129
    Registry: https://index.docker.io/v1/
    Labels:
    Experimental: false
    Insecure Registries:
    127.0.0.0/8
    Live Restore Enabled: false
    Product License: Community Engine

In most installations `/var/lib/docker` will be the default root directory.

### Downloading Image Updates

    docker pull ubuntu:latest

This pulls the latest version of an image

> Docker won’t automatically keep the local image up to date for you. You’ll be responsible for doing that yourself

> It’s always safest to deploy production code using a fixed tag rather than the latest tag. This helps guarantee that you got the version you expected.

### Inspecting a Container

Example: start a container

    docker run -d -t ubuntu /bin/bash

Inspect the container with:

    docker inspect 422ed51e84fc

### Exploring the Shell

Run an ubuntu 16.04 container with a bash shell as the top level process

    docker run -i -t ubuntu:16.04 /bin/bash

Check the processes we are running:

    ps -ef
    
    root         1     0  0 10:53 pts/0    00:00:00 /bin/bash
    root        11     1  0 10:55 pts/0    00:00:00 ps -ef

> The power of docker above. When we told docker to run bash - that is the only thing running.

> Docker containers don’t, by default, start anything in the background like a full virtual machine would.

Anything you do in a container will be lost in the future, you need to add it to the dockerfile for it to persist.

### Returning a Result

> Would you spin up a whole virtual machine in order to run a single process and get the result? You usually wouldn’t do that because it would be very time-consuming and require booting a whole operating system to simply execute one command

_containers are very lightweight and don’t have to boot up like an operating system_

> Running something like a quick background job and waiting for the exit code is a normal use case for a Docker container

Kind of like: **Function as a Service**

If you run the remote command in foreground mode, `docker` will redirect its stdin to the remote process, and the remote process’s `stdout` and `stderr` to your terminal

Docker starts up the container, executes the command that we requested inside the container’s namespaces and cgroups, and then exits, so that no process is left running between invocations

As an example, using the ubuntu image's id. `/bin/false` will always give an exit code of `0`. `/bin/true` will always give n exit code of `0`.

    docker run --rm 657d80a6401d /bin/false
    echo $?
    1

and:

    docker run --rm 657d80a6401d /bin/true
    echo $?
    0

You can also get the output:

    docker run --rm 657d80a6401d /bin/cat /etc/passwd

### Getting inside a running container

There is the docker way with `docker exec` or the linux way with `nsenter`.

#### Docker Exec

The easiest and best way.

Docker exec with an interactive and pseudo-TTY:

    docker exec -it 657d80a6401d /bin/bash

You can check what else is running in the container with:

    ps -ef

    root@422ed51e84fc:/# ps -ef
    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0 10:49 pts/0    00:00:00 /bin/bash
    root        22     0  0 12:02 pts/1    00:00:00 /bin/bash
    root        32    22  0 12:02 pts/1    00:00:00 ps -ef

whereas if we do the same thing on an lxd container:

    lxc exec third -- /bin/bash

there will be a lot more processes:

    root@third:~# ps -ef
    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0 11:59 ?        00:00:00 /sbin/init
    root        53     1  0 11:59 ?        00:00:00 /lib/systemd/systemd-journald
    root        65     1  0 11:59 ?        00:00:00 /lib/systemd/systemd-udevd
    systemd+   155     1  0 11:59 ?        00:00:00 /lib/systemd/systemd-networkd
    systemd+   157     1  0 11:59 ?        00:00:00 /lib/systemd/systemd-resolved
    root       191     1  0 11:59 ?        00:00:00 /usr/lib/accountsservice/accounts-daemon
    syslog     192     1  0 11:59 ?        00:00:00 /usr/sbin/rsyslogd -n
    daemon     194     1  0 11:59 ?        00:00:00 /usr/sbin/atd -f
    root       195     1  0 11:59 ?        00:00:00 /lib/systemd/systemd-logind
    root       196     1  0 11:59 ?        00:00:00 /usr/sbin/cron -f
    message+   199     1  0 11:59 ?        00:00:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-
    root       204     1  0 11:59 ?        00:00:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
    root       213     1  0 11:59 console  00:00:00 /sbin/agetty -o -p -- \u --noclear --keep-baud console 115200,38400,9600 vt220
    root       216     1  0 11:59 ?        00:00:00 /usr/sbin/sshd -D
    root       217     1  0 11:59 ?        00:00:00 /usr/lib/policykit-1/polkitd --no-debug
    root       221     1  0 11:59 ?        00:00:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
    root       304     0  0 12:01 ?        00:00:00 /bin/bash
    root       314   304  0 12:01 ?        00:00:00 ps -ef

`systemd` is installed and running on the `lxc` container. On docker, it is not present.

That shows that lxd containers are meant to be full vm's, whereas docker containers are processed based.

> You can't just start an empty container - well you can but it will exit successfully every time.

You can also run additional processes in the background via `docker exec -d` - but think long and hard before doing so. You will lose repeatability and is useful only for debugging.

> If you’re tempted to do this, you would probably reap bigger gains from rebuilding your container image to launch both processes in a repeatable way

### Nsenter

Part of `util-linux`, `nsenter` allows you to enter any linux namespace.

They are the core of what makes a container a container.

You can use docker to install `nsenter` on the docker server:

    docker run --rm -v /usr/local/bin:/target jpetazzo/nsenter

* this will only work on a linux docker host

> You should be very careful about doing this! It’s always a good idea to check out what you are running, and particularly what you are exposing part of your filesystem to, before you run a third-party container on your system

> With `-v`, we’re telling Docker to expose the host’s `/usr/local/bin` directory into the running container as `/target`

> it is then copying an executable into that directory on our host’s filesystem

More stuff on `nsenter` in the book

#### Docker Volume

List the volumes stored in your root directory

    docker volume ls

> These volumes are not bind-mounted volumes, but special data containers that are useful for persisting data

Create a volume with:

    docker volume create my-data

You can start a container with this volume attached to it:

    docker run --rm --mount source=my-data,target=/app ubuntu:latest touch /app/my-persistent-data

Delete a volume with:

    docker volume rm my-data

### Logging

> Logging is a critical part of any production application

You might expect logs to write to a local logfile, to the kernel buffer `dmesg` or to `systemd` available from `journalctl`. However none of these work because of container restrictions.

Docker makes logging easier because it captures all of the normal text output from applications in the containers it manages.
Anything send to `stdout` or `stderr` is captured by the docker daemon and sent to a configurable logging backend.

#### docker logs

The default logging mechanism.

Get logs with: `docker logs <container_id>`

Nice because you get logs remotely and on demand.

Options for logging:

* `docker logs 422ed51e84fc --tail 50`
* `docker logs 422ed51e84fc -f`
* `docker logs 422ed51e84fc --since 2002-10-02`

The actual files with the logs in are at: `/var/lib/docker/containers/<container_id>/`

Downsides to this form of logging:

* log rotation
* access to logs after rotation
* disk space usage for high-volume logging

You’ll want to make sure you specify the `--log-opt max-size` and `--log-opt max-file` settings if running in production.

### Configurable Logging Backends

`json-file`, `syslog`, `fluentd`, `journald`, `gelf`, `awslogs`, `splunk`, `etwlogs`, `gcplogs` and `logentries`

The simplest for running docker at scale is `syslog`.

You can specify this with `--log-driver=syslog` or setting it as the default in `daemon.json`

`daemon.json` file is the configuration for the `dockerd` server found in `/etc/docker/`

Unless you run `json-file` or `journald`, you will lose the ability to use the `docker logs` command

Many companies already have a syslog architecture in place so it makes it a easy migration path. Newer linux distributions use `systemd` and `journald`

You should be cautious about streaming logs from Docker to a remote log server over TCP or TLS, both run on top of connection-oriented TCP sessions.

> If it fails to make the connection, it will block trying to start the container. If you are running this as your default logging mechanism, this can strike at any time on any deployment.

We encourage you to use the `UDP` option for syslog logging if you intend to use the syslog driver. However, that means logs are not encrypted and not guaranteed delivery.

_We err on the side of reliability_

You can log directly to a remote syslog-compatible server from a single container by setting the log option syslog-address similar to this:

    --log-opt syslog-address=udp://192.168.42.42:123

Most logging pluggins are blocking by default. You can change this setting with: `--log-opt mode=non-blocking`

Then setting the max size: `--log-opt max-buffer-size=4m`

> The application will no longer block when that buffer fills up. Instead, the oldest loglines in memory will be dropped.

#### Non-plugin Community Options

* Log directly from your applicatoin (bypassing docker)
* Process manager relay the logs (`systemd`, `upstart`, `supervisord` or `runit`)
* Run a logging relay in the container that wraps `stdout/sterr`
* Relay docker json logs to a remote logging framework

> Some third party libraries like `supervisor` write to the filesystem.

 Writing logs inside the container is not recommended. It makes them hard to get to, prevents them from being preserved beyond the container lifespan, and can wreak havoc with the Docker filesystem backend.

The main drawback is **they hide logs from docker logs**

The [`svlogd`](http://smarden.org/runit1/svlogd.8.html) daemon can collect logs from your processes `stdout` and ship them to remote hosts over UDP.
It is simple to setup and available ubiquitously.

Another good option is [logsprout](https://github.com/gliderlabs/logspout) which runs in a seperate containe, talks to the docker daemon and logs to syslog.

You can turn off logging with `--log-driver=none`

### Monitoring Docker

> Production systems must be observable and measurable

Docker supports health checks and basic reporting via `docker stats` and `docker events`

    docker stats

works similar to `top`

    CONTAINER ID        NAME                 CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
    422ed51e84fc        competent_einstein   0.00%               788KiB / 1.952GiB     0.04%               2.26kB / 0B         1.68MB / 0B         1
    b8990dd4b1b0        inspiring_ritchie    0.32%               1.539MiB / 1.952GiB   0.08%               2.72kB / 0B         0B / 0B             4

> One common problem with running production containers is that overly aggressive memory limits can cause the kernel OOM (out of memory) killer to stop the container over and over again. The stats command can really help with tracking that down

> With regard to I/O statistics, if you run all of your applications in containers, then this summary can make it very clear where your I/O is going from the system. Before containers, this was much harder to figure out!

> The number of active processes inside the container is helpful for debugging as well. If you have an application that is spawning children without reaping them, this can expose it pretty quickly.

Get stats over http or unix socket:

    curl --unix-socket /var/run/docker.sock http://v1/containers/91c86ec7b33f/stats

#### Container Health Checks

* A container might never actually enter a healthy state where it could receive traffic
* Production systems also fail and may become unhealthy

> Many production environments have standardized ways to health-check applications. Unfortunately, there’s no clear standard for how to do that across organizations and so it’s unlikely that many companies do it in the same way

> Following the shipping container metaphor, Docker containers should really look the same to the outside world no matter what is inside the container

health-check mechanism not only standardizes health checking for containers but also maintains the isolation between what is inside the container and what it looks like on the outside

Example `Dockerfile`:

    FROM mongo:3.2

    COPY docker-healthcheck /usr/local/bin/
    
    HEALTHCHECK CMD ["docker-healthcheck"]

Contents of `docker-healthcheck`:

    #!/bin/bash
    set -eo pipefail

    host="$(hostname --ip-address || echo '127.0.0.1')"

    if mongo --quiet "$host/test" --eval 'quit(db.runCommand({ ping: 1 }).ok ? 0 : 2)'; then
        exit 0
    fi

    exit 1

The image inherits the entrypoint, default command and port to expose

Build the image:

    docker build -t mongo-with-check:3.2 .

Run the container:

    docker run -d --name mongo-hc mongo-with-check:3.2

The status will now have the `health` tag:

    $ docker ps
    CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS                    PORTS                    NAMES
    ff029b988a53        mongo-with-check:3.2   "docker-entrypoint.s…"   35 seconds ago      Up 34 seconds (healthy)   27017/tcp                mongo-hc

You can configure details about the healthchecks:

* `--health-interval` - how often
* `--health-retries` - how many failures are required to mark it unhealthy
* `--no-healthcheck` - disable the health check completely

#### Docker Events

The `dockerd` daemon internally generates an events stream around the container lifecycle

> This events stream is useful in monitoring scenarios or in triggering additional actions, like wanting to be alerted when a job completes

    docker events

Can also hit the api with:

    curl --unix-socket /var/run/docker.sock http://v1/events

Can also use `--since` and `--until` flags

#### Graphs and Visualisations

* DataDog
* GroundWork
* New Relic
* Prometheus
* Nagios

Install [`cAdvisor`](https://github.com/google/cadvisor):

    docker run \
        --volume=/:/rootfs:ro \
        --volume=/var/run:/var/run:rw \
        --volume=/sys:/sys:ro \
        --volume=/var/lib/docker/:/var/lib/docker:ro \
        --publish=8080:8080 \
        --detach=true \
        --name=cadvisor \
        google/cadvisor:latest

You can access it on `http://127.0.0.1:8080`, it also has REST API.

### Prometheus Monitoring

A popular solution for monitoring distributed applications: [Prometheus](https://prometheus.io/)

It works on a pull model, it reaches and gets the info.

**It is for monitoring the dockerd service**

Provide `--experimental` and `--metrics-addr=` options

In `daemon.json`:

    {
        "experimental": true,
        "metrics-addr": "0.0.0.0:9323"
    }

> Any time you make a service available on the network, you need to consider what security risks you might introduce

Restart docker:

    systemctl restart docker

More info on setting up prometheus in the docs

#### Exploration

You can explore some more stuff

* `docker cp` - Copy files in and out of a container
* `docker export` - Saving a container's filesystem to a tarball
* `docker save` - Saving an image to tarball
* `docker import` - Loading an image from tarball

## Debugging Containers

> It’s also important to have a good understanding of debugging containers before moving on to more complex deployments. Without debugging skills, it will be difficult to see where orchestration systems have gone wrong

> It is also critical to understand that your application is not running in a separate system from the other Docker processes. They share a kernel, likely a filesystem, and depending on your container configuration, they may share network interfaces

> Despite feeling in many ways like a virtualization layer, processes in containers are just processes on the Docker host itself

### Process Output

    docker top <container_id>

We get a list of processes running in the container ordered by `pid`.

> Some stripped-down versions of Linux run the Busybox shell, which does not have full ps support

The example in the book are intense - a bit over my head.

### Process Inspection

Again way over my head - using things like `strace`, `lsof` and `gdb`

### Controlling Processes

> Note that unless you kill the top-level process in the container (PID 1 inside the container), killing a process will not terminate the container itself

Killing processes in a container could confuse developers or worse the scheduler - Mesos or Kubernetes or any other system that is health-checking your application.

Some more signal stuff - over my head.

Unless you are using an orchestrator that can handle multiple containers in an abstraction called a pod, it is best to use some process control in production containers: `systemd`, `upstart`, `runit` and `s6`

> Try very hard not to run more than one thing inside your container

What the hell does this mean:

> There are some special needs in a container for processes that spawn background children—that is, anything that forks and daemonizes so the parent no longer manages the child process lifecycle

* Jenkins build containers are one common example where people see this go wrong.
* When daemons fork into the background, they become children of PID 1 on Unix systems. Process 1 is special and is usually an init process of some kind.
* PID 1 is responsible for making sure that children are reaped. In your container, by default your main process will be PID 1

One solution is installing an init system. Even easier is providing the `--init` flag to `docker run`, which will run a very small init system similar to [tini](https://github.com/krallin/tini).
Tini will run as pid 1.

> Whatever you specify in your Dockerfile as the CMD is passed to tini and otherwise works in the same way you would expect. It does, however, replace anything you might have in the `ENTRYPOINT` section of your Dockerfile.

Example:

    docker run -i -t alpine:3.6 sh

    / # ps -ef
    PID   USER     TIME   COMMAND
        1 root       0:00 sh
        6 root       0:00 ps -ef

In this case the `CMD` we launched is `pid 1` - meaning it is responsible for child reaping.

    docker run -i -t --init alpine:3.6 sh

    / # ps -ef
    PID   USER     TIME   COMMAND
        1 root       0:00 /sbin/docker-init -- sh
        6 root       0:00 sh
        7 root       0:00 ps -ef

In this case `pid 1` is `/sbin/docker-init`.

> It’s small enough that you should consider having at least tini inside your containers in production

### Network Inspection

More complicated than process inspection

> Docker containers can be connected to the network in a number of ways

By default it uses the default bridge network that docker creates. This is a virtual network where the host is the gateway to the rest of the world.

View networks:

    docker network ls

    NETWORK ID          NAME                DRIVER              SCOPE
    a4ea6aeb7503        bridge              bridge              local
    b5b5fa6889b1        host                host                local
    08b8b30a20da        none                null                local

* Host network for containers running in `host` network mode - containers share the same network space as the host
* None network that disables network access entirely

View containers connnected to networks with:

    docker network inspect < network_id or name >

You can also see the host `IPv4Address` and the host network address they are bound to `host_binding_ipv4`.

> Note that if you have containers on different networks, they may not have connectivity to each other, depending on how the networks were configured

> In general we recommend leaving your containers on the default bridge network unless you have a good reason not to

More stuff in the book

#### Image History

When you’re building and deploying a single container, it’s easy to keep track of where it came from and what images it’s sitting on top of

    docker history redis:5.0
    
An excellent utility when trying to figure out why the size of the final image is much larger than expected

#### inspecting a Container

If you are on a linux docker host containers are found in `/var/lib/docker/containers`.

* These folders container bind-mounted files and folders - `resolv.conf` and `hostname`.
* It also contains the docker logs by default.
* `config.v2.json` - the json config
* `hostconfig.json` - networking config

#### Filesystem inspection

> A common problem with Dockerized applications is that they continue to write things into the filesystem

Use `docker diff`

    sudo docker diff ff029b988a53
    C /tmp
    A /tmp/mongodb-27017.sock

* `A` - added
* `C` - changed

Usually you can see things like writing to a log `/var/log/redis/redis.log` or `crontab` changes.

## Exploring Docker Compose

To share your projects and work with complex projects requiring more than 1 container.

> If you’re running a whole stack of containers, however, every container needs to be run with the proper setup to ensure that the underlying application is configured correctly and will run as expected

Docker compose can streamline development tasks.

### Configuring Docker Compose

Shell scripts are ok, but they are big and error prone.

> Docker Compose is typically configured with a single, declarative YAML file for each project

Here is an example of the `docker-compose.yml`:

    version: '2'
    services:
      mongo:
        build:
          context: ../../mongodb/docker
        image: spkane/mongo:3.2
        restart: unless-stopped
        command: mongod --smallfiles --oplogSize 128 --replSet rs0
        volumes:
          - "../../mongodb/data/db:/data/db"
        networks:
          - botnet
      mongo-init-replica:
        image: spkane/mongo:3.2
        command: 'mongo mongo/rocketchat --eval "rs.initiate({ ..."'
        depends_on:
          - mongo
        networks:
          - botnet
      rocketchat:
        image: rocketchat/rocket.chat:0.61.0
        restart: unless-stopped
        volumes:
          - "../../rocketchat/data/uploads:/app/uploads"
        environment:
          PORT: 3000
          ROOT_URL: "http://127.0.0.1:3000"
          MONGO_URL: "mongodb://mongo:27017/rocketchat"
          MONGO_OPLOG_URL: "mongodb://mongo:27017/local"
          MAIL_URL: "smtp://smtp.email"
        depends_on:
          - mongo
        ports:
          - 3000:3000
        networks:
          - botnet
      zmachine:
        image: spkane/zmachine-api:latest
        restart: unless-stopped
        volumes:
          - "../../zmachine/saves:/root/saves"
          - "../../zmachine/zcode:/root/zcode"
        depends_on:
          - rocketchat
        expose:
          - "80"
        networks:
          - botnet
      hubot:
        image: rocketchat/hubot-rocketchat:latest
        restart: unless-stopped
        volumes:
          - "../../hubot/scripts:/home/hubot/scripts"
        environment:
          RESPOND_TO_DM: "true"
          HUBOT_ALIAS: ". "
          LISTEN_ON_ALL_PUBLIC: "true"
          ROCKETCHAT_AUTH: "password"
          ROCKETCHAT_URL: "rocketchat:3000"
          ROCKETCHAT_ROOM: ""
          ROCKETCHAT_USER: "hubot"
          ROCKETCHAT_PASSWORD: "HughTheBot"
          BOT_NAME: "bot"
          EXTERNAL_SCRIPTS: "hubot-help,hubot-diagnostics,hubot-zmachine"
          HUBOT_ZMACHINE_SERVER: "http://zmachine:80"
          HUBOT_ZMACHINE_ROOMS: "zmachine"
          HUBOT_ZMACHINE_OT_PREFIX: "ot"
        depends_on:
          - zmachine
        ports:
          - 3001:8080
        networks:
          - botnet
    networks:
      botnet:
        driver: bridge


Use `version` to tell docker the version of the [configuration language](https://docs.docker.com/compose/compose-file/)

    version: '2'

The rest of the doc is divided into `services` and `networks`.

    networks:
      botnet:
        driver: bridge

Create a single network, named botnet, using the (default) bridge driver, which will bridge the Docker network with the host’s networking stack

The `services` section tells docker compose what applications you want to launch: `mongo`, `mongo-init-replica`, `rocketchat`, `zmachine` and `hubot`.

Each named service tells docker how to build, configure and launch the service.

    build:
      context: ../../mongodb/docker

`build` informs docker compose that it should build this image and that the files needed for the build are in that directory. You can also do: `build: ../../mongo/docker`

    image: spkane/mongo:3.2

`image` specifies either the image tag to apply to your build or download and run

    restart: unless-stopped

`restart` specifies when you want to restart containers. 

`command` specifies the command your container should run at startup. In this case it is mongo with a few command line arguments:

    mongod --smallfiles --oplogSize 128 --replSet rs0

> A lot of services have at least some data that should be persisted during development, despite the ephemeral nature of containers. To accomplish this, it is easiest to mount a local directory into the containers.

Use `volumes` to achieve this:

    volumes:
      - "../../mongodb/data/db:/data/db"

The final subsection specifies which network this container should attach to:

    networks:
      - botnet

No `build` with an `image` tells docker compose to pull and launch an existing docker image.

In `environment` you can specify environment variables.

    environment:
      PORT: 3000
      ROOT_URL: "http://127.0.0.1:3000"
      MONGO_URL: "mongodb://mongo:27017/rocketchat"
      MONGO_OPLOG_URL: "mongodb://mongo:27017/local"
      MAIL_URL: "smtp://smtp.email"

Notice that `MONGO_URL` does not use an ip address or FQDN. This is because all services on on the same docker network, configures so containers can be found by their service name.

It makes rearranging easier and explicit the dependencies.

Making use of a `.env` file is useful for secrets and env variables that change between developers.

    depends_on:
      - mongo

`depends_on` defines a container that must be running before this one is started

`ports` defines the ports mapped from the container to the host:

    ports:
      - 3000:3000

`expose` tells docker that we want to expose this port to other containers on the docker network, but not to the underlying host.

Important to check the office [docker-compose](https://docs.docker.com/compose/compose-file/) doc.

### Launching Services

Be in the directory with the `docker-compose.yml` in and check the config:

    docker-compose config

If all is good it will print out the config.

You can build all containers with the `build` command. Services that use `images` will be skipped.

Then you can start all services in the background with:

    docker-compose up -d

> Docker Compose prefixes the network and container names with the name of the directory that contains your docker-compose.yaml

Once everything is up, we can look at the logs for all the services with:

    docker-compose logs

### Docker Compose Commands

Can do `docker-compose top` to see an overview of containers and the processes running that are running in them

You can also do a `docker exec -it` with docker compose:

    docker-compose exec mongo bash
    docker-compose exec <service_name> bash

You can also use `docker-compose start`, `docker-compose stop`.

When want to tear everything down do `docker-compose down`.

## The Path to Production Containers

### Getting to Production

> In that old shipping model, randomly-sized boxes, crates, barrels, and all manner of other packaging were all loaded by hand onto ships. They then had to be manually unloaded by someone who could tell which pieces needed to be unloaded first so that the whole pile wouldn’t collapse like a Jenga puzzle.

> Shipping containers changed all that: we have a standardized box with well-known dimensions. These containers can be packed and unloaded in a logical order and whole groups of items arrive together when expected

To ship to a single server the `docker` cli tooling is enough. To send it to many servers you need more advanced tooling.

1. Locally build and test a docker image on your dev box
2. Build the official image for testing and deployment from CI
3. Push the image to a registry
4. Deploy your docker image to your server

As your workflow evolves, you will eventually collapse those steps into a single fluid workflow.
**Orchestrate the deployment of images and the creation of containers on production servers**

A production story must be:

* Repeatable
* It must handle config for you
* It must deliver an executable artifact

### Dockers role in Production Environments

You can pick and choose the pieces to delegate to docker, to the deployment tool or to larger platforms like Mesos or Kubernetes

Lets look at old components vs New:

| Production Container Component | Component | Traditional COmponent |
|---|---|---|
|   |  Application |   |
| Orchestrator(K8s, Swarm) | Service Discovery, Scheduling, Monitoring  | Static load balancers, deployment scripts, nagios/centOS, on-call staff |
| Docker engine | logging | syslog, rsyslog, logfiles |
| Docker engine | delivery, packaging | deployment scripts, zip files, tarballs, git clone, sc, rsync |
| Docker engine | configuration, networking, resource limits, job control | virtual machines, puppet, chef, init systems |


> Your application is on top! Everything else is there to deliver functionality to your application. After all, it’s the application that delivers business value and everything else is there to make that possible, to facilitate doing it at scale and reliably, and to standardize how it works across applications

#### Job control

We tell the operating system to run a program and manage the lifecycle with `upstart`, `systemd`, `System V init` and `runit`.
We also rely on it to keep the application running. Some jobs also require `cron`.

We want to be able to treat all jobs the same way from the outside.
Docker provides a strong set of primitives around job control - `docker start/stop/run/kill` - simplist elements.

#### Resource Limits

To set limits we can use `cgroups`, `ulimit` and runtime limits for programming languages.
Virtual machines could set these limits hard for a single business application.

It is important to set the limits of CPU, memory and I/O.

#### Networking

Docker provides lots of configuration. YOu should decide on one mechanism to use and standardise across containers - trying to mix them is not an easy path to success.

#### Configuration

2 levels:

* Linux environment - we do this with a `Dockerfile` for a repeatable environment. More traditionally ansible, puppet or chef was used to supply the dependencies.
* Application configuration - Native mechanism is using environment variables.

#### Packaging and Delivery

We have a standardised and consistent way to package or applications and get them to places (docker push and pull). Application components created and configured by the developers handed over to operations to manage.

> In more traditional systems we would have built handcrafted deployment tooling, some of which we hopefully standardized across our applications - in a multilanguage environment, this would have been trouble

> In your containerized environment, you’ll need to consider how you handle packaging your applications into images and how you store those images

#### Logging

This sits on the boundary of docker and platform (k8s, swarm, mesos).
Docker can collect logs from your containers and ship them somewhere - usually to the local system.
In bigger environments you probably want the platform to handle this.

#### Monitoring

Health checking applications in a standardised way - still not fully standardised.
In many systems the platform handles monitoring and the scheduler automatically shuts down unhealthy containers.

> In older systems, it is generally engineers who are paged, respond to issues, and make decisions about how to handle failed applications. In dynamic systems, this work generally moves into more automated processes that belong in the platform

#### Scheduling

How to decide which services run on which servers.

> Containers are easy to move around because Docker provides such good mechanisms for doing so

* better resource usage
* better reliability
* self-healing services
* dynamic scaling

In a traditional sense: You often configured a list of servers into the deployment scripts and the same set of servers would receive the new application on each deployment.

> One-service-per-server models drove early virtualization in private data centers

**Distributed Schedulers**

Let you use it as if it were a single computer.
You define some policies about how you want the application to run and let the system figure out how to run it and how many instances to run.
If something goes wrong, you let the scheduler start it up again on resources that are healthy.
This fits in more with the original vision of docker - running the application without worrying how it gets there.

Zero downtime deployment is done in the blue-green style - ie. 2 production environments managed by a router.

> the scheduler is the system that plays Tetris for you, placing services on servers for best fit, on the fly - Kelsey Hightower

**Apache Mesos**, which was originally written at the University of California, Berkeley, and most publicly adopted by Twitter and Airbnb, is the most mature option

It predates docker, actual scheduling on Mesos is handled be: `HubSpot’s Singularity`, `Mesosphere’s Marathon`, `Mesos’s Chronos` or `Apache Aurora`.

**Kubernetes** came out in 2014, inheriting a lot of what they learned from their internal Borg system.
It was built on docker.

> There are now at least two dozen different commercial distributions of Kubernetes and at least a dozen cloud environments

> The Kubernetes ecosystem has fragmented at a really high rate, with lots of vendors trying to stake out their own territory early on

**Docker Swarm** came out in 2015 and is built as docker native from the ground up.

**Orchestration**

* `Spotify Helios`
* `Ansible's Docker Tooling`
* `NewRelics's Centurion`

Often the best path to production containers lies in containerizing your applications while running inside the traditional system, and then moving on to a more dynamic, scheduled system

**Service Discovery**

Mechanism by which the application finds all the other services and resources it needs on the network

* Rare is the application that has no dependency on anything else.
* Stateless, static websites are perhaps one of the only systems that may not need any service discovery.

In traditional systems, load balancers were one of the primary means for service discovery.

> Other means for service discovery in older systems are static database configurations or application configuration files

> For the vast majority of systems, service discovery is left to the platform

Existing service discovery methods:

* Load-balancers with well-known addresses
* DNS SRV records
* Round robin DNS
* Multicast DNS
* Overlay networks with well-known addresses
* Gossip protocols
* Apple's bonjour protocol
* Apache zookeeper
* Hashicorp's Consul
* CoreOS's etcd

> Often the best initial system (though not necessarily longer-term) is a system where you present dynamically configured load balancers that are easily reachable by systems in your older environment

Examples of the above (oh god what the hell is all this):

* Mesos backend for the Traefik load balancer
* Nixy for nginx and Mesos
* Kubernetes’s ingress controllers
* Standalone Sidecar service discovery with Lyft’s Envoy proxy
* Istio and Lyft’s Envoy

> We suggest using the lightest-weight tool for the job

### Docker and the Devops Pipeline

> One of the key promises of Docker is the ability to test your application and all of its dependencies in exactly the operating environment it would have in production

What it can't do:

* It can’t guarantee that you have properly tested external dependencies like databases
* it does not provide any magical test framework

> It can make sure that your libraries and other code dependencies are all tested together

_With Docker, you can build your image, run it on your development box, and then test the exact same image with the same application version and dependencies before shipping it to production servers_

Typical workflow:

1. build is triggered
2. build server kicks off a docker build
3. image is created on the local docker
4. the image is tagged with a build number or commit hash
5. a container is configured to run the test suite against the newly built image
6. Test suite is run against the container
7. The build is marked as passing or failing
8. Passed builds are shipped to the image store (registry)

Eg.

1. Push to git repo
2. Post commit hook triggers build on commit
3. Test server runs docker build on remote
4. Generating a new image on the remote docker server
5. Run a new container based on the image
6. Test the container 

We run this command:

    docker run -e ENVIRONMENT=testing -e API_KEY=12345 -i -t awesome_app:version1 /opt/awesome_app/test.sh

* We set a few environment variables for the container: `ENVIRONMENT` and `APIKEY`
* We ask for a particular tag for the image
* We override the `CMD` to call our test script `/opt/awesome_app/test.sh`

> In some cases you have to override `--entrypoint`

Ensure to always use the **precise** tag and not `latest` - to ensure you are testing the right version of the application.

> A critical point to make here is that docker run will exit with the exit status of the command that was invoked in the container

If the exit code is `0`, it was successful.

[Some greater tips on building images from OpenShift](https://docs.okd.io/latest/creating_images/guidelines.html)

The final step is taking our passed build and pushing that to the registry.

The **registry** is the interchange point between builds and deployments.

> Critically, our fictional company’s system makes sure they only ship applications whose test suite has passed on the same Linux distribution, with the same libraries and the same exact build settings. That container might then also be tested against any outside dependencies like databases or caches without having to mock them

#### Outside Dependencies

Examples: database, Memcache or Redis - you can solve this with docker compose.

> You’ll still need to rely on your own language’s testing framework for the tests

## Docker at Scale

> One of Docker’s major strengths is its ability to abstract away the underlying hardware and operating system so that your application is not constrained to any particular host or environment

You can scale not only horizontally but also across cloud providers.
A container on one cloud looks like a container on another.

The biggest efforts to implement docker in the public cloud is:

* ECS Amazon Elastic Container Service
* Google Kubernetes Engine
* Azure Container Service
* Red Hat Openshift

> Much of the tooling will work equally well in either a public cloud or your own data center.

> A first step using built-in tooling might be to leverage Docker Engine’s Swarm mode to deploy containers easily across a large pool of Docker hosts

Something even simpler would be Ansible's docker tooling, New Relic Centurion or Spotify's Helios, without the complexity of a full blown scheduler.

* Docker Swarm mode - used by Portainer
* Kubernetes
* Openshift
* Apache Mesos

### Centurion

Repeatable deployment of applications to a group of hosts.

* Most scheduler platforms treat the cluster as a single machine - you instead tell Centurion about each individual host
* It's focus is guaranteeing repeatability and zero down-time deployments
* First step in moving from traditional application
* It assumes a load balancer sits in front of your applications

Helios is similar but Centurion is deemed the easiest of the tools

It uses `ruby` - more in the book

### Docker Swarm Mode

After building the docker engine - the runtime for containers - docker engineers turned to orchestrating a fleet of docker hosts.

Originally `docker swarm` was standalone. But there is anotehr swarm called `swarm mode` - built into the docker engine.
Swarm mode is meant to replace standalone docker warm entirely.

Swarm mode has the major advantage of not requiring you to install something seperately.

Docker swarm is used to present a single interface to the docker client tool, but have the interface backed by a cluster.
In some situations it is possible to start with a simple solution like Swarm and graduate to Kubernetes without needing to change many of the tools that users rely on.

#### Setting up swarm

You need 3 ubuntu servers running `docker-ce` that can talk to each other.

Setup info is in the book.

To see the nodes:

    docker node ls

Wow, it looked complicated...more in the book

### Amazon ECS and Fargate

Support for running containers natively has existed since 2014 in Elastic Beanstalk - but this service assigns only a single container - not ideal for short-lived and light weight containers.

ECS (Elastic Container Service), EKS (Elastic Kubernetes Service) and Fargate has containers as first class citizens.

_Fargate_ is just a name for features allowing AWS to automatically manage all the nodes in your cluster

Setup is in the book

### Kubernetes

* Released to the public at DockerCon 2014
* Grown rapidly and is the most widely adopted platform
* Mesos is the most mature product - launching before docker in 2009
* Great mix of functionality and community

Like Linux - Kubernetes is available in a number of distributions, both free and commercial.

It has some nice tooling like `minikube`.

#### Minikube

A whole distribution of kubernetes for a single instance.
It runs on a virtual machine and has the same tooling as a production system.
It's a bit like `docker compose` - but it has all the production API's.

You need 2 tools:

* `minikube` - 
* `kubectl` - 

Install on MacOS:

    brew cask install minikube

Check it is on your path:

    which minikube
    /usr/local/bin/minikube

You then need `kubectl` installed with:

    brew install kubernetes-cli

Running kubernetes:

    minikube start

> We installed a virtual machine that has a properly configured version of Docker on it. It then runs all of the necessary components of Kubernetes inside Docker containers on the host.

To see what is happening you can ssh into `minikube` and check the containers running:

    minikube ssh

    $ docker container list

Check status of minikube:

    $ minikube status
    host: Running
    kubelet: Running
    apiserver: Running
    kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100

Check the ip of the minikube ip:

    $ minikube ip
    192.168.99.100

Check version:

    $ minikube update-check
    CurrentVersion: v1.4.0
    LatestVersion: v1.4.0

Starting and stopping the cluster:

    minkube start
    minikube stop

#### Kubernetes Dashboard

You access it with:

    minikube dashboard

Under the `nodes` tab, you will see a single node named `minikube`.

> Kubernetes exposes everything with the `kubectl` command

#### Kubernetes Containers and Pods

There is an abstraction that sits on layer above containers and that is `pods`.
A pod is one or more containers sharing the same `cgroups` and `namespaces`.

The idea is you have applications that need to be deployed together all the time. So the sheduler works with a group of applications not a single container.

All the containers in a pod can talkto eachother on localhost, eliminating the need to discover each other.

The advantage of a pod over a supercontainer is you can resource the individual application seperately and leverage public docker containers to construct your application.

A pod can also share mounted volumes.

Pods are also ephemeral - lasting a very short time.

Containers in a pod share the same ip when facing the outside world - they look like a single entity from the network level.

You generally run one instance of a container per pod.

A critical difference is that pods are not created in a build step. They are runtime abstractions existing only in kubernetes.

> So you build your Docker containers and send them to a registry, then define and deploy your pods using Kubernetes

You don't directly describe a pod either - the tools generate it for you.

_the pod is the unit of execution and scheduling in a Kubernetes cluster_

#### Let's Deploy

A deployment is a pod definition with some health checking and replication

To get things done on kubernetes we use the `kubectl` command.

    kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080

But that was `DEPRECATED` so better to run:

    kubectl run --generator=run-pod/v1
    
    kubectl create 

Now we can view what is in our cluster with:

    kubectl get all

    NAME                                  READY   STATUS    RESTARTS   AGE
    pod/hello-minikube-75cb6dd856-rgwhs   1/1     Running   0          2m59s

    NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   14h

    NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
    deployment.apps/hello-minikube   1/1     1            1           2m59s

    NAME                                        DESIRED   CURRENT   READY   AGE
    replicaset.apps/hello-minikube-75cb6dd856   1         1         1       2m59s

Kubernetes created a: `pod`, `service`, `deployment` and a `replicaset`

We now need to tell kubernetes to expose a port:

    kubectl expose deployment hello-minikube --type=NodePort

> We get a NodePort, which works a lot like EXPOSE would for a container on Docker itself, but this time for the whole deployment

We then ask kubernetes how to get to it:

    kubectl get svc

    NAME             TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
    hello-minikube   NodePort    10.109.80.87   <none>        8080:31288/TCP   3m14s
    kubernetes       ClusterIP   10.96.0.1      <none>        443/TCP          14h

but we can't actually get to: `10.109.80.87:8080`, as it is not accessible from your host system because it is in the vm running `minikube`.

So we need `minikube` to tell us how to access it:

    minikube service hello-minikube --url
    http://192.168.99.100:31288

The nice thing is this command is command-line friendly:

    curl $(minikube service hello-minikube --url)

Delete the service and deployment on `minikube`:

    kubectl delete service hello-minikube
    kubectl delete deployment hello-minikube

then all that is left is:

    $ kubectl get all
    NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   16h

#### Deploying a Realistic Stack

> Kubernetes, much like Docker Compose, lets us define our stack in one or more YAML files that contain all of the definitions we care about in one place

* `lazyraster` is the service
* `cache-data` will be the persistent volume

Kubernetes has a huge vocabulary some terms:

* `PersistentVolume` - physical resource that we provision inside the cluster, supports many kinds of volumes from local storage on a node to EBS volumes on AWS. Lifecycle is independent from our application.
* `PersistenVolumeClaim` - link between physical resource of `PersistentVolume` and the application that needs to consume it.

We set a policy for a single read/write claim or many.

Kubernetes has a [glossary](https://kubernetes.io/docs/reference/glossary/?fundamental=true).

**Service Definition**

    apiVersion: v1
    kind: Service
    metadata:
      name: lazyraster
      labels:
        app: lazyraster
    spec:
      type: NodePort
      ports:
        - port: 8000
          targetPort: 8000
          protocol: TCP
      selector:
        app: lazyraster
    ---
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: cache-data-claim
      labels:
        app: lazyraster
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 100Mi
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: lazyraster
      labels:
        app: lazyraster
    spec:
      selector:
        matchLabels:
          app: lazyraster
      strategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app: lazyraster
        spec:
          containers:
          - image: relistan/lazyraster:demo
            name: lazyraster
            env:
            - name: RASTER_RING_TYPE
              value: memberlist
            - name: RASTER_BASE_DIR
              value: /data
            ports:
            - containerPort: 8000
              name: lazyraster
            volumeMounts:
            - name: cache-data
              mountPath: /data
          volumes:
          - name: cache-data
            persistentVolumeClaim:
              claimName: cache-data-claim

There is alot of info in the book about this.
Create the service with:

    $ kubectl create -f lazyraster-service.yaml
    service/lazyraster created
    persistentvolumeclaim/cache-data-claim created
    deployment.apps/lazyraster created

we got a service, a persistent volume claim, and a deployment.

To view our volumes we have to ask seperately:

    kubectl get pvc
    NAME               STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
    cache-data-claim   Bound    pvc-9dd3c7ca-0c97-43b7-971d-83bc358e096e   100Mi      RWO            standard       4m24s

There is a [kubernetes cheat sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) for easier commands

> A ReplicaSet is a piece of Kubernetes that is responsible for making sure that our application is running the right number of instances all the time and that they are healthy

View the url:

    minikube service --url lazyraster

To scale a service up we do:

    kubectl scale --replicas=2 deploy/lazyraster

Check that it worked:

    kubectl scale --replicas=2 deploy/lazyraster
    deployment.apps/lazyraster scaled

Now we have 2 instances:

    $ kubectl get deploy/lazyraster
    NAME         READY   UP-TO-DATE   AVAILABLE   AGE
    lazyraster   2/2     2            2           24m

You can check the logs with:

    kubectl logs deploy/lazyraster

To get logs for a specific container:

    kubectl get po
    
    NAME                         READY   STATUS    RESTARTS   AGE
    lazyraster-8769c6b7b-gmcww   1/1     Running   0          2m42s
    lazyraster-8769c6b7b-qg9zq   1/1     Running   0          26m

then you can get the logs for a specific pod:

    kubectl logs po/lazyraster-6b8dd8cb66-rqmfx

Check it out on the dashboard

    minikube dashboard

#### Kubectl API

There is also a kubectl API

### Conclusion Kubernetes at Scale

There are many options, that overlap and have their own ideas of what production systems should look like.

Underlying all these tools is the `docker` bedrock.

## Advanced Topics

> Docker has good defaults

> You should stick to the defaults on your operating system unless you have a good reason to change them

### Containers in Details

Control groups (`groups`), namespaces and SELinux all contain the process.

> When running Docker, your computer is the hotel. Without Docker, it’s more like a hostel with open bunk rooms. In our modern hotel, each container that you launch is an individual room with preferably only 1 guest in it.

Control groups are like the floor, walls and ceiling of the room - preventing guests from using other rooms' resources.
SELinux and AppArmour are like hotel security.

A lot on cgroups, namespaces, security, privileged modes, SELinux, AppArmour, the docker daemon, host networking, configuring networks, storage and the structure of docker in the book.

## Container Platform Design

> If, instead of simply deploying Docker into your existing environment, you take the time to build a well-designed container platform on top of Docker, you can enjoy the many benefits of a Docker-based workflow while simultaneously protecting yourself from some of the sharper edges that can exist in such high-velocity projects

### The 12 Factor App

12 practices for designing applications that will thrive and grow in a modern container-based Software-as-a-Service (SaaS) environment

_1. One codebase tracked in revision control_

> A good test might be to give a new developer in your company a clean laptop and a paragraph of directions and then see if they can successfully build your application in under an hour

_2. Explicitly declare and isolate dependencies_

Dependencies should be defined in the repoand pulled by the build process

_3. Store configuration in environment variables, not in files checked into the codebase_

This makes it simple to deploy the exact same codebase to different environments, like staging and production, without maintaining complicated configuration in code or rebuilding your container for each environment

> These configuration items are now an external dependency that we can inject at runtime

In case of secrets, use [docker secret](https://docs.docker.com/engine/swarm/secrets/) and [Hashicorp Vault](https://www.vaultproject.io/)

_4. Treat backing services as attached resources_

> Applications should handle the loss of an attached resource gracefully

> When using containers, you achieve high availability most often through horizontal scaling and rolling deployments, instead of relying on the live migration of long-running process, like on traditional virtual machines

_5. Strictly separate build and run stages_

_6. Execute the app as one or more stateless processes_

> All shared data must be accessed via a stateful backing store so that application instances can easily be redeployed without losing any important session data

> You don’t want to keep critical state on disk in your ephemeral container, nor in the memory of one of its processes

When you must maintain state, the best approach is to use a remote datastore like Redis, PostgreSQL, Memcache, or even Amazon S3, depending on your resiliency needs.

_7. Export services via port binding_

_8. Scale out via the process model_

Adding and removing instances is easier than increasing resources.

This is where tools like: Docker swarm mode, kubernetes, Mesos and Openshift; beign to shine.

_9. Maximise Robustness with fast startup and graceful shutdown_

Services should be designed to be ephemeral.

_10. Keep development, staging, and production as similar as possible_

The same processes, artifacts and people should be used.
Repeatability is very important.

_11. Treat logs as event streams_

Services should not concern themselves with routing or storing logs. Events should be streamed, unbuffered to `STDOUT` or `STDERR`.

_12. Run admin/management tasks as once off processes_

One-off administration tasks should be run via the exact same codebase and configuration that the application uses. You should never rely on random cron-like scripts to perform administrative and maintenance functions.

### The Reactive Manifesto

* Responsive - _The system responds in a timely manner if at all possible_
* Resilient - _The system stays responsive in the face of failure._
* Elastic - _The system stays responsive under varying workload_
* Message-Driven - _Reactive systems rely on asynchronous message passing to establish a boundary between components that ensures loose coupling, isolation, and location transparency._

## Conclusion

In traditional software development and deployment: there are many steps.
Every step introduces risk.

Problems docker helps solve:

* Large divergence between deployment environments
* Requiring developers to manage configuration and logging
* Outdated release processes requiring multiple hand-offs
* Complex and fragile build processes
* Divergent dependency versions
* Managing multiple linux distributions
* Building a one-off deployment process for each application

Using the registry as a handoff point eases the communication between operations and development.
Docker isolates operations teams from the build process and puts developers in charge of their dependencies.

Docker defines a single artifact as the result of a build.

Docker allows software developers to create Docker images that, starting with the very first proof of concept, can be run locally, tested with automated tools, and deployed into integration or production environments without ever having to be rebuilt

The application that is launched in production is exactly the same as what was tested

> A single build step replaces a typically error-prone process that involves compiling and packaging multiple complex components for distribution

> Organizations can begin to move away from having to create custom physical servers or virtual machines for most applications, and instead deploy fleets of identical Docker hosts that can be used as a large pool of resources to dynamically deploy their applications to

_Developers gain more ownership of their complete application stack_

> Operations teams are freed from spending most of their time supporting the application and can focus on creating a robust and stable platform for the application to run on

## Important Points

> You should build your container image exactly as you’ll ship it to production. If you need to make concessions for testing, they should be externally provided switches, either via environment variables or through command-line arguments

> The whole idea is to test the exact build that you’ll ship, so this is a critical point.


## Containers and Images

In Dockerland, there are images and there are containers.

Images:

* Inert, immutable, file that's essentially a snapshot of a container
* Created with the `build` command
* Produce a container when started with `run`
* Images are stored in a docker registry

View images with `docker image list`

    $ docker image list
    REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
    vm-api_web              latest              6073bacca5c4        4 days ago          1.08GB
    <none>                  <none>              94fccc848ad4        4 days ago          919MB

Container:

* Instances of the image
* Lightweight and portable encapsulations of an environment in which to run applications

    $ docker container list
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
    22b895f2b5d6        postgres:10.10      "docker-entrypoint.s…"   4 days ago          Up 4 days           5432/tcp                 vm-api_db_1
    9832a0d8363e        vm-api_web          "python manage.py ru…"   4 days ago          Up 4 days           0.0.0.0:8000->8000/tcp   vm-api_web_1

## Cleaning up

There is a seemingly constant buildup of untagged images and stopped containers....what do you do?

Remove stopped containers first:

    docker rm `docker ps --no-trunc -aq` 

Remove untagged images:

    docker images -q --filter "dangling=true" | xargs docker rmi


Manual Config: SSH and manually install on other servers have to repeat effort. Not portable, minimal overhead

Configuration management tools: Still need to run on each VM

Docker (In between): Offers most isolation benefits of traditional virtual machines without overhead of a guest OS

Traditional VM: Very portable, lots of overhead

Docker has no guest OS, the docker engine leverages the host OS to provide virtual environment.
Binaries and libraries can be shared across applications.

## Running Containers

Rule of thumb: 1 docker container for each process in your stack

- Single image for load balancer
- Single image for applications
- Single image for database

## Benefits of Docker

There is a lot of shit going on in your development environment. But when sharing between developers and deploying you couldn't manage the environment.

Emulating the environment is easier, espescially in corporates.

Someone has to create the initial environment, there is a learning curve.

## Running docker

You need the `docker toolbox`

It uses `virtualbox`

## Getting into a docker container

Getting in and running commands on the container means getting into it's shell with:

    docker exec -it <container_id> /bin/bash

or 

    docker exec -it <container_id> sh

## Sources

* [Docker: Up and Running](https://learning.oreilly.com/library/view/docker-up)
* [How to automate docker deployments](http://paislee.io/how-to-automate-docker-deployments/)