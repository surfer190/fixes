---
author: ''
category: Python
date: '2019-07-16'
summary: ''
title: Pytest
---
# Pytest

## Install

Install pytest

    pip install pytest

## Naming of Tests

* Your test functions need to be of the form `*_test.py` or `test_*.py`, with or without the underscore.
* Your test class needs to start with `Test`, it seems like pytest discourages using classes

Strangely the class needn't inherit from a pytest test case.

Example:

    class TestClient(object):

        def test_one(self):
            x = "this"
            assert 'h' in x

        def test_two(self):
            x = "hello"
            assert hasattr(x, 'startswith')


