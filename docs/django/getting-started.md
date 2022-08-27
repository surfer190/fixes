---
author: ''
category: Django
date: '2020-06-14'
summary: ''
title: Django - Getting Started
---
## Django: Getting Started

### Create a project

1. Create a virtual env

    virtualenv -p python3.6 env
    source env/bin/activate

2. Install django

    pip install django

3. Create a project

    django-admin startproject learning_site

  Ensure `underscore` as it is a module name

The `learning_site` folder:

* is not an `app` but a `stub`
* holds the `settings.py`
* holds the `urls.py` = base urls
* `wysgi.py` is entry point to web server

### Run the server

    cd learning_site
    ./manage.py runserver

Go to the link it shows you

**Unapplied migrations** - ways to track db schema changes

`ctrl` + `c` to cancel serving

#### Run Migrations

    ./manage.py migration

Database is created automatically with `sqlite3` - which is good to play around with.
For live sites it is best to use `mysql`

### Hello World

Django is different in that it calls templates - `templates` and functions that return rendered templates - `views`

All `views` have to accept a `request` object

`views.py`:

    from django.http import HttpResponse

    def hello_world(request):
        return HttpResponse('Hello World')

* Some frameworks have implicit routing by function name
* Some functions lets you set route for function name
* Django URL's are created with regular expressions

To import from the current directory use `from . import views`

`urls.py`:

    from django.conf.urls import url
    from django.contrib import admin

    from . import views

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', views.hello_world),
    ]

## Pluggable Apps

* Apps - self contained bit of functionality
* Pluggable - django apps that can be moved

### Create an app

It is a good idea to name the app after it's main model

    ./manage.py startapp courses

`__init__.py` mark a directory as a module

Add the `courses` to `INSTALLED APPS` in `settings.py` 
