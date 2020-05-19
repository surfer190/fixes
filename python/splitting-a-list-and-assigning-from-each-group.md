# Splitting a list and assigning data from each group in a round robin way

Sometimes you need to split a list into a numer of groups and assign data to each one.
round robin splitting python.
Splitting a List into chunks in Python.

Use [itertools.cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle)

    from itertools import cycle

    ids = [1, 2, 3]
    id_cycle = cycle(ids)

    for item in range(10):
        print(next(id_cycle))

Running the above you get:

    $ python item.py 
    1
    2
    3
    1
    2
    3
    1
    2
    3
    1

It is an infinite iterator.

