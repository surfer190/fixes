# Fixes

Mostly Technology related summaries, fixes, solutions and notes

[fixes.co.za](http://fixes.co.za)

![Build Status](https://jenkins.fixes.co.za/buildStatus/icon?job=fixes)

* Common problems and solutions, fixes, notes and tips gathered while trying to solve problems
* _fixes_ are displayed as technical documentation using [mkdocs](https://www.mkdocs.org/) and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
* Some interpretations and summaries of tech related documentation and books

### Where to view Fixes

The collection of fixes can be viewed with your web browser at: [http://fixes.co.za](http://fixes.co.za)

## Getting Started

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    mkdocs serve

### Create / Update the index page

When making an update make sure to run:

    python3 update_index.py

This updates the index page.

### Install a `pre-commit` hook

Install a `pre-commit` hook:

    sudo vim ./fixes/.git/hooks/pre-commit

and write:

    #!/bin/sh
    source ./env/bin/activate && python update_index.py
