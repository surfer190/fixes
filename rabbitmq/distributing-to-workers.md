# Distribute time-consuming tasks among multiple workers on RabbitMQ

If you need images to be resized or pdf files to be generated or another task that may be too much or too long to
handle for a single HTTP request.

So just add more workers and that way you can **scale easily**

## Round robin distribution

By default, RabbitMQ will send each message to the next consumer, in sequence. On average every consumer will get the same number of messages. This way of distributing messages is called round-robin.

## Message acknowledgement

What if a task takes so long and the worker dies with the task only half done. The message will be lost.
All subsequent tasks sent to the worker will also be lost.
But we don't want to lose any tasks. If a worker dies, we'd like the task to be delivered to another worker.

To prevent this we use **Message Acknowledgements**

An ack(nowledgement) is sent back from the consumer to tell RabbitMQ that a particular message had been received, processed and that RabbitMQ is free to delete it.

If a consumer dies (its channel is closed, connection is closed, or TCP connection is lost) without sending an ack, RabbitMQ will understand that a message wasn't processed fully and will re-queue it.

If there are other consumers online at the same time, it will then quickly redeliver it to another consumer.

That way you can be sure that no message is lost, even if the workers occasionally die.

##### Forgotten acknowledgement

It's a common mistake to miss the `basic_ack`

To debug this you can use `sudo rabbitmqctl` to print the `messages_unacknowledged` field

## Message durability

So if a worker(consumer) dies we know our task is not lost.
But our tasks will still be lost if the server stops.

Two things are required to make sure that messages aren't lost: we need to mark both the queue and messages as durable.

Make sure rabbitMQ never loses our queue:

```
channel.queue_declare(queue='hello', durable=True)
```

_RabbitMQ doesn't allow you to redefine an existing queue with different parameters and will return an error to any program that tries to do that._

So must change the name of the queue

Mark our messages as persistent - by supplying a `delivery_mode` property with a value `2`.

```
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
```

There are some instances when messages won't persist, if you need a stronger guarantee then you can use **publisher confirms**

## Fair dispatch

With round robin, if al the odd messages are heavy then one worker will have to do much more and will suffer much higher load thanthe other.

_This happens because RabbitMQ just dispatches a message when the message enters the queue. It doesn't look at the number of unacknowledged messages for a consumer. It just blindly dispatches every n-th message to the n-th consumer._

```
channel.basic_qos(prefetch_count=1)
```

The above, tells RabbitMQ not to give more than one message to a worker at a time. Or, in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one. Instead, it will dispatch it to the next worker that is not still busy.

> Note: If all the workers are busy, your queue can fill up. You will want to keep an eye on that, and maybe add more workers, or have some other strategy.
