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

### Avoid Using start, end, and stride in a Single Slice

    somelist[start:end:stride]

The stride lets you take every `nth` item

    >>> colours = ['red', 'orange', 'yellow', 'blue', 'green']
    >>> colours[::2]
    ['red', 'yellow', 'green']

* Can be very confusing, espescially negative strides
* Avoid `start` and `end` when doing a stride
* Use `itertools` module `islice` function if necessary

### Use List Comprehensions Instead of map and filter

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

### Avoid More Than Two Expressions in List Comprehensions

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

### Consider Generator Expressions for Large Comprehensions

* List comprehensions create a new list with at most the same number of values in the input sequence
* For large inputs this may cause the program to crash due to memory usage
* To solve this, Python provides generator expressions, a generalization of list comprehensions and `generators`
* generator expressions evaluate to an iterator that yields one item at a time from the expression

> When you’re looking for a way to compose functionality that’s operating on a large stream of input, generator expressions are the best tool for the job

it = (len(x) for x in open('/tmp/my_file.txt'))

gen = (print(i) for i in [9,1,2,3,3,])
print(next(gen))

### Prefer Enumerate over Range

If you need the index use `enumerate`, Python `enumerate` wraps any iterator with a lazy generator

As opposed to:

    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print('{}: {}'.format(i + 1, flavor))

consider (and setting where enumerate should being counting):

    for i, flavor in enumerate(flavor_list, 1):
        print('{}: {}'.format(i  , flavor))

### Use zip to process iterators in parrallel

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

For processing a list and derived list simulateously you can use `enumerate` to get the index:

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

But python provides `zip`, that wraps 2 or more iterators with a lazy generator.
The zip generator yields tuples containing the next value from each iterator

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

* If the iterators supplied are not the same length, it keeps going until 1 is exhausted.
* `zip` will truncate quietly

### Avoid Else blocks after for and while

    for i in range(3):
        print('Loop {}'.format(i))
    else:
        print('Else block!')

Python weirdly has an else after a `for` and that makes it difficult for new programmers.
The reason is it works more like an `except` because the `else` part will run at the end of the loop.
So it will execute regardless of whether the loop was entered or not.

* A `break` statement in the `for` part will skip the `else` block
* The behaviour is not *obvious** or **intuitive**

### Take Advantage of Each Block in try/except/else/finally

#### Finally Blocks

Use `try...finally` when you want exceptions to propagate up but you also want to run cleanup code when exceptions occur.

    handle = open('/tmp/random_data.txt')  # May raise IOError
    try:
        data = handle.read()  # May raise UnicodeDecodeError
    finally:
        handle.close()        # Always runs after try:

#### Else Blocks

* When the `try` block doesn’t raise an exception, the `else` block will run.
* The `else` block helps you **minimize the amount of code in the try block and improves readability**

    def load_json_key(data, key):
        try:
            result_dict = json.loads(data)  # May raise ValueError
        except ValueError as e:
            raise KeyError from e
        else:
            return result_dict[key]

If decoding is successful the result key is returned if there is a `KeyError` that propagtes up to the caller

#### Everything together Try...Except...Else...Finally

    UNDEFINED = object()

    def divide_json(path):
        handle = open(path, 'r+')   # May raise IOError
        try:
            data = handle.read()    # May raise UnicodeDecodeError
            op = json.loads(data)   # May raise ValueError
            value = (
                op['numerator'] /
                op['denominator'])  # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)    # May raise IOError
        return value
    finally:
        handle.close()          # Always runs”

## Functions

Best organisation tool that help break up large programs into smaller pieces.
They improve readibility and make code more approachable.

### Prefer Exceptions to Returning None

There’s a draw for Python programmers to give special meaning to the return value of None

A helper function that divides one number by another. In the case of dividing by zero, returning None seems natural because the result is undefined.

    def divide(a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return None

Using the function:

    result = divide(x, y)
    if result is None:
        print('Invalid inputs')

The problem is what if the numerator is 0 and denominator not zero, that returns 0.
Then when you evaluate in an `if` condition and look for false istead of `is None`

That is why returning `None` is error prone

There are two ways to fix this, the first is returning a two tuple of `(success_flag, result)`
The problem is that some will just ignore that with the `_` for unused variables

The better way is to not return `None` at all, rather raise an exception and have them deal with it.

    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            raise ValueError('Invalid inputs') from e

I would even not raise the `ValueError`

It is then handled better on the caller (no check for None):

    x, y = 5, 2
    try:
        result = divide(x, y)
    except ValueError:
        print('Invalid inputs')
    else:
        print('Result is %.1f'.format(result))

    >>>
    Result is 2.5

> Raise eceptions instead of returning None

### Know How Closures Interact with Variable Scope

* closures: functions that refer to variables from the scope in which they were defined
* functions are first class objects: you can refer to them directly, assign them to variables, pass them as arguments to other functions

When you reference a variable the python interpreter resolves the reference in this order:
1. Current function's scope
2. Any enclosing scopes
3. Scope of the module containing the code (__global scope__)
4. The built-in scope (python built in functions: `len`, `str`, etc.)

If none of these find the reference a `NameError` is raised.

> Assigning a value to a variable works differently. If the variable is already defined in the current scope, then it will just take on the new value. If the variable doesn’t exist in the current scope, then Python treats the assignment as a variable definition

    def sort_priority2(numbers, group):
        found = False         # Scope: 'sort_priority2'
        def helper(x):
            if x in group:
                found = True  # Scope: 'helper' -- Bad!
                return (0, x)
            return (1, x)
        numbers.sort(key=helper)
        return found

So how do you get the data out:

The `nonlocal` statement is used to indicate that scope traversal should happen upon assignment for a specific variable name. It won't go up the module level.

    def sort_priority3(numbers, group):
        found = False
        def helper(x):
            nonlocal found
            if x in group:
                found = True
                return (0, x)
            return (1, x)
        numbers.sort(key=helper)
        return found

* It’s complementary to the `global` statement, which indicates that a variable’s assignment should go directly into the module scope.
* When your usage of nonlocal starts getting complicated, it’s better to wrap your state in a helper class.
* By default, closures can’t affect enclosing scopes by assigning variables.
* Avoid `nonlocal`

A class can be used to make it much easier to read:

    class Sorter(object):
        def __init__(self, group):
            self.group = group
            self.found = False

        def __call__(self, x):
            if x in self.group:
                self.found = True
                return (0, x)
            return (1, x)

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert sorter.found is True

### Consider Generators Instead of Returning Lists








