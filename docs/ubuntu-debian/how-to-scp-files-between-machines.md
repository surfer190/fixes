---
author: ''
category: Ubuntu-Debian
date: '2019-08-27'
summary: ''
title: How To Scp Files Between Machines
---
#How to Secure Copy (SCP) files between machines

> _Note: [Rsync](https://linux.die.net/man/1/rsync) is a more performant tool_

Copy from another machine to local

    scp <username>@<server>:/path/to/file.txt /local/dir

Copy from local machine to remote machine

    scp file.txt <username>@<server>:/path/to/directory

Copy full directory from remote host to local

    scp -r <username>@<server>:/path/to/directory /local/dir

Copy full directory from local to remote host

    scp -r <dirname> <username>@<server>:/path/to/directory

Copy files between 2 remote hosts from local

    scp <username>@<server1>:/some/dir/file.txt \ <username>@<server2>:/some/directory/
