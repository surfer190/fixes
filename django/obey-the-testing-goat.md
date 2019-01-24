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

## Saving User Input

> The point of TDD is to allow you to do one thing at a time

What if a functional test fails with a cryptic message:
* Add `print` statements, to show, for example, what the current page text is.
* Improve the error message to show more info about the current state.
* Manually visit the site yourself.
* Use `time.sleep` to pause the test during execution.

If you ever get a `StaleElementReferenceException` exception try increasing `time.sleep(4)`

Giving actual response in `assert` using an `f` string:

        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            f"New todo item is not in the table. Contents were: \n{ table.text }"
        )

But always watch _You should always be very worried whenever you think you’re being clever, because what you’re probably being is overcomplicated_

The above assertion can be simplified with:

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

### Red, Green, Refactor

The unit testing cycle is known as:

1. Red: failing unit test
2. Green: simplist code to pass the test
3. Refactor for better code that makes more sense

Remeber to avoid `duplication` and a `magic constant` by writing a test that forces the magix constant to fail

ie. list items enumerated with `1,2,3`

### Three Strikes and refactor

It is okay to repeat yourself once (_Don't repeat Yourself_) but not 3 times.
Then you need to refactor.

You can use helper methods (those that don't start with `test_`) in your test classes, best to put them below `tearDown()`

## Django model test example

        class ItemModelTest(TestCase):

        def test_saving_and_retrieving_items(self):
            first_item = Item()
            first_item.text = 'The first (ever) list item'
            first_item.save()

            second_item = Item()
            second_item.text = 'Item the Second'
            second_item.save()

            saved_items = Item.objects.all()
            self.assertEqual(saved_items.count(), 2)

            first_saved_item = saved_items[0]
            second_saved_item = saved_items[1]

            self.assertEqual(first_saved_item.text, 'The first (ever) list item')
            self.assertEqual(second_saved_item.text, 'Item the Second')

> Purists will tell you that a "real" unit test should never touch the database, and that the test I’ve just written should be more properly called an integrated test, because it doesn’t only test our code, but also relies on an external system—​that is, a database.

### Another test involving db

        def test_can_save_a_POST_request(self):
            response = self.client.post('/', data={'item_text': 'A new list item'})

            self.assertEqual(Item.objects.count(), 1)  
            new_item = Item.objects.first()  
            self.assertEqual(new_item.text, 'A new list item')  

            self.assertIn('A new list item', response.content.decode())
            self.assertTemplateUsed(response, 'home.html')

But this is testing multiple things.
**It is best to test one thing at a time**

The reason is that tests with multple assertion won't test the next assertions if an earlier one fails

Another good rule of thumb:

> Always redirect after a POST

So you would test that the `POST` is saved and a different test to test that is `redirects`

### Structuring your test

Sometimes it is nice to structure the code that `setsup` the test, actually `does work` and the part that `tests`

        def test_displays_all_list_items(self):
            Item.objects.create(name='Itemy one')
            Item.objects.create(name='Itemy two')

            response = self.client.get('/')

            self.assertIn('Itemy one', response.content.decode())
            self.assertIn('Itemy two', response.content.decode())

__Regession: When new code breaks some other part of the application that used to work__

## Improving Functional Tests

Taking steps to make our tests **more deterministic and more reliable**

### Isolation

Classic problem of `isolation`:

> Each run of our functional tests was leaving list items lying around in the database, and that would interfere with the test results when you next ran the tests.

One way to fix this is clearing up in `tearDown` and `setUp`

But even better django has created `LiveServerTestCase` which can do this work for you.
* Automatically creates a test database
* Stars dev server to functional test against

#### Organising your tests

1. Add a `functional_tests` folder as an app in your project.
2. Make it a package by adding `__init__.py` file into that folder

Now instead of running functional tests with:

        python functional_tests.py

We can use:

        python manage.py test functional_tests

It is best to keep them seperate from apps as they are usually cross cutting.

Now the tests should extend from `LiveServerTestCase`

Instead of hard-coding the url we can use the `self.live_server_url` variable

        self.browser.get(self.live_server_url)

Also remove the `__main__` method

Now `./manage.py test` will run both unit and functional tests.
To run just unit tests you must specify the app name:

        ./manage.py test lists

## Upgrading Selenium and Geckodriver

When `firefox` autoupdates a `selenium` and `geckodriver`update is also needed:

        pip install --upgrade selenium

Then download the latest [geckodriver](https://github.com/mozilla/geckodriver/releases)

__One of those things you have to put up with__

## Implicit and Explicit Waits

Explicit waits are `time.sleep(5)`
The implicit waits are automatic with the method `implicitly_wait`

In `selenium 3` implicit waits became flakey and were deemed a bad idea.

But the `time.sleeps` will slow down the functional test running process, but if they are too short you will get a spurrious failure.

Unexpected `NoSuchElementException` and `StaleElementException` are signs of no explicit `time.sleep()`
### One way of waiting for elements

        from selenium.common.exceptions import WebDriverException
        MAX_WAIT = 10


        class SuperListTests(LiveServerTestCase):

        [...]

        def wait_for_row_in_list_table(self, row_text):
                start_time = time.time()
                while True:
                try:
                        table = self.browser.find_element_by_id('id_list_table')
                        rows = table.find_elements_by_tag_name('tr')
                        self.assertIn(row_text, [row.text for row in rows])
                        return
                except (AssertionError, WebDriverException) as e:
                        if time.time() - start_time > MAX_WAIT:
                        raise e
                        time.sleep(0.5)

* We set a `MAX_WAIT` time constant
* `WebDriverException` means the page has not loaded and selenium can't find the element
* `AssertionError` when the table is there but there are no rows in as it has not reloaded

That shaves some seconds off and it all adds up

**Avoid voodoo `time.sleeps` and seleniums implicit wait helpers**

## Working Incrementally

Going from working state to working state when adapting existing code

> TDD is closely associated with the agile movement in software development, which includes a reaction against `Big Design Up Front`

> The agile philosophy is that you learn more from solving problems in practice than in theory

### Yagni

But we obey another tenet of the agile gospel: "YAGNI" 

__You ain't gonna need it__

As software developers, we have fun creating things, and sometimes it’s hard to resist the urge to build things just because an idea occurred to us and we might need it.
The trouble is that more often than not, no matter how cool the idea was, you won’t end up using it.

Be Rest(ish) -  URL strucuture should match the data structure

You can use `##` meta comments indicating how the tests are working and why, distinguishing from regular `user story` comments

1. Write the functional test
2. Write the minimal unit test to fulfill the test
3. Write the minimal code to fulfil the unit test

When an old test fails as well as a new test, then a _regression_ has been introduced.

When testing you want a case often to work for n cases.
Going from 0 to 1, is the first task and often makes going from 1 to n _trivial_.

Tip: Use `assertContains(response, x)` instead of `assertIn/response.content.decode()` as it will automatically fail when the response is not `200`

Anohter good one is `assertRedirects` which checks location and response code.

> A second clue is the rule of thumb that, when all the unit tests are passing but the functional tests aren’t, it’s often pointing at a problem that’s not covered by the unit tests, and in our case, that’s often a template problem.

A good trick to see all the test classes and tests in a file:

        grep -E "class|def" lists/tests.py

Another crazy convention:

        URLs without a trailing slash are "action" URLs which modify the database

Showing variables that are pythonreserved words - adding an underscore afterwards

        list_ = []

Making minimal changes getting a solution is _counterintuitive_

> But remember the Testing Goat! When you’re up a mountain, you want to think very carefully about where you put each foot, and take one step at a time, checking at each stage that the place you’ve put it hasn’t caused you to fall off a cliff.

## Web Development Sine Qua Nons - a thing that is absolutely necessary

* static files
* form data validation
* the dreaded JavaScript
* deployment to a production server

### Prettification

Testing aesthetics are a bit like testing a constant

But we can test our implementation

#### Example test an input is in the middle of the page

        class NewVisitorTest(LiveServerTestCase):
        [...]


        def test_layout_and_styling(self):
                # Edith goes to the home page
                self.browser.get(self.live_server_url)
                self.browser.set_window_size(1024, 768)

                # She notices the input box is nicely centered
                inputbox = self.browser.find_element_by_id('id_new_item')
                self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
                )

#### Static Assets

`runserver` automagivally finds static files but `LiveServerTestCase`doesn't.
But do not fear as django has a test class for this case too: `StaticLiveServerTestCase`

Check the [docs](https://docs.djangoproject.com/en/1.11/howto/static-files/#staticfiles-testing-support)

The `collectstatic` command is used to collect all static assets in app folders and put them in a single location for serving with a CDN.

The destination is set in the `STATIC_ROOT` of `settings.py`

This folder should be ignored by version control

### Selenium Webdriver Docs

View the [Selenium Webdriver docs](http://selenium-python.readthedocs.io/api.html)

## Deploying to a staging site

You can run functional tests against the staging server url instead of local.
It involves checking for an environment variable and then changing the `live_server_url`

        def setUp(self):
                self.browser = webdriver.Firefox()
                staging_server = os.environ.get('STAGING_SERVER')  
                if staging_server:
                    self.live_server_url = 'http://' + staging_server

But here we find the `LiveServerTestCase` limitations, it always want to use its own test server.

## Splitting up tests

> Remember that functional tests are closely linked to "user stories"

A feature has many user stories.

### Skipping a test

Sometimes when refactoring your tests you want all of them passing

You can delbrately skip a test by importing `skip`:

        from unittest import skip

and using the annotation on the function:

        @skip
        def test_cannot_add_empty_list_items(self):

**Skips are dangerous—​you need to remember to remove them before you commit your changes back to the repo**

#### Splitting tests

        class FunctionalTest(StaticLiveServerTestCase):

                def setUp(self):
                        [...]
                def tearDown(self):
                        [...]
                def wait_for_row_in_list_table(self, row_text):
                        [...]


                class NewVisitorTest(FunctionalTest):

                def test_can_start_a_list_for_one_user(self):
                        [...]
                def test_multiple_users_can_start_lists_at_different_urls(self):
                        [...]


                class LayoutAndStylingTest(FunctionalTest):

                def test_layout_and_styling(self):
                        [...]



                class ItemValidationTest(FunctionalTest):

                @skip
                def test_cannot_add_empty_list_items(self):
                        [...]

What we have now is test classes that inherit from `FunctionalTest` which does all the hreavy lifting in terms of `setUp`, `tearDown` and setting the `live_server_url`

This is **very important**. If you have a common `setUp` step then best to create a class that can be extended from instead of duplicating the `setUp` in multiple test classes.

### We can split even further

Create a `base.py` in `functional_tests`and add the `FunctionalTest` class which contains all our helper methods.

Split out the tests now into indicidual files, ensure that they start with `test_...` and that they `from .base import FunctionalTest`

Now functional tests can be run individually:

        python manage.py test functional_tests.test_list_item_validation

## A genric wait helper

> Whenever you submit a form with Keys.ENTER or click something that is going to cause a page to load, you probably want an explicit wait for your next assertion.

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

You can then make use of it with a lambda, a throwaway function not requiring a `def`.

        self.wait_for(lambda: self.assertEqual(
                self.browser.find_element_by_css_selector('.has-error').text,
                "You can't have an empty list item"
        ))

So the function is now passed as an argument to `self.wait_for`

### Refactoring Unit Tests

Create a directory `tests` within the `app` folder.
Add the dunderinit `__init__.py`

Then split the files into: `test_models.py` and `test-views.py`

## Validation at the Database Level

> In a web app, there are two places you can do validation: on the client side (using JavaScript or HTML5 properties, as we’ll see later), and on the server side. The server side is "safer" because someone can always bypass the client side, whether it’s maliciously or due to some bug.

> Similarly on the server side, in Django, there are two levels at which you can do validation. One is at the model level, and the other is higher up at the forms level. I like to use the lower level whenever possible, partially because I’m a bit too fond of databases and database integrity rules, and partially because, again, it’s safer—​you can sometimes forget which form you use to validate input, but you’re always going to use the same database.

### A Django Quirk: Django models don’t run full validation on save

**Django models don’t run full validation on save**

Django does have a method to manually run full validation, however, called `full_clean`

__Tip: There are sometimes special characters in the html response__

                <span class="help-block">You can&#39;t have an empty list item</span>

Which you can hack in for the actual response in a test, but it is better to use the `escape` helper function.

                from django.utils.html import escape

                expected_error = escape("You can't have an empty list item")

# Absolute URl

Model objects are usually associated with a particular url with `get_absolute_url`

It is good practise to always set this for a model
so write the test:

        def test_get_absolute_url(self):
            list_ = List.objects.create()
            self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

Simple instruction

        class List(models.Model):
    
            def get_absolute_url(self):
                return reverse('view_list', args=[self.id])

You can then redirect with:

        return redirect(list_)

### A note on Database Validations

* It is a gaurentee at the lowest level of validity and consistency
* At the expense of flexibility, you cannot have partial models
* Not designed for user friendliness the user will get a nasty `500 IntegrityError`

# Forms

> In Django, a complex view is a code smell. Could some of that logic be pushed out to a form? Or to some custom methods on the model class? Or maybe even to a non-Django module that represents your business logic?

When testing a form you can use the `as_p()` method:

        from django.test import TestCase
        from lists.forms import ItemForm


        class ItemFormTest(TestCase):

        def test_form_renders_item_text_input(self):
                form = ItemForm()
                self.assertIn('placeholder="Enter a to-do item"', form.as_p())
                self.assertIn('class="form-control input-lg"', form.as_p())

We can customise the input using a widget:

        class ItemForm(forms.Form):
            item_text = forms.CharField(
                    widget=forms.fields.TextInput(attrs={
                    'placeholder': 'Enter a to-do item',
                    }),
            )

These modifications can become tedious and it may be better to look into [cripy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) or [floppy-forms](http://django-floppyforms.readthedocs.io/en/latest/)

### ModelForms

If you want to use the validation rules from your `model` then it is best to use a `ModelForm`

It is configured with `class Meta:`:

        class ItemForm(forms.models.ModelForm):

        class Meta:
            model = Item
            fields = ('text',)

You can override the defaults in a `ModelForm`:

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }

### Testing validation

Calling `form.is_valid()` returns `True` or `False`, but it also has the side effect of validating the input data, and populating the errors attribute

        def test_form_validation_for_blank_items(self):
            form = ItemForm(data={'text': ''})
            self.assertFalse(form.is_valid())
            self.assertEqual(
                form.errors['text'],
                ["You can't have an empty list item"]
            )

The default error message from django is different:

        AssertionError: ['This field is required.'] != ["You can't have an empty list
item"]

You can change it in `class Meta`:

        class ItemForm(forms.models.ModelForm):

            class Meta:
                [...]
                error_messages = {
                    'text': {'required': "You can't have an empty list item"}
                }

#### A note on constants

Sometimes creating constants like:

    EMPTY_ITEM_ERROR = "You can't have an empty list item"

Lets us import them in tests so we are only changing them in one place:

    from lists.forms import EMPTY_ITEM_ERROR, ItemForm

#### Keep commits seperate

Try and keep `rename` separate from the `logic` change

#### Creting a helper function

Remember that we are inheriting from a helper class in functional tests. If you find that you have a piece of code that if it chnages will need to change in mulitple places consider making that a helper function.

### Ensuring correct form is used

    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertIsInstance(
            response.context['form'],
            ItemForm
        )

#### Refactoring Tests

You can refactor for finding elements:

Say you have a lot of:

        self.browser.find_element_by_id('id_text')

And the id changes, you can create a function:

        def get_item_input_box(self):
                return self.browser.find_element_by_id('id_text')

And make calls like:

        inputbox = self.get_item_input_box()

or enter text with:

        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

**Be wary of testing too many things in a single test. Tests should clearly test one thing.**

Another way to ensure many smalltests is create a helper method called `post_invalid_data` for example.

Then have `response = self.post_invlaid_data()`

__Helper methods are one of the tools that lower the psychological barrier.__

## Free Browser Client-Side Validation

With html5 if an input has the `required` attribute 

Make sure to check for the CSS psuedo-selector `:invalid`

        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

> You can’t be writing tests for every possible way we could have coded something wrong

> One way of putting it is that you should trust yourself not to do something deliberately stupid, but not something accidentally stupid.

## Skipping a test

Sometimes you may want to `skip` a test.

This can be done:

        from unittest import skip
        [...]

                @skip
                def test_duplicate_item_validation_errors_end_up_on_lists_page(self):

## Asserting Instance fo Form

You can use `unittests`'s `assertIsInstance`

    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertIsInstance(
            response.context['form'],
            ExistingListItemForm
        )

## Ensure something is displayed

Use selenium's: `is_displayed()`

        self.wait_for(lambda: self.assertTrue(  
                self.browser.find_element_by_css_selector('.has-error').is_displayed()  
                ))

# Testing Javascript

Choosing a testing library and a test runner with python and django is straightforward. We use the standard library's `unittest` and django's `manage` testrunner.

There are others though: [pytest](https://docs.pytest.org/en/latest/), [nose](http://nose.readthedocs.io/en/latest/) and [green](https://github.com/CleanCut/green)

It is not as straightforward in the js testing world...

There are a lot of options: jsUnit, Qunit, Mocha, Chutzpah, Karma, Jasmine and many more

Unfortunately it does not stop there, you need to find an __assertion framework__ and a __reporter__, and maybe a __mocking library__, and it never ends!

Let's try [QUnit](http://qunitjs.com/)

Follow the instructions and put the files in `<app_name>/static/tests`

A QUnit test looks like:

        QUnit.test("smoke test", function (assert) { 
            assert.equal(1, 1, "Maths works!"); 
        });

`QUnit.test` defines a test case much like `def test_something(self)` with the test name the first argument

`assert.equal` is much like `assertEqual`. The message is displayed whether it works or not so make it a positive message.

### Asserting html properties

        QUnit.test("smoke test", function(assert) {
            assert.equal($('.has-error').is(':visible'), true);
            $('.has-error').hide();
            assert.equal($('.has-error').is(':visible'), false);
        });

> QUnit tests do not run in a predictable order

So we need a `setUp` and `tearDown` which can be achieved with a `qunit-fixture`

It will reset each time if it is in:

    <div id="qunit-fixture">
        ...
    </div>

> Order execution is the biggest headache in JS testing and how it interacts with the global DOM state

An element's events are removed when that element is removed and reloaded into the DOM

Make use of `console.log()` statements

Make use of an initialize function:

    var initialize = function () {
        $('input[name="text"]').on('keypress', function () {
            $('.has-error').hide();
        });
    };

Then be sure to call it as the first thing in your tests:

    QUnit.test("errors should be hidden on keypress", function (assert) {
        initialize();
        $('input[name="text"]').trigger('keypress'); 
        assert.equal($('.has-error').is(':visible'), false);
    });

    QUnit.test("errors aren't hidden if there is no keypress", function (assert) {
        initialize();
        assert.equal($('.has-error').is(':visible'), true);
    });

Then once your tests are passing then add them to your django template and call `initialize`:

    <script src="/static/list.js"></script>

    <script>
      initialize();
    </script>

### Onload Boilerplate and Namespacing

Initialize is too generic. Another 3rd party javascript library might use it. So use a `namespace`.

    window.Superlists = {}; 
    window.Superlists.initialize = function () { 
        $('input[name="text"]').on('keypress', function () {
            $('.has-error').hide();
        });
    };

Then run:

    window.Superlists.initialize();

Then it is good to ensure that the page has loaded before running js:

    $(document).ready(function () {
        window.Superlists.initialize();
    });

### Testing Cycle Update

1. Write a FT and see it fail
2. Figure out which kind of code your are testing. Javascript or Python.
3. Write a unit test in either language and see it fail.
4. Write code in either language and see it pass.
5. Rince and repeat.

**Gotchas**:

* You can make QUnit run tests from the command line as well
* If you are using Angular, React or Vue it might be easier to use [jasmine](https://jasmine.github.io/) for tests

# USer Authenticaiton, Spiking and DeSpiking

> Whenever you hear a user requirement, it’s important to dig a little deeper and think—​what is the real requirement here?

## Spiking

Spiking refers to a quick, exploratory, investigation that involves coding.
[See more info about how the spike word came about](https://stackoverflow.com/questions/249969/why-are-tdd-spikes-called-spikes)

Despiking is replacing the prototype with tested production ready code.

## Mocking

### Monkey Patching

During testing you never want to be sending out real data and doing real actions against 3rd-party services.

For example `send_mail`. We want to tell python to swap out the `send_mail` function with a fake version at runtime.

You define a fake version that takes the same parameters, inside the parent test function:

    def fake_send_mail(subject, body, from_email, to_list):  
        self.send_mail_called = True
        self.subject = subject
        self.body = body
        self.from_email = from_email
        self.to_list = to_list

It saves information about how it was called

Then you simply swap out the real one in the view with the fake one:

    accounts.views.send_mail = fake_send_mail

> It’s important to realise that there isn’t really anything magical going on here; we’re just taking advantage of Python’s dynamic nature and scoping rules.

Remember we need the corect namespace which means the correct scope that the function is being swapped out at.

**Always mock before the function you want to call is run**

## UnitTest.Mock

As of Python 3.3 you can `from unittest.mock import Mock`

Allows you to do:

        >>> from unittest.mock import Mock
        >>> m = Mock()
        >>> m.any_attribute
        <Mock name='mock.any_attribute' id='140716305179152'>
        >>> type(m.any_attribute)
        <class 'unittest.mock.Mock'>
        >>> m.any_method()
        <Mock name='mock.any_method()' id='140716331211856'>
        >>> m.foo()
        <Mock name='mock.foo()' id='140716331251600'>
        >>> m.called
        False
        >>> m.foo.called
        True
        >>> m.bar.return_value = 1
        >>> m.bar(42, var='thing')
        1
        >>> m.bar.call_args
        call(42, var='thing')

## Unittest.patch

We can use `patch` to do monkey patching.

First import it:

        from unittest.mock import patch

Add a decorator to the test, specifying which dot-notated fucntion to patch.
The mocked object is then injected as an argument to the test

        @patch('accounts.views.send_mail')
        def test_sends_mail_to_address_from_post(self, mock_send_mail):
            ...

Convention is to use the `mock_` prefix then the name of function being replaced.

Then assertions can be made about the test:

    self.assertEqual(mock_send_mail.called, True)  
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args  
        self.assertEqual(subject, 'Your login link for Superlists')
        self.assertEqual(from_email, 'noreply@superlists')
        self.assertEqual(to_list, ['edith@example.com'])

> mocks can leave you "tightly coupled with the implementation". We usually say it’s better to test behaviour, not implementation details; test what happens, not how you do it

## The Call Object

A `call` object is essentially a tuple of `(positional_args, keyword_args)`

    from unittest.mock import call

* `positional_args` is itself a tuple, consisting of the set of positional arguments
* `keyword_args` is a dictionary

So the below 2 are the same:

        self.assertEqual(
            mock_auth.authenticate.call_args,
            ((,), {'uid': 'abcd123'})
        )
        # or this
        args, kwargs = mock_auth.authenticate.call_args
        self.assertEqual(args, (,))
        self.assertEqual(kwargs, {'uid': 'abcd123'})

> When you call a mock, you get another mock. But you can also get a copy of that returned mock from the original mock that you called.

**Geez!**

You can patch at class level if needed (more than 3 cases):

        @patch('accounts.views.auth')  
        class LoginViewTest(TestCase):

            def test_redirects_to_home_page(self, mock_auth):  
                [...]

            def test_calls_authenticate_with_uid_from_get_request(self, mock_auth):  
                [...]

            def test_calls_auth_login_with_user_if_there_is_one(self, mock_auth):  
                [...]


            def test_does_not_login_if_user_is_not_authenticated(self, mock_auth):
                mock_auth.authenticate.return_value = None  
                self.client.get('/accounts/login?token=abcd123')
                self.assertEqual(mock_auth.login.called, False)

> One good justification for using mocks is when they will reduce duplication between tests. It’s one way of avoiding combinatorial explosion. 

### Avoid Mock’s Magic assert_called

Instead of:

        self.assertEqual(a_mock.call_args, call(foo, bar))

Just do:

        a_mock.assert_called_with(foo, bar)

The problem is it is too easy to make a type on the mock method, which will return a regular mock which will pass.

# Test Fixtures and a Decorator for Explicit Waits

We’re going to have to write FTs that have a logged-in user. Rather than making each test go through the (**time-consuming**) login email dance, we want to be able to skip that part.

## Skipping the Login Process by Pre-creating a Session

Usually a user will return to a site with a session anyway, so it is not an unrealistic cheat.

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY
from django.contrib.sessions.backends.db import SessionStore

from .base import FunctionalTest

User = get_user_model()


        class MyListTest(FunctionalTest):

        def create_pre_authenticated_session(self, email):
                user = User.objects.create(email=email)
                session = SessionStore()
                # session key is the primary key of the user object
                session[SESSION_KEY] = user.pk
                session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
                session.save()
                # To set a cookie we first need to visit the domain
                # 404 pages load the quickest!
                self.browser.get(self.live_server_url + "/404_no_such_url/")
                # Add a cookie to the browser matching the session on server
                self.browser.add_cookie(dict(
                name=settings.SESSION_COOKIE_NAME,
                value=session.session_key,
                path='/'
                ))

Using it in a test:

        def test_logged_in_users_lists_are_saved_as_my_lists(self):
                email = 'edith@example.com'
                self.browser.get(self.live_server_url)
                self.wait_to_be_logged_out(email)

                # Edith is a logged-in user
                self.create_pre_authenticated_session(email)
                self.browser.get(self.live_server_url)
                self.wait_to_be_logged_in(email)

### JSON Test Fixtures

Sometimes creating json fixtures wtih `dumpdata` can seem to save time, when setting up a test.

The problem is they are a:

* Nightmare to maintain with model changes.
* Difficult for the reader to determine which attributes are important and which are just fillers. 
* Shareing fixtures that need something slightly different, will end up with you copying the whole thing to keep them isolated.

So it is advisable just to load directly from the ORM.

### A Wait Decorator

The difference is that the decorator doesn’t actually execute any code itself—it returns a modified version of the function that it was given.

    def wait(fn):
        def modified_fn():
            start_time = time.time()
            while True:
                try:
                    return fn()
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)

        return modified_fn

* The decorator take a function as an argument and returns a modified function
* We keep catching exceptions until the timer runs out


Using it with:

       table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    @wait
    def wait_to_be_logged_in(self, email):
        self.browser.find_element_by_link_text('Log out')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)


    @wait
    def wait_to_be_logged_out(self, email):
        self.browser.find_element_by_name('email')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)

But when we run it we get:

        TypeError: modified_fn() takes 0 positional arguments but 2 were given

So our arguments are not being sent into the `modified_fn`

We use [variadic arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments) with `*args` and `**kwargs`

    def wait(fn):
        def modified_fn():
            start_time = time.time()
            while True:
                try:
                    return fn()
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)

        return modified_fn

We can now use the `@wait` with `wait_for`:

    @wait
    def wait_for(self, fn):
        return fn()
    
# Server Side Debugging

Skipped this...ruffhouse

# Outside-In TDD

Writing the functional test first nd then the unit test is a manifestation of outside-in.

Design the system from the outside and build up the code in layers.

Inside-out is starting with the innermost components first.
It **feels** comfortable because you are never working on a piece of code that depends on something that has not been implemented.

Why "Inside-out" is kak?:

* We might have ideas in our head about the new desired behaviour of our inner layers like database models that  are actually just speculation
* Inside out causes us to stray from the TDD workflow. 
* One problem that can result is to build inner components that are more general or more capable than we actually need
* You might end up with inner components which, you later realise, don’t actually solve the problem that your outer layers need solved

> In contrast, working outside-in allows you to use each layer to imagine the most convenient API you could want from the layer beneath it

> Another Pass, Outside-In

At each stage, we still let the FT drive what development we do.

> Outside-In TDD is sometimes called "programming by wishful thinking"

### A Decision Point: Whether to Proceed to the Next Layer with a Failing Test

Should we use a mock to isolate something from the model layer?

It is mroe effort to use mocks, and mocks can make the test harder to read.

But what if there are 5 or more layers, we would leave this failing test and still won't have an idea if anything is working.

# Test Isolation, and "Listening to Your Tests"

Proceeding to work on lower levels while you’re not sure that the higher levels are really finished or not is a risky strategy

> Using mocks does tie you to specific ways of using an API. This is one of the many trade-offs involved in the use of mock objects. 

You have to use `List()` instead of django's `List.objects.create`

Sometimes it's not enough just to check an attribute, we need to ensure the sequence is correct. That assignment is done before a `save`

You would use a `side_effect`

eg:

    def test_list_owner_is_saved_if_user_is_authenticated(
            self, mockItemFormClass, mockListClass
        ):
            user = User.objects.create(email='a@b.com')
            self.client.force_login(user)
            mock_list = mockListClass.return_value

            def check_owner_assigned():  
                self.assertEqual(mock_list.owner, user)
            mock_list.save.side_effect = check_owner_assigned  

            self.client.post('/lists/new', data={'text': 'new item'})

            mock_list.save.assert_called_once_with()

So when `save` function is called it will run the assertion.

It is important to ensure the side_effect is run using:

    mock_list.save.assert_called_once_with()

So importantly:

* Always assign the side_effect earlier rather than later (to ensure it is assigned when it runs)
* Ensure the method assigned the side_effect is actually run

> In order to rewrite our tests to be fully isolated, we need to throw out our old way of thinking about the tests in terms of the "real" effects of the view on things like the database, and instead think of it in terms of the objects it collaborates with, and how it interacts with them.

A veey isolated test:

    from unittest.mock import patch
    from django.http import HttpRequest
    from lists.views import new_list2
    [...]

    @patch('lists.views.NewListForm')  
    class NewListViewUnitTest(unittest.TestCase):  

        def setUp(self):
            self.request = HttpRequest()
            self.request.POST['text'] = 'new list item'  

        def test_passes_POST_data_to_NewListForm(self, mockNewListForm):
            new_list2(self.request)
            mockNewListForm.assert_called_once_with(data=self.request.POST)

### Patching a redirect

**patch decorators are applied innermost first**

    @patch('lists.views.redirect')
    def test_redirects_to_form_returned_object_if_form_valid(
        self, mock_redirect, mockNewListForm
    ):
        mock_form = mockNewListForm.return_value
        mock_form.is_valid.return_value = True

        response = new_list2(self.request)

        # Ensure response is result of redriect function
        self.assertEqual(
            response,
            mock_redirect.return_value
        )

        # Ensure redirect called with object we return from save
        mock_redirect.assert_called_once_with(mock_form.save.return_value)

### Patching a render

    @patch('lists.views.render')
    def test_renders_home_template_with_form_if_form_invalid(
        self, mock_render, mockNewListForm
    ):
        mock_form = mockNewListForm
        mock_form.is_valid.return_value = False

        response = new_list2(self.request)

        self.assertEqual(response, mock_render.return_value)
        mock_render.assert_called_once_with(
            self.request, 'home.html', {'form': mock_form}
        )

### A horrendous form test

    @patch('lists.models.List')
    @patch('list.models.Item')
    def test_save_creates_new_list_and_item_from_post_data(
        self, mockItem, mockList
    ):
        mock_item = mockItem.return_value
        mock_list = mockList.return_value
        user = Mock()

        form = NewListForm(data={'text': 'My New Item'})
        # populate cleaned_data
        form.is_valid()

        def check_item_text_and_list():
            self.assertEqual(mock_item.text, 'My New Item')
            self.assertEqual(mock_item.list, mock_list)
            self.assertTrue(mock_ist.save.called)
        mock_item.save.side_effect = check_item_text_and_list

        form.save(owner=user)

        self.assertEqual(mock_item.save.called)

### Hiding ORM Code Behind Helper Methods

Many people try and limit the ORM methods in views and forms because it is easier to test.

Helper functions also help us express our domain logic more clearly.

compare:

    list_ = List()
    list_.save()
    item = Item()
    item.list = list_
    item.text = self.cleaned_data['text']
    item.save()

with:

    List.create_new(first_item_text=self.cleaned_data['text'])

This also includes read queries:

    Book.objects.filter(in_print=True, pub_date__lte=datetime.today())

instead of:

    Book.all_available_books()

We can give more descriptive names, making the code more readible and the application more loosely coupled.

### Model Layer

At the model layer the whole point is storing data in the database, so no longer need isolated tests and can use integrated tests.

The model helper method can be a static method:

    def create_new(self):
        pass

turns to:

    @staticmethod
    def create_new(first_item_text):
        list_ = List.objects.create()
        Item.objects.create(text=first_item_text, list=list_)

> Use in-memory (unsaved) model objects in your tests whenever you can; it makes your tests faster. 

An example of in-memory tests:

    def test_lists_can_have_owners(self):
        List(owner=User())

    def test_list_owner_optional(self):
        List().full_clean()

> Here’s an important lesson to learn about test isolation: it might help you to drive out good design for individual layers, but it won’t automatically verify the integration between your layers.

### Thinking of Interactions Between Layers as "Contracts"

A functional test would catch these thigns but they take a long time to run. 
Whenever we mock out the behaviour of one layer, we have to make a mental note that there is now an implicit contract between the layers, and that a mock on one layer should probably translate into a test at the layer below.

**Each contract should have a test in the lwoer layer**

Complexity should be your guide as to when to write isolated tests with mocks.

### Pros and cons of test types

Functional tests:

* Provide the best guarantee that your application really works correctly, from the point of view of the user
* Slower feedback cycle
* Don’t necessarily help you write clean code

Integrated tests (Reliant on ORM or test client)

* Quick to write
* easy to understand
* Warn you of any integration issues
* May not always drive good design (that’s up to you!)
* Slower than isolated tests

Isolated ("mocky") tests

* Most hard work
* Harder to read and understand
* Best ones for guiding you towards better design
* Run the fastest

# Continuous Integration (CI)

As our site grows, it takes longer and longer to run all of our functional tests. If this continues, the danger is that we’re going to stop bothering.

In day-to-day development, we can just run the FT that we’re working on at that time, and rely on the CI server to run all the tests automatically and let us know if we’ve broken anything accidentally. The unit tests should stay fast enough that we can keep running them every few seconds.

There is info about how to setup how jenkins instance for running functional and JS tests: http://www.obeythetestinggoat.com/book/chapter_CI.html

# Fast Tests, Slow Tests, and Hot Lava

> There is an argument that a true unit test should always be isolated, because it’s meant to test a single unit of software. If it touches the database, it can’t be a unit test. The database is hot lava!


