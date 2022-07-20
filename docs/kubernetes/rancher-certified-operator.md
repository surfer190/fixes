---
author: ''
category: Kubernetes
date: '2020-08-13'
summary: ''
title: Rancher Certified Operator
---
# Rancher Certified Operator

Rancher is a distributed microservices applications that runs in kubernetes.

## 1.1 Learning the Rancher Architecture

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

## 1.2 Discovering RKE

2 Ways to install rancher:

* Standalone way - sandbox environemnts
* Into KA kubernetes cluster (cluster that uses RKE - rnacher kubernetes engine)

RKE: 100% upstream kubernetes certfified by CNCF running entirely in docker containers.

Only thing needed on the host is `docker`.

`kubeadm` requires kubelet and proxy to go onto each host then manually setup networking - before you can stup the cluster with `kubeadm` command.

When adding or removing nodes you need to repeat those steps.

RKE uses `yaml` to define the cluster so after entering the hosts and their roles you just run `rke up` and provision the cluster.

Command can be run from a local workstation.

1. Connects to nodes over SSH
2. Installs kubernetes
3. Connects nodes and returns kubeconfig

Changes are made with the config file:

1. Change config file
2. Run RKE up

### Installing RKE

RKE is a kubernetes distribution and an installer.
It is a binary.

[rke onn github](https://github.com/rancher/rke)

1. Download the binary
2. Change the name
3. Move into your path

### Preparing nodes for kubernetes

Provision whichever way you want:

* manually
* ansible
* terraform
* cloud-init

As a final step install `docker` on them

Preqrequisites:

1. SSH user in the docker group
2. Disable swap on worker nodes (default in cloud environments)

CentOS and red hat linux need a few additional changes for docker.

> If you can, install upstream docker from rancher scripts

It works best on a non-modified version of upstream docker

Traffic from the node you are running `rke` needs to be able to reach port `22` on every kubernetes node and port `6443` on every control plane node - port for k8s api.

SSH Config:

* `AllowTcpForwarding yes`
* Your public key in `authorized_keys` file on nodes

If SSH key has a passphrase:

use `--ssh-agent-auth` 

### Creating the Cluster configuration file

* `cluster.yml`

Minimal config needs just 1 node - single node cluster.

You can start with a single node and move to a 3 node HA cluster by adding 2 or more hosts to the config.

Another way is to run:

    rke config

> You don't want your `Service Cluster IP Range` to overlap with your internal environment

    [+] Cluster Level SSH Private Key Path [~/.ssh/id_rsa]: 
    [+] Number of Hosts [1]: 
    [+] SSH Address of host (1) [none]: 192.168.0.1
    [+] SSH Port of host (1) [22]: 
    [+] SSH Private Key Path of host (192.168.0.1) [none]: 
    [-] You have entered empty SSH key path, trying fetch from SSH key parameter
    [+] SSH Private Key of host (192.168.0.1) [none]: 
    [-] You have entered empty SSH key, defaulting to cluster level SSH key: ~/.ssh/id_rsa
    [+] SSH User of host (192.168.0.1) [ubuntu]: 
    [+] Is host (192.168.0.1) a Control Plane host (y/n)? [y]: y
    [+] Is host (192.168.0.1) a Worker host (y/n)? [n]: y
    [+] Is host (192.168.0.1) an etcd host (y/n)? [n]: y
    [+] Override Hostname of host (192.168.0.1) [none]: 
    [+] Internal IP of host (192.168.0.1) [none]: 
    [+] Docker socket path on host (192.168.0.1) [/var/run/docker.sock]: 
    [+] Network Plugin Type (flannel, calico, weave, canal) [canal]: 
    [+] Authentication Strategy [x509]: 
    [+] Authorization Mode (rbac, none) [rbac]: 
    [+] Kubernetes Docker image [rancher/hyperkube:v1.18.6-rancher1]: 
    [+] Cluster domain [cluster.local]: 
    [+] Service Cluster IP Range [10.43.0.0/16]: 
    [+] Enable PodSecurityPolicy [n]: 
    [+] Cluster Network CIDR [10.42.0.0/16]: 
    [+] Cluster DNS Service IP [10.43.0.10]: 
    [+] Add addon manifest URLs or YAML files [no]: 

This creates the `cluster.yml` file

### Certificate Options

Kubernetes secures communication between nodes with TLS certificates - they do not need to be signed by a root CA.
RKE autogenerates the certificates for you.

You can use a customer certificate directory or have RKE generate certificate signing requests (CSR) to an external CA.

### Deploying Kubernetes

* RKE installed
* config file generated
* Hosts and networking connfigured
* SSH user in docker group
* SSH key in `authorized_keys` file on kubernentes node

    rke up

> whenever a change is made to clsuter config, run `rke up`

### Summary

* RKE deploys Kubernetes components as docker containers
* SSH is used to orchestrate RKE across servers
* To deploy: SSH enabled, SSH user in docker user group, swap is disabled
* `cluster.yml` contains all the info RKE needs for a k8s cluster
* You can supply your own TLS certs
* `rke up` starts the provisioning of kubernetes
* RKE supports _the Latest patch releases from the three most recent minor releases_ by default

## 1.3: Day 2 Operations for RKE

Once provsioned you get 2 files:

* `kube_config_cluster.yml` - kube config file (add to `.kube`) - keep original
* `cluster.rkestate` - certificate and credentials

Critical to backup securely

Regular backups of etcd datastore: very active (every 15 minutes), less active - once a day

RKE defaults to once every 6 hours and keeps them for 1 day

Taking a manual snapshot:

    rke etcd snapshot-save

writes snapshot to: `/opt/rke/etcd-snapshots` on all etcd nodes

Get them off:

* manually moving them
* mounting an NFS volume at that location
* Send them to S3

Can configure RKE to make recurring snapshots automatically:

* In etcd service backup config key
* `interval_hours`
* `retention`

    services:
      etcd:
        backup_config:
          interval_hours: 5
          retention: 8

A container on the host is run called `etcd backup`

> Can use minio

If you use a self signed certficate or unknown CA you will need to add the Cert signing information to the custom CA key in the backup config

#### Restoring a snapshot

    rke etcd snapshot-restore --name <name of snapshot>

Must run from the diretory of the configs

Restoring a cluster is destructive. It will destroy the current cluster.

Always create a snapshot of current cluster state before restore.

### Upgrading Kubernetes

New features - sometimes you need to edit existing resources to change the definition based on the API

Steps to upgrade:

1. upgade `rke` binary on your system
2. View available versions: `rke config --list-version --all`
3. Take a snapshop and move off the cluste host (no automatic way to rollback a backup)
4. Set the version in `cluster.yml`: `kubernetes_version` key
5. Run `rke up`

> Do not set it under `system_images` - remove this key as `rke` will update these images

The versions are the tags of [rancher hypercube](https://hub.docker.com/r/rancher/hyperkube/tags)

Verify version

    kubectl get nodes -o wide

### Cert Management

Rotate certficates for same CA

    rke cert rotate

Can set flags for:

* all certficates
* certs for a specific service
* all certs and the CA

Rotate for a particular service:

    rke cert rotate --service kubelet

Rotate even the CA

    rke cert rotate --rotate-ca

### Adding and Removing Nodes

HA cluster has:

* 2 control plane nodes
* 3 etcd nodes
* as many workers as necessary

All changes happen in `cluster.yml` with roles

> Only make 1 change as a time

Add `control-plane` to a node

Then ensure stability then remove from another node

### Summary

* `cluster.rkestate` and `kube_config_cluster.yml` is generated by `rke up` and must be kept safe
* RKE can write backups to local disk and s3 compatible storage
* Upgrading RKE change `kubernetes_version` in `cluster.yml` and run `rke up`
* RKE manages: etcd snapshots, provisioning k8s components across nodes and upgrades

# 2. Installing and Manaing Rancher

## 2.1: Installing Rancher With Docker

### Install Rancher (Server)

* Single docker conntainer for everything - easy and fast (dev, lab)
* Kubernetes HA cluster

Docker conntainer method is not compatible with the HA method - can't migrate form one to the other

Container startup flags

    docker run -d -p 80:80 -p 443:443 --restart=unless-stopped rancher/rancher:v2.4.0

If `always` you can never stop it to upgrade

4 options for connecting securely to rancher server:

* rancher generates self-signed TLS cert (default)
* bring your own self-signed certs - need private key, full chain certificate and CA cert - columes must be attached for each
* bring your own root CA signed certificates - for public sites (private key and full chain certificate)
* request from letsencrypt where rnahcer server can access internet - DNS server must point to rancher ip

To do the letsencrypt option use: `--acme-domain ranncher.mydomain.com`

* API autologin
* custom CA certs
* Air gapped installs

> Uses http-01 challenges

Bind mounting a volume fot persistent data - rancher stores persistent data in the container at `/var/lib/rancher`

By default a docker volume is mounted at that location

You can bind mount a directory from the host at this location:

    -v /opt/ranncher:/var/lib/rancher

Backups and restores a way easier with the bind mount

### Making Backups: Rancher Server

Back up the persistent data at `/var/lib/rancher`

Identify the backup with date and rancher version, eg: `rancher-data-backup-v2.3.5-2020-03-15.tar.gz`

Backup (non-bind mount)

1. Stop the rancher container
2. Create a data container that uses the same volume
3. Backup with a temp container (tarball or `/var/lib/ranncher`)
4. Start rancher
5. Move backup off the host

Maintain file and directory permissions with `-p`

Backup (bind mount)

1. Stop rancher
2. Tar the local directory
3. Start rancher
4. Move back off the host

Can also make a copy of the entire `/var/lib/rancher` directory and restart container

### Restoring From a Backup

Overwrite contents of `/var/lib/rancher` with the contents of that tarball

1. Move tarball onto rancher server in `/opt/backup`
2. Stop rancher
3. Make a fresh backup of rancher
4. Run a temporary container that uses volumes from ranhcer container - extract info into it
5. Start rancher

When it restarts it will use the contents of the backup

Restoring with bindmount

1. Move tarball backup into `/opt`
2. stop ranncher
3. Move `/opt/rancher` to `/opt/rancher.bak`
4. Extract the tarball
5. Start rancher

### Upgrading Rancher

Docker volume

1. Stop rancher
2. Create data container
3. Backup `/var/lib/rancher` into tarball
4. Pull a new container iamge
5. Start a new container (with `volumes-from`)
6. Verify upgrade
7. Delete the stopped rancher container

Bound volume

1. Stop rancher container
2. Create tarball from `/var/lib/rancher`
3. Pull new container image
4. Start a new container (with same cert and bind mount to `/var/lib/rancher`)
5. Verify the upgrade
6. Delete the stopped rancher container

### Summary

* Docker method for installing Rancher is for sandbox and demo purposes
* First step in backing up an install is stopping the container
* Upgrading Rancher server is similar to making a backup but with a new image tag
* delete the old Rancher container after an upgrade - so it doesn't accidentally start and overwrite the /var/lib/rancher folder

### 2.2: Installing Rancher server with Kubernetes

Rancher server is an application that runs inside kubernetes.
Used for production.
Access RKE cluster with single url - ingress controller will listen on all nodes in the cluster

Rancher server can only be deployed into an RKE cluster - may not work correctly or be eligible for support

> Best to choose a hostname and keep it for the life of the environment. Eg. `rancher.mycloud.co.za`

load balancer type:

* hardware
* cloud (elb or nlb)
* software load balancer (nginx or HAproxy)

> Only run it at layer 4 - passing traffic on 80 and 443 - do not configure at layer 7.

You can terminate TLS on the layer 4 and connect with rancher unencrypted - but it is **not recommended**

The load balancer you create will be dedicated to the ranhcer server clsuter - appearing inside rancher as the local cluster.
Workloads other than rancher should not be run on the local cluster - downstream clusters need their own load balancer.

Configure rancher server hostname to point to address/hostname of load balancer.

[MetalLB load ba;ancer service on the cluster](https://metallb.universe.tf/) sits in front of ingress.

Rancher is installed with helm - the package manager for kubernetes.

All of these steps run on the same place you ran `rke up` and where you have the config file for kubectl.

Check you are on the right cluster:

    kubectl get nodes

* `latest` are for new features - not recommended for production
* `stable` is for production
* `alpha`

Add helm repo

    helm repo add rancher-stable

Create namespace before installing the helm chart:

    kubectl create namespace cattle-system

SSL Cert options:
* rancher self-signed certificates (default)
* real certificates from letsencrypt
* provide your own certs

First 2 require kubernetes package `cert-manager` = handling cert management and renewal from external sources.

`cert-manager` is under active development by a company called jetstack - instructions will always be from their documentation.

Default install uses self-signed certs:

    helm install rancher rancher-stable/rancher --version v2.4.5 --set hostname=rancher.mycloud.co.za --namespace cattle-system

Check status

    kubectl rollout status deployment -n cattle-system rancher

For a letencrypt installation:

* `set ingress.tls.source=letsEncrypt`
* `set letsEncrypt.email=you@mycloud.co.za`

Using your own certificates

1. Load private key and certificates into kubernetes secret
2. Tell kubernetes to use that

* `set ingress.tls.source=secret`
* `set privateCA=true`

Create `tls.crt` with the certficate
Create `tls.key` with the private key

Create a tls type secret from those files: `tls-rancher-ingress`

For PKI (Public key infrastructure)

    kubectl create secret -n cattle-system tls tls-rancher-ingress --cert=server.crt --key=server.key

With a private CA:

* create `cacerts.pem` with CA info
* create a secret called `tls-ca` from this file
* Type `generic`

    kubectl create secret -n cattle-system generic tls-ca --from-file=cacerts.pem=./ca.crt

### Making Backups

When you install rancher server into an RKE cluster - it uses the `etcd` datastore to hold its configuration.

If you backup the RKE cluster - you are also backing up rancher.

Use the same method.

### Restoring from a Backup

Changes the normal RKE restore 

3 node HA RKE cluster

1. Shut down the old cluster - all down stream clusters disconnect
2. Those clusters will continue to function but users conencting through rancher server to the clusters won't be able to do so until restored
3. Prepare 3 new nodes - choose 1 as the intial target node
4. Make backup copy of rke files for original cluster (restore genenrates new state files)
5. Edit `cluster.yml` - comment out `addons` section, change `nodes` to point to the new nodes and comment out all but the `target` node

Restore the database (local)

1. Place the snapshot into `/opt/rke/etcd-snapshots`
2. Restore with `rke etcd snapshot-restore --name <etcd-snapshot-name>`

Once etcd is restored on the target node bring up the cluster with `rke up`

rke will write a credentials file to the local dir, use `kubectl` to check status

1. When the target node is `ready`, remove the old nodes with `kubectl delete node`
2. Reboot the target node
3. wait till all pods in `kube-system`, `ingress-nginx` and `rancher` pod in `cattle-system` are running
4. `cattle-cluster-agent` and `cattle-node-agent` will be in error or crashloopbackup until it is up

#### Add New Nodes

1. Edit `cluster.yml` and uncomment the additional nodes
2. Run `rke up`
3. ensure they are ready in status of `kubectl get nodes`

#### Finishing Up

1. Securely store the new cluster config and state files
2. Delete the archived config files
3. Delete or cleann the old cluster nodes

### Upgrading Rancher

Rancher is packaged with Helm

1. Make a one time snapshot 
2. Update the helm repo
3. Fetch the most recent chart version from the repo
4. Retrieve the values in the original installation
5. Use `helm upgrade` with namespace and those values
6. Verify upgrade - check ui bottom left

    helm repo update
    helm list --all-namespaces -f ranncher -o yaml

Get the namespace and values passed in

    helm get values -n cattle-system rancher -o yaml > values.yaml
    helm upgrade rancher rancher-stable/rancher --version v2.4.0 --namespace cattle-system --values values.yaml

Check  deployment

    kubectl rollout status deployment -n cattle-system rancher

Check bottom left - upgraded version

> If it fails - restore from the snapshot taken before the upgrade

### Summary 

* A TCP-based load balancer is a valid loadbalancer for rancher
* It is **not** possible to migrate from rancher alpha to latest or stable
* Types of TLS certs you can use with rancher: self-signed, certs from external CA or Letsencrypt
* You make a backup of Rancher in RKE - by making a normal RKE backup (Since ranhcer is the only thing that RKE cluster is for)
* A rancher Server RKE backup will have downtime when being restored
* You cannot rollback a failed upgrade with `helm rollback` - because of ranhcer's integration with etcd the only way to rollback is with a restore

# 3. Designing and Provisioning Clusters

## 3.1: Where will my cluster live?

Types:

* Hosted provider (EKS, AKS, GKE) - support for this is very good
* Infrastructure provider then you have to deploy kubernetes into it
    - ranhcer deploys systems
    - ranhcer deploys kubernetes
    - full liecycle management
* Provisioning / connfig management - use custom drver to build nodes into kubernetes cluster
    - only `docker` is needed for rke
    - add docker run command at end of provisioner
* Existing clusters can be imported (or k3s)
    - rancher gives you a `kubectl` apply command

> Anything that can be done through kubernetes can be done on all cluster types

Rancher's access to dataplane or infrastructure layer defines the scope of benefits it provides.
..

Rancher cannot backup or restore hosted clusters because it has no access to the dataplane or control plane

> Imported clusters are the most opaque to rancher

Imported clusters do not include lifecycle management or integrated backup/restore.

Need to use the providers tools

### Size requirements

Control plane, data plane and worker roles reside on different node pools

If things are inconsistent just add more hardware and see if the problems go away

Always deploy with CPU reservations and limits - prevennt processes taking over resources causing other applications to fail

### Networking and Port Requirements

Don't lock down too early

Test that pods on one host can communicate with pods on another host

### Cluster Roles

* When you create a cluster - rancher sets you as the cluster owner
* Cluster owners have full control over the entire cluster
* cluster members - view most cluster level resources, create new projects
* custom

Go to cluster and `Add member`

### Summary

* etcd backup/restore and some monitoring of etcd is not available on hosted clusters (EKS, AKS)
* Node templates describe how to provision nodes and RKE templates how to deploy Kubernetes

## 3.2 Deploying a Kubernetes Cluster

### RKE Configuration Options

* Choose the version to install (RKE supports the last 2 minor versions)
* Choose network provider (flannel, calico, Canal)
* Enable windows work support

> Canal network provider allows project network isolation - namespaces in different projects will not be able to access each other over the network (multitenancy)

### RKE Templates

RKE templates launch clusters with same kubernetes configuration - can allow new clusters to customize certain options

On the cluster -> click `...` -> Save as RKE template

To edit the template you need to create a new revision name.

Once the template is updates the clusters using it will show a notification to update.

### Node Templates and Cloud Credentials

Node templates - make it easier to reuse existing configuration for each node

Cloud credentials - define how you communicate with a cloud provider
For different providers or regions

1. Create cloud credentials for infrastructure API
2. Once created it can be used in a node template to configure the kinds of nodes rancher can provision

Create a cluster using the node driver matching the template provider - you can use the existing template.

### Cloud Providers

Infrastrucutre and cusotm clusters allow you to set a cloud provider.
This changes how the deployment happens - based on the cloud provider.


### Deploying a cluster

Hosted kubernetes (Amazon) - AWS will run the control plane so you will only see worker nodes when inspecting nodes.

Nodes in an infrastrucutre provider utilise node templates and can also use RKE templates.

A node driver is needed.

Cloud credential and node template is needed for the target environment.

Rancher creates the master nodes -to bootstrap the datastore and api server. Workers are added after bootstrapping.

Custom cluster is used when provisioning by any other means - ansible etc.Including bare metal.
Rancher does not control nodes in this situation
* You need a docker command to run on the nodes to add to the cluster
* Better to use `cloud-init` or `ansible`

Host should have a supported version of docker installed.

Rancher supports kubernetes on windows

Rancher deploying a windows cluster expects that you will be using windows workloads by default

A linux control plane needs to be deployed - required by kubernetes. A linux node is also needed for the ingress controller as that is a linux only function

kubernetes on windows works with the flannel CNI

Windows can only be done with the custom clusters technique

> Remember etcd and control plane nodes must run on linux

Import an existing cluster with `kubectl apply` command:

will install agents allowing rancher to control it

* rancher isntallation real certificates from a root CA
* rancher installation from an unknown CA - kubectl wont connect to this endpoint - so need to pull the manifest with `curl` and pipe to `kubectl`

### Summary

* RKE templates specify the Kubernetes configuration options that should be used
* Node Templates allow you to deploy new nodes without having to re-enter the node parameters
* Rancher cloud provider - allows Kubernetes to leverage cloud-specific features such as load balancers and network storage
* Imported clusters **do not** have a special import flag that enables you to manage the nodes from within Rancher.
* Only **flannel** network provider works with Windows clusters

## 3.3 Basic Troubleshooting

### Ranchers API Server

Look at the logs in the pods of the `cattle-system` namespace with the label `app=rancher`

If no logs are returned ennsure they are running

First port of call is the rancher API server

    kubectl get pods -n cattle-system -l app=rancher -o wide

Inspect lgos

    kubectl logs -n cattle-system -l app=rancher

### Docker/Container Runtime

Why it can't pull an image or start a container...

Docker engine could be experiencing issues

container runtime:

* docker
* containerd
* cr-o

On the host or log file in syslog

    systemctl status docker

Check journald:

    journalctl -u docker.service

### Node Conditions

The `kubelet` maintains a set of sensors about the state of every node - if any is triggered - a node give a node condition.

    kubectl describe node <name>

Will say:

* DiskPression
* PIDPressure
* MemoryPressure
...

These commands:

    kubectl get nodes -o go-template='{{range .items}}{{$node := .}}{{range .status.conditions}}{{if ne .type "Ready"}}{{if eq .status "True"}}{{$node.metadata.name}}{{": "}}{{.type}}{{":"}}{{.status}}{{"\n"}}{{end}}{{else}}{{if ne .status "True"}}{{$node.metadata.name}}{{": "}}{{.type}}{{": "}}{{.status}}{{"\n"}}{{end}}{{end}}{{end}}{{end}}'

and

    kubectl get nodes -o go-template='{{range .items}}{{$node := .}}{{range .status.conditions}}{{$node.metadata.name}}{{": "}}{{.type}}{{":"}}{{.status}}{{"\n"}}{{end}}{{end}}'
    
Taken from [rancher troubleshooting](https://rancher.com/docs/rancher/v2.x/en/troubleshooting/kubernetes-resources/#get-node-conditions)

### Kubelet worker node

kubelet is responsible for invoking containers on the node

If infra issues onn node - kubelet pod might show it in the logs

    docker ps -a -f=name=kubelet

> Make sure both containers (kubelet and proxy) are running

* no kubelet: API changes wont reflect on the worker 
* no proxy: pods on worker may experience network issues

    docker logs kubelet
    docker logs kube-proxy

### Summary

* Check the logs on rancher API service - using Kubectl with the logs subcommand for one of the pods in the `cattle-system` namespace
* Find details on node sensors: `kubectl describe node < node name > `
* Infrastructure issues on a particular node are often revealed by the kubelet logs.
True correct 
* Docker daemon logs are useful for understanding if an image cannot be pulled for some reason

### ETCD

Stores state of kubernetes and rancher application

* Is `etcd` constantly electing new leaders - something causing leaders to fail?
* Are all etcd nodes of the same cluster? Might be trying to reconnect with different clsuter id's
* Are there any active alarms that prevent receiving write data.

> Must inspect logs directly as this component is insntalled via rke with docker

`etcd` runs as a container - check logs with `docker logs`

1. SSH into node
2. `docker logs etcd`
3. `docker exec etcd etcdctl alarm list`

Disk latency being slow means etcd will fall behind peer - if peer see that as unresponsive it might be ejeted from the cluster

Ensure etcd nodes have enough IO performance

### Control plane

Where cluster wide PAI and logic engines run

First look at the logs

Need to determine the leader - the one handling the requests

    kubectl get endpoints -n kube-system kube-controller-manager -o jsonnpath='{.metadatamannotatons.control-plane\.alpha\.kubernetes.\io/leader}{"\n"}'

    docker logs kube-controller-manager

Get scheduler leader

    kubectl get endpoints -n kube-system kube-scheduler -o jsonnpath='{.metadatamannotatons.control-plane\.alpha\.kubernetes.\io/leader}{"\n"}'

    docker logs kube-scheduler

Use `tmux` and sync them to get logs of all nodes at once

### Nginx-Proxy

Non-control plane nodes can reach the services in the control plane without knowing what node they are on

    docker ps -a -f=name=nginx-proxy

    # Make sure pointing to all control plane nodes
    docker exec nginx-proxy cat /etc/nginx/nginx.conf

    docker logs nginx-proxy

### Container Network / CNI

Validate the transport layer between all hosts is working correctly

If any firewalls or proxies are blocking the connnections the CNI will fail

Deploy a daemonset on all nodes on a cluster and use the pods to run a `ping` test across the network fabric

    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: overlaytest
    spec:
        selector:
        matchLabels:
            name: overlaytest
        template:
        metadata:
            labels:
            name: overlaytest
            spec:
            tolerations:
            - operator: Exists
            containers:
            - image: busybox:1.28
                imagePullPolicy: Always
                name: busybox
                command: ["sh", "-c", "tail -f /dev/null"]
                terminationMessagePath: /dev/termination-log

Apply

    kubectl create -f ds-overlay-test.yml

Check status

    kubectl rollout status ds/overlaytest

Check status:

    echo "=> Start network overlay test"; kubectl get pods -l name=overlaytest -o jsonpath='{range .items[*]}{@.metadata.name}{" "}{@.spec.nodeName}{"\n"}{end}' | while read spod shost; do kubectl get pods -l name=overlaytest -o jsonpath='{range .items[*]}{@.status.podIP}{" "}{@.spec.nodeName}{"\n"}{end}' | while read tip thost; do kubectl --request-timeout='10s' exec $spod --/bin/sh -c "ping -c2 $tip > /dev/null 2>&1"; RC=$?; if [ $RC -ne 0 ]; then echo $shost cannot reach $thost; fi; done; done; echo "=> End network overlay test"

### Summary

* logs for etcd in an RKE cluster are fonud with docker
* Control plane nodes only have one active controller manager so log data may not be present equally across nodes
* the point of `nginx-proxy` is so non-control plane nodes can reach control plane components without knowing node addresses 
* Rancher API server logs is best place to start troubleshooting
* Common reason for CNi failure: Network port restrictions between nodes correct 

# 4. Editing Clusters

## 4.1 Editing Cluster Options

You can't change the network provider (CNI) after provisioning

Adding workers and removing the `worker` role from existing nodes:

    kubectl drain <node name> --ingore-daemonsets=true

### Upgrading Kubernetes

Patch versions are available independent of rancher server upgrades

> Can be done live - zero downtime

1. First take a snapshot
2. Edit page of cluster -> Change kubernetes version and save
3. Need workloads to be HA

* When you update the version of a Kubernetes cluster, it immediately starts updating the worker, control plane, and etcd nodes with new components

## 4.2: Using the CLI Tools

`kubectl` interacts with the kubernetes APi using the kubernetes API endpoint

Same on rancher - ui changes are done to ranchers API endpoints

Every UI action can be donne with rancher CLI or HTTP

Defacto way of interacting wiht kubernetes is `kubectl`

Rancher acts as an authnetication proxy - handing off communication to downstream kubernetes cluster.

Each cluster in rancher has its own kubectl config file

Start in default namespace and context, to change:

    kubectl config set-context --current --namepsace academy

Can also get the `kubeconfig` file for your user

### Rancher CLI

Everything you can do with kubernetes - you can do with rancher

For things outside of kubernetes - the `rancher cli` is used

Can download the cli in the bottom right of the rancher UI

Rancher CLI uses Bearer Tokens - derived from an API key.
Can be scoped to a specific cluster - directly onn authorization endpoint.
Can have expiration date.

Ket information is only shown once

Account profile from UI

Give a description for the key - what it is used for

    rancher login <endpoint> --token name:key

Cluster and project = context.

Most commands are run against a project - need to switch to that project / context

    rancher context switch

Help with:

    rancher <item> --help

Install:

    rancher app install --set persistentVolume.enabled=false --set env.email=my-email@mycloud.co.za pgadmin4 pgadmin4

    rancher app ls

> Rancher apps and helm are not compatible

rancher CLI you get an SSH proxy to your cluster nodes - works with RKE clusters launched with an infrastructure provider cause rnacher has ssh keys

    rancher ssh

    rancher nodes

YOu can also use:

    rancher kubectl ...

so you don't need to pull down the kubectl config file - as rancher is a proxy to the downstream clusters

### Summary

* `kubectl` makes comamnds to the Kubernetes API of the cluster you are working with
* Rancher acts as an authentication proxy
* View active API keys: Click on your user profile icon in the top right and select "API & Keys"

Use Rancher CLI instead of kubectl:

* To not have to manage multiple kubectl config files
* For access to Rancher-specific functions of Kubernetes
* To create projects and move namespaces into them

## 4.3: Interacting With Monitoring and Logging

Enable advanced moniotring from the dashboard

Prometheus and grafana are enabled

Prometheus configuration:

* data retention period
* persistent storage - data exist beyond the life of the pod
* node exporter - monitor host
* selectors / tolerations - where monitoring workloads are deployed

Project monitoring needs clustering monitoring enabled

Project monitoring -> `tools` -> `monitoring`

### Use the Grafana Dashboards

Click grafana icon

Cluster level grafana and prometheus resource

To access proetheus and grafana directly - go to the `index.html` links on the apps page

### Configure Notifiers

Services that notify oyu of alert events

* slack
* email
* pagerduty
* webhook
* wechat

Target for notified should be in a different cluster from sender

    Cluster -> tools -> notifier

### Configure Alerts

Need to attach a notified to defualt alerts

Alert timing:

* Group wait time - buffers alerts from the same group - before sending the first alert
* Group interval time - delay for new alerts from group
* Repeat interval time - how long to wait before sending any alert that whas already been sent

Cluster alert types:

* system - controller manager, etcd, scheduler
* resource events - kubernetes
* node events - unresponsive nodes
* node selector events
* metric expression

Edit alert and configure the notifier at the bottom

Project alert types:

* Pod alerts - a specific pod
* Workload alerts - All pods in a workload
* Workload selector alerts
* metric expression alerts - special PROMQL expressions

Imported and hosted clusters dont provide access to `etcd` - so rancher cannot monitor the data plane

### Configure Logging

Available at cluster and project level

`stderr` and `stdout` and `/var/log/containers`

Can write logs to:

* elasticsearch
* splunk
* fluentd
* kafka
* syslog

### Summary

* Enabling Advanced Monitoring deploys Prometheus and Grafana
* Clusters that are built using RKE permit alerts for etcd

# 4. Managing Kubernetes with Rancher

## 4.1 Configuring Namespaces

Namespace - logical seperation of resources, helps keep organised, "virtual clusters"

### Projects as namespace groups

Rancher uses "projects" to group namespaces and rbac config.
Simplifies management.

Resources assigned to a project are visible to all namespaces within a project

Some resources can be assinged:

* ConfigMaps
* Secrets
* Certificates
* Registry Credentials

Resources that can only be assigned to a namespace within the project:

* workloads
* load balancers
* services
* PVC's
* Service Discovery records 

Rancher creates 2 default proejcts:

* Default - User workloads
* system projects - important not to be deleted

    kubectl create namespace mytest

Must be added to a project with rancher UI or CLI

### Project Security

Users having access to a project have access to all resources

* Onwer - full access
* member - control over resources - not project
* read only - view but cannot change
* custom

Users or user groups can come from the Single sign on provider

Recommended that PSP's (Pod Security Policies) are only assigned to clusters

Only apply to pods after PSP is applied - existing pods need to be redeployed.

### Resource Quotas

Total amount of particular resource a project can use

stops project from monopolising resources

Project limit and default limit...

Total CPu and memory to project

### Resource Limits

Project can define a default limit - workloads will inherit this default.
Existing namespaces with need to be adjusted.

> Do it first

Make sure no single workload can spin out of control

Many users forget to set these limits

Do not set it too low - cluster will be regualrly be restarting workloads

### Summary 

* A Project can have more than one namespace.
* Canal CNI supports project level isolation
* Resources in different namespaces in the same Project **can** use the same name
* Resource quota - controls the amount of resources a Project can use 
* Set resource limit - To set a limit on workloads that don’t set one in their configuration

## 4.5: Working Inside a Project

Can move a namespace to a different project - new project resource config is applied

Remove resource limit from project

### Project Monitoring

Available on a project by project basis

deploys prometheus and grafana into the project

cluster and project must have enough resources

### Project Alerts

Send alerts for workloads inn project

### Project Logging

works same as logging at cluster level

### Summary

* Namespaces cannot move to a Project with resource quotas 
* You can use Rancher Advanced Monitoring to scrape metrics from your workloads.
* notifiers are configured at the cluster level
* PromQL is used for direct queries to prometheus

# 5. Running Kubernetes Workloads

## 5.1: Deploying and managing Workloads

Top down approach

Deployment type:

* Deployment
* DaemonSet
* StatefulSet
* Job
* CronJob

Image: full path to image

* Always specify an image tag that isn't `latest`
* If it is `latest` kubernetes sets the ImagePullpolicy to `Always`
    * Kubernetes will always pull a new image when it starts (even if iamge already exists onn the node)
    * Kubernetes doesn't know if there is a newer version
    * If image is on an externnal registry that is not available - pod won't start
    * If pod restarts - new versionn will be pulled - pods cann be running different versions

If tag is set the `ImagePullPolicy` becomes `IfNotPresent`

Ports of a workload are automatically deployed as a service - except with resources deployed with `kubectl` or with `yaml` import - containerPorts won't

Enter environment variables driectly or from another source

When using a field or resource - you are using the downward API

Node scheduling can choose a nnode matching the rules - if no node exists with those labels - it will choose any.

Ensuring workload is on specific nodes

Taint / Tolerations - taint a node

For example GPU on node

Edit deployment and add taint tolerance for noGPU

Ease to find and attach volumes to your workloads:

* bind volume from node
* ephemeral
* PVC
* Secret
* configMap as volume

Command control:

* entry point
* change working directory
* set user and group

Networking options:

* set hostname / domain
* Configure host entries
* Override DNS config
* use host networking

Security/Host config:

* How is image pulled
* Use privileged mode
* run as root
* privilege escalation
* CPU and RAM limits
* GPU reservation
* Add and remove capabilities

Cluster scope:

* Creates non existing namespaces
* Namespace not added to project
* Import non-scoped resources

Project scope;

* Namespace added to current proejct

Namespace scope:

* All resources into namespace, if it specifies a different namespace it will fail

> Import YAML

Add sidecar into pod: swissarmyknife - shell into sidecar

### Upgrading Workloads

You can upgrade the workload by directly editing the yaml image or other parameters.
Or click the edit going through the form changing values.

Scaling, upgrade policy or number of replicas does not result in a redeployment of the workload.

Click `..` and `edit` or `view/edit yaml`

Making changes directly to the specs / manifests

Can also edit yaml outside of rancher and apply with `kubectl`

### Rolling Back Workloads

All edits on rancher are equivalent to `kubectl --record=true`

You can rollback to prior workloads

Click `..` and `rollback`

You will see the diff

### Summary

* Kubelet node alarms, Node taints, Pod Anti-affinity rules would prevent a workload being scheduled on a node
* You can deploy a workload by importing YAML through the Rancher UI.
* Rancher will create services for ports that you configure in the Workload deployment screen.
* Changing the console type **can** effect on Rancher’s ability to collect log data from stdout/stderr.
* To launch a Pod with multiple containers in rancher - Launch the pod with the primary container and then add sidecars 


Never use the `latest` tag:

* It can increase the time to deploy new Pods 
* It can result in inconsistent container application versions 
* It can cause service interruptions if the registry is down 

Rancher can pull environment variables from:

* ConfigMaps 
* Secrets 
* Key/value pairs in the workload deployment screen 

health check method for Workloads:

* HTTP/HTTPS 
* TCP
* Command run inside of the container 

## 5.2: Using Persistent Storage

### Provisioning Storage

Persistent storage is needed for applications that retain data

Kubernetes delivers this with Persistent Volumes (PV's), Persistent Volume Claims (PVC's) and Storage Classes.

Storage can be provisioned statically or dynamically.

If you have provisioned storage - simply create a persistent volume that points to it.
A PV does not provision the storage for you it just creates an object in the cluster pointing to existing storage.

You need to add the PV to a PVC (Persistent volume claim) to add it to a workload.

Edit the workload and add the PVC -> mount it to a specific path.

Storage classes are about removing bottlenecks - instead of waiting for someone to provision storage and make it available for your workload.
You can request storage dynacally from the cluster when your workload launches.

Cluster admins configure the storage classes with the info of where to acquire storage - the storage class does the provisioning for you and connects your workload to the storage.

* VMware vsphere volumes
* cloud provider volumes
* rancher longhorn
* custom

You can also add storage classes from the app catalog

rancher partners have apps that connect your cluster to storage solutions:

* HPE
* OpenEBS
* Portworx
* StorageOS
* NFS volume

### Using Storage

volumes are attached to workloads when they are launched

A workload can create a new persistent volume claim that points to an existing PV or requests a new PV according to a storage class

Once the workload has been created the PV is mounted in the pod

Add a storage class

### Summary

* Common cloud providers have their storage providers built into Rancher/Kubernetes
* Dynamic Provisioning - allows Kubernetes to allocate storage as users request it
* Storage classes are configured on the Cluster level
* You can have multiple StorageClasses but only 1 default

How can you attach storage to a workload:

* Create a PV and PVC and then use it with the workload 
* Create a PV and create a PVC when launching the workload 
* Create a PVC that references a StorageClass when launching the workload 

## 5.3: Dynamic Data with ConfigMaps, Secrets and Certificates

Applications have dependencies on small bits of code we want to use across pods in our environment.
Some are more sensitive.

### ConfigMaps

A set of key value pairs that kubernetes stores.

Configmaps can onnly be assigned to a namespace - not a project.

### Secrets

Store sensitive key value pairs

Base64 encoded - providing a minimal amount of security

> kubernetes does not encrypt secrets by default

Secrets can be assigned to a namespace or a project

### Certificates

The backbone of secure communication on the internet

Kubernetes secures internal communication with TLS certificates

You can also upload certificates to be used to secure ingress traffic (traffic coming in from outside the cluster)

You can then use it with the inngress congiuration for inbound traffic

Adding them automatically with vault is encouraged but they can be done manually.

> A chain of certs can be inncluded in the public key area

`cert-manager` is a conntroller from jetstack that runs in the cluster and dynamically generates certificates on demand from: internal CA, internal vault service or letsencrypt

You can request cert-manager create a cert when you create the ingress - or cert resources that request from a specific issuer.

### Registry Credentials

Docker registry is a private registry that holds docker container images.

Workloads use the kubernetes registry to access the docker registry

kubernetes registry secret is automatically included if from ui.

if you use `kubectl` you need to specify the `imagePullSecret` in the container spec.

### Resource Naming

Kubernetes treats secrets, certficates and registry credentials as secrets.

They must be unique in the namespace and cluster.

### Summary

* `ConfigMaps` are stored in the Kubernetes datastore 
* You can store text files in ConfigMaps
* Rancher Hardening Guide has more info on how to configure additional security for Secrets

## 5.4: Understanding Service Discovery and Load Balancing

### Services in Rancher

Pods are ephemeral

No gaurentee a pod will be at that ip - nodes can fail

Kuberneters solves this with a service - a stable ip and DNS to a group of pods.

Services are automatically created for workloads exposing a port

Type of service:

* cluster IP
* Nodeport
* Loadbalancer

External name service - points to specific ip or hostname (CNAME or A)
alias service - acts like an internal CNAME to another DNS name in the cluster - handy for AB deployments


external name service allows you to use a local service that points to an external service (like a database) - what are the advantages of this?

### Layer 4 vs Layer 7

Load balancing in kubernetes:

* layer 4 with load balancer services
* layer 7 with ingress

OSI network manager

layer 4 receives traffic ona port and sends to backend on another port - does not look at traffic no decisions are made - great for encrypted and non-HTTP TCP traffic

layer 7 - receives traffic on a port, inspects it and directs it based on rules. Intelligent load balancers.

Ingresses are served by the ingress controller which is a layer 7 load balancer.

### Load Balancer Service

In cloud providers, kubernetes deploys an instance of the cloud providers load balancer and configures it to route traffic to the cluster.

vSphere

On premise - configure MetalLB

### Ingress

Ingress controller installed by default is the nginx ingress controller.

You can install anotehr controller like traefik or HAproxy - it works fine.

Rancher can generate an xip.io hostname which is useful for development or demo

worker nodes in AWS don't know their external address - so tell kubernetes the internal and external address of the nodes

    rke.cattle.io.externalip
    rke.cattle.io.inernalip

You can set a default backend where traffic arriving doesnt have a destination - you can have a cuastom backend for customers.

When creating an ingress - you can direct it to a service entry or directly to the workload.

The later works for workloads that don't expose ports with a service entry
Rancher labels the workload and creates a service that uses the label as the selector.

Future versions of rancher will only use services - so recommended to expose your workload with service entries.

If you have installed cert manager you can annotate your ingress to request a certificate from the issuer when you deploy the ingress - not integrated into th eui needs YAML direct edit.

    kubectl get ingress 
    
    kubectl get ingress -o yaml

You can add additional targets of an ingress based on the `/path`

It also good for `www.domain.com` and `domain.com`

By default an ingress controller runs as a `DaemonSet` and listens on every node in the cluster.

Can also be configured as a deployment to work on selected nodes in the cluster.

You need a dumb level 4 load balancer sending traffic for port 780 and 443 directly to the worker nodes.
The will be no `X-forarded-for` http header

### Summary

* The `ClusterIP` for a Service does not change when the Workload is upgraded
* You configure a kubernetes ingress to terminate SSL by uploading your certs as a Certificate and configuring the Ingress with a reference to that Certificate 
* `ExternalName` mimics a `A` record or `CNAME` record
* For loadbalancer services to provision - A Cloud provider configuration is needed

Ingress:

* Is generally used for HTTP/HTTPS traffic 
* It can be powered by a number of popular open source load balancers 
* You can only have one Ingress per cluster 

## 5.5: Discovering the Rancher Application Catalog

### How it Works

Rancher application catalog integrates helm and rancher apps

When an app is requested an ephemeral helm service is created - preventing a user getting higher privileges.

After a helm repo - known as a catalog - is added to rancher the apps are available to install

### Catalog Scope

Catalogs are scoped at the global, cluster and project levels.

### Included Global Catalogs

* 3 default catalogs only 1 is active by default
* `library` is a curated list of apps that rancher provides catalog entries
* apps themselves are not supported by rancher
* `helm-stable` and `helm-incubator` - global admins can activate these

### Adding Custom Catalogs

Can be a git repo or helm repository

Add the catalog url or the helm repo

### Using Catalog Apps

* Helm app: view insntrucitons and manually enter key value pairs
* Rancher app: form with same defaults

A rancher app has a more comprehensive interface

Rancher docs on how to build your own rancher app

Same application can run in its own namespace - adding 5 characters to the default name

You can clone an application - copying the keys and values

When you delete a catalog app - the namespace is not deleted.
Must be done manually.

Always delete from the app page first.

### Summary

* The page of installed apps will show that the app has an upgrade available when there is a new helm chart available
* Helm apps are installed through a Rancher service account - administrator privileges are not required.
* Helm charts require you to enter key/value pairs for answers and Rancher apps use a form to configure the answers
* A catalog that is enabled at the Global scope **cannot** be disabled at the Project scope.
* who can add new catalogs - depends on the RBAC permissions for the account and the scope at which the catalog is being added 
* You **cannot** clone an application into the same namespace.


What can rancher use as a catalog repo:

* A public git repo serving over HTTP 
* A Helm repo serving over HTTP 
* A private git repo that requires username or password 

<!-- # Final Evaluation

* The only supported Kubernetes distributions where Rancher can be installed are RKE and K3s (as of 2.4)
* When communicating through Rancher, which party is responsible for the authorization component - the downstream cluster 
* RKE deploys Kubernetes components as Docker containers
* RKE can generate CSRs to use with an external CA to request certificates.
* Upgrading Kubernetes involves changing the version in the system_images key and running `rke up`
* Use a bind-mounted volume - for easier backups, upgrades, and rollbacks
* You **cannot** roll back a failed Rancher upgrade with `helm rollback`
* To use the Custom provider only requires that a supported version of Docker to be installed on the node
* When deploying into a cloud provider, where do the options that Rancher presents to you come from? It's fetched in real time from the provider, using your cloud credentials correct 
* Check logs for rancher api server: Using Kubectl with the logs subcommand for one of the pods in the cattle-system namespace
* How do you find the logs for etcd in an RKE cluster - docker logs
* Rancher acts as an authentication proxy when kubectl initiates a connection to a cluster
* Metric expression - requires that advanced monitoring is enabled for the cluster
* Even if the cluster has advanced monitoring enabled - project level adavanced monitoring still needs to be enabled
* Only `Service Discovery records` can only be assigned to a namespace
* Canal CNI supports project level isolation
* Rancher will create services for ports that you configure in the Workload deployment screen.
* You can designate a custom scheduler for Pod scheduling on nodes.
* ConfigMaps can only be assigned to a namespace.
* Secrets can be assigned to a project or namespace
* the ClusterIP for a Service does not change whenever the Workload is upgraded. -->
