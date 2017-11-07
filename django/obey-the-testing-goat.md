# Notes to obey the testing goat

## Installing Geckodriver

1. Download the [release](https://github.com/mozilla/geckodriver/releases)
2. Copy that and put it somehere on your path
3. Test that it is working

    geckodriver -- version

Source: [Obey the Testing Goat Prerequisites](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html)

## Write your first functional test

Activate your `venv`:

        workon superlists

Install django and selenium:

        pip install "django<1.12" "selenium<4"

In `functional_tests.py`

        from selenium import webdriver

        browser = webdriver.Firefox()
        browser.get('http://localhost:8000')

        assert 'Django' in browser.title

**Make sure to update your firefox to the latest version**

Run the test:

        python functional_tests.py

The test has failed

### Functional tests

Selenium let us drive a real web browser, they let us see how the application __functions__ from the user's perspective.
It tracks a `user story` which is what a user does and response expected.

Too much redundant terminology:

        Functional Test == Acceptance Test == End-to-End Test

Functional tests should have a **real human story** which can be highlighted in comments

They are good for non-programmers when discussing requirements

## Annoyances

There are some annoyances when dealing with functional tests

### AssertionError

Instead of just getting an `assertionError` it would be nice to get a bit more info

So you can use:

        assert 'To-Do' in browser.title, "Browser title was " + browser.title


### Browser stays open

`Firefox` also stays open which is pretty bad.

### Fixing these problems that have already been solved

By using the `unittest` module we can now make use of `setUp` and `tearDown` methods:

        from selenium import webdriver
        import unittest

        class NewVisitorTest(unittest.TestCase):  

            def setUp(self):  
                self.browser = webdriver.Firefox()

            def tearDown(self):  
                self.browser.quit()

            def test_can_start_a_list_and_retrieve_it_later(self):
                self.browser.get('http://localhost:8000')

                self.assertIn('To-Do', self.browser.title)  
                self.fail('Finish the test!') 

        if __name__ == '__main__':  
            unittest.main(warnings='ignore')

A few things to note:

* Tests organised in classes extending from `unittest.TestCase`
* `setUp` and `tearDown` run before and after all tests
* Using built-in `self.assertIn` instead of just `assert` which gives better errors.
* The `__main__` method checks if the script was run from command line.

**If you have an error in setUp or tearDown is spelt wrong it will not run**

## Functional tests vs Unit Tests

* __Functional tests__ test the application from the outside, from the point of view of the user
* __Unit tests__ test the application from the inside, from the point of view of the programmer

A functional test can be seen as teh driver at a `high level`, unit tests can then be used at the `low level` to complete the steps to achieve the functional success.

## Writing a django Unit Test

Open `<my_app>/tests.py`;

        from django.test import TestCase

        class SmokeTest(TestCase):

            def test_bad_maths(self):
                self.assertEqual(1 + 1, 3)

Run the test with:

    ./manage.py test


