---
author: ''
category: Python
date: '2022-08-08'
summary: ''
title: Click - command line arguments in python
---

I only found out about `click` last month. I am surprised because it is the 15th [most downloaded package on pypi](https://pypistats.org/top) at time of writing.

Let us see what it is...

## What is click?

> Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary

It features:

* Arbitrary nesting of commands
* Automatic help page generation
* Supports lazy loading of subcommands at runtime

## Installation

    pip install click

## Usage

The module:

    import click

    @click.command()
    @click.option("--count", default=1, help="Number of greetings.")
    @click.option("--name", prompt="Your name",
                help="The person to greet.")
    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for _ in range(count):
            click.echo("Hello, %s!" % name)

    if __name__ == '__main__':
        hello()

Calling it:

    $ python hello.py --count=3
    Your name: John
    Hello John!
    Hello John!
    Hello John!

Getting help:

    $ python hello.py --help
    Usage: hello.py [OPTIONS]

    Simple program that greets NAME for a total of COUNT times.

    Options:
    --count INTEGER  Number of greetings.
    --name TEXT      The person to greet.
    --help           Show this message and exit.

## Why Click?

There are other libraries - like [argparse](./argparse-getting-arguments-nicely-in-python.md) in the standard library, [optparse](https://docs.python.org/3/library/optparse.html) or [docopt](http://docopt.org/)

There is no single cli utility for python that does all of this:

* lazily composable without restrictions (what the hell does that mean?)
* Support implementation of Unix/POSIX command line conventions. Posix are standards for [portable operating system interfaces](https://itsfoss.com/posix/)
* Supports loading values from environment variables out of the box
* Support for prompting of custom values
* Is fully nestable and composable
* Supports file handling out of the box
* Comes with useful common helpers (getting terminal dimensions, ANSI colors, fetching direct keyboard input, screen clearing, finding config paths, launching apps and editors, etc.).

> Click promises multiple Click instances will continue to function as intended when strung together

Click is internally based on optparse instead of argparse.

## Sources

* [Click pallets project](https://palletsprojects.com/p/click/)
* [Why click?](https://click.palletsprojects.com/en/8.1.x/why/)