---
author: ''
category: Python
date: '2019-07-16'
summary: ''
title: Pytest
---
# Pytest and a Summary of a Gentle Introduction to Pytest

* A test is code that executes code.
* You can define your requirements as code
* Documenting the implementation
* Continuously testing and ensuring it does not regress

## Test Cases

Say we want to validate email addresses with:

    def is_valid_email(email):
        ...

A test case would be an example:

    print(is_valid_email(happychappy@myorg.com))

Lets Install pytest and test or function...

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

### Test Cases

In `test_email.py`:

    from validators import is_valid_email_address

    def test_regular_email_validates():
        assert is_valid_email_address('test@example.org')
        assert is_valid_email_address('user123@subdomain.example.org')
        assert is_valid_email_address('john.doe@email.example.org')

    def test_valid_email_has_one_at_sign():
        assert not is_valid_email_address('john.doe')

    def test_valid_email_has_only_allowed_chars():
        assert not is_valid_email_address('john,doe@example.org')
        assert not is_valid_email_address('not valid@example.org')

Now run `pytest`

    $ pytest
    ================================================================= test session starts =================================================================
    platform darwin -- Python 3.9.9, pytest-7.1.0, pluggy-1.0.0
    collected 3 items                                                                                                                                     

    test_email.py ...                                                                                                                               [100%]

    ================================================================== 3 passed in 0.01s ==================================================================

Add a few more tests:

    def test_valid_email_can_have_plus_sign():
        assert is_valid_email_address('john.doe+abc@gmail.com')

    def test_valid_email_must_have_a_tld():
        assert not is_valid_email_address('john.doe@example')

> Remember `pytest` only uses assert there are no intense assertions like in `unittest`

> Writing tests first based on requirements it called `Test Driven Development`

### Fixtures

In django `fixtures` are a term used for intial data to be loaded into the db.
In pytest, fixtures refer to functions run before and after tests.

We can create these functions with the `@pytest.fixture()` decorator

    import pytest
    
    @pytest.fixture()
    def database_environment():
        setup_database()
        yield
        teardown_database()

* `yield` indicates where pytest runs the tests
* To use the fixture it must be added as an argument to the function

    def test_world(database_environment):
        assert 1 == 1

You can also get data from fixtures:

    import pytest

    @pytest.fixture()
    def my_fruit():
        return "apple"

    def test_fruit(my_fruit):
        assert my_fruit == "apple"

### Configuration Files

Pytest can read project specific config files:

* `pytest.ini`
* `tox.ini`
* `setup.cfg`

In `pytest.ini` and `tox.ini`:

    [pytest]
    addopts = ​-rsxX -l --tb=short --strict​

In `setup.cfg`:

    [tool:pytest]
    addopts = ​-rsxX -l --tb=short --strict​

There can be a file `conftest.py` shared between tests - for common fixtures.
It is also a good place to set the `PATH`, plugins and modifiers.

### CLI / PDB

#### Running a single test

    pytest test_validator.py::test_regular_email_validates

#### List all the tests

    pytest --collect-only

#### Exit on the first error

    pytest -x

#### Run the last failed test

    pytest --lf

#### Show value of local values in output

    pytest -l

#### Using Python Debugger (pdb)

> `pdb` is a command line debugger built into Python. You can pytest to debug your test function’s code.

To drop into `pdb` after an exception (not very useful):

    pytest --pdb

To begin a trace at the start of the last test that failed:

    pytest --lf --trace

## Sources

* [Bas Codes - Gentle introduction to pytest](https://bas.codes/posts/python-pytest-introduction)