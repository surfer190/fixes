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

## A proper example

        from django.urls import resolve
        from django.test import TestCase
        from lists.views import home_page


        class HomePageTest(TestCase):

            def test_root_url_resolves_to_home_page_view(self):
                found = resolve('/')
                self.assertEqual(found.func, home_page)

* `resolve` maps a `uri` to a view function
* The view does not exist yet so the function returns:

        ImportError: cannot import name 'home_page'

Let us make it pass:

    home_page = None

then run the test again and you will get a `traceback`

        ======================================================================
        ERROR: test_root_url_resolves_to_home_page_view (lists.tests.HomePageTest)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "/Users/stephen/projects/testing-goat/superlists/lists/tests.py", line 9, in test_root_url_resolves_to_home_page_view
            found = resolve('/')
        File "/Users/stephen/Envs/superlists/lib/python3.6/site-packages/django/urls/base.py", line 27, in resolve
            return get_resolver(urlconf).resolve(path)
        File "/Users/stephen/Envs/superlists/lib/python3.6/site-packages/django/urls/resolvers.py", line 392, in resolve
            raise Resolver404({'tried': tried, 'path': new_path})
        django.urls.exceptions.Resolver404: {'tried': [[<RegexURLResolver <RegexURLPattern list> (admin:admin) ^admin/>]], 'path': ''}

So let us decrypt this gibberish:

* `django.urls.exceptions.Resolver404` is the actual error, sometimes it is self-evident other times not so much.
* Double check what test is actually failing
* Then trace through and find the part of `our` code that actually kicked off the failure (ie. not in django env)

        found = resolve('/')

So to sum it up django can't find a mapping for `/` and a `404` is given

It can be fixed with adding the `url`:

    urlpatterns = [
        url(r'^$', views.home_page, name='home'),
    ]

Now it is complaining that `views.home_page` is not a callable:

    TypeError: view must be a callable or a list/tuple in the case of include()

**Every code change is driven by a test**

        def home_page():
            pass

**Tests Pass**

        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.001s

        OK

## The TDD Cycle

The cycle now has 2 steps

1. In the terminal, run the unit tests and see how they fail.
2. In the editor, make a minimal code change to address the current test failure.

> The more nervous we are about getting our code right, the smaller and more minimal we make each code change—​the idea is to be absolutely sure that each bit of code is justified by a test.

> TDD is a discipline, and that means it’s not something that comes naturally

## Interacting with the page with Selenium

* `find_element_by_tag_name` / `find_elements_by_tag_name`

        header_text = self.browser.find_element_by_tag_name('h1').text

* `find_element_by_id`

        inputbox = self.browser.find_element_by_id('id_new_item')

* `send_keys` - seleniums way of typing into an element
        
        inputbox.send_keys('Buy peacock feathers')

* Use the `ENTER` key

        from selenium.webdriver.common.keys import Keys
        inputbox.send_keys(Keys.ENTER)

* Wait for the page to refresh

        import time
        time.sleep(1)

## Asserting existance in iterables

Make use of `any` to ensure existance in iterables

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

> Big changes to a functional test are usually a good thing to commit on their own

## Dont test constants rule

> Unit tests are really about testing logic, flow control, and configuration. Making assertions about exactly what sequence of characters we have in our HTML strings isn’t doing that.

**refactor - improve the code without changing its functionality**

## The Django Test Client

Instead of manually creating an `HttpRequest()` we can use `response = self.client.get('/')`

You can then make use of `assertTemplateUsed`:

    self.assertTemplateUsed(response, 'home.html')

**Always be suspicious of tests you have not seen fail**

This lets us remove tests about `resolve` and tests about actual html

So we are now _testing our implementation and not constants_

## On Refactoring

> keep refactoring and functionality changes entirely separate

We can pass a custom error message as an argument to most assertX methods in unittest

Example:

        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

## The TDD Process

1. Functional test
2. Unit test
3. Minimal code ot pass test
4. Refactor

> The functional tests are the ultimate judge of whether your application works or not. The unit tests are a tool to help you along the way.




