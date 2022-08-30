---
author: ''
category: AWS
date: '2022-07-14'
summary: ''
title: Commonly used AWS Services
---

## Commonly used AWS Services

This _fix_ shows a few common AWS services and similar other services you may have worked with outside of the public cloud

## Analytics

* `MSK` (Apache Kafka) - Managed Service for Apache Kafka

### Compute

* `EC2` - Virtual machines (vmware vcloud director, digital ocean droplets, virtual private servers)
* `Lambda` - Serverless

### Containers

* `ECR` (Elastic Container Registry) - container registry (vmware harbor, docker registry)
* `ECS` (Elastic Container Service) - 
* `EKS` (Elastic Kubernetes Service) - downstream kubernetes (rancher rke, openshift okd, vmware tanzu, minikube)

### Database

* `DynamoDB` - Managed NoSQL (MongoDB, Cassandra, CouchDB but managed)
* `Amazon RDS` - Relation Database Service (Mysql, Postgres, Sqlite)

### Developer Tools

* `CodeBuild` - Build and Test Code (Jenkins, Gitlab CI)

### Management and Governance

* `Cloudwatch` - Monitor resources and applications (elasticsearch, LibreNMS, Mmonit)
* `CloudFormation` (CFN) - Create and manage resources with tempaltes - (terraform)
* `ControlTower` - Manage a Multi-account environment
* `Service Catalog` - Create and use standardised products (foreman, terraform, ansible)

### Networking and Content Delivery

* `Route 53` - DNS and Domain registration (Your DNS manager, PowerDNS)

### Storage

* `S3` - Storage in the cloud (Minio, dropbox, CDN provider)

### Load Balancing

* `ELB` (Elastic Load Balancer) - A subservice of EC2

### Security, Identity and Compliance

* `Secrets Manager` (Easily rotate, manage and retrieve secrets) - Hashicorp vault



## Other Things

* [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) - Used as a hub connecting many VPCs (virtual private clouds) and on-premises networks
