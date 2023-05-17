---
author: ''
category: Celery
date: '2020-06-14'
summary: ''
title: Celery Basics
---
# Celery Fundamentals

> Celery is a task queue with batteries included

## Broker

Celery relies on  broker a message queue to send and receive messages

* RabbitMQ
* Redis

Message queues align quite well with containers due to their ephemeral nature and need of being fault tolerant.

You can start a rabbitmq docker container with:

    docker run -d -p 5462:5462 rabbitmq

You can start a redis docker container with:

    docker run -d -p 6379:6379 redis

> You can asoo use Amazon SQS

## Installing

    pip install celery

## Application

You need a celery instance - an app.
It is the entrypoint for everything you want to do in celery: creating tasks and managing workers.

In `tasks.py`:

    from celery import Celery

    app = Celery('tasks', broker='pyamqp://guest@localhost//')

    @app.task
    def add(x, y):
        return x + y

* The first argument to Celery is the name of the current module
* The second argument is the broker keyword argument - the url of the message queue you want to use

For rabbitmq: `amqp://localhost`
For redis: `redis://localhost`

You create a single task that returns the sum of 2 values

## Running the Celery Worker Server

    celery -A tasks worker --loglevel=info

## Calling the task

    from tasks import add
    add.delay(4, 4)

Calling a task returns an `AsyncResult` instance

This can be used to check the state of the task, wait for the task to finish, or get its return value (or if the task failed, to get the exception and traceback)

> Results are not enabled by default. In order to do remote procedure calls or keep track of task results in a database, you will need to configure Celery to use a result backend

## Keeping Results

If you want to keep track of the tasks’ states, Celery needs to store or send the states somewhere

Backends:

* Django / SQLAlchemy ORM
* Memcached
* Redis
* RPC

You need to set the `result_backed`

    app = Celery('tasks', backend='rpc://', broker='pyamqp://')

You can then keep the `AsyncResult`:

    from tasks import add
    result = add.delay(4, 8)
    
    result.ready()
    True
    
    result.get()
    12
    
    #If there was an error
    result.traceback
