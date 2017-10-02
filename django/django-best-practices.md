# Django Best Practices

## Some Important Rules

### Keep it simple

> When building software projects, each piece of unnecessary complexity makes it harder to add new features and maintain old ones

> Simplicity is the ultimate sophistication - Leonardo Da Vinci

### Fat Models, Utility Modules, Thin Views, Stupid Templates

Stay away from putting more logic in views and templates

### Start with Django by default

Forget custom modules, keep to standard django as far as possible

### Stay Aware of Django design philosophies

Check django's [design philosophy](https://docs.djangoproject.com/en/1.11/misc/design-philosophies/)

### 12 Factor App

Be aware and implement [https://12factor.net/](The 12 factor app)

## Source

[https://www.twoscoopspress.com/](2 scoops of django)

## Coding Style

### Make your code readable

Readable code is easier to maintain.

* avoid abbreviating variable names
* Write out function argument names
* Document your classes and methods
* comment code
* refactor repeated code into reusable functions
* keep functions short, you shouldn't need to scroll

Shortcuts come at the expense of hours of technical debt

Write out the entire variable name `balance_sheet_decrease` instead of `bsd`

### Pep-8

[The official python style](http://www.python.org/dev/peps/pep-0008/)

There is a linter for your text editor

Also use flake8 for checking code quality and as part of CI

#### 79 Character limit

The 79 character limit should be adhered to on open source, 99 on closed project projects.

## Imports

Imports should be grouped in this **order**:

1. Standard library imports
2. Related-third party imports (Imports from django, then those related to django)
3. Local app or library specific imports

### Use Explicit relative imports

With hardcoded imports, you **can't just change the name of the app**, you have to change all the imports as well.

It also helps to tell global imports from local imports

```
# Use this relative import
from .models import WaffleCone

# Instead of
from cones.models import WaffleCone
```

### Avoid using import *

```
# Use
from django import forms

# Instead of
from django.forms import *
```

because there can be naming collisions like:

        # Don't do this models overrites the forms
        from django.forms import CharField
        from django.db.models import CharField

to overcome naming collisions you can use `as`

        from django.db.models import CharField as ModelCharField 
        from django.forms import CharField as FormCharField

## Django coding Style

### Use django style guide

[https://docs.djangoproject.com/en/1.10/internals/contributing/writing-code/coding-style/](Django style guide)

### Use underscore in url() name

```
# wrong
name='add-topping'
# correct
name='add_topping'
```

        url(
            regex='^add/$',
            view=views.add_topping,
            name='add_topping'
        ),

Also use underscores in template block names ie. `content_block`

### Choose a Javascript or HTML style guide

* [Standard Javascript style guide](https://github.com/standard/standard)
* [Idiomatic css style guide](https://github.com/necolas/idiomatic-css)

### Never Code to the IDE or Text Editor

**Never code to the IDE or Text Editor**

# Development Setup

* Use the same db engine in all environments everywhere
* Fixtures are not a reliable tool for moving data from different environments, they are fine to use for basic data with `loaddata` and `dumpdata` though.
* Dob't use `sqlite3` with `django` in production
* Use pip and virtualenv - toptip: use [https://virtualenvwrapper.readthedocs.io/en/latest/](virtualenvwrapper), unfortunately I have found it quite difficult to set up.

Instead of typing something like

        source Users/suefer190/projects/my-project/env/bin/activate

You can simply type

        workon my-project

* Install django with `pip` and use `requirement` files
* Eliminate differences between environments


        * Operating system differences - windows, osX, ubuntu
        * Python setup differences - python version
        * developer setup differences

# How to Layout Django Projects

Use [Cookie Cutter](http://cookiecutter-django.readthedocs.io/en/latest/index.html) as a reference

## Recommended setup

- Top level repo root: `readme.md`, `gitignore`, `requirements.txt`
- Second level: project root: `django project`
- Configuration root: `settings module`

# Django App Design Fundementals

> Write apps that do one thing and do it well

Each app should be tightly focused on its task
It should be explained in a simple sentence (with not many `ands...`)

### Naming your Apps

Your app's name should be the `plural` form of the app's main model: `flavours`, `animals`, `polls`, `dreams`

There are many exceptions: `blog` being one

Also be aware of the `url` so that it seperates which part of the site

**When in doubt, keep apps small**

#### Uncommon App Modules

* `api/` - A package for isolating various modules when creating an API
* `behaviours.py` - Option for locating model mixins
* `constants.py` - App level settings, if there are enough of them
* `decorators.py` - Where we locate decorators
* `db/` - custom db fields or components
* `fields.py` - used for form fields, sometimes for model fields when not enough code for full `db` package
* `factories.py` - where we create test data factories
* `helpers.py`- helper functions
* `managers.py` - Move custom model managers to this module
* `signals.py` - custom signals (argued against)
* `utils.py` - same as `helpers`
* `viewmixins.py` - view modules can be thinned by putting view mixings here

## Settings

* All settings should be version controlled
* Don't repeat yourself - inherit from a base settings file
* Keep secret keys safe, outside version control

Don't use the `local_settings.py` as it can cause headaches

Instead of having a single `settings.py` file, use multiple files in the `settings/` directory

* `base.py`
* `local.py`
* `staging.py`
* `test.py`
* `production.py`

Each settings module should have its own `requirements` file

        python manage.py runserver --settings=twoscoops.settings.local

Specify the settings file to use

Rather make use of environment settings

## Models

> Don't rush into creating models

If an app has more than 20 models, it should be broken down into smaller apps

Avoid multi-table inheritance

### The TimeStamed Model

Adds a `created` and `modified` fields for all models, as an abstract class.

No seperate tables are created. The fields are merely added to the new models.

        from django.db import models

        class TimeStampedModel(models.Model):
                """
                An abstract base class model that provides self-
                updating ``created`` and ``modified`` fields
                """
                created = models.DateTimeField(auto_now_add=True)
                modified = models.DateTimeField(auto_now=True)

                class Meta:
                        abstract = True

Usage:

        from django.db import models
        from core.models import TimeStampedModel

        class Flavour(TimeStampedModel):
                title = models.CharField(max_length=200)

### Migrations

Make a new migration after each new model

Always put data migration code into version control

Stay normalised and use caching, try and avoid denormalisation asmuch as possible

#### Null and Blank

When to use `null=True` and `blank=True`

`FileField` and `ImageField` use `blank`

`BooleanField`, use `NullBooleanField`

