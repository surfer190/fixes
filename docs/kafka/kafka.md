---
author: ''
category: Kafka
date: '2020-06-14'
summary: ''
title: Kafka
---
# Kafka

A distributed streaming platform.

what is does:

* publish and subscribe to streams of records - similar to a message queue
* store streams of records in a fault tolerant way
* Process streams of records as they occur

Used for:

* real-time streaming data pipelines
* real-time applications to transform or react to streams of data

Concepts:

* Run as a cluster of one or more servers
* Stores streams of records in categories called topics
* Each record consists of a key, value and timestamp

Four core API's:

* Producer API - publish a stream of records
* Consumer API - allows application to subscribe to one or more topics to process
* Streams API - allows application to act as a stream processor - taking input streams and producting output streams
* Connector API - reusable producers or consumers that connect to kafka topics eg. a db

## Python clients

* [confluent kafka python](https://github.com/confluentinc/confluent-kafka-python)
* [kafka-python](https://github.com/dpkp/kafka-python)
* [pykafka](https://github.com/Parsely/pykafka)

## Topics and Logs

The topic is a category or feed name to which records are published.
Topics are **multi-subscriber** - that is a topic can have zero, one or many consumers that subscribe to the data written to it.

> The Kafka cluster durably persists all published records—whether or not they have been consumed—using a configurable retention period

If the retention policy is set to two days, then for the two days after a record is published, it is available for consumption, after which it will be discarded to free up space

Kafka's performance is effectively constant with respect to data size so storing data for a long time is not a problem

The offset a consumer reads from is controlled by the consumer itself

## Producers

Publish data to the topic of their choice. The producer chooses which topic to assign to a record.

## Consumers

Label themselves with a consumer group name, each record published to a topic is delivered to 1 consumer instance within a group.

## Guarantees

* Messages sent by a producer to a particular topic partition will be appended in the order they are sent
* A consumer instance sees records in the order they are stored in the log

## Kafka as a Messaging System

Messaging has 2 models:

* queuing: pool of consumers read from a server and each record goes to one of them. They are not multisubscriber, once a process reads the data - it is gone. It lets you scale processing.
* publish-subscribe: allows you to broadcast data to multiple subscribers, but does not scale processing as every message goes to every subscriber.

The `consumer group` concept generalizes these 2 models.

> By having a notion of parallelism— _the partition_ —within the topics, Kafka is able to provide both ordering guarantees and load balancing over a pool of consumer processes.

## Kafka as a Storage System

Kafka is a good storage system

> Data written to Kafka is written to disk and replicated for fault-tolerance

## Kafka as a Stream Processor

# Kafka: Use Cases

* Messaging
* Website Activity Tracking
* Metrics
* Log Aggregation
* Stream Processing
* Event Sourcing
* Commit Log

Usually queues allow for some transaction, to ensure a desired action was executed before the message gets removed.
Once a message has been processed it is removed from the queue.

> It doesn’t allow you to kick off multiple independent actions based on the same event

This means messages in the queue are actually commands, suited towards imperitive programming.

Kafka, on the other hand, publish messages to topics and they get persisted.
They don't get removed when consumers receive them.
Allowing you to replay messages and many consumers to process logic.

## Kafka Commands

View (consume) messages from the beginning

    ./bin/kafka-console-consumer --topic veeam --from-beginning --bootstrap-server localhost:9092

