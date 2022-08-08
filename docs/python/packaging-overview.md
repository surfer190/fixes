---
author: ''
category: Python
date: '2022-08-08'
summary: ''
title: Python Packaging - an Overview
---

# Overview: Python packaging

Python packaging is extremely broad. It has a long history and isn't easily learned and understood in a day.
You need to gradually learn and apply - by packaging yourself.
If you have never packaged (or even if you have) you won't know all the ins and outs - caveats etc.

In this post I am going to attempt to touch on certain parts of packaging gradually until a full overview is formed.

### Command Line Scripts

How do you package command line tools in your package? Command lines tools usually look to the user like a binary and are in `/usr/bin` or `/usr/local/bin` on unix based machines.

There are 2 mechanisms for this:

1. `scripts` keyword in `setup.py`
2. `console-scripts` - entrypoints

#### Scripts

Write your script in a seperate file:

    #!/usr/bin/env python

    import funniest
    print funniest.joke()

put it in `mypackage/bin`

In `setup.py`

    setup(
        ...
        scripts=['bin/funniest-joke'],
        ...
    )

When we install the package pip will make it available on the path. This is generalizable - the script could be any type: `go`, `bash`, etc.

#### The Console Scripts Entrypoint

Setuptools allows modules to register entrypoints which other packages can hook into to provide certain functionality

This allows **Python functions (not scripts!)** to be directly registered as command-line accessible tools.

Create a python module (a new `.py` file) and create the function:

    import funniest

    def main():
        print funniest.joke()

in `mypackage/package_dir/command_line.py`

You can test it directly:

    >>> import funniest.command_line
    >>> funniest.command_line.main()

register the main function:

    setup(
        ...
        entry_points = {
            'console_scripts': ['funniest-joke=funniest.command_line:main'],
        }
        ...
    )

when the package is installed it will move it to the `bin` path

> Setuptools will generate a standalone script ‘shim’ which imports your module and calls the registered function.

This method has the advantage that it’s very easily testable, instead of having to shell out to spawn the script we can do:

    from unittest import TestCase
    from funniest.command_line import main

    class TestConsole(TestCase):
        def test_basic(self):
            main()

> To make that more useful we might want to use a context manager for `sys.stdout`

## Source

* [python-packaging readthedocs](https://python-packaging.readthedocs.io/en/latest/index.html)
