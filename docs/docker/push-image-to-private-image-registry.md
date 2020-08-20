---
author: ''
category: Docker
date: '2020-06-14'
summary: ''
title: Push Image To Private Image Registry
---
## Pushing Docker Image to a Private Image Registry

Many docker scheduler and orchestrator platforms provide an internal private registry.
This means that you do not use the default and public `index.docker.io` image registry.

I know that the following platforms let you create an internal registry:

* portainer
* Openshift: OKD

_Setting up a docker registry is beyond the scope of this article_

### Intial Setup

The first thing to do is ensure that the image you have created has been tested and is production ready.

Do you have to know which registry you are building for?

Try and login to your registry to ensure it is setup correctly:

    docker login some.docker.host.com
    Username: foo
    Password:
    Login Succeeded

1. Find the container id and commit it to a new image name

    docker commit c16378f943fe my-api

2. Tag the remote repo for that image

    docker tag my-api registry.example.co.za:5000/my-api:0.1

3. Push the image

    docker push registry.example.co.za:5000/my-api:0.1

Check if it worked by doing:

    docker image list

It should list both the local and remote versions

## Sources

* [Docker Push](https://docs.docker.com/engine/reference/commandline/push/)




