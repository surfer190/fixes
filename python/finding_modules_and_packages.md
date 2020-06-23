# Finding Modules and Packages

Python most times is simple but sometimes it appears complex and even complicated when your modules or packages just won't import.

Usually you will get an error:

    ImportError: No module named 'xxx'

Before we get over this hurdle let's take a step nback and understand some of the fundementals

## Fundmentals of Modules and Packages

* A module is a single python file
* A package is a folder containing python files along with a `__init__.py` that tells python it is a package to import files from

Remember all these files have `.py` extensions but importing them with the `.py` is not needed

## Where does python look for modules and packages

Python looks in the environment variable: `$PYTHONPATH`

[More on $PYHTONPATH](https://docs.python.org/3/using/cmdline.html?highlight=pythonpath#envvar-PYTHONPATH)

Printing out the environment variable does not work for me:

    printenv PYTHONPATH

To find out the directories where python is looking for modules and packages use:

    import sys
    print(sys.path)


## How do I add a directory to the PYTHONPATH

One way is in your file:

    import sys
    sys.path.insert(0, "/path/to/your/package_or_module")

Another way is to add it to your environemtn variables permanently:

Add the following line to your `~/.profile` or `~/.bashrc` file.

    export PYTHONPATH=$PYTHONPATH:/path/you/want/to/add

But this method is not the best because usually you will be in a virtual environment for a specific project and don't want to globally set your environment

## Finding where a module is coming from

The module `__file__` attribute

Say you have imported a module but you are unsure where it is coming from you can use the:

    my_module.__file__

which will output the location of the directory that module is coming from

> Note: The file attribute is not present for C modules that are statically linked into the interpreter

## Recent changes to PYTHONPATH

[The current working directory is not added if PYTHONPATH is empty](https://docs.python.org/3/whatsnew/3.4.html#changes-in-python-command-behavior)

An empty `PYTHONPATH`  was equivalent to setting it to `.` previously.

## How to add the current working directory in the python path without modifying the package

SAy you are getting import errors and need to add the current working directory to the `PYTHONPATH` but because this is a package that others are going to use you do not want to use the methods above.

You can set the python path in your virtual environemnt:

`vim /env/bin/activate`

and add:

    export PYTHON_PATH='/my-module/working/dir'

> Note this only works with an activated `pipenv` shell and not when riunning `pipenv run`

### Sources

* [How to add a Python module to syspath?](https://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath/471168)
* [The module `__file__` directory](https://leemendelowitz.github.io/blog/how-does-python-find-packages.html)
* [Definitive guide on python imports](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)