---
author: ''
category: Kubernetes
date: '2020-01-13'
summary: ''
title: Troubleshooting And Debugging Kubernetes
---
## Troubleshooting K8s - Common Issues in K8S - finding the reasons and Fixing Them

## Pod in ImagePullBackOff

With an error message like: `Back-off pulling image registry.co.za/repo/image_name:hash`

A lot of tutorials say uou should use `describe` on the pod. This is **wrong**.
You **cannot describe the pod if it is not running**.
It will not be running as k8s cannot even get the image is should run.

The best place to start is to look at the [`events` of a pod](https://stackoverflow.com/questions/51931113/kubectl-get-events-only-for-a-pod) with:

    kubectl get event -n portal --field-selector involvedObject.name=my-pod-zl6m6

You will get output like:

    LAST SEEN   TYPE      REASON    OBJECT                                 MESSAGE
    21m         Normal    BackOff   pod/my-pod-zl6m6   Back-off pulling image "registry.co.za/repo/image_name:hash"
    71s         Warning   Failed    pod/my-pod-zl6m6   Error: ImagePullBackOff

but that is telling us what we already know.

If there is only 1 pod in the namespace it is easier to look at all events in the namespace:

    kubectl get event -n portal

But there is no clear indication except for in rancher on a rare occasion it will show the actual error from the registry:

    ErrImagePull: rpc error: code = Unknown desc = Error response from daemon: Get https://registry.co.za/v2/repo/image_name/manifests/1c9d75694a5c7a016da73d851b44737eb5bff0b8: Get https://core.harbor.domain/service/token?scope=repository%3Acrepo%2Fimage_name%3Apull&service=harbor-registry: dial tcp: lookup core.harbor.domain: no such host

In which case sometimes the registry gives errors...

### A Pod is stuck in Pending State

Here a MySQL pod has been stuck for 48 minutes in a `Pending` state

    $ kubectl get pods
    NAME          READY   STATUS    RESTARTS   AGE
    mysql-6q5hp   0/1     Pending   0          48m

Describe the pod:

    $ kubectl describe pod mysql-6q5hp
    Name:           mysql-6q5hp
    Namespace:      default
    Priority:       0
    Node:           <none>
    Labels:         app=mysql
    Annotations:    <none>
    Status:         Pending
    IP:             
    IPs:            <none>
    Controlled By:  ReplicaSet/mysql
    Containers:
    database:
        Image:      mysql
        Port:       3306/TCP
        Host Port:  0/TCP
        Requests:
        cpu:     1
        memory:  2Gi
        Liveness:  tcp-socket :3306 delay=0s timeout=1s period=10s #success=1 #failure=3
        Environment:
        MYSQL_ROOT_PASSWORD:  some-password-here
        Mounts:
        /var/lib/mysql from database (rw)
        /var/run/secrets/kubernetes.io/serviceaccount from default-token-mbn5b (ro)
    Conditions:
    Type           Status
    PodScheduled   False 
    Volumes:
    database:
        Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
        ClaimName:  database
        ReadOnly:   false
    default-token-mbn5b:
        Type:        Secret (a volume populated by a Secret)
        SecretName:  default-token-mbn5b
        Optional:    false
    QoS Class:       Burstable
    Node-Selectors:  <none>
    Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                    node.kubernetes.io/unreachable:NoExecute for 300s
    Events:
    Type     Reason            Age        From               Message
    ----     ------            ----       ----               -------
    Warning  FailedScheduling  <unknown>  default-scheduler  0/1 nodes are available: 1 Insufficient memory.
    Warning  FailedScheduling  <unknown>  default-scheduler  0/1 nodes are available: 1 Insufficient memory.


Source: [My pod stays pending](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-pod-replication-controller/#my-pod-stays-pending)

### Pod Status shows a RunContainerError

    $ kubectl get pods -w
    NAME                       READY   STATUS              RESTARTS   AGE
    nginx-fast-storage-wknfz   1/1     Running             0          128m
    parallel-kcvxt             0/1     ContainerCreating   0          10s
    parallel-lpttv             0/1     ContainerCreating   0          10s
    parallel-ng5xd             0/1     RunContainerError   0          10s
    parallel-pjwdz             0/1     ContainerCreating   0          10s
    parallel-vnskl             0/1     ContainerCreating   0          10s
    parallel-pjwdz             0/1     RunContainerError   0          11s
    parallel-lpttv             0/1     RunContainerError   0          13s
    parallel-vnskl             0/1     RunContainerError   0          16s
    parallel-kcvxt             0/1     RunContainerError   0          19s

Check the events for any info

You can get the events causing the error:

    kubectl get events --sort-by=.metadata.creationTimestamp

That said the error:

    41m         Normal    Created                pod/parallel-ng5xd   Created container kuard
    41m         Warning   Failed                 pod/parallel-ng5xd   Error: failed to start container "kuard": Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "exec: \"--keygen-enable\": executable file not found in $PATH": unknown

## View DNS Records

    kubectl get pods -n kube-system

## Pod in CrashLoopBackoff shows secrets error in logs

Check pod status

    $ kubectl get po
    NAME                                                   READY   STATUS             RESTARTS   AGE
    dashboard-demo-kubernetes-dashboard-59db4d65dc-dnbx8   0/1     CrashLoopBackOff   6          8m11s

Check the logs:

    kubectl logs dashboard-demo-kubernetes-dashboard-59db4d65dc-dnbx8
    ...
    Storing encryption key in a secret
    panic: secrets is forbidden: User "system:serviceaccount:default:dashboard-demo-kubernetes-dashboard" cannot create resource "secrets" in API group "" in the namespace "kube-system"

**Solution**:

?

