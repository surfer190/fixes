# Effective Python Summary Notes

I've been wanting to learn and improve my python so I read a book and took notes from `Effective Python - Brett Slatkin`. He has [some good tech reads on his blog](https://www.onebigfluke.com/).

## Pythonic Thinking

### Know which python version you are using

$ python --version

of

    >>> import sys
    >>> print(sys.version_info)
    sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)
    >>> print(sys.version)
    3.6.4 (default, Mar  9 2018, 23:15:03) 
    [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)]

* Prefer python 3 for new projects.
* There are many runtimes: CPython, Jython, Itonpython, PyPy. Default is CPython.

### Follow PEP8 Style Guide

Conistent style makes code more approachable and easy to read
Facilitates collaboration

[Read the pep8 style guide](https://www.python.org/dev/peps/pep-0008/)

### Know the Differences Between bytes, str, and unicode

In python 3 there is `bytes` and `str`.
`str` contain unicode values
`bytes` contain raw 8-bit values

* You need to use `encode` and `decode` to convert unicode to `bytes`
* Do encoding and decoding at the furtherest boundary of the interface (so core of program works with unicode)
* bytes and str instances are never equivalent (In python 3)
* File handles (using `open`) default to UTF-8 encoding

Ensure to use `wb` write-banary mode as opposed to `w` wrote character mode:

    with open('/tmp/random.bin', 'wb') as f:

### Write helper functions, instead of complex expressions

Consider:

    red = int(my_values.get('red', [''])[0] or 0)

This code is not obvious. There is a lot of visual noise and it is not approachable.

You could use a `ternary`:

    red = my_values.get('red', [''])
    red = int(red[0]) if red[0] else 0

but it is still not great.

So a helper function:

    def get_first_int(values, key, default=0):
        found = values.get(key, [''])
        if found[0]:
            found = int(found[0])
        else:
            found = default
        return found

and calling:

    green = get_first_int(my_values, 'green')

is much clearer.

* Use complex expressions to a help function, espescially when logic is repeated

### Know how to slice sequences

* `list`, `str` and `bytes` can be sliced
* The result of a slice is a whole new list, the original is not changed

Syntax is:

    somelist[start:end]

eg:
    a = [1, 2, 3, 4]
    a[:2]
    a[:5]
    a[0:5]

## Avoid Using start, end, and stride in a Single Slice

    somelist[start:end:stride]

The stride lets you take every `nth` item

    >>> colours = ['red', 'orange', 'yellow', 'blue', 'green']
    >>> colours[::2]
    ['red', 'yellow', 'green']

* Can be very confusing, espescially negative strides
* Avoid `start` and `end` when doing a stride
* Use `itertools` module `islice` function if necessary

## Use List Comprehensions Instead of map and filter

List comprehensions derive one list from another

    >>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> [x**2 for x in numbers]
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Preferable over using `map` that requires a lambda

    squares = map(lambda x: x ** 2, a)

You can also use lsit comprehensions to filter with an if:

    [x**2 for x in numbers if x % 2 == 0]

which can be achieved with `map` and `filter`:

    alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
    list(alt)

There are also list comprehensions for `dict` and `set`

    chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
    # dict comprehension
    rank_dict = {rank: name for name, rank in chile_ranks.items()}
    # set comprehensoin
    chile_len_set = {len(name) for name in rank_dict.values()}

## Avoid More Than Two Expressions in List Comprehensions

List comprehensions support multiple loops

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]

and multiple if conditions

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [x for x in a if x > 4 if x % 2 == 0]
    c = [x for x in a if x > 4 and x % 2 == 0]


You can also use conditions at each level:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)

But this is horrendous for someone else to comprehend

## Consider Generator Expressions for Large Comprehensions

* List comprehensions create a new list with at most the same number of values in the input sequence
* For large inputs this may cause the program to crash due to memory usage
* To solve this, Python provides generator expressions, a generalization of list comprehensions and `generators`
* generator expressions evaluate to an iterator that yields one item at a time from the expression

> When you’re looking for a way to compose functionality that’s operating on a large stream of input, generator expressions are the best tool for the job

it = (len(x) for x in open('/tmp/my_file.txt'))

gen = (print(i) for i in [9,1,2,3,3,])
print(next(gen))

## Prefer Enumerate over Range

If you need the index use `enumerate`, Python `enumerate` wraps any iterator with a lazy generator

As opposed to:

    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print('{}: {}'.format(i + 1, flavor))

consider (and setting where enumerate should being counting):

    for i, flavor in enumerate(flavor_list, 1):
        print('{}: {}'.format(i  , flavor))




