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

A significant amount of your time in data analysis and modelling is spent on data preparation: loading, cleaning, transforming and rearranging.

Apparently taking up to 80% of your codng time

## Handling Missing Data

All descriptive statistics exclude missing data by default.

The missing sentinel value for floating points is `NaN` which is imperfect but functional.

    In [1]: import pandas as pd
    In [2]: import numpy as np

    In [5]: string_data = pd.Series(['Aardvark', 'Artichoke', np.nan, 'Avocado'])

    In [6]: string_data.isnull()
    Out[6]:
    0    False
    1    False
    2     True
    3    False
    dtype: bool

In pandas, we've adopted a convention used in the R languageby reffering to missing data as `NA` (Not Available).
`NA` may mean data that does not exist or data that exists but was not observed (due to data collection problems).

The built-in python `None` value is also treated as `NA` in object arrays

    In [7]: string_data[0] = None

    In [8]: string_data
    Out[8]:
    0         None
    1    Artichoke
    2          NaN
    3      Avocado
    dtype: object

    In [10]: string_data.isnull()
    Out[10]:
    0     True
    1    False
    2     True
    3    False
    dtype: bool

### Filtering out Missing Data

You can use `isnull()` and boolean indexing but `dropna` can also be helpful.

    In [11]: from numpy import nan as NA

    In [12]: data = pd.Series([1, NA, 3.5, 7])

    In [13]: data.dropna()
    Out[13]:
    0    1.0
    2    3.5
    3    7.0
    dtype: float64

which is equivalent to:

    In [15]: data[data.notnull()]
    Out[15]:
    0    1.0
    2    3.5
    3    7.0
    dtype: float64

On a dataframe `dropna()` drops all rows containing a missing value

Passing `how=all` will only drop rows where all the values are missing

    data.dropna(how='all')

To drop columns, do the same thing but where `axis=1`

    data.dropna(axis=1, how='all')

Suppose you only want to keep rows containing a certain number of observations. For that you would use `thresh`:

    In [16]: df = pd.DataFrame(np.random.randn(7, 3))

    In [17]: df
    Out[17]:
            0         1         2
    0  0.871250 -1.434184  1.323816
    1 -2.049019  1.685563 -0.028869
    2 -0.284594 -1.658746 -0.893838
    3 -0.306614 -0.045451  0.072289
    4  1.253934  0.242588  0.802684
    5  1.301810 -1.869278  0.492717
    6  0.307062 -0.273495 -0.468776

    In [18]: df.iloc[:4, 1] = NA

    In [19]: df
    Out[19]:
            0         1         2
    0  0.871250       NaN  1.323816
    1 -2.049019       NaN -0.028869
    2 -0.284594       NaN -0.893838
    3 -0.306614       NaN  0.072289
    4  1.253934  0.242588  0.802684
    5  1.301810 -1.869278  0.492717
    6  0.307062 -0.273495 -0.468776

    In [20]: df.iloc[:2, 2] = NA

    In [21]: df
    Out[21]:
            0         1         2
    0  0.871250       NaN       NaN
    1 -2.049019       NaN       NaN
    2 -0.284594       NaN -0.893838
    3 -0.306614       NaN  0.072289
    4  1.253934  0.242588  0.802684
    5  1.301810 -1.869278  0.492717
    6  0.307062 -0.273495 -0.468776

    In [22]: df.dropna(thresh=3)
    Out[22]:
            0         1         2
    4  1.253934  0.242588  0.802684
    5  1.301810 -1.869278  0.492717
    6  0.307062 -0.273495 -0.468776

    In [23]: df.dropna(thresh=2)
    Out[23]:
            0         1         2
    2 -0.284594       NaN -0.893838
    3 -0.306614       NaN  0.072289
    4  1.253934  0.242588  0.802684
    5  1.301810 -1.869278  0.492717
    6  0.307062 -0.273495 -0.468776

### Filling in Missing Data

Calling `fillna` with a constant replaces missing values with that value:

    In [24]: df.fillna(0)
    Out[24]:
            0         1         2
    0  0.871250  0.000000  0.000000
    1 -2.049019  0.000000  0.000000
    2 -0.284594  0.000000 -0.893838
    3 -0.306614  0.000000  0.072289
    4  1.253934  0.242588  0.802684
    5  1.301810 -1.869278  0.492717
    6  0.307062 -0.273495 -0.468776

You can use a different fill value for a different column with a dict:

    In [28]: df.fillna({0: -1, 1: 0.5, 2: 0})
    Out[28]:
            0         1         2
    0  0.871250  0.500000  0.000000
    1 -2.049019  0.500000  0.000000
    2 -0.284594  0.500000 -0.893838
    3 -0.306614  0.500000  0.072289
    4  1.253934  0.242588  0.802684
    5  1.301810 -1.869278  0.492717
    6  0.307062 -0.273495 -0.468776

You can change it inplace with `inplace=True` instead of retruning a new object

The same indexing methods available can be used with `fillna`:

    In [30]: df = pd.DataFrame(np.random.randn(6, 3))

    In [31]: df.iloc[2:, 1] = NA; df.iloc[4:, 2] = NA

    In [32]: df
    Out[32]:
            0         1         2
    0  0.427217 -0.321663  0.806618
    1 -0.918541  1.607939 -0.374820
    2 -0.720018       NaN -0.989154
    3  0.740126       NaN  0.176258
    4 -0.920978       NaN       NaN
    5  0.449166       NaN       NaN

    In [33]: df.fillna(method='ffill')
    Out[33]:
            0         1         2
    0  0.427217 -0.321663  0.806618
    1 -0.918541  1.607939 -0.374820
    2 -0.720018  1.607939 -0.989154
    3  0.740126  1.607939  0.176258
    4 -0.920978  1.607939  0.176258
    5  0.449166  1.607939  0.176258

and limit:

    In [34]: df.fillna(method='ffill', limit=2)
    Out[34]:
            0         1         2
    0  0.427217 -0.321663  0.806618
    1 -0.918541  1.607939 -0.374820
    2 -0.720018  1.607939 -0.989154
    3  0.740126  1.607939  0.176258
    4 -0.920978       NaN  0.176258
    5  0.449166       NaN  0.176258

You could also fill data with the mean:

    In [35]: data = pd.Series([1.0, NA, 3.5, NA, 7])

    In [36]: data.fillna(data.mean())
    Out[36]:
    0    1.000000
    1    3.833333
    2    3.500000
    3    3.833333
    4    7.000000
    dtype: float64

## Data Transformation

### Removing Duplicates

The `duplicated()` method returns a boolean series of whether each row is duplicated or not:

    df.duplicated() == True

To get a dataframe with duplciates dropped:

    df.drop_duplicates()

Both methods consider all of the columns by default.

Suppose you want to filter only on a certain column:

    data.drop_duplicates(['k1'])

The first occurance is kept by default, if you want to keep the last use the kwarg `keep='last'`

### Transforming Data Using a Function or Mapping

    In [39]: data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'pastrami', 'corned beef', 'Bacon', 'Pastrami'],
    ...: 'ounces': [4, 3, 12, 6, 7.5, 8, 3,]})
    In [40]: data
    Out[40]:
            food  ounces
    0        bacon     4.0
    1  pulled pork     3.0
    2        bacon    12.0
    3     pastrami     6.0
    4  corned beef     7.5
    5        Bacon     8.0
    6     Pastrami     3.0

Suppose you wanted to add a column for the animal a type of meat comes from:

    meat_to_animal = {
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
    }

The `map` method on a series accepts a function or dict-like mapping, but there is a problem some meats are capitalised.

In [42]: data['animal'] = data['food'].str.lower().map(meat_to_animal)

    In [43]: data
    Out[43]:
            food  ounces animal
    0        bacon     4.0    pig
    1  pulled pork     3.0    pig
    2        bacon    12.0    pig
    3     pastrami     6.0    cow
    4  corned beef     7.5    cow
    5        Bacon     8.0    pig
    6     Pastrami     3.0    cow

We could have also used a function:

    In [45]: data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])

### Replaceing Values

Take this data:

    In [48]: data = pd.Series([1., -999., 2., -999., -1000., 3.])

    In [49]: data
    Out[49]:
    0       1.0
    1    -999.0
    2       2.0
    3    -999.0
    4   -1000.0
    5       3.0
    dtype: float64

Say that `-999` is a sentinel for missing data. To replace this with data pandas understands we can use `replace`:

    In [50]: data.replace(-999, np.NAN)
    Out[50]:
    0       1.0
    1       NaN
    2       2.0
    3       NaN
    4   -1000.0
    5       3.0
    dtype: float64

You can replace multiple values:

    In [51]: data.replace([-999, -1000], np.NAN)
    Out[51]:
    0    1.0
    1    NaN
    2    2.0
    3    NaN
    4    NaN
    5    3.0
    dtype: float64

Multiple specific replacements:

    In [52]: data.replace({-999: 0 , -1000: np.NAN})
    Out[52]:
    0    1.0
    1    0.0
    2    2.0
    3    0.0
    4    NaN
    5    3.0
    dtype: float64

### Renaming axis

    transform = lambda x: x[:4].upper()
    data.index.map(transform)

or 

data.rename(index=str.title, columns=str.upper)
data.rename(index={'OHIO': 'INDIANA'}, inplace=True)

## Discretisation and Binning

Continuous data is often seperated into bins

Say you have ages:

    In [53]: ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

    In [54]: ages
    Out[54]: [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

    In [55]: bins = [18, 25, 35, 60, 100]

You then use the `cut` function

In [56]: cats = pd.cut(ages, bins)

    In [57]: cats
    Out[57]:
    [(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
    Length: 12
    Categories (4, interval[int64]): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]

The object returned is a special `Categorical` object

    In [58]: cats.codes
    Out[58]: array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)

    In [59]: cats.categories
    Out[59]:
    IntervalIndex([(18, 25], (25, 35], (35, 60], (60, 100]]
                closed='right',
                dtype='interval[int64]')

    In [60]: pd.value_counts(cats)
    Out[60]:
    (18, 25]     5
    (35, 60]     3
    (25, 35]     3
    (60, 100]    1
    dtype: int64

Consistent with mathemtical notation: a parenthesis `(` means that side is open while a square bracket means closed `]` (inclusive).
You can set which side is open or closed with `right=False`

    In [61]: cats = pd.cut(ages, bins, right=False)

    In [62]: cats
    Out[62]:
    [[18, 25), [18, 25), [25, 35), [25, 35), [18, 25), ..., [25, 35), [60, 100), [35, 60), [35, 60), [25, 35)]
    Length: 12
    Categories (4, interval[int64]): [[18, 25) < [25, 35) < [35, 60) < [60, 100)]

If you give cut an integer instead of explicit bin edges it will computer equal length bins based on minimum and maximum values in the data.

    In [64]: data = np.random.randn(20)

    In [65]: data
    Out[65]:
    array([ 0.31992007, -1.37057101, -0.78414082,  1.41844717, -0.29812797,
            0.9521121 ,  0.82879956,  2.77438651,  0.75959752, -1.31259677,
            0.51138379, -0.32840281,  1.81732981, -0.52482447,  0.72973532,
            0.49750981, -0.56058252, -0.25608326,  0.28111671,  2.05995848])

    In [66]: pd.cut(data, 4, precision=2)
    Out[66]:
    [(-0.33, 0.7], (-1.37, -0.33], (-1.37, -0.33], (0.7, 1.74], (-0.33, 0.7], ..., (-0.33, 0.7], (-1.37, -0.33], (-0.33, 0.7], (-0.33, 0.7], (1.74, 2.77]]
    Length: 20
    Categories (4, interval[float64]): [(-1.37, -0.33] < (-0.33, 0.7] < (0.7, 1.74] < (1.74, 2.77]]

A similar related function `qcut`, cuts bins based on quantiles.
Depending on the distribution of the data using `cut` will not usually result in each bin having the same amount of data points.

`qcut` uses sample quantiles instead, by definition you receive roughly equal sized bins.

    In [67]: data = np.random.randn(1000)

    In [68]: cats = pd.qcut(data, 4)

    In [69]: cats
    Out[69]:
    [(-0.647, 0.0519], (0.719, 3.005], (-0.647, 0.0519], (-0.647, 0.0519], (-0.647, 0.0519], ..., (0.719, 3.005], (0.0519, 0.719], (0.719, 3.005], (-0.647, 0.0519], (0.719, 3.005]]
    Length: 1000
    Categories (4, interval[float64]): [(-3.189, -0.647] < (-0.647, 0.0519] < (0.0519, 0.719] <
                                        (0.719, 3.005]]

    In [70]: pd.value_counts(cats)
    Out[70]:
    (0.719, 3.005]      250
    (0.0519, 0.719]     250
    (-0.647, 0.0519]    250
    (-3.189, -0.647]    250
    dtype: int64

You can pass your own quantiles (values from 0 to 1):

    In [71]: cats = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1])

    In [72]: cats.value_counts()
    Out[72]:
    (-3.189, -1.305]    100
    (-1.305, 0.0519]    400
    (0.0519, 1.257]     400
    (1.257, 3.005]      100
    dtype: int64

### Detecting and Filtering Outliers

Filtering or transforming outliers is largely a matter of applying array operations.

    In [73]: data = pd.DataFrame(np.random.randn(1000, 4))

    In [74]: data.describe()
    Out[74]:
                    0            1            2            3
    count  1000.000000  1000.000000  1000.000000  1000.000000
    mean     -0.007788    -0.010025     0.029215     0.011847
    std       0.983244     1.028296     1.004748     1.009238
    min      -3.015770    -3.204882    -3.727639    -2.709379
    25%      -0.650793    -0.670933    -0.699211    -0.655731
    50%      -0.028469    -0.024508     0.036163    -0.006192
    75%       0.675486     0.668831     0.762269     0.694783
    max       3.156981     3.034008     2.976704     3.516318

Suppose you want to find the values in a column exceeding 3 in magnitude:

    In [76]: col[np.abs(col)> 3]
    Out[76]:
    218    3.128675
    509    3.011054
    699    3.516318
    Name: 3, dtype: float64

To select all the rows have a magnitude greater than 3, use `any`

    In [77]: data[(np.abs(data) > 3).any(1)]
    Out[77]:
                0         1         2         3
    187 -3.015770 -0.028759 -0.087647  1.514852
    218  0.677857  0.448257  0.334189  3.128675
    313  3.156981 -0.842627 -0.762875  0.803619
    487 -0.620277 -3.094748  0.769148 -0.081738
    509  0.346854 -1.075202  0.175269  3.011054
    640  0.538403 -3.204882 -2.088300  1.448109
    697 -0.388438  1.511103 -3.727639  0.479053
    699  0.580033  1.228524  1.146316  3.516318
    953  1.060103  3.034008  0.980496  0.985401
    962 -0.683237 -3.093548  0.467704  0.111335

You can set the values of the outliers, eg:

    data[np.abs(data) > 3] = np.sign(data) * 3

> `np.sign` returns -1 or 1 based on the sign of the values

### Permutation and Random Sampling

Permuting (random reordering) a series or rows in a dataframe is easy to do suing the `numpy.random.permutations` function.

You can create a sampler and then use `df.take` - return values in positional indexing

    In [79]: df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))

    In [80]: df
    Out[80]:
        0   1   2   3
    0   0   1   2   3
    1   4   5   6   7
    2   8   9  10  11
    3  12  13  14  15
    4  16  17  18  19

    In [81]: sampler = np.random.permutation(5)

    In [82]: sampler
    Out[82]: array([3, 0, 4, 1, 2])

    In [83]: df.take(sampler)
    Out[83]:
        0   1   2   3
    3  12  13  14  15
    0   0   1   2   3
    4  16  17  18  19
    1   4   5   6   7
    2   8   9  10  11

To get a random subset without replacement:

    In [85]: df.take(np.random.permutation(len(df))[:3])
    Out[85]:
    0  1   2   3
    1  4  5   6   7
    0  0  1   2   3
    2  8  9  10  11

To generate a sample with replacement:

    In [86]: bag = np.array([5, 7, -1, 6, 4])

    In [87]: sampler = np.random.randint(0, len(bag), size=10)

    In [88]: sampler
    Out[88]: array([0, 0, 0, 0, 2, 1, 0, 3, 1, 2])

    In [89]: draws = bag.take(sampler)

    In [90]: draws
    Out[90]: array([ 5,  5,  5,  5, -1,  7,  5,  6,  7, -1])

    In [91]: bag
    Out[91]: array([ 5,  7, -1,  6,  4])

## Computing Indicator / Dummy Variables

Another type of trasformation for statistical modelling and machine learning is converting a categorical variable into a "dummy" or "indicator" matrix. 

**More in the book about this**

## String Manipulation

Most text handling in python is made easy with the built in string object and functions.

### String Object Methods

Split a broken string

    In [92]: values = 'a,b,    guido'

    In [93]: values.split(',')
    Out[93]: ['a', 'b', '    guido']

It is often combined with `strip()` to trim whitespace and linebreaks

    In [96]: pieces = [x.strip() for x in values.split(',')]

    In [97]: pieces
    Out[97]: ['a', 'b', 'guido']

These values can be concatenated

    In [98]: first, second, third = pieces

    In [99]: first + '::' + second + '::' + third
    Out[99]: 'a::b::guido'

A more pythonic and faster way is using `str.join()`:

    In [101]: '::'.join(pieces)
    Out[101]: 'a::b::guido'

> This always feels like it is called in reverse

Detecting substring use `in`, but you can use `find` and `index`:

    In [104]: 'guido' in values
    Out[104]: True

    In [105]: values.index(',')
    Out[105]: 1

    In [108]: values.find(':')
    Out[108]: -1

> `index` raises an exception if the string isn't found. Found returns `-1`

Number of occurances of a string, use `count`:

    In [109]: values.count(',')
    Out[109]: 2

Substitution and removal of certain chars can use `str.replace()`

    In [110]: values.replace(',', '::')
    Out[110]: 'a::b::    guido'

Remove with an empty string:

    In [111]: values.replace(',', '')
    Out[111]: 'ab    guido'

## Regular Expressions

A way to search or match string patterns in text. Python's `re` module is responsible for applying regilar expressions to strings.

3 categories:
* pattern matching
* substitution
* splitting

Splitting a string by variable whitespace:

    In [112]: import re

    In [113]: text = 'Foo     Bar\t baz     \tqux'

    In [115]: re.split('\s+', text)
    Out[115]: ['Foo', 'Bar', 'baz', 'qux']

> Split with one or more white spaces

The regular expression is first compiled and then apploied to the text. It is much more efficient to compile a regular expression to create a reusable opbject with `re.compile()`

    In [117]: regex = re.compile('\s+')

    In [118]: regex.split(text)
    Out[118]: ['Foo', 'Bar', 'baz', 'qux']

If instead you want a list of all pattterns matching the regex:

    In [119]: regex.findall(text)
    Out[119]: ['     ', '\t ', '     \t']

> To avoid verbose escaping with the `\` character, it is better to use raw string literals eg. r'C:\x' isntead of 'C:\\x'

`match` and `search` are closely related to `findall`:

* `search` only returns the first match
* `match` only matches the beginning of a string

Lets consider a block of text with email addresses:

    In [120]: text = """Dave dave@google.com
        ...:         Steve steve@gmail.com
        ...:         Rob rob@gmail.com
        ...:         Ryan ryan@yahoo.com
        ...:         """

    In [121]: pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

    In [122]: regex = re.compile(pattern, flags=re.IGNORECASE)

    In [123]: regex.findall(text)
    Out[123]: ['dave@google.com', 'steve@gmail.com', 'rob@gmail.com', 'ryan@yahoo.com']

`re.IGNORECASE` makes the search case insensitive

`search` returns a special match objectfor the first email found. The match object only shows use the start and end characters.

    In [124]: m = regex.search(text)

    In [125]: m
    Out[125]: <_sre.SRE_Match object; span=(5, 20), match='dave@google.com'>

    In [126]: text[m.start():m.end()]
    Out[126]: 'dave@google.com'

`match` returns `None` as it will only match if the string starts with a match

`sub` will return a new string with matches replaced:

    In [127]: print(regex.sub('REDACTED', text))
    Dave REDACTED
            Steve REDACTED
            Rob REDACTED
            Ryan REDACTED

Suppose you want to group parts of the match, you should use parenthesis `()`:

    In [130]: pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

    In [131]: regex = re.compile(pattern, flags=re.IGNORECASE)

    In [132]: m = regex.match('abc@example.com')

    In [133]: m.groups()
    Out[133]: ('abc', 'example', 'com')

`findall` will return tuples:

    In [134]: regex.findall(text)
    Out[134]:
    [('dave', 'google', 'com'),
    ('steve', 'gmail', 'com'),
    ('rob', 'gmail', 'com'),
    ('ryan', 'yahoo', 'com')]

`sub` has access to special symbols `\1` and `'\2` which correspond to matched groups

    In [136]: regex.sub(r'Username: \1 Domain: \2 Suffix: \3', text)
    Out[136]: 'Dave Username: dave Domain: google Suffix: com\n        Steve Username: steve Domain: gmail Suffix: com\n        Rob Username: rob Domain: gmail Suffix: com\n        Ryan Username: ryan Domain: yahoo Suffix: com\n        '
You can also name matched groups using the notation:

    r'(?P<name>[A-Z]+)'

Example:

    In [139]: pattern = r'(?P<username>[A-Z0-9._%+-]+)@(?P<domain>[A-Z0-9.-]+)\.(?P<suffix>[A-Z]{2,4})'

    In [140]: regex = re.compile(pattern, flags=re.IGNORECASE|re.VERBOSE)

    In [141]: m = regex.match('abc@example.com')

    In [142]: m.groupdict()
    Out[142]: {'username': 'abc', 'domain': 'example', 'suffix': 'com'}

### Vectorised String Functions

    In [144]: data = {'Dave': 'dave@gmail.com', 'Pat': 'pat@yahoo.com', 'elaine': 'elaine@gmail.com', 'petri': np.NaN}

    In [145]: data = pd.Series(data)

    In [146]: data
    Out[146]:
    Dave        dave@gmail.com
    Pat          pat@yahoo.com
    elaine    elaine@gmail.com
    petri                  NaN
    dtype: object

    In [147]: data.isnull()
    Out[147]:
    Dave      False
    Pat       False
    elaine    False
    petri      True
    dtype: bool

You can use string functoins using `.str`:

    In [148]: data.str.upper()
    Out[148]:
    Dave        DAVE@GMAIL.COM
    Pat          PAT@YAHOO.COM
    elaine    ELAINE@GMAIL.COM
    petri                  NaN
    dtype: object

    In [149]: data.str.contains('gmail')
    Out[149]:
    Dave       True
    Pat       False
    elaine     True
    petri       NaN
    dtype: object

Regular expressions can be applied:

    In [150]: data.str.findall(pattern, flags=re.IGNORECASE)
    Out[150]:
    Dave        [(dave, gmail, com)]
    Pat          [(pat, yahoo, com)]
    elaine    [(elaine, gmail, com)]
    petri                        NaN
    dtype: object

Retrieval:

    In [151]: matches = data.str.match(pattern, flags=re.IGNORECASE)

    In [152]: matches
    Out[152]:
    Dave      True
    Pat       True
    elaine    True
    petri      NaN
    dtype: object

Not sure what this does:

    In [154]: matches.str.get(1)
    Out[154]:
    Dave     NaN
    Pat      NaN
    elaine   NaN
    petri    NaN
    dtype: float64

You can also slive strings:

    In [155]: data.str[:5]
    Out[155]:
    Dave      dave@
    Pat       pat@y
    elaine    elain
    petri       NaN
    dtype: object

# Chapter 8: Data Wrangling, Join, Combine and Reshape

In many applications data is spread across different files or databases and arranged in a form that is difficult to analyse.

## Hierachical Indexing

Allows you to have multiple index levels on an axis.

It allows you to work with higher dimension data in a lower dimension form.

    In [163]: data = pd.Series(np.random.randn(9), index = [['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd' ], [1, 2, 3, 1, 3, 1, 2, 2, 3]])

    In [164]: data
    Out[164]:
    a   1   -0.766229
        2    0.041728
    3    0.114579
    b   1   -0.726996
        3   -1.168821
    c   1    0.851205
        2   -0.131947
    d   2   -0.447351
        3    0.449313
    dtype: float64

This is a series with `MultiIndex` as its index.

    In [165]: data.index
    Out[165]:
    MultiIndex(levels=[['a', 'b', 'c', 'd'], [1, 2, 3]],
            labels=[[0, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 2, 0, 1, 1, 2]])

_Partial Indexing_ is possible to select subsets:

    In [166]: data['b']
    Out[166]:
    1   -0.726996
    3   -1.168821
    dtype: float64

    In [168]: data[['b', 'd']]
    Out[168]:
    b   1   -0.726996
        3   -1.168821
    d   2   -0.447351
        3    0.449313
    dtype: float64

    In [169]: data['b':'c']
    Out[169]:
    b   1   -0.726996
        3   -1.168821
    c   1    0.851205
        2   -0.131947
    dtype: float64

Select the second element in the inner level from each outer level:

    In [170]: data.loc[:, 2]
    Out[170]:
    a    0.041728
    c   -0.131947
    d   -0.447351
    dtype: float64

Hierachical indexing plays an important role in reshaping data and group-based operations like forming a _pivot_ table.

This data could be rearranged into a dataframe using the `unstack()` method:

    In [171]: data.unstack()
    Out[171]:
            1         2         3
    a -0.766229  0.041728  0.114579
    b -0.726996       NaN -1.168821
    c  0.851205 -0.131947       NaN
    d       NaN -0.447351  0.449313

The inverse operation is `stack()`:

    In [172]: data.unstack().stack()
    Out[172]:
    a   1   -0.766229
        2    0.041728
    3    0.114579
    b   1   -0.726996
        3   -1.168821
    c   1    0.851205
        2   -0.131947
    d   2   -0.447351
        3    0.449313
    dtype: float64

With a dataframe, each axis can have a hierachical index:

    In [173]: frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
        ...: index=[['a', 'a', 'b', 'b',],[1, 2, 1, 2]],
        ...: columns=[['Ohio', 'Ohio', 'Colarado'], ['Green', 'Red', 'Green']])

    In [174]: frame
    Out[174]:
        Ohio     Colarado
        Green Red    Green
    a 1     0   1        2
      2     3   4        5
    b 1     6   7        8
      2     9  10       11

Hierachical levels can have names. Don't confuse index names for axis labels:

In [176]: frame.index.names = ['key1', 'key2']

In [177]: frame.columns.names = ['state', 'colour']

    In [178]: frame
    Out[178]:
    state      Ohio     Colarado
    colour    Green Red    Green
    key1 key2
    a    1        0   1        2
         2        3   4        5
    b    1        6   7        8
         2        9  10       11

With partial indexing:

    In [179]: frame['Ohio']
    Out[179]:
    colour     Green  Red
    key1 key2
    a    1         0    1
         2         3    4
    b    1         6    7
         2         9   10

### Reorderng and Sorting Levels

`swaplevel` takes 2 level number or names and returns a new object with the levels interchanged.

    In [180]: frame.swaplevel('key1', 'key2')
    Out[180]:
    state      Ohio     Colarado
    colour    Green Red    Green
    key2 key1
    1    a        0   1        2
    2    a        3   4        5
    1    b        6   7        8
    2    b        9  10       11

`sort_index` can sort the values in a single level.

    In [181]: frame.sort_index(level=1)
    Out[181]:
    state      Ohio     Colarado
    colour    Green Red    Green
    key1 key2
    a    1        0   1        2
    b    1        6   7        8
    a    2        3   4        5
    b    2        9  10       11

Data selectino performance is much better on hierachically indexed objects if the index is alphabetically sorted starting from the outermost level. ie. the result of `sort_index()` or `sort_index(level=0)`

### Summary Statistics by Level

Many descricptive statistics have a `level` option to apply on a specific axis.

    In [183]: frame
    Out[183]:
    state      Ohio     Colarado
    colour    Green Red    Green
    key1 key2
    a    1        0   1        2
         2        3   4        5
    b    1        6   7        8
         2        9  10       11

    In [185]: frame.sum(level='key2')
    Out[185]:
    state   Ohio     Colarado
    colour Green Red    Green
    key2
    1          6   8       10
    2         12  14       16

    In [189]: frame.sum(level='colour', axis=1)
    Out[189]:
    colour     Green  Red
    key1 key2
    a    1         2    1
         2         8    4
    b    1        14    7
         2        20   10

> It uses `groupby`

### Indexing with dataframe's columns

    In [190]: frame = pd.DataFrame({'a': range(7), 'b': range(7, 0 , -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two',], 'd': [0, 1, 2, 0, 1,
        ...: 2, 3]})

    In [191]: frame
    Out[191]:
    a  b    c  d
    0  0  7  one  0
    1  1  6  one  1
    2  2  5  one  2
    3  3  4  two  0
    4  4  3  two  1
    5  5  2  two  2
    6  6  1  two  3

`set_index` will return a new dataframe that will use one or more of its columns as the inex:

    In [192]: frame2 = frame.set_index(['c', 'd'])
    In [193]: frame2
    Out[193]:
        a  b
    c   d
    one 0  0  7
        1  1  6
        2  2  5
    two 0  3  4
        1  4  3
        2  5  2
        3  6  1

By default the columns are removed from the dataframe, though you can leave them in:

    In [194]: frame.set_index(['c', 'd'], drop=False)
    Out[194]:
           a  b    c  d
    c   d
    one 0  0  7  one  0
        1  1  6  one  1
        2  2  5  one  2
    two 0  3  4  two  0
        1  4  3  two  1
        2  5  2  two  2
        3  6  1  two  3

To undo this hierachical indexing use `reset_index()`:

    In [196]: frame2.reset_index()
    Out[196]:
        c  d  a  b
    0  one  0  0  7
    1  one  1  1  6
    2  one  2  2  5
    3  two  0  3  4
    4  two  1  4  3
    5  two  2  5  2
    6  two  3  6  1

### Integer Indexes

There are subtle differences in integer indexing between python and numpy/pandas:

    In [197]: ser = pd.Series(np.arange(3.))
    In [198]: ser[-1]

gives an error:

    KeyError: -1

Whereas with a non-integer index, there is no potencial for ambiguity:

    In [200]: ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])

    In [201]: ser2
    Out[201]:
    a    0.0
    b    1.0
    c    2.0
    dtype: float64

    In [203]: ser2[-1]
    Out[203]: 2.0

With an axis containing integers, data indexing with always be label-oriented.
Use `loc` for label selection and `iloc` for integer selection

    In [204]: ser[:1]
    Out[204]:
    0    0.0
    dtype: float64

    In [205]: ser.iloc[:1]
    Out[205]:
    0    0.0
    dtype: float64

    In [206]: ser.loc[:1]
    Out[206]:
    0    0.0
    1    1.0
    dtype: float64

## Combining and Merging Datasets

The following ways:
* `pandas.merge` - connects rows based on keys, similar to a db `join`
* `pandas.concat` - concatenates or stacks objects together along an axis
* `combine_first` - instance method that enables splicing together ovverlapping data to fill in missing data in one obejct with values in another

### Database-style joins

    In [207]: df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})

    In [208]: df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

    In [209]: df1
    Out[209]:
        key  data1
    0   b      0
    1   b      1
    2   a      2
    3   c      3
    4   a      4
    5   a      5
    6   b      6

    In [210]: df2
    Out[210]:
        key  data2
    0   a      0
    1   b      1
    2   d      2

    In [211]: pd.merge(df1, df2)
    Out[211]:
        key  data1  data2
    0   b      0      1
    1   b      1      1
    2   b      6      1
    3   a      2      0
    4   a      4      0
    5   a      5      0

This is a _many-to-one_ join as `df2` only has single values for each `key`

If the column to join on is not specified `merge` uses the overlapping column names as keys.

It is good practice to to `explicit, not implicit` about what to join on:

    In [213]: pd.merge(df1, df2, on='key')
    Out[213]:
        key  data1  data2
    0   b      0      1
    1   b      1      1
    2   b      6      1
    3   a      2      0
    4   a      4      0
    5   a      5      0

If the colum names are different on each dataframe, you can specify them seperately:

    In [214]: df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})

    In [215]: df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})

    In [216]: pd.merge(df3, df4, left_on='lkey', right_on='rkey')
    Out[216]:
       lkey  data1 rkey  data2
    0    b      0    b      1
    1    b      1    b      1
    2    b      6    b      1
    3    a      2    a      0
    4    a      4    a      0
    5    a      5    a      0

> By default, merge does an `inner join` which results in an intersection or the common set in the tables.

Other options are `left`, `right` and `outer`. `outer` takes the union by applying both left and right joins:

    In [218]: pd.merge(df1, df2, how='outer')
    Out[218]:
       key  data1  data2
    0   b    0.0    1.0
    1   b    1.0    1.0
    2   b    6.0    1.0
    3   a    2.0    0.0
    4   a    4.0    0.0
    5   a    5.0    0.0
    6   c    3.0    NaN
    7   d    NaN    2.0

_many-to-many_ joins have well-defined but not intuitive behaviour:

    In [222]: df1
    Out[222]:
        key  data1
    0   b      0
    1   b      1
    2   a      2
    3   c      3
    4   a      4
    5   a      5
    6   b      6

    In [223]: df2
    Out[223]:
        key  data2
    0   a      0
    1   b      1
    2   a      2
    3   b      3
    4   d      4

    In [224]: pd.merge(df1, df2, on='key', how='left')
    Out[224]:
        key  data1  data2
    0    b      0    1.0
    1    b      0    3.0
    2    b      1    1.0
    3    b      1    3.0
    4    a      2    0.0
    5    a      2    2.0
    6    c      3    NaN
    7    a      4    0.0
    8    a      4    2.0
    9    a      5    0.0
    10   a      5    2.0
    11   b      6    1.0
    12   b      6    3.0

Many-to-many joins form a cartesian product of the rows. There were 3 b's in `df1` and 2 b's in `df2` therefore in the merged dataframe there are 6 b's.

    In [225]: pd.merge(df1, df2, how='inner')
    Out[225]:
       key  data1  data2
    0    b      0      1
    1    b      0      3
    2    b      1      1
    3    b      1      3
    4    b      6      1
    5    b      6      3
    6    a      2      0
    7    a      2      2
    8    a      4      0
    9    a      4      2
    10   a      5      0
    11   a      5      2

To join with multiple keys, pass a list of column names:

    In [226]: left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})

    In [227]: right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})
    In [229]: left

    Out[229]:
        key1 key2  lval
    0  foo  one     1
    1  foo  two     2
    2  bar  one     3

    In [230]: right
    Out[230]:
        key1 key2  rval
    0  foo  one     4
    1  foo  one     5
    2  bar  one     6
    3  bar  two     7

    In [228]: pd.merge(left, right, on=['key1', 'key2'], how='outer')
    Out[228]:
        key1 key2  lval  rval
    0  foo  one   1.0   4.0
    1  foo  one   1.0   5.0
    2  foo  two   2.0   NaN
    3  bar  one   3.0   6.0
    4  bar  two   NaN   7.0

> To determine which combination will appear in the results think of multiple keys as forming an array of tuples to be used as a single join key.

Overlapping column names can be addressed manually by renaming the axis labels. `merge` has a `suffix` option for specifying strings to append to overlapping key names:

    In [231]: pd.merge(left, right, on='key1')
    Out[231]:
        key1 key2_x  lval key2_y  rval
    0  foo    one     1    one     4
    1  foo    one     1    one     5
    2  foo    two     2    one     4
    3  foo    two     2    one     5
    4  bar    one     3    one     6
    5  bar    one     3    two     7

    In [232]: pd.merge(left, right, on='key1', suffixes=['_left', '_right'])
    Out[232]:
        key1 key2_left  lval key2_right  rval
    0  foo       one     1        one     4
    1  foo       one     1        one     5
    2  foo       two     2        one     4
    3  foo       two     2        one     5
    4  bar       one     3        one     6
    5  bar       one     3        two     7

## Merging on Index

Sometimes the merge keys are found in its index.
To indicate which index should be used as the merge key use `left_index=True` or `right_index=True` or both.

    In [233]: left1 = ({'key': ['a', 'b', 'a', 'b', 'c'], 'value': range(6)})

    In [245]: right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

    In [240]: left1
    Out[240]:
       key  value
    0   a      0
    1   b      1
    2   a      2
    3   a      3
    4   b      4
    5   c      5

    In [246]: right1
    Out[246]:
        group_val
    a        3.5
    b        7.0

    In [247]: pd.merge(left1, right1, left_on='key', right_index=True)
    Out[247]:
        key  value  group_val
    0   a      0        3.5
    2   a      2        3.5
    3   a      3        3.5
    1   b      1        7.0
    4   b      4        7.0

You can do the union instead of intersection:

    In [248]: pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
    Out[248]:
    key  value  group_val
    0   a      0        3.5
    2   a      2        3.5
    3   a      3        3.5
    1   b      1        7.0
    4   b      4        7.0
    5   c      5        NaN

Hierachically indexed data, things are more complicated as joining on index is innherantly a multiple key merge.

In this case you have to state the multiple keys to merge on. More in the book...

### Concatenating along an axis

Concatenating, binging or stacking

    In [249]: arr = np.arange(12).reshape((3, 4))
    In [256]: arr
    Out[256]:
    array([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])

    In [257]: np.concatenate([arr, arr], axis=1)
    Out[257]:
    array([[ 0,  1,  2,  3,  0,  1,  2,  3],
        [ 4,  5,  6,  7,  4,  5,  6,  7],
        [ 8,  9, 10, 11,  8,  9, 10, 11]])

In a dataframe context:
* Should we combine or use shared values on an index?
* Do concatenated chunks of data need to be identifiable in the resulting object?
* Does the concatenation axis contain data that needs to be preserved? In many cases the integer integer labels should be discarded.

The `concat` function in pandas provides a conistent way to do the above.

    In [258]: s1 = pd.Series([0, 1], index=['a', 'b'])

    In [259]: s2 = pd.Series([2, 3,4], index=['c', 'd', 'e'])

    In [260]: s3 = pd.Series([5, 6], index=['f', 'g'])

    In [263]: s1
    Out[263]:
    a    0
    b    1
    dtype: int64

    In [264]: s2
    Out[264]:
    c    2
    d    3
    e    4
    dtype: int64

    In [265]: s3
    Out[265]:
    f    5
    g    6
    dtype: int64

Concatenated:

    In [262]: pd.concat([s1, s2, s3])
    Out[262]:
    a    0
    b    1
    c    2
    d    3
    e    4
    f    5
    g    6
    dtype: int64

By default `concat` works along `axis=0`

If you pass `axis=1` the result is a `DataFrame`:

    In [266]: pd.concat([s1, s2, s3], axis=1)
    Out[266]:
        0    1    2
    a  0.0  NaN  NaN
    b  1.0  NaN  NaN
    c  NaN  2.0  NaN
    d  NaN  3.0  NaN
    e  NaN  4.0  NaN
    f  NaN  NaN  5.0
    g  NaN  NaN  6.0

You can intersect with `join=inner`

alot more detailed stuff in the bool...like `join_axes`

Also combing data with an overlap is explained

## Reshaping and Pivoting

### Reshaping with Hierachical Indexing

`stack` rotates or pivots from the columns in the data to rows

`unstack` pivots from rows to columns

    In [3]: data = pd.DataFrame(np.arange(6).reshape(2,3), index=pd.Index(['Ohio', 'Colarado']), columns=pd.Index(['one', 'two', 'three'], name='number'))

    In [4]: data
    Out[4]:
    number    one  two  three
    Ohio        0    1      2
    Colarado    3    4      5

`stack()` pivots the columns into rows, producing a series:

    In [5]: result = data.stack()

    In [6]: result
    Out[6]:
            number
    Ohio      one       0
            two       1
            three     2
    Colarado  one       3
            two       4
            three     5
    dtype: int64

You can rearrange the series back into a dataframe with `unstack()`:

    In [7]: result.unstack()
    Out[7]:
    number    one  two  three
    Ohio        0    1      2
    Colarado    3    4      5

By default the innermost level is unstacked, you can choose a different level by giving the name or number:

    In [8]: result.unstack(0)
    Out[8]:
            Ohio  Colarado
    number
    one        0         3
    two        1         4
    three      2         5

> Unstacking might give missing data

Stacking filters out missing data, you can stop that by passing `dropna=False`:

    data2.unstack().stack(dropna=False)

> The level unstacked becomes the lowest level in the result

### Pivoting Long to Wide Format

A comoon way of storing time series in a database and CSV is _long_ or _stacked_ format.

Lets load time series data and do some wrangling on it:

    In [4]: data = pd.read_csv('macrodata.csv')

    In [5]: periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='data')

    In [6]: data.head()
    Out[6]:
        year  quarter   realgdp  realcons  realinv  realgovt  realdpi    cpi     m1  tbilrate  unemp      pop  infl  realint
    0  1959.0      1.0  2710.349    1707.4  286.898   470.045   1886.9  28.98  139.7      2.82    5.8  177.146  0.00     0.00
    1  1959.0      2.0  2778.801    1733.7  310.859   481.301   1919.7  29.15  141.7      3.08    5.1  177.830  2.34     0.74
    2  1959.0      3.0  2775.488    1751.8  289.226   491.260   1916.4  29.35  140.5      3.82    5.3  178.657  2.74     1.09
    3  1959.0      4.0  2785.204    1753.7  299.356   484.052   1931.3  29.37  140.0      4.33    5.6  179.386  0.27     4.06
    4  1960.0      1.0  2847.699    1770.5  331.722   462.199   1955.5  29.54  139.6      3.50    5.2  180.007  2.31     1.19

    In [7]: data = pd.DataFrame(data.to_records(), columns=pd.Index(['realgdp', 'infl', 'unemp'], name='item'),
    ...: index=periods.to_timestamp('D', 'end'))

    In [8]: data.head()
    Out[8]:
    item         realgdp  infl  unemp
    data
    1959-03-31  2710.349  0.00    5.8
    1959-06-30  2778.801  2.34    5.1
    1959-09-30  2775.488  2.74    5.3
    1959-12-31  2785.204  0.27    5.6
    1960-03-31  2847.699  2.31    5.2

    In [9]: ldata = data.stack().reset_index().rename(columns={0: 'value'})

    In [10]: ldata.head()
    Out[10]:
            data     item     value
    0 1959-03-31  realgdp  2710.349
    1 1959-03-31     infl     0.000
    2 1959-03-31    unemp     5.800
    3 1959-06-30  realgdp  2778.801
    4 1959-06-30     infl     2.340

This is `long` format as it is time series with multiple keys.
Each row represents a single observation.

Data is frequently stored like this in MySQL db's.
In this case `date` (`data`) and `item` would be primary keys.

You may prefer a dataframe with one column per distinct date.
The `pivot` method does this:

    In [11]: pivoted = ldata.pivot('data', 'item', 'value')

    In [13]: pivoted.head()
    Out[13]:
    item        infl   realgdp  unemp
    data
    1959-03-31  0.00  2710.349    5.8
    1959-06-30  2.34  2778.801    5.1
    1959-09-30  2.74  2775.488    5.3
    1959-12-31  0.27  2785.204    5.6
    1960-03-31  2.31  2847.699    5.2

The first two arguments passed are the row and column index, then fianlly an optional value to fill the data.

More in the book omn pivoting mutliple keys with multiple values per keys - it will create a hierachical index.

# Chapter 9: Plotting and Visualisation

Informative visualisations (plots) is one of the most important tasks in data analysis.
It may be part of the exploratory process: identifying outliers, ideas for models and data transformations.

For others building interactive visualisations for the web may be the end goal.

Matplotlib is  desktop plotting package for creating two-dimensional publicationquality plots.

* `mplot3d` for 3d plots
* `basemap` for mappingand projections

The best way to follow along is with inline plotting in a jupyter notebook: `%matplotlib line`

## matplot API Primer

Import convention:

    from matplotlib.pyplot import plt

First plot:

    plt.plot(np.arange(10));

Libraries like seaborn and panda's built-in plotting functions deal with the mundane tasks of creating plots, it is important to learn a bit about the api.

### Figures and Subplots

Plots in `matplotlib` reside within a `Figure` object.

Check the [Chapter 9: Figures and Subplots Jupter Notebook Notes](https://fixes.co.za/notebooks/chp_9_plots.html), which I will attempt to host if possible.

# Chapter 10: Data Aggregation and Group Operations


Excerpt From: Unknown. “Python for Data Analysis, 2nd Edition.” iBooks. 

Source: [O'reilly Python for Data Analysis](http://shop.oreilly.com/product/0636920050896.do)