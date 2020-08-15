---
author: ''
category: Kubernetes
date: '2019-12-24'
summary: ''
title: Ssh Into Kubernetes Pod
---
# How do you SSH into a Kubernetes Pod

Get your pod name

    $ kubectl get pods
    NAME                       READY   STATUS    RESTARTS   AGE
    nginx-fast-storage-wknfz   1/1     Running   0          8h
    queue-pfmq2                1/1     Running   0          149m

Then run `kubectl exec -it`

    kubectl exec -it queue-pfmq2 -- sh

