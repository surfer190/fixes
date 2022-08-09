---
author: ''
category: Microservices
date: '2022-06-27'
summary: ''
title: gRPC
---

## gRPC Overview

> Important to note that gRPC is meant for a public endpoint - as it has support for authentication methods like OAuth. Whereas JSON, Nats and ZeroMQ have no authentication and are purely meant for service to service communication with no auth.

* A client application can directly call a method on a server application on a different machine as if it were a local object
* Easier distributed applications and services
* Service is defined: methods that can be called, parameters and return types
* Server implements interface and runs a gRPC server
* Client has a [stub](https://en.wikipedia.org/wiki/Stub_(distributed_computing)) providing the same methods as the server
* Language agnostic

gRPC client sends Proto request to gRPC server. gRPC sends proto response to gRPC client.

> The stub converts the parameters between clients and servers in a remote procedure call

### Why would I want to use gRPC?

* Low latency, highly scalable, distributed systems.
* Developing mobile clients which are communicating to a cloud server.
* Designing a new protocol that needs to be accurate, efficient and language independent.
* Layered design to enable extension eg. authentication, load balancing, logging and monitoring etc.

#### How does gRPC help in mobile application development?

> gRPC and Protobuf provide an easy way to precisely define a service and auto generate reliable client libraries for iOS, Android and the servers providing the back end. The clients can take advantage of advanced streaming and connection features which help save bandwidth, do more over fewer TCP connections and save CPU usage and battery life.

#### Whay is gRPC better than binary blob over HTTP/2?

* Interaction with flow-control at the application layer
* Cascading call-cancellation
* Load balancing & failover

### Working with Protocol Buffers

> gRPC can use protocol buffers as both its Interface Definition Language (IDL) and as its underlying message interchange format

* Protocol buffers is what gRPC uses as default

> You define gRPC services in ordinary proto files, with RPC method parameters and return types specified as protocol buffer messages

    // The greeter service definition.
    service Greeter {
      // Sends a greeting
      rpc SayHello (HelloRequest) returns (HelloReply) {}
    }

    // The request message containing the user's name.
    message HelloRequest {
      string name = 1;
    }

    // The response message containing the greetings
    message HelloReply {
      string message = 1;
    }

> gRPC uses protoc with a special gRPC plugin to generate code from your proto file

It is recommended to use `proto3` version with gRPC

### Core concepts, architecture and lifecycle

Kinds of services:

* `unary` - single request and response

        rpc SayHello(HelloRequest) returns (HelloResponse);

* `streaming` - single request with a sequence of responses

        rpc LotsOfReplies(HelloRequest) returns (stream HelloResponse);

* `client streaming` - client sends many messages and then waits for single server response

        rpc LotsOfGreetings(stream HelloRequest) returns (HelloResponse);

* `bi-directional streaming` - both sides send a stream of messages

### The API

* `protoc` compiles the classes and methods for the client and server
* server implements the methods - gRPC will handle the incoming request, service methods and encoded service responses
* client has a local stub (client) - the client calls methods on that local object. gRPC makes the request behind the scenes.

> The gRPC programming API in most languages comes in both synchronous and asynchronous flavors

### Lifecycles

#### Unary

1. Client calls stub - server notified with client metadata and request info
2. server can optionally send its own metadata
3. response generated and sent with status code and status message

#### Server streaming

Similar to unary but multiple messages are sent then once complete it sends the status message and status code.

#### Client streaming

Client sends multiple messages and optionally the server sends a status message and status code.

#### Bidirectional Streaming

Started by the client invoking a message. 

### Deadlines, Timeouts, Canceling and Terminations

* gRPC lets you set the length of time you are willing to wait before a RPC is terminated with a `DEADLINE_EXCEEDED`. 
* The client or server could terminate successfully while the other party fail.
* The client of server can cancel the RPC

### Metadata

Information about the call. Key value pairs. 

### Channels

* A gRPC channel provides a connection to a gRPC server on a specified host and port
* Clients can specify channel arguments to modify gRPC’s default behavior, such as switching message compression on or off.
* A channel has state, including connected and idle.

### Python Quickstart

Required packages are:

* `grpcio`
* `grpcio-tools` which installs `protobuf`

Generating the service from `.proto` files:

    python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/helloworld.proto

> Take note that we use `grpc_tools.protoc`

1. In `protos/greeter.proto`:

        syntax = "proto3";

        package greeter;

        // The greeting service definition.
        service Greeter {
            // Sends a greeting
            rpc SayHello (HelloRequest) returns (HelloReply) {}
            // Sends another greeting
            rpc SayHelloAgain (HelloRequest) returns (HelloReply) {}
        }

        // The request message containing the user's name.
        message HelloRequest {
            string name = 1;
        }

        // The response message containing the greetings
        message HelloReply {
            string message = 1;
        }

2. Then generate the clients / stubs
3. Create the server: `greeter_server.py`:

        """The Python implementation of the GRPC helloworld.Greeter server."""

        from concurrent import futures
        import logging

        import grpc
        import greeter_pb2
        import greeter_pb2_grpc


        class Greeter(greeter_pb2_grpc.GreeterServicer):
            def SayHello(self, request, context):
                return greeter_pb2.HelloReply(message='Hello, %s!' % request.name)

            def SayHelloAgain(self, request, context):
                return greeter_pb2.HelloReply(message='Hello again, %s!' % request.name)


        def serve():
            server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
            greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
            server.add_insecure_port('[::]:50051')
            server.start()
            server.wait_for_termination()


        if __name__ == '__main__':
            logging.basicConfig()
            serve()

4. Create the client: `greeter_client.py`:

        from __future__ import print_function

        import logging

        import grpc
        import greeter_pb2
        import greeter_pb2_grpc


        def run():
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = greeter_pb2_grpc.GreeterStub(channel)
                response = stub.SayHello(greeter_pb2.HelloRequest(name='Happy Chappy'))
                print("Greeter client received: " + response.message)
                response = stub.SayHelloAgain(greeter_pb2.HelloRequest(name='Happy Chappy'))
                print("Greeter client received: " + response.message)


        if __name__ == '__main__':
            logging.basicConfig()
            run()


5. Run the server: `python greeter_server.py` and then send client messages:

    $ python greeter_client.py
    Greeter client received: Hello, Happy Chappy!
    Greeter client received: Hello again, Happy Chappy!

#### Errors

##### Function not implemented or mismatch of message types expected

        grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
                status = StatusCode.UNIMPLEMENTED
                details = "Method not found!"
                debug_error_string = "{"created":"@1656325966.282133000","description":"Error received from peer ipv6:[::1]:50051","file":"src/core/lib/surface/call.cc","file_line":967,"grpc_message":"Method not found!","grpc_status":12}"

##### Server not running

        grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
                status = StatusCode.UNAVAILABLE
                details = "failed to connect to all addresses"
                debug_error_string = "{"created":"@1656326197.515755000","description":"Failed to pick subchannel","file":"src/core/ext/filters/client_channel/client_channel.cc","file_line":3261,"referenced_errors":[{"created":"@1656326197.515754000","description":"failed to connect to all addresses","file":"src/core/lib/transport/error_utils.cc","file_line":167,"grpc_status":14}]}"

##### Enable logging on server side

It was unsettling for me to see the clients get responses but for grpc to not report on that in the cli output.

You can run it with [environment variables](https://github.com/grpc/grpc/blob/master/doc/environment_variables.md):

    GRPC_VERBOSITY=DEBUG python greeter_server.py

However that did not respond when a client made a request.

### Deeper Dive with gRPC and Python

[Python's gRPC Implementation Docs](https://grpc.github.io/grpc/python/index.html)

[Guide](https://grpc.io/docs/guides/)

Some topics:

* Authentication
* Benchmarking
* Error Handling
* Performance Best practices

## Sources

* [gRPC Core Concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
* [Does gRPC vs NATS vs Kafka make any sense?](https://stackoverflow.com/questions/63418503/does-grpc-vs-nats-or-kafka-make-any-sense)