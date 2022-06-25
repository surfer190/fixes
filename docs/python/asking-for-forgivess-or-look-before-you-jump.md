---
author: ''
category: Python
date: '2022-06-22'
summary: ''
title: Asking for Forgiveness or Look Before you Jump
---

# Asking for Forgiveness or Look Before you Jump (Leap)

These 2 python concepts were introduced to me when reading an article on [database concurrency from Haki Benita](https://hakibenita.com/django-concurrency):

* [EAFP](https://docs.python.org/3.11/glossary.html#term-EAFP) - Easier to ask for forgiveness than permission
* [LBYL](https://docs.python.org/3.11/glossary.html#term-LBYL) - Look before you leap

These concepts seems to apply to life and developing in a business as well but let us look at it from a concurrency point of view.

### Look Before you Leap (LBYL)

From the python glossary:

    Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups.

    This style contrasts with the EAFP approach and is characterized by the presence of many if statements.

    In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the looking” and “the leaping”. For example, the code, if key in mapping: return mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. This issue can be solved with locks or by using the EAFP approach.

The `Time-of-Check to Time-of-Use` problem is mentioned 

### Easier to Ask for Forgiveness than Permission (EAFP)

From the python glossary:

    Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.

Essentially you are attempting to do something - and only if it is a problem will you look at corrective action.

I think this ties in with premature optimisation - you think you might face a problem - but then you never do...

The EAFP method is deamed more pythonic.

Javascript and Java are languages that prefer the LBYL method. I see it as a negative and risk sensitive way to look at problem - you always expect there to be problems at the expense of the 99% of the time there are no problems.


## Sources

* [database concurrency from Haki Benita](https://hakibenita.com/django-concurrency):
* [python glossary](https://docs.python.org/3.11/glossary.html)