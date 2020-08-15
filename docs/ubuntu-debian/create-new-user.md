---
author: ''
category: Ubuntu-Debian
date: '2016-12-14'
summary: ''
title: Create New User
---
# How to create a new user with sudo priveleges on Ubuntu 16

1. Log in as root

2. Create the user

    `adduser newuser`

3. See user's groups

    `groups newuser`

4. Add to sudo group

    `usermod -aG sudo newuser`

5. Become `newuser`

    `sudo su newuser - `

6. Create SSH key

    `ssh-keygen`

7. Logout and copy your ssh key to server

    `ssh-copy-id ubuntu@your-server-ip`

    Use password to copy it over

8. Disable password authentication

   sudo vim /etc/ssh/sshd_config

   PasswordAuthentication no

   sudo systemctl reload ssh
