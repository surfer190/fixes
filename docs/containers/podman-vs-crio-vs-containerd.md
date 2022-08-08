---
author: ''
category: Containers
date: '2022-06-30'
summary: ''
title: Podman vs Cri-o vs Containerd
---

I have always used `docker` to build my images.
Docker pretty much did all things and contained various parts:

* `Docker engine`: powers docker locally - a portable, lightweight runtime and packaging tool
* `Docker hub`: cloud service to share images
* `docker compose`: mechanism to define and run multi-container applications
* `docker swarm`: container orchestration for production
* `docker registry`: server side application that stores and lets you distribute Docker images
* `docker machine`: tool that lets you install Docker Engine on virtual hosts and manage hosts

The part that does the image building from a `Dockerfile` is the `docker engine`.

There was corporate action - docker was acquired by Mirantis - and that shook up the industry.

It was noted that: Kubernetes is deprecating support for Docker as a container runtime starting with Kubernetes version 1.20.

A CRI (Container Runtime Interface) is a a standard way of communicating between Kubernetes and the container runtime.

Docker does not implement a CRI and a docker shim was created by kubernetes to support it.
Docker is a collection of tools that sit on top of `containerd`

Docker makes the process easier of using the `containerd` runtime.

If you are using docker as teh container runtime on kubernetes you will need to remove the middleman.

### Confusion: Container Runtime vs Container Engine

When reading the podman docs they refer to:

* Container engines: Docker, CRI-O, containerd
* Container runtimes: runc, crun, runv

## Podman vs Cri-o vs Containerd

So we know now that Docker is not a container runtime and uses containerd behind the scenes.

[More info on LWN][lwn_link]


## Sources

* [Kubernetes deprecating docker what you need to know](https://acloudguru.com/blog/engineering/kubernetes-is-deprecating-docker-what-you-need-to-know)
* [Podman](https://docs.podman.io/en/latest/)
* [containerd](https://containerd.io/docs/getting-started/)
* [cri-o](https://cri-o.io/)
* [container terminology](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction)

<!-- https://arcticicestudio.github.io/styleguide-markdown/rules/links.html -->
[lwn_link]: https://lwn.net/SubscriberLink/902049/374614a66c0367f3/