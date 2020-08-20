---
author: ''
category: Apple
date: '2015-09-20'
summary: ''
title: Mac Osx Homebrew
---
# Mac OSX Homebrew and Casks

[`Homebrew`](http://brew.sh) is a package manager for Mac OSX.

There are also things called casks which as far as I can tell are full on applications (gui), while normal homebrew packages are just command line utils.

## Install Homebrew

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Searching for a Homebrew Package
```
brew search <term>
```

#### Searching for a Homebrew Cask

```
brew cask search <term>
```

###### Source:

[OSX Yosemite: Clean Install Gist](https://gist.github.com/surfer190/dc2d98049f998939c4c2)
[SuperUser Homebrew Info](http://superuser.com/questions/390191/where-can-i-find-a-list-of-all-formulas-available-for-homebrew)
