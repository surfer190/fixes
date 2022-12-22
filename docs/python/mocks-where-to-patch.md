---
author: ''
category: Python
date: '2022-11-10'
summary: ''
title: Mocks - Where to Patch?
---

## Where to Patch?

A fundmental lesson to learn when it comes to mocks is...

[Where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)

For about 5 years, this mind was patching in the wrong place...

> `patch()` works by (temporarily) changing the object that a name points to with another one

There can be many names pointing to any individual object, so for patching to work you must ensure that you patch the name used by the system under test.

The basic principle is that you patch where an object is looked up, which is not necessarily the same place as where it is defined.

Let that be started again...

**Patch where an object is looked up (where it is imported)**

    a.py
        -> Defines SomeClass

    b.py
        -> from a import SomeClass
        -> some_function instantiates SomeClass

* If we use `patch()` to mock out `a.SomeClass` then it will have _no effect_ on our test
* module `b` already has a reference to the real `SomeClass`

The key is to patch out SomeClass where it is used (or where it is looked up):

    @patch('b.SomeClass')

However if in `b.py` it does:

    import a

    my_obj = a.SomeClass()

in this case, the functional patch would be:

    @patch('a.SomeClass')

## Sources

* [Python 3 docs: Unittest - Where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
