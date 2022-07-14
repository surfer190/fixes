---
author: ''
category: Code
date: '2022-07-14'
summary: ''
title: Remote Dev Debugging with SSHD
---

## Remote Dev Debugging with SSHD

The [remote debugging from vscode does not work on the open source VS Codium](https://github.com/VSCodium/vscodium/issues/240). They are closed source.

No matter. There was mention of mounting a [remote file system with `sshfs`](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)

### Getting started with SSHFS

Easiest is to install on linux hosts:

    sudo apt install sshfs

Installing on other systems:

* Mac can use [Macfuse](https://github.com/osxfuse/osxfuse)
* Windows can use [sshfs-win](https://github.com/winfsp/sshfs-win)

> With the mac version you have to enable system extensions
