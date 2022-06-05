---
author: ''
category: Python
date: '2017-09-26'
summary: ''
title: Create An Md5 Hash
---
# Create an MD5 Hash with Python

Import [Hashlib](https://docs.python.org/3/library/hashlib.html)

    >>> import hashlib

Create an object of type `<type '_hashlib.HASH'>`

    >>> m = hashlib.md5()

Add a byte-string with the `update` method

    >>> m.update(b"email@example.com")

Check the digest

    >>> m.digest()
    b'VX\xff\xcc\xee\x7f\x0e\xbf\xda+"b8\xb1\xebn'

Check the hex digest

    >>> m.hexdigest()
    '5658ffccee7f0ebfda2b226238b1eb6e'

### Source

* [Hashlib Python 3.6](https://docs.python.org/3/library/hashlib.html)
