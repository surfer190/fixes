---
author: ''
category: Python
date: '2019-07-12'
summary: ''
title: How To Skip A Unit Test
---
# How to skip a unit test

    from unittest import skip, TestCase

    class MyTestCase(TestCase):
        @skip("skipping this")
        def test_vpls_short_conversion(self):
            ...

## Source

* [Python docs: Skipping a Unittest](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)