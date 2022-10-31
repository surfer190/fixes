---
author: ''
category: Python
date: '2022-08-20'
summary: ''
title: Python Logging
---

## Python Logging

> Use the source...Luke

A good place to look is the standard library's `logging` module/file.

Most IDEs will go there when you `cmd + click` on `import logging`.

I was reading:

    #---------------------------------------------------------------------------
    #   Level related stuff
    #---------------------------------------------------------------------------
    #
    # Default levels and level names, these can be replaced with any positive set
    # of values having corresponding names. There is a pseudo-level, NOTSET, which
    # is only really there as a lower limit for user-defined levels. Handlers and
    # loggers are initialized with NOTSET so that they will log all messages, even
    # at user-defined levels.
    #

    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

So the default logging level is `0` or `NOTSET`.

You can verify this yourself:

    logger = logging.getLogger(__name__)
    logger.level
    >>>> 0

So by default all log messages should be sent...

However not all logging will print a message - only levels warning and above

## Set the Logging Level from Environment Variable

    LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
    logging.basicConfig(level=LOGLEVEL)

Another way is:

    logging.basicConfig(level=logging.getLevelName(log_level))

Both are fine but the top one have less calls to `_nameToLevel`

## Logging Patterns

### The Big Tarp Pattern

    try:
        main_loop()
    except Exception:
        logger.exception("Fatal error in main loop")

* A broad catch-all
* It can raise a number of different exceptions and you don't want the program to terminate
* Preferred to log and continue
* The `exception` method captures the full stacktrace and logs it
* By default, `logger.exception` uses the log level of `ERROR`.

### The “Pinpoint” Pattern

    try:
        places = find_burrito_joints(criteria)
    except BurritoCriteriaConflict as err:
        logger.warn("Cannot resolve conflicting burrito criteria: {}".format(err.message))
        places = list()

* Handling a specific exception

### The Message and Raise Pattern

    try:
        something()
    except SomeError:
        logger.warn("...")
        raise

* You are not actually handling the exception
* With an existing higher level handler, you want to log that the error occurred, or the meaning of it, at a certain place in the code.
* Most Useful in troubleshooting

### The Cryptic Message Antipattern

    try:
        something()
    except Exception:
        logger.error("...")

It is hard to figure out where in the code it actually broke.
In that instance it is best to set `exc_info`

    try:
        something()
    except Exception:
        logger.error("something bad happened", exc_info=True)

### The Most Diabolical Python Antipattern

    try:
        something()
    except Exception:
        pass

* No useful exception information is generated
* Completely hides that there is something wrong
* You may not even know a variable name was typed wrong - `NameError` is hidden


## Sources

* [Nifty Python Logging Trick](https://powerfulpython.com/blog/nifty-python-logging-trick/)
* [Exceptional logging of exceptions in Python](https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/)
