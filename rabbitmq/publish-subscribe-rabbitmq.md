# Publish/Subscribe

Deliver a message to multiple consumers

The _producer_ always sends messages to an _exchange_

The exchange must know exactly what to do with a message it receives.
The rules on what is does, is governed by the _exchange_ type

Exchange types:
- direct
- topic
- headers
- fanout - broadcasts all the messages it receives to all the queues

### Publish

```
channel.exchange_declare(exchange='logs',
                         type='fanout')
```

## Namesless exchange

The default exchange is nameless

```
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
```

## Temporary queues

`result = channel.queue_declare()`

Disconnect and delete:

`result = channel.queue_declare(exclusive=True)`

## Binding

We need to tell the exchange to send messages to our queue. That relationship between exchange and a queue is called a `binding`.

```
channel.queue_bind(exchange='logs',
                   queue=result.method.queue)
```

**Top tip: List existing bindings with:**

```
sudo rabbitmqctl list_bindings
```

The messages will be lost if no queue is bound to the exchange yet, but that's okay for us; if no consumer is listening yet we can safely discard the message.
