---
author: ''
category: Python
date: '2023-05-01'
summary: ''
title: Joblib and Memoization
---
## Memoization

The memoization pattern - is a caching method.
It caches the result of inputs so when the same inputs are used again the calculation/work is skipped and the result is produced.

To be remembered...

A good example of this in the python standard library is [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)

Caveats - ideally you want to memoize functions that are deterministic

## Joblib

[joblib](https://joblib.readthedocs.io/en/latest/index.html) is a python library to provide lightweight pipelining.
Running multiple jobs in parrallel for large datasets specifically for numpy arrays.

It appears to be a tool more focused on the data and analytics processing side of things - instead of real-time transactional processing.


## Sources

* [Dan Bader - Python Memoization](https://dbader.org/blog/python-memoization)
