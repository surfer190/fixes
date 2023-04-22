---
author: ''
category: git
date: '2023-04-10'
summary: ''
title: Git Checkout a Tag
---

## How to Checkout a Remote Git Tag

Fetch tags from the remote:

    git fetch --all --tags

then checkout:

    git checkout tags/<tag> -b <branch>

eg:

    git checkout tags/v2.1.0 -b v2.1.0-branch

## Source

* [How to Checkout a git tag](https://devconnected.com/how-to-checkout-git-tags/)
