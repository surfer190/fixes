---
author: ''
category: Python
date: '2022-07-30'
summary: ''
title: Python Gotchas
---

## Python Gotchas

### Do Not Name Modules after Python Built-in

You may get an error like this:

    Traceback (most recent call last):
    File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 183, in _run_module_as_main
        mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
    File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 142, in _get_module_details
        return _get_module_details(pkg_main_name, error)
    File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 109, in _get_module_details
        __import__(pkg_name)
    File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/unittest/__init__.py", line 59, in <module>
        from .case import (TestCase, FunctionTestCase, SkipTest, skip, skipIf,
    File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/unittest/case.py", line 6, in <module>
        import logging
    File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/logging/__init__.py", line 210, in <module>
        _lock = threading.RLock()
    AttributeError: module 'threading' has no attribute 'RLock'

It will then say:

    Exception ignored in: <module 'threading' from '/my/python/project/threading/__init__.py'>
    AttributeError: module 'threading' has no attribute '_shutdown'

This means the standard library is using my local version of threading.
It is a naming conflict.
You probably have a folder with a `__init__.py` inside it that is called `threading/` or you have a file called `threading`.

> Generally, its not a good idea to name python scripts after builtin scripts.

You can get a list of `keywords` and `builtins` with:

    import keyword
    >>> keyword.kwlist
    ['False',
    'None',
    'True',
    '__peg_parser__',
    'and',
    'as',
    'assert',
    'async',
    'await',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'not',
    'or',
    'pass',
    'raise',
    'return',
    'try',
    'while',
    'with',
    'yield']

    import builtins
    dir(builtins)

    ['ArithmeticError',
    'AssertionError',
    'AttributeError',
    'BaseException',
    'BlockingIOError',
    'BrokenPipeError',
    'BufferError',
    'BytesWarning',
    'ChildProcessError',
    'ConnectionAbortedError',
    'ConnectionError',
    'ConnectionRefusedError',
    'ConnectionResetError',
    'DeprecationWarning',
    'EOFError',
    'Ellipsis',
    'EnvironmentError',
    'Exception',
    'False',
    'FileExistsError',
    'FileNotFoundError',
    'FloatingPointError',
    'FutureWarning',
    'GeneratorExit',
    'IOError',
    'ImportError',
    'ImportWarning',
    'IndentationError',
    'IndexError',
    'InterruptedError',
    'IsADirectoryError',
    'KeyError',
    'KeyboardInterrupt',
    'LookupError',
    'MemoryError',
    'ModuleNotFoundError',
    'NameError',
    'None',
    'NotADirectoryError',
    'NotImplemented',
    'NotImplementedError',
    'OSError',
    'OverflowError',
    'PendingDeprecationWarning',
    'PermissionError',
    'ProcessLookupError',
    'RecursionError',
    'ReferenceError',
    'ResourceWarning',
    'RuntimeError',
    'RuntimeWarning',
    'StopAsyncIteration',
    'StopIteration',
    'SyntaxError',
    'SyntaxWarning',
    'SystemError',
    'SystemExit',
    'TabError',
    'TimeoutError',
    'True',
    'TypeError',
    'UnboundLocalError',
    'UnicodeDecodeError',
    'UnicodeEncodeError',
    'UnicodeError',
    'UnicodeTranslateError',
    'UnicodeWarning',
    'UserWarning',
    'ValueError',
    'Warning',
    'ZeroDivisionError',
    '__IPYTHON__',
    '__build_class__',
    '__debug__',
    '__doc__',
    '__import__',
    '__loader__',
    '__name__',
    '__package__',
    '__spec__',
    'abs',
    'all',
    'any',
    'ascii',
    'bin',
    'bool',
    'breakpoint',
    'bytearray',
    'bytes',
    'callable',
    'chr',
    'classmethod',
    'compile',
    'complex',
    'copyright',
    'credits',
    'delattr',
    'dict',
    'dir',
    'display',
    'divmod',
    'enumerate',
    'eval',
    'exec',
    'filter',
    'float',
    'format',
    'frozenset',
    'get_ipython',
    'getattr',
    'globals',
    'hasattr',
    'hash',
    'help',
    'hex',
    'id',
    'input',
    'int',
    'isinstance',
    'issubclass',
    'iter',
    'len',
    'license',
    'list',
    'locals',
    'map',
    'max',
    'memoryview',
    'min',
    'next',
    'object',
    'oct',
    'open',
    'ord',
    'pow',
    'print',
    'property',
    'range',
    'repr',
    'reversed',
    'round',
    'set',
    'setattr',
    'slice',
    'sorted',
    'staticmethod',
    'str',
    'sum',
    'super',
    'tuple',
    'type',
    'vars',
    'zip']

or anything in the [`Lib` folder of python](https://github.com/python/cpython/tree/3.10/Lib)

## Source

* [Import error](https://stackoverflow.com/questions/18192967/why-am-i-getting-an-import-error-upon-importing-multiprocessing)
* [Reserved keywords and builtins](https://stackoverflow.com/questions/22864221/is-the-list-of-python-reserved-words-and-builtins-available-in-a-library)
