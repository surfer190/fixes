---
author: ''
category: Ubuntu-Debian
date: '2016-12-14'
summary: ''
title: Setup Firewall on Ubuntu (UFW)
---
# How to setup firewall on Ubuntu

UFW stands for uncomplicated firewall.
It is a friendly interface to `iptables`.

Some commands:

    sudo ufw app list

    sudo ufw allow OpenSSH

    sudo ufw allow http

    sudo ufw allow https

    sudo ufw enable

## Source

* [UFW Ubuntu Help](https://help.ubuntu.com/community/UFW)