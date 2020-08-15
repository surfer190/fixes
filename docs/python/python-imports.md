---
author: ''
category: Python
date: '2019-06-13'
summary: ''
title: Python Imports
---
# Python Imports

There is some fundamentals we should understand:

> A Python module is just a file with Python code

> A Python package is a folder containing a `__init__.py` file

## Subfolders

The problem usually comes in when you are calling python modules or scripts from a subfolder.

For example, a project of this form:

    my_package/
        __init__.py
        apples.py
        grapes/
            __init__.py
            red_grapes.py
            white_grapes.py

If you want to import `apples` from `red_grapes` you will struggle when calling your script like this:

    python red_grapes.py 

You can't just `from my_package import apples`, as that package is not on the python path.

    Traceback (most recent call last):
      File "red_grapes.py", line 1, in <module>
        from my_package import apples
    ModuleNotFoundError: No module named 'my_package'

You can't just do a relative import `from ..my_package import apples` for the same reason, the parent directory is not added to the python path

    Traceback (most recent call last):
      File "red_grapes.py", line 1, in <module>
        from ..my_package import apples
    ValueError: attempted relative import beyond top-level package

You can run it as a package, not as a file:

    python -m red_grapes

But you will get the same errors:

    ModuleNotFoundError: No module named 'my_package'

and:

    ImportError: attempted relative import with no known parent package

### The Solution

You have to add the parent folder to the `sys.path`

    sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

Even better is to structure your project of the form:

    /main
        __init__.py
        script.py
        my_package/
            class_file.py
            ...


## Sources

* [Import Traps](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)
* [Hitchhikers guide python imports](https://alex.dzyoba.com/blog/python-import/)
* [Dzyoba Python Imports](https://alex.dzyoba.com/blog/python-import/)


