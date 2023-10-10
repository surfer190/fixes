---
author: ''
category: Python
date: '2023-08-30'
summary: ''
title: Python Sockets How To
---

# Python Sockets How To

Terms:

* INET - IPv4 Socket
* STREAMING - TCP Socket

Types of sockets:

* "client" socket - an endpoint of a conversation. A client application like a browser uses client sockets exclusively.
* "server" socket - a switchboard operator. A web server uses both server client sockets.

Sockets are a form of inter process communication (IPC) - for cross-platform communication they are the only game in town.

Invented in BSD - spread quickly as INET (IPv4 Sockets) made communicating with devices around the world easy

## Example

When you click a link in browser, the browser does:

    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect(("www.python.org", 80))

* When the `connect` completes, the socket `s` can be used to send in a request for the text of the page.
* The same socket will read the reply, and then be destroyed.
* Client sockets are normally only used for one exchange (or a small set of sequential exchanges).

On the server side:

    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind((socket.gethostname(), 80))
    # become a server socket
    serversocket.listen(5)

* `socket.gethostname()` is used so the socket is available to the outside world
* `s.bind(('', 80))` - specifies the socket is reachable by any address
* `s.bind(('127.0.0.1', 80))` - specifies the socket is reachable only by loopback
* `serversocket.listen(5)` - queue up 5 connections before refusing outside connections

> low number ports are usually reserved for “well known” services (HTTP, SNMP etc). If you’re playing around, use a nice high number (4 digits).

Now that the socket is created on the webserver - enter the mainloop:

    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
        ct = client_thread(clientsocket)
        ct.run()

3 ways the loop could work:

* dispatching a thread to handle clientsocket
* create a new process to handle clientsocket
* restructure this app to use non-blocking sockets

> It doesn’t send any data. It doesn’t receive any data. It just produces “client” sockets.

IPC tip:

> If you need fast IPC between two processes on one machine, you should look into pipes or shared memory. If you do decide to use `AF_INET` sockets, bind the “server” socket to `localhost`. On most platforms, this will take a shortcut around a couple of layers of network code and be quite a bit faster.

### Using a Socket

A client and server socket are identical - they are peer-to-peer. There is no rules. The designer must decide on the ettiquette.

There are 2 verbs: `send` and `recv`, or you can transform your client socket into a file-like beast and use `read` and `write`.

> Remember to `flush` on file sockets

`send` and `recv` operate on the network buffers - they do not necessarily handle all the bytes you hand them because their major focus is handling the network buffers

In general, they return when the associated network buffers have been filled (`send`) or emptied (`recv`)

When a `recv` returns 0 bytes, it means the other side has closed (or is in the process of closing) the connection. You will not receive any more data on this connection. Ever.

A protocol like HTTP uses a socket for only one transfer. The client sends a request, then reads a reply. That’s it. The socket is discarded. This means that a client can detect the end of the reply by receiving 0 bytes.

There is no EOT (end of transfer) on a socket.

Fundamental truths, messages must be:

* fixed length
* be delimited
* indicate how long they are
* end by shutting down the connection








## Source
* [Python 3 docs: sockets howto](https://docs.python.org/3/howto/sockets.html)