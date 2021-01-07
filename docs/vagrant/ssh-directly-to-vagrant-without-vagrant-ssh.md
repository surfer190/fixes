---
author: ''
category: Vagrant
date: '2019-08-12'
summary: ''
title: Ssh Directly To Vagrant Without Vagrant Ssh
---
# How to SSH directly to a vagrant box without using vagrant ssh

You know you can ssh to vagrant with:

    vagrant ssh

which is cool and all, but it doesn't work like that in the real world.

The first thing you should do is ensure your vagrant box has its own private internal ip, which you can set in the vagrantfile:

    config.vm.network "private_network", ip: "192.168.33.10"

Now we need to know how vagrant is doing the sshing

    vagrant ssh-config

Now we know the user and the private key used to connect

    $ vagrant ssh-config
    Host default
    HostName 127.0.0.1
    User vagrant
    Port 2222
    UserKnownHostsFile /dev/null
    StrictHostKeyChecking no
    PasswordAuthentication no
    IdentityFile /Users/stephen/lxd-terraform/.vagrant/machines/default/virtualbox/private_key
    IdentitiesOnly yes
    LogLevel FATAL

> Note: The port 2222 is not actually being used, it is 22

So we can create the following ssh connection:

    ssh vagrant@192.168.33.10 -i .vagrant/machines/default/virtualbox/private_key

This will hopefully connect you to your host

> This won't work if you are tunneling via another connection as you box is not connected to the internet

Ensure virtualbox and vagrant are installed folow [this guide](https://github.com/Juniper/vqfx10k-vagrant/blob/master/INSTALL.md)

    vagrant box add juniper/vqfx10k-re 
    vagrant box add juniper/vqfx10k-pfe

    git clone https://github.com/Juniper/vqfx10k-vagrant.git
    cd vqfx10k-vagrant/full-2qfx
    vagrant up




## Sources

* [How to ssh to vagrant without actually running “vagrant ssh”?](https://stackoverflow.com/questions/10864372/how-to-ssh-to-vagrant-without-actually-running-vagrant-ssh)