---
author: ''
category: Datascience
date: '2017-10-29'
summary: ''
title: Ipython
---
## IPython

[Interactive python](http://ipython.org/)

Enter `ipython` by typing `ipython` in terminal

You can use print:

    In [1]: print("Hello world")
    Hello world

Get help with `<function_name>?`:

    In [2]: print?
    Docstring:
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    Type:      builtin_function_or_method

[IPython Documentation](http://ipython.org/ipython-doc/dev/index.html) and [Jupyter Notebooks Documentation](http://jupyter.readthedocs.io/en/latest/content-quickstart.html)

You can run a script from ipython with:

    In [1]: %run my_file.py
    Hello World

You can then explore the available variables

    In [2]: s
    Out[2]: 'Hello World'

View all available variables with:

    In [3]: %whos
    Variable   Type    Data/Info
    ----------------------------
    s          str     Hello World

#### Tips and Tricks

**Command History**

Tap up and down of the keyboard to access previous commands

**Tab completion**

After typing an object name you can type `<TAB>` to access available methods

**Magic Functions**

Start with the `%` character

* `%cd` - change currect directory
* `%cpaste` - paste code from other websites
* `%timeit` - time the execution of a short snippet of code
* `%debug` - enter post mortem debugger, which opens `ipdb` so you can use `locals()` to view local variables

You can pretty much use alot of standard linux commands: `ls`, `cp`, `rm`

which you view with `%quickref`

#### Sources

* [Scipy lectures](http://www.scipy-lectures.org/)
