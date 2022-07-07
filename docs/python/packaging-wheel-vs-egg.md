---
author: ''
category: Python
date: '2022-07-05'
summary: ''
title: Packaging - Wheel vs Egg
---

Wheel and Egg are both packaging formats that aim to install artifacts without building or compilation

* The Egg format was introduced by setuptools in 2004
* The Wheel format was introduced by [PEP 427](https://peps.python.org/pep-0427/) in 2012.

### Egg

* Python eggs are an older distribution format for Python
* An egg file is basically a zip file with a different extension. Python can import directly from an egg.
* The `setuptools` package is required

### Wheel

Wheel is the standard.

Wheel:

* Has an official PEP
* is a distribution package: A versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release. Egg was a distribution and a runtime instllation format (if left zipped)
* does not include `.pyc` files - if there is no compiled extensions the package can be universal
* Uses a [PEP 376](https://peps.python.org/pep-0376/) compliant `.dist-info` folder (egg uses `.egg-info`)
* Has a richer file naming convention to indicate compatiblity with language versions, ABIs (Application Binary Interface) and system architectures
* is versioned
* organised by [sysconfig path type](https://docs.python.org/2/library/sysconfig.html#installation-paths) - so it is easier to convert to other formats

> With a `.egg`: The code is unzipped at runtime and cannot be inspected with an IDE





## Sources

* [Python101: The Python Egg](https://python101.pythonlibrary.org/chapter38_eggs.html)
* [Python Packaging: Wheel vs Egg](https://packaging.python.org/en/latest/discussions/wheel-vs-egg/)