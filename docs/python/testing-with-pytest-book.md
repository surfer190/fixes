---
author: ''
category: Python
date: '2023-01-15'
summary: ''
title: Testing with Pytest
---

# Testing with Pytest

Pytest is a software testing framework.

Arguments for:

* Simple to write tests
* Tests are easy to read
* tests are verified with the single `assert` keyword
* Use for tests written for `nose` and `unittest`

## 1. Getting Started

: `test_one.py`:

    def test_passing():
        assert (1, 2, 3) == (1, 2, 3)

* It is discovered because the function starts with `test_` and the file name starts with `test_`
* `assert` keyword determines if the test passes or not - an `AssertionError` is raised if it does not

Install pytest:

    pip install pytest

Running tests:

    pytest
    pytest test_one.py

Results:

    $ pytest 1/test_one.py 
    ============================= test session starts ==============================
    platform darwin -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
    rootdir: /Users/stephen/projects/pytest_book
    collected 1 item                                                               

    1/test_one.py .                                                          [100%]

    ============================== 1 passed in 0.00s ===============================

* The `.` means a test passed

For more info you can use the verbose flag `-v`:

    1/test_one.py::test_passing PASSED                                       [100%]

A failing test:

    def test_failing():
        assert (1, 2, 3) == (3, 2, 1)

Results:

    1/test_two.py F                                                          [100%]

    =================================== FAILURES ===================================
    _________________________________ test_failing _________________________________

        def test_failing():
    >       assert (1, 2, 3) == (3, 2, 1)
    E       assert (1, 2, 3) == (3, 2, 1)
    E         At index 0 diff: 1 != 3
    E         Use -v to get more diff

    1/test_two.py:2: AssertionError
    =========================== short test summary info ============================
    FAILED 1/test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
    ============================== 1 failed in 0.03s ===============================

* `pytest` tells you wy it fails - `index 0` is not a match

Verbose gives more info:

        def test_failing():
    >       assert (1, 2, 3) == (3, 2, 1)
    E       assert (1, 2, 3) == (3, 2, 1)
    E         At index 0 diff: 1 != 3
    E         Full diff:
    E         - (3, 2, 1)
    E         ?  ^     ^
    E         + (1, 2, 3)
    E         ?  ^     ^

* Carets `^` are added to show exactly where the problem is

> If you don’t specify any files or directories, pytest will look for tests in the current working directory and subdirectories. It looks for `.py` files starting with `test_` or ending with `_test`.

Turning off traceback: `--tb=no`

    pytest --tb=no

same as:

    pytest --tb=no 1/test_one.py 1/test_two.py 

Results in:

    1/test_one.py .                                                          [ 50%]
    1/test_two.py F                                                          [100%]

specify a test file to run by adding `::test_name`:

Eg.

    pytest​​ ​​-v​​ ​​1/test_one.py::test_passing

### Test Discovery

* test methods or functions should be names `test_*`
* test classes should be named `Test*`
* test files should be name `test_*.py` or `*_test.py`

### Test Outcomes

* PASSED `.`
* FAILED `F`
* SKIPPED `s`
* XFAILED `x` - test was not supposed to pass
* XPASS `X` - marked as xfail but it passed
* ERROR `E` - exception happened during hook or fixture - not during the execution of a test function

## 2. Writing Test Functions

We will be testing the `cards` python package

To install the package with the local source code:

    pip install ./cards_proj/

The `cards` command line script will now be available

    cards

Try it out:

    cards add make tea --owner fixes
    cards add meditate

View cards:

    $ cards
                                    
    ID   state   owner   summary   
    ─────────────────────────────── 
    1    todo    fixes   make tea  
    2    todo            meditate 

Change status:

    cards start 1
    cards start 2
    cards finish 1

    ID   state     owner   summary   
    ───────────────────────────────── 
    1    done      fixes   make tea  
    2    in prog           meditate  

Delete:

    cards delete 1

    ID   state     owner   summary   
    ───────────────────────────────── 
    2    in prog           meditate  

### Knowledge Building Tests

3 layers:

* CLI - command line interface
* API - application programmable interface
* DB - database

The `Card` [dataclass](https://docs.python.org/3/library/dataclasses.html):

    @dataclass
    class Card:
        summary: str = None
        owner: str = None
        state: str = "todo"
        id: int = field(default=None, compare=False)

        @classmethod
        def from_dict(cls, d):
            return Card(**d)
            
        def to_dict(self):
            return asdict(self)

> When faced with a new data structure, it’s often helpful to write some quick tests so that you can understand how the data structure works.

These tests are exploratory tests - no checking for failure cases:

    from cards.api import Card

    def test_field_access():
        my_card = Card(
            summary='Buy clothers', owner='HappyCheppy', state='todo', id=123
        )
        assert my_card.summary == 'Buy clothers'
        assert my_card.owner == 'HappyCheppy'
        assert my_card.state == 'todo'

    def test_card_defaults():
        my_card = Card()
        assert my_card.summary == None
        assert my_card.owner == None
        assert my_card.state == 'todo'
        assert my_card.id == None

    def test_card_equality_diff_ids():
        my_card = Card('buy', 'Harry', 'todo', 100)
        other_card = Card('buy', 'Harry', 'todo', 101)
        assert my_card == other_card

    def test_inequality():
        my_card = Card('sell', 'Heppy', 'todo', 100)
        other_card = Card('sell', 'Harold', 'todo', 101)
        assert my_card != other_card

    def test_from_dict():
        my_card = Card.from_dict({
            'summary': "Yello World",
            'owner': "Bob",
            'state': "todo",
            "id": 1000
        })
        assert my_card == Card(
            summary="Yello World",
            owner="Bob",
            state="todo",
            id=1000
        )
        
    def test_to_dict():
        my_card = Card(
            summary="Yello World",
            owner="Bob",
            state="todo",
            id=1000
        )
        assert my_card.to_dict() == {
            'summary': 'Yello World',
            'owner': 'Bob',
            'state': 'todo',
            'id': 1000
        }

### Using Assert Statements

In pytest `assert` is your primary tool.

Comparing with `unittest`:

* `assertTrue(something)` is now `assert something`
* `assertFalse(something)` is now `assert not something`
* `assertEqual(a, b)` is now `assert a == b`
* `assertNotEqual(a, b)` is now `assert a != b`
* `assertIsNone(a)` is now `assert a is None`
* `assertIsNotNone(a)` is now `assert a is not None`
* `assertLessEqual(a, b)` is now `assert a <= b`

Failure output can be very specific:

        def test_equality_fail():
            card1 = Card('Something', 'owner')
            card2 = Card('Chappies', 'mark')
    >       assert card1 == card2
    E       AssertionError: assert Card(summary=...odo', id=None) == Card(summary=...odo', id=None)
    E         
    E         Omitting 1 identical items, use -vv to show
    E         Differing attributes:
    E         ['summary', 'owner']

Running it with `-vvv`:

        def test_equality_fail():
            card1 = Card('Something', 'owner')
            card2 = Card('Chappies', 'mark')
    >       assert card1 == card2
    E       AssertionError: assert Card(summary='Something', owner='owner', state='todo', id=None) == Card(summary='Chappies', owner='mark', state='todo', id=None)
    E         
    E         Matching attributes:
    E         ['state']
    E         Differing attributes:
    E         ['summary', 'owner']
    E         
    E         Drill down into differing attribute summary:
    E           summary: 'Something' != 'Chappies'
    E           - Chappies
    E           + Something
    E         
    E         Drill down into differing attribute owner:
    E           owner: 'owner' != 'mark'
    E           - mark
    E           + owner

### Skip and Fail Tests

    import pytest

    def test_fail_me():
        pytest.fail()

    def test_skip_me():
        pytest.skip()

With messages:

    def test_fail_me():
        pytest.fail('Failing this one!')

    def test_skip_me():
        pytest.skip('Got to skip!')

Output:

    2/test_card_fail.py::test_equality_fail FAILED                                                                                        [ 33%]
    2/test_card_fail.py::test_fail_me FAILED                                                                                              [ 66%]
    2/test_card_fail.py::test_skip_me SKIPPED (Got to skip!)   

    E       Failed: Failing this one!

### Assertion Helper

For complex assertions that are reused...

    from cards import Card
    import pytest

    def assert_identical(c1: Card, c2: Card):
        __tracebackhide__ = True
        assert c1 == c2
        if c1.id != c2.id:
            pytest.fail(f"id's don't match. {c1.id} != {c2.id}")

    def test_identical():
        c1 = Card("foo", id=123)
        c2 = Card("foo", id=123)
        assert_identical(c1, c2)

### Testing Expected Excpetions

Use `pytest.raises()`

Say there is this test:

    import cards

    def test_no_path_fail():
        cards.CardsDB()

Which raises:

    _____________________________________________________________ test_no_path_fail _____________________________________________________________
    2/test_experiment.py:4: in test_no_path_fail
        cards.CardsDB()
    E   TypeError: CardsDB.__init__() missing 1 required positional argument: 'db_path'

This is an expected and reasonable error that we want to ensure is raised:

    import cards

    def test_no_path_raises_typerror():
        with pytest.raises(TypeError):
            cards.CardsDB()

If we want to catch the message:

    def test_no_path_raises_typerror_match_regex():
        match_text = "missing 1 .* positional argument"
        with pytest.raises(TypeError, match=match_text):
            cards.CardsDB()

    def test_no_path_raises_typerror_mwith_info_alt():
        with pytest.raises(TypeError) as exc_info:
            cards.CardsDB()
        expected = 'missing 1 required positional argument'
        assert expected in str(exc_info.value)

> `exc_info` will be of type [`ExceptionInfo`](https://docs.pytest.org/en/latest/reference/reference.html#exceptioninfo)

### Structuring Test Functions

Keep asserts at the end

1. Get ready to do something
2. Do something
3. Check if doing something was successful

> Harder to maintain when tests fails with asserts throughout - not clear exactly where it failed

### Grouping Tests with Classes

Example:

    from cards.api import Card

    class TestEquality:
        def test_equality(self):
            c1 = Card("something", "heppy", "todo", 1)
            c2 = Card("something", "heppy", "todo", 1)
            assert c1 == c2
        
        def test_equality_with_diff_ids(self):
            c1 = Card("something", "heppy", "todo", 123)
            c2 = Card("something", "heppy", "todo", 456)
            assert c1 == c2

        def test_inequality(self):
            c1 = Card("something new", "heppy", "todo", 123)
            c2 = Card("something", "heppy", "todo", 456)
            assert c1 != c2

Run tests of the class:

    pytest --tb=short 2/test_classes.py::TestEquality

Run tests of a single method of the class:

    pytest --tb=short 2/test_classes.py::TestEquality::test_inequality

## 3. Pytest Fixtures

Functions run before and after test functions.
Pytest's equivalent of `setUp` and `tearDown` of `unittest`.

Used to set up data and prepare a state for tests.

`@pytest.fixture()` decorator is used to tell pytest that a function is a decorator.

The name of the fixture is then used as a parameter of the test function - telling pytest to use it for this test.

An exception in a fixture is reported as `E` - an error. An exception during test code is reported as `F` - failure.

Example:

    import pytest

    @pytest.fixture()
    def some_data():
        return 42

    def test_dome_data(some_data):
        assert some_data == 42

### setUp and tearDown

Dealing with the database is where fixtures help a lot.

Example:

    import pathlib
    from tempfile import TemporaryDirectory
    import cards

    def test_empty():
        with TemporaryDirectory() as db_dir:
            db_path = pathlib.Path(db_dir)
            db = cards.CardsDB(db_path)
            count = db.count()
            db.close()
            
            assert count == 0

The problem here is that the database close must happen before the assert otherwise - the db conneciton will not be closed.

This can be fixed with:

    @pytest.fixture()
    def cards_db():
        with TemporaryDirectory() as db_dir:
            db_path = pathlib.Path(db_dir)
            db = cards.CardsDB(db_path)
            yield db
            db.close()

    def test_empty(cards_db):
        assert cards_db.count() == 0

* The test function is easier to read
* The `yield` part is where the tests run
* The database is setUp before the test and closed after it (tearDown)
* Fixture can be reused
* Make sure to name your test correctly

> We never call fixture functions directly. pytest does that for us. With the name of the fixture in the parameter.

### Tracing Fixture Execution with -setup-show

See what is executed when with `--setup-show`

    pytest --setup-show 3/test_count.py

Results in:

    3/test_count.py 
            SETUP    F cards_db
            3/test_count.py::test_empty (fixtures used: cards_db).
            TEARDOWN F cards_db
            SETUP    F cards_db
            3/test_count.py::test_two (fixtures used: cards_db).
            TEARDOWN F cards_db

* The `F` indicates that the fixture is using the function scope - meaning the fixture is called before and torn down after each test that uses it.

### Specifying Scope

* Scope specifies when the setup and teardown runs relative to the test running the fixture.
* Default scope is the function scope

Say a database setup is slow - we may want the setup to only happen once for all tests in a module.
In which case the _module_ scope is used.

    @pytest.fixture(scope=​"module"​)

Scopes:

* `function` - Once per test function
* `class` - Once per test class
* `module` - Once per test file (module)
* `package` - Once per package or test directory
* `session` - Once per session - all tests share the same setup and teardown.

> Scope is set at the definition of the fixture

The `session` and `package` scope must be put in a `conftest.py` file.

### Sharing Fixtures through Conftest.py

* A `conftest.py` file is needed to share fixtures between files.
* It is considered a local plugin

In `conftest.py`:

    import pathlib
    from tempfile import TemporaryDirectory

    import pytest

    import cards

    @pytest.fixture(scope="session")
    def cards_db():
        with TemporaryDirectory() as db_dir:
            db_path = pathlib.Path(db_dir)
            db = cards.CardsDB(db_path)
            yield db
            db.close()

Then in `test_count.py`:

    import cards

    def test_empty(cards_db):
        assert cards_db.count() == 0

    def test_two(cards_db):
        cards_db.add_card(cards.Card("first"))
        cards_db.add_card(cards.Card("second"))
        assert cards_db.count() == 2

* Fixtures can only depend on other fixtures of same or greater scope
* Don't import `conftest.py` it is meant to be read automatically
* There can be a `conftest.py` at every level of a test directory

### Finding where Fixtures are defined

    pytest --fixtures
    
or

    pytest --fixtures -v

* Fixtures defined by conftest are at the bottom

To check fixtures per test:

    pytest​​ ​​--fixtures-per-test​​ ​​test_count.py::test_empty

### Multiple Fixture Levels

> tests shouldn’t rely on the run order

Sometimes the database has elements added and is not cleaned up. Need to be smart .

A child fixture can be used to set state on a lesser scope

    @pytest.fixture(scope=​"session"​)
    ​def​ ​db​():
    ​    ​"""CardsDB object connected to a temporary database"""​
    ​    ​with​ TemporaryDirectory() ​as​ db_dir:
    ​        db_path = Path(db_dir)
            db_ = cards.CardsDB(db_path)
    ​        ​yield​ db_
    ​        db_.close()

    ​@pytest.fixture(scope=​"function"​)
    ​​def​ ​cards_db​(db):
        ​"""CardsDB object that's empty"""​
    ​    db.delete_all()
        ​return​ db

### Using Multiple Fixtures per Test

In `conftest.py`:

    import pytest

    import cards

    @pytest.fixture(scope='session')
    def some_cards():
        return [
            cards.Card("write book", "fixes", "todo"),
            cards.Card("edit book", "Katie", "done"),
            cards.Card("run marathon", "random", "started")
        ]

In `test_multiple.py`:

    def test_add_some(cards_db, some_cards):
        expected_count = len(some_cards)
        for card in some_cards:
            cards_db.add_card(card)
        assert cards_db.count() == expected_count


> Fixtures can user multiple other fixtures

### Dynamically deciding fixture scope

A callable can be given to the `fixture` decorator's `scope` parameter

Eg.

    @pytest.fixture(scope=db_scope)
    def abc():
        ...
    
    def db_scope(fixture_name, config):
        if fixture.getoption('--func-db', None)
            return 'function'
        return 'session'

> The `--func-db` option is made available through a hook function

    def pytest_addoption(parser):
        parser.addoption(
            '--func-db',
            action='store_true',
            default=False,
            help='new db for each test'
        )

### Autouser for Fixtures that always get used

When defining a fixture set `autouse=True` to get a fixture to run all the time.

    import time

    import pytest

    @pytest.fixture(autouse=True, scope='function')
    def footer_time_function():
        '''
        Report time at end of the session
        '''
        start = time.time()
        yield
        end = time.time()
        print(f'Took: {end-start:.2f} seconds')

    def test_slow():
        time.sleep(2)

    def test_fast():
        time.sleep(0.2)

To get the standard out use the `-s` flag or `--capture=no`

    $ pytest -v -s test_autouse.py 

    test_autouse.py::test_slow PASSED
    Took: 2.01 seconds

    test_autouse.py::test_fast PASSED
    Took: 0.20 seconds

> Explicit is better than implicit - so use sparingly

### Renaming Fixtures
    
    @pytest.fixture(name="ultimate_answer")
    def my_ultimate_answer_fixture():
        ...
    
    def test_hello(ultimate_answer):
        ...

## 4. Builtin Fixtures

### Tmp_path and Tmp_path_factory

Read the fixture docstrings with: `pytest --fixtures -v`

* The `tmp_path` function-scope fixture returns a pathlib.Path instance that points to a temporary directory
* The `tmp_path_factory` session-scope fixture returns a TempPathFactory object.
* With `tmp_path_factory` you have to call `mktemp()`

> The base directory for all of the pytest temporary directory fixtures is system- and user-dependent, and includes a pytest-NUM part, where NUM is incremented for every session

Eg.

    def test_tmp_path(tmp_path):
        file = tmp_path / "file.txt"
        file.write_text("Hello")
        assert file.read_text() == "Hello"

    def test_tmp_path_factory(tmp_path_factory):
        path = tmp_path_factory.mktemp("sub")
        file = path / "file.txt"
        file.write_text("Hello")
        assert file.read_text() == "Hello"

### Using capsys

Sometimes application outputs to `stderr` or `stdout`

Example:

    $ cards version
    1.0.0

Or in a repl:

    >>> import cards
    >>> cards.__version__
    '1.0.0'

One way to test would be with a `subprocess.run()`:

    import subprocess

    import cards

    def test_version_v1():
        process = subprocess.run(
            ["cards", "version"], capture_output=True, text=True
        )
        output = process.stdout.rstrip()
        assert output == cards.__version__

Capsys version:

    import cards

    def test_version(capsys):
        cards.cli.version()
        output = capsys.readouterr().out.rstrip()
        assert output == cards.__version__

> `capsys.readouterr()` method returns a `namedtuple` that has `out` and `err`

To show stderr or stdout in test output one uses `-s` or `--capture=no`

One can also use `capsys.disabled()`:

    def test_normal(capsys):
        with capsys.disabled():
            print("\nhello world")

To test logging messages the [caplog](https://docs.pytest.org/en/7.1.x/how-to/logging.html#caplog-fixture) fixture can be used.

### Monkeypatch

The `typer` library used by `cards` provides a good testing util for cli:

    from typer.testing import CliRunner

    import cards

    def test_version_v3():
        runner = CliRunner()
        result = runner.invoke(cards.app, "version")
        output = result.output.rstrip()
        assert output == cards.__version__

A “monkey patch” or simply "Patch" is a dynamic modification of a class or module during runtime.

Cool thing about the fixture is it handles the setup and teardown for you - instead of having to manually handle it.

Now lets make it easier to run the other commands:

    from typer.testing import CliRunner

    import cards


    def run_command(*params):
        runner = CliRunner()
        result = runner.invoke(cards.app, params)
        return result.output.rstrip()


    def test_version():
        output = run_command("version")
        assert output == cards.__version__

In `cards_proj/src/cards/cli.py`:

    def get_path():
        db_path_env = os.getenv("CARDS_DB_DIR", "")
        if db_path_env:
            db_path = pathlib.Path(db_path_env)
        else:
            db_path = pathlib.Path.home() / "cards_db"
        return db_path

> We want to test get_path but don't want to set the env variable - so it can be monkey patched for the purpose of the test

    def test_get_path(tmp_path, monkeypatch):
        def get_fake_path():
            return tmp_path

        monkeypatch.setattr(cards.cli, "get_path", get_fake_path)
        assert run_command("config") == str(tmp_path)

This might break the head but we are setting the `cli.py` files function called `get_path` to the callable function `get_fake_path`. 

Monkey path has a few functions:

* `setattr(target, name, value, raising=True)` - sets an attribute
* `delattr(target, name, raising=True)` - deletes an attribute
* `setenv(name, value, prepend=None)` - set an environment variable
* `delenv(name, raising=True)` - delete an environment variable

> Design for testability

## 5. Parameterisation

Turning one test function into many test cases

3 ways:

* parameterising functions
* parameterising fixtures
* using a hook function called `pytest_generate_tests`

Testing the state of a task when running `finish()`:

    from cards import Card

    def test_finish_from_in_prog(cards_db):
        index = cards_db.add_card(Card("second edition", state="in prog"))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"

    def test_finish_from_done(cards_db):
        index = cards_db.add_card(Card("second edition", state="done"))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"

    def test_finish_from_todo(cards_db):
        index = cards_db.add_card(Card("second edition", state="todo"))
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"

Results:


    test_finish.py::test_finish_from_in_prog PASSED                                                                                        [ 33%]
    test_finish.py::test_finish_from_done PASSED                                                                                           [ 66%]
    test_finish.py::test_finish_from_todo PASSED   

One way to combine the above into a single test:

    def test_combined(cards_db):
        for card_status in ['todo', 'done', 'in prog']:
            index = cards_db.add_card(Card("second edition", state=card_status))
            cards_db.finish(index)
            card = cards_db.get_card(index)
            assert card.state == "done"

Results:

    test_combined.py::test_combined PASSED 

Problems:

* Only 1 test case reported
* If one test fails - unknown which one - needs further investigation
* If one test fails - the execution of other tests will not continue

### Parameterising Functions

> The pytest spelling is: `parametrize`

Use `@pytest.mark.parametrize()`

import pytest

    from cards import Card

    @pytest.mark.parametrize(
        "start_summary, start_state",
        [
            ("write a book", "done"),
            ("second edition", "in prog"),
            ("create course", "todo")
        ]
    )
    def test_finish(cards_db, start_summary, start_state):
        initial_card = Card(summary=start_summary, state=start_state)
        index = cards_db.add_card(initial_card)
        
        cards_db.finish(index)
        
        card = cards_db.get_card(index)
        assert card.state == "done"

Results:

    test_func_param.py::test_finish[write a book-done] PASSED                                                                              [ 33%]
    test_func_param.py::test_finish[second edition-in prog] PASSED                                                                         [ 66%]
    test_func_param.py::test_finish[create course-todo] PASSED                                                                             [100%]

* The first argument to `@pytest.mark.parametrize` is a list of names of parameters.
* The second argument is a list of test cases
* The first argument can be used as a fixture (in test function signature)

### Parameterising Fixtures

Shifting the parameterising to the fixture.
Every down stream test depending on the fixture is parameterised.

    import pytest

    from cards import Card

    @pytest.fixture(params=["done", "in prog", "todo"])
    def start_state(request):
        return request.param

    def test_finish(cards_db, start_state):
        initial_card = Card(summary="write a book", state=start_state)
        index = cards_db.add_card(initial_card)
        
        cards_db.finish(index)
        
        card = cards_db.get_card(index)
        assert card.state == "done"

* `start_state` is called 3 times, one for each param
* Each value is saved to `request.param`
* In each `start_state` some code could do modification and return the params
* Benefit is a fixture run for each argument


### Parameterisation with Pytest_generate_tests

Using a hook function `pytest_generate_tests`

    from cards import Card

    def pytest_generate_tests(metafunc):
        if "start_state" in metafunc.fixturenames:
            metafunc.parametrize("start_state", ["done", "in prog", "todo"])
        
    def test_finish(cards_db, start_state):
        initial_card = Card(summary="write a book", state=start_state)
        index = cards_db.add_card(initial_card)
        
        cards_db.finish(index)
        
        card = cards_db.get_card(index)
        assert card.state == "done"

### Running a Subset of Tests

Say we just wanted to test the `todo` case:

Use the `-k` option flag

    pytest -v -k todo

    test_finish.py::test_finish_from_todo PASSED                                                                                           [ 25%]
    test_func_param.py::test_finish[create course-todo] PASSED                                                                             [ 50%]
    test_gen.py::test_finish[todo] PASSED                                                                                                  [ 75%]
    test_para_fixture.py::test_finish[todo] PASSED

> Best to quote the parameter to not conflict with the shell

One can do something like this `pytest -v -k "not(in prog or todo)"`

## 6. Markers

A way to tell pytest there is something special about a test.

* `@pytest.mark.slow` - mark a test as slow and do not run when in a hurry
* `@pytest.mark.smoke` - early stage tests in the pipeline
* `@pytest.mark.parametrize` - used before to run with multiple parameters
* `@pytest.mark.filterwarnings(warning)` - warning filter to given test
* `@pytest.mark.skip(reason=None)` - skips a test with optional reason
* `@pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, strict=xfail_strict)` - expecting a test to fail

Examples in the book...

## 7. Strategy

### Determining Test Scope

More stuff in the book...

## 8. Configuration Files

Define how pytest runs.

> If you find yourself always using certain flags in your tests, like `--verbose` or `--strict-markers`, you can tuck those away in a config file and not have to type them all the time.

Files:

* `pytest.ini` - primary config file in the root directory of the tests
* `conftest.py` - fixtures and hook functions
* `tox.ini` - alternate to pytest.ini - `tox` is a cli testing tool
* `pyproject.toml` - used for packaging python projects
* `setup.cfg` - used for packaging

### Settings and Flags in Pytest.ini











## Source

* [Python Testing with pytest, Second Edition - Brian Okken](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/)