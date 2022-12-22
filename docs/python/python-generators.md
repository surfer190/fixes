---
author: ''
category: Python
date: '2018-07-11'
summary: ''
title: Python Generators
---
# Python Generators

This is not a simple topic, avoid it for a while.

Generators allow you to declare functions that behave like iterators.

### Iterator

* An iterator is an object that can be iterated (looped) upon
* Any class implementing `__iter__` and `__next__`
* Save memory as only compute when you ask for it: `lazy evaluation`
* Important in large data sets (doesn't stop you from working)

Example:

Remember `**` is the power operator, more with `>>> help('**')`

    def check_prime(number):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False
        return True
    
A prime iterator would be created with:

    class Primes:
        def __init__(self, max):
            self.max = max
            self.number = 1

        def __iter__(self):
            return self

        def __next__(self):
            self.number += 1
            if self.number >= self.max:
                raise StopIteration
            elif check_prime(self.number):
                return self.number
            else:
                return self.__next__()

To summarise what this does is it is initialised with a maximum (number) value and sets the number to 1.
The next iteration will increment `number`.
If `number` is great than `max` iteration will stop.
If `number` is a prime number that number is returned.
If it is not prime, the `__next__` iteration will be calculated and returned.

Using the iterator:

    primes = Primes(100000000000)

    print(primes)

    for x in primes:
        print(x)

    ---------

    <__main__.Primes object at 0x1021834a8>
    2
    3
    5
    7
    11
    ...


By using an iterator we are not creating a huge list of prime numbers in memory, we are generating the prime number when we ask for it.

**Importantly: Iterators can only be iterated over once**

> If you try to iterate over it again, no value will be returned. It will behave like an empty list.


## Generators

> Generator functions allow us to create iterators in a more simple fashion. - Free Code Camp

Generators introduce the `yield` statement to Python. It works a bit like `return` because it returns a value.

The difference is that it saves the state of the function. The next time the function is called, execution continues from where it left off, with the same variable values it had before yielding.

Example:

    def Primes(max):
        number = 1
        while number < max:
            number += 1
            if check_prime(number):
                yield number

Usage:

    primes = Primes(100000000000)

    print(primes)

    for x in primes:
        print(x)

    ---------

    <generator object Primes at 0x10214de08>
    2
    3
    5
    7
    11
    ...

We can attempt to make it simpler (less code doesn't mean it is more obvious to the reader)

We can use `Generator Expressions`, which are similar to list comprehensions except they use `()` instead of `[]`

    primes = (i for i in range(2, 100000000000) if check_prime(i))

* Generators can only be iterated over once

### Sources

* [Freecode camp post on generators - not the simplest to understand](https://medium.freecodecamp.org/how-and-why-you-should-use-python-generators-f6fb56650888)