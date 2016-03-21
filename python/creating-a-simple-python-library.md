# Creating a Simple Library

To create a simple python library that you can `import` into another python file create the file
Create a new file and `define` a function, give this function a comment as to what is Does

**textutils_pack.py**

def split_words(paragraph):
  """This function splits a sentence by spaces

  returns a list of words"""
  words = paragraph.split(' ')
  return words

# Using the Library

Now you can `import` the library

  import textutils_pack

  sentence = "And on that day, no a single damn was given."
  words = textutils_pack.split_words(sentence)

You can also call the function without referencing the library:

  from textutils_pack import *

  words = split_words(sentence)

## Other Cool things

Open the Python Interpreter: `python`

Import the library: `import textutils_pack`

You can then check help on the library with:

  help(textutils_pack)

or on a specific function

  help(textutils_pack.split_words)

## Marking a Directory as a Library

To mark a directory as a library add a file in it called: `__init__.py`. Most of the time they are blank.

#### Source

[Learn Python the Hard Way](http://learnpythonthehardway.org/book/ex25.html)
