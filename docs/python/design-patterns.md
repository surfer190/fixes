---
author: ''
category: Design Patterns
date: '2022-01-21'
summary: ''
title: Python
---
# Design Patterns

## The Composition Over Inheritance Principle

> In Python as in other programming languages, this grand principle encourages software architects to escape from Object Orientation and enjoy the simpler practices of Object Based programming instead.

**Favor object composition over class inheritance**

### The subclass explosion

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

### Solution 1: The Adapter Pattern

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

### Solution 2: The Bridge Pattern

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

### Solution 3: The Decorator Pattern

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

### Solution 4: Beyond the Gang of Four patterns

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

### Dodge: “if” statements

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

### Dodge: Multiple Inheritance

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


### Dodge: Mixins

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

### Dodge: Building classes dynamically

...over it...check the source

## Sources

* [Python Design Patterns](https://python-patterns.guide/)