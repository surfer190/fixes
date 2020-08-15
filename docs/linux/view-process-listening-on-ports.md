---
author: ''
category: Linux
date: '2019-09-04'
summary: ''
title: View Process Listening On Ports
---
# View the processes listening on ports

## Nettools

Install net-tools

    sudo yum install net-tools

Check applications and what ports they are listening on

    netstat -ltnp

* `-l` - Only show listening sockets
* `-t` - Display tcp connections
* `-n` - Show numerical addresses
* `-p` - Show process id and name

## LSOF

Install:

    sudo apt install lsof

Use `lsof`:

For example check the port `8200`:

    lsof -i :8200

Returns:

    COMMAND   PID    USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    vault   13459 stephen    5u  IPv4 0xe0d88d9fe57581cf      0t0  TCP localhost:trivnet1 (LISTEN)

### Source

[Find out process listening on a port](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/)