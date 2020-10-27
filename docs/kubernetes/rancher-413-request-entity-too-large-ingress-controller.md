---
author: ''
category: Kubernetes
date: '2020-10-27'
summary: ''
title: Rancher RKE 413 Request Entity Too Large when uploading a file Nginx controller
---

Sometimes you will get an error in you client application when uploading a large file to a server running kubernetes and the nginx ingress controller

    413 Client Error: Request Entity Too Large

What we need to do in this case is change the settings for the specific ingress controller (loab balancer) for your workload.

## To Fix

Go to: `Workloads > Load balancing > (Select your Ingress) > Labels & Annoations`

and add the annotatoin:

    nginx.ingress.kubernetes.io/proxy-body-size: 0

![rancher-fix-kubernetes-413](/img/kubernetes/rancher-annotation-nginx-413.png)

## Sources

* [Fixing 413 Request Entiy Too Large on Rancher](https://github.com/rancher/rancher/issues/14323)