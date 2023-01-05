---
author: ''
category: Mac
date: '2019-07-22'
summary: ''
title: Where Binaries Should Stay
---
# Where should mac binaries go

Recently [downloaded vault](https://learn.hashicorp.com/vault/getting-started/install) which is a simple binary. Unsure where to put it for it to be available on the `echo $PATH` and not much help from the docs...

A search was initiated and found that local binaries should go in: `/usr/local/bin` which is already part of the path.

One can do:

    cp ~/Downloads/vault /usr/local/bin

and the binary became available.

Another option is using `install`:

    sudo install -m 0755 ~/Downloads/vault /usr/local/bin/

## Source

* [Conventional places binaries should exist on OSX](https://superuser.com/questions/7150/mac-os-x-conventional-places-where-binary-files-should-live)
