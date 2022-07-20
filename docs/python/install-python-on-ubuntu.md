---
author: ''
category: Python
date: '2015-01-25'
summary: ''
title: Install Python On Ubuntu
---
# Install Python on Ubuntu

In 2015, I suggested this:

```
sudo apt-get install python-pip python-dev
```

**Now I think it is probably better to install python from source on ubuntu**

It is best to install from source. 

## The Correct Way 

1. Install expected system C packages and libraries

    sudo apt install software-properties-common build-essential \
    libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev \
    tk-dev libgdbm-dev libc6-dev libbz2-dev libncurses-dev libgdbm-dev \
    libpcap-dev libexpat1-dev libffi-dev liblzma-dev libgdbm-compat-dev

2. Go to [Python Downloads](https://www.python.org/downloads/source/)

3. Download the source tarball and unzip

    cd /opt
    wget https://www.python.org/ftp/python/3.10.5/Python-3.10.5.tar.xz
    tar xzf Python-3.10.5.tar.xz
    
4. Follow instructions in the `README.rst`

    ./configure
    make
    sudo make install # or: sudo make altinstall

5. Python should now be on your path as:

    python3.10
