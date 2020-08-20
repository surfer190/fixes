---
author: ''
category: Docker
date: '2019-10-24'
summary: ''
title: Docker Faq
---
# Docker Frequently Asked Questions

## Can you Assign port mappings to running containers

**No, you can't**

You need to recreate the containers

Eg.

    docker run -d -p 15672:15672 -p 5672:5672 rabbitmq:3-management

Source: [Stackoverflow assign port mappings to exisitng containers](https://stackoverflow.com/questions/19335444/how-do-i-assign-a-port-mapping-to-an-existing-docker-container/58432955#58432955)

## Can you access a docker container directly via it's internal ip or do you have to bind to the host port

You can, but not on mac.

Inspecting your containers ip will gives its internal ip.

[Docker Desktop for Mac can’t route traffic to containers](https://docs.docker.com/docker-for-mac/networking/#i-cannot-ping-my-containers), do you won't be able to ping or access it.

Weirdly you can nmap that private ip.

Source: [Networking features in Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/networking/#i-cannot-ping-my-containers)