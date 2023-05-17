---
author: ''
category: Celery
date: '2023-04-17'
summary: ''
title: Celery vs Faust
---

## Celery vs Faust

Celery provides tooling for python to process large amounts of data on queues.
Looking through the [celery backends and brokers](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html) it was noticed that Apache Kafka was not in the list.

The brokers celery lists as supported are:

* rabbitmq
* redis
* amazon sqs

A broker actually runs the tasks, a backend stores the results of a task.

Result backends:

* sqlalchemy: sqlite, mysql and postgres
* redis
* rabitmq
* many others: es, dynamo, etc.

A bit of searching took place and Faust was found as a library for event/stream processing on kafka (as the topic - similar to a queue).

They provide some documentation on [Faust vs Celery](https://faust.readthedocs.io/en/latest/playbooks/vscelery.html)

In the current environment the ability is there to test all 5 brokers and these 2 coordination tooling packages.

The idea is to get a real world example of work to be done - set up and run it on the different tools and backends.

Then compare the setup process, configuration ease of getting the job setup as well as the performance of the different methods.

Look at resilience and abilty to replay events.

## Getting Started

There are [bundles to install via pip](https://docs.celeryq.dev/en/stable/getting-started/introduction.html#bundles) for using the different brokers or result backends

Thinking this may work:

    pip install "celery[librabbitmq,redis,sqs]"

## Run Redis Locally

    redis-server

or run as a docker container with podman:

    podman run -d --name redis-server -p 6379:6379 redis:6.2

## Run Rabbtimq locally

    rabbitmq-server

> Will crash and say port in use if already running

or run as a docker container with podman:

    podman run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

## Run Kafka Locally

Tried to run a docker image but it seems `docker-compose` is required:

* [hub.docker.com/r/bitnami/kafka/](https://hub.docker.com/r/bitnami/kafka/)
* [docs.redpanda.com/docs/get-started/quick-start/](https://docs.redpanda.com/docs/get-started/quick-start/)

## Run SQS locally

Found this interesting project called [localstack](https://github.com/localstack/localstack).

> You can run your AWS applications or Lambdas entirely on your local machine without connecting to a remote cloud provider

    pip install localstack

> This installs the localstack-cli which is used to run the Docker image that hosts the LocalStack runtime

Start localstack runtime:

    localstack start -d

Unfortunately podman is not well supported for MacOS for localstack

## On Redis

configure the location of your Redis database:

    app.conf.broker_url = 'redis://localhost:6379/0'

you can also connect to a list of redis sentinel:

    app.conf.broker_url = 'sentinel://localhost:26379;sentinel://localhost:26380;sentinel://localhost:26381'
    app.conf.broker_transport_options = { 'master_name': "cluster1" }

Setting the results backend:

    app.conf.result_backend = 'redis://localhost:6379/0'

> Calling a task returns an AsyncResult instance. This can be used to check the state of the task, wait for the task to finish, or get its return value (or if the task failed, to get the exception and traceback).

Results are not enabled by default. In order to do remote procedure calls or keep track of task results in a database, you will need to configure Celery to use a result backend.

Celery is a bit confusing to configure.
Errors are raised when one does not give the pid and log files:

    celery multi stop w1 -A project -l INFO --logfile="%n%I.log" --pidfile="%n.pid"

Otherwise one needs to ensure the celery user has permission to:

* `/var/run/celery/`
* `/var/log/celery`

It also looks for config in a number of places (celery runtime config). It uses `/etc/default/celeryd` ([ref](https://docs.celeryq.dev/en/stable/userguide/daemonizing.html#example-configuration)) and `/etc/conf.d/celery` ([ref](https://docs.celeryq.dev/en/stable/userguide/daemonizing.html#generic-systemd-celery-example)) depending on use of generic init scripts or systemd.

Quite confusing. If one wanted to run it in the context of k8s - how would the config for celery be provided?
There is a proposal for a [celery k8s operator](https://docs.celeryq.dev/projects/celery-enhancement-proposals/en/latest/draft/celery-kubernetes-operator.html?highlight=kubernetes)


