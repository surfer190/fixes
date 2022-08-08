---
author: ''
category: Python
date: '2022-07-25'
summary: ''
title: What is the meaning of Underscores in Variables Names in Python?
---

## What is the meaning of Underscores in Variables Names in Python?

Single and double underscore before an object name?

* `_foo`: _Convention_. A way for the programmer to indicate that the variable is private or for internal use only.
* `__foo`: _Real meaning_. The interpreter replaces this name with `_classname__foo` as a way to ensure that the name will not overlap with a similar name in another class.
* `__foo__`: _Convention_. A way for the Python system to use names that won't conflict with user names.
* `foo_`: _Convention_. Used to avoid naming conflicts in python. eg. `type_`
* `_`: `_Convention_` User to identify a variable as insignficant. Eg. `for _ in range(10):`

> Convention means it is not enforced by the compiler or interpreter

Remember a variable in a class is an attribute and a function in a class is a method

## Leading underscores do impact how names get imported from modules

    def external_func():
        return 23

    def _internal_func():
        return 42

If you did a wildcard import that function with a `_` to start will not be imported:

    >>> from my_module import *
    >>> external_func()
    23
    >>> _internal_func()
    NameError: "name '_internal_func' is not defined"

> Wildcard imports should be avoided

Regular imports are not affected:

    >>> import my_module
    >>> my_module.external_func()
    23
    >>> my_module._internal_func()
    42

## Name Mangling

A `__` prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses.

Changing the name to avoid collisions.

    class Test:
        def __init__(self):
            self.foo = 11
            self._bar = 23
            self.__pop = 23

    if __name__ == "__main__":
        test_object = Test()
        print(dir(test_object))

The output from the above:

    $ python main.py
    ['_Test__pop', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']

There is no variable with the `__pop` name. It is now called `_Test__pop`

If we extend from `Test`:

    class ExtendedTest(Test):
        def __init__(self):
            super().__init__()
            self.foo = 'overridden'
            self._bar = 'overridden'
            self.__pop = 'overridden'

    if __name__ == "__main__":
        test_object = ExtendedTest()
        print(dir(test_object))
        print('_Test__pop:', test_object._Test__pop)
        print('_ExtendedTest__pop:', test_object._ExtendedTest__pop)

Both vairables are still around:

    $ python main.py
    ['_ExtendedTest__pop', '_Test__pop', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']
    _Test__pop: 23
    _ExtendedTest__pop: overridden

It is transparent to the program:

    def get_mangled(self):
        return self.__pop
    
    print(test_object.get_mangled())

**Name mangling also apples to method names**

    class MangledMethod:
        def __method(self):
            return 42

        def call_it(self):
            return self.__method()

**Perhaps surprisingly, name mangling is not applied if a name starts and ends with double underscores.**

ie. Does not apply to `__dunder__`

## Source

* [What is the meaning of single and double underscore before an object name?](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name)
* [Meaning of underscores in python](https://dbader.org/blog/meaning-of-underscores-in-python)