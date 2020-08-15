---
author: ''
category: Servers
date: '2016-08-12'
summary: ''
title: Copy Your Ssh Key To Clipboard Fast
---
# Copy your SSH public Key to you clipboard fast

Install xclip

	sudo apt-get install xclip

Copy the ssh public key

	xclip -sel clip < ~/.ssh/id_rsa.pub


### Source

[Github copy ssh key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
