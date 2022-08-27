---
author: ''
category: Azure
date: '2016-09-27'
summary: ''
title: Azure Linux Vm Active Directory
---
# Setup to authenticate against active directory to login via SSH to Linux Azure VM

1. Login to Linux
2. Install node and npm

        sudo apt-get install npm
        sudo ln -s /usr/bin/nodejs /usr/bin/node

3. Follow the steps on [Buredo Aad Login](https://github.com/bureado/aad-login)
4. Create a active directory user on the ad server with crednetials in `aad-login.js`
5. Create user on server (`linuxguy` is on active directory)

        sudo useradd -m linuxguy

6. Allow password login `/etc/ssh/sshd_config`: `PasswordAuthentication yes`
6. Login to server

        ssh -l linuxguy { server_ip}
