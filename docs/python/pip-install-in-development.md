---
author: ''
category: Python
date: '2022-07-12'
summary: ''
title: Packaging - Pip Install for Development
---

## Pip install in Development

A.k.a `pip install -e`

### What is Setup.py

`setup.py` is a python file, the presence of which is an indication that the module/package you are about to install has likely been packaged and distributed with Distutils, which is the standard for distributing Python Modules.

### Installing Modules

* [Installing Python Modules (Legacy version)](https://docs.python.org/3/install/)
* [Installing Python Modules (current version)](https://docs.python.org/3/installing/index.html#installing-index)

If there is a `setup.py` in your module (or directory).
You can usually install everything you need with:

    pip install .

> This copies the files and folders of your package/module to your python env's `~/.virtualenvs/your-venv-name/lib/python3.7/site-packages`

If you want to develop on the current module, use editable mode:

    pip install -e .

> This leaves the files where they are and adds a `<my-module>.egg-link` which is a symlink to the module folder. So you can then edit the files where they are and have it reflect in the running code.

These installation methods are preferred over the legacy:

    python setup.py install


### Sources

* [.egg-link definition](https://wiki.python.org/moin/PythonPackagingTerminology)
* [pip install editable mode](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install)
* [What is setup.py](https://stackoverflow.com/questions/1471994/what-is-setup-py)
