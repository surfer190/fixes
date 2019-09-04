# Unix Sockets

An inter-process communication method allowing bi-directional data exchange between processes running on the same machine

## Ip Sockets

IP sockets are a method for allowing communication between processes over a network. In some cases you can use a loopback interface to talk with processes running on the same computer.

Unix domain sockets know they are on the same system, so they can avoid some checks and operations like routing.
So better to use on the same host over ip sockets.

Unix domain sockets however are subject to file system permissions, while TCP sockets can only be controlled on packet filtering.

## Sources

* [Difference between Unix socket and TCP/IP socker](https://serverfault.com/questions/124517/whats-the-difference-between-unix-socket-and-tcp-ip-socket)


