# Python Basics

* Variables don't need to be declared before you can use them
* Everything is an object - everything has attributes and methods
* `def <function_name>():`
* Preferred variable name: `my_var`
* naming files: `hello_world.py`

### Style

* Blocks - code in function or loop - are indented extra one step (4 spaces)

### Python shell

Sometimes called REPL: Read Evaluate Print Loop

### Getting help

Use `help`:

        Objects

        >>> help(print)

        Methods

        >>> help(str.center)

### Errors

* `NameError` - variable with that name is not defined (couldn't be found). Also happens with functions.
* `TypeError` - doing something a particular type does not support eg. `5 + "Hello world"`
* `SyntaxError` - Python can't understand - most cryptic
* `ZeroDivisionError` - Can't divide by 0

## Variables

Can't contanin hyphen or start with a number

Eg. `favourite_nmber = 42`

Can explicitly delete a variable

Eg. `del favourite_number`

## Floats

When dividing a number `python 2` always returns a float egardless if answer is a whole number.
`Python 3` will return an `int` in that case

Don't use for banking / financials

### Rounding

`round(4.5) = 5,0`
`int(4.5) = 4`

can cast variables with `int()`, `float()`

### Order of operations

Can be controlled with parenthesis `()`. Eg. `(5 + 5) * 2`

### Take note

There are no `--` and `++` in python..here is the [explaination](http://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python)

There is however `**` which is `to the power of`

## Strings

Group of letter, numbers, spaces between two quote marks

Can use single or double quotes

Can escape special characters with a `\`

### Triple quotes

```
"""
        He's right
"""
```

Python holds onto new lines with triple quotes

Can also cast to string: `str(5)`

Can add strings with `+` and `+=`

But can't subtract strings and can't add different types together.
You **can multiple** but can't divide.

### Templates

Leaving holes in strings to fill in later

Create a placeholder with `{}`

`my_string = "I have {} puzzles"`

Set the value with: `print(my_string).format(10)`

## Lists

Similar to arrays

Can hold any type of item

You make a list with brackets: `[]`

`my_list = [1, 2, 3]

Can only concatenate lists with other lists

You can **multiply** lists

### operations

#### Append

`my_list.append(6)`

Only 1 at a time
If you append a list, you get a `2d` list

#### Extend

`my_list.extend(5,6,7)`

Add multiple items

`my_list.extend([8, 9])`

#### Remove

`my_list.remove(8)`

Can remove a list within

### Lists

Casting an int or float to a list: `list(5)` returns an error Not Iterable

But a string is iterable and you can do:

```
>>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```
#### Split

Breaks up a string (on whitespae by default)

```
>>> 'hello there students'.split()
['hello', 'there', 'students']
```

Can specify what to use as delimiter: `.split(':')`

#### Join

```
>>> flavours = ['choc','mint','strawberry']
>>> ', '.join(flavours)
'choc, mint, strawberry'
```

```
>>> "My favourite flavours are: " + ', '.join(flavours)
'My favourite flavours are: choc, mint, strawberry'
>>> "My favourite flavours are: {}".format(", ".join(flavours))
'My favourite flavours are: choc, mint, strawberry'
```

Strings and lists are **iterable**

`.index('a')` returns the first matching index

Get element at an index: `my_list[0]`

### Keywords

Python has reserved keywords not called as a function

`del var_name` - gets rid of variable
`del alpha_list[2]` - delete a specific entry (Can't delete from a string)

`is` - `c is d` - whether in same place in memory (best use is checking if variable is None)

`not` - flips the result

eg. `if not age > 3600`

`in` - check for containment / inclusion

eg. `"cheese" in "cheeseshop"`

Can use multiple: `if x not in y`

`break` - lets us end a loop early

`continue` - lets you skip the rest of the iteration

`def`

`return` return a value to whatever called a function

`try` - block element

`import`

### Booleans

`bool(var)` - check Booleans

python has a keyword `None` meaning empty

#### Comparison

`==` / `!=` - equality
`>` / `<` - greater than or less than

#### Conditions

`if`, `else`, `elif`

#### Loops

`for` loop - do an action a certain number of times
`while` loop - runs an unknown number of times

Is a block so requires `:` at the Append

Eg. `for word in my_list:`

```
while start:
    print(start)
    start -= 1
```

### Getting user input

Use `input("Question?")`

```
age = input("What is your age? ")
```

It is a string though, must cast

### Functions

function name = same as variable name with parentheses:

```
def hows_the_parent():
    print("He's pining for the fjords!")
```

Call a function: `hows_the_parent()`

#### Argument

```
def lumberjack(name):
    print name;
```

### Handling Exceptions

`try`...`except`...`else`

```
try:
    count = int(input("Give me a number: "))
except ValueError:
    print("That's not a number")
else:
    print("Hi " * 5)
```

### Using the standard library

Use `import` keyword

`import <library_name>`