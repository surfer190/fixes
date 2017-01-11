# Django Best Practices

## Some Important Rules

### Keep it simple

> When building software projects, each piece of unnecessary complexity makes it harder to add new features and maintain old ones

### Fat Models, Utility Modules, Thin Views, Stupid Templates

Stay away from putting more logic in views and templates

### Start with Django by default

Forget custom modules, keep to standard django as far as possible

### Stay Aware of Django design philosophies

Check django's [https://docs.djangoproject.com/en/1.10/misc/design-philosophies/](design philosophy)

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

### Pep-8

[http://www.python.org/dev/peps/pep-0008/](The official python style)

There is a linter for your text editor

Also use flake8 for checking code quality and as part of CI

#### 79 Character limit

The 79 character limit should be adhered to on open source, 99 on closed project projects.

## Imports

Imports should be grouped:

1. Standard library imports
2. Related-third party imports (Imports from django, then those related to django)
3. Local app or library specific imports

### Use Explicit relative imports

With hardcoded imports, you can't just change the name of the app, you have to change all the imports as well.

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

```
# Don't do this models overrites the forms
from django.forms import CharField
from django.db.models import CharField
```

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

Also use underscores in template block names

# Development Setup

* Use the same db engine in all environemnts either: sqlite3, postgreSQL or mysql
* Use pip and virtualenv - toptip: use [https://virtualenvwrapper.readthedocs.io/en/latest/](virtualenvwrapper)
* Use vagrant or docker

## Recommended setup

- Top level repo root: `readme`, `gitignore`, `django project root`
- Second level: project root: `django project`
- Configuration root: `settings module`
