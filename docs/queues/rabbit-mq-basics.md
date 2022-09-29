---
author: ''
category: Queues
date: '2019-10-24'
summary: ''
title: Rabbit Mq Basics
---
# RabbitMQ

* A producer is a user application that sends messages.
* A queue is a buffer that stores messages.
* A consumer is a user application that receives messages.

## Hello World - Message Queue

Message queue - communication between systems.
A simple example.

python send.py

    #!/usr/bin/env python
    import pika

    # Establish a connection with rabbitMQ - a broker on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Make sure the recipient queue exists - otherwise it will be dropped
    channel.queue_declare(queue='hello')

    # In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
    # The default exchange is an empty string
    # queue name must be specified in the routing_key
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello World!'
    )
    print(" [x] Sent 'Hello World!'")

    # Ensure network buffers flushed and message sent
    connection.close()

python receive.py

    #!/usr/bin/env python
    import pika

    # Establish a connection with rabbitMQ - a broker on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Make sure the recipient queue exists - otherwise it will be dropped
    # We are not sure that the queue exists already
    channel.queue_declare(queue='hello')

    # Receiving messages on the queue requires subscribing a callback function to a queue
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Tell RabbitMQ that this particular callback function should receive messages from our hello queue
    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )

    # finally, we enter a never-ending loop that waits for data and runs callbacks whenever necessary
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

## Sleep - Task Queue

Work queue - distributing long running tasks among workers

Real tasks here would be: images to be resized, pdf files to be rendered or emails to be sent.

Round-robin dispatching - easily parallelise work - add more workers and that way, scale easily.

We can run more than 1 `worker.py` at a time

> By default, RabbitMQ will send each message to the next consumer, in sequence

    python worker.py
    python worker.py
    python new_task.py First message.
    python new_task.py Second message..
    python new_task.py Third message...
    python new_task.py Fourth message....
    python new_task.py Fifth message.....

Messages are distributed to workers in a round robin

## CLI

Add it to you path on homebrew with:

    export PATH=/usr/local/Cellar/rabbitmq/3.7.16/sbin:$PATH  

View available queues

    sudo rabbitmqctl list_queues

List exchanges on a server

    sudo rabbitmqctl list_exchanges

List existing bindings

    rabbitmqctl list_bindings

## Message Acknowledgement

What if a consumer dies with a task only halfway done?

Currently rabbitMQ will mark a message for deletion as it is delivered

> But we don't want to lose any tasks. If a worker dies, we'd like the task to be delivered to another worker.

For this RabbitMQ supports message acknowledgements.
An `ack` tells RabbitMQ that it is free to delete a task

Manually message acknowledgements are enabled by default. We turn that off with:

    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )

We should remove the `auto_ack=True` and send a real acknowledgement once the task is complete.
You do that with:

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(
        queue='hello',
        on_message_callback=callback
    )

It is common to forget acknowledgements, so use:

    sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

### Message durability

> When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to

Tell rabbitmq it is durable:

    channel.queue_declare(queue='hello', durable=True)

Ensure the queue name os different

You also need to mark the messages as persistent with `delivery_mode = 2`:

    channel.basic_publish(
        exchange='',
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode = 2, # make message persistent
        )
    )

### Fair Displatch

This tells RabbitMQ not to give more than one message to a worker at a time

    channel.basic_qos(prefetch_count=1)

> If all the workers are busy, your queue can fill up

## Pub Sub

The assumption behind a work queue is that each task is delivered to exactly one worker.

You can also deliver a message to multiple consumers, known as "publish/subscribe"

_the producer can only send messages to an exchange_

An exchange receives messages from producers and pushes them to queues

What should the exchange do:

* Append to a particular queue
* Append to many queues
* Should it get discarded

The exchange type define the rules: 

* direct
* topic
* headers
* fanout - broadcasts all messages it receives to all the queues it knows

Lets crate a `fanout` exchange:

    channel.exchange_declare(exchange='logs',
                            exchange_type='fanout')

We can now publish to this names exchange with:

    channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

Create a fresh empty queue with:

    result = channel.queue_declare(queue='')

Once a consumer connection is closed the queue should be deleted:

    result = channel.queue_declare(queue='', exclusive=True)

### Bindings

The relationship between the exchange and the queue
