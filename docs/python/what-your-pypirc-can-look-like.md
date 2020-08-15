---
author: ''
category: Python
date: '2019-07-17'
summary: ''
title: What Your Pypirc Can Look Like
---
# What your Pypirc can look like

This is what my `.pypirc` looks like:

    [distutils]
    index-servers =
    pypi
    pypitest
    testpypi

    [pypi]
    repository=https://upload.pypi.org/legacy/
    username=my_user
    password=my_pass

    [testpypi]
    repository=https://test.pypi.org/legacy/
    username=my_user
    password=my_pass

    [pypitest]
    repository=https://testpypi.python.org/pypi
    username=my_user
    password=my_pass
