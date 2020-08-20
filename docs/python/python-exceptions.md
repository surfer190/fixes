---
author: ''
category: Python
date: '2019-07-17'
summary: ''
title: Python Exceptions
---
## Guidelines for Python Exceptions

### Code with no exceptions

Code that doesn't use exceptions is always checking if it's OK to do something

> It's easier to ask forgiveness than it is to get permission. - Grace Hopper

    def print_object(some_object):
        # Check if the object is printable...
        if isinstance(some_object, str):
            print(some_object)
        elif isinstance(some_object, dict):
            print(some_object)
        elif isinstance(some_object, list):
            print(some_object)
        # 97 elifs later...
        else:
            print("unprintable object")

can be simplified to:

    def print_object(some_object):
        # Check if the object is printable...
        try:
            printable = str(some_object)
            print(printable)
        except TypeError:
            print("unprintable object")

### Choosing an exception

Choose the one that matches most closely from the [exception hierachy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

### Intrinsic Checks

Never duplicate error checks that python does intrinsically for you

### The try, except else

    try:
        this()
    except TypeError:
        print('problem')
    else:
        no_exception()
    finally:
        clean_up()

`else` is run when there is **no exception** in the `try`

### Narrow First

Matching is beginning to end, a more general clause will stop other exceptions so best to keep the narrowest expection first.

### Base raise

When `raise` is used in excpetion handling code it bubbled the exception up. For example when we want to keep a record of the crash but have no inetention of handling it.

### Don't raise generic Exception

More specific catches will not catch it and a more specific raise beforehand will be caught in the catch of `Exception`

### Idiomatic Python

Idiomatic Python is written in the EAFP (`Easier to Ask for Forgiveness than Permission`) style (where reasonable). We can do so because exceptions are cheap in Python.

### Best Practices

Never use a **bare** `except:` clause or you'll end up suppressing real errors you didn't intend to catch

Take advantage of Python built-ins and standard library modules that already throw exceptions

### Merely logging and moving on

    logger = logging.getLogger(__name__)

    try:
        do_something_in_app_that_breaks_easily()
    except AppError as error:
        logger.error(error)
        raise

By using the base `raise` it simply bubbles up the exception as opposed to returning a new stack trace if you specify the error

## Unhandled

If the exception is left unhandled, the default behavior is for the interpreter to print a full traceback and the error message included in the exception.

It is better to print a more user-friendly version of the error

   except Exception as err:
        sys.stderr.write('ERROR: {}'.format(str(err)))
        return 1

## Catching multiple exceptions

You can catch multiple exception types with:

    except (RuntimeError, TypeError, NameError):
        pass

> If your code only deliberately raises exceptions that you define within your module’s hierarchy, then all other types of exceptions raised by your module must be the ones that you didn’t intend to raise. These are bugs in your API’s code.

## Having a root exception for your package

> The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention)

From the [Python docs on Exceptions](https://docs.python.org/3/tutorial/errors.html#exceptions)


## Sources

* [Cleaner python with exceptions](https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/)
* [Python Exceptions queston on Stackoverflow](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python)
* [Python exception handling technique](https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/)