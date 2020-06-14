# AsyncIO

* Python 3.4 introduced `Asyncio`
* Python 3.5 introduced the `async` and `await` keywords

The community is wary, they seems to see them as complex and difficult to understand.

Many however have experienced _blocking_

Even when using `requests` your program pauses for a bit when it does a `requests.get(....)`

For once off tasks that is fine but for 10000 URL's it becmes difficult.

Large scale concurrency is a big reason to to learn and use `asyncio`, it is also much safer than _premeptive threading_

Goals for the book:

* compare `asyncio` and `threading`
* An udnerstanding of the `async` and `await` keywords
* A general overview of `asyncio`
* Examples and case studies

## 1. Introducing Asyncio

> Central focus of Asyncio is on how best to best perform multiple _waiting_ tasks at the same time 

The key thing is while you wait on one task to complete, work on another.

The waiting is usally associated with **network IO**. CPU's spending time doing network operations spend a lot of time waiting.

If you can direct the CPU to move between tasks - you need fewer CPU's but also you eliminate race conditions - compared to a threading (multi-CPU) approach.

### What is AsyncIO Solving

Using async based concurrency over thread based concurrency

* It is safer - than pre-emptive multitasking avoiding bugs and race conditions
* Support thousands of long lived connections - like websockets and MQTT

> Threading — as a programming model — is best suited to certain kinds of computational tasks that are best executed with multiple CPUs and shared memory for efficient communication between the threads

**Network programming** is not one of the domains that requires threading

There is too much waiting in network programming.

Event based programming models - asyncio:

* Will not make your code faster - if you want that use `cython` instead
* does not make threading redundant - True value of threading lies in multi-CPU applciations where tasks share memory.
* does not remove problems with the GIL (Global Interpreter Lock) - locks your interpreter to a single CPU to maintain thread safety. It prevents true _parrallelism_. Asyncio is single-threaded so it is not affected by the GIl - but is therefore locked to a single CPU.
* does not prevent all race conditions - asyncio can elimate `intra-process shared memory access` but other race conditions still happen.
* does not make concurrent programming easy - _concurrency is always complex_. Application design is still difficult: health checks, number of database connections, graceful termination, logging, disk access...

> The main advantage of Asyncio over threaded code is that the points at which control of execution is transferred between `co-routines` (functions) is visible - because of the `await` keyword presence. so it is much easier to figure out what is going on.

## 2. Truth about Threads

Features of an operating system made available to developers so they can inidcate what parts of the program operate in parrallel.
The OS decides how to share the CPU for these parts.

> Asyncio is an alternative to threading

### Benefits of Threading

* Ease of reading code - you can still set it out in a simple top down way
* Parallelism with shared memory - code can use multiple CPUs and share memory space
* know-how and existing code - there is a large body of knowledge and best practices

With python parrallelism is questionable as the GIL Global interpreter lock - pins all threads to a single CPU.

Generally speaking the best thing to use with threads is the `ThreadPoolExecutor` class from the `concurrent.futures` package - passing all required data through the `submit()` method.


    from concurrent.futures import ThreadPoolExecutor as Executor
    
    def worker(data):
        <process the data>
    
    with Executor(max_workers=10) as exe:
        future = exe.ubmit(worker, data)

You can convert the pool of threads into a pool of subprocesses with by switching to a `ProcessPoolExecutor`.

You want your tasks to be short so you can use: `Executor.shutdown(wait=True)` to shut it down

Also try to prevent your threaded code (in the preceding example, the `worker()` function) from accessing or writing to any global variables.

### Drawbacks of Threading

* Threading is difficult - race conditions are the hardest kinds of problems
* Threads are resource intensive - require upfront memory - less of an issue with 64bit OSes.
* Threading can affect throughput - with more than about 5000 threads there is a cost of context switching.
* Threading is inflexible - CPU time is shared between threads regardless of their waiting state. The OS may switch to a thread many thousands of times that is still waiting for the response to be recevied. In the async world a `select()` system call is made to check if the response awaiting function needs a turn - if it doesn't it is given no CPU time.

How to Test out resource usage by creating do-nothing threads:

    import os
    from time import sleep
    from threading import Thread

    threads = [
    Thread(target=lambda: sleep(60)) for i in range(10000)
    ]

    [t.start() for t in threads]
    print(f'PID = {os.getpid()}')
    [t.join() for t in threads]

Great quotes in the book about threading

Main points:

* Threading makes coding hard
* Threading is an inefficient model for large scale concurrency

**Some complex threading example with code is in the book...**

### Race Condition

THe problem in the code was:

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks

It created a race condition. The inline `+=` is implemented in C code as:

1. read `self.knives` into a temp location
2. add the new value `knives` to the value in the temp lcoaiton
3. Copy the new total from the temp location into the original

The problem with prememptive multitasking is that any thread can be stopped at _any time_...

Suppose ThreadBotA does step 1, the the OS scheduler pauses A and switches to ThreadbotB.
B also reads the value of `self.knives`. Then execution goes back to `A`...A increments its total and writes it back.
But then B continues from where it got paused and writes back its total.
Thereby erasing the changes made by A...

What?

This problem can be fixed by placing a `lock` around the modificaiton of the shared state.

    def change(self, knives, forks):  
        with self.lock:
            self.knives += knives
            self.forks += forks

We would have needed to add a `Threading.Lock` to the `Cutlery` class.

> But this requires you to know all the places where state will be shared between multiple threads

An issue when you use 3rd party libraries

> Note that it was not possible to see the race condition by looking at the source code alone. This is because the source code provides no hints about where execution is going to switch between threads. That wouldn’t be useful anyway, because the OS can switch between threads just about anywhere.

A much better solution - and the point of async programming - is to modify our code so a single thread - a single threadbot - moves between all the tables.
So the knives and forks will only be modified by a single thread.

Even better is in `async` programs we can see exactly where the context will switch because of the `await` keyword.

## 3. Async Walkthrough

There are 2 target audiences for `asyncio`:

1. End user developers - make applications using `asyncio`
2. Framework developers - make frameworks and libraries for end users

**the official Python documentation for asyncio is more appropriate for framework developers**

> end-user developers reading those docs quickly become shell-shocked by the apparent complexity

### Quickstart

> You only need to know about seven functions to use Asyncio - Yury Selivanov ([PEP492](https://www.python.org/dev/peps/pep-0492/)) which added `async` and `await` keywords to python

The main features an end user should care about:

* Starting the `syncio` event loop
* Calling `async/await` functions
* Waiting for multiple tasks to complete
* Closing the loop after all concurrent tasks have completed

    import asyncio, time

    async def main():
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Goodbye!')

    asyncio.run(main())

Asyncio provides a `run()` function to execute an `async def` and all other functions from there.

The equivalent of the above is:

    import asyncio
    import time

    async def main():
        print(f"{time.ctime()} Hello!")
        await asyncio.sleep(1.0)
        print(f"{time.ctime()} Goodbye!")

    loop = asyncio.get_event_loop()  
    task = loop.create_task(main())  
    loop.run_until_complete(task)  
    pending = asyncio.all_tasks(loop=loop)
    for task in pending:
        task.cancel()
    group = asyncio.gather(*pending, return_exceptions=True)  
    loop.run_until_complete(group)  
    loop.close()

* `loop = asyncio.get_event_loop()` - Get a loop instance - it will return the same one as long as you use a single thread. Inside a `def async` you should use `asyncio.get_running_loop()`
* `task = loop.create_task(coro)` - coro is your async function name. `create_task` schedules your coroutine to run in the loop. Cancel a task with `task.cancel()`
* `loop.run_until_complete(coro)` - blocks the current thread. Keeps the loop running only until the function completes - all other tasks will also run while the loop is running.
* `group = asyncio.gather(*pending, return_exceptions=True)` - when the `main` part of the program unblocks due to a process signal or `loop.stop()`  - gather still pending tasks, cancel them and then use `loop.run_until_complete()` until those tasks are done.
* `loop.close()` - final action - must be called on a stopped group. A stopped loop can be restarted a closed loop is gone for good. 

All these steps are done for you with `asyncio.run()`

#### How to run blocking functions

I/O bound functions need to coopoerate - o achieve coopoerative multitasking.
That means allowing a context switch back to the loop using `await`.

Most python code does not do this - it relies on you running such functions in threads.
Until there is more widespread support for `async def` such blocking libraries are unavoidable.

`asyncio` provides an API very similar to `concurrent.futures`...

    import time
    import asyncio

    async def main():
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Goodbye!')

    def blocking():  
        time.sleep(0.5)  
        print(f"{time.ctime()} Hello from a thread!")

    loop = asyncio.get_event_loop()
    task = loop.create_task(main())

    loop.run_in_executor(None, blocking)  
    loop.run_until_complete(task)

    pending = asyncio.all_tasks(loop=loop)  
    for task in pending:
        task.cancel()
    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()

* `blocking()` calls the traditional `time.sleep()` which would have blocked the main thread preventing your event loop from running. You can't even run this function from the main thread (where `asyncio` is running) - it must be run in an executor
* `loop.run_in_executor` allows us to run in a seperate thread or seperate process - does not block the main thread it returns a `Future` (not a `Task`) which means you can `await` it. It will begin only after `run_until_complete()` is called.
* `asyncio.all_tasks` returns all tasks not futures

What are futures?

### The Tower of Asyncio

* Tier 9: Network Streams - `StreamReader`, `StreamWriter`, `asyncio.open_connection()`, `asyncio.start_server()`
* Tier 8: Network TCP and UDP - `Protocol`
* Tier 7: Network Transports - `BaseTransport`
* Tier 6: Tools - `asyncio.Queue`
* Tier 5: Subprocesses and Threads - `run_in_executor()`, `asyncio.subprocess`
* Tier 4: Tasks - `asyncio.Task`, `asyncio.create_task()`
* Tier 3; Futures - `asyncio.Future`
* Tier 2: Event Loop - `asyncio.run()`, `BaseEventLoop`
* Tier 1: Coroutines - `async def`, `async with`, `async for`, `await`

Frameworks [curio](https://github.com/dabeaz/curio) and [trio](https://github.com/python-trio/trio) focus only on native coroutines - nothing whatsoever from the `asyncio` library module.

The next level is the event loop (curio and trio implement their own event loops), `asyncio` provides the specification `AbstractEventLoop` and an implmentation `BaseEventLoop`. [Uvloop](https://github.com/MagicStack/uvloop) uses the spec as a drop in replacement for the asyncio event loop.

A `Future` is loop aware. A `Task` is both loop aware and corouting aware.
An end user will use tasks much more than futures.

The Network Streams is the c=most convenient API to work with.

Tier 1: How to write `async def` functions and use `await` to call other functions is essential
Tier 2: Interacting and manading the event loop is essential: start, shut down and interaction
Tier 5: Executors are necessary for blocking code in your async application (like `SQLAlchemy`)
Tier 6: If you need to feed data to long running coroutines best way is with `asyncio.Queue` 
Tier 9: Simplest way to handle socket communication over a network

`aiohttp` is a third party library that handles socket communication for you.

### Components

#### Coroutine

`async def` is a corouting function. 

    In [1]: async def f(): 
    ...:     return 123 
    ...:                                                                                                                                          

    In [2]: type(f)                                                                                                                                  
    Out[2]: function

    In [3]: import inspect                                                                                                                           

    In [4]: inspect.iscoroutinefunction(f)                                                                                                           
    Out[4]: True

    In [5]: def g(): 
    ...:     yield 123 
    ...:                                                                                                                                          

    In [6]: type(g)                                                                                                                                  
    Out[6]: function

    In [7]: gen = g()                                                                                                                                

    In [8]: type(gen)                                                                                                                                
    Out[8]: generator

    In [9]: coro = f()                                                                                                                               

    In [10]: type(coro)                                                                                                                              
    Out[10]: coroutine

    In [11]: inspect.iscoroutine(coro)                                                                                                               
    Out[11]: True

    In [12]: inspect.iscoroutine(f)                                                                                                                  
    Out[12]: False

**A coroutine is an object that encapsulates the ability to resume an underlying function that has been suspended before completion**

Coroutines are very similar to generators.

When a coroutine returns, what really happens is that a `StopIteration` exception is raised

    In [13]: try: 
        ...:     coro.send(None) 
        ...: except StopIteration as e: 
        ...:     print('The answer was:', e.value)
    The answer was: 123

A coroutine is initialised by sending it a `None` - this is what the eventloop is going to be doing.

You don't need to do this as `await` and `loop.create_task(coro)` does this behind the scenes.

#### Await Keyword

The `await` keyword always takes a parameter and will accept only a thing called an `awaitable` which is:

* A corooutine (the result of a `async def` function)...ie. my_f = f()
* Any object implenting the `__await()__` special method. That special method must return an iterator.

    async def f():
        await asyncio.sleep(1)
        return 123

    async def main():
        result = await f()
        return result

When you `task.cancel` internally it will do a  `coro.throw()` to raise a `asyncio.CancelledError` in the coroutine.

    coro = f()
    coro.send(None)
    coro.throw(Exception, 'blah')

...
...
...
Much more intense shit dicussed in the book for about 40 - 50 pages

## 4. Asyncio librariesyou aren't using

### Streams (Standard Library)

The Streams API is a high level interface for async socket programming

#### Case Study: A Message Queue

    More in the book

### Twisted

Predates `asyncio` and has been flying the flag of async programming for 14 years now.

It implements a large number of internet protocols.
Teisted had to get around the lack of language support for async programming.
It did this using `callbacks`

### The Janus Queue

Provides communication between `queue.Queue` and `asyncio.Queue`

### Aiohttp

Brings all things `http` to `asyncio`.

An example of a very minimal async web server:

    from aiohttp import web

    async def hello(request):
        return web.Response(text="Hello, world")

    app = web.Application()  
    app.router.add_get('/', hello)  
    web.run_app(app, port=8080)

#### Case Study: Scraping the news

`aiohttp` can be used as both a server and client, like the very popular blocking `requests` library.

Documentation for [aiohttp](https://docs.aiohttp.org/en/stable/client_reference.html)

We will use [splash - Javascript rendering](https://splash.readthedocs.io/en/stable/index.html) because websites these days require javascript rendering to show usabel content.

The example is extremely convoluted - too many parts to make a good argument.
I would have just done a multiple requests done in under 2 seconds story but the author can choose his own adventure.

There was no need to go overboard with the use of a splash docker container whose image is in excess of 700 MB.

The important part is:

    async def news_fetch(url, postprocess):
        proxy_url = (
            f'http://localhost:8050/render.html?'  
            f'url={url}&timeout=60&wait=1'
        )
        async with ClientSession() as session:
            async with session.get(proxy_url) as resp:  
                data = await resp.read()
                data = data.decode('utf-8')
        return postprocess(url, data)  

and calling it with:

    sites = [
        ('http://edition.cnn.com', cnn_articles),  
        ('http://www.aljazeera.com', aljazeera_articles),
    ]
    tasks = [create_task(news_fetch(*s)) for s in sites] 
    await gather(*tasks)

#### Complete Example

Here is a more pallatable example of just getting a few quotes with `aiohttp`:

    from aiohttp import ClientSession
    import asyncio
    import time

    async def get_sites(sites):
        tasks = [asyncio.create_task(fetch_site(s)) for s in sites] 
        return await asyncio.gather(*tasks)  
        
    async def fetch_site(url):
        async with ClientSession() as session:
            async with session.get(url) as resp:  
                data = await resp.json()
        return data

    if __name__ == '__main__':
        categories = ["inspire", "management", "sports", "life", "funny", "love", "art", "students"]
        
        sites = [
            f'https://quotes.rest/qod?category={category}' for category in categories
        ]
        
        start_time = time.time()
        data = asyncio.run(get_sites(sites))
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} sites in {duration} seconds")
        
        print()
        print('*****Quotes*****')
        for response in data:
            quote = response['contents']['quotes'][0]
            text = quote.get('quote')
            author = quote.get('author')
            print(f'{text} - {author}')

> Remember many older examples would get the event loop and then run until completed with `asyncio.get_event_loop().run_until_complete(coro)`. But this is no longer needed, as `asyncio.run(coro)` was introduced in python3.7.

`asyncio.create_task(coro())` was also added in python3.7, which used to be `task = asyncio.ensure_future(coro())` in prior versions of python.

### ZeroMQ

Language agnostic library for networking applications giving smart sockets - it handles the more annoying and tedious tasks of conventional sockets.

* Manages message passing
* automatic reconnection logic - zeroMQ will automatically reconnect to the socket if the server goes down

It will still send out the info when reconnecting - providing functions of a message broker directly in the socket themselves. It is referred to as _brokerless messaging_

ZeroMQ sockets are already asyncronous - they can maintain many thousands of connections. 
We will use ZeroMQ via [PyZMQ](https://github.com/zeromq/pyzmq)

For more in depth examples check out [ZGuide](http://zguide.zeromq.org/page:all)

#### Case Study: Mulitple Sockets

You need a poller to send data between mutliple sockets because the sockets are not threadsafe

**poller.py**

    import zmq

    context = zmq.Context()
    # ZeroMQ sockets have _types_. `PULL` is receive only, `PUSH` is send only.
    # `SUB` is another socket that can only be fed by a `PUB` socket which is send only
    # To move data between multiple sockets in a threaded application you need a `poller`
    # because the sockets are not threadsafe, so you cannot `recv()` on different sockets in different threads


    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://localhost:5557')

    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://localhost:5556')
    subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

    poller = zmq.Poller()
    poller.register(receiver, zmq.POLLIN)
    poller.register(subscriber, zmq.POLLIN)

    # The poller will unblock when there is data ready to be received on one of the registered sockets
    while True:
        try:
            socks = dict(poller.poll())
        except KeyboardInterrupt:
            break
        
        if receiver in socks:
            message = receiver.recv_json()
            print(f'Via PULL: { message }')
        
        if subscriber in socks:
            message = subscriber.recv_json()
            print(f'Via SUB: { message }')

**poller_srv.py**

    import itertools
    import time
    import zmq

    context = zmq.Context()

    # There is a PUSH socket and a PUB socket
    # The loop sends data to both sockets every second

    pusher = context.socket(zmq.PUSH)
    pusher.bind('tcp://*:5557')

    publisher = context.socket(zmq.PUB)
    publisher.bind('tcp://*:5556')

    for i in itertools.count():
        time.sleep(1)
        pusher.send_json(i)
        publisher.send_json(i)

Now what does `asyncio` offer us for the `poller.py` side. Remember asyncio runs in a single thread.
This means it is fine to handle different sockets in different coroutines.

Readability is much improved with asyncio

**poller-aio.py**

    import asyncio
    import zmq
    from zmq.asyncio import Context

    context = Context()

    # Now we can deal with each socket in isolation
    # All `send()` and `recv()` must use `await`
    # The poller is no longer needed - it is integrated into the asyncio event loop

    async def do_receiver():
        receiver = context.socket(zmq.PULL)  
        receiver.connect("tcp://localhost:5557")
        while message := await receiver.recv_json():  
            print(f'Via PULL: {message}')

    async def do_subscriber():
        subscriber = context.socket(zmq.SUB)  
        subscriber.connect("tcp://localhost:5556")
        subscriber.setsockopt_string(zmq.SUBSCRIBE, '')
        while message := await subscriber.recv_json():  
            print(f'Via SUB: {message}')

    async def main():
        await asyncio.gather(
            do_receiver(),
            do_subscriber(),
        )

    asyncio.run(main())

It looks alot like threaded code but you don't have to risk the race condition

#### Case Study: Application Performance Monitoring

With containerised microservice based deployment practices of today - trivial things like monitoring CPU and memory usage has become more complicated than just running `top`.

There are tools that have been built but cost alot.

Lets build a prototype:

* Application layer: Add a ZeroMQ `transmitting` socket to each application to send metrics to a central server.
* Collection layer: Central server exposes a 0MQ socket to collect the data from all running applcations - weill also show a graph of performance
* Visualisation layer: Web page being served - charts must update in realtime. For simplicity using the [smoothiecharts](smoothiecharts.org) js library


Server-Sent Events (SSE's) are often preferable over websockets - due to their simplicity.

**app.py**

    import argparse
    import asyncio
    from random import randint, uniform
    from datetime import datetime as dt
    from datetime import timezone as tz
    from contextlib import suppress
    import zmq, zmq.asyncio, psutil

    '''
    A long lived coroutine to continually send data to the server
    It will use a `PUB` socket which handles all reconnection and buffering logic
    It will need to connect to the server on localhost:5555
    When a KeyboardInterrupt is received the task is cancelled
    The task cancelling is handled with `suppress()` from `contextlib`

    A continuous loop is used and stats are sent every second including the isoformatted date

    The `main()` function symbolizes the actual microservice for some data for the visulaisation
    The `--color` parameter lets us use a different colour per application

    The stats are acquired with `psutil` 
    '''


    ctx = zmq.asyncio.Context()

    async def stats_reporter(color: str):  
        p = psutil.Process()
        sock = ctx.socket(zmq.PUB)  
        sock.setsockopt(zmq.LINGER, 1)
        sock.connect('tcp://localhost:5555')  
        with suppress(asyncio.CancelledError):  
            while True:  
                await sock.send_json(
                    dict(  
                        color=color,
                        timestamp=dt.now(tz=tz.utc).isoformat(),  
                        cpu=p.cpu_percent(),
                        mem=p.memory_full_info().rss / 1024 / 1024
                    )
                )
                await asyncio.sleep(1)
        sock.close()  

    async def main(args):
        asyncio.create_task(stats_reporter(args.color))
        leak = []
        with suppress(asyncio.CancelledError):
            while True:
                sum(range(randint(1_000, 10_000_000)))  
                await asyncio.sleep(uniform(0, 1))
                leak += [0] * args.leak

    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--color', type=str)  
        parser.add_argument('--leak', type=int, default=0)
        args = parser.parse_args()
        try:
            asyncio.run(main(args))
        except KeyboardInterrupt:
            print('Leaving...')
            ctx.term()

**metric-server.py**

    import asyncio
    from contextlib import suppress
    import zmq
    import zmq.asyncio
    import aiohttp
    from aiohttp import web
    from aiohttp_sse import sse_response
    from weakref import WeakSet
    import json

    '''
    SSE (server-sent events) are the part that sends info to the frontend
    `WeakSet()` holds all the currently connected webclients which has a `Queue()` instance.

    The collected will `SUB`scribe to the publishing applications - no topic is specified - we will take everything
    In ZeroMQ you can make either end `pub` or `sub` the server - on other message queues the `pub` is usually the server.
    In our case the `SUB` is the server.

    We can `await` data from our connected apps

    The `feed()` coroutine creates a coroutine for each connected client.

    When a connection is closed the `weakset` will automatically be removed from connections

    `aiohttp_sse` provides `sse_response()` context manager - a scope to send data to the client.

    `index()` is the primary page load serving a static `html` file

    '''


    # zmq.asyncio.install()
    ctx = zmq.asyncio.Context()
    connections = WeakSet()  

    async def collector():
        sock = ctx.socket(zmq.SUB)  
        sock.setsockopt_string(zmq.SUBSCRIBE, '')  
        sock.bind('tcp://*:5555')  
        with suppress(asyncio.CancelledError):
            while data := await sock.recv_json():  
                print(data)
                for q in connections:
                    await q.put(data)  
        sock.close()

    async def feed(request):  
        queue = asyncio.Queue()
        connections.add(queue)
        with suppress(asyncio.CancelledError):
            async with sse_response(request) as resp:  
                while data := await queue.get():  
                    print('sending data:', data)
                    resp.send(json.dumps(data))  
        return resp

    async def index(request):  
        return aiohttp.web.FileResponse('./charts.html')

    async def start_collector(app):  
        app['collector'] = app.loop.create_task(collector())

    async def stop_collector(app):
        print('Stopping collector...')
        app['collector'].cancel()  
        await app['collector']
        ctx.term()

    if __name__ == '__main__':
        app = web.Application()
        app.router.add_route('GET', '/', index)
        app.router.add_route('GET', '/feed', feed)
        app.router.add_routes([web.static('/static', 'static')])
        app.on_startup.append(start_collector)  
        app.on_cleanup.append(stop_collector)
        web.run_app(app, host='127.0.0.1', port=8088)

**chart.html**

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Server Performance</title>
        <script src="./static/smoothie.js"></script>
        <script type="text/javascript">
            function createTimeline() {
                var cpu = {};  
                var mem = {};

                var chart_props = {
                    responsive: true,
                    enableDpiScaling: false,
                    millisPerPixel:100,
                    grid: {
                        millisPerLine: 4000,
                        fillStyle: '#ffffff',
                        strokeStyle: 'rgba(0,0,0,0.08)',
                        verticalSections: 10
                    },
                    labels:{fillStyle:'#000000',fontSize:18},
                    timestampFormatter:SmoothieChart.timeFormatter,
                    maxValue: 100,
                    minValue: 0
                };

                var cpu_chart = new SmoothieChart(chart_props);  
                var mem_chart = new SmoothieChart(chart_props);

                function add_timeseries(obj, chart, color) {  
                    obj[color] = new TimeSeries();
                    chart.addTimeSeries(obj[color], {
                        strokeStyle: color,
                        lineWidth: 4
                    })
                }

                var evtSource = new EventSource("/feed");  
                evtSource.onmessage = function(e) {
                    var obj = JSON.parse(e.data);  
                    if (!(obj.color in cpu)) {
                        add_timeseries(cpu, cpu_chart, obj.color);
                    }
                    if (!(obj.color in mem)) {
                        add_timeseries(mem, mem_chart, obj.color);
                    }
                    cpu[obj.color].append(
                        Date.parse(obj.timestamp), obj.cpu);  
                    mem[obj.color].append(
                        Date.parse(obj.timestamp), obj.mem);
                };

                cpu_chart.streamTo(
                    document.getElementById("cpu_chart"), 1000
                );
                mem_chart.streamTo(
                    document.getElementById("mem_chart"), 1000
                );
            }
        </script>
        <style>
            h1 {
                text-align: center;
                font-family: sans-serif;
            }
        </style>
    </head>
    <body onload="createTimeline()">
        <h1>CPU (%)</h1>
        <canvas id="cpu_chart" style="width:100%; height:300px">
        </canvas>
        <hr>
        <h1>Memory usage (MB)</h1>
        <canvas id="mem_chart" style="width:100%; height:300px">
        </canvas>

We use javascripts [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) the interface for server-sent events.

The `onmessage` method is fired when it receives a message from the server.
The data is appended to a time series with the colour as the key.

Start up everything:

    python metric-server.py
    pyhton backend-app.py --color red &
    python backend-app.py --color blue --leak 10000 &
    python backend-app.py --color green --leak 100000 &
    
**Unfortunately the example did not work for me - the frontend showed the charts but with no content - I don't think `onMessage` ever fired as I put a `console.log('hello')` in there and it never printed out**

### asyncpg and Sanic

[asyncpg](https://github.com/MagicStack/asyncpg) provides client access to postgres but focusses on speed.

It achieves the speed by working with the PostgreSQL binary protocol.

Let's set up a local postgres instance with docker...exposing port `55432` to the host which maps to `5432` in the container.

    docker run -d --rm -p 55432:5432 postgres

Damn, it goes deep and low level here. I try to stay ORM and up when it comes to databases...

So more in the book if you want to go a bit lower.

It also introduces and gives examples with the [sanic web framework](https://sanic.readthedocs.io/en/latest/).

I hear that [GINO](https://github.com/python-gino/gino) and [tortoiseORM ](https://github.com/tortoise/tortoise-orm) is doing good work.










## Sources

* [Book: Using Asyncio in python - Caleb Hattingh (2020)](https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/)
