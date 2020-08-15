---
author: ''
category: Python
date: '2017-09-11'
summary: ''
title: Writing Better Python
---
# Writing Better Python

Whenever you build something big, it usually gets messy.
Python has some tools to help

## Pep

`pep` stands for python enhancement proposal.

Anyone can submit a pep and they contain a single idea to implement in python

### Important peps

pep8 - how python code should look (don't live by the rule, it is for preferences)

**Avoid single letter variable names** as this causes problems with the python debugger

You can use `flake8 <script>` to check pep8 rules

pep20 - the zen of python

    >>> import this

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

**Coding should be pleasant**

## Docstring

A `docstring` is a string at the beginning of a class, method or function that documents what that bit of code does

You should never have to read the source code to find out what a library does, that is the job of documentation

Enclosed in 3 quote marks (triplequotes)..`doc.py`

    def does_something(my_var):
        """Takes one argument and does something based on the type
        If arg is a string, returns arg * 3
        If arg is a int or float, returns arg + 10
        """
        ....


then check help

    help(doc.does_something)

returns the info

Better to use them as docstring and not comments, use `#` for comments

## Logging

        import logging

        logging.info("You won't see this")
        logging.warn("Oh no")

But this prints the `warn` out to standard output

Some old packages use camelCase. 

        logging.basicConfig(filename='game.log',level=logging.DEBUG)

Now logs into filename (relative)

Level specifies what logging to pay attention to

### Logging Levels

CRITICAL
ERROR
WARNING - Keep track of questionable things
INFO - Monitoring
DEBUG - Info about running of app
NOTSET

Also remember to log errors in the `Except` block

## Debugging

Track the state of variables at any given time

You can actually go inside the script and see the state of variables

You can use the `Python Debugger`

        import pdb

To set a breakpoint / trace, use:

        pdb.set_trace()

        $ python ar.py
        > /Users/surfer190/projects/object-oriented-python/test/ar.py(7)<module>()
        -> del my_list[3]
        (Pdb)

The `7` and **next** line tells us the line and code that will be run

It works just like python shell and you can inspect variables

### Commands

* Use `next` or `n` to run the next line
* `q` - quit
* `c` - continue running as normal

**Important to remove pdb when you are done**

Most of the time you wil use:

        import pdb;pdb.set_trace()

The only time you can use a `;` in python

[Other python debugger commands](https://docs.python.org/3/library/pdb.html?highlight=pdb#debugger-commands)

