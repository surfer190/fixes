## Notes on the talk about the Black Magic of Python Wheels

## Brief History

### Eggs

* Organically adopted - no guiding PEP (Python enhancement proposal)
* No standard for shipping packages to users
* Designed to be directly importable (contain some or exclusively `.pyc` files) - which may not be compatible with your python version

### The Wheel

* Directed by PEP 427, 376 and 426.
* More portable, cannot contain `.pyc` files

3 types of wheels:

* Pure wheels - just python code, can target a specific version of python.
* universal wheels - python 2 and 3 compatible
* extension wheels - contains a python extension

For pure and universal wheels you run these commands:

    pip install wheel
    python setup.py bdist_wheel

### Python Extensions and the Right of Passage

You install a `requirements.txt` and you need `crytography` so you can use `ssl/tls`.

    pip install cryptography

And the installation fails with `gcc xxxx` and you are missing `#include <Python.h>`

So you check on stackoverflow and it says you need to `apt install python-dev`

It turns out you are missing `ffi.h` as well: `apt install libffi-dev`

Now you need `openssl` as well: `apt install libssl-dev`

Finally the orginal command works

### An Extension Wheel contains the Binaries required

It contains all the packages and takes much less time

* Conda tried to fix these issues but was also not adopted by a PEP
* Conda can package anything and is not supported by PyPI
* Conda packages are not compatible with non-conda environments

### What is a Python Native Extension

Native - specifically for my OS, CPU type and python version
Extension - extends python functionality with non-python code

`cryptography` is a python native extension

* Includes a bit of `c` and c dependencies
* `setup.py` declares is uses `cffi` C foreign function interfaces

Now we have to manage `C` code....oh no

### C is a compiled language

You invoke the `gcc` the GNU C Compiler








## Sources

* [The Black Magic of Python Wheels](https://www.youtube.com/watch?v=02aAZ8u3wEQ)

