# Numpy

The core tool for performant numerical computing with Python

### Numpy arrays

* multi-demensional arrays
* closed to hardware - faster
* designed for scientific computation

        import numpy as np
        ar = np.array([1,2,3,4])
        ar
        array([0, 1, 2, 3])

### Testing the speed difference

We will use ipthyons `%timeit`

Normal python array

        In [12]: L = range(1000)

        In [13]: %timeit [i**2 for i in L]
        414 µs ± 8.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

Numpy array

In numpy mathematical operations are automatically operated on each element of array

        In [14]: L = np.arange(1000)

        In [16]: %timeit L**2
        1.57 µs ± 71.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

### Getting help

[Numpy Docs](https://docs.scipy.org/doc/numpy-1.13.0/reference/)


    np.array?

    In [3]: np.lookfor('create array')
    Search results for 'create array'
    ---------------------------------
    numpy.array
        Create an array.
    numpy.memmap
        Create a memory-map to an array stored in a *binary* file on disk.
    
## Import convention

When importing numpy use

    import numpy as np

## Creating Arrays

### 1D

Creating

        >>> a = np.array([0,1,2,3])
        >>> a
        array([0, 1, 2, 3])

Checking number of dimensions

        >>> a.ndim
        1

Checking number of deimensions

        >>> a.shape
        (4,)
        >>> len(a)
        4
    
### 2D

Create it with an array/list oflists

        >>> b = np.array([[1,2,3,4], [5,6,7,8]])
        >>> b
        array([[1, 2, 3, 4],
            [5, 6, 7, 8]])

Checking number of dimensions

        >>> b.ndim
        2

Return a tuple of the shapeof an array

        >>> b.shape
        (2, 4)

Check number of objects in first dinmesion

        >>> len(b)
        2

### Evenly spaced

Use `np.arange(x)`

    arange([start,] stop[, step,], dtype=None)

    >>> a = np.arange(100000)
    >>> a
    array([    0,     1,     2, ..., 99997, 99998, 99999])

### Number of points within a range

    linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

    a = np.linspace(0, 1, 100)
    array([ 0.        ,  0.01010101,  0.02020202,  0.03030303,  0.04040404, ...

### Common arrays

**np.ones**

    ones(shape, dtype=None, order='C')
    Return a new array of given shape and type, filled with ones.

**np.zeros**

    zeros(shape, dtype=float, order='C')
    Return a new array of given shape and type, filled with zeros.

**np.eye**

    eye(N, M=None, k=0, dtype=<class 'float'>)
    Return a 2-D array with ones on the diagonal and zeros elsewhere.

**np.diag**

    diag(v, k=0)
    Extract a diagonal or construct a diagonal array.

    >>> d = np.diag(np.array([1, 2, 3, 4]))
        >>> d
        array([[1, 0, 0, 0],
               [0, 2, 0, 0],
               [0, 0, 3, 0],
               [0, 0, 0, 4]])

**np.random**

        >>> a = np.random.rand(4)
        >>> a
        array([ 0.14365585,  0.96317038,  0.57808752,  0.30486506])

**Gaussian random numbers**

Numbers on a "standard normal" distribution of mean 0 and variance 1

        >>> a = np.random.randn(4)
        >>> a
        array([-0.72186413,  1.89644724, -1.63709681, -0.76200216])

## Basic data types

Numbers sometimes displayed with a trailing `.`: `2.`

    >>> a = np.array([1.,2.,3.,])
    >>> a
    array([ 1.,  2.,  3.])
    >>> a.dtype
    dtype('float64')

No `.` is `int64` with a dot is `float64`

You can explicitly specify the datatype with:

    c = np.array([1, 2, 3], dtype=float)

There is also:

**complex128**:

    d = np.array([1+2j, 3+4j, 5+6*1j])

**String**:

    >>> a = np.array(['hello','is','it','me','you','are','looking','for'])
    >>> a.dtype
    dtype('<U7')

### Indexing and Slicing

You access items the same as python lists

    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> a[0], a[2], a[9]
    (0, 2, 9)

Reversing a numpy array

    >>> a[::-1]
    array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

For multi-dimensional arrays indexes are tuples of intergers
The Row is specified first and column second

    >>> a[2,1]
    # third row, second column

Arrays can be sliced (Just like python)

    >>> a[12:20:2] # [start:end:step]
    array([22, 24, 26, 28])

No slice components are requered, default is `0:last:1`

    >>> a[:]

**Remember that the end/last element is not included

    >>> a = np.array([1,2,3,4])
    >>> a[1:3]
    array([2, 3])
    >>> a[1:4]
    array([2, 3, 4])

Now the differences is you can assign slices to numpy arrays but not python lists

    >>> a[2:] = 10
    >>> a
    array([ 1,  2, 10, 10])

Slicing a 2-d array:

a[<slicing of row>, <slicing of column>]

Example:

    >>> a = np.diag(np.arange(1,7, dtype='float'))
    >>> a
    array([[ 1.,  0.,  0.,  0.,  0.,  0.],
            [ 0.,  2.,  0.,  0.,  0.,  0.],
            [ 0.,  0.,  3.,  0.,  0.,  0.],
            [ 0.,  0.,  0.,  4.,  0.,  0.],
            [ 0.,  0.,  0.,  0.,  5.,  0.],
            [ 0.,  0.,  0.,  0.,  0.,  6.]])

And you want the entire rows of 3 to 5 diagonally: 
* y: starting at 2 ending at 4 inclusive (5) = `2:5`
* x: starting at 0 and ending at index 4 inclusive (5) = `0:5`

It is wierd as you start with the `y-axis` in the notation

        >>> a[2:5,:5]
        array([[ 0.,  0.,  3.,  0.,  0.],
               [ 0.,  0.,  0.,  4.,  0.],
               [ 0.,  0.,  0.,  0.,  5.]])

## Copies and Views

The slicing operation creates a view on the original array which is just a way of accessing array data. The original array is not copied.

You can use `np.may_share_memory(x, y)` to check if 2 arrays share memory

If memory is shared changing the copied or original affect the other.

To force a copy use:

    >>> c = a[:2].copy()

## Fancy Indexing

Using boolean masks

    >>> a = np.random.randint(0, 21, 15)
    >>> a
    array([10,  3,  8,  0, 19, 10, 11,  9, 10,  6,  0, 20, 12,  7, 14])
    >>> (a % 3 == 0)
    array([False,  True, False,  True, False, False, False,  True, False,
            True,  True, False,  True, False, False], dtype=bool)
    >>> mask = (a % 3 == 0)
    >>> extract_from_a = a[mask]
    >>> extract_from_a
    array([ 3,  0,  9,  6,  0, 12])

Assigning new values to sub array that meets a criterion:

    a[a % 3 == 0] = -1

Using integer array mask (repeating some values):

    >>> a = np.arange(0, 100, 10)
    >>> a
    array([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
    >>> a[[1,2,2,3,3,4,4]]
    array([10, 20, 20, 30, 30, 40, 40])

Can be used to assign as well:

    >>> a[[7,9]] = 100

A new array created by an array of arrays will share the same shape

    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> idx = np.array([[3,4],[9,7]])
    >>> idx
    array([[3, 4],
        [9, 7]])
    >>> a[idx]
    array([[3, 4],
        [9, 7]])


**Remember for an element `a[5,6]` the x-axis is `6` and the y-axis is `5`

### Indexing 

An iteratable can be used `tuple` works the same as a `list`:

    full[[0,1,2,3,4], [1,2,3,4,5]]
    full[(0,1,2,3,4), (1,2,3,4,5)]

You can use standard list manipulation notation:

    full[(3:, [0,2,5]]

## Numerical operations on arrays

### With Scalars

scalars are single element or number fields

You can simply apply the arithmetic to the whole array

    >>> a = np.array([1, 2, 3, 4])
    >>> a + 1
    array([2, 3, 4, 5])

Lets try `a` to the power of `2`

    >>> a**2
    array([ 1,  4,  9, 16])

**All arithmetic operates element-wise**

    >>> b = np.ones(4) + 1
    >>> b
    array([ 2.,  2.,  2.,  2.])
    >>> a - b
    array([-1.,  0.,  1.,  2.])

Another example:

    >>> j = np.arange(5)
    >>> j
    array([0, 1, 2, 3, 4])
    >>> 2**(j + 1) - j
    array([ 2,  3,  6, 13, 28])

__The operations are much faster than if you did them in pure python__

### Matrix Multiplcation

In [6]: c = np.ones((3, 3))

In [7]: c
Out[7]:
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])

**Using `*` is not matrix multiplication**

In [8]: c * c
Out[8]:
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])

**Using the `dot` function is matrix multiplciation**

`dot` is the product of 2 arrays

In [9]: c.dot(c)
Out[9]:
array([[ 3.,  3.,  3.],
       [ 3.,  3.,  3.],
       [ 3.,  3.,  3.]])

### Comparison is also element-wise

        In [20]: a = np.array([1, 2, 3, 4])

        In [21]: b = np.array([4, 2, 2, 4])

        In [22]: a == b
        Out[22]: array([False,  True, False,  True], dtype=bool)

        In [23]: a > b
        Out[23]: array([False, False,  True, False], dtype=bool)

If you want to compare the entire array use `np.array_equal()`:

        a = np.array([1, 2, 3, 4])
        b = np.array([1, 2, 3, 4])
        np.array_equal(a, b)

### Logic operations

Use `np.logical_or()` and `np.logical_and()`

    >>> a = np.array([1, 1, 0, 0], dtype=bool)
    >>> b = np.array([0, 1, 1, 0], dtype=bool)
    >>> np.logical_or(a, b)
    array([ True,  True,  True, False], dtype=bool)
    >>> np.logical_and(a, b)
    array([False,  True, False, False], dtype=bool)

### Transcendental operations

Use `np.sin`, `np.cos`, `np.tan`, `np.log` and `np.exp`

        >>> a = np.array([-1, 0, 1, 2])
        >>> a
        array([-1,  0,  1,  2])
        >>> np.sin(a)
        array([-0.84147098,  0.        ,  0.84147098,  0.90929743])
        >>> np.log(a)
        __main__:1: RuntimeWarning: divide by zero encountered in log
        __main__:1: RuntimeWarning: invalid value encountered in log
        array([        nan,        -inf,  0.        ,  0.69314718])
        >>> np.exp(a)
        array([ 0.36787944,  1.        ,  2.71828183,  7.3890561 ])

### Mimatch

    >>> a = np.arange(4)
    >>> a + np.array([1, 2])
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: operands could not be broadcast together with shapes (4,) (2,)

When the shapes of the arrays do not match they cannot be **broadcast**

### Transpose

Invert and reflect. Opposite on both axis.

Create a triangle with `np.triu` (Use `help(np.triu)`)

    >>> np.triu(np.ones((3,3)),1)
    array([[ 0.,  1.,  1.],
        [ 0.,  0.,  1.],
        [ 0.,  0.,  0.]])

then transpose with:

    >>> a.T
    array([[ 0.,  0.,  0.],
        [ 1.,  0.,  0.],
        [ 1.,  1.,  0.]])

**Remember a transposition is a view, so when arrays become larger they will fail in unpredicatable ways**

### Extras

* `np.allclose` - Returns True if two arrays are element-wise equal within a tolerance.
* `np.tril`- Lower triangle of an array.

## Basic Reductions

### Finding the sum of an array

    >>> a
    array([ 0,  5, 10, 15, 20, 25])
    >>> a.sum()
    75
    >>> np.sum(a)
    75

On the `axis`:

    >>> a = np.array([[1,1], [2,2]])
    >>> a
    array([[1, 1],
        [2, 2]])

Find sum of the `column` along the `y-axis` - `first dimension`

    >>> a.sum(axis=0)
    array([3, 3])

Find the sum of `column` along the `x-axis` - `second dimension`:

    >>> a.sum(axis=1)
    array([2, 4])

Same idea at higher dimensions:

    >>> x = np.random.rand(2, 2, 2)
    >>> x
    array([[[ 0.73091254,  0.3126328 ],
            [ 0.52196148,  0.51212003]],

        [[ 0.07157999,  0.15920737],
            [ 0.75733851,  0.99707551]]])
    >>> x.sum(axis=2)[0, 1]
    1.0340815143357149

`min`, `max` and index of min and max

    x = np.array([1, 3, 2])
    >>> x.min()
    1
    >>> x.max()
    3

Get the index of the min or max:


    >>> x.argmin()
    0
    >>> x.argmax()
    1

### Logic operations

    >>> np.all([True, True, False])
    False
    >>> np.any([True, True, False])
    True

Can be used with an argument:

    >>> a = np.array([1, 2, 3, 2])
    >>> b = np.array([2, 2, 3, 2])
    >>> np.all(a < 4)
    True
    >>> np.any(a > 4)
    False
    >>> np.any(a > 3)
    False
    >>> np.any(a > 2)
    True

With multiple conditions:

    >>> a = np.array([1, 2, 3, 2])
    >>> b = np.array([2, 2, 3, 2])
    >>> c = np.array([6, 4, 4, 5])
    >>> ((a <= b) & (b <= c))
    array([ True,  True,  True,  True], dtype=bool)
    >>> ((a <= b) & (b <= c)).all()
    True

### Statistics

>>> y = np.array([[1, 2, 3], [5, 6, 1]])

The average or `mean`:

    >>> y.mean()
    3.0

The median along the `-1` last axis

    >>> np.median(y, axis=-1)
    array([ 2.,  5.])

The standard devication

    >>> x.std()
    0.81649658092772603

cumsum is the cumulative sum

    >>> y.cumsum(axis=0)
    array([[1, 2, 3],
        [6, 8, 4]])
    >>> y.cumsum(axis=1)
    array([[ 1,  3,  6],
        [ 5, 11, 12]])
    >>> y
    array([[1, 2, 3],
        [5, 6, 1]])

**Remember in ipython you can run bash commands with `!` in front**

Eg. `!cat data/populations.txt`

