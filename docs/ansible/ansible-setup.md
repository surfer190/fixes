---
author: ''
category: Ansible
date: '2019-02-05'
summary: ''
title: Ansible Setup
---
### Install Ansible

    sudo apt-get update
    sudo apt-get install python-pip python-devel
    sudo pip install ansible

### Basics

#### Inventory File

just like a `hosts` file the inventory file matches ip addresses and domain names to groups

Default place is:

    /etc/ansible/hosts

eg.

    [example]
    www.example.com

or with a non-standard (22) port

    www.example.com:2222

> Ansible assumes you are using key-based (password less) login

#### Running simple commands

    ansible example -m ping -u [username]

Just pings the server.

To check memory usage run:

    ansible example -a "free -m" -u [username]
