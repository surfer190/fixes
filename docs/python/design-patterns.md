---
author: ''
category: Design Patterns
date: '2022-01-21'
summary: ''
title: Python
---
# Design Patterns

## Gang of Four: Principles

### The Composition Over Inheritance Principle

> In Python as in other programming languages, this grand principle encourages software architects to escape from Object Orientation and enjoy the simpler practices of Object Based programming instead.

**Favor object composition over class inheritance**

#### The subclass explosion

A logger:

import sys
import syslog

    # The initial class.

    class Logger(object):
        def __init__(self, file):
            self.file = file

        def log(self, message):
            self.file.write(message + '\n')
            self.file.flush()

    # Two more classes, that send messages elsewhere.

    class SocketLogger(Logger):
        def __init__(self, sock):
            self.sock = sock

        def log(self, message):
            self.sock.sendall((message + '\n').encode('ascii'))

    class SyslogLogger(Logger):
        def __init__(self, priority):
            self.priority = priority

        def log(self, message):
            syslog.syslog(self.priority, message)

However now we want to filter the logged do a `error` word:

    # New design direction: filtering messages.

    class FilteredLogger(Logger):
        def __init__(self, pattern, file):
            self.pattern = pattern
            super().__init__(file)

        def log(self, message):
            if self.pattern in message:
                super().log(message)

    # It works.

    f = FilteredLogger('Error', sys.stdout)
    f.log('Ignored: this is not important')
    f.log('Error: but you want to see this')

The problem now if if you want to use the filtered logger with a socket.
You need to create another class.

Exponentially creating classes:

    Logger            FilteredLogger
    SocketLogger      FilteredSocketLogger
    SyslogLogger      FilteredSyslogLogger

> The solution is to recognize that a class responsible for both filtering messages and logging messages is too complicated. In modern Object Oriented practice, it would be accused of violating the “Single Responsibility Principle.”

#### Solution 1: The Adapter Pattern

Decide that the original logger does not need to be improved because any mechanism for outputting messages can be wrapped up to look like the file the logged expects.

The `Logger` and `FilteredLogged` are kept. New classes are created for other loging mechanisms to mimic the file:

    import socket

    class FileLikeSocket:
        def __init__(self, sock):
            self.sock = sock

        def write(self, message_and_newline):
            self.sock.sendall(message_and_newline.encode('ascii'))

        def flush(self):
            pass

    class FileLikeSyslog:
        def __init__(self, priority):
            self.priority = priority

        def write(self, message_and_newline):
            message = message_and_newline.rstrip('\n')
            syslog.syslog(self.priority, message)

        def flush(self):
            pass

> Python encourages duck typing, so an adapter’s only responsibility is to offer the right methods — our adapters, for example, are exempt from the need to inherit from either the classes they wrap or from the file type they are imitating.

Only the methods the Logger uses - need to be implemented.

Use:

    sock1, sock2 = socket.socketpair()

    fs = FileLikeSocket(sock1)
    logger = FilteredLogger('Error', fs)
    logger.log('Warning: message number one')
    logger.log('Error: message number two')

    print('The socket received: %r' % sock2.recv(512))

> Note that it was only for the sake of example that the FileLikeSocket class is written out above — in real life that adapter comes built-in to Python’s Standard Library. Simply call any socket’s `makefile()` method to receive a complete adapter that makes the socket look like a file.

#### Solution 2: The Bridge Pattern

The Bridge Pattern splits a class’s behavior between an outer “abstraction” object that the caller sees and an “implementation” object that’s wrapped inside

    # The “abstractions” that callers will see.

    class Logger(object):
        def __init__(self, handler):
            self.handler = handler

        def log(self, message):
            self.handler.emit(message)

    class FilteredLogger(Logger):
        def __init__(self, pattern, handler):
            self.pattern = pattern
            super().__init__(handler)

        def log(self, message):
            if self.pattern in message:
                super().log(message)

    # The “implementations” hidden behind the scenes.

    class FileHandler:
        def __init__(self, file):
            self.file = file

        def emit(self, message):
            self.file.write(message + '\n')
            self.file.flush()

    class SocketHandler:
        def __init__(self, sock):
            self.sock = sock

        def emit(self, message):
            self.sock.sendall((message + '\n').encode('ascii'))

    class SyslogHandler:
        def __init__(self, priority):
            self.priority = priority

        def emit(self, message):
            syslog.syslog(self.priority, message)

Abstraction objects and implementation objects can be freely combined at runtime:

    handler = FileHandler(sys.stdout)
    logger = FilteredLogger('Error', handler)

    logger.log('Ignored: this will not be logged')
    logger.log('Error: this is important')

Explosion avoided as 2 types of classes are combined at runtime.

#### Solution 3: The Decorator Pattern

What if we wanted to apply two different filters to the same log? The above solutions would not work.

        # The loggers all perform real output.
        
        class FileLogger:
            def __init__(self, file):
                self.file = file

            def log(self, message):
                self.file.write(message + '\n')
                self.file.flush()

        class SocketLogger:
            def __init__(self, sock):
                self.sock = sock

            def log(self, message):
                self.sock.sendall((message + '\n').encode('ascii'))

        class SyslogLogger:
            def __init__(self, priority):
                self.priority = priority

            def log(self, message):
                syslog.syslog(self.priority, message)

        # The filter calls the same method it offers.

        class LogFilter:
            def __init__(self, pattern, logger):
                self.pattern = pattern
                self.logger = logger

            def log(self, message):
                if self.pattern in message:
                    self.logger.log(message)

For the first time, the filtering code has moved outside of any particular logger class

Use:

    log1 = FileLogger(sys.stdout)
    log2 = LogFilter('Error', log1)

    log1.log('Noisy: this logger always produces output')

    log2.log('Ignored: this will be filtered out')
    log2.log('Error: this is important and gets printed')

    log3 = LogFilter('severe', log2)

    log3.log('Error: this is bad, but not that bad')
    log3.log('Error: this is pretty severe')

#### Solution 4: Beyond the Gang of Four patterns

It wanted more flexibility - multiple loggers and multiple filters:

1. The Logger class that callers interact with doesn’t itself implement either filtering or output. Instead, it maintains a list of filters and a list of handlers.
2. For each log message, the logger calls each of its filters. The message is discarded if any filter rejects it.
3. For each log message that’s accepted by all the filters, the logger loops over its output handlers and asks every one of them to emit() the message.

Example:

        # There is now only one logger.

        class Logger:
            def __init__(self, filters, handlers):
                self.filters = filters
                self.handlers = handlers

            def log(self, message):
                if all(f.match(message) for f in self.filters):
                    for h in self.handlers:
                        h.emit(message)

        # Filters now know only about strings!

            class TextFilter:
                def __init__(self, pattern):
                    self.pattern = pattern

                def match(self, text):
                    return self.pattern in text

        # Handlers look like “loggers” did in the previous solution.

        class FileHandler:
            def __init__(self, file):
                self.file = file

            def emit(self, message):
                self.file.write(message + '\n')
                self.file.flush()

        class SocketHandler:
            def __init__(self, sock):
                self.sock = sock

            def emit(self, message):
                self.sock.sendall((message + '\n').encode('ascii'))

        class SyslogHandler:
            def __init__(self, priority):
                self.priority = priority

            def emit(self, message):
                syslog.syslog(self.priority, message)

Usage:

    f = TextFilter('Error')
    h = FileHandler(sys.stdout)
    logger = Logger([f], [h])

    logger.log('Ignored: this will not be logged')
    logger.log('Error: this is important')

> There’s a crucial lesson here: design principles like Composition Over Inheritance are, in the end, more important than individual patterns like the Adapter or Decorator. 

#### Dodge: “if” statements

Simple is better than complex - why not add if statements instead.

    # Each new feature as an “if” statement.
    class Logger:
        def __init__(self, pattern=None, file=None, sock=None, priority=None):
            self.pattern = pattern
            self.file = file
            self.sock = sock
            self.priority = priority

        def log(self, message):
            if self.pattern is not None:
                if self.pattern not in message:
                    return
            if self.file is not None:
                self.file.write(message + '\n')
                self.file.flush()
            if self.sock is not None:
                self.sock.sendall((message + '\n').encode('ascii'))
            if self.priority is not None:
                syslog.syslog(self.priority, message)

    # Works just fine.

    logger = Logger(pattern='Error', file=sys.stdout)

    logger.log('Warning: not that important')
    logger.log('Error: this is important')

The class can be grasped by reading top to bottom

What has been lost:

1. Locality - readability and ability to enhance or fix issues is a problem.
2. Deletability - Deleting a feature can be done by deleting `SocketHandler` - deleting it with `if` statements may break adjacent code.
3. Dead code analysis - dead code analysers won't work with the `if` statement version
4. Testing - Requiring to set up multiple irrelevant circumstances and parameters to test code.
5. Efficiency - code only runs for features declared - not all conditions

> One of the strongest signals about code health that our tests provide is how many lines of irrelevant code have to run before reaching the line under test.
#### Dodge: Multiple Inheritance

But Python supports multiple inheritance, so the new FilteredSocketLogger can list both SocketLogger and FilteredLogger as base classes and inherit from both:

    class Logger(object):
        def __init__(self, file):
            self.file = file

        def log(self, message):
            self.file.write(message + '\n')
            self.file.flush()

    class SocketLogger(Logger):
        def __init__(self, sock):
            self.sock = sock

        def log(self, message):
            self.sock.sendall((message + '\n').encode('ascii'))

    class FilteredLogger(Logger):
        def __init__(self, pattern, file):
            self.pattern = pattern
            super().__init__(file)

        def log(self, message):
            if self.pattern in message:
                super().log(message)

    # A class derived through multiple inheritance.
    class FilteredSocketLogger(FilteredLogger, SocketLogger):
        def __init__(self, pattern, sock):
            FilteredLogger.__init__(self, pattern, None)
            SocketLogger.__init__(self, sock)

    # Works just fine.
    logger = FilteredSocketLogger('Error', sock1)
    logger.log('Warning: not that important')
    logger.log('Error: this is important')

    print('The socket received: %r' % sock2.recv(512))

Unit tests:

* Multiple inheritance depends on behavior that cannot be verified by simply instantiating the classes in question.
* Multiple inheritance has introduced a new `__init__()` method because neither base class’s `__init__()` method accepts enough arguments for a combined filter and logger
* You will have to test every combination to ensure it is safe - an explosion of subclasses

#### Dodge: Mixins

A mixin is a class that defines and implements a single, well-defined feature.

    # Simplify the filter by making it a mixin.

    class FilterMixin:  # No base class!
        pattern = ''

        def log(self, message):
            if self.pattern in message:
                super().log(message)

    # Multiple inheritance looks the same as above.

    class FilteredLogger(FilterMixin, FileLogger):
        pass  # Again, the subclass needs no extra code.

    # Works just fine.

    logger = FilteredLogger(sys.stdout)
    logger.pattern = 'Error'
    logger.log('Warning: not that important')
    logger.log('Error: this is important')

#### Dodge: Building classes dynamically

...over it...check the source

### Cool Pattern

I noticed a cool pattern - when constructing an object you can also tell the class what underlying class to use. I saw it in the [Python Elasticsearch Client](https://elasticsearch-py.readthedocs.io/en/7.x/transports.html)

You could run:

    from elasticsearch import Elasticsearch, RequestsHttpConnection
    es = Elasticsearch(
        'my-es:9200',
        use_tls=True,
        headers={'my-api-key': 'XXX'},
        connection_class=RequestsHttpConnection
    )

This told ElasticSearch to use the `RequestsHttpConnection` class. You could also use `Urllib3HttpConnection`.

Then in `Elasticsearch::__init__`:

    def __init__(self, hosts=None, transport_class=Transport, **kwargs):
        """
        :arg transport_class: :class:`~elasticsearch.Transport` subclass to use.
        """
        self.transport = transport_class(_normalize_hosts(hosts), **kwargs)

In the constructor it instantiates the class with the host info and keyword arguments supplied.

I am not sure what design pattern this is - or if it even is one - but it looked nice and let me set headers on the Elasticsearch client so I could auth. Pretty neat.

## Python-Specific Patterns

### The Global Object Pattern

> Python parses the outer level of each module as normal code. Un-indented assignment statements, expressions, and even loops and conditionals will execute as the module is imported. An excellent opportunity for constants and data structures that callers will find useful. The dangers are that global objects can wind up coupling distant code, and I/O operations impose import-time expense and side effects.

Every Python module is a separate namespace.

Separate namespaces are crucial to making a programming language tractable.

> Programmers who are forced to code in a language without namespaces soon find themselves festooning global names with prefixes, suffixes, and extra punctuation in a desperate race to keep them from conflicting.

#### The Constant Pattern

Examples from the standard library

    January = 1                   # calendar.py
    WARNING = 30                  # logging.py
    MAX_INTERPOLATION_DEPTH = 10  # configparser.py
    SSL_HANDSHAKE_TIMEOUT = 60.0  # asyncio.constants.py
    TICK = "'"                    # email.utils.py
    CRLF = "\r\n"                 # smtplib.py

constants can also be tuples or frozensets:

    all_errors = (Error, OSError, EOFError)  # ftplib.py
    bytes_types = (bytes, bytearray)         # pickle.py
    DIGITS = frozenset("0123456789")         # sre_parse.py
    _EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)  # datetime

Even mutable dtastructures are used:

    # socket.py
    _blocking_errnos = { EAGAIN, EWOULDBLOCK }
    # locale.py
    windows_locale = {
    0x0436: "af_ZA", # Afrikaans
    0x041c: "sq_AL", # Albanian
    0x0484: "gsw_FR",# Alsatian - France
    ...
    0x0435: "zu_ZA", # Zulu
    }

> Constants are often introduced as a refactoring: the programmer notices that the same value `60.0` is appearing repeatedly in their code, and so introduces a constant `SSL_HANDSHAKE_TIMEOUT` for the value instead. Each use of the name will now incur the slight cost of a search into the global scope, but this is balanced by a couple of advantages. The constant’s name now documents the value’s meaning, improving the code’s readability. And the constant’s assignment statement now provides a single location where the value can be edited in the future without needing to hunt through the code for each place `60.0` was used.

#### Dunder Constants

* `__name__` - the functions name - remember the fake name `'__main__'` is set for any command-line top level script
* `__file__` - the full filesystem path to the module’s Python file itself

Used to find data files:

    here = os.path.dirname(__file__)

If `__all__` is assigned a sequence of identifiers eg. `__all__ = ['run', 'walk', 'jump']`. Only those names are imported when you do a `from x import *`

`import *` became an anti-pattern but `__all__` is still used for sphinx autodoc. It is better to assign it as a tuple.

#### Global Objects that are mutable

For example `os.environ`

* Affecting tests and tests that run in parrallel mofifying this global object
* If tests don't restore environ to the original state

#### Import-time I/O

For example if `/etc/hosts` does not exist.

> Avoid network or file oeprations at import time

* Errors at import time are far more serious than errors at runtime - there are still a stack of imports the program is going through and will not be in a error hanlding place `try...except`
* Sometimes your library is imported but not even used

Your libraries should wait until they’re first called before opening files and creating sockets

### The Prebound Method Pattern

...


### The Sentinel Object Pattern

...

## Gang of Four: Creational Patterns

### The Singleton Pattern

Python already had a singleton - before it became a thing.

* A tuple of length one is called a singleton - it reflects the original definition of a singleton in mathematics: a set containing exactly one element
* Modules are “singletons” in Python because import only creates a single copy of each module - subsequent import of the same module return the same object
* A singleton is a class instance that has been defined a global name - [How do I share global variables across modules?](https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules)
* The actual singleton design pattern: the lone object returned by its class every time the class is called - there can only be one.

In Python3 `None` and `Ellipsis` were upgraded to use the singleton pattern.

So you can:

    Nonetype = type(None)
    new_none = NoneType()
    print(new_none)
    >>> None

> Rarely used - usually ther global object pattern is used and you just type the name `None`

#### The Gang of Four's Implementation

> Unlike a global function, a class method avoided adding yet another name to the global namespace, and unlike a static method, it could support subclasses that were singletons as well.

    class Logger(object):
        _instance = None

        def __init__(self):
            raise RuntimeError('Call instance() instead')

        @classmethod
        def instance(cls):
            if cls._instance is None:
                print('Creating new instance')
                cls._instance = cls.__new__(cls)
                # Put any initialization here.
            return cls._instance

This prevents the client from institating the object from the class.
Callers are instructed to use the `instance()` method which returns the object.

    log1 = Logger.instance()
    print(log1)
    log2 = Logger.instance()
    print(log2)
    print('Are they the same object?', log1 is log2)

Subsequent calls do not initiatialise again and returns the same object.

> Apparently this is not a good fit for python

#### A more Pythonic implementation

Python started with a head start - by lacking a `new` keyword. Instead objects are created by invoking a callable.
There is no limitation on what the callable does.

    log = Logger()

Python 2.4 added the [`__new__()`](https://docs.python.org/3/reference/datamodel.html?highlight=__new__#object.__new__) dunder method to support alternative creational patterns like the Singleton Pattern and the Flyweight pattern.

The problem is `__init__()` always gets called on the return value, whether the object that’s being returned is new or not

    class Logger(object):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                print('Creating the object')
                cls._instance = super(Logger, cls).__new__(cls)
                # Put any initialization here.
            return cls._instance

> the above pattern is the basis of every Python class that hides a singleton object behind what reads like normal class instantiation.

Drawbacks:

* Difficult to read compared to the global object pattern, you need to know what `__new__()` does
* Hard to test a singleton - you are forced to use the class in a specific way - Unless the caller is willing to stoop to monkey patching; or temporarily modifying _instance to subvert the logic in `__new__()`
* It is not obvious you are instantiating a singleton

The pattern is generally best avoided in favour of the global object pattern or [sharing global objects across modules](https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules)

> If your program only needs one of a certain object, you can just make one

    class ChessBoard:
        def __init__(self):
            ...

    the_chess_board = ChessBoard()

If you want centralised management, make it global:

    _the_chess_board = None

    def the_chess_board():
        global _the_chess_board
        if _the_chess_board is None:
            _the_chess_board = ChessBoard()
        return _the_chess_board


## Gang of Four: Structural Patterns

...

## Gang of Four: Behavioral Patterns

...


## Sources

* [Python Design Patterns](https://python-patterns.guide/)
* [Singleton is a bad idea - Ned Batchelder](https://nedbatchelder.com/blog/202204/singleton_is_a_bad_idea.html)