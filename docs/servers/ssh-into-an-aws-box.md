---
author: ''
category: Servers
date: '2015-09-20'
summary: ''
title: Ssh Into An Aws Box
---
# SSH (Secure Shell) into an Amazon Webserices box

1. Go through the motions register etc, selcted `ec2`

2. Click next make sure to download the `.pem` file

3. `chmod 400 <myfile>.pem`

4. `ssh -i <myfile>.pem ubuntu@default-dns.amazonaws.com`
