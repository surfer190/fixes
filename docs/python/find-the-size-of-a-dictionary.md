---
author: ''
category: Python
date: '2022-12-01'
summary: ''
title: Find the Size of a Python Dictionary
---

### Find the Size of a Python Dictionary

This is one way that returns the number of bytes _I think_...

    import pickle

    dumped = _my_python_object_

    size_estimate = len(pickle.dumps(dumped))

### Sources

* [Stackoverflow.com: Determine the size of an object in python](https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python)
* [Medium.com: Find the size of a json object in python](https://medium.com/@r_chan/tips-tricks-how-to-find-a-json-object-size-in-python-8c1f6d208dc1)
