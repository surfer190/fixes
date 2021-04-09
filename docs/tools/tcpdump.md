---
author: ''
category: Tools
date: '2021-03-13'
summary: ''
title: TCPDump
---

# Using TCPDump

TCPDUmp lets you capture and inspect TCP packets tramitted from your device

Check available interfaces to capture traffic on:

    $ sudo tcpdump -D
    1.en0 [Up, Running]
    2.p2p0 [Up, Running]
    ...

Get your default route (to get the interface you are connected to net with)

    netstat -rn

Capture on all active interfaces:

    sudo tcpdump --interface any

Disable port and name resolution with `-nn`:

    sudo tcpdump -i en0 -nn

### Filtering

Protocol ICMP

    sudo tcpdump -i any -c5 icmp

Host (to and from 54.204.39.132)

    sudo tcpdump -i any -c5 -nn host 54.204.39.132

Source or Destinatino

    sudo tcpdump -i any -c5 -nn src 192.168.122.98
    sudo tcpdump -i any -c5 -nn dst 192.168.122.98

Complex

    sudo tcpdump -i any -c5 -nn src 192.168.122.98 and port 80

### Inspect packet content as ASCII

    sudo tcpdump -i any -c10 -nn -A port 80

## Saving to a File (-w)

    sudo tcpdump -i any -c10 -nn -w webserver.pcap port 80


## Source

* [Introduction TCPdump](https://opensource.com/article/18/10/introduction-tcpdump)