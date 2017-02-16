# Python Doc Tests

* Written in a docstring
* Ensure to leave a blank line above and below your doc test
* Any statement to run with python start with `>>>`
* Can use any other functions in the file

Eg.

    """Get area of a square

    >>> size = get_area(2,2)
    >>> size
    4

    """

### Running doctest

`python -m doctest <filename>.py`

Use the `doctest` module

#### Shortcomings

* Bound to code
* uses strings, Tricky to test floats
