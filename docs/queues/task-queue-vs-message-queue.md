---
author: ''
category: Queues
date: '2022-07-25'
summary: ''
title: Task Queue vs Message Queue
---

## Task Queue vs Message Queue

RabbitMQ, Kafka, Amazon SQS, Celery, Redis and ZeroMQ...

There are queues or brokers that we may have seen or heard of in a general sense. Oftentimes they are called a message queue or a task queue.
So the terms seem to get muddled up and confused.
There is a difference between a message queue and a task queue.

A `Message Queue` - receives and delivers messages.

A `Task Queue` - receives tasks with the related data, runs them and delivers the results.

### Message Queue

Anything `MQ` is a message queue. It deals with receiving and sending messages.
Rabbit**MQ** and Zero**MQ** are message queues.

The developer needs to understand how AMPQ works (maybe) and how to handle the sending of messages and receiving of messages from the queue.

### Task Queue

The task queue knows the operations to run for a specific message. Celery handles the interactions and gives an easy interface to tell the other compontents what to do. You can then switch out the message broker for RabbitMQ, Redis or even a database. Celery also handles the results of the tasks.

## Sources

* [Stackoverflow: message-queue-vs-task-queue-difference](https://stackoverflow.com/questions/10075817/message-queue-vs-task-queue-difference)
