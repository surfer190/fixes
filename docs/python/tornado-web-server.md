---
author: ''
category: Python
date: '2022-07-14'
summary: ''
title: Tornado Web Server
---

# Tornado Web Server 4.5.3

> This is an old version of tornado

* Python web framework and asynchronous networking library
* Non-blocking network io, tornado can scale to 10s of thousands of open connections
* Ideal for long polling and web sockets
* Is not based on WSGI (Web Server Gateway Interface) spec defined in [PEP3333](https://peps.python.org/pep-3333/)
* Is run one thread per process
* Can use `tornado.wsgi` but better to use `tornado.web`
* Integration with asyncio only happened in tornado>=6

## Install

    pip install tornado

## Hello World Example

    import asyncio

    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    async def main():
        app = make_app()
        app.listen(8888)
        await asyncio.Event().wait()

    if __name__ == "__main__":
        asyncio.run(main())

Tested:

    $ http localhost:8888      
    HTTP/1.1 200 OK
    Content-Length: 12
    Content-Type: text/html; charset=UTF-8
    Date: Mon, 11 Jul 2022 06:43:32 GMT
    Etag: "e02aa1b106d5c7c6a98def2b13005d5b84fd8dc8"
    Server: TornadoServer/6.2

    Hello, world

> This example does not use tornado's async features...

#### Load Test Hello World

    $ ab -c 100 -n 1000 http://localhost:8888/
    Requests per second:    5915.93 [#/sec] (mean)
    Time per request:       16.903 [ms] (mean)
    Time per request:       0.169 [ms] (mean, across all concurrent requests)
    Transfer rate:          1184.34 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        0    2   1.5      2       7
    Processing:     5   14   3.5     13      23
    Waiting:        2   14   3.5     13      23
    Total:          6   16   3.6     16      24

    Percentage of the requests served within a certain time (ms)
    50%     16
    66%     17
    75%     18
    80%     19
    90%     21
    95%     22
    98%     24
    99%     24
    100%     24 (longest request)

`ab` or tornado seems to break (on mac) when there are more than 200 conurrect requests:

    apr_socket_recv: Connection reset by peer (54)

### Structure of a Tornado web application

* One or more `RequestHandler` subclasses
* An `Application` object - that routes incoming requests to handlers
* a `main()` function to start the server

The `Application` object - global config and routing requests to handlers.
A list of `URLSpec` objects - mapping a regular expression to a handler, initialization arguments it sends to `RequestHandler.initialize` and it also has a name so it can be reversed with `RequestHandler.reverse_url`.
Regular expression variables are sent as a string to the `get` function.

Subclassing `RequestHandler` - the main entry point is the HTTP method being handled `get()`, `post()`. To return a response `RequestHandler.render` or `RequestHandler.write` are called. Render needs a template. Write accepts dicts that will return as json.

#### BaseHandler

It is common to define a `BaseHandler` class that overrides methods such as `write_error` and `get_current_user` and then subclass your own BaseHandler instead of RequestHandler for all your specific handlers

#### Handling request input

You can access the [`HttpServerRequest`](https://www.tornadoweb.org/en/branch4.5/httputil.html#tornado.httputil.HTTPServerRequest) with `self.request`.

Tornado does not parse json request bodies - if you want to do that you can override `prepare`:

    def prepare(self):
        if self.request.headers["Content-Type"].startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

#### Sequence of Calls

1. A new `RequestHandler` object is created
2. `initialize()` is called with the argument defined in main
3. `prepare()` is called - usually in the base class - may produce output; if it calls finish (or redirect, etc), processing stops here
4. One of the http methods is called `get()`, `post()`, `put()`
5. When finished `on_finish()` is called. Synchronously it runs after `get()`, asyncronously it runs after `finish()`

Commonly overidden things of [RequestHandler](https://www.tornadoweb.org/en/branch4.5/web.html#tornado.web.RequestHandler):

* `write_error` - outputs HTML for use on error pages.
* `on_connection_close` - called when the client disconnects; applications may choose to detect this case and halt further processing. Note that there is no guarantee that a closed connection can be detected promptly.
* `get_current_user` - see User authentication
* `get_user_locale` - returns Locale object to use for the current user
* `set_default_headers` - may be used to set additional headers on the response (such as a custom Server header)

#### Error Handling

* `RequestHandler.write_error` generates an error page. Override this for a custom error messag (in the base handler).

#### Redirection

* `RequestHandler.redirect` - use `redirect()`
* point to a `RedirectHandler` instead of a `RequestHandler`

#### Asynchronous handlers

Tornado handlers are synchronous by default: when the `get()`/`post()` method returns, the request is considered finished and the response is sent.
Since all other requests are blocked while one handler is running, any long-running handler should be made asynchronous so it can call its slow operations in a non-blocking way.

The simplest way to make asynchornous server handler according to the docs is using [coroutines](https://www.tornadoweb.org/en/branch4.5/guide/coroutines.html) but there is no example there.

The example they use:

    class MainHandler(tornado.web.RequestHandler):
        @tornado.gen.coroutine
        def get(self):
            http = tornado.httpclient.AsyncHTTPClient()
            response = yield http.fetch("http://friendfeed-api.com/v2/feed/bret")
            json = tornado.escape.json_decode(response.body)
            self.write("Fetched " + str(len(json["entries"])) + " entries "
                    "from the FriendFeed API")

You can also use the `asynchornous` decorator with a async client with a callback

    class MainHandler(tornado.web.RequestHandler):
        @tornado.web.asynchronous
        def get(self):
            http = tornado.httpclient.AsyncHTTPClient()
            http.fetch("http://friendfeed-api.com/v2/feed/bret",
                    callback=self.on_response)

        def on_response(self, response):
            if response.error: raise tornado.web.HTTPError(500)
            json = tornado.escape.json_decode(response.body)
            self.write("Fetched " + str(len(json["entries"])) + " entries "
                    "from the FriendFeed API")
            self.finish()

> When `get()` returns, the request has not finished. When the HTTP client eventually calls `on_response()`, **the request is still open**, and the response is finally flushed to the client with the call to `self.finish()`.

In the above examples when the request is seen - it immediately puts the work to a thread and deals with the next incoming requests.

You can also inspect the results in the callback or after the `yield` keyword with `import ipdb; ipdb.set_trace()`

Instead `yield` and the `gen.coroutine` decorator you can use `async` and `await` if you are on `python3.5` and later:

    class MainHandler(tornado.web.RequestHandler):
        async def get(self):
            http = tornado.httpclient.AsyncHTTPClient()
            response = await http.fetch("http://friendfeed-api.com/v2/feed/bret")
            json = tornado.escape.json_decode(response.body)
            self.write("Fetched " + str(len(json["entries"])) + " entries "
                    "from the FriendFeed API")

> Only tasks that will take a long time (usually IO - network and file based operations) need to be defferred. That means more requests can be deal with quickly and none will be blocked.

### Running and deploying

Tornado supplies its own HTTPServer - so it is different from other web frameworks (fast api, django).

> Tornado is normally intended to be run on its own, without a WSGI container. In some environments only `wsgi` is allowed.

The features that are not allowed in WSGI mode include:

* coroutines
* the `@asynchronous` decorator
* AsyncHTTPClient
* the auth module
* WebSockets

Instead of configuring a WSGI container to find your applciation, you write a `main()` function:

    def main():
        app = make_app()
        app.listen(8888)
        IOLoop.current().start()

    if __name__ == '__main__':
        main()

> Configure your OS or process manager to run this program

_Remember to increase the number of open files per process (to avoid “Too many open files”-Error)_

#### Processes and ports

Because of the Python GIL (Global Interpreter Lock) you need to run multiple processes to make full use of the number of cores on your computer or server.

> Typically it is best to run one process per CPU

You can enable multiprocess mode with:

    def main():
        app = make_app()
        server = tornado.httpserver.HTTPServer(app)
        server.bind(8888)
        server.start(0)  # forks one process per cpu
        IOLoop.current().start()

> Note you must use `server.bind()` and not `server.listen()`

Limitations:

* each child process will have its own IOLoop - so do not modify before forking
* all processes share the same port - it is hard to monitor individually
* difficult to do zero downtime updates

For more sophisticated deployments, it is recommended to start the processes independently, and have each one listen on a different port.
The [`process groups`](http://supervisord.org/configuration.html#program-x-section-settings) feature of supervisord is one good way to arrange this

#### Debug mode

Passing `debug=True` to the app constructor enables:

* `autoreload=True` - automatic reload (only works in single process mode)
* `compiled_template_cache=False` - templates will not cache
* `static_hash_cache=False` - static files will not be cached
* `serve_traceback=True` - an error page and stack trace will be generated

Automatic reload standalone: `python -m tornado.autoreload myserver.py`

### Templates and UI

Info on [templates and ui](https://www.tornadoweb.org/en/branch4.5/guide/templates.html)

### Authentication

Info on [authentication](https://www.tornadoweb.org/en/branch4.5/guide/security.html#user-authentication)

### Major components of Tornado

* A web framework `RequestHandler` sub-classed / inherited from to create web applications
* Client- and server-side implementions of HTTP (`HTTPServer` and` AsyncHTTPClient`).
* An asynchronous networking library including the classes `IOLoop` and `IOStream`, which serve as the building blocks for the HTTP components and can also be used to implement other protocols.

## Threads

* Tornado is not thread-safe - manipulation of shared data structures between threads can have unintended consequences - like race conditions.
* `IOLoop.add_callback` is the only method safe to call from other threads
* `IOLoop.run_in_executor` is the recommended way to runsynchronously blocking code in another thread
* Integrated with standard lib `ayncio` (only in versions 6 and greater)

### Asynchronous and non-blocking IO

Real-time web features require a long-lived mostly-idle connection per user. In a traditional synchronous web server, this implies devoting one thread to each user, which can be very expensive.

To minimize the cost of concurrent connections, Tornado uses a single-threaded event loop.
This means that all application code should aim to be asynchronous and non-blocking because only one operation can be active at a time.

#### Asynchronous

* An asynchronous function returns before it is finished
* They do work in the background before triggering a future action
* Synchronous functions do everything they need to do before returning
* asynchronous functions by definition interact differently with their callers - there is no free way to make a syncronous function asyncronous
* systems like gevent use lightweight threads to offer performance comparable to asynchronous systems, but they do not actually make things asynchronous

Styles of asynchronous interfaces:

- Callback argument
- Return a placeholder (Future, Promise, Deferred)
- Deliver to a queue
- Callback registry (e.g. POSIX signals)

#### Blocking

* A function blocks when it waits for something to happen before returning.
* A function blocks for many reasons: network I/O, disk I/O, mutexes
* In fact, every function blocks, at least a little bit, while it is running and using the CPU (be careful with password hashing like `bcrypt`)

### More Info

More info in the docs:

* [Web framework](https://www.tornadoweb.org/en/branch4.5/webframework.html)
* [HTTP servers and clients](https://www.tornadoweb.org/en/branch4.5/http.html)
* [Asynchronous Networking](https://www.tornadoweb.org/en/branch4.5/networking.html)
* [Coroutines and concurrency](https://www.tornadoweb.org/en/branch4.5/coroutine.html)
* [Integrations with other services](https://www.tornadoweb.org/en/branch4.5/integration.html)
* [FAQ](https://www.tornadoweb.org/en/branch4.5/faq.html)

Sometimes it is hard to even get a `time.sleep()` working asynchronously as per the docs. The recommendation is to find a [async library for your task made for tornado](https://github.com/tornadoweb/tornado/wiki/Links)

## Source

* [Tornado 4.5 docs](https://www.tornadoweb.org/en/branch4.5/guide.html)
