---
author: ''
category: Django
date: '2017-11-07'
summary: ''
title: Must Have Python And Django Libraries
---
# Must have python and django libraries

## Python

### Interactive Python Debugger (Ipdb)

        pip install ipdb

## Django

### Django Debug Toolbar

        pip install django-debug-toolbar

### Django Extensions

[Django extensions](https://github.com/django-extensions/django-extensions)

        pip install django-extensions

### Dependent dropdowns

Dependent dynamic dropdowns for admin and frontend:

[Django Smart Selects](https://github.com/digi604/django-smart-selects)

Remember if you aren't getting expected results, then insepect the ajax request with developer tools and get decent error messages which will help you correct.

Also keep in mind that the selects are globally accessible so if you want to protect them you may want to use []django-decorrator-incldue(https://github.com/twidi/django-decorator-include) and have the incldued urls decorated with a `login_required`

