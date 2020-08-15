---
author: ''
category: Python
date: '2017-11-08'
summary: ''
title: Comprehensions
---
# Comprehensions

## Adding halves to a list of a range of numbers

    >>> nums
    range(5, 101)
    >>> halves = []
    >>> for num in nums:
    ...     halves.append(num/2)
    ...
    >>> halves
    [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0]


## List comprehension

Always creates a list

We want to create a list of halves, which is `num` divide by 2 for each `num` in `nums`

    halves = [num/2 for num in nums]

### Fizzbuzz

Numbers 1 to 100. If number is divisisble by 3 print `fizz`, by 7 prints `buzz`, both `fizzbuzz`

List comprehensions become difficult to understand when there are too many conditions

        >>> print([num for num in range(0, 101) if num % 3 == 0])

## Looping through 2 iterables

        rows = range(4)
        cols = range(10)
        (x, y) for y in rows for x in cols]

The inner loop is run for each in the outer

        >>> [(letter, number) for letter in 'abcde' for number in range(0,6)]
        [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('d', 0), ('d', 1), ('d', 2), ('d', 3), ('d', 4), ('d', 5), ('e', 0), ('e', 1), ('e', 2), ('e', 3), ('e', 4), ('e', 5)]

## Creating a dictionary

        >>> {number:letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}
        {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

## Zip

Basically returns the same index position for all iterables

        >>> help(zip)
        Help on class zip in module builtins:

        class zip(object)
        |  zip(iter1 [,iter2 [...]]) --> zip object
        |
        |  Return a zip object whose .__next__() method returns a tuple where
        |  the i-th element comes from the i-th iterable argument.  The .__next__()
        |  method continues until the shortest iterable in the argument sequence
        |  is exhausted and then it raises StopIteration.
        |
        |  Methods defined here:
        |
        |  __getattribute__(self, name, /)
        |      Return getattr(self, name).

## Sets

Sets are like a list but they don't have an order and are **unique**

They are created with `{` `}` but they don't have a colon to seperate values

## Interesting Reads

[Python History: The history of List Comprehensions](http://python-history.blogspot.co.za/2010/06/from-list-comprehensions-to-generator.html)
