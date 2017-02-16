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
