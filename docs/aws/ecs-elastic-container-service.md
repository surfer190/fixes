---
author: ''
category: AWS
date: '2022-07-25'
summary: ''
title: ECS - Elastic Container Service
---

## What is Amazon Elastic Container Service?

* Highly scalable and fast container management service
* run, stop, and manage containers on a cluster.
* containers are defined in a task definition - to run an individual task or task within a service
* a service is a configuration that lets you run a number of tasks simultaneosly
* You can run your tasks and services on a serverless infrastructure that's managed by _AWS Fargate_ or on a a cluster of _Amazon EC2 instances_
* Integrated with _Amazon Elastic Container Registry_ and Docker
* CI/CD: monitors changes to source dir, Builds new Docker image, pushes to container registry (ecr) and updates your ecs service to use the new image
* Supports service discovery
* Sending logs and metrics to _Amazon Cloudwatch_

### Launch Types

* Fargate - pay-as-you-go - run containers without having to manage your infrastructure
* EC2 - configure and deploy ec2 instances in your cluster

Fargate better for large workloads requiring minimal overhead, small workloads with occasional bursts, tiny workloads and batch workloads
EC2 better for workloads needing constantly high cpu and memeory, large workloads to optimise for price, access to persistent storage and you must self manage.

### Managment

* AWS Management Console - web interface
* [AWS Command Line Interface](https://aws.amazon.com/cli/) - cli
* AWS SDKs - language specific interface for python that it [boto3](https://aws.amazon.com/sdk-for-python/)
* [AWS copilot](https://github.com/aws/copilot-cli) - open source tool for ecs
* [Amazon ECS CLI](https://github.com/aws/amazon-ecs-cli) - command line interface to Fargate and ECS - you can test locally or in the cloud
* [AWS CDK](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-ecs-web-server-cdk.html) - Amazon Cloud Development kit



## Source

* [Amazon - Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

