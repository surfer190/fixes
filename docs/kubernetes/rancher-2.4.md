---
author: ''
category: Kubernetes
date: '2020-04-20'
summary: ''
title: Rancher 2.4
---
## Rancher 2.4

### Security

* Cluster CIS scans - scan for vulnerabilities - leverages [kubebench](https://github.com/aquasecurity/kube-bench)
* Security Policies for users - example: only deploy from specific registry or organisation. Rancher is integrated with [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper

> CIS scans require internet activity

> Tools -> CIS Scans -> "Run Scan"

You can add alerts to the security scan to notify when a security breach is made

Scan is done on per cluster basis

#### Gatekeeper Examples

* Allowed Repos - which image reigstries can be used
* Container limits - set limits on container eg. CPU, memory
* Required Labels - require resources have specific Labels
* Pod Security Policies - Set policies on pods

Pod securitiy policies only apply to the pods itself, gatekeeper can restrict across the whole cluster.

OPA does not inspect running processes/containers - it only checks resource defintitions against a policy.

### Rancher 2.4

* Upgrading is much easier - zero downtime delpoys
* Can support many more clusters and nodes (Up to 2000 clusters, up to 20000 nodes)

RKE clusters are clusters that Rancher has provisioned directly.
Imported RKE clusters still need to be upgraded manually.

Rollback is not zero downtime - rewinds the world very quickly.

The Snapshots, upgrade and rollback is done on the cluster main page...on the dots on the side next to `kube config` download

Snapshots are saved to the localhost on `etcd` or you can configure backups to go through `s3` or an s3 api like minio as an adapter to other providers.

