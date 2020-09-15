---
author: ''
category: Centos
date: '2020-09-15'
summary: ''
title: Installing Pandoc on CentOS
---

## Installing Pandoc on CentOS

Pandoc is not in yum repos, the release with the binary needs to be downloaded from their [pandoc releases page](https://github.com/jgm/pandoc/releases)

On centos:

    cd /opt
    wget https://github.com/jgm/pandoc/releases/download/2.10.1/pandoc-2.10.1-linux-amd64.tar.gz
    tar -xvf pandoc-2.10.1-linux-amd64.tar.gz

Symlink a directory from the path to the binary just extracted:

    ln -s /opt/pandoc-2.10.1/bin/pandoc /usr/bin/pandoc

Most likely xetex is also needed to for example export `pdf` or `epub` with `nbconvert`, this is in the repos:

    yum install texlive-xetex

### Source

* [How to install pandoc on CentOS](http://tutorialspots.com/how-to-install-pandoc-on-centos-4902.html)



