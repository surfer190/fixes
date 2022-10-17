---
author: ''
category: Mac
date: '2019-07-22'
summary: ''
title: Where Binaries Should Stay
---
# Where should mac binaries go

I recently [downloaded vault](https://learn.hashicorp.com/vault/getting-started/install) (the binary) and was unsure where to put it for it to automatically be available on the `echo $PATH`

The documents they recommended were also shit.

So I googled and found that local binaries should go in: `/usr/local/bin` which is already part of the path

All I needed to do was:

    cp ~/Downloads/vault /usr/local/bin

and the binary became available

## Source

* [Conventional places binaries should exist on OSX](https://superuser.com/questions/7150/mac-os-x-conventional-places-where-binary-files-should-live)
