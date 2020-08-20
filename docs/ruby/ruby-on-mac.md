---
author: ''
category: Ruby
date: '2019-09-23'
summary: ''
title: Ruby On Mac
---
# Ruby Mac Error Command Line tools

    Error running './configure --prefix=/Users/xxx/.rvm/rubies/ruby-2.5.1 --with-opt-dir=/usr/local/opt/libyaml:/usr/local/opt/readline:/usr/local/opt/libksba:/usr/local/opt/openssl@1.1 --disable-install-doc --enable-shared',
    please read /Users/xxx/.rvm/log/1568975665_ruby-2.5.1/configure.log
    There has been an error while running configure. Halting the installation.

when you check the tools it will say:

    xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist
    Use `sudo xcode-select --switch path/to/Xcode.app` to specify the Xcode that you wish to use for command line developer tools, or use `xcode-select --install` to install the standalone command line developer tools.
    See `man xcode-select` for more details.

Use this:

    sudo xcode-select --switch /Library/Developer/CommandLineTools

### Sources

* [Change crun developer path](https://stackoverflow.com/questions/11456918/change-xcrun-developer-path/26749000)