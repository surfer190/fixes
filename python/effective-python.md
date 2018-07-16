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
* Done line by line espescially useful in a stream of reading from a file

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

The `None` arugment is espescially important for arguments that are mutable.
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

THere is one version of a concrete subclass that reads from a file on disk:

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

I have a set of classes with reaonable abstractions and interfaces, but they are only useful once the class is constructed. What is responsible for building the objects and orchestrating the map reduce?

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

This polymorphism extends to whole classes, not just their constructed objects.

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

> Similarly, I can make the create_workers helper part of the GenericWorker class. Here, I use the input_class parameter, which must be a subclass of GenericInputData, to generate the necessary inputs. I construct instances of the GenericWorker concrete subclass using cls() as a generic constructor.

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

Calling the parent class `__init__` mthod can ead to unpredictable behaviour espescially with multiple inheritance as the `__init__`.

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

### Use Descriptors for erusable @property methods

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


