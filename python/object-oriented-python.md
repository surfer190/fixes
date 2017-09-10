## Object Oriented Programming with Python

In python, __everything is an object__. Even functions are function objects.

The keyword `class` is used to define eventual objects

Classes have `attributes`, which are similar to variables but are defined inside a class and belong to that class.

Classes have `methods` to give them abilities

When we use a class, the resulting object is an `instance`. 

### Example

        class NewClass:
            name_attribute = "Kenneth"

            def name_method(self):
                return self.name

        new_instance = NewClass()
        new_instance.name_method()

* By convention classes always start with a **capital letter**
* If they have multiple words in, then each first  letter is capitalised

### Most basic class

    class Thief:
        pass

    >>> from characters import Thief
    >>> surfer190 = Thief()
    >>> surfer190
    <characters.Thief object at 0x101cbe278>

It is like running a function but classes don't run. It creates an instance of the class.

### Attributes

    class Thief:
        sneaky = True

Access the class member with `.` syntax

    >>> surfer190.sneaky
    True

You can also get the classes member with

    >> Thief.sneaky
    True

But instances are responsible for their own attribute values

    >>> surfer190.sneaky = False
    >>> surfer190.sneaky
    False

Delete an instance of a class (object)

    >>> del surfer190

### Methods

Methods are functions that belong to a class

#### Self

Whenever they are used, they are used by an instance. Not the actual class.
That is why `methods` always take at least one parameter that is the instance using the method
By convention that parameter is always called `self`

If you call the class method diretly you get an error unless you give it the instance:

        >>> from characters import Thief
        >>> surfer = Thief()
        >>> surfer.pickpocket()
        Called by <characters.Thief object at 0x101bbe2e8>
        False
        >>> Thief.pickpocket()
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: pickpocket() missing 1 required positional argument: 'self'
        >>> Thief.pickpocket(surfer)
        Called by <characters.Thief object at 0x101bbe2e8>
        True

Another thing is you can always refer to `self` in the method:

        import random

        class Thief:
            sneaky = True

            def pickpocket(self):
                print("Called by {}".format(self))
                return bool(random.randint(0, 1))

## Init

When you create a new method python looks for a method called `def __init__`

Dunders indicate that it is a method python will run on it's own. We need not run it ourselves.

        def __init__(self, name, sneaky=True, **kwargs):
            self.name = name
            self.sneaky = sneaky

            for key, value in kwargs.items():
                # Very useful function
                setattr(self, key, value)

when you initialise you will be required to provide a `name` parameter

`**kwargs` is a dictionary of key-value pairs

## Class attributes

Attributes set on the class are universal and can be changed just by specifying in `.` notation

        redcar.laps = 0

To prevent this you have to set the number of laps attribute in `__init__`

## Inheritance

You can inherit attributes and methods from a parent class by adding that class in the definition

    class Thief(Character):
        ...

**Note: Every class in python inherits from the built-in class called `object`**

In python 2 you had to do this manually but python3 improved this to automatically inherit

## Using the Super Class

We can use methods on demand from the super class from the child class with `super()`

Usually done of overridden classes. So redefine the method and call `super()`

When using `super()` Must include the method name and required arguments too.

Sub classes can take different arguments from their parent classes

        class Character:
            def __init__(self, name, **kwargs):
                self.name = name

                for key, value in kwargs.items():
                    setattr(self, key, value)


        class Thief(Character):
            sneaky = True

            def __init__(self, name, sneaky=True, **kwargs):
                '''
                Super must be called first as sneaky could be defined in key word arguments
                '''
                super().__init__(name, **kwargs)
                self.sneaky = sneaky

### Refactoring

Tech jargon for rearranging code nto a more logical state, by deleting, renaming, comibing and breaking code up.

## Inferiting from multiple classes (Multiple Inheritance)

You can inherit from multiple classes with an `inheritance chain`.
The order that you inherit from classes is important because of `super()`

The MRO - Method Resolution Order

You can use `class.__mro__` or `inspect.getmro()` to look at your class's method resolution order (MRO)

Tightly coupled code / design means that classes have to know a lot about other classes.
Makes it harder to add in new functionality.

Loosely coupled code is the way to go, so it becomes easier to mix and match. 

## Useful functions

`isinstance('abc', str)` - Tells you whether something is an instance of a particular class

        >>> isinstance(5.22, (int, str))
        False
        >>> isinstance(5.22, (int, float))
        True

You can use a `tuple` to check against

### Easter Egg

        >>> isinstance(True, int)
        True
        >>> isinstance(True, bool)
        True

`issubclass(bool, int)` - Tells you whether a class is an instance of another class

        >>> issubclass(Thief, Character)
        True
        >>> issubclass(bool ,int)
        True

`type('stephen')` - Tells you the type of object an instance is

Better to use `isinstance` as it will check the full inheritance tree

There are a lot of dunder attributes `__attribute__`

* `myvar.__class__` - tells you the class of an instance

Can even get the class name:

        >>> stephen = Thief('stephen')
        >>> stephen.__class__
        <class 'characters.Thief'>
        >>> stephen.__class__.__name__
        'Thief'

Python leans towards ducktyping where if a class looks and quacks like a duck it should be considered a duck. It is still handy to tell if instance of class is expected.

Another good one is `dir(my_var)` which shows you available methods

## Magic Methods

Methods that python calls for you. We have seen `__init__` already.

`__str__`: Returns a string to identify object whenever it is turned into a string

`__repr__`: Return official string representation, used for debugging, as much info as possible

`__int__` / `__float__`: Return integer and float representations

        >>> five = NumString(5)
        >>> five
        <numstring.NumString object at 0x101bbe278>
        >>> str(five)
        '5'
        >>> int(five)
        5
        >>> float(five)
        5.0

`__add__`: Addition Math operation, from the left hand side

`__radd__`: Reflective addition, addition from the right hand side

`__iadd__`: which is `+=` (`i` stands for `in place` )

You can check the full list in [Emulating numeric types docs](https://docs.python.org/3/reference/datamodel.html?#object.__mul__)

        class NumString:
            def __init__(self, value):
                self.value = str(value)

            def __str__(self):
                return self.value

            def __int__(self):
                return int(self.value)

            def __float__(self):
                return float(self.value)

            def __add__(self, other):
                return self.value + str(other)

            def __radd__(self, other):
                return self + other

            def __iadd__(self, other):
                self.value = self + other
                return self.value

The `len(my_obj)` is implemented with `__len__`

To check if `item in my_obj` you use `__contains__`

If `__contains__` does not exist, python uses `__iter__` or `__getitem__`

        def __iter__(self):
            for item in self.slots:
                yield item

## Making an iterable

What is `yield`? It is very similar to `return` but it does not immediately stop execution like `return` does

`yield` lets you send items out of the method as they are available and keep on working

This construct is called a `generator`

We can simplify above to:

            def __iter__(self):
                yield from self.slots

Because `self.slots` is a list, python knows how to iterate through it.

When you use these default built-in methods with your custom class, it makes them easier to use and more what you are used to.

## Custom verisions of built-ins

When building custom classes you will usually make use of `built-in` classes of your language.
The two most important of which are `__init__` and `__new__`

`__new__` - is for customising an `immutable` data type

`immutable` means the only time you should change them is at `creation` time

**Unlike `init`, `new` does a return**

**New does not take `self`, as it is a special method that operates on a `class`, not an instance**

With immutable types, it can be unsafe to use `super()` inside of `__new__`, it is better to use parent method directly eg:

        self = str.__new__(*args, **kwargs)

Take this code:

        for _ in range(count): 
            ....

The `_` implies that you don't care what that value is

And if you use `copy.copy()` you are not using references, but copy by reference

## Mimicking dot notation

        class javascriptObject(dict):
            def __getattribute__(self, item):
                try:
                    return self[item]
                except KeyError:
                    return super().__getattribute__(item)


## Another immutable example

        class Double(int):
            def __new__(value, *args, **kwargs):
                self = int.__new__(value, *args, **kwargs)
                self *= 2
                return self

# Class Methods

* Construct an instance of your class without having to have a class instance already
* They often work as a `factory` for an object
* Don't take `self` as their first argument, they take the `class` but that is a reserved keyword so `cls` is used (sometimes `klass` is used)
* `cls(books)` is basically calling the constructor `__init__`
* `@classmethod` is a decorator - a function that takes another function, does something with it then returns it


        class Book:
            def __init__(self, title, author):
                self.title = title
                self.author = author

            def __str__(self):
                return '{} by {}'.format(self.title, self.author)


        class BookCase:
            def __init__(self, books=None):
                self.books = books

            @classmethod
            def create_bookcase(cls, book_list):
                books = []
                for title, author in book_list:
                    books.append(Book(title, author))
                return cls(books)

**Remember with classmethod you don't call init, you just cal cls()**

Usage:

        >>> bc = BookCase.create_bookcase([('Moby-Dick', 'Melville'), ('Jungle Book', 'Rudyard Kipling')])
        >>> bc
        <books.BookCase object at 0x1024bd470>
        >>> bc.books
        [<books.Book object at 0x1024bd5f8>, <books.Book object at 0x1024bd630>]
        >>> str(bc.books[0])
        'Moby-Dick by Melville'

## Static Methods

Static methods don't require an instance or a class at all

## Encapsulation (Hising elements of class away)

Python motto: "We're all adults here"

Just prepend the name of method or attribute with an underscore `_`

Double underscore `__` makes method or underscore inaccessible outside of the class (`private`)

So `python` does **name mangling** on the attribute and methods

But you can find them by checking `dir(obj)`

### Example

        class Protected:
            __name = "Security"

            def __method(self):
                return self.__name

        >>> from protected import Protected
        >>> prot = Protected()
        >>> prot.__name
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: 'Protected' object has no attribute '__name'
        >>> prot.__method
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: 'Protected' object has no attribute '__method'
        >>> dir(prot)
        ['_Protected__method', '_Protected__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
        >>> prot._Protected__method
        <bound method Protected.__method of <protected.Protected object at 0x1024bd668>>
        >>> prot._Protected__method()
        'Security'
        >>> prot._Protected__name
        'Security'

So in python nothing is truly ever **locked** away

## Property decorator

If you don't want people to know it is a method, you can use the `@property` decorator

        class Circle:
            def __init__(self, diameter):
                self.diameter = diameter

            @property
            def radius(self):
                return self.diameter / 2

So properties act as attributes

        small = Circle(10)
        print(small.radius)

But they cannot be set, as python does not know how to set it

        small.radius = 15

But there is a way to create a setter
Use a decorator of the form `@<property_name>.setter`. Then use the same property method but take in another parameter

        class Circle:
            def __init__(self, diameter):
                self.diameter = diameter

            @property
            def radius(self):
                return self.diameter / 2

            @radius.setter
            def radius(self, radius):
                self.diameter = radius * 2

### Implement Equality and Add

        class Die:
            def __init__(self, sides=2, value=0):
                if not sides >= 2:
                    raise ValueError("Must have at least 2 sides")

                if not isinstance(sides, int):
                    raise ValueError("Sides must be a whole number")

                self.value = value or random.randint(1, sides)

            def __int__(self):
                return self.value

            def __eq__(self, other):
                return int(self) == other

            def __ne__(self, other):
                return not int(self) == other

            def __gt__(self, other):
                return int(self) > other

            def __lt__(self, other):
                return int(self) < other

            def __ge__(self, other):
                return int(self) > other or int(self) == other

            def __le__(self, other):
                return int(self) < other or int(self) == other

            def __add__(self, other):
                return int(self) + other

            def __radd__(self, other):
                return int(self) + other

#### Usage

        >>> d6 = D6()
        >>> d6.value
        1
        >>> d6 < 3
        True
        >>> d6 <= 1
        True
        >>> d6 <= 2
        True
        >>> d6 >= 2
        False
        >>> d6 >= 1
        True
        >>> d6 != 4
        True
        >>> d6 == 6
        False
        >>> d6 == 1
        True

If you need to implement all of the methods try using the [attrs library](https://attrs.readthedocs.io/en/stable/)

Or if you just need equality and math ones then use the built-in [functools.total_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering)

#### Interesting

You can pass around a class Just like you would an integer or string

Just don't call or initialise the class with `()` when passing it, unless you want result to be sent in