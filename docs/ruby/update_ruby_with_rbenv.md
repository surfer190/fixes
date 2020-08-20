---
author: ''
category: Ruby
date: '2015-03-16'
summary: ''
title: Update Ruby With Rbenv
---
#How to Update Ruby Versions on Linux with rbenv

##Update `ruby-build` as an rbenv plugin

`cd ~/.rbenv/plugins/ruby-build`

`git pull`

##Find Available versions

`rbenv install --list`

##Install version

`rbenv install 2.1.5`

##Set the ruby version to use globally

`rbenv global 2.1.5`

##Check ruby version

`ruby -v`

##Note: You need to Reinstall bundler for each version of Ruby you use

##Errors:

```
./libffi-3.2.1/.libs/libffi.a: could not read symbols: Bad value
```

##Solution: Install `libffi-dev`

```
sudo apt-get install libffi-dev
```

Sources: [makandracards](http://makandracards.com/makandra/25477-rbenv-how-to-update-list-of-available-ruby-versions-on-linux)
[digitalocean](https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-with-rbenv-on-debian-7-wheezy)
