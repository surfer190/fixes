---
author: ''
category: Python
date: '2023-01-04'
summary: ''
title: Importing a module gives module has no attribute
---

## Python importing a module gives module has no attribute

An unexpected error was raised when importing a package and trying to use a module inside the imported package.

    AttributeError: module 'system_utilities' has no attribute 'events'

This is an error of the standard form:

    AttributeError: module 'x' has no attribute 'y'

The strange thing was one expected it work. Here is the code in `run.py`:

    import system_utilities
    system_utilities.events.NewEvent()

The folder structure:

    run.py
    system_utilities/
        __init__.py
        events.py

> The strange thing is that compared to a package import like `import datetime` you can access attributes and methods (or functions) levels down...eg: `datetime.datetime.now()`

## Confusing a Module and a Package

A module is simply a file. Above, `events.py` is a module.

A package is a folder (directory) of modules (file). It is a name (a namespace). Python knowns it is a package due to the presence of a `__init__.py` (package constructor) file inside. Above, `system_utilities` is a package.

`import datatime` is importing a module - in the standard library of python that corresponds with a file called `datetime.py`.

`import urllib` on the other hand imports a package from the standard library. 

> Interesting to note that most things are implemented as straight modules in teh python standard library - something to apply to simplify our own code?

## Module vs Package

* All attributes in a module are imported by default.
* All modules in a package are not imported by default.

Module:

    >>> import datetime
    >>> datetime.datetime.now()
    datetime.datetime(2023, 1, 5, 12, 38, 3, 320737)

package (without automatic import):

    >>> import urllib
    >>> urllib.request.urlopen('https://example.org')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: module 'urllib' has no attribute 'request'

package (with automatic import):

    >>> import unittest
    >>> unittest.case.TestCase()
    <unittest.case.TestCase testMethod=runTest>

In the above example `urlib` has an `__init__.py` that is empty. In this case you must import the modules directly from within the package.

In the case of `unittest` the `__init__.py` file does the imports and exposed the string names available with the package is run:

    __all__ = ['TestResult', 'TestCase', 'IsolatedAsyncioTestCase', 'TestSuite',
            'TextTestRunner', 'TestLoader', 'FunctionTestCase', 'main',
            'defaultTestLoader', 'SkipTest', 'skip', 'skipIf', 'skipUnless',
            'expectedFailure', 'TextTestResult', 'installHandler',
            'registerResult', 'removeResult', 'removeHandler',
            'addModuleCleanup']

    # Expose obsolete functions for backwards compatibility
    __all__.extend(['getTestCaseNames', 'makeSuite', 'findTestCases'])

    __unittest = True

    from .result import TestResult
    from .case import (addModuleCleanup, TestCase, FunctionTestCase, SkipTest, skip,
                    skipIf, skipUnless, expectedFailure)





