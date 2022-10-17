---
author: ''
category: Python
date: '2019-06-13'
summary: ''
title: Python Imports
---
# Python Imports and ImportErrors

Ever get this error:

    ImportError: attempted relative import beyond top-level package

or

    ValueError: attempted relative import beyond top-level package

or

    ImportError: attempted relative import with no known parent package

> Usually this is the case when you are in a directory that has a `test/` folder/module and a `utils/` folder. When you run the tests the from the parent of `test/` and `utils/` and some tests rely on code in `utils/`.

What the hell is going on....

There is some fundamentals we should understand:

> A Python module is just a file with Python code (a single python script)

> A Python package is a folder containing a `__init__.py` file (a collection of modules)

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

If you want to import `apples` from `red_grapes` you will struggle when calling your script from the `grapes` directory like this:

    cd grapes
    python red_grapes.py 

You can't do `from my_package import apples`, as that package is not on the python path.

    Traceback (most recent call last):
      File "red_grapes.py", line 1, in <module>
        from my_package import apples
    ModuleNotFoundError: No module named 'my_package'

You can't do a relative import `from ..my_package import apples` for the same reason, the parent directory is not added to the python path

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

or put this in your `__init__.py` file and remove all relative imports.

    import sys
    sys.path.append("..")

Even better is to structure your project of the form:

    /main
        __init__.py
        script.py
        my_package/
            class_file.py
            ...

## Is That really the solution?

> Relative imports use a module's name attribute to determine that module's position in the package hierarchy. If the module's name does not contain any package information (e.g. it is set to 'main') then relative imports are resolved as if the module were a top level module, regardless of where the module is actually located on the file system.

1. Just knowing what directory a file is in does not determine what package Python thinks it is in
2. There is a big difference between directly running a Python file, and importing that file from somewhere else

There are two ways to load a Python file:

* A top-level script: `python3 myfile.py`
* As a module: loaded as a module in another file with the `import statement`

> There can only be one top-level script run at a time

### Naming

When a file is loaded it is given the `__name__` attribute

* Loaded as a top level script is always named `__main__`
* Loaded as a module - its name is the filename, preceded by the names of any packages/subpackages of which it is a part. Eg. `package.subpackage1.moduleX`

> When a module is run as the top-level script, it loses its normal name and its name is instead `__main__`.

### Accessing a module NOT through its containing package

> the module's name depends on whether it was imported "directly" from the directory it is in or imported via a package

if you `import moduleX` from `package/subpackage1` - the name of `moduleX` will be `moduleX` and not `package.subpackage1.moduleX`

Python adds the current directory to its search path when the interpreter is entered interactively

> if a module's name has no dots, it is not considered to be part of a package

All that matters is what its name is, and its name depends on how you loaded it.

Relative imports use the module's name to determine where it is in a package

Running `from .. import foo` from `package.subpackage1.moduleX` it will import `package.moduleA`.
For this to work the module name must have at least as many dots as in the import statement.

if your module's name is` __main__`, it is not considered to be in a package. Its name has no dots, and therefore you cannot use from .. import statements inside it. If you do this you will get `ImportError: attempted relative import with no known parent package`

Relative imports will always fail when the module name is set to `__main__`

> Python will find the module in the current directory "too early" without realizing it is part of a package - Python adds the current directory to its search path when the interpreter is entered interactively

Also remember that when you run the interactive interpreter, the "name" of that interactive session is always __main__. Thus you cannot do relative imports directly from an interactive session. Relative imports are only for use within module files.

### Solutions

1. Run the module as is it were part of a package `python -m package.subpackage1.moduleX` - `-m` means load it as a module not a top-level script
2. Move the file you are running outside of the package directory

The full name is created with: `__package__ + __name__`

For any of this to work the `package` directory must be in the python search path `sys.path`

## My Solution

The most important thing to do is find out what `__name__` and `__package__` is.

So if you are running tests or just running a normal file do:

    print(__package__)
    print(__name__)

> If you are doing this in a test script make sure to run with `-s` for no capture eg. `nosetests -s`

So relative imports will work as expected when you are in a module:

    __name__: my_package.utils.tests.test_pools
    __package__: my_package.utils.tests

But if you run tests on the `utils` folder on its own you will get:

    __name__: tests.test_timespan
    __package__: tests

For the relative imports to work the `__package__` must not be a top-level / root.

We want it to look like:

    __name__: tests.test_timespan
    __package__: utils.tests

The important part is the `__package__` having more than 1 dot

## Interesting things

Python has a package called `threading` in the standard library.
If you have a folder or file called `threading` in your current path - python adds these modules first.
So you will get issues where `import threading` is importing your file/folder instead of the standard libraries.

Your expected package for the threading module may be: `my_package.utils.threading`

> `from __future__ import absolute_import` means that if you import string, Python will always look for a top-level `strin`g` module, rather than `current_package.string`. This is default behaviour on python2.7 and up.

### __package__

* empty string / `""` : Package is root or top level and run with `python -m current_module` or `import current_module`
* None: Module is run with the filename `python current_module.py`
* A dot seperated package name: when the module is a package: the `__package__` is the same as `__name__`, when it is not a package it is set to the parent package name `utils.current_module` for example.

### Omitting __init__.py

When `__init__.py` is present you are saying it is a regular package.
Then `__init__.py` is omitted it is a [namespace-packages](https://peps.python.org/pep-0420/).

> `unittest` will not search directories that do not have a `__init__.py`

## Sources

* [Relative imports for the billionth time](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912)
* [Import Traps](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)
* [Hitchhikers guide python imports](https://alex.dzyoba.com/blog/python-import/)
* [Dzyoba Python Imports](https://alex.dzyoba.com/blog/python-import/)
* [Understanding Python Imports](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355)
* [The import system](https://docs.python.org/3/reference/import.html)
* [whats-the-purpose-of-the-package-attribute-in-python?](https://stackoverflow.com/questions/21233229/whats-the-purpose-of-the-package-attribute-in-python)
* [Do not omit __init__](https://dev.to/methane/don-t-omit-init-py-3hga)
* [Relative imports python](https://gideonbrimleaf.github.io/2021/01/26/relative-imports-python.html)
