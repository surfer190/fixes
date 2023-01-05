---
author: ''
category: Python
date: '2016-05-10'
summary: ''
title: Getting Help Using Pydoc And Help
---
# Getting Help with Documentation - Using Pydoc and help

## Pydoc

You use pydoc in the same way you use `man` on linux

Example:

  `pydoc raw_input`

Output:

    raw_input(...)
      raw_input([prompt]) -> string

      Read a string from standard input.  The trailing newline is stripped.
      If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
      On Unix, GNU readline is used if enabled.  The prompt string, if given,
      is printed without a trailing newline before reading.

You can also view a specific function or a package:

  `pydoc file.seek`

It can also be run as a function:

    python3.9 -m pydoc functools.cache

## Help

To use help you need to be inside the python shell

`python`

Then:

`>>>> help(range)`

returns:

  range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers

    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

## Sources

* [youtube: anthonywritescode - lrucache](https://www.youtube.com/watch?v=sVjtp6tGo0g)