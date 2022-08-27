---
author: ''
category: Django
date: '2017-11-06'
summary: ''
title: Django Migrations
---
# Django Migrations

## The workflow

1. Create the model class in `models.py`

2. Make sure the `app` is added to `INSTALLED_APPS`

3. Create the migration files

    ./manage.py makemigrations

4. Run the Migration

    ./manage.py migrate

## RunPython

RunPython is a way to initialise data or run operations during migrations.
They are tightly coupled with migrations and can be viewed here: [RunPython docs](https://docs.djangoproject.com/en/1.11/ref/migration-operations/#runpython)

## Reversing all migrations to Zero

    ./manage.py migrate <app_name> zero

## Unapplying migrations

Say for example you are playing around with the model and make multiple changes and multiple migrations before deciding on the correct way.

You will probably see something like this in `git`:

    Untracked files:
    (use "git add <file>..." to include in what will be committed)

            entries/migrations/0006_auto_20171106_0930.py
            entries/migrations/0007_auto_20171106_0938.py
            entries/migrations/0008_auto_20171106_0939.py
            entries/migrations/0009_auto_20171106_1004.py

Now you want to remove these testing migrations and just apply a single one.

It can be done by unapplying migrations to a specific version with:

    ./manage.py migrate <app_name> <migration_name>
    ./manage.py migrate entries 0005_auto_20171103_1341

You can then delete the migrations and create a single one afresh with:

    ./manage.py makemigrations
    ./manage.py migrate

### Sources

* [Reverting last migration](https://stackoverflow.com/questions/32123477/django-revert-last-migration)
* [Undoing Migreations](https://stackoverflow.com/questions/43267339/theres-a-way-to-undo-a-migration-on-django-and-uncheck-it-from-the-list-of-show)
