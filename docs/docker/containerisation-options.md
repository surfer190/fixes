---
author: ''
category: Docker
date: '2019-11-04'
summary: ''
title: Containerisation Options
---
# Orchestration Options

## Container Orchestration Systems
 
Treats a cluster of machines as a single deployment and manages containers

* Apache Mesos
* Docker Swarm mode - only docker containers
* Kubernetes

## Container Orchestration Framework/Platform

* Marathon + DC/OS - uses Apache Mesos (Can manage a kubernetes cluster)
* Openshift - uses Kubernetes
* Rancher - uses Kubernetes
* Kubernetes "vanilla" - installed from the official repos is also a platform

> Why are people doing Openshift OKD vs Kubernetes. Kubernetes is an upstream to OKD.

There are alot of articles and information overlaod but what you really want is simplification

## Cloud Based Container Orchestration

* Amazon ECS (Elastic Container Service) and EKS (Elastic Kubernetes Service)
* Google Cloud Platform (GCP)
* Azure Container Service
* Digital Ocean Kubernetes Service
* Red Hat OpenShift Online

### Sources

* [Container Orchestration Explained](https://blog.newrelic.com/engineering/container-orchestration-explained/)
* [Awesome Linux Containers](https://github.com/Friz-zy/awesome-linux-containers#readme)
* [A Comparison of Kubernetes Distributions](https://dzone.com/articles/kubernetes-distributions-how-do-i-choose-one)