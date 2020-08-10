# Rancher Certified Operator

Rancher is a distributed microservices applications that runs in kubernetes.

### Rancher Components

* The company is **Rancher Labs**
* Flagship product is **Rancher**

The core of the rancher product is the rancher server - not the official name.

Rancher acts as the server with kubernetes clusters as its clients - downstream clusters.

* RKE - Rancher Kubernetes Engine - a kubernetes distribution that runs upstream kubernetes entirely in docker containers. A distribution like: PKS (Pivotal Container Service), Red Hat Openshift Container Platform (OKP)

Make installing kubernetes easier - reducing host dependencies - things required on the host before installing kubernetes.

Otherwise you need the kubelet,proxy and networking stuff needed to create a cluster with `kubeadm`.

Rancher only needs `ssh` and `docker`

All this is done with a binary called `rke`

### Rancher Server Components

A.k.a the **Rancher Management Cluster**

* Authentication proxy
* Rancher API Server
* `etcd` datastore
* A Cluster controller per cluster it manages

The `etcd` datastore is the most important part as it can be used to rebuild your server anywhere.

When something is `HA` it is highly available - it doesn't have a single point of failure.

A HA k8s hait has at least 3 nodes running `etcd` components and 2 nodes running control plane components.

When rancher is deployed into an RKE cluster it is a rancher management cluster.

Downstream clusters run a `cluster agent`. A bridge between the cluster controller and the k8s api server in each cluster.

Advanced functionality available in rancher for RKE clusters (outside of kube API) -rancher can do that because it built them:

* certificate rotation
* etcd backup and restore
* automatically healing or replacing failed nodes

### Communicating with Downstream Clusters

Authentication proxy is the gatekeeper:

1. Authenticates user
2. Sets k8s impersonation headers before forwarding the request to the downstream clusters's API server
3. Downstream cluster performs authorization of the request

* Authentication - you are who you say you are - handled by rancher
* Authorization - what you can and can't do - kubernetes is responsible

One cluster controller per cluster rancher manages

Cluster controller in rancher management cluster does:

* watches for resource changes in downstream cluster
* bringing state of downstream cluster to the desired state
* configuring access control policies
* provision clusters - with docker machine drivers - rke, gke or others

cluster controller communicates with the cluster agent.
If cluster agent is not available a node agent is user as fallback

cluster agent handles:

* connecting to the kubernetes API of clusters that rancher launched
* managing workloads - creating pods and deployments
* applying roles and bindings in each clusters security policies
* communicated with rancher server through tunnel to cluster controller

Node agent:

* Runs as a `DaemonSet` one pod per node in cluster
* upgrades kubernetes
* restores etcd snapshots
* if cluster agent is unavailable - node agent can establish tunnel to rancher server

RKE clusters that rancher launches - runs a `kubeapi` auth microservice. THat acts as endpoint for managing that cluster with kubectl.

Authorized cluster endpoints are in the kubeconfig file that rancher generates.

Authorized cluster endpoint:

* Users can communicate with downstream cluster if rancher is down and authentication proxy is unavailable
* Users can communicate with cluster geographically closer to them

Why does this only exist with RKE clusters?

* Imported clusters - `kubectl` config file already exists as the cluster is already built
* Hosted clusters (eks) - generate `kubeconfig` from provider and use that to communicate directly with the cluster

### Architecture Best Practices

**Run a docker deployment of Rancher on its own node** - seperate from kubernetes workloads

Do not run it on the same node of the kubernetes cluster it is managing

**If you are running the kubernetes deployment of Rancher only run it in an RKE cluster and dedicate that cluster to the rancher server process**

Do not run user workloads on it

**If using Rancher for production workloads - run it in an HA RKE cluster**

**Use a layer 4 load balancer in from of a rancher server** - passing TCP through on 80 and 443.

Don't do SSL termination on the load balancer

**Run the rancher cluster close to the downstream clusters it is managing - or central**

Run it on reliable and flexible infrastructure

**Rancher management cluster can start with 3 nodes and add additional workers as it grows - each with etcd, control plane and worker**

**If using Authorized cluster endpoints on down stream clusters - create a layer 4 load balancer in front of the control plane nodes**

**The rancher management cluster needs to grow as you add more downstream clusters**

### Summary

* The Rancher Management Server can only be installed on RKE (Ranchers Kubernetes distribution)
* Rancher can manage any CNCF certifified distribution
* Racher communicates with downstream kubernetes clusters with the kubernetes API
* Minimum number of nodes for a rancher server installation is **1**





















