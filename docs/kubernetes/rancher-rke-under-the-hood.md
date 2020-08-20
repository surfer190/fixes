---
author: ''
category: Kubernetes
date: '2019-12-24'
summary: ''
title: Rancher Rke Under The Hood
---
# Rancher Kubernetes Engine

* RKE (Rancher Kubernetes Engine) is a CNCF-certified kubernetes distribution
* Runs entirely with docker containers

RKE uses `cluster.yml` to define the kubernetes cluster
Each `cluster.yml` represents a seperate kubernetes cluster.

    rke up --config cluster.yml

**cluster.yml**

    ---
    nodes:
      - address: 10.0.0.1
        role: [controlplane, etcd, worker]
        user: ubuntu
        hostname_override: node1

Check RKE version

    $ rke --version
    rke version v0.3.2

