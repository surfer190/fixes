---
author: ''
category: Python
date: '2022-04-15'
summary: ''
title: Summary of Understanding Decorators in Python
---
# Summary of Understanding Decorators in Python

* Decorators are wrappers around Python functions (or classes) that change how these classes work
* Notation designed not to be invasive

Common example the `@propery` decorator - lets you specify a function as an attroibute of an object.

    class Rectangle:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        @property
        def area(self):
            return self.a * self.b

    rect = Rectangle(5, 6)
    print(rect.area)

Writing `@property` is the same as writing `area = property(area)`

`property` is a function - taking another function as an argument. Exactly what decorators do - changing the behaviour of the decorated function.

### Retry Decorator

    def retry(func):
        def _wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                time.sleep(1)
                func(*args, **kwargs)
        return _wrapper

    @retry
    def might_fail():
        print("might_fail")
        raise Exception

    might_fail()

* `retry` is the name of our decorator - accepting any function `func`
* the `_wrapper` function is defined inside the existing `retry` function - syntactically fine and ensures the `_wrapper` function only exists within retry.
* When `might_fail()` is run - it is really running `retry` with `might_fail` as the first argument. Since `retry` does not have `()` - it is not called.

### How do we accept arguments?

    def retry(max_retries):
        def retry_decorator(func):
            def _wrapper(*args, **kwargs):
                for _ in range(max_retries):
                    try:
                        func(*args, **kwargs)
                    except:
                        time.sleep(1)
            return _wrapper
        return retry_decorator


    @retry(2)
    def might_fail():
        print("might_fail")
        raise Exception


    might_fail()

* `retry` accepts the number of `max_retries`
* `retry_decorator` is the function retured by `retry` and is the actual decorator
* `wrapper` works the same way but handles the number of retries
* the results of the `retry(2)` call is the function that wraps `might_fail`

### Timer Decorator

Let us measure the run time of functions it decorates

    import functools
    import time

    def timer(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            runtime = time.perf_counter() - start
            print(f"{func.__name__} took {runtime:.4f} secs")
            return result
        return _wrapper

    @timer
    def complex_calculation():
        """Some complex calculation."""
        time.sleep(0.5)
        return 42

    print(complex_calculation())

> `functools.wraps` - You might have noticed that the `_wrapper` function itself is decorated with `@functools.wraps`. This does not in any way change the logic or functionality of our timer decorator

The main use of it is to set the magic reflection attributes:

* `__module__`
* `__name__`
* `__qualname__`
* `__doc__`
* `__annotations__`

### Class Decorators

> Class methods are not automatically decorated when decorating a class - using a normal decorator to decorate a normal class decorates its constructor `__init__` method only.

    @timer
    class MyClass:
        def complex_calculation(self):
            time.sleep(1)
            return 42

    my_obj = MyClass()
    my_obj.complex_calculation()

will give:

    Finished 'MyClass' in 0.0000 secs

We can decorate a function with a class:

    class MyDecorator:
        def __init__(self, function):
            self.function = function
            self.counter = 0
        
        def __call__(self, *args, **kwargs):
            self.function(*args, **kwargs)
            self.counter+=1
            print(f"Called {self.counter} times")


    @MyDecorator
    def some_function():
        return 42


    some_function()
    some_function()
    some_function()

### Using Decorators

* `@property` is used to access a method as you would an attribute
* `@staticmethod` is to call a function defined inside a class without instantiating the class
* `@functools.cache` a complex calculation can be cached
* `@dataclass` adds constructors and json representations to an object

> decorators can be nested

## Source

* [Bas codes: Understanding Python Decorators](https://bas.codes/posts/python-decorators)