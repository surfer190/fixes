## Python Unit Tests

### Writing Unit Tests

* Are run in a seperate file
* Must import `unittest`

        import unittest

* Create a testcase class that extends `unittest.TestCase`

        class MoveTests(unittest.TestCase)

* Test functions must start with the word `test`
* Use `assert` to ensure `True`

### Running unit tests

        python3 -m unittest tests.py

### Automatically run tests

        if __name__ == '__main__':
            unittest.main()

Run it with

        python3 tests.py

### Assertions

Assertions test a condition in your code that must be met

        self.assertEqual(x, x)
        self.assertNotEqual(x, y)
        self.assertGreater(x, y)
        self.assertLess(x, y)
        self.assertTrue(x)
        self.assertFalse(y)
        self.assertIn(x, [x, y])


### setUp()

A function that runs before every test

        def setUp(self):
            ...


## Using context to ensure Exception is raised

Use the `with` keyword

        def test_bad_description(self):
            with self.assertRaises(ValueError):
                dice.Roll('2b6')

There is also `assertWarns` and `assertLogs`