---
author: ''
category: Postgres
date: '2022-07-22'
summary: ''
title: ZeroMQ
---

## ZeroMQ

* a.k.a `zmq` 
* a high-performance asynchronous messaging library
* aimed for use in distributed or concurrent applications
* Provides a message queue
* a ZeroMQ system can run without a dedicated message broker (unlike other message-oriented middleware)
* supports common messaging patterns: `pub/sub`, `request/reply`, `client/server` and others
* supports a variety of transports: `TCP`, `in-process`, `inter-process`, `multicast`, `WebSocket` and more

> The zero is for zero broker (ZeroMQ is brokerless), zero latency, zero cost (it’s free), and zero administration.

> More generally, “zero” refers to the culture of minimalism that permeates the project. We add power by removing complexity rather than by exposing new functionality.

### In 100 words

* looks like an embeddable networking library but acts like a concurrency framework
* It gives you sockets that carry atomic messages across various transports like in-process, inter-process, TCP, and multicast
* You can connect sockets N-to-N with patterns like fan-out, pub-sub, task distribution, and request-reply.

ZeroMQ is for scale - the best possible results with the least costs

Pieter Hintjens created ZeroMQ and AMPQ. He also has some [interesting reads on his website unrelated to this](https://cultureandempire.com/).

> HTTP is perhaps the one solution to have been simple enough to work, but it arguably makes the problem worse by encouraging developers and architects to think in terms of big servers and thin, stupid clients

A good [python based zeroMQ intro](https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/basics.html)

### Python Example: CLient and Server

`hello_world_server.py`:

    import time
    import zmq

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print(f"Received request: {message}")

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send_string("World")

`hello_world_client.py`:

    import zmq

    context = zmq.Context()

    #  Socket to talk to server
    print("Connecting to hello world server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #  Do 10 requests, waiting each time for a response
    for request in range(10):
        print(f"Sending request {request} ...")
        socket.send_string("Hello")

        #  Get the reply.
        message = socket.recv()
        print(f"Received reply {request} [ {message} ]")

Running:

    pip install pyzmq
    python hello_world_server.py
    python hello_world_client.py

What are they doing:

1. They create a ZeroMQ context to work with, and a socket.
2. The server binds its REP (reply) socket to port 5555
3. The server waits for a request in an indefinite loop
4. Replies when a request is received
5. Client binds its REQ (request) socker to port 5555
6. Client sends a request and reads the reply from the server

> If you kill the server and restart it - the client won't recover. [Recovering from a crashed process is difficult](https://zguide.zeromq.org/docs/chapter4/#reliable-request-reply)

This is the request-reply pattern, probably the simplest way to use ZeroMQ. It maps to RPC and the classic client/server model.

* ZeroMQ doesn’t know anything about the data you send except its size in bytes. That means you are responsible for formatting it safely so that applications can read it back.
* Doing this for objects and complex data types is a job for specialized libraries like Protocol Buffers.

_Note: In C a string is terminated with a null byte, but in other languages not. So when communicating with services of other programming languages - problems and inconsistency may arise. Make sure C is checking for the null byte.

### Checking Version

Check `libzmq` version with `zmq.zmq_version()`. Check `pyzmq` version with `zmq.__version__`

    import zmq

    print(f"Current libzmq version is {zmq.zmq_version()}")
    print(f"Current  pyzmq version is {zmq.__version__}")

### One Way Data Distribution

A server pushes updates to a set of clients

A weather update server: that pushes the zip code and temparature. There is no start and no end - it is a never ending broadcast.

    import zmq
    from random import randrange


    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5556")

    while True:
        zipcode = randrange(1, 100000)
        temperature = randrange(-80, 135)
        relhumidity = randrange(10, 60)

        socket.send_string(f"{zipcode} {temperature} {relhumidity}")

The client listens to the broadcast and looks for new york info:

    import sys
    import zmq


    #  Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    print("Collecting updates from weather server...")
    socket.connect("tcp://localhost:5556")

    # Subscribe to zipcode, default is NYC, 10001
    zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
    socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

    # Process 5 updates
    total_temp = 0
    for update_nbr in range(5):
        string = socket.recv_string()
        zipcode, temperature, relhumidity = string.split()
        total_temp += int(temperature)

        print((f"Average temperature for zipcode " 
        f"'{zip_filter}' was {total_temp / (update_nbr+1)} F"))

#### Publish Subscribe

* When you use a `SUB` socket you must set a subscription using `zmq_setsockopt()` and SUBSCRIBE.
* If you don’t set any subscription, you won’t get any messages.
* The subscriber can set many subscriptions, which are added together. That is, if an update matches ANY subscription, the subscriber receives it.

> The PUB-SUB socket pair is asynchronous. The client does `zmq_recv()`, in a loop (or once if that’s all it needs). Trying to send a message to a SUB socket will cause an error. Similarly, the service does `zmq_send()` as often as it needs to, but must not do zmq_recv() on a PUB socket.

> There is one more important thing to know about PUB-SUB sockets: you do not know precisely when a subscriber starts to get messages. Even if you start a subscriber, wait a while, and then start the publisher, the subscriber will always miss the first messages that the publisher sends. This is because as the subscriber connects to the publisher (something that takes a small but non-zero time), the publisher may already be sending messages out.

_Slow joiner_ is a problem: Making a TCP connection involves to and from handshaking that takes several milliseconds depending on your network and the number of hops between peers. In that time, ZeroMQ can send many messages.

For a publisher that sends out 1000 messages: For sake of argument assume it takes 5 msecs to establish a connection, and that same link can handle 1M messages per second. During the 5 msecs that the subscriber is connecting to the publisher, it takes the publisher only 1 msec to send out those 1K messages.

You can use [synchronisation in chapter 2](https://zguide.zeromq.org/docs/chapter2/#sockets-and-patterns). Do not be tempted to use `sleeps`.

> The alternative to synchronization is to simply assume that the published data stream is infinite and has no start and no end. One also assumes that the subscriber doesn’t care what transpired before it started up.

Publish-subscribe:

* A subscriber can connect to more than one publisher, using one connect call each time. Data will then arrive and be interleaved (“fair-queued”) so that no single publisher drowns out the others.
* If a publisher has no connected subscribers, then it will simply drop all messages.
* If you’re using TCP and a subscriber is slow, messages will queue up on the publisher. We’ll look at how to protect publishers against this using the “high-water mark” later.
* From ZeroMQ v3.x, filtering happens at the publisher side when using a connected protocol (`tcp:@<>@` or `ipc:@<>@`). Using the `epgm:@<//>@` protocol, filtering happens at the subscriber side. In ZeroMQ v2.x, all filtering happened at the subscriber side.

Test the speed on your local:

    time python wu_client.py

### Divide and Conquer: Parrallel Pipeline

The model:

* A ventilator that produces tasks that can be done in parallel
* A set of workers that process tasks
* A sink that collects results back from the worker processes

Ventillator - generates 100 tasks, each a message telling the worker to sleep for some number of milliseconds:

    # Task ventilator
    # Binds PUSH socket to tcp://localhost:5557
    # Sends batch of tasks to workers via that socket
    #
    # Author: Lev Givon <lev(at)columbia(dot)edu>

    import zmq
    import random
    import time


    context = zmq.Context()

    # Socket to send messages on
    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5557")

    # Socket with direct access to the sink: used to synchronize start of batch
    sink = context.socket(zmq.PUSH)
    sink.connect("tcp://localhost:5558")

    print("Press Enter when the workers are ready: ")
    _ = input()
    print("Sending tasks to workers...")

    # The first message is "0" and signals start of batch
    sink.send(b'0')

    # Initialize random number generator
    random.seed()

    # Send 100 tasks
    total_msec = 0
    for task_nbr in range(100):

        # Random workload from 1 to 100 msecs
        workload = random.randint(1, 100)
        total_msec += workload

        sender.send_string(f"{workload}")

    print(f"Total expected cost: {total_msec} msec")

    # Give 0MQ time to deliver
    time.sleep(1)

Worker application - receives a message, sleeps for that number of seconds, and then signals that it’s finished:

    # Task worker
    # Connects PULL socket to tcp://localhost:5557
    # Collects workloads from ventilator via that socket
    # Connects PUSH socket to tcp://localhost:5558
    # Sends results to sink via that socket
    #
    # Author: Lev Givon <lev(at)columbia(dot)edu>

    import sys
    import time
    import zmq


    context = zmq.Context()

    # Socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5557")

    # Socket to send messages to
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5558")

    # Process tasks forever
    while True:
        s = receiver.recv()

        # Simple progress indicator for the viewer
        sys.stdout.write('.')
        sys.stdout.flush()

        # Do the work
        time.sleep(int(s)*0.001)

        # Send results to sink
        sender.send(b'')

Sink - collects the 100 tasks, then calculates how long the overall processing took, so we can confirm that the workers really were running in parallel if there are more than one of them:

    # Task sink
    # Binds PULL socket to tcp://localhost:5558
    # Collects results from workers via that socket
    #
    # Author: Lev Givon <lev(at)columbia(dot)edu>

    import sys
    import time
    import zmq


    context = zmq.Context()

    # Socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5558")

    # Wait for start of batch
    s = receiver.recv()

    # Start our clock now
    tstart = time.time()

    # Process 100 confirmations
    for task_nbr in range(100):
        s = receiver.recv()
        if task_nbr % 10 == 0:
            sys.stdout.write(':')
        else:
            sys.stdout.write('.')
        sys.stdout.flush()

    # Calculate and report duration of batch
    tend = time.time()
    print(f"Total elapsed time: {(tend-tstart)*1000} msec")

* The workers connect upstream to the ventilator, and downstream to the sink - we say that the ventilator and sink are stable parts of our architecture and the workers are dynamic parts of it.
* We have to synchronize the start of the batch with all workers being up and running. This is a fairly common gotcha in ZeroMQ and there is no easy solution. If you don’t synchronize the start of the batch somehow, the system won’t run in parallel at all.
* The ventilator’s PUSH socket distributes tasks to workers (assuming they are all connected before the batch starts going out) evenly. This is called load balancing and it’s something we’ll look at again in more detail.
* The sink’s PULL socket collects results from workers evenly. This is called fair-queuing.

### Programming with ZeroMQ

> Before you start that, take a deep breath, chillax, and reflect on some basic advice that will save you much stress and confusion

* Learn ZeroMQ step-by-step.
* Write nice code. Ugly code hides problems and makes it hard for others to help you.
* Test what you make as you make it
* When you find that things don’t work as expected, break your code into pieces, test each one, see which one is not working.

> Classy programmers share the same motto as classy hit men: always clean-up when you finish the job.

When you use ZeroMQ in a language like Python, stuff gets automatically freed for you.

> If you’re doing multithreaded work, it gets rather more complex than this.

**If you’re doing multithreaded work, it gets rather more complex than this.**

**some of you will, despite warnings, try to run before you can safely walk**

_Do not try to use the same socket from multiple threads_

## Why We Needed ZeroMQ

It is always good to go back to the _why_

Many applications these days consist of components that stretch across some kind of network, either a LAN or the Internet. So many application developers end up doing some kind of messaging.

Most of the time developers reinvent the wheel and use TCp or UDP themselves with disasterous consequences...

What is a message layer trying to solve:

* Handling I/O not letting it block - blocking I/O doesn't scale well
* Handling pieces that go away temporarily
* Presenting a message on a wite: so it is safe from overflow and easy to write and read
* Handling messages we can't deliver immediately - discard messages, put in db or put on redis
* Where do we store messages - what if there is a build up of messsages?
* How do we handle a lost message?
* Routing messages
* How do we write an api for another language
* How do we present data that can be read by different architectures - is this MQ responsibility?
* How do we handle network errors

> Zookeeper should be using a generic messaging layer and an explicitly documented wire level protocol. It is incredibly wasteful for teams to be building this particular wheel over and over.

So small to medium application developers are trapped. Either they avoid network programming and make monolithic applications that do not scale. Or they jump into network programming and make brittle, complex applications that are hard to maintain.
Or they bet on a messaging product, and end up with scalable applications that depend on expensive, easily broken technology.

> What we need is something that does the job of messaging, but does it in such a simple and cheap way that it can work in any application, with close to zero cost. It should be a library which you just link, without any other dependencies. No additional moving pieces, so no additional risk. It should run on any OS and work with any programming language.

This is ZeroMQ.

### Socket Scalability

When you have multiple clients and a single server - you have a singel socket. The socket is acting as a server and shoving data to the clients.

### Warning: Unstable Paradigms!

Traditional network programming is built on the general assumption that one socket talks to one connection, one peer.

> In the ZeroMQ universe, sockets are doorways to fast little background communications engines that manage a whole set of connections automagically for you

**A messaging pattern sitting in ZeroMQ scales more cheaply than a messaging pattern sitting in your application code.**

### Chapter 2

YOu can go through [zguide:Chapter 2](https://zguide.zeromq.org/docs/chapter2/) yourself.

## Sources

* [ZeroMQ](https://zeromq.org/get-started/)
* [Z Guide](https://zguide.zeromq.org/)
