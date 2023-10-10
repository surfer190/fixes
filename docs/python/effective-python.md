---
author: ''
category: Python
date: '2020-06-14'
summary: ''
title: Effective Python
---
# Effective Python Summary Notes

I've been wanting to learn and improve my python so I read a book and took notes from `Effective Python - Brett Slatkin`. He has [some good tech reads on his blog](https://www.onebigfluke.com/).

## Pythonic Thinking

### 1. Know which python version you are using

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

### 2. Follow PEP8 Style Guide

Conistent style makes code more approachable and easy to read
Facilitates collaboration

[Read the pep8 style guide](https://www.python.org/dev/peps/pep-0008/)

### 3. Know the Differences Between bytes, str, and unicode

In python 3 there is `bytes` and `str`.
`str` contain unicode values
`bytes` contain raw 8-bit values

* You need to use `encode` and `decode` to convert unicode to `bytes`
* Do encoding and decoding at the furtherest boundary of the interface (so core of program works with unicode)
* bytes and str instances are never equivalent (In python 3)
* File handles (using `open`) default to UTF-8 encoding

Ensure to use `wb` write-banary mode as opposed to just `w` wrote character mode:

    with open('/tmp/random.bin', 'wb') as f:

When reading a file you can specify the mode:

    with open('data.bin', 'r', encoding='cp1252') as f:
        ....

Get the default encoding on your system:

    python3 -c 'import locale; print(locale. getpreferredencoding())'
    UTF-8

### 4. Prefer Interpolated f-strings over C-style format and str.format

C-style format:

    a = 0b1011010
    b = 0xc5f
    print('Binary is %d, hex is %d' % (a,b))
    
    Binary is 187, hex is 3167

Problems with C-style format:

* Changing the order of the tuple makes the expression fail also changing the format and keeping the order, same error
* Tuple and format becomes long forcing splitting across lines - hurting readability
* Using the same value multiple times, must duplicate in tuple
* redundancy in dictionaries

Advanced string formatting:

    a = 1234.5678
    formatted = format(a, ',.2f')
    print(formatted)
    1,234.57

Instead of c-style formatting you can use placeholders `{}`, which are replaced by positional arguments:

    key = 'my_key'
    value = 1244
    '{} = {}'.format(key, value)
    my_key = 1244

You can optionally format the placeholder with a colon character:

    formatted = '{:<10} = {:.2f}'.format(key, value)
    print(formatted)
    my_key     = 1244.00

The formatting per class can be customised per class with `__format__`

With C-style and formatting you need to double the special character to insure it is not interpreted.

    print('%.2f%%' % 12.5)
    12.50%
    
    print('{} replaces {{}}'.format(1.23))
    1.23 replaces {}

Positional index can be specified when formatted:

    formatted = '{1} = {0}'.format(key, value) 
    print(formatted)
    1244 = my_key

The same index can be used multiple times, not needing the value to be passed again.

    formatted = '{0} loves food. {0} loves eating.'.format('john')
    print(formatted)
    john loves food. john loves eating.

> Using `str.format` is not recommended

#### Interpolated format strings

Python 3.6 added interpolated format strings.

You precede the string with `f`, like `b` for byte-strings and `r` for raw unescaped strings.

f-strings remove the redundancy of declaring the strings to be formatted.

    formatted = f'{key} = {value}'
    my_key = 1244

The format specifiers are still available

    formatted = f'{key!r:<10} = {value:.2f}'
    'my_key'   = 1244.00

Comparison:

    f_string = f'{key:<10} = {value:.2f}'
    c_tuple = '%-10s = %.2f' % 0key, value)
    str_args = '{:<10} = {:.2f}'.format(key, value)
    str_kw = '{key:<10} = {value:.2f}'.format(key=key, value, value)
    c_dict = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}

F-strings let you put a full python expression in 
    
    pantry = [('plums', 2), ('horse raddish', 1), ('corn', 4)]

    for i, (item, count) in enumerate(pantry):
        f_string = f'#{i+1}: {item.title():<15s} = {round(count)}'
        print(f_string)
    
Results:

    $ python f_string.py 
    #1: Plums           = 2
    #2: Horse Raddish   = 1
    #3: Corn            = 4

You can even use a parameterised format:

    places = 3
    number = 1.23456
    print(f'My number is {number:.{places}f}')
    My number is 1.235

> Choose f-strings


### 5. Write helper functions, instead of complex expressions

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

* Use complex expressions to a help function, especially when logic is repeated

### 6. Prefer Multiple Assignment Unpacking over Indexing

Python uses `tuples` to create immutable, ordered sequences of values.

    snack_calories = {
        'chips': 140,
        'popcorn': 80,
        'nuts': 190,
    }
    items = tuple(snack_calories.items())
    print(items)

* You can access an item in a tuple with the index.
* Once created, you cannot modify a tuple value

#### Unpacking

Python has syntax to let you unpack a tuple into variables.

    item = ('Peanut butter', 'Jelly')
    first, second = item # Unpacking
    print(first, 'and', second)

There is less noise in the code than using indexes

> The same unpacking logic applies to more complex structures: unpacking lists of tuples

You can also swap items in place:

    a[i -1], a[i] = a[i], a[i - 1]

> There is usually no need to access anything by indexes

> Avoid indexing where possible

### 7. Prefer Enumerate over Range

If you need the index use `enumerate`, Python `enumerate` wraps any iterator with a lazy generator

As opposed to:

    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print(f'{i + 1}: {flavour}')

consider (and setting where enumerate should start counting from):

    for i, flavor in enumerate(flavor_list, 1):
        print(f'{i}: {flavour}')

`enumerate`  yields pairs of the loop index and the next value from the given iterator.

    flavour_list = ['chocolate', 'strawberry', 'bubblegum']
    it = enumerate(flavour_list)
    print(next(it))
    (0, 'chocolate')
    print(next(it))
    (1, 'strawberry')
    print(next(it)
    (2, 'bubblegum')

That is why unapacking works:

    for index, value in enumerate(flavour_list):
        ...

### 8. Use zip to process iterators in parrallel

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

    print(longest_name)

* If the iterators supplied are not the same length, it keeps going until 1 is exhausted.
* `zip` will truncate quietly

You can use `itertools.zip_longest` to always extinguish the longest list and use fill values:

    import itertools
    for name, count in itertools.zip_longest(names, counts):
        print(f'{name}: {count}')

### 9. Avoid Else blocks after for and while

    for i in range(3):
        print('Loop {}'.format(i))
    else:
        print('Else block!')

Python weirdly has an else after a `for` and that makes it difficult for new programmers.
The reason is it works more like an `except` because the `else` part will run at the end of the loop.
So it will execute regardless of whether the loop was entered or not.

* A `break` statement in the `for` part will skip the `else` block
* The behaviour is not **obvious** or **intuitive**

This is also the case with a `while` loop:

    while False:
        print('Never Runs!')
    else:
        print('While Else block runs!')

### 10. Prevent Repitition with Assignment Expressions

> The infamous _walrus operator_

Introduced in python 3.8. 

    a := b

pronounced, _a walrus b_

They allow you to assign variabled in places where assignment is disallowed.

For example, we want to make sure there is at least 1 lemon to squeeze for lemonade.

    fresh_fruit = {
        'apple': 10,
        'banana': 8,
        'lemon': 5,
    }

    def make_lemonade(count):
        ...
    def out_of_stock():
        ...

    count = fresh_fruit.get('lemon', 0)
    if count:
        make_lemonade(count)
    else:
        out_of_stock()

The problem above is the `count` variable is only used in the `if` portion of the if statement.

So we could rewrite the above as:

    if count:= fresh_fruit.get('lemon', 0):
        make_lemonade(count)
    else:
        out_of_stock()

If I needed more than 4 apples for cider:

    if (count := fresh_fruit.get('apple', 0)) >= 4:
        make_cider(count)
    else:
        out_of_stock()

> You need to surround the assignment with parenthesis for it to work

Used to improve the imitation of the `switch/case` statements:

    if (count := fresh_fruit.get('banana', 0)) >= 2:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    elif (count := fresh_fruit.get('apple', 0)) >= 4:
        to_enjoy = make_cider(count)
    elif count := fresh_fruit.get('lemon', 0):
        to_enjoy = make_lemonade(count)
    else:
        to_enjoy = 'Nothing'

> Improvements on readability and indentation

* The `assignment` expression both assigns and evaluates
* If it is a subexpression it needs parenthesis

## Lists and Sequences

### 11. Know how to slice sequences

* `list`, `str` and `bytes` can be sliced
* The result of a slice is a whole new list, the original is not changed

Syntax is:

    somelist[start:end]

eg:
    a = [1, 2, 3, 4]
    a[:2]
    a[:5]
    a[0:5]

### 12. Avoid Striding and slicing in a single Expression

    somelist[start:end:stride]

The stride lets you take every `nth` item

    >>> colours = ['red', 'orange', 'yellow', 'blue', 'green']
    >>> colours[::2]
    ['red', 'yellow', 'green']

* Can be very confusing, especially negative strides
* Avoid `start` and `end` when doing a stride
* Use `itertools` module `islice` function if necessary

### 13. Prefer Catch all unpacking over Slicing

A limitation of unpacking is you need to know the number of items in the list or sequence.

    car_ages = [10, 0, 5, 6, 16, 21, 8]
    car_ages_descending = sorted(car_ages, reverse=True)
    oldest, second_oldest = car_ages_descending

You get an error:

    ValueError: too many values to unpack (expected 2)

Newcomers will overcome this with indexing - which can become messy and noisy.
Also error prone to the off by one error/

The solution invovles python's **catch-all unpacking with a starred expressions**.
If allows one part of the expression to match any other part of the matching pattern.

    oldest, second_oldest, *others = car_ages_descending    
    print(oldest, second_oldest, others)
    21 16 [10, 8, 6, 5, 0]

A starred expression can appear anywhere:

    oldest, *others, youngest = car_ages_descending
    print(oldest, others, youngest)
    21 [16, 10, 8, 6, 5] 0

* You cannot use a catch-all expression on its owns
* You cannot use multiple catch-alls

Catchalls become lists in all instances, if no items - it comes an empty list.

The danger is if the catchall catches an iterator too large for memory - always know the size is smaller than memory.

### 14. Sort by Complex Criteria using the key parameter

The `list` built-in type provides a `sort` method for ordering items in a list based on criteria.

By default `.sort()` will order in ascending order.

    numbers = [55, 78, 13, 0, 12, -8]
    numbers.sort()
    print(numbers)
    [-8, 0, 12, 13, 55, 78]

It works for nearly all built-in types, but won't for your custom class if it the class cannot be compared.

Example `Tool` class:

    class Tool:
        def __init__(self, name, weight):
            self.name = name
            self.weight = weight

        def __repr__(self):
            return f'Tool({self.name!r}, {self.weight}'


    if __name__ == "__main__":
        tools = [
            Tool('level', 3.5),
            Tool('hammer', 1.25),
            Tool('screwdriver', 0.5),
            Tool('chisel', 0.25),
        ]

        tools.sort()

You will get an error:

    TypeError: '<' not supported between instances of 'Tool' and 'Tool'

Often there is an attribute of the class that can be used for ordering, for this `sort()` accepts a `key` parameter - that is expecter to be a function. In this case we will use the lambda keywork to represent the name.

    tools.sort(key=lambda x: x.name)
    print(tools)
    [Tool('chisel', 0.25, Tool('hammer', 1.25, Tool('level', 3.5, Tool('screwdriver', 0.5]

You can use any attribute that has a natural order.

They can also be used to transform and sort in one, eg. for a string type `lambda x: x.lower()`

What about sorting on more than 1 criteria:

* Tuples are comparable by default and have a natural ordering, meaning that they implement all of the special methods, such as `__lt__`, that are required by the sort method.

You can take advantage of this by sorting the tuple:

    tools.sort(key=lambda x: (x.weight, x.name))
    print(tools)
    [Tool('chisel', 0.25, Tool('screwdriver', 0.5, Tool('hammer', 1.25, Tool('level', 3.5]

One disadvantage is they must all be in ascedning order or descending (with the `reverse=True` paramter)

    tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
    [Tool('level', 3.5, Tool('hammer', 1.25, Tool('screwdriver', 0.5, Tool('chisel', 0.25]

More edge cases in the book...

### 15. Be Cautious when Relying on Dict Insertion Ordering

In Python3.5 and prior - iterating over dictionary would return keys in random order.
The order of iteration would not match the order of insertion.

Functions `keys`, `values`, `items` and `popitem` would also show this behaviour - prior to python 3.6.

There are many repercussions to this change.

`**kwargs` would come in any order.

Classes also use the `dict` type for their instance dictionaries `__dict__`

`collections` used to be the goto for `OrderedDict` class that preserved insertion ordering - it may still be preferable over python's `dict` due to the speed.

Python makes it easy to define custom container types for standard protocols `list`, `dict` and others.

> Python is not statically typed - so most code relies on duck typing - where an object's behaviour is its defacto type - instead of rigid class hierachies.

When you don't get the `dict` object but a similar duck typed object you have 3 options:

1. Change your program to expect different objects
2. Check the expected type and raise an Exception if it is different
3. Use a type annotation to ensure it is a `dict` instance and not a `MutableMapping` with `mypy`

Then check it with static analysis: `python3 -m mypy --strict example.py`

### 16. Prefer `get` over `in` and `KeyError` to handle Missing Dict Keys

    counters = {
        'pumpernickel': 2,
        'sourdough': 1,
    }

    count = counters.get(key, 0)
    counters[key] = count + 1

> There is a `Counter` class with a built-in `colletions` module

If you wanted to know who voted for each type:

    votes = {
        'baguette': ['Bob', 'Alice'],
        'ciabatta': ['Coco', 'Deb'],
    }
    key = 'brioche'
    who = 'Elmer'

    if key in votes:
        names = votes[key]
    else:
        votes[key] = names = []

    names.append(who)
    print(votes)

You could also use:

    names = votes.get(key)
    if names is None:
        votes[key] = names = []

or with an assignment expression:

    if (names := votes.get(key)) is None:
        votes[key] = names = []

    names.append(who)

> Not the most readable

`setdefault` fetches the value of a key - if it isn't repsent it assigns the default value provided.

    names = votes.setdefault(key, [])
    names.append(who)

> `setdefault` is not self explanatory - it should be `get_or_set` so new developers would understand faster and without having to look at the docs.

Important that a new default value is set directly for each key and not copied. If the value assigned is modified after being set as the default it will change the key value.

> There are only a few circumstances in which using setdefault is the shortest way to handle missing dictionary keys, such as when the default values are cheap to construct, mutable, and there’s no potential for raising exceptions (e.g., list instances).

### 17. Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State

For the instance where you are creating a mechanism for storing countries and cities:

    class Visits:
        def __init__(self):
            self.data = {}

        def add(self, country, city):
            city_set = self.data.setdefault(country, set())
            city_set.add(city)

> hiding `setdefault` from the caller - a nicer interface for the caller

    visits = Visits()
    visits.add('Russia', 'Yekaterinburg')
    visits.add('Tanzania', 'Zanzibar')
    print(visits.data)

    >>>
    {'Russia': {'Yekaterinburg'}, 'Tanzania': {'Zanzibar'}}

Using `defaultdict`:

from collections import defaultdict

    class Visits:
        def __init__(self):
            self.data = defaultdict(set)

        def add(self, country, city):
            self.data[country].add(city)
    
    visits = Visits()
    visits.add('England', 'Bath')
    visits.add('England', 'London')
    print(visits.data)

    >>> defaultdict(<class 'set'>, {'England': {'London', 'Bath'}})

### 18. Know how to construct key dependent values with `__missing__`

For example, say that I’m writing a program to manage social network profile pictures on the filesystem. I need a dictionary to map profile picture pathnames to open file handles so I can read and write those images as needed.

> You can subclass the dict type and implement the __missing__ special method to add custom logic for handling missing keys

    class Pictures(dict):
        def __missing__(self, key):
            value = open_picture(key)
            self[key] = value
            return value

    pictures = Pictures()
    handle = pictures[path]
    handle.seek(0)
    image_data = handle.read()

* The `setdefault` method of dict is a bad fit when creating the default value has high computational cost or may raise exceptions.
* The function passed to `defaultdict` must not require any arguments

## Functions

> Functions enable you to break large programs into smaller, simpler pieces with names to represent their intent. They improve readability and make code more approachable. They allow for reuse and refactoring.

### 19. Never Unpack more than 3 Variables when functions return Multiple Values

One effect of unpacking is it allows python functions to return more than 1 value

    def get_stats(numbers):
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum

    lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

    minimum, maximum = get_stats(lengths) # Two return values

Unpacking more than 3 makes it easy to reorder them - causing hard to spot bugs.

    # Correct:
    minimum, maximum, average, median, count = get_stats(lengths)

    # Oops! Median and average swapped:
    minimum, maximum, median, average, count = get_stats(lengths)

The line line might become very long - PEP8 forces next line - hurting readability

> Never unpack more than 3 - if you do want to unpack more than 3 you are better off defining a lightweight class or namedtuple

### 20. Prefer Raising Exceptions to Returning None



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
            value = (op['numerator'] / op['denominator'])
            # May raise ZeroDivisionError
        except ZeroDivisionError as e:
            return UNDEFINED
        else:
            op['result'] = value
            result = json.dumps(op)
            handle.seek(0)
            handle.write(result)    # May raise IOError
            return value
        finally:
            handle.close() # Always runs

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

Take getting the indices of words in a sentence:

    def index_words(text):
        result = []
        if text:
            result.append(0)
        for index, letter in enumerate(text):
            if letter == ' ':
                result.append(index + 1)
        return result

* It is dense and noisy
* One line for creating result list and one for returning it
* It requires all results to be stored in the list before being returned (inefficent use of memory)

The better way is to use a _generator_. When called, `generator` functions do not actually run but instead immediately return an iterator.

With each call to `__next__` of the iterator, it will advance to the next `yield` expression

    def index_words_iter(text):
        if text:
            yield 0
        for index, letter in enumerate(text):
            if letter == ' ':
                yield index + 1

* It is easier to read as references to the result list have been eliminated
* The iterator returned by the generator can be converted with `list()`
* Done line by line especially useful in a stream of reading from a file

### Be Defensive when Iterating over Arguments

**An iterator only produces its results a single time**

> If you iterate over an iterator or generator that has already raised a StopIteration exception, you won’t get any results the second time around

Using out previous example:

    address = 'Four score and seven years ago...'
    word_iterator = index_words_iter(address)
    print(list(word_iterator))
    print(list(word_iterator))

returns

    [0, 5, 11, 15, 21, 27]
    []

Also no exception is raised as python functions are looking for the `StopIteration` exception during normla operation. They don't know the difference between an Iterator with no output and an iterator whose output has been exhausted.

One way to fix this is to copy the results of the iterator but the output could be large and cause your program to crash.

The better way to achieve the same result is to provide a new container class that implements the iterator protocol

The iterator protocol is how Python for loops and related expressions traverse the contents of a container type. When Python sees a statement like for x in foo it will actually call iter(foo). The iter built-in function calls the `foo.__iter__` special method in turn. The `__iter__` method must return an iterator object (which itself implements the `__next__` special method). Then the for loop repeatedly calls the next built-in function on the iterator object until it’s exhausted (and raises a StopIteration exception).
It sounds complicated, but practically speaking you can achieve all of this behavior for your classes by implementing the `__iter__` method as a generator

    class WordIndexer:
        def __init__(self, text):
            self.text = text

        def __iter__(self):
            if self.text:
                yield 0
            for index, letter in enumerate(self.text):
                if letter == ' ':
                    yield index + 1

calling it with:

    word_index = WordIndexer(address)
    print(list( word_index))
    print(list( word_index))

Now `WordIndex` is a class that implements the _Iterator Protocal_ (A conatiner for an iterator).
Now we need to ensure that the iterator to a function is not an iterator:

    def normalize_defensive(numbers):
        '''When an iterator object is passed into iter() it returns the iterator,
        when a container is entered a new iterator is returned each time'''
        if iter(numbers) is iter(numbers):
            raise TypeError('Must supply a container')

### Reduce Visual Noise with Variable Positional Arguments

Optional positional arguments (`*args`) can make a function call more clear and remove visual noise.

Take this example:

    def log(message, values):
        if not values:
            print(message)
        else:
            values_str = ', '.join(str(x) for x in values)
            print('{}: {}'.format(message, values_str))

To just print out my message, I have to send an empty `[]`

    log('My numbers are', [1, 2])
    log('hello world', [])

You can tell python it is an optional parameters with:

    def log(message, *values):
        ...

 and then call it with:

    log('hello world')

You would need to change how you send values in though:

    favorites = [7, 33, 99]
    log('Favorite colors', *favorites)

The `*favourites` tells python to pass items from the sequence as positional arguments:

    *favourites == (7, 33, 99)
    favourites == ([7, 33, 99],)

There are a few problems:

1. The variable arguments are always turned into a tuple before they are passed to your function.

This could consume alot of memory on a generator as it is turned into a tuple.

> Functions that accept `*args` are best for situations where you know the number of inputs in the argument list will be reasonably small

2. You can’t add new positional arguments to your function in the future without migrating every caller

Ie. adding `def log(sequence, message, *values):` will break an existing call to `log('hello world')`

Bugs like this are hard ot track down.

Therefore you should use keyword only arguments when extending a function already accepting `*args`

### Provide Optional Behavior with Keyword Arguments

All positional arguments in python can also be called with keywords. They can be called:

    def remainder(number, divisor):
        return number % divisor

    assert remainder(20, 7) == 6
    assert remainder(20, divisor=7) == 6
    assert remainder(number=20, divisor=7) == 6
    assert remainder(divisor=7, number=20) == 6

One way it cannot be called is with:

    assert remainder(number=20, 7) == 6

as that raises: `SyntaxError: positional argument follows keyword argument`

Also each argument must be specified once:

    remainder(20, number=7)

gives: `TypeError: remainder() got multiple values for argument 'number'`

* Keyword arguments make function calls clearer to new readers of code
* They can have default values - reducing repetitive code and reducing noise (gets difficult with complex defaults)
* They provide a powerful way to extend a function's parameters while maintaining backwards compatibility with existing callfs

With a default period of per second:

    def flow_rate(weight_diff, time_diff, period=1):
        return (weight_diff / time_diff) * period

would be preferable to:

    def flow_rate(weight_diff, time_diff, period):
        return (weight_diff / time_diff) * period

You could also extend this without breaking existing calls with:

def flow_rate(weight_diff, time_diff,
              period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff) * period

The only problem with this is that optional arguments `period` and `units_per_kg` may still be specified as positional arguments.

    pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2) 

> The best practice is to always specify optional arguments using the keyword names and never pass them as positional arguments.

### Use None and Docstrings to specify dynamic default arguments

Sometimes you need to use a non-static type as a keyword arguments defualt value

For example when logging a message oyu want to include the time and date of the log:

    def log(message, when=datetime.datetime.now()):
        print('{}: {}'.format(when, message))

    log('Hi there!')
    sleep(0.1)
    log('Hi again!')

    >>> 2018-07-13 21:34:08.251207: Hi there!
    >>> 2018-07-13 21:34:08.251207: Hi again!

Remember `datetime.datetime.now` is **only run once, when the function is defined**

The convension for achieving the desired result is to set `when=None` and document how to use the function is a docstring.

    def log(message, when=None):
        '''Log a message with a timestamp

        Args:
            message: Message to print
            when: datetime of when the message occured
                Default to present time
        '''
        when = datetime.datetime.now() if when is None else when
        print('{}: {}'.format(when, message))

The `None` arugment is especially important for arguments that are mutable.
Say you want to decode some json with a default:

    def decode(data, default={}):
        try:
            return json.loads(data)
        except ValueError:
            return default

    foo = decode('bad data')
    foo['stuff'] = 5
    bar = decode('also bad data')
    foo['jink'] = '45'
    print('Foo:', foo)
    print('bar:', bar)

    >>> Foo: {'stuff': 5, 'jink': '45'}
    >>> bar: {'stuff': 5, 'jink': '45'}

Unforunately both `foo` and `bar` are both equal to the `default` parameter.
They are the same dictionary object being modified.

The fix is setting `default=None`

Change it like:

    def decode(data, default=None):
        if default is None:
            default = {}
        try:
            return json.loads(data)
        except ValueError:
            return default

* **Use None as the default argument for keyword arguments that have a dynamic value**
* Keyword arguments are evaluated once, at module load time

### Enforce Clarity with Keyword-Only Arguments

Say you have a function with signature:

def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    ...

Expecting the `ignore_overflow` and `ignore_zero_division` flags to be boolean. You can call it:

    >>> result = safe_division(1, 0, False, True)
    >>> result = safe_division(1, 10**500, True, False)

It is not clear what the boolean flags are and it is easy to confuse them.
One way to change this is to default them to false and callers must say which flags they want to switch.
The problem is you can still call it with:

    safe_division(1, 10**500, True, False)

In **python 3** you can demand clarity with keyword only arguments. These arguments can only be supplied by keyword never by position.

You do this using the `*` symbol in the argument list, which indicates the end of positional arguments and the beginning of keyword-only arguments.

    def safe_division_c(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
        ...

Now calling it badly:

    safe_division_c(1, 10**500, True, False)
    >>> TypeError: safe_division_c() takes 2 positional arguments but 4 were given

## Classes and Inheritance

Python supports `inheritance` (acquiring attribute and methods from a parent class), `polymorphism` (A way for multiple classes to implement their own unique versions of a method) and `encapsulation` (Restricting direct access to an objects attributes and methods)

### Prefer Helper functions over bookkeeping with tuples and dictionaries

When a class is getting very complex with many dictionaries and tuples within then it time to use classes, a **hierachy of classes**.

This is a common problem when scope increases (at first you didn't know you had to keep track of such and such). It is important to remember that **more than one layer of nesting is a problem**.

* Avoid dictionaries that contain ditionaries
* It makes your code hard to read
* It makes maintenance difficult

Breaking it into classes:

* helps create well defined interfaces encapsulating data
* A layer of abstraction between your interfaces and your concrete implementations

Extending tuples is also an issue, as associating more data now cause an issue with calling code.
A `namedtuple` in the `collections` module does exactly what you need...defining a tiny immutable data class.

Limitations of `namedtuple`:

* You cannot specify default argument values. With a handful of optional values a class is a better choice.
* Attributes are still accessible by numerical indices and iteration

A complete example:

    Grade = collections.namedtuple('Grade', ('score', 'weight'))


    class Subject(object):
        def __init__(self):
            self._grades = []

        def report_grade(self, score, weight):
            self._grades.append(Grade(score, weight))

        def average_grade(self):
            total, total_weight = 0, 0
            for grade in self._grades:
                total += grade.score * grade.weight
                total_weight += grade.weight
            return total / total_weight


    class Student(object):
        def __init__(self):
            self._subjects = {}

        def subject(self, name):
            if name not in self._subjects:
                self._subjects[name] = Subject()
            return self._subjects[name]

        def average_grade(self):
            total, count = 0, 0
            for subject in self._subjects.values():
                total += subject.average_grade()
                count += 1
            return total / count


    class Gradebook(object):
        def __init__(self):
            self._students = {}

        def student(self, name):
            if name not in self._students:
                self._students[name] = Student()
            return self._students[name]

Usage:

    book = Gradebook()
    albert = book.student('Albert Einstein')
    math = albert.subject('Math')
    math.report_grade(80, 0.10)
    print(albert.average_grade())
    >>> 80.0

It may have become longer but it is much easier to read

### Accept Functions for Simple Interfaces Instead of Classes

Python's built-in API's let you customise behavious by passing in a function.
Like the `list`, `sort` function that takes a `key` argument to determine the order.

Ordering by length:

    names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
    names.sort(key=lambda x: len(x))
    print(names)

    >>> ['Plato', 'Socrates', 'Aristotle', 'Archimedes']

Functions are ideal for hooks as tehy are easier to describe and simpler to define than classes.
Ie. better than using `Abstract Class`

* Functions are often all you need to interact(interface) between simple components
* The `__call__` special method enables instances of a class to behave like plain old python functions
* When you need a function to maintain state consider providing a class that provides a `__call__`

Refer to the book for more information...

### Use @classmethod Polymorphism to construct methods generically

Polymorphism is a way for multiple classes in a hierachu to implement their own unique version of a method.

> This allows many classes to fulfill the same interface or abstract base class while providing different functionality

Say you want a common class to represent input data for a MapReduce function, you create a common class to represent this.

    class InputData(object):
        def read(self):
            raise NotImplementedError

There is one version of a concrete subclass that reads from a file on disk:

    class PathInputData(InputData):
        def __init__(self, path):
            self.path = path

        def read(self):
            return open(self.path).read()

Now you could also have a class that reads from the network

Now we want a similar setup for a MapReduce worker to consume input data in a standard way

class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError

> Remember a concrete class is a class where all methods are completely implemented. An abstract class is one where functions are not fully defined (An abstract of a class).

The concrete subclass of `Worker`:

    class lineCountWorker(Worker):
        def map(self):
            data = self.input_data.read()
            self.data = data.count('\n')
        
        def reduce(self, other):
            self.result += other.result

Now the big hurdle...**What connects these pieces?**

I have a set of classes with reasonable abstractions and interfaces, but they are only useful once the class is constructed. What is responsible for building the objects and orchestrating the map reduce?

We can manually build this with helper functions:

    def generate_inputs(data_dir):
        for name in os.listdir(data_dir):
            yield PathInputData(os.path.join(data_dir, name))

    def create_workers(input_list):
        workers = []
        for input_data in input_list:
            workers.append(LineCountWorker(input_data))
        return workers

    def execute(workers):
        threads = [Thread(target=w.map) for w in workers]
        for thread in threads: thread.start()
        for thread in threads: thread.join()

        first, rest = workers[0], workers[1:]
        for worker in rest:
            first.reduce(worker)
        return first.result

    def mapreduce(data_dir):
        inputs = generate_inputs(data_dir)
        workers = create_workers(inputs)
        return execute(workers)

There is a big problem here. The **functions are not generic at all**.
If you write a different type of `InputData` or `Worker` subclass you would have to rewrite all of these functions. This boils down to **needing a generic way to construct objects**.

In other languages you could solve this problem with constructor polymorphism, making each subclass of `InputData` have a special constrcutor that can be used generically.

The problem is that python only has a single constructor method: `__init__`. It is unreasonable to require each subclass to have a compatible constructor.

The best way to solve this is with: `@classmethod` polymorphism

**Python class method polymorphism extends to whole classes, not just their constructed objects.**

> Remember polymorphism means to take on different forms

class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

`generate_inputs` takes a dictionary of configuration parameters than the concrete class must interpret.

class PathInputData(GenericInputData):
    def __init__(self, path):
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

> Similarly, I can make the create_workers helper part of the GenericWorker class. Here, I use the input_class parameter, which must be a subclass of GenericInputData, to generate the necessary inputs. I construct instances of the GenericWorker concrete subclass using `cls()` as a generic constructor.

    class GenericWorker(object):
        # ...
        def map(self):
            raise NotImplementedError

        def reduce(self, other):
            raise NotImplementedError

        @classmethod
        def create_workers(cls, input_class, config):
            workers = []
            for input_data in input_class.generate_inputs(config):
                workers.append(cls(input_data))
            return workers

The call to `input_class.generate_inputs` is the class polymorphism. Also the `cls(input_data)` provides an alternate way to instantiate instead of using `__init__` directly.

We can then just change the parent class:

    class LineCountWorker(GenericWorker):
        ...

and finally rewrite `mapreduce` to be more generic:

    def mapreduce(worker_class, input_class, config):
        workers = worker_class.create_workers(input_class, config)
        return execute(workers)

Calling the function now requires more parameters:

    with TemporaryDirectory() as tmpdir:
        write_test_files(tmpdir)
        config = {'data_dir': tmpdir}
        result = mapreduce(LineCountWorker, PathInputData, config)

### Initialise Parent classes with Super

Calling the parent class `__init__` mthod can ead to unpredictable behaviour especially with multiple inheritance as the `__init__`.

Python 2.2 introduced `super` and set the `MRO` - Method Resolution Order.
Python 3 introduced `super` with no arguments and it should be used because it is clear, concise and always does the right thing.

### Use Multiple Inheritance Only for Mix-in utility Classes

Python makes multi-inheritance possible and traceable, but is **better to avoid it altogether**.

If you want the encapsultion and convenience of multiple inheritance, use a _mixin_ instead.
A _mixin_ is a small utility class that only defines a set of additional methods a class should provide.

Mixin classses don't define their own instance attributes and don't require their `__init__` constructor to be called.

Example: you want the ability to convert a python object from its in-memory representation to a dictionary ready for serialisation.

    class ToDictMixin(object):
        def to_dict(self):
            return self._traverse_dict(self.__dict__)

        def _traverse_dict(self, instance_dict):
            output = {}
            for key, value in instance_dict.items():
                output[key] = self._traverse(key, value)
            return output

        def _traverse(self, key, value):
            if isinstance(value, ToDictMixin):
                return value.to_dict()
            elif isinstance(value, dict):
                return self._traverse_dict(value)
            elif isinstance(value, list):
                return [self._traverse(key, i) for i in value]
            elif hasattr(value, '__dict__'):
                return self._traverse_dict(value.__dict__)
            else:
                return value

Using it:

    class BinaryTree(ToDictMixin):
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)),
                        right=BinaryTree(13, left=BinaryTree(11))
    )
    print(tree.to_dict())

The mixin methods can also be overriden.

Alot more to read on this in the book...

### Prefer public attributes of private ones

In python there are only 2 attribute visibility types: _private_ and _public_.

    class MyObject(object):
        def __init__(self):
            self.public_field = 5
            self.__private_field = 10
        
        def get_private_field(self):
            return self.__private_field

Public attribues can be accessed with `dot notation`:

    my_obj = MyObject()
    print(my_obj.public_field)

Private fields start with a double underscore `__` and can be accessed by methods of the containing class.

    print(my_obj.get_private_field())

Directly accessing a private atrribute gives an error:

    print(my_obj.__private_field)
    >>> AttributeError: 'MyObject' object has no attribute '__private_field'

* Class methods can access private attributes because they are declared within the class block]
* A subclass cannot access it's parent classes private fields

The python compiler just does a check on the calling class name, thereforethis works:

    class MyChildObject(MyObject):
        pass

    print(my_child_obj.get_private_field())
    >>> 10

but if MyChildObject held the `get_private_field()` method it would fail.

If you look at the `__dict__` of a object you can see parent attributes:

    (Pdb) my_child_obj.__dict__
    {'public_field': 5, '_MyObject__private_field': 10}

and accessing them is easy:

    print(my_child_obj._MyObject__private_field)

Why isn't visibility restricted? The python motto:

> “We are all consenting adults here.”

The benfits of being open outweigh the downsides of being closed.

To minimise the damage of accessing internals unknowingly follow the PEP8 naming conventions.
Fields prefixed with underscore(`_protected_fields`) are _protected_ meaning external users of the class should proceed with caution.

By choosing private fields you are making subclass overrides and extensions cumbersome and brittle. Then if these private references will break due to the hierachy changing.

It is better to allow subclasses to do more by using `_protected` attributes. Make sure to document their importance and that they be treated as _immutable_.

### Inherit from collections.abc for custom Container Types

Much of python is defining classes, data and how they relate. Each python class is a container of some kind.
Oftentimes when creating a sequence you will extend (inherit from) `list`.

But what about a BinaryTree that you want to allow indexing for, that isn't a list but is similar.

class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

You can access an item with `obj.__getitem__(0)` ie. `obj[0]`

class IndexableNode(BinaryNode):
    def _search(self, count, index):
        # ...
        # Returns (found, count)

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value

But then you would also need implementations of `__len__`, `count` and `index`

You should use an abstract base class (`abc`) from `collections`:

    from collections.abc import Sequence

Then once you implement the `__gettitem__` and `__len__` the other methods come for free.

* You can still inherit directly from python's container types `list` and `dict` for simple cases

## Metaclasses and Attributes

_Metaclass_ let you intercept python's `class` statement to provide special behviour each time it is defined.

Remember to follow the rule of **least surprise**

### Use Plain attributes instead of Get and Set Methods

These can be done in python and may be seen as good to:

* encapsulate functionality
* validate usage
* define boundaries

In python, you never need to do this. Always start with simle public attributes. 

If you need special behaviour you can us `@property` and the `setter` method. This also helps to add validation and type checking.

    class BoundedResistance(Resistor):
        def __init__(self, ohms):
            super().__init__(ohms)

        @property
        def ohms(self):
            return self._ohms

        @ohms.setter
        def ohms(self, ohms):
            if ohms <= 0:
                raise ValueError('%f ohms must be > 0' % ohms)
            self._ohms = ohms

> Don't set other attributes in getter property methods. Only modify related object state in `setters`

If you are doing something slow and complex, rather do it in a normal method. People are expecting this to behave like a property.

### Consider @property Instead of Refactoring Attributes

> “One advanced but common use of @property is transitioning what was once a simple numerical attribute into an on-the-fly calculation”

Check the book for a good example...

* Use `@property`to give existing instance attributes new functionality
* Make incremental progress towards better data models
* Consider refactoring a class when using a `@property` too regularly
### Use Descriptors for reusable @property methods

The big problem with `@property` is reuse. The methods it decorates cannot be reused for multiple attributes in the same class or external classes.

Take the example:

    class Exam(object):
        def __init__(self):
            self._writing_grade = 0
            self._math_grade = 0

        @staticmethod
        def _check_grade(value):
            if not (0 <= value <= 100):
                raise ValueError('Grade must be between 0 and 100')

        @property
        def writing_grade(self):
            return self._writing_grade

        @writing_grade.setter
        def writing_grade(self, value):
            self._check_grade(value)
            self._writing_grade = value

        @property
        def math_grade(self):
            return self._math_grade

        @math_grade.setter
        def math_grade(self, value):
            self._check_grade(value)
            self._math_grade = value

We are duplicating properies and the grade validations.
The better way to do this is to use a _descriptor_, that describes how attribute access is interpreted by the language.
* Provide `__get__` and `__set__` methods to reuse grade validation behaviour. 
* They are better than mixins at this because you can reuse the same logic for many attributes in the same class.

The class implementing descriptor:

    class Grade(object):
        def __get__(*args, **kwargs):
            # ...

        def __set__(*args, **kwargs):
            # ...

The exam:

    class Exam(object):
        # Class attributes
        math_grade = Grade()
        writing_grade = Grade()
        science_grade = Grade()

Assigning properties:

    exam = Exam()
    exam.writing_grade = 40

    # Which is really
    Exam.__dict__['writing_grade'].__set__(exam, 40)

Retrievingproperties:

    print(exam.writing_grade)

    # Which is really
    print(Exam.__dict__['writing_grade'].__get__(exam, Exam))

In short, when an Exam **instance** doesn’t have an attribute named writing_grade, Python will fall back to the Exam class’s attribute instead. If this class attribute is an object that has `__get__` and `__set__` methods, Python will assume you want to follow the descriptor protocol.

There are still many gotchas here you can go through in the book...

### Use __getattr__, __getattribute__, and __setattr__ for Lazy Attributes

Read the book...

### Validate subclasses with Meta Classes

* Use metaclasses to ensure that subclasses are well formed at the time they are defined, before objects of their type are constructed.
* The `__new__` method of metaclasses is run after the class statement’s entire body has been processed.

### Register Class Existence with Metaclasses

Hectic topic...read the book

### Annotate Class Attributes with Metaclasses

Again...hectic

## Concurrency and Parrallelism

Concurrency is when a computer does many different things _seemingly_ at the same time. Interleaving execution of a program making it seem like it is all being done the same time.

Parallelism is _actually_ doing many different things at the same time.

Concurrency provides no speedup for the total work.

These topics are a bit too hectic for now... you are welcome to read the book...I will leave the headings here

### Use Subprocess to manage Child processes

Read full details in the book...

### Use Threads for Blocking I/O, Avoid Parrallelism

Read full details in the book...

### Use Lock to Prevent Data Races in Threads

Read full details in the book...

### Use Queue to Coordinate Work between Threads

Read full details in the book...

### Consider Coroutines to Run Many Functions Concurrently

Read full details in the book...

### Consider concurrent.futures for True Parrallelism

Read full details in the book...Item 41

## Built-in Modules

Python takes a _batteries included_ approach to the standard library. Some of these built-in modules are closely intertwined with idiomatic python they may as well be part of the language specification.

### Define Function Decorators with functools.wraps

Decorators have the ability to run additional code before or after any calls to the function they wrap. This allows them to access and modify input arguments and return values.

Say you want to print aruments and return values for a recursive function call:

    def trace(func):
        '''Decorator to display input arguments and return value'''
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{ func.__name__ }({ args },{ kwargs }) -> { result}')
            return result
        return wrapper

You can apply this function with the `@` symbol

    @trace
    def fibonacci(n):
        '''Return the n-th fibonacci number'''
        if n in (0, 1):
            return 1
        return fibonacci(n-1) + fibonacci(n-2)

The `@` symbol is equivalent to calling: `fibonacci = trace(fibonacci)`

Testing it:

    result = fibonacci(3)
    print(result)

gives:

    fibonacci((1,),{}) -> 1
    fibonacci((0,),{}) -> 1
    fibonacci((2,),{}) -> 2
    fibonacci((1,),{}) -> 1
    fibonacci((3,),{}) -> 3
    3

There is however an unintended side effect, the function returned does not think it is called `fibonacci`.

    print(fibonacci)
    <function trace.<locals>.wrapper at 0x108a0fbf8>

The `trace` function returns the `wrapper` it defines. The `wrapper` function is what is assigned to the `fibonacci` name with the decorator. The problem is that is undermines debuggers and object serialisers.

For example the help is useless:

    >>> from test import fibonacci
    >>> help(fibonacci)
    Help on function wrapper in module test:

    wrapper(*args, **kwargs)

The solution is to use the `wraps` helper function from the `functools` built-in module.
**This is a decorator that helps you write decorators**

Applying it to `wrapper` copies the important metadata about the innner function to the outer function.
The important part below is **`@wraps(func)`**

    from functools import wraps

    def trace(func):
        '''Decorator to display input arguments and return value'''
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            ...

Now `help()` works well

    In [1]: from test import fibonacci
    In [2]: help(fibonacci)
    Help on function fibonacci in module test:

    fibonacci(n)
        Return the n-th fibonacci number

### Consider contextlib and with statements for reuasable try/finally behaviour

The `with` statement in python is used to indicate when code is running in a special context.

    lock = Lock()
    with lock:
        print('Lock is held')

is equivalent to:

    lock.acquire()
    try:
        print('Lock is held')
    finally:
        lock.release()

The `with` is better asit eliminates the need to write repetitive code.

> It’s easy to make your objects and functions capable of use in with statements by using the contextlib built-in module. This module contains the contextmanager decorator, which lets a simple function be used in with statements. This is much easier than defining a new class with the special methods `__enter__` and `__exit__` (the standard way).

There is more information in the book...Item 43

### Make pickle reliable with copyreg

The `pickle` built in module can serialize python objects into a strema of bytes and deserialise back into python objects. Pickle byte streams houldn't be used to communicate between untrusted parties. The purpose of pickle is to communicate between 2 programs you control over binary channels.

> The `pickle` module’s serialization format is unsafe by design. The serialized data contains what is essentially a program that describes how to reconstruct the original Python object. This means a malicious pickle payload could be used to compromise any part of the Python program that attempts to deserialize it.
In contrast, the `json` module is safe by design. Serialized JSON data contains a simple description of an object hierarchy. Deserializing JSON data does not expose a Python program to any additional risk. Formats like JSON should be used for communication between programs or people that don’t trust each other.

Say you have a class tracking the state of a game for a player:

    class GameState(object):
        '''Track the state of you game'''
        def __init__(self):
            self.level = 0
            self.lives = 4

You use and save the state of a player:

    state = GameState()
    state.level += 1
    state.lives -= 1

    state_path = '/tmp/game_state.bin'
    with open(state_path, 'wb') as f:
        pickle.dump(state, f)

You can later resume the game state with:

    state_path = '/tmp/game_state.bin'
    with open(state_path, 'rb') as f:
        state_after = pickle.load(f)

    print(state_after.__dict__)

But what if you add a new field to the state class? Serialising and deserialising a `GameState` instance will work but resuming the old state will not have the `points` attribute.

Even though the instance is of the `GameState` type.

Fixing these issues requires `copyreg`

#### Default attribute values

You can set default attribute values:

    def __init__(self, lives=4, level=0, points=0):
        ...

To use this constuctor for pickling, create a helper function that takes a `GameState` object and turns it into a tuple of parameters for the `copyreg`module.
The returned tuple contains the function and paramters to use when unpickling:

    def pickle_game_state(game_state):
        kwargs = game_state.__dict__
        return unpickle_game_state, (kwargs,)

Now I need `unpickle_game_state` that takes serialised data and parameters and returns a `GameState` object

    def unpickle_game_state(kwargs):
        return GameState(**kwargs)

Now register them with `copyreg`:

    import copyreg, pickle
    copyreg.pickle(GameState, pickle_game_state)

Unfortunately this worked for new objects, but did not work for me when deserialising the old saved pickle file.
The `unpickle_game_state` function was not run.

There is more info in the book on versioning of classes and providing stable import paths...

### Use datetime instead of local clocks

`UTC` Coordinated Universal Time is the standard timezone independent representation of time. It is good for computers but not great for humans as they need a reference point.

Use `datetime` with the help of `pytz` for conversions. The old `time` module should be avoided.

#### The time module

The `localtime` function from the `time` built-in module lets you convert unix time (from epock in seconds) to local time of the home computer.

    from time import localtime, mktime, strftime, strptime

    now = 1407694710
    local_tuple = localtime(now)

    time_format = '%Y-%m-%d %H:%M:%S'
    time_str = strftime(time_format, local_tuple)
    print(time_str)

    time_tuple = strptime(time_str, time_format)
    utc_now = mktime(time_tuple)
    print(utc_now)

    >>> 2014-08-10 20:18:30
    >>> 1407694710.0

The problem comes when converting time to other timezones. The `time` module uses the host platform/operating system and this has different formats and missing timezones.

**If you must use time, only use it for converting unixtime to the local pc time, in all other times use `datetime`**

#### The datetime module

You can use `datetime` to convert a time to your local timezone:

    now = datetime.datetime(2014, 8, 10, 18, 18, 30)
    now_utc = now.replace(tzinfo=datetime.timezone.utc)
    now_local = now_utc.astimezone()
    print(now_local)

Datetime lets you change timezones but it does not hold the definitions of the rules for the timezones.

Enter [pytz](https://pypi.org/project/pytz/) 

`pytz` holds the timezone information of every timezone you might need.
To use `pytz` effectively always convert first to `UTC` then to the target time.

Top tip, you can get all timezones with: `pytz.all_timezones`

In this example I convert a sydney flight arrivcal time into utc (note all these calls are required):

    import datetime
    import pytz

    time_format = '%Y-%m-%d %H:%M:%S'
    arrival_sydney = '2014-05-01 05:33:24'
    sydney_dt_naive = datetime.datetime.strptime(arrival_sydney, time_format)
    sydney = pytz.timezone('Australia/Sydney')
    sydney_dt = sydney.localize(sydney_dt_naive)
    utc_dt = pytz.utc.normalize(sydney_dt.astimezone(pytz.utc))
    print(utc_dt)

    >>> 2014-04-30 19:33:24+00:00

Now I can convert that UTC time to Johannesburg time:

    jhb_timezone = pytz.timezone('Africa/Johannesburg')
    jhb_dt = jhb_timezone.normalize(utc_dt.astimezone(jhb_timezone))
    print(jhb_dt)

    >>> 2014-04-30 21:33:24+02:00

### Use Built-in algorithms and data structures

When implementing programs with non-trivial amounts of data eventually you see slowdowns.
Most likely due to you not using the most suitable alorithms and data structures.
On top of speed, these algorithms also make life easier.

#### Double Ended Queue

The `deque` class from the `collections` module is a double ended queue.
Ideal for a FIFO (First in, firsdt out) queue

    from collections import deque
    fifo = deque()
    fifi.append(1)
    x = fife.popleft()

`list` also contains a sequence of items, you can insert or remove items from the end in constant time. Inserting and removing items from the head of the list takes liner time O(n) and constant time for a `deque` O(1)

#### Ordered Dictionary

Standard dictionaries are unordered. Meaning the same `dict` can have different orders of iteration.

The `OrderedDict` class from the `collections` module is a special type of dictionary that keeps track of the order keys were inserted. Iteracting through it has predictable behaviour.

    a = OrderedDict()
    a['one'] = 1
    a['two'] = 2
    b = OrderedDict()
    b['one'] = 'red'
    b['two'] = 'blue'

    for number, colour in zip(a.values(), b.values()):
        print(number, colour)

#### Default Dictionary

Useful for bookeeping and tracking statistics. 

With dictionaries you cannot assume a key is present, making it difficult to increase a counter for example:

    stats = {}
    key = 'my_counter'
    if key not in stats:
        stats['key'] = 0
    stats['key'] += 1

`defaultdict` automatically stores a default value when a key does not exist, all you need to do is to provide a function for when a key does not exist. In this case `int() == 0`

    from collections import defaultdict
    stats = defaultdict(int)
    stats['my_counter'] += 1

#### Heap Queue

Heaps are useful for maintaining a priority queue. The `heapq` module provides functions for creating heaps in standard `list` types with functions like `heappush`, `heappop` amd `nsmallest`.

Remember items are always removed with highest priority first (lowest number):

    a = []
    heapq.heappush(a, 5)
    heapq.heappush(a, 3)
    heapq.heappush(a, 7)
    heapq.heappush(a, 4)

    print(
        heapq.heappop(a),
        heapq.heappop(a),
        heapq.heappop(a),
        heapq.heappop(a)
    )

Accessing the list with `list[0]` always returns the smallest item:

    assert a[0] == nsmallest(1, a)[0] == 3

Calling the sort method on the list maintains the heap invariant.

    print('Before:', a)
    a.sort()
    print('After: ', a)

    >>>
    Before: [3, 4, 7, 5]
    After:  [3, 4, 5, 7]

`list` takes linear time, heap sort logarithmic.

#### Bisection

Search for an item in a list takes linear time proportional to it's length when you call the `index` method.

The `bisect` module's function `bisect_left` provides an efficient binary search through a sequence of srted items. The value it returns is the insertion point of the value into the sequence.

    x = list(range(10**6))
    i = x.index(991234)
    i = bisect_left(x, 991234)

Teh binay search is logarithmic.

#### Iterator Tools

`itertools` contains a large number of functions for organising and interacting with iterators.

There are 3 main categories:

1. Linking iterators together:

    * `chain` - Combines multiple iteractors into a single  sequential iterator
    * `cycle` - Repeat's an iterators items forever
    * `tee` - Splits a single iterator into multiple parrallel iterators
    * `zip_longest` - `zip` for iterators of differing lengths

2. Filtering:

    * `islice` - slices an iteractor by numerical indexes without copying
    * `takewhile` - returns items from an iteractor while predicate condition is true
    * `dropwhile` - returns items from an iteractor when previous function returns `False` he first time
    * `filterfalse` - Returns items from iteractor when predicate function returns false

3. Comnbinations:

    * `product` - returns cartesian product of items from an iterator
    * `permutations` - returns ordered permutations of length N with items from an iterator
    * `combination` - returns ordered combinations of length N with unrepeated items from an iterator


### Use decimal when precision is paramount

    rate = 1.45
    seconds = 3*60 + 42
    cost = rate * seconds / 60
    print(cost)

    print(round(cost, 2))

With floating point math and rounding down you get:

    5.364999999999999
    5.36

This wont do. The `Decimal` class provides fixed point math of 28 decimal points by default.
It gives you more precision and control over rounding.

    from decimal import Decimal, ROUND_UP
    rate = Decimal('1.45')
    seconds = Decimal('222')  # 3*60 + 42
    cost = rate * seconds / Decimal('60')
    print(cost)
    rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
    print(rounded)  

Gives:

    5.365
    5.37

Using the quantize method this way also properly handles the small usage case for short, cheap phone calls.
So it still returns `0` if it is zero, but `001` if it is `0.000000000001`.

### Know where to find Community built modules

Python has a central repo of modules called [pypi](https://pypi.org/), that are maintained by the community. 

## Collaboration

There are language features in python to help you construct well defined API's with clear interface boundaries.
The python community has established best practices that maximise the maintainability over time.
You need to be deliberate in your collaboration goal.

### Write docstrings for every function, class and module

Documentation is very important due to the dynamic nature of the language. Unlike other languages the documentation from source is available when a program runs.

You can add documentation imeediately after the `def` statement of a function:

    def palindrom(word):
        '''Return True if the given word is a palindrome'''
        return word == word[::-1]

You can retrive the docstring with:

    print(repr(palindrom.__doc__))

Consequences:

* Makes interactive development easier with `ipython` and using the `help` function
* A standard way of defining documentation makes it easier to build tools to convert it into more appealing formats like `html`: Like [sphinx](http://www.sphinx-doc.org/en/master/) or [readthedocs](https://readthedocs.org/)
* First class, accessible and good looking documentation encourages people to write it

#### Documenting Modules

Each module should ahve a top level doc string. 

    #!/usr/bin/env python3
    '''Single sentence describing modules purpose

    The paragraphs that follow should contain details that all
    users should know about

    It is a good place to highlight important features:
    - 
    -

    Usage information for command line utilities
    '''

#### Documenting Classes

Each class should have a docstring highlighting public attributes and methods, along with guidance on interating with protected attributes etc.

eg.

    class Player(object):
        """Represents a player of the game.

        Subclasses may override the 'tick' method to provide
        custom animations for the player's movement depending
        on their power level, etc.

        Public attributes:
        - power: Unused power-ups (float between 0 and 1).
        - coins: Coins found during the level (integer).
        ""”

#### Documenting Functions

Every public method and function should have a docstring. Similar to other docstrings with arguments at the end.

eg.

    def find_anagrams(word, dictionary):
        """Find all anagrams for a word.

        This function only runs as fast as the test for
        membership in the 'dictionary' container. It will
        be slow if the dictionary is a list and fast if
        it's a set.

        Args:
            word: String of the target word.
            dictionary: Container with all strings that
                are known to be actual words.”
        Returns:
            List of anagrams that were found. Empty if
            none were found.
        """

* If your function has no arguments and a simple return value, a single sentence description is probably good enough.
* If your function uses `*args` and `**kwargs` use documentation to describe their purpose.
* Default values should be mentioned
* Generators should describe what the generator yields


### Use packages to organise modules and provide stable APIs

As the size of a codebase grows it is natural to reogranise its structure into smaller functions.
You may find yourself with so many modules that another layer is needed.
For that python provides `packages` which are modules containing other modules.

In most cases `packages` are created by putting a `__init__.py` file into a directory.
Once that is present you can import modules from that package:

    main.py
    mypackage/__init__.py
    mypackage/models.py
    mypackage/utils.py

in `main.py`:

    from mypackage import utils

#### Namespaces

Packages let you divide modules into seperate namespaces.

    from analysis.utils import inspect as analysis_inspect
    from frontend.utils import inspect as frontend_inspect

When functions have the same name you can imports them as a different name

> Even better is to avoid the `as` altogether and access the function with the `package.module.function` way

#### Stable API

Python provides a strict, stable API for external consumers.
You will want to provide stable functionality that does not change between releases.

Say you want all functions in `my_module.utils` and `my_module.models` to be accessible via `my_module`.

You can, add a `__init__.py`:

    __all__ = []
    from . models import *
    __all__ += models.__all__
    from . utils import *
    __all__ += utils.__all__”

in `utils.py`:

    from . models import Projectile

    __all__ = ['simulate_collision']

    ...

in `models.py`:

    __all__ = ['Projetile', ]

    class Projectile:
        ...

Try avoid using `import *` as they can overwrite names existing in your module and they hide the source fo names of functions to new readers

### Define a root exception to insulate callers from APIs

> Python has a built-in hierarchy of exceptions for the language and standard library. There’s a draw to using the built-in exception types for reporting errors instead of defining your own new types

Sometimes raising a `ValueError` makes sense but it is much more powerful for an API to define its own hierachy of exceptions.

    # my_module.py
    class Error(Exception):
        """Base-class for all exceptions raised by this module."""

    class InvalidDensityError(Error):
        """There was a problem with a provided density value.""”

Having a root exception lets consumers of your API catch exceptions you raise on purpose. 

eg: We are specifically catching the `my_module.Error`

    try:
        weight = my_module.determine_weight(1, -1)
    except my_module.Error as e:
        logging.error('Unexpected error: %s', e)

These root exceptions:

* Let callers know there is a problem with the usage of the API
* If an exception is not caught properly it will propagate all the way up to an `except` - bringing attention to the consumer (Catching the Python `Exception` base class can help you find bugs)
* They help find bugs in your API code - so other exeptions (non-root) are one's you did not intend to raise
* Futureproof's API when expanding

        class NegativeDensityError(InvalidDensityError):
            """A provided density value was negative."""
            ...

The calling code will still work as it catches the parent `InvalidDensityError`


### Know How to Break Circular Dependencies

When collaborating with others you will have a mutual independency between modules. 

You have a dialog module, importing `app`:

    import app

    class Dialog(object):
        def __init__(self, save_dir):
            self.save_dir = save_dir
        # ...

    save_dialog = Dialog(app.prefs.get('save_dir'))

    def show():
        # ...

The `app` modules contains a `prefs` object that also imports the `dialog` class:

    import dialog

    class Prefs(object):
        # ...
        def get(self, name):
            # ...

    prefs = Prefs()
    dialog.show()

It is a `circular dependency` if you try to use the `app` module you will get:

    AttributeError: 'module' object has no attribute 'prefs'

So how does python's import work?...In dept first order:

1. Searches for your module in `sys.path`
2. Loads the code and ensures it compiles
3. Creates corresponding empty module object
4. Inserts the module into `sys.modules`
5. Runs the code in the module object to define its contents

The **attributes** of a module aren't defined until the code runs in step 5. But a module can be loaded immediately after it is inserted into `sys.modules`

The `app` module imports `dialog`. The `dialog` module imports `app`. 

`app.prefs` raises the error because `app` is just an empty shell at this point.

The best way to fix this is to ensure that `prefs` is at the bottom of the dependency tree.

Here are 3 approaches to breaking the circular dependency:

#### Reordering Imports

Import `dialog` at the bottom of `app`:

    class Prefs(object):
        # ...

    prefs = Prefs()

    import dialog  # Moved
    dialog.show()

This will avoid the `AttributeError` but it goes against `PEP8`

#### Import, Configure, Run

Have modules minimise side effects at import time.
Have modules only define `functions`, `classes` and `constants`
Avoid running any functions at import time.

Then each module provides a `configure` function once all other modules have finished importing. 

dialog.py:

    import app

    class Dialog(object):
        # ...

app.py:

    import dialog

    class Prefs(object):
        # ...

    prefs = Prefs()

    def configure():
        # ...

main.py:

    import app
    import dialog

    app.configure()
    dialog.configure()

    dialog.show() 

Then your `main.py` should:

1. Import
2. Configure
3. Run

This can make your code harder to read but will allow for the _dependency injection_ design pattern.

#### Dynamic Import

The simplest is to use an `import` statement in a function. A dynamic import as the importing is done when the program is running.

dialog.py:

    class Dialog(object):
        # ...

    save_dialog = Dialog()

    def show():
        import app  # Dynamic import

It requires no structural changes to the way modules are defined and imported. 
There are downsides: the cost can be bad especially inside loops, by delaying execution there may be surprising failures at runtime.


### Use Virtual Environments for isolated and reproducible Deendencies

Potencially use [pipenv](https://docs.pipenv.org/) in this case...

## Production

### Consider Module-scoped code to configure deployment environments

When putting things into production you have to rely on database configurations and these can be handled by your module, take a test and produciton database.

You can override parts of your program at startup time to provide different functionality:

dev_main.py:

    TESTING = True
    import db_connection
    db = db_connection.Database()

prod_main.py:

    TESTING = False
    import db_connection
    db = db_connection.Database()

The only difference is the value of `TESTING`

Then in your code you can decide which db to use with:

db_connection.py

    import __main__

    class TestingDatabase(object):
        # ...

    class RealDatabase(object):
        # ...

    if __main__.TESTING:
        Database = TestingDatabase
    else:
        Database = RealDatabase

> Once your deployment environments get complicated, you should consider moving them out of Python constants (like `TESTING`) and into dedicated configuration files. Tools like the `configparser` built-in module let you maintain production configurations separate from code, a distinction that’s crucial for collaborating with an operations team.

Another example is if you know your program works differently based on the host platform, you can inspect the `sys` module.

db_connection.py:

    import sys

    class Win32Database(object):
        # ...

    class PosixDatabase(object):
        # ...

    if sys.platform.startswith('win32'):
        Database = Win32Database
    else:
        Database = PosixDatabase

You can also get environment variables with: `os.environ`

### Use repr Strings for Debugging Output

`print` will get you surprisingly far when debugging.

The problem is that these human readable results don't show the type.

    >>> print('5')
    5
    >>> print(5)
    5

You always want to see the `repr` version which is the printable representation of an object.

    >>> print(repr('5'))
    '5'
    >>> print(repr(5))
    5

The `repr` of a class is not partocularly helpful although if you have control of th class you can define your own `__repr__` method to display the object:

    class BetterClass(object):
        def __init__(self, x, y):
            # ...

        def __repr__(self):
            return 'BetterClass(%d, %d)' % (self.x, self.y)

When you don't hve control over the class you can check the object's instance dictionary with `obj.__dict__`

### Test Everything with unittest

So many people don't do this (you should start with the test)

* Python doesn't have static type checking, so the compiler doesn't stop the program when types are wrong.
* You don't knwo whether functions will be defined at runtime.

This is a blessing by most python dev's because of the productivity gained from the brevity and simplicity.

Also type safety isn't everything and code needs to be tested. **You should always test your code no matter what language it is written in**. 

In python the only way to have _any_ confidence in your code is to write tests, there is no veil of static type checking to make you feel safe.

Tests are easy to write in python due to the same dynamic features like easily overridable behaviours.
Tests are insurance, giving you confidence your code is correct but also making it harder for future modification and refactoring to burden functionality.

The simplesdt way to write a tesdt is by using `unittest`.

[See more on writing Unit Tests](https://fixes.co.za/python/python-unit-tests/)

For more advance testing libraries see [pytest](https://docs.pytest.org/en/latest/) and [nose](http://nose.readthedocs.io/en/latest/)

### Consider Interactive Debugging with pdb

Everyone encounters bugs.
Writing tests isolates code but does not help you find the root cause of issues.

You should use pythons built-in `interactive debugger`

Other programming languages make you put a breakpoint on a certain line. The python debugger differs in that you directly initiate the debugger in the code.

All you need to do is add: `import pdb; pdb.set_trace()`

    def complex_func(a, b, c):
        # ...
        import pdb; pdb.set_trace()

As soon as the statement runs, execution is paused and you can inspect local variables.
You can use `locals`, `help` and `import`.

inspecting current state:

* `bt` - Print the traceback of the current execution stack
* `up` - Move the scope up, to caller of current function
* `down` - Move scope down one level on function call

Resuming execution:

* `step` - Run the program till the next line stopping in next function called
* `next` - Run the next line, do not stop when the next function is called
* `return` - Run the program until the current function returns
* `continue` - continue running until the next breakpoint.

### Profile Before Optimising

Slowdowns can be obscure. The best thing to do is ignore intuition and directly measure the performance of a program before you try optimise it.

Python provides a built in _profiler_.

Lets try it on this insertion sort:

    from random import randint
    max_size = 10**4
    data = [randint(0, max_size) for _ in range(max_size)]
    test = lambda: insertion_sort(data)

    def insertion_sort(data):
        result = []
        for value in data:
            insert_value(result, value)
        return result


    def insert_value(array, value):
        for i, existing in enumerate(array):
            if existing > value:
                array.insert(i, value)
                return
        array.append(value)

Python provides `profile` in pure python and `cProfile` a C-extension with low overhead.

> Ensure to only test the portion of the code you have control over, not external systems.

    import cProfile
    from pstats import Stats

    profiler = cProfile.Profile()
    profiler.runcall(test)
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()

Also a nice visualizer is [snakeviz](https://jiffyclub.github.io/snakeviz/)

    python -m cProfile -o expiring_dict_test expiring_dict_test.py
    snakeviz expiring_dict_test

Results:

    $ python test.py
            20003 function calls in 2.167 seconds

    Ordered by: cumulative time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         1    0.000    0.000    2.167    2.167 test.py:198(<lambda>)
         1    0.004    0.004    2.167    2.167 test.py:181(insertion_sort)
     10000    2.142    0.000    2.163    0.000 test.py:188(insert_value)
      9988    0.020    0.000    0.020    0.000 {method 'insert' of 'list' objects}
        12    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

* `ncalls` - Number of calls to function during profiling period
* `tottime` - Number of seconds spent executing the function `9not other functions it calls)
* `percall` - Average time spent in seconds spent in function per call
* `cumtime` - Cumulative sends in call including other calls
* `cumtimepercall` - Average seconds spent including other calls

You can see the time spent in `insert_value` is the biggest time waster

    from bisect import bisect_left

    def insert_value(array, value):
        i = bisect_left(array, value)
        array.insert(i, value)

Now the results:

            30003 function calls in 0.067 seconds

    Ordered by: cumulative time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.067    0.067 test.py:196(<lambda>)
        1    0.007    0.007    0.067    0.067 test.py:182(insertion_sort)
    10000    0.008    0.000    0.060    0.000 test.py:189(insert_value)        10000    0.028    0.000    0.028    0.000 {method 'insert' of 'list' objects}
    10000    0.024    0.000    0.024    0.000 {built-in method _bisect.bisect_left}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Sometimes for more complex issues you can use `stats.print_callers()`

### Use tracemalloc to Understand Memory Usage and Leaks

More about this in the book...Item 59

Source: 

* “Effective Python: 59 Specific Ways to Write Better Python (Effective Software Development Series).” - Brett Slatkin