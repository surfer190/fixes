---
author: ''
category: Linux
date: '2019-06-13'
summary: ''
title: Python Linux Exit Codes
---
# Python Linux Exit Codes

Sometimes you need to create scripts that give an exit status code to the calling program.
Here is some info with [exit codes with special meaning](http://tldp.org/LDP/abs/html/exitcodes.html)

At it's code:

* `0` - means successful
* `1 - 255` - means failure / error

In python that is done using [`sys.exit()`](https://docs.python.org/2/library/sys.html#sys.exit):

    import sys
    # fail
    sys.exit(1)

