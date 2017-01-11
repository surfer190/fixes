# Docker Basics

## What is docker?

* Virtualization: vmware, virtual box (a.k.a a hypervisor - makes it think it is on real hardware) - emulate hardware
* VM manager: vagrant - a virtual machine manager
* Configuration management - Chef, Ansible and Puppet

Docker is **not** in any of these categories

Open platform to build, ship and run distributed applications

2 Parts:
* Docker engine: powers docker locally
* Docker hub: cloud service to share images

Manual Config: SSH and manually install on other servers have to repeat effort. Not portable, minimal overhead

Configuration management tools: Still need to run on each VM

Docker (In between): Offers most isolation benefits of traditional virtual machines without overhead of a guest OS

Traditional VM: Very portable, lots of overhead

Docker has no guest OD, the docker engine leverages host OS to provide virtual environment.
Binaries and libraries can be shared across applications.

## Running Containers

Rule of thumb: 1 docker container for each process in your stack

- Single image for load balancer
- Single images for applications
- Single image for database

## Benefits of Docker

There is a lot of shit going on in your development environment. But when sharing between developers and deploying you couldn't manage the environment.

Emulating the environment is easier, espescially in corporates.

Someone has to create the initial environment, there is a learning curve.

## Running docker

You need the `docker toolbox`

It uses `virtualbox`
