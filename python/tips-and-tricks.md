# Find Out what Attributes an Object has

```
dir(object)
```

# Find out the Type of Obejct

```
type(object)
```

# Clear the python terminal screen

```
ctrl + l
```

# Merge 2 dicts 

Must be Python3.5+ and will give preference to 2nd dict

        >>> x = {'a': 1, 'b': 2}
        >>> y = {'b': 3, 'c': 4}
        >>> z = {**x, **y}
        >>> z
        {'a': 1, 'b': 3, 'c': 4}

# Testing Multiple flags

        x, y, z = 0, 1, 0

        if x == 1 or y == 1 or z == 1:
            print('passed')

        if 1 in (x, y, z):
            print('passed')

        if x or y or z:
            print('passed')

        if any((x, y, z)):
            print('passed')

# A dicts get() method has a default argument

        >>> names = {1: "surfer", 2: "joe sloan", 3: "tam lovelace"}
        >>> f'Hi, {names.get(1)}'
        'Hi, surfer'
        >>> f'Hi, {names.get(4, "there!")}'
        'Hi, there!'

# Named tuples instead of a class

        >>> Car = namedtuple('Car', 'colour mileage')
        >>> my_gti = Car('red', 126713.2)
        >>> my_gti
        Car(colour='red', mileage=126713.2)
        >>> type(my_gti)
        <class '__main__.Car'>
        >>> my_gti.colour
        'red'

Remember `namedtuple` is immutable, like a normal `tuple`

        >>> my_gti.colour = 'blue'
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: can't set attribute

# Prett print JSON

        >>> gti = {'rims': 18, 'top_speed':235, 'power':147}
        >>> import json
        >>> print(json.dumps(gti, indent=4, sort_keys=True))
        {
            "power": 147,
            "rims": 18,
            "top_speed": 235
        }

# Function argument unpacking

        def myfunc(x, y, z):
            print(x, y, z)

        tuple_vec = (1, 0, 1)
        dict_vec = {'x': 1, 'y': 0, 'z': 1}

Remember `*` means treat this as an iterable 

        >>> myfunc(*tuple_vec)
        1, 0, 1

Remember `**` means treat this as a `dict`

        >>> myfunc(**dict_vec)
        1, 0, 1

# In-place variable swapping

No need for a temporary variable

        >>> a = 45
        >>> b = 10
        >>> a, b = b, a
        >>> b
        45
        >>> a
        10

# Is vs "=="

* "is" expressions evaluate to True if two 
* "==" evaluates to True if the objects 

        >>> opp = [1, 2, 3]
        >>> rod = [1, 2, 3]
        >>> opp == rod
        True
        >>> opp is rod
        False
        >>> rod = opp
        >>> opp is rod
        True

# Function are first-class citizens

They can be passed as arguments, returned as values and assigned to variables and stored in data structures

        >>> def myfunc(a, b):
        ...     return a + b
        ...
        >>> funcs = [myfunc]
        >>> funcs[0]
        <function myfunc at 0x107012230>
        >>> funcs[0](2, 3)
        5

## Dicts can be used as a switch statement

A lambda is just an unnamed function

        def dispatch_dict(operator, x, y):
            return {
                'add': lambda: x + y,
                'sub': lambda: x - y,
                'mul': lambda: x * y,
                'div': lambda: x / y,
            }.get(operator, lambda: None)()

## List comprehension


        vals = [expression 
                for value in collection 
                if condition]

Equivalent to:

        vals = []
        for value in collection:
            if condition:
                vals.append(expression)

Example:

        >>> vals = list(range(1, 11))
        >>> vals
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> evens = [x for x in vals if x % 2 == 0]
        >>> evens
        [2, 4, 6, 8, 10]

## Delete all items from alist

        >>> lst = list(range(0, 6))
        >>> lst
        [0, 1, 2, 3, 4, 5]
        >>> del lst[:]
        >>> lst
        []

### Source

[Dan Bader Python Tips](https://dbader.org/)