---
author: ''
category: Python
date: '2017-09-10'
summary: ''
title: Setting Kwargs To An Instance
---
# How to set kwargs as attributes of an instance

Use the `setattr` function

class Test():

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)

## Use

    >>> test = Test(name="surfer", age=5)
    >>> test.name
    >>> surfer

## Only want specific keyword args use

        self.species = kwargs.get("species")

## The Sneakier Way

Every object has an attribute called `__dict__`, the dictionary representation of writable attributes of an object.

But `__dict__` is suppsed to be read only but you can do...

        class Test():

            def __init__(self, **kwargs):
                self.__dict__.update(kwargs)