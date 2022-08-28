---
author: ''
category: Networking
date: '2019-06-13'
summary: ''
title: Centos Routes
---
# View Routes

View all routes

    netstat -rn

Will return an ip routing table

    Kernel IP routing table
    Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
    0.0.0.0         192.168.0.1     0.0.0.0         UG        0 0          0 eth0
    0.0.0.0         192.168.0.1     0.0.0.0         UG        0 0          0 eth0
    192.168.0.0     0.0.0.0         255.255.255.0   U         0 0          0 eth0
    192.168.0.1     0.0.0.0         255.255.255.255 UH        0 0          0 eth0

Try to telnet or ping a host

    telnet 196.41.6.162 389

Add a route

    route add -net 196.41.6.162 netmask 255.255.255.255 gw 10.200.1.249

Delete a route

    route del -net 196.41.6.162 netmask 255.255.255.255 gw 10.200.1.249

