---
author: ''
category: C
date: '2015-09-13'
summary: ''
title: The C Programming Language Summarised
---
## How to Access the Python Docs Offline

It is too easy these days...just type what you want into a search engine eg. `python concurrency` or `python debugger` and the python docs will show up.

Unfortunately it is often the third or fourth result item.

The official python docs are always the recommended source - straight from the horses mouth. Instead of another person abstraction or interpretation.

Reading the docs from scratch I believe is an extremely good thing to do and skill to build. Instead of fast tracking with videos and short tutorials that often cut corners.

So how can we access the docs without a browser and using a third party tracking our searches?

There are 3 methods:

* Download the docs as: `html`, `epub`, `pdf`, `windows help` or `plain text`
* `pydoc` - Command line utility - The python documentation tool
* `help()` - Interactive (in python repl)  help utility

### Download the Docs

Go to [https://docs.python.org/3/download.html](https://docs.python.org/3/download.html) and download the file:

* HTML
* PDF
* Text
* EPUB
* Windows CHM

> HTML is the best to navigate

> Reading and exploring the docs like this is the best. Yu will find tutorials, easter eggs and cookbooks that are key and can fast forward you years of plodding along

### Pydoc

Run pydoc as a GUI or in the browser with `-g` (deprecated in python 3.2)

    python3.9 -m pydoc -g

or run python docs locally on port `4444`

    python3.9 -m pydoc -p 4444

Go to: [http://localhost:4444/](http://localhost:4444/) and the docs will be there

> This will actually build docs for python and anything in the current directory with doc strings etc.

You can also access docs from the cli with:

    python3.9 -m pydoc <topic>
    # Eg.
    python3.9 -m pydoc dict

### Help

Enter a python repl with `python3` (or something similar)

Then get help:

    help('dict')

and you will receive...

