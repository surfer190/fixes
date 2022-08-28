---
author: ''
category: Servers
date: '2018-08-19'
summary: ''
title: Setup A Vps Quickly
---
# Setup and secure a VPS Quickly

Quick guide to setting up a virtual private server quickly

After creating a server

1. Login as root

    ssh root@123.123.123.123

2. Update and upgrade

    sudo apt update
    sudo apt upgrade

3. Create a user

    adduser newuser

4. Add user to the `sudo` group

    usermod -aG sudo newuser

5. Become the new user

    sudo su newuser -

6. Create an ssh key

    ssh-keygen -t rsa -b 4096 -C "stephen@synergysystems.co.za"

7. logout of the server

    exit

8. On your local machine, copy your ssh key to the new user on the server

    ssh-copy-id newuser@123.123.123.123

9. Test log in

    ssh newuser@123.123.123.123

10. Disable password auth

    vim /etc/ssh/sshd_config

set

    PasswordAuthentication no

11. Reload ssh

    sudo systemctl reload sshd

12. Allow ssh and enable the [ufw (uncomplicated firewall)](https://help.ubuntu.com/community/UFW) firewall

    sudo ufw app list
    sudo ufw allow OpenSSH
    sudo ufw enable

## Add the server to your ssh config for easy ssh

    vim ~/.ssh/config

Add:

    Host newserver
        HostName 123.123.123.123
        Port 22
        User newuser
        IdentityFile ~/.ssh/id_rsa
        IdentitiesOnly yes

Re-source:

    source ~/.bashrc

Now you can ssh into the server with:

    ssh newserver

### References

* [Securing ubuntu 16.04 server](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)
* [Github create ssh key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
