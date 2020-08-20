---
author: ''
category: Kubernetes
date: '2020-06-14'
summary: ''
title: K3s
---
# K3S

### Arm

* Global leader in IP licensing. ARM CPU's are designed and licensed.
* Don't create any chips or sell systems - just sell the IP
* Partners have freedom to create and build interesting things

### Data Bandwidth and latency drive future designs

The internet started when clients would be primarily downloading from the cloud - from the cloud to endpoints.

Now we have many devices that want to share data and send it upstream.

### Why k3s on ARM?

Now applications on devices are being deployed as containers - with more smarts on the device.
k3s is a good fit for these devices - lightweight.

Deploying applications on devices from the cloud.



## Architecture

    k8s master == k3s server
    k8s worker == k3s agent

### k3s HA Requirements

* Unique hostnames
* Linux - Ubuntu 16, 18 or raspbian buster

Minimum: 512Mb RAM, 1 CPU and SSD is recommended

Networking:

* 6443 (api-server)
* 8472 UDP (flannel - CNI?)
* 10250 (metrics-server)

Need to be open for nodes

HA can be setup with 2 nodes.
2 combined server/agent + 1 external db

For k8s 3 nodes are needed for etcd requirements and need for a quorum
