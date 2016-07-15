# Intro to RabbitMQ

RabbitMQ is a message broker. It accepts and forwards messages.
It is a **postbox, post office and post man**.
It only deals with messages, blobs of data.

### Jargon

* Producing - sending a message
* Queue - mailbox
* Consuming - raceiving a message

### Libraries

RabbitMQ speaks [AMQP 0.9.1](https://www.rabbitmq.com/tutorials/amqp-concepts.html), a messaging protocol.

There are various [libraries available](https://www.rabbitmq.com/devtools.html) in your preferred programming language.

## Getting Started

The first thing you need to do is [install rabbit](../install-rabbitmq-on-ubuntu.md)

#### Sending

1. Connect to the rabbitMQ server
2. Make sure the recipient queue exists
3. Send the message to the exchange, The queue name needs to be specified in the `routing_key`
    **In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.**
4. Close the connection

#### Receiving

1. Connect to the rabbitMQ server
2. Create or make sure the queue exists. Creating a queue using `queue_declare` is idempotent - it makes sure it exists.
3. Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue. Whenever we receive a message, this callback function is called by the Pika library.
4. Start a never ending loop to receive messages: `channel.start_consuming()`

## Code

The code is available [here](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

##### Source:

- [Libraries for RabbitMQ](https://www.rabbitmq.com/devtools.html)
