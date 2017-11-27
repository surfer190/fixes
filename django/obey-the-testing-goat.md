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

