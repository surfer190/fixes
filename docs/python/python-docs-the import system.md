---
author: ''
category: Python
date: '2022-07-25'
summary: ''
title: Python docs - The Import System
---

## The Import system from the Python Docs

Python code in one module gains access to code in another module by `import`ing it

The `import` statement is the most common way but you can also:

* `importlib.import_module()`
* `__import__()`

The import statement:

1. it searches for the named module
2. it binds the results of that search to a name in the local scope

> A direct call to `__import__()` performs only the module search and, if found, the module creation operation.

If the named module cannot be found, a `ModuleNotFoundError` is raised

[importlib](https://docs.python.org/3/library/importlib.html#module-importlib) - is an interface for interacting with the `import` system

### Packages

Packages:

* organise modules
* provide a naming hierachy

> You can think of packages as the directories on a file system and modules as files within directories

> It’s important to keep in mind that all packages are modules, but not all modules are packages.

Any module that contains a `__path__` attribute is considered a package

> All modules have a name. Subpackage names are separated from their parent package name by a dot, akin to Python’s standard attribute access syntax. Eg. `email.mime.text`

#### Regular packages

* A regular package is typically implemented as a directory containing an `__init__.py` file.
* When a regular package is imported, this `__init__.py` file is implicitly executed, and the objects it defines are bound to names in the package’s namespace. (A good place to setup logging)
* The `__init__.py` file can contain the same Python code that any other module can contain

    parent/
        __init__.py
        one/
            __init__.py
        two/
            __init__.py
        three/
            __init__.py

> That is a top level parent with 3 subpackages. Importing `parent.one` implicitly executes `parent/__init__.py` and `parent/one/__init__.py`

#### Namespace packages

* Namespace packages may or may not correspond directly to objects on the file system; they may be virtual modules that have no concrete representation.
* With namespace packages, there is no `parent/__init__.py` file. In fact, there may be multiple parent directories found during import search, where each one is provided by a different portion.

### Searching

* Python needs the **fully qualified** name - dotted name showing the “path” from a module’s global scope to a class, function or method.
* e.g. `foo.bar.baz` In this case, Python first tries to import `foo`, then `foo.bar`, and finally `foo.bar.baz`. If any of the intermediate imports fail, a ModuleNotFoundError is raised.
* During import, the module name is looked up in `sys.modules`
* Python includes a number of default finders and importers. The first one knows how to locate built-in modules, and the second knows how to locate frozen modules. A third default finder searches an import path for modules. The import path is a list of locations that may name file system paths or zip files.

### Keywords

* `__path__` -  if a module has a `__path__` attribute, it is a package. Non-package modules should not have a `__path__` attribute.
* `__name__` - fully qualified name of the module - uniquely identifies the module
* `__loader__` - the loader object used to laod the module
* `__package__` - When the module is a package, its `__package__` value should be set to its `__name__`. When the module is not a package, `__package__` - should be set to the empty string for top-level modules, or for submodules, to the parent package’s name
* `__spec__` - the moduel specification used to import the module
* `__file__` - is optional. If set, this attribute’s value must be a string. Import system may leave it unset.

### Source

* [Python docs - the import system](https://docs.python.org/3/reference/import.html)
