---
author: ''
category: Ubuntu-Debian
date: '2020-06-21'
summary: ''
title: Add Someone Elses Public Key To Remote Server
---
# How to Add Someone elses SSH public key to a remote server

```
cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
```

or using `ssh-copy-id`:

    ssh-copy-id -f -i <someones.pub> user@hostname

For AWS - where you are given an initial private key to ssh with:

    ssh-copy-id -f "-o IdentityFile my-private-key.pem" ubuntu@10.10.10.12

## Source

* [How to Add Someone elses public SSH key to a remote server](http://www.howtogeek.com/168147/add-public-ssh-key-to-remote-server-in-a-single-command/)
* [Why can't I ssh-copy-id to an ec2 isntance](https://superuser.com/questions/331167/why-cant-i-ssh-copy-id-to-an-ec2-instance)