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






Source: [O'reilly Python for Data Analysis](http://shop.oreilly.com/product/0636920050896.do)