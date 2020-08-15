---
author: ''
category: Python
date: '2019-07-17'
summary: ''
title: Dictionaries
---
# Python dictionaries

Everything (most things) in python is built around a dictionary.

A class is a `dict`

    from requests import Session
    
    session = Session()
    session.headers.update({'token': 'tabalubbahuptaga'})
    
To get the dictionary representation you can use `var()`:

    >>> vars(session)
    {'headers': {'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'token': 'tabalubbahuptaga'},
    'auth': None,
    'proxies': {},
    'hooks': {'response': []},
    'params': {},
    'stream': False,
    'verify': True,
    'cert': None,
    'max_redirects': 30,
    'trust_env': True,
    'cookies': <RequestsCookieJar[]>,
    'adapters': OrderedDict([('https://',
                <requests.adapters.HTTPAdapter at 0x10ed56b00>),
                ('http://', <requests.adapters.HTTPAdapter at 0x10ee1d518>)])}

It returns the same content as `session.__dict__`

In `python 2.7` dictionaries were big. The order is scrambled but deterministic...every python3.7 will return the same order.

In `python 3.5` the key sharing dictionary was introduced, where dictionaries that shared keys were not duplicated. Each time python started the hash changes and dict keys are `randomized`

In `python 3.6` dictionaries got compacted and are now ordered.

## Source

* [Modern Dictionaries talk by Raymond Hettinger](https://www.youtube.com/watch?v=p33CVV29OG8)
