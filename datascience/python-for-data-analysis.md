# Python for Data Analysis Notes

## What Data?

* Tabular like a CSV or excel
* Multi-dimensional arrays (matrices)
* Related data tables
* Evenly spaced out time series

## Why Python?

**Not from the book**

Because it is the best.

Python can be used at any stage research to prototyping to production systems.

## Why not python?

It's maximum performance is not great due to it being interpreted and not compiled.
The GIL (Global Interpreter Lock) prevents the interpreter from running more than 1 instruction at a time.
Developer time is more important than CPU time in most cases so it is a good tradeoff.

## Essential Python Libraries

### Numpy

Numerical python provides data structures, algorithms and library glue for scientific applications using numerical data.

* A fast multi-dimensional arrray `ndarray`
* Functions for perofming element-wise and array-wise operations
* Tools for writing datasets to disk
* Linear algebra, fourier transform and random number generation
* A mature C Api to enable python extensions and native C and C++ code to access the numpy array.

It is a container for using and manipulating data, more efficient than built-in python data structures.
C can run operations on a numpy array without copying data into an in-memory representation

### Pandas

Provides high level data strcutures and functions that make working with tabular data fast, easy and expressive.
It's primary data structure is a `DataFrame` - a tabular column-oriented data structure with row and column labels.
It provides the tools for data manipulation, preparation and cleaning.

* Labeled axis with data alignments
* Integrated time series
* Same data structure for time series and non-time series data
* Arithmetic and reductions would pass on meta data
* Flexible handling of missing data
* Operations similar to those in db's

The name _pandas_ is derived from `panel data` an econometrics term and *P*ython *An*alysis *Da*ta

### Matplotlib

Most popular python library for creating plots and other 2d visualisations. It is well suited for creating publication ready charts.

### iPython and Jupyter

The interative python interpreter, it maximises developer productivity by allowing interactive exploration `execute-explore` as opposed to `edit-compile-run`. Data analysis involves a lot of trial and error, that is why it works well.

Jupyter is a language agnostic interactive computing tool. It provides an interactive code book called a notebook.

### SciPy

A collection of packages addressing a number of problem domains in scientific computing

* `scipy.integrate` - Numerical integrations routines and differential equation solvers
* `scipy.linalg` - Linear algebra routines
* `scipy.optimize` - Function optimizers and root finding algorithms
* `scipy.signal` - Signal processing tools
* `scipy.sparse` - Sparse matrices and sparse linear system solvers
* `scipy.special` - Wrapper around `SPECFUN` A fortran library.
* `scipy.stats` - Continuous and discrete probability distributions, density functions, samplers, statistical and descriptive tests.
* `scipy.weave` - ools for using C++ to accelerate array computations

### Scikit-learn

A general purpose machine learning toolkit for python programmers.

Submodules:

* `classification` - SVM, nearest neighbours, random forest
* `Regression` - Lasso, Ridge regression, Logistic
* `Clustering` - k-means, special clustering
* `Dimensionality reduction` - PCA, feature selection, matrix factorisation
* `Preprocessing` - Feature extraction, normalisation

### Statsmodels

A statistical analysis package for classical statistics and econometrics.

Submodules:

* Regression models: linear regression, generalised linear models, robust linear models, linear mixed effect models.
* ANOVA - Analysis of variance
* Time series analysis - AR, ARMA, ARIMA, VAR
* Nonparametric methods: kernel density estimation, kernel regressino
* Visualisation of statistical model results

## Tasks in this book

### Interacting with the Outside world

Reading and writing various file formats

### Preparation

Cleaning, munging, combining, normalising, reshaping, slicing, dicing and transforming data for analysis.

### Transformation

Applying mathematical and statistical operations to groups of data sets to derive new data sets

### Modeling and computation

Connecting your data to statistical models, machine learning algorithms.

### Presentation

Creating interactive or static graphical visualisations or textual summaries

## Import Conventions

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import sklearn as sk
    import statsmodels as sm

As it is bad practice to `from numpy import *`

## Jargon

Munge/Munging/Wrangling - Manipulating unstructured or messy data into a structured clean form

# Chapter 2: Python, iPython and Jupyter Notebooks

## Python Interpreter

Python is `interpreted`, that is it executes code line by line. 

Enter the interpreter with (provided python is installed)

    python

exit it with:

    >>> exit()

Running programs from the terminal

    $ python hello_world.py
    Hello world


Many data scientists make use of `ipython`, an interactive python shell that gives you tab completion features, lets you run files and pretty prints output

    ipython

You can use `%run` to execute scripts within a shell:

    In [1]: %run hello_world.py
    Hello world

## Ipython basics

Get a quick reference

    %quickref

Basic variable assignment

    In [5]: a = 5

    In [6]: a
    Out[6]: 5

Printing data is nicer eg:

    In [10]: data = {i : np.random.randn() for i in range(7)}

    In [11]: data
    Out[11]: 
    {0: 0.6470083582639674,
    1: -0.07424180544449763,
    2: 1.017173940313301,
    3: 0.5332176226383887,
    4: 0.4663520822888573,
    5: 0.9544131609184705,
    6: -1.2202876585351747}

## Jupyter Notebook

A notebook, an interactive document for code, text, markdown and visualisations

The jupyer notebook interacts with _kernels_, which are implementations of the interactive computing protocols of various programming languages.

Start a notebook:

    $ jupyter notebook

It will usually open the browser automatically at: http://localhost:8888/tree

> Jupyter can also be used on a remote computer

Create a new python 3 notebook:

    File -> New -> Python3

Execute code:

    Shift + Enter

The extensions is `.ipynb` for python notebooks

> You can use `Tab` to complete partially completed commands or paths

### Introspection

Use `?` before or after any command:

    In [6]: ?any
    Signature: any(iterable, /)
    Docstring:
    Return True if bool(x) is True for any x in the iterable.

    If the iterable is empty, return False.
    Type:      builtin_function_or_method

This is `object` introspection, it shows us the docstring.

Using `??` will show the source code if possible.

You can also use it to search for functions

    In [8]: import numpy as np

    In [9]: np.*load*?
    np.__loader__
    np.load
    np.loads
    np.loadtxt
    np.pkgload

### The %run Command

Any file can be run as a python program in your interactive shell.

    In [550]: %run ipython_script_test.py

The script is run in the _empty namespace_ same as running it from the shell. (No existing imports will be used)

To include in the current namespace:

    %run -i ipython_script_test.py

In `jupyter` you can also load the code in a file using:

    %load ipython_script_test.py

### Interrupting running code

You can use `Ctrl + C` which causes a `KeyBoardInterrupt` when code execution seems stuck.

> When a piece of Python code has called into some compiled extension modules, pressing <Ctrl-C> will not cause the program execution to stop immediately in all cases 

### Executing code from the clipboard

Copy the code and in a `jupyter notebook` use:

    %paste

Or to edit before pasting

    %cpaste

### Terminal Keyboard Shortcut

Has some `emacs` style shortcuts (boooh!)

* `ctrl-p` or `up-arrow`: previous command
* `ctrl-n` or `down-arrow`: next command
* `ctrl-r`: reverse history search
* `ctrl-shift-p`: paste from clipboard
* `ctrl-c`: cancel executing code
* `ctrl-a`: go to beginning of line
* `ctrl-e`: go to end of line
* `ctrl-k`: delete from cursor to end of line
* `ctrl-u`: discard all text from current line
* `ctrl-l`: clear screen

### Exceptions and Tracebacks

With `%run` you may get an exception. It has alot more context that standard python interpreter, set with `%xmode`.

You can use `%pdb` or `%debug` to step into things.

### Magic Commands

All commands that start with `%` (not available to standard python interpreter)

For example use `%timeit` to check execution time:

    In [13]: a = np.random.randn(100, 100)

    In [14]: %timeit np.dot(a, a)
    26.5 µs ± 805 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

You can use help `?` on magic methods:

    %debug?

You can use then without the `%` provided no variables with the same name with `%automagic`

* `%quickref` - quick reference card
* `%magic` - detailed docs for magic commands
* `%hist` - Print command input history
* `%pdb` - Automatically enter debugger on excpetion
* `%paste` - Execute code from clipboard
* `%cpaste` - Manually paste in code from clipboard
* `%reset` - Delete all variables and names defined in the interactive namespace.
* `%page obejct` - page through an object (like `less`)
* `%run script.py` - Execute a python script
* `%prun statement` - execute a command in the profiler
* `%time statement` - output length of time for statement
* `%timeit` - Run a statement multiple times and get execution time
* `%who`  - Show variables defined in namespace
* `%xdel variable` - delete variable from context

### Jupyter Magic Commands

Often loaded by third party extensions, use `%%`

Eg. Creating a cython extension in jupyter

    %%cython

    cimport numpy as cnp
    cnp.import_array()

    def sum_arr(cnp.ndarray[cnp.float64] arr):
        cdef int i
        cdef double total = 0
        for i in range(len(arr)):
            total += arr[i]

        return total

Can be run with:

    In [2]: arr = np.random.randn(1000000)

    In [3]: sum(arr)
    Out[3]: 340.78566319852672

I got the following error:

    UsageError: Cell magic `%%cython` not found.

The above did not work apparently you should use `%load_ext Cython` but that didn't work for me either.
Also there might be an error in the book `sum(arr)` should be `sum_arr(arr)`

### Matplotlib integration

Using `%matplotlib` or in Jupyter `%matplotlib inline`.

I didn't even do that though, ust executed:

    import numpy as np
    import matplotlib.pyplot as plt

    plt.plot(np.random.randn(50).cumsum())

## Python Language Basics

### Semantics

* use indentation, not braces (**white spaces** are very important)
* a colon denates the start of an (indented) block
* It makes thing cosmetically constant and easier to read through (a convention)
* Default to `4 spaces`
* Semicolon is still used rarely for statements on a single line: eg. x = 5; y = 6; z = 1;
* Everything is an object - every number, string, class, module or function is an obejct and has a `type()`
* Variables are passed by reference be default.
* The type of an object is stored in the object itself. Python is a `strongly-typed` language

    >>> 5 + '5'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

* In python, operations are carried out stricly or immediately (not lazily or when it is needed like Haskell). Python uses generators for more efficient evaluation.
* In python 3, Unicode has become a first class string type.
* In python a module is simply a `x.py` file

Eg.

    # some_module.py
    PI = 3.14159

    def f(x):
        return x + 2

Used in another file:

    import some_module
    result = some_module.f(5)
    pi = some_module.PI

the same as:

    from some_module import f, g, PI
    result = g(5, PI)

#### Binary Operators

    a + b	Add a and b
    a - b	Subtract b from a
    a * b	Multiply a by b
    a / b	Divide a by b
    a // b	Floor-divide a by b, dropping any fractional remainder
    a ** b	Raise a to the b power
    a & b	True if both a and b are True. For integers, take the bitwise AND.
    a | b	True if either a or b is True. For integers, take the bitwise OR.
    a ^ b	For booleans, True if a or b is True, but not both. For integers, take the bitwise EXCLUSIVE-OR.
    a == b	True if a equals b
    a != b	True if a is not equal to b
    a <= b, a < b	True if a is less than (less than or equal) to b
    a > b, a >= b	True if a is greater than (greater than or equal) to b
    a is b	True if a and b reference same Python object
    a is not b	True if a and b reference different Python objects

#### Mutable and immutable

Most python objects are mutable: lists, dicts and numpy arrays. This means their contents can be changed. 

Some objects are immutable, once they are treated their contents cannot be changed. Like a `tuple`.

>>> a = (10, 15, 20)
>>> a[1] = 40
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a
(10, 15, 20)

#### Scalar Types

    None	The Python “null” value (only one instance of the None object exists)
    str	String type. Holds Unicode (UTF-8 encoded) strings.
    bytes	Raw ASCII bytes (or Unicode encoded as bytes)
    float	Double-precision (64-bit) floating point number. Note there is no separate double type.
    bool	A True or False value
    int	Arbitrary precision signed integer.

#### Dates and Time

    Type	Description
    %Y	4-digit year
    %y	2-digit year
    %m	2-digit month [01, 12]
    %d	2-digit day [01, 31]
    %H	Hour (24-hour clock) [00, 23]
    %I	Hour (12-hour clock) [01, 12]
    %M	2-digit minute [00, 59]
    %S	Second [00, 61] (seconds 60, 61 account for leap seconds)
    %w	Weekday as integer [0 (Sunday), 6]
    %U	Week number of the year [00, 53]. Sunday is considered the first day of the week, and days before the first Sunday of the year are “week 0”.
    %W	Week number of the year [00, 53]. Monday is considered the first day of the week, and days before the first Monday of the year are “week 0”.
    %z	UTC time zone offset as +HHMM or -HHMM, empty if time zone naive
    %F	Shortcut for %Y-%m-%d, for example 2012-4-18
    %D	Shortcut for %m/%d/%y, for example 04/18/12

Convert a string time to a datetime object: (String - Parse - Time )

    In [108]: datetime.strptime('20091031', '%Y%m%d')
    Out[108]: datetime.datetime(2009, 10, 31, 0, 0)

Format a datetime as a string: (String - format - time)

    In [107]: dt.strftime('%m/%d/%Y %H:%M')
    Out[107]: '10/29/2011 20:30

Rounding time down to minute:

    In [109]: dt.replace(minute=0, second=0)
    Out[109]: datetime.datetime(2011, 10, 29, 20, 0)

> A lot more stuff in the book, I recommend reading it

# Chapter 3: Built In Data Structures, Functions and Files

## Tuple

One dimensinal, fixed length, immutable sequence of python objects.

    >>> tup = 4, 5, 6
    >>> tup
    (4, 5, 6)

or 

    >>> tup = (4, 5, 6)

A nested tuple:

    >>> nested_tup = (3, 5, 6), (7, 8)
    >>> nested_tup
    ((3, 5, 6), (7, 8))

Convert a list to a tuple:

    >>> a = [1, 2, 3]
    >>> tuple(a)
    (1, 2, 3)

Elements can be accessed with square brackets and an index:

    >>> nested_tup[1]
    (7, 8)

> tuples can be concatenated with `+` and multiplied with `*`

You can unpack tuples by assigning a tuple like-object:

    >>> a, b = nested_tup
    >>> a
    (3, 5, 6)
    >>> b
    (7, 8)

or

    >>> a, (b, c,) = nested_tup
    >>> a
    (3, 5, 6)
    >>> b
    7
    >>> c
    8

Too many values raises a `ValueError` but you can catch the rest with `*the_rest`:

    >>> values = 1, 2, 3, 4, 5, 6
    >>> first, second, rest = values
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: too many values to unpack (expected 3)

    >>> first, second, *the_rest = values
    >>> first
    1
    >>> second
    2
    >>> the_rest
    [3, 4, 5, 6]

Count occurances of an element:

    >>> the_rest.count(3)
    1

## List

Variable length, one-dimensional and are mutable (can be modified in place)

    >>> list_ = [1, 2, 3, None]
    >>> list_
    [1, 2, 3, None]

or

    >>> list(nested_tup)
    [(3, 5, 6), (7, 8)]

Add elements:

    In [39]: b_list.append('dwarf')

Insert elements at specified location:

    In [41]: b_list.insert(1, 'red')

Take an element out by index:

    In [43]: b_list.pop(2)

Take an element out by value, ie. remove all occurances of:

    In [46]: b_list.remove('foo')

Check if a list contains element:

    >>> None in list_
    True

Concatenating lists:

    >>> x = [1, 2, 3]
    >>> y = [1, 2, 3, 4]
    >>> z = x + y
    >>> z
    [1, 2, 3, 1, 2, 3, 4]

or `extend`:

    >>> x.extend([5, 6, 7])
    >>> x
    [1, 2, 3, 5, 6, 7]

`extend` is less expensive that `+` and assignment.

### Sorting

Can be sorted in place with `sort()`:

    >>> x = [5, 7, 3, 9, 99]
    >>> x.sort()
    >>> x
    [3, 5, 7, 9, 99]

You can also supply a function to sort using the `key` kwarg:

    >>> x = ['hello', 'world', 'lets', 'be', 'friends']
    >>> x.sort(key=len)
    >>> x
    ['be', 'lets', 'hello', 'world', 'friends']

### Binary search and maintaining sorted list

    import bisect
    >>> x
    [3, 5, 7, 9, 99]

`bisect.bisect` calculates where it should be inserted

    >>> bisect.bisect(x, 2)
    0

`bisect.insort` actually does the inserting

    >>> bisect.insort(x, 2)
    >>> x
    [2, 3, 5, 7, 9, 99]

> The honus is on you to ensure the list is sorted already. It is too expensive for bisect to do it.

### Slicing

You can select portions of the list or any list-like types (tuples, numpy arrays, pandas series)

    >>> x
    [2, 3, 5, 7, 9, 99]
    >>> x[2:4]
    [5, 7]

### Enumerate

Looping over a list and keeping the index

    >>> for index, value in enumerate(x):
    ...     print(index, value)
    ...
    0 2
    1 3
    2 5
    3 7
    4 9
    5 99

### Sorted

Returns a new sorted list

    >>> sorted([7, 1, 2, 6, 0, 3, 2])
    [0, 1, 2, 2, 3, 6, 7]

### Zip

Zip pairs up 2 lists with each other creating a `zip` object that when cast to a list becomes a list of tuples:

    >>> numbers = [1, 2, 3]
    >>> words = ['one', 'two', 'three']
    >>> combined = zip(numbers, words)
    >>> combined
    <zip object at 0x10f850148>
    >>> list(combined)
    [(1, 'one'), (2, 'two'), (3, 'three')]

The most common use of it is iterating over both lists together which you can do with:

    >>> for i, (a, b) in enumerate(zip(numbers, words)):
    ...     print(i, a, b)
    ...
    0 1 one
    1 2 two
    2 3 three

### Reversed

Creates an iterator of the reverse of the list:

    >>> list(reversed([7, 1, 2, 6, 0, 3, 2]))
    [2, 3, 0, 6, 2, 1, 7]

## Dict

A flexibly sized collection key-value pairs, where keys and values are python objets.
Also known as a `hash map` or `associative array`

    empty_dict = {}

Create with elements:

    my_dict = {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}

Access an element with `[]`:

    >>> my_dict['a']
    'some value'

Check if a dict contains a key:

    >>> 'c' in my_dict
    False
    >>> 'a' in my_dict
    True

Keys can be deleted with `del` or `pop`:

    >>> del my_dict['a']
    >>> my_dict
    {'b': [1, 2, 3, 4], 7: 'an integer'}

    >>> b = my_dict.pop('b')
    >>> b
    [1, 2, 3, 4]

Get all keys or all values:

    >>> list(my_dict.keys())
    ['a', 'b', 7]
    >>> list(my_dict.values())
    ['some value', [1, 2, 3, 4], 'an integer']

Concatenating with `+` does not work:

    >>> my_a = {'a': 1, 'b':2}
    >>> my_b = {'c': 3, 'd': 4}
    >>> my_c = my_a + my_b
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

You can merge 2 dicts together with `update()`:

    >>> my_a
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}

There is another way to create a new list:

    >>> my_c = dict(my_a.items() | my_b.items())
    >>> my_c
    {'c': 3, 'a': 1, 'b': 2, 'd': 4}

Creating dicts from sequences:

    mapping = {}
    for key, value in zip(key_list, value_list):
        mapping[key] = value

### Default Values

`get()` and `pop()` can return default values. 

    value = some_dict.get(key, default_value)
    >>> my_c.get('e', 5)
    5

Even better might be to use `defaultdict`

### Valid dict keys

A key is only valid if it can be _hashable_, you can check if an object is hashable with `hash()`

    >>> datetime.date(2018,10,11)
    datetime.date(2018, 10, 11)
    >>> my_dict
    {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}
    >>> my_dict[datetime.date(2018,10,11)] = 3
    >>> my_dict[[3, 4, 5]] = 3
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

## Set

A set is an unordered collection of unique elements

    >>> {2, 2, 3, 4, 1, 1}
    {1, 2, 3, 4}

or

    >>> set([2, 2, 3, 4, 1, 1])
    {1, 2, 3, 4}

It supports mathemtical operations like `union` (or):

    >>> a = {1, 2, 3, 4, 5}
    >>> b = {3, 4, 5, 6, 7, 8}
    >>> a | b
    {1, 2, 3, 4, 5, 6, 7, 8}

Intersection (`and`):

    >>> a & b
    {3, 4, 5}

Difference:

    >>> a - b
    {1, 2}

Exclusive or:

    >>> a ^ b
    {1, 2, 6, 7, 8}

There are inplace counterparts to keep the returned set that are more efficient:

    c = a.copy()
    c |= b

or

    c &= b

Check if is a subset:

    In [24]: a.issubset(b)
    Out[24]: False

    In [25]: a.issubset(c)
    Out[25]: True

Sets are equal if there contents are equal:

    In [26]: {1, 2, 3} == {3, 2, 1}
    Out[26]: True

### Set Operations

    Function	Alternate Syntax	Description
    a.add(x)	N/A	Add element x to the set a
    a.clear()	N/A	Reset the set a to an empty state, discarding all of its elements.
    a.remove(x)	N/A	Remove element x from the set a
    a.pop()	N/A	Remove an arbitrary element from the set a, raising KeyError if the set is empty.
    a.union(b)	a | b	All of the unique elements in a and b.
    a.update(b)	a |= b	Set the contents of a to be the union of the elements in a and b.
    a.intersection(b)	a & b	All of the elements in both a and b.
    a.intersection_update(b)	a &= b	Set the contents of a to be the intersection of the elements in a and b.
    a.difference(b)	a - b	The elements in a that are not in b.
    a.difference_update(b)	a -= b	Set a to the elements in a that are not in b.
    a.symmetric_difference(b)	a ^ b	All of the elements in either a or b but not both.
    a.symmetric_difference_update(b)	a ^= b	Set a to contain the elements in either a or b but not both.
    a.issubset(b)	N/A	True if the elements of a are all contained in b.
    a.issuperset(b)	N/A	True if the elements of b[…]

## List, Set and Dict Comprehensions

List comprehensions allow us to concisely form a new list by filtering an existing list

The basic form:

    [expr for val in collection if condition]

Equavalent to:

    result = []
    for val in collection:
        if condition:
            result.append(expr)

Example:

    In [30]: strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

    In [31]: [x.upper() for x in strings if len(x) > 2]
    Out[31]: ['BAT', 'CAR', 'DOVE', 'PYTHON']

Dict comp:

    dict_comp = {key-expr : value-expr for value in collection if condition}

Set comp:

    set_comp = {expr for value in collection if condition}

## Functions, Namespace and Scope

Functions can access variables from `local` and `global` scope. In python this is called a `namespace`.

Variables by default are assigned to the `local` namespace

Local variables are declared within a function.
You can declare global variables within a function, but you need to use the `global` keyword.

    def global_array():
        global a
        a = []

## Returning Multiple Values

    def f():
        a = 5
        b = 6
        c = 7
        return a, b, c

    a, b, c = f()

Pretty much the same as tuple unpacking discussed earlier

## Functions are objects

You can use functions as arguments to other functions

    def remove_punctuation(value):
        return re.sub('[!#?]', '', value)

You can use `map`, that applies a function to a collection.

    In [23]: map(remove_punctuation, states)

## Anonymous Lambda functions

> Don't use these

Example:

    def short_function(x):
        return x * 2

if equivalent to

    equiv_anon = lambda x: x * 2

## Closures: Functions that return Functions

A dynamically generated function returned by another function

> A key property is that the returned function has access to the variables in the local namespace it was created

Example:

    In [32]: def make_closure(a):
        ...:     def closure():
        ...:         print('I know the secret: {}'.format(a))
        ...:     return closure
        ...: 
        ...: 

    In [33]: closure = make_closure(5)

    In [34]: closure()
    I know the secret: 5

You can even mutate values in that local scope, one limitation is that you cannot create new variables. So best to modify an existing list or dict. Or you can make use of the `nonlocal` keyword.

## Args and Kwargs

A functions `func(a, b, c, d=some, e=value)` are packed up into a tuple and a dict.

    a, b, c = args
    d = kwargs.get('d', d_default_value)
    e = kwargs.get('e', e_default_value)

which is done behind the scenes. You can therefore send variables into a function that aren't in the signature.

Alot more hectic stuff in the book...generators etc.

## Files and Operating Systems

Most examples in this book will use `pandas.read_csv` to import data files. However it is good to know how it is done:

Open a file for reading or writing:

    In [1]: path = './hello_world.txt'

    In [2]: f = open(path)

By default the file is opening in `r` mode (read only).

You can iterate over it:

    In [4]: for line in f:
   ...:     print(line)

If we had done `f = open(path, 'w')` a new empty file would have overwritten that file.

Using `x` would work to create a file and skip if it already existed.

You can read a certain number of characters or the whole thing:

    In [3]: f.read()
    Out[3]: 'Hello\nWorld\n\nWhoopee!!\n'

Or reset it, once it is read no more characters are read:

    In [8]: f.read(2)
    Out[8]: 'He'

You can read it in `binary` mode;

    In [9]: f = open(path, 'rb')

    In [10]: f.read()
    Out[10]: b'Hello\nWorld\n\nWhoopee!!\n'

You can check where read is with:

    In [11]: f.tell()
    Out[11]: 23

Go to another location with `seek`:

    In [12]: f.seek(2)
    Out[12]: 2

    In [13]: f.read()
    Out[13]: b'llo\nWorld\n\nWhoopee!!\n'

### File Modes

    Mode	Description
    r	Read-only mode
    w	Write-only mode. Creates a new file (erasing the data for any file with the same name)
    x	Write-only mode. Creates a new file, but fails if the file path already exists.
    a	Append to existing file (create it if it does not exist)
    r+	Read and write
    b	Add to mode for binary files, that is 'rb' or 'wb'
    t	Text mode for files (automatically decoding bytes to unicode). This is the default if not specified. Add t to other modes to use this, that is 'rt' or 'xt

### File Methods

    read([size])	Return data from file as a string, with optional size argument indicating the number of bytes to read
    readlines([size])	Return list of lines in the file, with optional
    lines([size])	Return list of lines in the file, with optional size argument
    readlines([size])	Return list of lines (as strings) in the file
    write(str)	Write passed string to file.
    writelines(strings)	Write passed sequence of strings to the file.
    close()	Close the handle
    flush()	Flush the internal I/O buffer to disk
    seek(pos)	Move to indicated file position (integer).
    tell()	Return current file position as integer.
    closed	True if the file is closed.

# Chapter 4: Numpy Basics

Numerical Python. Most important foundational packages for numerical computing.

Features:
* `ndarray` - An efficient multi-dimensional array providing fast array-oriented and flexible broadcasting
* Mathemtical functions on all elements, no loops
* Tools for reading and writing to disc and working with memory mapped files
* Linear algebra, random number generation
* A C Api for connecting with C, C++ and FORTRAN

Knowing `numpy` will help you use `pandas` more effectiely.

For datascience:
* Fast vectorised array operations
* Effecient descriptive statistics (aggregate and summary)
* Data alignment and relational DB manipulation

`pandas` provides time series manipulation not found in `numpy`

> Designed for efficiency on large arrays of data

    my_arr = np.arange(1000000)
    my_list = list(range(1000000))

    In [20]: %timeit for _ in range(10): my_arr2 = my_arr * 2
    20.1 ms ± 949 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    In [21]: %timeit for _ in range(10): my_list2 = [x * 2 for x in my_list]
    769 ms ± 14.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

## Ndarray

An N-dimensinal array object for homogenous (the sametype) data, that lets you perform scalar operations on it (which really applies these operations to each element)

    In [1]: import  numpy as np

    In [2]: data = np.random.randn(2, 3)

    In [3]: data
    Out[3]:
    array([[-0.33620461,  1.62919406, -0.75813031],
        [ 0.47703292,  0.67547306, -0.03832895]])

    In [4]: data * 10
    Out[4]:
    array([[-3.36204611, 16.29194062, -7.5813031 ],
        [ 4.77032922,  6.75473056, -0.38328952]])

    In [5]: data + 10
    Out[5]:
    array([[ 9.66379539, 11.62919406,  9.24186969],
        [10.47703292, 10.67547306,  9.96167105]])

### Shape

A tuple indicating the `size of each dimension`

    In [7]: data.shape
    Out[7]: (2, 3)

### Datatype

    In [9]: data.dtype
    Out[9]: dtype('float64')

> An array, numpy array and ndarray are the same thing in this book

### Dimensions

Number of array dimensions

    In [28]: data.ndim
    Out[28]: 2

## Creatng NdArrays

Use the `array` function. 

    In [11]: numbers = [0.1, 0.2, 0.3, 0.5678]

    In [13]: number_array = np.array(numbers)

    In [14]: number_array
    Out[14]: array([0.1   , 0.2   , 0.3   , 0.5678])

Nested sequences will be converted into a multi-dimensional array

    In [15]: numbers = [[1, 2, 3], [4, 5, 6]]

    In [16]: multi_arr = np.array(numbers)

    In [17]: multi_arr
    Out[17]:
    array([[1, 2, 3],
        [4, 5, 6]])

You can create array's of zeroes and ones with, `zeros` and `ones`

    In [29]: np.zeros(10)
    Out[29]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

    In [33]: np.ones((10, 10))
    Out[33]:
    array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])

> It is not safe to assume `np.empty` will return zeroes. It will return unintialised garbage values.

    In [34]: np.empty((2, 3, 2))
    Out[34]:
    array([[[ 1.72723371e-077, -4.34288275e-311],
            [ 2.96439388e-323,  2.22028315e-314],
            [ 2.20432227e-314,  2.26173552e-314]],

        [[ 2.20290004e-314,  2.20304074e-314],
            [ 2.26375497e-314,  2.20285084e-314],
            [ 2.20285084e-314,  8.34402697e-309]]])

`arange`, is the numpy array equivalent of python's `range`:

    In [35]: np.arange(10)
    Out[35]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

### Datatypes

The source of numpys flexibility in working with other systems and programming languages.

    In [36]: arr1 = np.array([1, 2, 3], dtype=np.float32)

    In [37]: arr2 = np.array([1, 2, 3], dtype=np.int32)

    In [38]: arr1.dtype
    Out[38]: dtype('float32')

    In [40]: arr2.dtype
    Out[40]: dtype('int32')

Knowing exact number of bits is not required, jsut a general idea of the type: int, float, decimal, str is ok.

You can cast to another datatype with `astype`:

    In [42]: arr1.dtype
    Out[42]: dtype('float32')

    In [43]: int_arr = arr1.astype(np.int32)

    In [44]: int_arr.dtype
    Out[44]: dtype('int32')

> Decimal part will be truncated

A `ValueError` is raised if casting fails.

Calling `astype` **always** creates a new array

## Operations between Arrays and Scalars

You can do operations on an `ndarray` without loops, called _vectorization_.

    In [45]: arr = np.array([[1, 2, 3,], [4, 5, 6]])

    In [46]: arr
    Out[46]:
    array([[1, 2, 3],
        [4, 5, 6]])

    In [47]: arr * arr
    Out[47]:
    array([[ 1,  4,  9],
        [16, 25, 36]])

    In [48]: arr - arr
    Out[48]:
    array([[0, 0, 0],
        [0, 0, 0]])

    In [49]: 1/ arr
    Out[49]:
    array([[1.        , 0.5       , 0.33333333],
        [0.25      , 0.2       , 0.16666667]])

    In [50]: arr ** 0.5
    Out[50]:
    array([[1.        , 1.41421356, 1.73205081],
        [2.        , 2.23606798, 2.44948974]])

Operations between different sized arrays is called **broadcasting**.

## Basic INnexing and Slicing

They work the same as python lists.

    In [51]: arr = np.arange(10)

    In [52]: arr[5]
    Out[52]: 5

    In [53]: arr[2:3]
    Out[53]: array([2])

    In [54]: arr
    Out[54]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    In [55]: arr[2:3] = 33

    In [56]: arr
    Out[56]: array([ 0,  1, 33,  3,  4,  5,  6,  7,  8,  9])

Importantly, the slices on `nparray` are not copies of the data, merely views. Therefore modiifation on a copied slive **will** modify the original `ndarray`.

> Numpy is performance oriented and not so eager to make frivolous copies

To copy a slice you must explicity use `copy()`:

    arr_slice = arr[2:3].copy()

Multi dimensional arrays can be accessed recursively or via comma seperated numbers:

    In [74]: arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    In [76]: arr2d[2]
    Out[76]: array([7, 8, 9])

    In [77]: arr2d[2][0]
    Out[77]: 7

    In [78]: arr2d[2, 0]
    Out[78]: 7

Multi-dimensional sliving is hectic...read the book for more info

## Boolean Indexing

Say we have names and data:

    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    data = np.random.randn(7, 4)

We can run boolean expressions against the ndarray and it will be applied element-wise

    In [82]: names == 'Joe'
    Out[82]: array([False,  True, False, False, False,  True,  True])

The boolean array can be used to index another array axis (provided the axis it is slicing is the same size)

    In [83]: data[names == 'Joe']
    Out[83]:
    array([[-1.61727753e-03,  1.11134244e+00,  3.17965850e-01,
            1.66651524e-01],
        [ 1.71907497e+00,  5.76550942e-01, -1.09187824e+00,
            -8.16713776e-01],
        [ 4.16526723e-01,  2.90342599e-02, -1.77285758e+00,
            4.69447898e-01]])

If you wanted to use multiple boolean conditions with `AND` and `OR`, remember to sue brackets around each condition:

        In [85]: (names == 'Joe') | (names == 'Will')
        Out[85]: array([False,  True,  True, False,  True,  True,  True])

> Selecting data from an array with boolean indexing _always_ creates a copy of the data

Only `|` and `&` work not their reserved keyword equivalents

You can then set data of the returned arrray

    In [93]: data[names == 'Joe'] = 4

    In [94]: data
    Out[94]:
    array([[-0.80941878, -0.9509764 , -0.27128519,  1.30517233],
        [ 4.        ,  4.        ,  4.        ,  4.        ],
        [ 2.35196404, -0.60165119, -1.00170882, -1.25451698],
        [-1.2806518 ,  0.42240918, -0.57464507, -1.22217808],
        [-0.26818876, -0.32669154,  2.20744615, -0.95180174],
        [ 4.        ,  4.        ,  4.        ,  4.        ],
        [ 4.        ,  4.        ,  4.        ,  4.        ]])

## Fancy Indexing

Fancy Indexing is indexing using integer arrays

    arr = np.empty((8, 4))

    for i in range(8):
        arr[i] = i

    In [100]: arr
    Out[100]:
    array([[0., 0., 0., 0.],
        [1., 1., 1., 1.],
        [2., 2., 2., 2.],
        [3., 3., 3., 3.],
        [4., 4., 4., 4.],
        [5., 5., 5., 5.],
        [6., 6., 6., 6.],
        [7., 7., 7., 7.]])
    
To select a subset of rows in a particular order:

    In [104]: arr[[2, 4, 5, 6]]
    Out[104]:
    array([[2., 2., 2., 2.],
        [4., 4., 4., 4.],
        [5., 5., 5., 5.],
        [6., 6., 6., 6.]])

Using multiple indices:

    In [105]: arr = np.arange(32).reshape((8, 4))

    In [106]: arr
    Out[106]:
    array([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23],
        [24, 25, 26, 27],
        [28, 29, 30, 31]])

    In [107]: arr[[1, 2, 3], [0, 3, 1]]
    Out[107]: array([ 4, 11, 13])

The resulting **copy** returned elements `(1, 0)`, `(2, 3)` and `(3, 1)`

> Fancy indexing always _copies_ the data

## Transposing arrays nd swapping indices

Transposing returns a view, not a copy.

Arrays have the `transpose` method and the special `T` attribute.

    In [109]: arr = np.arange(15).reshape((5, 3))

    In [110]: arr
    Out[110]:
    array([[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14]])

    In [111]: arr.T
    Out[111]:
    array([[ 0,  3,  6,  9, 12],
        [ 1,  4,  7, 10, 13],
        [ 2,  5,  8, 11, 14]])

Calculating the inner matrix product( whatever that means):

    In [114]: np.dot(arr.T, arr)
    Out[114]:
    array([[270, 300, 330],
        [300, 335, 370],
        [330, 370, 410]])

Higher dimensional arrays can be given an array of axis numbers to transpose around:

    In [115]: arr = np.arange(16).reshape((2, 2, 4))

    In [116]: arr
    Out[116]:
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7]],

        [[ 8,  9, 10, 11],
            [12, 13, 14, 15]]])

    In [117]: arr.transpose((1, 0, 2))
    Out[117]:
    array([[[ 0,  1,  2,  3],
            [ 8,  9, 10, 11]],

        [[ 4,  5,  6,  7],
            [12, 13, 14, 15]]])

`swapaxes` takes a pair of axis to swap:

    In [118]: arr
    Out[118]:
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7]],

        [[ 8,  9, 10, 11],
            [12, 13, 14, 15]]])

    In [119]: arr.swapaxes(1, 2)
    Out[119]:
    array([[[ 0,  4],
            [ 1,  5],
            [ 2,  6],
            [ 3,  7]],

        [[ 8, 12],
            [ 9, 13],
            [10, 14],
            [11, 15]]])

## Universal Functions

A `ufunc` universal function performs elementwise operations on data in ndarrays. 

### unaray ufuncs

`np.sqrt()`

    In [120]: arr = np.arange(10)

    In [121]: np.sqrt(arr)
    Out[121]:
    array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,
        2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ])

`np.exp()` - Calculate exponential

    In [124]: np.exp(arr)
    Out[124]:
    array([1.00000000e+00, 2.71828183e+00, 7.38905610e+00, 2.00855369e+01,
        5.45981500e+01, 1.48413159e+02, 4.03428793e+02, 1.09663316e+03,
        2.98095799e+03, 8.10308393e+03])

**Others**

    abs, fabs, sqrt, square, exp, log, log10, sign, ceil, floor, rint, modf, isnan, isfinite, isinf, cos, cosh, sin, sinh, tan, tanh, logical_not

### Binary Functions

`np.maximum(arr)` - Gives the element-wise maximum

    In [126]: x = np.random.randn(8)

    In [127]: y = np.random.randn(8)

    In [128]: x
    Out[128]:
    array([ 1.0055233 , -0.15194186,  0.89593432,  0.40450036, -0.21771624,
            0.61883328, -1.18958781, -1.13737865])

    In [129]: y
    Out[129]:
    array([-0.84924147, -0.79931119,  1.11336264, -0.19901553, -0.33127759,
        -0.48134005,  0.17885233,  1.33822367])

    In [130]: np.maximum(x, y)
    Out[130]:
    array([ 1.0055233 , -0.15194186,  1.11336264,  0.40450036, -0.21771624,
            0.61883328,  0.17885233,  1.33822367])

**Others**:

    add, subtract, multiple, divide, power, maximum, minimum, mod, copysign, greater, greater_equal, less, not_equal, logical_and, logical_or, logical_xor

## Loop Free Programming

`np.meshgrid` takes two 1D arrays and produces two 2D matrices corresponding to all pairs of (x, y) in the two arrays.

    In [131]: arr = np.arange(-5, 5, 0.01) # 1000 equally spaced

    In [135]: xs, ys = np.meshgrid(arr, arr)

    z = np.sqrt(xs ** 2 + ys ** 2)

    plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

## Expressing Conditional Logic as Array Operations

Getting the value from different arrays depending on a boolean array

    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]

    In [7]: result
    Out[7]: [1.1, 2.2, 1.3, 1.4, 2.5]

The problem with the above is it will be slow as it is being done by python, it also won't work with multidimensional arrays. Better to make use of `where`:

    In [8]: result = np.where(cond, xarr, yarr)

    In [9]: result
    Out[9]: array([1.1, 2.2, 1.3, 1.4, 2.5])

## Mathematical and Statistical Methods

Get normally distributed random data:

    In [10]: arr = np.random.randn(400)

### Mean

    In [12]: arr.mean()
    Out[12]: 0.02312549029816819

or:

    In [13]: np.mean(arr)
    Out[13]: 0.02312549029816819

### Sum

    In [14]: arr.sum()
    Out[14]: 9.250196119267276

The above functions take an options axis argument

Eg.

    arr.mean(1)
    arr.mean(axis=1)

# Cumsum and Cumprod

Cumulative sum and cumulative product produce an array of intermediate results

    arr.cumprod()
    arr.cumsum()

In a multidimensional array, accumulation returns an array of the same size it is calculated along the specified axis:

    In [20]: arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    In [21]: arr
    Out[21]:
    array([[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]])

    In [22]: arr.cumsum(0)
    Out[22]:
    array([[ 0,  1,  2],
        [ 3,  5,  7],
        [ 9, 12, 15]])

as opposed to:

    In [23]: arr.cumsum()
    Out[23]: array([ 0,  1,  3,  6, 10, 15, 21, 28, 36])

### Available methods

    sum, mean, std, var, min, max, argmin, argmax, cumsum, cumprod

## Methods of Boolean Arrays

Sum is often used to count `True` values

    In [24]: arr = np.random.randn(100)
    In [28]: (arr > 0).sum()
    Out[28]: 48

Other methods:
* `any()` checks if any are True
* `all()` checks if all are true

    In [29]: (arr > 0).any()
    Out[29]: True

    In [30]: (arr > 0).all()
    Out[30]: False

## Sorting

Can be sorted in place with `arr.sort()`:

    In [31]: arr = np.random.randn(10)
    In [32]: arr
    Out[32]:
    array([ 0.71608056,  1.34479278,  1.41800966, -0.48860031, -0.56617617,
        -1.42766719, -0.30723866, -0.91101707,  1.70796963, -0.09524445])

    In [33]: arr.sort()

    In [34]: arr
    Out[34]:
    array([-1.42766719, -0.91101707, -0.56617617, -0.48860031, -0.30723866,
        -0.09524445,  0.71608056,  1.34479278,  1.41800966,  1.70796963])

A multidimensional array can sorted along the axis:

0 would be column-wise and 1 would be row wise...eg:

    In [45]: arr = np.random.randn(2, 3)

    In [46]: arr
    Out[46]:
    array([[ 0.28019483, -0.05325257, -2.63604385],
           [-0.24228228, -0.63299377, -1.84148469]])

    In [47]: arr.sort(0)

    In [48]: arr
    Out[48]:
    array([[-0.24228228, -0.63299377, -2.63604385],
           [ 0.28019483, -0.05325257, -1.84148469]])

Finding a quantile:

    In [49]: large_arr = np.random.randn(1000)

    In [50]: large_arr.sort()

    In [51]: large_arr[int(0.05 * len(large_arr))]
    Out[51]: -1.6273103628065735

This gives the 5% quantile

## Unique and Other set logic

`np.unique` returns sorted unique values in an array

    In [52]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

    In [55]: np.unique(names)
    Out[55]: array(['Bob', 'Joe', 'Will'], dtype='<U4')

Testing membership of one array in another:

    In [56]: values = np.array([6, 0, 0, 3, 2, 5, 6, 9, 7, 9, 7, 9])

    In [57]: np.in1d(values, [6, 7, 9])
    Out[57]:
    array([ True, False, False, False, False, False,  True,  True,  True,
            True,  True,  True])

Other methods:

    unique(x), itersect1d(x, y), union1d(x, y), in1d(x, y), setdiff1d(x, y), setxor1d(x, y)

## File Input and Output

`np.load` and `np.save` are the workhorses of saving and loading from disk.
Files are saved uncompressed with extension `.npy`

    In [58]: arr = np.arange(10)

    In [59]: arr
    Out[59]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    In [60]: np.save('some_array', arr)

    In [61]: %pwd
    Out[61]: '/Users/stephen/projects/fixes'

    In [62]: np.load('some_array.npy')
    Out[62]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

You can save multiple arrays in a zip with `savez()`

    np.savez('array_archive.npz', a=arr, b=arr)

## Linear Algebra

Matrix multiplication, decompositions, determinants and other square matrix math.

Multiplying 2, 2-dimensional arrays with `*` is an element-wise product instead of a matrix dot product.
That is the reason there is a function `dot`, an array method and a function in the `numpy` namespace for matrix multiplication.

    In [197]: x = np.array([[1., 2., 3.], [4., 5., 6.]])

    In [198]: y = np.array([[6., 23.], [-1, 7], [8, 9]])

    In [199]: x
    Out[199]: 
    array([[ 1.,  2.,  3.],
        [ 4.,  5.,  6.]])

    In [200]: y
    Out[200]: 
    array([[  6.,  23.],
        [ -1.,   7.],
        [  8.,   9.]])

    In [68]: x.dot(y)
    Out[68]:
    array([[ 28.,  64.],
        [ 67., 181.]])

You can use `@` as an infix operator that performs matrix multiplication

    In [69]: x @ np.ones(3)
    Out[69]: array([ 6., 15.])

`numpy.linalg` has a standard set of matrix decompositions and things like determinant and inverse.

It is a bit over scope at this stage...read the book

## Pseudorandom Number Generation

`numpy.random` supplements the standard python `random` library. 

You can get a random array 4 x 4 with a normal distribution using `normal`:

    In [71]: samples
    Out[71]:
    array([[-0.5007292 , -0.34324411, -0.22568356,  0.6718186 ],
        [-1.10226626,  1.36328937,  0.87324304,  0.62881017],
        [ 0.12820656,  0.7683322 ,  1.45949403,  1.93611694],
        [ 0.63583831, -2.30817119, -1.42783868, -0.79192873]])

### Random Functions

    Function	Description
    seed	Seed the random number generator
    permutation	Return a random permutation of a sequence, or return a permuted range
    shuffle	Randomly permute a sequence in place
    rand	Draw samples from a uniform distribution
    randint	Draw random integers from a given low-to-high range
    randn	Draw samples from a normal distribution with mean 0 and standard deviation 1 (MATLAB-like interface)
    binomial	Draw samples from a binomial distribution
    normal	Draw samples from a normal (Gaussian) distribution
    beta	Draw samples from a beta distribution
    chisquare	Draw samples from a chi-square distribution
    gamma	Draw samples from a gamma distribution
    uniform	Draw samples from a uniform [0, 1) distribution

## Random Walks

More on Random Walks in the book

# Chapter 5: Getting Started with Pandas

Pandas contains data structures and data manipulation tools designed to make data cleaning and analysis fast and easy.

Import convention:

    import pandas as pd

## Data Structures

Pandas two workhorse data structures are: `DataFrame` and `Series`

### Series

A one-dimensional array-like object containing a sequence of values of a single type and associated labels, called an `index`.

    In [2]: series = pd.Series([1, 4, 6, 7, 8])

    In [3]: series
    Out[3]:
    0    1
    1    4
    2    6
    3    7
    4    8
    dtype: int64

Labels on the left, values on the right

Get the values of a series as an array:

    In [5]: series.values
    Out[5]: array([1, 4, 6, 7, 8])

Get the index of the series:

    In [7]: series.index
    Out[7]: RangeIndex(start=0, stop=5, step=1)

Often you want to set data with labels:

    In [8]: series = pd.Series([4, 5, 6],['a', 'b', 'c'])

    In [9]: series
    Out[9]:
    a    4
    b    5
    c    6
    dtype: int64

Select a single value:

    In [11]: series['b']
    Out[11]: 5

Select multiple values:

    In [12]: series[['b', 'c']]
    Out[12]:
    b    5
    c    6
    dtype: int64

Filtering, scalar multiplication and pplying math functions will preserve the index link:

    In [15]: series[series > 4]
    Out[15]:
    b    5
    c    6
    dtype: int64

    In [16]: series * 2
    Out[16]:
    a     8
    b    10
    c    12
    dtype: int64

    In [19]: np.exp(series)
    Out[19]:
    a     54.598150
    b    148.413159
    c    403.428793
    dtype: float64

You can think of a series as a fixed length, ordered dict.

Check if a label / index exists:

    In [20]: 'b' in series
    Out[20]: True

Creating a series from a python dict:

    In [23]: p_data = {'Gauteng': 5900, 'Western Cape': 3200, 'Northern Cape': 200}

    In [24]: province_series = pd.Series(p_data)

    In [25]: province_series
    Out[25]:
    Gauteng          5900
    Western Cape     3200
    Northern Cape     200
    dtype: int64

You can ignore an index and set the order with the `index` kwarg:

    In [26]: province_series = pd.Series(p_data, index=['Northern Cape', 'Western Cape'])

    In [27]: province_series
    Out[27]:
    Northern Cape     200
    Western Cape     3200
    dtype: int64

If a corresponding value for the index is not found you get a `NaN`

    In [28]: province_series = pd.Series(p_data, index=['Northern Cape', 'Western Cape', 'KwaZulu Natal'])

    In [29]: province_series
    Out[29]:
    Northern Cape     200.0
    Western Cape     3200.0
    KwaZulu Natal       NaN
    dtype: float64

`NaN` stands for Not a Number, which in pandas shows `NA` or missing values.

`pandas.isnull` and `pandas.notnull` should be used to detet missing values.

    In [30]: pd.isnull(province_series)
    Out[30]:
    Northern Cape    False
    Western Cape     False
    KwaZulu Natal     True
    dtype: bool

> Data Alignment can be thought of as a Database `JOIN`

The series and index have a `name` attribute, which integrates with other pandas fucntionality.

    In [32]: series.name = 'FF+ Voters'

    In [33]: series.name
    Out[33]: 'FF+ Voters'

    In [36]: series.index.name = 'Province'

An index can be altered in-place:

    In [37]: series.index = ['Eastern', 'Western', 'Northern']

    In [38]: series
    Out[38]:
    Eastern     4
    Western     5
    Northern    6
    Name: FF+ Voters, dtype: int64


### DataFrame

Rectangular table of data, with an ordered colletin of columns that can be different types.
It has row and column labels.

Under the hood it is stored as one or more two-dimensional blocks. 

You can use hierachical indexing to represent higher dimensional data.

Creating a dataframe from a dict of of equal length lists or numpy arrays.

    In [41]: data = {'province': ['gauteng', 'limpopo', 'northern cape'], 'year': ['2000', '2001', '2002'], 'pop': ['10000', '20000', '30000']}

    In [42]: frame = pd.DataFrame(data)

    In [43]: frame
    Out[43]:
            province  year    pop
    0        gauteng  2000  10000
    1        limpopo  2001  20000
    2  northern cape  2002  30000

To view the first few rows use `head()`:

    In [44]: frame.head()
    Out[44]:
            province  year    pop
    0        gauteng  2000  10000
    1        limpopo  2001  20000
    2  northern cape  2002  30000

Use columns to re-arrange the columns in that order:

    In [45]: frame = pd.DataFrame(data, columns=['province', 'pop', 'year'])

    In [46]: frame
    Out[46]:
            province    pop  year
    0        gauteng  10000  2000
    1        limpopo  20000  2001
    2  northern cape  30000  2002

If you pass a column that does not exist, it will be created with missing values:

    In [51]: frame = pd.DataFrame(data, columns=['province', 'pop', 'year', 'dest'])

    In [52]: frame
    Out[52]:
            province    pop  year dest
    0        gauteng  10000  2000  NaN
    1        limpopo  20000  2001  NaN
    2  northern cape  30000  2002  NaN

Get the columns:

    In [53]: frame.columns
    Out[53]: Index(['province', 'pop', 'year', 'dest'], dtype='object')

Retrieve a single column as a series:

    In [55]: frame.year
    Out[55]:
    0    2000
    1    2001
    2    2002
    Name: year, dtype: object

or

    In [56]: frame['year']
    Out[56]:
    0    2000
    1    2001
    2    2002
    Name: year, dtype: object

> It is more precise to use the index notation (not property dot-notation)

Columns can be modified with assignment of a scalar

    In [61]: frame['pop'] = 100

    In [62]: frame
    Out[62]:
            province  pop  year dest
    0        gauteng  100  2000  NaN
    1        limpopo  100  2001  NaN
    2  northern cape  100  2002  NaN

or a numpy array vector

    In [67]: frame['pop'] = np.arange(3.)

    In [68]: frame
    Out[68]:
            province  pop  year dest
    0        gauteng  0.0  2000  NaN
    1        limpopo  1.0  2001  NaN
    2  northern cape  2.0  2002  NaN

> When assigning an array, the length must much the dataframe's

Assigning a column that does not exist will create a new column

the `del` keyword will delete columns

    In [71]: del frame['dest']

    In [72]: frame
    Out[72]:
            province  pop  year
    0        gauteng    0  2000
    1        limpopo    1  2001
    2  northern cape    2  2002

Create a new column with a boolean expression

    In [75]: frame['is_gauteng'] = frame['province'] == 'gauteng'

    In [76]: frame
    Out[76]:
            province  pop  year  is_gauteng
    0        gauteng    0  2000        True
    1        limpopo    1  2001       False
    2  northern cape    2  2002       False

> The column returned much liek a numpy array is a view, not a copy. Therefore any inplace modification will result in an update to the dataframe.

Another common scenario is nested dicts, which will take outer dict keys as column labels and inner dict keys as row indices.

You can transpose (swap) a dataframes columns and rows.

with `T`:

    In [77]: frame.T
    Out[77]:
                    0        1              2
    province    gauteng  limpopo  northern cape
    pop               0        1              2
    year           2000     2001           2002
    is_gauteng     True    False          False

Set the `index` and `column` names:

    frame.index.name = 'year'
    frame.column.name = 'province'

View the values of a dataframe as a 2-d numpy array:

    In [83]: frame.values
    Out[83]:
    array([['gauteng', 0, '2000', True],
        ['limpopo', 1, '2001', False],
        ['northern cape', 2, '2002', False]], dtype=object)

If the datatypes are different, the `dtype=object`

## Index Objects

Index objects hold `axis labels` and other meta data like axis names. 

    In [5]: obj = pd.Series(range(3), index=['a', 'b', 'c'])

    In [6]: obj.index
    Out[6]: Index(['a', 'b', 'c'], dtype='object')

Index objects are immutable so they cannot be changed by the user

Immutability makes it easier to share index objects among data structures.

Types of Indexes:
* `Index` - array of python objects
* `Int64Index` - integer values
* `Float64Index` - float values for hierachical indexes
* `MultiIndex` - array of tuples
* `RangeIndex` - Spaced sequence 
* `CategoricalIndex` - An index of values with category
* `DateTimeIndex` - Nanosecond timestamps using numpy's `datetime64`
* `PeriodIndex` - Timespans

## Essential Functionality

### Reindexing

Create a new obejct _conformed_ to a new index

    In [7]: obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    In [8]: obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    In [9]: obj
    Out[9]:
    d    4.5
    b    7.2
    a   -5.3
    c    3.6
    dtype: float64
    In [10]: obj2
    Out[10]:
    a   -5.3
    b    7.2
    c    3.6
    d    4.5
    e    NaN
    dtype: float64

For ordered data like timeseries it might be useful to fill in values with the `ffill` method

    In [11]: obj3 = pd.Series(['red', 'green', 'blue'], index=[1, 3, 5])
    In [14]: obj3
    Out[14]:
    1      red
    3    green
    5     blue
    dtype: object

    In [15]: obj3.reindex(range(6), method='ffill')
    Out[15]:
    0      NaN
    1      red
    2      red
    3    green
    4    green
    5     blue
    dtype: object

`bfill` on the other hand fills backwards:

    In [17]: obj3.reindex(range(6), method='bfill')
    Out[17]:
    0      red
    1      red
    2    green
    3    green
    4     blue
    5     blue
    dtype: object

`reindex` an alter the (row) index, columns or both.

    In [18]: frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'b', 'c'],
        ...: columns=['gauteng', 'northern cape', 'limpopo'])

    In [19]: frame
    Out[19]:
    gauteng  northern cape  limpopo
    a        0              1        2
    b        3              4        5
    c        6              7        8

    In [20]: frame2 = frame.reindex(['a', 'b', 'c', 'd'])

    In [21]: frame2
    Out[21]:
    gauteng  northern cape  limpopo
    a      0.0            1.0      2.0
    b      3.0            4.0      5.0
    c      6.0            7.0      8.0
    d      NaN            NaN      NaN

Columns are reindexed using the `columns` keyword:

    In [22]: frame.reindex(columns=['western cape', 'mpumalanga', 'kwazulu natal'])
    Out[22]:
    western cape  mpumalanga  kwazulu natal
    a           NaN         NaN            NaN
    b           NaN         NaN            NaN
    c           NaN         NaN            NaN

Re-indexing can be done better with the label indexing `loc`:

    In [24]: frame.loc[['a', 'b', 'c', 'd'], ['gauteng', 'limpopo', 'northern cape']]
    /Library/Frameworks/Python.framework/Versions/3.6/bin/ipython:1: FutureWarning:
    Passing list-likes to .loc or [] with any missing label will raise
    KeyError in the future, you can use .reindex() as an alternative.

    See the documentation here:
    https://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate-loc-reindex-listlike
    #!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
    Out[24]:
    gauteng  limpopo  northern cape
    a      0.0      2.0            1.0
    b      3.0      5.0            4.0
    c      6.0      8.0            7.0
    d      NaN      NaN            NaN

### Dropping Entries from index

Use `drop`:

    In [28]: frame2
    Out[28]:
    gauteng  limpopo  northern cape
    a      0.0      2.0            1.0
    b      3.0      5.0            4.0
    c      6.0      8.0            7.0
    d      NaN      NaN            NaN

    In [29]: frame2.drop('b')
    Out[29]:
    gauteng  limpopo  northern cape
    a      0.0      2.0            1.0
    c      6.0      8.0            7.0
    d      NaN      NaN            NaN

drop a column:

    In [30]: frame2.drop(columns=['gauteng', 'northern cape'])
    Out[30]:
    limpopo
    a      2.0
    b      5.0
    c      8.0
    d      NaN

Modify in place without returning a value, use `inplace=True`:

    frame2.drop(columns=['gauteng', 'northern cape'], inpalce=True)

### Indexing, Selection and Filtering

Indexing works the same as a `numpy` array except you can use things other than integers.

`loc` and `iloc` (integer label selection) enable you to select a subset of rows and columns
with numpy notation

    data.loc['Colorado', ['two', 'three']]
    data.iloc[[1, 2], [3, 0, 1]]

### Arithmetic and Data Alignment

Adding series or dataframes with create a new series or dataframe with `NaN` values for those that dont exist in both.

You can fill values with:

    df1.add(df2, fill_value=0)

Also works with `reindex`

> Operations between a series and a dataframe are called `broadcasting`

### Function application and mappings

    In [165]: frame
    Out[165]: 
                b         d         e
    Utah   -0.204708  0.478943 -0.519439
    Ohio   -0.555730  1.965781  1.393406
    Texas   0.092908  0.281746  0.769023
    Oregon  1.246435  1.007189 -1.296221

    In [166]: np.abs(frame)
    Out[166]: 
                b         d         e
    Utah    0.204708  0.478943  0.519439
    Ohio    0.555730  1.965781  1.393406
    Texas   0.092908  0.281746  0.769023
    Oregon  1.246435  1.007189  1.296221

### Sorting and Ranking

On a series index use `sort_index`:

    obj.sort_index()

In a dataframe you can sort the whole thing or jsut a single axis:

    frame.sort_index()  

or

    frame.sort_index(axis=1)

You can set to ascending or descending order:

    frame.sort_index(axis=1, ascending=False)

You can sort values with, you guesed it, `sort_values()`

`Nan` values are sent to the end by default.

In a dataframe you can sort by 1 or more columns:

    frame.sort_values(by='b')

or

    frame.sort_values(by=['a', 'b'])

Ranking is similar to sorting, it gives numbers representing where the value should rank in sorting:

    In [32]: series = pd.Series([1, 6, -5, -6, 7, 8, 10, -5])

    In [33]: series.rank()
    Out[33]:
    0    4.0
    1    5.0
    2    2.5
    3    1.0
    4    6.0
    5    7.0
    6    8.0
    7    2.5
    dtype: float64

Rank based on the order they appear in the data (whatever that means):

    In [36]: series.rank(method='first')
    Out[36]:
    0    4.0
    1    5.0
    2    2.0
    3    1.0
    4    6.0
    5    7.0
    6    8.0
    7    3.0
    dtype: float64

Tie breaking methods:

    average, min, max, first, sense

### Duplicate Index values

Unique axis labels are not mandatory

    In [37]: obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])

    In [38]: obj
    Out[38]:
    a    0
    a    1
    b    2
    b    3
    c    4
    dtype: int64

Check of the index is unique:

    In [39]: obj.index.is_unique
    Out[39]: False

Selecting an index will return both values:

    In [40]: obj['a']
    Out[40]:
    a    0
    a    1
    dtype: int64

### Descriptive Statistics

`sum()`

    In [41]: frame
    Out[41]:
    gauteng  northern cape  limpopo
    a        0              1        2
    b        3              4        5
    c        6              7        8

    In [42]: frame.sum()
    Out[42]:
    gauteng           9
    northern cape    12
    limpopo          15
    dtype: int64

`sum(axis=1)`

    In [43]: frame.sum(axis=1)
    Out[43]:
    a     3
    b    12
    c    21
    dtype: int64

Set an `NaN` value:

    In [56]: frame.loc['a', 'gauteng'] = 'NaN'

    In [57]: frame
    Out[57]:
    gauteng  northern cape  limpopo
    a     NaN              1        2
    b       3              4        5
    c       6              7        8

So you can choose to not `skipna` values which is True by default:

    In [58]: frame.mean(axis=1)
    Out[58]:
    a    1.5
    b    4.5
    c    7.5
    dtype: float64

    In [59]: frame.mean(axis=1, skipna=False)
    Out[59]:
    a    1.5
    b    4.5
    c    7.5
    dtype: float64

> no difference in the above case

`describe` the frame:

    In [63]: frame.describe()
    Out[63]:
        northern cape  limpopo
    count            3.0      3.0
    mean             4.0      5.0
    std              3.0      3.0
    min              1.0      2.0
    25%              2.5      3.5
    50%              4.0      5.0
    75%              5.5      6.5
    max              7.0      8.0

It will return alternate data if it is non-numeric

Methods:

    count, describe, min, max, sum, mean, median, prod, var, std, skew, kurt, cumsum, diff

### Correlation and Covariance

Lets consider some stock price close and volume for these summary statistics.

We need:

    pip install pandas_datareader

Lets get the data:

    import pandas as pd
    import pandas_datareader.data as web

    all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}

    price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
    volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})

    In [9]: price.head()
    Out[9]:
                    AAPL         IBM       MSFT        GOOG
    Date
    2010-01-04  27.095369  102.944206  24.827723  311.349976
    2010-01-05  27.142210  101.700638  24.835745  309.978882
    2010-01-06  26.710482  101.039986  24.683319  302.164703
    2010-01-07  26.661104  100.690277  24.426620  295.130463
    2010-01-08  26.838356  101.700638  24.595085  299.064880

Compute the percentage changes in the price:

    In [10]: returns = price.pct_change()

    In [11]: returns.tail()
    Out[11]:
                    AAPL       IBM      MSFT      GOOG
    Date
    2018-10-17 -0.004321 -0.076282 -0.002613 -0.004985
    2018-10-18 -0.023374 -0.026110 -0.019962 -0.024846
    2018-10-19  0.015230 -0.011107  0.001475  0.007804
    2018-10-22  0.006110  0.007126  0.008927  0.004287
    2018-10-23  0.009427  0.009152 -0.013956  0.002297

The `corr` method of `Series` computes the correlation of the overlapping, non-NA, aligned-by-index values in two Series. `cov` computes the covariance.

    In [15]: returns['MSFT'].corr(returns['IBM'])
    Out[15]: 0.4723006230591393

    In [16]: returns['MSFT'].cov(returns['IBM'])
    Out[16]: 8.074798783252494e-05

Using these methods on the `DataFrame` returns a correlation or covariance matrix.

    In [17]: returns.cov()
    Out[17]:
            AAPL       IBM      MSFT      GOOG
    AAPL  0.000251  0.000069  0.000094  0.000105
    IBM   0.000069  0.000145  0.000081  0.000073
    MSFT  0.000094  0.000081  0.000201  0.000111
    GOOG  0.000105  0.000073  0.000111  0.000231

    In [18]: returns.corr()
    Out[18]:
            AAPL       IBM      MSFT      GOOG
    AAPL  1.000000  0.362561  0.419753  0.436144
    IBM   0.362561  1.000000  0.472301  0.396107
    MSFT  0.419753  0.472301  1.000000  0.513596
    GOOG  0.436144  0.396107  0.513596  1.000000

You can do pair-wise corrlation with `corrwith`:

    In [20]: returns.corrwith(returns['GOOG'])
    Out[20]:
    AAPL    0.436144
    IBM     0.396107
    MSFT    0.513596
    GOOG    1.000000
    dtype: float64

correlation of percentage changes with volume:

    In [21]: returns.corrwith(volume)
    Out[21]:
    AAPL   -0.066129
    IBM    -0.173960
    MSFT   -0.087216
    GOOG   -0.017287
    dtype: float64

### Unique Values, Value Counts and Membership

    In [22]: obj = pd.Series(['a', 'b', 'c', 'c', 'b', 'b', 'a', 'b', 'a', 'c', 'b' ])

    In [23]: uniques = obj.unique()

    In [24]: uniques
    Out[24]: array(['a', 'b', 'c'], dtype=object)

> Unique values are not retruned in sorted order but can be sorted after the fact if needed

`value_counts()` computes a series containing value frequencies:

    In [25]: obj.value_counts()
    Out[25]:
    b    5
    c    3
    a    3
    dtype: int64

> It is sorted in descending order for convenience

You can use `value_counts()` from the package

In [26]: pd.value_counts(obj, sort=False)
Out[26]:
b    5
a    3
c    3
dtype: int64

Membership check with `isin()`:

    In [27]: mask = obj.isin(['b', 'c'])

    In [28]: mask
    Out[28]:
    0     False
    1      True
    2      True
    3      True
    4      True
    5      True
    6     False
    7      True
    8     False
    9      True
    10     True
    dtype: bool

    In [29]: obj[mask]
    Out[29]:
    1     b
    2     c
    3     c
    4     b
    5     b
    7     b
    9     c
    10    b
    dtype: object

`Index.get_indexer` gives you an index array from an array of possible non-distinct values into another array of distinct values

    In [30]: unique_vals = obj.unique()

    In [31]: unique_vals
    Out[31]: array(['a', 'b', 'c'], dtype=object)

    In [32]: pd.Index(unique_vals).get_indexer(obj)
    Out[32]: array([0, 1, 2, 2, 1, 1, 0, 1, 0, 2, 1])

# Chapter 6: Data Loading, Storage and File Formats

## Reading and writing data in text formats

Python is good for working with text and file mungingdue to its:
* simple syntax for interacting with files
* lightweight built-in datastructures
* convenient language features (tuple packing and unpacking)

Reading data into a dataframe:

* `read_csv` - comma seperated values
* `read_table` - load delimited data from a file (`\t` is default delimiter)
* `read_fwf` - load dat from file with fixed width column format
* `read_clipboard` - Reads data from clipboard (from webpages)
* `read_excel` - Read tabular data from excel xls
* `read_hdf` - Read from HDF5
* `read_html` - Read from `<table>`s in an html document
* `read_json` - Reads from json (javascript object notation) string
* `read_msgpack` - read from MessagePack binary format
* `read_pickle` - read an object from python pickle format
* `read_sas` - Read a SAS dataset
* `read_sql` - Read the result on a sql query (using SQLALchemy) as a pandas Dataframe.
* `read_stata` - Read from a stata file format
* `read_feather` - Read from feather file format

Data is messy in the real world and hence there are many options available to `read_csv` for example for neatening data.

_type inference_ means you don't need to explicitly specify the data type of the columns for numeric, integer, boolean or string.
Dates however do require a bit of effort

    In [1]: !cat ex1.csv
    a,b,c,d,message
    1,2,3,4,hello
    5,6,7,8,world
    9,10,11,12,foo

    In [3]: df = pd.read_csv('ex1.csv')

    In [4]: df
    Out[4]:
    a   b   c   d message
    0  1   2   3   4   hello
    1  5   6   7   8   world
    2  9  10  11  12     foo

We could have also used:

    In [7]: df = pd.read_table('ex1.csv', delimiter=',')

If your data does not have headers (the first line), you can specify none and let pandas default:

    df = pd.read_csv('ex1.csv', headers=None)

or set them with:

    df = pd.read_csv('ex1.csv', headers=['a', 'b', 'c', 'd', 'message'])

Hierachical data can be split using `index_col`:

    In [11]: !cat csv_mindex.csv
    key1,key2,value1,value2
    one,a,1,2
    one,b,3,4
    one,c,5,6
    one,d,7,8
    two,a,9,10
    two,b,11,12
    two,c,13,14
    two,d,15,16

    In [13]: parsed = pd.read_csv('csv_mindex.csv', index_col=['key1', 'key2'])

    In [14]: parsed
    Out[14]:
            value1  value2
    key1 key2
    one  a          1       2
         b          3       4
         c          5       6
         d          7       8
    two  a          9      10
         b         11      12
         c         13      14
         d         15      16

In some cases a file may not have a delimiter, perhaps it is just whitespace in that case you can give it a regular expression to the `sep` kwarg:

    In [23]: list(open('ex2.txt'))
    Out[23]:
    ['            A         B         C\n',
    ' aaa -0.264438 -1.026059 -0.619500\n',
    ' bbb  0.927272  0.302904 -0.032399\n',
    ' ccc -0.264273 -0.386314 -0.217601\n',
    ' ddd -0.871858 -0.348382  1.100491\n']

    In [24]: result = pd.read_table('ex2.txt', sep='\s+')

    In [25]: result
    Out[25]:
                A         B         C
    aaa -0.264438 -1.026059 -0.619500
    bbb  0.927272  0.302904 -0.032399
    ccc -0.264273 -0.386314 -0.217601
    ddd -0.871858 -0.348382  1.100491

You can skip certain rows with `skiprows=[0, 3, 4]`

Handling missing values in pandas is important. Missing data is usually an empty string or a _sentinel_ value: `NA`, `-1.#IND`, `NULL`

The `na_values` kwarg can take a list or set of strings to consider mssing values:

    result = pd.read_csv('examples/ex5.csv', na_values=['NULL'])

Different `NA` sentinels can be specified for each column in a dict:

    sentinels = {'message': ['foo', 'NA'], 'something': ['two']
    pd.read_csv('examples/ex5.csv', na_values=sentinels)

### Some Other Arguments

* `path` - location or url of object
* `sep` or `delimiter` - character sequence or regular expression to seperate data in rows
* `comment` - character to split comment out at end of lines
* `parse_dates` - Attemptt o parse data to `datetime`, can give a list of columns to try. It is `False` by default.

## Reading Text Files in Pieces

For large files you may want to work on small chunks of a file at a time, and not have the entire file in memory.

Check the book

## Writing Data out to Text Format

Data can be exported to a file using panda's `to_csv` function.

    In [28]: df.to_csv('out.csv')

    In [29]: !cat out.csv
    ,a,b,c,d,message
    0,1,2,3,4,hello
    1,5,6,7,8,world
    2,9,10,11,12,foo

You can use a different seperator and write to `stdout` with:

    In [30]: import sys

    In [31]: df.to_csv(sys.stdout, sep='|')
    |a|b|c|d|message
    0|1|2|3|4|hello
    1|5|6|7|8|world
    2|9|10|11|12|foo

Missing values are shown as empty strings to use something else use `na_rep='NULL'`

Both row and columnlabels are written by default, this can be disabled with:

`index=False` and `header=False`

You can also specify which columns you want to write:

    In [32]: df.to_csv('out.csv', columns=['a', 'b', 'message'])

    In [33]: !cat out.csv
    ,a,b,message
    0,1,2,hello
    1,5,6,world
    2,9,10,foo

### Manually working with delimited formats

Sometimes you receive a csv with malformed lines

    In [35]: !cat ex7.csv
    “a","b","c"
    "1","2","3"
    "1","2","3","4”

For any file with a single character delimiter you can use pythons's `csv` module:

    In [36]: import csv

    In [37]: f = open('ex7.csv')

    In [38]: reader = csv.reader(f)

    In [39]: for line in reader:
        ...:     print(line)
    ['“a"', 'b', 'c']
    ['1', '2', '3']
    ['1', '2', '3', '4”\n']

From there you can do the wrangling you need

Defining a new csv format with a different delimiter, string quoting or line termination convension is done by defining a subclass of `csv.Dialect`

    class my_dialect(csv.Dialect):
        line_terminator = '\n'
        delimiter = ';'
        quote_char = '"'
        quoting = csv.QUOTE_MINIMAL

    reader = csv.reader(f, dialect=my_dialect)

Individual parameters can be given as keywords:

    reader = csv.reader(f, delimiter='|')

> Files with fixed multi-character delimiters won't be able to use `csv`

To write csv files:

    with open('mydata.csv', 'w') as f:
        writer = csv.writer(f, dialect=my_dialect)
        writer.writerow(('one', 'two', 'three'))
        writer.writerow(('1', '2', '3'))
        writer.writerow(('4', '5', '6'))
        writer.writerow(('7', '8', '9'))

### JSON Data

JSON (Javascript Object Notation) has become a standard for sending data over HTTP.
It is nearly valid python code except for its null value `null` and nuances like not allowing trailing commas.
All the keys in a JSON object must be strings.

We will make use of the built-in `json` module.

To convert a json string to a python, use `json.loads`:

    obj = """
    {"name": "Wes",
    "places_lived": ["United States", "Spain", "Germany"],
    "pet": null,
    "siblings": [{"name": "Scott", "age": 29, "pets": ["Zeus", "Zuko"]},
                {"name": "Katie", "age": 38,
                "pets": ["Sixes", "Stache", "Cisco"]}]
    }
    ""”

    In [45]: import json
    In [46]: result = json.loads(obj)
    In [47]: result
    Out[47]:
    {'name': 'Wes',
    'places_lived': ['United States', 'Spain', 'Germany'],
    'pet': None,
    'siblings': [{'name': 'Scott', 'age': 29, 'pets': ['Zeus', 'Zuko']},
    {'name': 'Katie', 'age': 38, 'pets': ['Sixes', 'Stache', 'Cisco']}]}

`json.dumps` converts a python object back to json:

    In [48]: as_json = json.dumps(obj)

    In [49]: as_json
    Out[49]: '"\\n{\\"name\\": \\"Wes\\",\\n \\"places_lived\\": [\\"United States\\", \\"Spain\\", \\"Germany\\"],\\n \\"pet\\": null,\\n \\"siblings\\": [{\\"name\\": \\"Scott\\", \\"age\\": 29, \\"pets\\": [\\"Zeus\\", \\"Zuko\\"]},\\n              {\\"name\\": \\"Katie\\", \\"age\\": 38,\\n          \\"pets\\": [\\"Sixes\\", \\"Stache\\", \\"Cisco\\"]}]\\n}\\n"'

You can pass a list of JSON objects to the DataFrame constructor:

    In [51]: siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])

    In [52]: siblings
    Out[52]:
        name  age
    0  Scott   29
    1  Katie   38

`pd.read_json` automatically converts json datasets into a Series or DataFrame.

    data = pd.read_json('examples/example.json')

To export data from pandas to json use `to_json`:

    data.to_json()

### XML and HTML: Web Scraping

Python has a few libraries to read and write data: `lxml`, Beautiful Soup and `html5lib`

Pandas has the built-in `read_html` which automatically parses tables out of html files into a DataFrame.
By default it find and parses data in `<table>` tags.

    In [3]: tables = pd.read_html('fdic_failed_bank_list.html')

Returns a list

    In [9]: type(tables)
    Out[9]: list

The data is held in elements of that list:

    In [14]: failures = tables[0]

    In [15]: failures.head()
    Out[15]:
                        Bank Name             City  ST        ...                        Acquiring Institution        Closing Date       Updated Date
    0                   Allied Bank         Mulberry  AR        ...                                 Today's Bank  September 23, 2016  November 17, 2016
    1  The Woodbury Banking Company         Woodbury  GA        ...                                  United Bank     August 19, 2016  November 17, 2016
    2        First CornerStone Bank  King of Prussia  PA        ...          First-Citizens Bank & Trust Company         May 6, 2016  September 6, 2016
    3            Trust Company Bank          Memphis  TN        ...                   The Bank of Fayette County      April 29, 2016  September 6, 2016
    4    North Milwaukee State Bank        Milwaukee  WI        ...          First-Citizens Bank & Trust Company      March 11, 2016      June 16, 2016

    [5 rows x 7 columns]

We can compute the number of bank failures per year:

    In [16]: close_timestamps = pd.to_datetime(failures['Closing Date'])

    In [18]: close_timestamps.dt.year.value_counts()
    Out[18]:
    2010    157
    2009    140
    2011     92
    2012     51
    2008     25
    2013     24
    2014     18
    2002     11
    2015      8
    2016      5
    2004      4
    2001      4
    2007      3
    2003      3
    2000      2
    Name: Closing Date, dtype: int64

### Parsing XML with lxml.objectify

Read the book...

### Binary Data Formats

One of the easiest ways to store data (serialisaton) is using python's `pickle`.
It is efficient and stores data in binary.

    In [19]: frame = pd.read_csv('ex1.csv')

    In [21]: frame
    Out[21]:
    a   b   c   d message
    0  1   2   3   4   hello
    1  5   6   7   8   world
    2  9  10  11  12     foo

    In [23]: frame.to_pickle('frame_pickle')

Any pickled object can be read by `pickle` directly or with `pd.read_pickle`:

> Pickle is recommended for short term storage. It is hard to gaurentee that the format will be stable over time.

Other formats `HDF5` and `MessagePack` as well as `Feather` can be checkout out in the book

### Reading Microsoft Excel Files

Excel 2003 and higher. You use it with `pd.ExcelFile` and `pd.read_excel`.

Internally these tools add on the `xlrd` and `openpyxl` packages. YOu will probably need to isntall these packages seperately.

First create the excel file:

    In [2]: xlsx = pd.ExcelFile('ex1.xlsx')

    In [3]: xlsx
    Out[3]: <pandas.io.excel.ExcelFile at 0x119658dd8>

Then read it with:

    In [5]: pd.read_excel(xlsx)
    Out[5]:
    a   b   c   d message
    0  1   2   3   4   hello
    1  5   6   7   8   world
    2  9  10  11  12     foo

> If you are reading a file with multiple sheets it is faster to create the file, otherwise you can simple pass the file path to `pd.read_excel`

To write to an excel file you must first create an `ExcelWriter`, then write data to it using `to_excel`:

    In [9]: writer = pd.ExcelWriter('ex2.xlsx')
    In [10]: frame.to_excel(writer)
    In [11]: writer.save()

### Interacting with Web Apis

A good package to familiarise yourself with is `requests`

We can pass data directly into a dataframe and extract fields of interest.

    In [15]: url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

    In [16]: resp = requests.get(url)

    In [17]: resp
    Out[17]: <Response [200]>

    In [18]: data = resp.json()

    In [19]: data[0]['title']
    Out[19]: 'ENH: Implement IntervalIndex.is_overlapping'

    In [20]: issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])

    In [21]: issues
    Out[21]:
        number                                              title                                             labels state
    0    23327        ENH: Implement IntervalIndex.is_overlapping  [{'id': 76812, 'node_id': 'MDU6TGFiZWw3NjgxMg=...  open
    1    23326         Data type of new assigned DataFrame column  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open
    2    23325  AttributeError: module 'pandas' has no attribu...                                                 []  open
    3    23324  Rounding valid timestamps near daylight saving...  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open
    4    23323                 TST: Update sparse data generation  [{'id': 49182326, 'node_id': 'MDU6TGFiZWw0OTE4...  open
    5    23321           Support for partition_cols in to_parquet  [{'id': 685114413, 'node_id': 'MDU6TGFiZWw2ODU...  open
    6    23320  BUG/TST: timedelta-like with Index/Series/Data...                                                 []  open

### Interacting with Databases

In a business setting most data will be stored in a relational database: SQLServer, PosgreSQL and MySQL.

It is much faster to use [sqlalchemy](https://docs.sqlalchemy.org/en/latest/) instead of using native drivers.

    pip install SQLAlchemy
    pip install mysqlclient

Typically you would connect to a database with a url like:

    dialect+driver://username:password@host:port/database

Eg.

    engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
    engine = create_engine('mysql://scott:tiger@localhost/foo')
    engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')
    engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')
    engine = create_engine('mssql+pyodbc://scott:tiger@mydsn')


    In [5]: queue_frame = pd.read_sql('select * from chart_queue', db)

# Chapter 7: Data Cleaning and Preparation





Excerpt From: Unknown. “Python for Data Analysis, 2nd Edition.” iBooks. 

Source: [O'reilly Python for Data Analysis](http://shop.oreilly.com/product/0636920050896.do)