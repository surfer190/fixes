# How to skip a unit test

    from unittest import skip, TestCase

    class MyTestCase(TestCase):
        @skip("skipping this")
        def test_vpls_short_conversion(self):
            ...

## Source

* [Python docs: Skipping a Unittest](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)