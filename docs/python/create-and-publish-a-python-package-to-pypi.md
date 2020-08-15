---
author: ''
category: Python
date: '2019-07-10'
summary: ''
title: Create And Publish A Python Package To Pypi
---
# Create and publish a python package to pypi

Pypi (said py-pee-aye) - package repository for python maintainers

A package - A module, class or functions that you deploy for other users

### Contents of a package

* `readme.md`
* `mypackage`
    * `__init__.py`
    * `mypackage.py`
* `setup.py`

Contents of `mypackage.py`:

    class MyPackage():
        def spam(self):
            return "eggs"

### Deploying to Pypi

Create a `setup.py` file. At a minimum you need 4 things:

    import setuptools
    
    setuptools.setup(
        name='mypackage',
        version='0.0.1',
        description='My first package',
        packages=setuptools.find_packages()
    )

This `setuptools.find_packages()` is a helper function to discover packages

### Test locally

1. Create a virtual env
2. Validate the package can be imported and installed

    python -m venv env
    source env/bin/activate

3. Install with `-e, --editable <path/url>`   Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url.)

    pip install -e .

Ie. When making changes you don't have to keep reinstalling

4. Enter python repl and import the package and run it

    $ python
    >>> from mypackage import mypackage  
    >>> mypackage.MyPackage().spam()

5. Create an account on test.pypi.org and create a [`~.pypirc`](https://docs.python.org/3.3/distutils/packageindex.html#the-pypirc-file)

    [distutils]
    index-servers =
    pypi
    testpypi

    [pypi]
    repository=https://pypi.python.org/pypi
    username=abc
    password=XXX

    [testpypi]
    repository=https://test.pypi.org
    username=abc
    password=XXX

6. Install dependencies

    pip install twine wheel

7. Package and upload

    python setup.py sdist bdist_wheel
    twine upload --repository testpypi dist/*
    
**This is the bare minimum**

8. Running sdist on your pc would ask you to add extra info

    warning: Check: missing required meta-data: url

    warning: Check: missing meta-data: either (author and author_email) or (maintainer and maintainer_email) must be supplied

9. Add this info to your `setup.py`

    setuptools.setup(
        url='https://github.com/user/repo',
        author='Stephen H',
        author_email='stephenh@startmail.com'
    )

Adding more rich info into packages is [`classifiers`](https://pypi.org/classifiers/)

10. Think...

    setuptools.setup(
        classifiers=[
            'Development Status :: 1 - Planning',
            'Programming Language',
            'Operating System :: OS Independent',
            'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        ]
    )

11. Specify a license

12. Specify a long description

    with open('readme.md') as f:
        long_description = f.read()
    
    setuptools.setup(
        ...
        long_description=long_description,
        long_description_content_type="text/markdown"
        ...
    )

13. Require a specific python version

    setuptools.setup(
        ...
        python_requires='>=3.5',
        ...
    )

14. Specify Required dependencies

    setuptools.setup(
        install_requires=[
            'urllib3',
            'requests'
        ]
    )

15. Excluding tests and test data

    setuptools.setup(
        packages=find_packages(
            exclude=['docs', 'tests', ]
        )
    )

### Cookiecutter

You may want to use [python package cookiecutter](https://github.com/audreyr/cookiecutter-pypackage)

### Reasons to automate this process

* You Aren't managing credentials - a risk and doesn't work well past 1 person
* Ensure consistency - repeatable
* You allow for things to scale

Choose an automation tools:

* `tox` - popular, `.ini` based
* `nox` - flexible, python based


## Source

* [Pycon talk: Python packages](https://www.youtube.com/watch?time_continue=60&v=P3dY3uDmnkU)
* [Python packaging](https://packaging.python.org/tutorials/packaging-projects/)
* [Pypi classifiers](https://pypi.org/classifiers/)
