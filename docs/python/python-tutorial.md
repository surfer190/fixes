---
author: ''
category: Python
date: '2022-08-15'
summary: ''
title: Python Tutorial
---

> Shortcut to the [Python Tutorial](https://docs.python.org/3/tutorial/index.html)

> Shortcut to the [Python FAQ](https://docs.python.org/3/faq/)

When you start programming you are so focussed on making applications that reading the docs is the last thing on your mind.
Over the years I have learnt that the docs - the official python docs - are excellent.
They teach you things most skip over and make you a better, more robust developer.

Python provides an[extensive tutorial](https://docs.python.org/3/tutorial/index.html) that most have us have never even looked at.
We just watch other people on videos, search for our specific issue at this point in time or read books from people that are involved in python.

The python source code and official documentation however _should_ in my opinion be the single source of truth.

In this extended post I will _gradually_ look at aspects of this Python tutorial and write summaries and learn along the way,
It will not be done in order.

Also how many python programmers - have actually gone through the [python FAQs?](https://docs.python.org/3/faq/)

## 8. Errors and Exceptions

Two types:

* SyntaxError - parsing error. The offending line has an arrow where the problem is.
* Exceptions - statement is syntactically correct. Errors detected during execution are called _exceptions_ and are not unconditionally fatal. Most exceptions are not handled by programs, however, and result in error messages.

> Where does `IndentationError` fall?

Syntax Error example:

    $ python3 main.py
    File "./main.py", line 1
        print "hello"
            ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?

Exception examples:

    Traceback (most recent call last):
    File "./main.py", line 3, in <module>
        print(tree)
    NameError: name 'tree' is not defined

    Traceback (most recent call last):
    File "./main.py", line 5, in <module>
        '2' + 2
    TypeError: can only concatenate str (not "int") to str

    Traceback (most recent call last):
    File "./main.py", line 7, in <module>
    1/0
    ZeroDivisionError: division by zero

These are standard exceptions built-into the python language. Standard exception names are built-in identifiers (not reserved keywords).
The preceding part of the error message shows the context where the exception occurred, in the form of a stack `traceback` - a reverse stack trace.

`NameError`, `TypeError` and `ZeroDivisionError` are shown. Here is a list of [all built-in exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

### Handling Exceptions

    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

How does `try` work?

1. It attempts the code between `try` and `except`
2. If no excpetion occurs the `except` clause is skipped and execution continues
3. If an expetion occurs - the rest of the code is skipped and if the exception type matches that of the except clause - the except clause is run
4. If an exception occurs that does not match it is passed to outer `try` statements. If no handler is found, it is an unhandled exception and execution stops with a message as shown above.

* A try statement may have more than one except clause
* At most one handler will be executed
* An except clause can name multiple exceptions

    except (RuntimeError, TypeError, NameError):
        pass

A rule of thumb is to except the most specific class first. The base (or parent) class of an excpetion will be compatible with the exception.

> All exceptions inherit from `BaseException` - it can serve as a wildcard. Use with extreme caution, it can mask a real programming error. It can also be used to print an error message and then re-raise the exception.

    import sys

    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

The `try...except` has an optional `else` clause. It is useful for code that must be executed if the try clause does not raise an exception.

An exception has name and arguments:

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses

### Raising Exceptions

Use `raise` to force an exception to occur

    raise NameError('HiThere')

You can give it an isntance or a class

    raise ValueError # will instantiate and raise

If you need to determine if an exception was raised but don't intend on handling it:

    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise

### Exception Chaining

Using an optional `from` to a `raise`:

    raise RuntimeError from exc

> This can be useful when you are transforming exceptions

Example:

    def func():
        raise ConnectionError

    try:
        func()
    except ConnectionError as exc:
        raise RuntimeError('Failed to open database') from exc

Gives:

    $ python3 exception_chaining.py
    Traceback (most recent call last):
    File "./exception_chaining.py", line 5, in <module>
        func()
    File "./exception_chaining.py", line 2, in func
        raise ConnectionError
    ConnectionError

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
    File "./exception_chaining.py", line 7, in <module>
        raise RuntimeError('Failed to open database') from exc
    RuntimeError: Failed to open database

> Exception chaining happens automatically when an exception is raised inside an `except` or `finally` section. To disable it you use `from None`

### User Defined Exceptions

Naming convention is to usually end with `Error`

Example:

    class Error(Exception):
        """Base-class for all exceptions raised by this module."""

    class InvalidDensityError(Error):
        """There was a problem with a provided density value.""”

### Finally - Clean Up Actions

The `finally` runs the last task before the `try` statement completes. It will fun whether or not an exception is raised.

* If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed
* Exception raised in an else caluse it also reraised after finally has been handled
* If `finally` executes a: `break`, `continue` or `return` exceptions are not reraised
* If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break
* If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.

> In real world applications, the finally clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

### Predefined Cleanup Actions

    for line in open("myfile.txt"):
        print(line, end="")

Use the `with` statement ensures the file will be cleaned up:

    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")

## 9. [Classes](https://docs.python.org/3/tutorial/classes.html)

* Bundle data and functionality together
* A new class creates a new `type` of object
* Each class instance can have attributes attached to it for maintaining its state
* Classes also have methods to modify states
* Python classes provide all the standard features of Object Oriented Programming:
    - class inheritance allows for multiple base classes
    - a derived class can override any methods of its base class or classes
    - a method can call the method of a base class with the same name
* Classes themselves are objects

> As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

### 9.1 Names and Objects

> Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object.

* This is usually used to the benefit of the program, since aliases behave like pointers in some respects
* Passing an object is cheap since only a pointer is passed by the implementation
* If a function modifies an object passed as an argument, the caller will see the change

### 9.2 Python Scopes and Namespaces

* A `namespace` is a mapping from names to objects.
* Examples: built-in names (functions and exceptions), global names in a module, local names in a function invocation
* There is absolutely no relation between names in different namespaces

Anything with a dot after is an attribute...

    modname.the_answer = 42
    del modname.the_answer

> The above is setting and deleting a module attribute

* The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The module name is `builtins`.
* The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits
* The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function.
* The statements executed by the top-level invocation of the interpreter are considered part of the `__main__` module

* A `scope` is a textual region of a Python program where a namespace is directly accessible

scopes are accessed dynamically:

* the innermost scope, which is searched first, contains the `local` names
* the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains `non-local`, but also `non-global` names
* the next-to-last scope contains the current module’s `global` names
* the outermost scope (searched last) is the namespace containing `built-in` names

> if no `global` or `nonlocal` statement is in effect – assignments to names always go into the innermost scope

Assignments do not copy data — they just bind names to objects. The same is true for deletions: the statement `del x` removes the binding of`x` from the namespace referenced by the local scope.

* `import` statements and function definitions bind the module or function name in the local scope
* The `global` statement can be used to indicate that particular variables live in the global scope and should be rebound there
* The `nonlocal` statement indicates that particular variables live in an enclosing scope and should be rebound there.

#### 9.2.1 Scopes and Namespace Example

    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)

Results in:

    $ python3 scope_test.py 
    After local assignment: test spam
    After nonlocal assignment: nonlocal spam
    After global assignment: nonlocal spam
    In global scope: global spam

> The variables are all updated in the correct scope but at call time they are shown.

* `scope_test()`'s binding was not changed by the `local` scope of `do_local()`
* The `nonlocal` scope did change `scope_test()` from `do_nonlocal()`
* The `global` assignment changed the module level `spam`

### 9.3 First Look - Classes

    class ClassName:
        ...

> When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace.

#### 9.3.1 Class Objects

* Class objects support two kinds of operations: attribute references and instantiation
* attribute refence like `obj.name`

    class MyClass:
        """A simple example class"""
        i = 12345

        def f(self):
            return 'hello world'

    if __name__ == '__main__':
        print('MyClass.i: ', MyClass.i)
        print('MyClass.f: ', MyClass.f)
        print('MuClass.__doc__: ', MyClass.__doc__)

Returns:

    $ python3 access_class.py 
    MyClass.i:  12345
    MyClass.f:  <function MyClass.f at 0x102be5120>
    MuClass.__doc__:  A simple example class

Class instantiation uses function notation:

    x = MyClass()

assigns a new instance of `MyClass` to the local variable `x`

* The instantiation operation (“calling” a class object) creates an empty object
* Many classes like to create objects with instances customized to a specific initial state using `__init__` method
* Calling `x.f()` is exactly equivalent to calling `MyClass.f(x)`

    def __init__(self):
        self.data = []

The `__init__` method can also have arguments for flexibility

    class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart

Instance objects have `attributes` - data of a class and `methods` - functions of a class.

> The special thing about methods is that the instance object is passed as the first argument of the function

#### Class and Instance Variables

* Instance variables are for data unique to each instance
* Class variables are for attributes and methods shared by all instances of the class

    class Dog:

        kind = 'canine'         # class variable shared by all instances

        def __init__(self, name):
            self.name = name    # instance variable unique to each instance

    if __name__ == "__main__":
        my_dog = Dog('Ace')
        my_dog2 = Dog('Casey')

        print(my_dog.kind)
        print(my_dog.name)

        print(my_dog2.kind)
        print(my_dog2.name)

Mistaken use of class variables:

    class Dog:
        tricks = []             # mistaken use of a class variable

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    if __name__ == "__main__":
        d = Dog('Fido')
        e = Dog('Buddy')
        d.add_trick('roll over')
        e.add_trick('play dead')
        print(d.tricks)

Results in:

    $ python3 class_variable_caveat.py   
    ['roll over', 'play dead']

> The single class variable list is shared among all instances

Correct design of the class should use an instance variable instead:

    class Dog:

        def __init__(self, name):
            self.name = name
            self.tricks = []    # creates a new empty list for each dog

        ...

### 9.4 Random Remarks

* If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance
* Nothing in Python makes it possible to enforce data hiding — it is all based upon convention.
* Often, the first argument of a method is called `self`. This is nothing more than a convention: the name `self` has absolutely no special meaning to Python
* Methods may call other methods by using method attributes of the `self` argument

You can assign the method of a class - that is outside the class:

    def f1(self, x, y):
        return min(x, x+y)

    class C:
        f = f1

        def g(self):
            return 'hello world'

        h = g

    if __name__ == "__main__":
        my_c = C()
        print(my_c.f(4, 5))
        print(my_c.h())

Results in:

    $ python3 method_defined_outside_class.py
    4
    hello world

> This only serves as to confuse the reader

* Each value is an object
* Therefore has a class (also called its `type`).
* It is stored as `object.__class__`

    >>> 'monkey'.__class__
    >>> str

### 9.5 Inheritance



## Source

* [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)