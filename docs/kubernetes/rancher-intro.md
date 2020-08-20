---
author: ''
category: Kubernetes
date: '2020-06-14'
summary: ''
title: Rancher Intro
---
# Rancher Introduction

> Everything Rancher does is free and open source

Rancher sells support to enterprises, all of Cloud Native Foundation is covered.

Challenges that Rancher tries to fix:

* Deploying consistently across different infrastructure
* Implement and manage access control across clusters and namespaces
* Integrating with a central authentication system
* Partitioning clusters to more efficiently use resources
* Managing multi-tenancy, mulitple dedicated and shared clusters
* Make clusters highly available
* Ensure that security policies are enforced
* Monitoring

Kubernetes wants to _maintain flexibiility_ it cannot do certain things like:

* tell you how to authenticate with an identity provider
* tell you how to do backups
* how to do cluster replication

> We want to spend more time using that platform than working on the platform

Abstracted complex stuff away and consolidated things together and included benefits.

Kubernetes is a commodity, I don't care where the electricity comes from as long as the lights turn on.

It is a complete container management platform.

## K3S

[Ketchup k3s](https://github.com/alexellis/k3sup) is a light-weight utility to get from zero to KUBECONFIG on any local or remote VM. Need 512MB RAM to run all of kubernetes.

Using k3s:

1. Create a VM - take note of ip and add ssh key

2. Using the local `k3sup` tool to install kubernetes on the remove

    k3sup install --ip <my-ip> --user <my-user>

3. Copy the `kubeconfig` to a safe place and set the env variable

    export KUBECONFIG=/Users/stephen/kubeconfig/kubeconfig

4. Ensure port 6443 is open and run `kubectl` commands

    kubectl get node -o wide

5. Get pods

    $ kubectl get pods -A
    NAMESPACE     NAME                         READY   STATUS      RESTARTS   AGE
    kube-system   coredns-66f496764-lrzsq      1/1     Running     0          8m8s
    kube-system   helm-install-traefik-hzhmd   0/1     Completed   0          8m7s
    kube-system   svclb-traefik-qgwr9          3/3     Running     0          7m37s
    kube-system   traefik-d869575c8-2xsb7      1/1     Running     0          7m37s

## Kubernetes 101

Building blocks, that can be assembled into an application:

* pods 
* deployments
* services
* config maps
* ingress

> Everything in kubernetes is written in yaml - they are called manifests

### Pods

* Smallest unit that can be deployed in kubernetes
* Consist of one or more containers always scheduled together
* Each pod has a unique ip address
* Containers in a host speak to eachother with localhost

> Pods often have 1 container in it

A single unit of functionality - pods are the things that scale when you need more power

#### Basic Pod Spec

    apiVersion: v1
    kind: Pod
    metadata:
        name: myapp-prod
        labels:
            app: myapp
    spec:
        containers:
        - name: myapp-container
          image: busybox
          command: ['sh', '-c', 'echo Hello Kubernetes! && sleep 10']

The `containers` part is important - you tell it the name, the image to run and the command to override the default.

Creating with `kubectl` you can use:

* `kubectl create`
* `kubectl apply`

    kubectl apply -f pod.yaml

Unless you specifically tell kubernetes that this pod is going to run once then stop (like a bash command), kubernetes expects that it will continue running.

If it stops and kubernetes does not know why it restarts it - kubernetes will then increase to `2s` before restarting then `4s` and continue doubling until `10 mins`. To prevent excess resource usage on the cluster. A `CrashLoopBackoff`.

Delete the pod:

    kubectl delete po/myapp-pod

> You're never going to create pods as there will be something else managing it

### Replica Set

* Defined the desired scale and state of a group of pods
* A replica set will ensure there are a certain number of pods running - so if you lose a node with 4 pods on it - another 4 pods will start on other nodes.
* Kubernetes works with 2 states: actual state and desired state

> Everything you do with kubernetes is telling it the desired state

### Deployments

* You create this
* Deployment creates Replice Set, Replica set creates pods
* Deployment is rolling - you can also roll back

`deployment.yaml`:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
        replicas: 3
        selector:
          matchLabels:
            app: nginx
        template:
          metadata:
            labels:
              app: nginx
          spec:
            containers:
            - name: nginx:1.14-alpine
              ports:
              - containerPort: 80

`metadata`  - Everything in kubernetes has a label, many labels - key-value pairs. They are used with selectors, since pods and versions can change you tell the replicaset and the deployment what it should be managing.

Best practice is to name things that are related with the same name

    kubectl create deploy nginx --image=nginx:1.17-alpine

The better way to do things instead of create yaml by hand

You can view the pod running:

    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    nginx-767868858-5728k   1/1     Running   0          103s

Replica sets:

    $ kubectl get rs
    NAME              DESIRED   CURRENT   READY   AGE
    nginx-767868858   1         1         1       2m55s

deployment:

    $ kubectl get deploy
    NAME    READY   UP-TO-DATE   AVAILABLE   AGE
    nginx   1/1     1            1           3m23s

If we delete that pod, kubernetes will restart it:

    $ kubectl delete po/nginx-767868858-5728k
    pod "nginx-767868858-5728k" deleted

    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    nginx-767868858-gp96g   1/1     Running   0          18s

We can scale our deployments:

    $ kubectl scale deploy/nginx --replicas=3
    deployment.extensions/nginx scaled

Now we have 3 replicas:

    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    nginx-767868858-gp96g   1/1     Running   0          96s
    nginx-767868858-cs9wg   1/1     Running   0          31s
    nginx-767868858-c79th   1/1     Running   0          31s

### Image Update and Rollback Scenario

You can also update the image of a deployment:

**We are deliberately spelling this image wrong**

    kubectl set image deploy/nginx nginx=nginx:1.15-alpne --record

> `--record` means remember the previous state if we need to roll back

You can watch the rollout happen with:

    kubectl rollout status deploy/nginx

> Kubernetes launches new things before stopping old things by default

You cannot view logs for a pod that never launched

When you want to view what kubernetes sees about objects running inside it, use `kubectl describe`

    $ kubectl get pods
    NAME                    READY   STATUS             RESTARTS   AGE
    nginx-767868858-gp96g   1/1     Running            0          10m
    nginx-767868858-cs9wg   1/1     Running            0          9m28s
    nginx-767868858-c79th   1/1     Running            0          9m28s
    nginx-fd7f5f55c-jzqzj   0/1     ImagePullBackOff   0          89s

    kubectl describe po/nginx-fd7f5f55c-jzqzj

Check under `Events`:

    Warning  Failed     42s (x4 over 2m15s)  kubelet, k3sup     Failed to pull image "nginx:1.15-alpne": rpc error: code = Unknown desc = failed to resolve image "docker.io/library/nginx:1.15-alpne": docker.io/library/nginx:1.15-alpne not found

You can undo the deployment with:

    $ kubectl rollout undo deploy/nginx
    deployment.extensions/nginx rolled back

Let's change it a different way:

    kubectl edit deploy/nginx

Once you change it and save, the changes are automatically applied to the cluster.

Check the rollout:

    $ kubectl rollout status deploy/nginx
    deployment "nginx" successfully rolled out

Delete the deployment:

    $ kubectl delete deploy/nginx
    deployment.extensions "nginx" deleted

### Services

* Creates a DNS entry and stable IP address that refers to a group of pods - a layer 4 load balancer
* Types:
    * clusterIP - for communication not exposed
    * nodePort - used with external load balancers
    * loadbalancer

On prem and you want to use the loadbalancer service type you want to use [MetalLB](https://metallb.universe.tf/), an in cluster resource that you give a pool of ip's.
It allocates the ip and arping that ip is on that mac.
**Only works when you can have multiple ip addresses to a single node - not cloud providers**

Also does BGP injection.

    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: nginx
      name: nginx
    spec:
      ports:
      - port: 80
        protocol: TCP
        targetPort: 80
      selector:
        app: nginx
      sessionAffinity: None
      type: ClusterIP

It does it does round robin load balancing you can set session affinity.

    $ kubectl apply -f deployment.yaml
    deployment.apps/nginx created

Expose the service

    kubectl expose deploy/nginx --type=NodePort

View services:

    $ kubectl get services
    NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
    kubernetes   ClusterIP   10.43.0.1     <none>        443/TCP        131m
    nginx        NodePort    10.43.69.11   <none>        80:31612/TCP   33s

Now jsut ensure that port is open on the firewall on the node and go:

    my-ip:31612

you should see an nginx instance

Services are good for non-HTTP protocols as well. MQTT, database etc.

If you are dealing with HTTP exclusively however you might want to look at ingresses...

### Ingresses

* Define how traffic outside the cluster is routed to inside the cluster
* Used to expose kubernetes services to the world
* Route traffic to internal services based on route and path
* Usually implemented by load balancer (Nginx, HAProxy)

You can use Some nodes as Layer 7 load balancer

An Ingress controller is a software based load balancer like Nginx, HAProxy, Kong, GLuu or Istio.

For example you have a microservices architecture and the following go to different places:

* `/products`
* `/store`
* `/profile`

All of that can sit between a single ingress.

The regular clustIP service is listening on port 80:

    $ kubectl get service
    NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
    kubernetes   ClusterIP   10.43.0.1      <none>        443/TCP   161m
    nginx        ClusterIP   10.43.60.248   <none>        80/TCP    19m

More information on [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
      name: single-ingress
      annotations:
        nginx.ingress.kubernetes.io/rewrite-target: /
    spec:
      rules:
      - host: nginx.fixes.co.za
        http:
          paths:
          - path: /
            backend:
              serviceName: nginx
              servicePort: 80

Get Ingresses:

    kubectl get ingress

Now that host `nginx.fixes.co.za` will work as long as dns points to the node and port 80 is open on the host node.

### What do we have

A deployment

    $ kubectl get deploy
    NAME    READY   UP-TO-DATE   AVAILABLE   AGE
    nginx   3/3     3            3           53m

In front of that, a service called nginx

    $ kubectl get service
    NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
    kubernetes   ClusterIP   10.43.0.1      <none>        443/TCP   3h1m
    nginx        ClusterIP   10.43.60.248   <none>        80/TCP    39m

In front of that an ingress

    NAME             HOSTS               ADDRESS        PORTS   AGE
    single-ingress   nginx.fixes.co.za   41.79.79.104   80      6m20s

### Changing the Image

    kubectl set image deploy/nginx nginx=monachus/rancher-demo:pink --record

Check the rollout

    $ kubectl rollout status deploy/nginx
    deployment "nginx" successfully rolled out

It is still called nginx, the name of it has nothing to do with what it is running.

    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    nginx-86774cd58-bst6h   1/1     Running   0          57s
    nginx-86774cd58-7twqf   1/1     Running   0          46s
    nginx-86774cd58-jhgn2   1/1     Running   0          44s

However this container listens on port `8080` not `80` so lets edit the service

    kubectl edit service/nginx

Change the `targetPort` to `8080`

`k3s` runs `trafaek` as its ingress controller by default. The container uses `/ping` to get its updates.
`RTrafaek` intercepts `/ping` to return `OK`.

Switch the image with:

    kubectl set image deploy/nginx nginx=monachus/rancher-demo --record

then scale the deployment:

    kubectl scale deploy/nginx --replicas=7

That is the basics of kubernetes:

* deployments that create pods
* Services and ingresses 

Other things sit on the perifery of that:

* config maps
* secrets
* volumes
* storage

Deployments deal with _stateless_ traffic - like HTTP.

A database is not stateless...they are important...the master is the master.

Things that matter will use a stateful set. There are also daemon sets which will launch 1 copy of the pod on every node on the cluster. For example your ingress controller on every host node.

Then there are jobs and cron jobs.

### Rollout History

You can get the history of deployments with:

    deployment.extensions/nginx 
    REVISION  CHANGE-CAUSE
    1         <none>
    2         kubectl set image deploy/nginx nginx=monachus/rancher-demo:pink --record=true
    3         kubectl set image deploy/nginx nginx=monachus/rancher-demo --record=true

## Rancher

Check out the [Rancher Installation docs](https://rancher.com/docs/rancher/v2.x/en/installation/).

Remember you can't go from a single install to high availability.

Rancher installs by default with self signed certificates

### Security

You can connect Rancher to some backend identity providers.
* Active Directory
* Azure AD
* Github
* Ping (SAML)
* Keycloak (SAML)
* AD FS (SAML)
* Okta (SAML)
* FreeIPA (LDAP)
* OpenLDAP (LDAP)
* Google

> Always have an admin user on Rancher incase auth is down

Full management of Kubernetes role based access control

Kubernetes RBAC is very complicated , rancher makes it easier.

Also have pod security policies (psp) which tell pods whether they can run as root, can they use host based networking and can they run in privileged mode

### Catalogs

The package manager for kubernetes is called helm.
Rather than creating a readme giving steps to deploy an application you can make it available as a chart.

You can add, remove and activate helm repos

You can't have 2 deployments called the same thing in a particular namespace.
You can have a production, staging and development namespace.

You need RBAC per namespace.

## Installing Rancher Single-node

1. Install docker on the server
2. Find the [latest stable release](https://github.com/rancher/rancher/releases)
3. Install it:

    docker run -d --restart=unless-stopped -p 80:80 -p 443:443 -v /opt/rancher:/var/lib/rancher rancher/rancher:v2.3.2

Then add a node locally