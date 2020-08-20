---
author: ''
category: Django
date: '2016-03-21'
summary: ''
title: Django Shell
---
# Using the Django Shell

The django shell is similar to the python shell and lets you test out pieces of code in the interpreter.

The django shell just loads django and all your models and settings as well.

#### Opening the shell

  python manage.py shell

#### Working with models

Import the model

  from App.models import ModelName

Get all records

  ModelName.objects.all()

This returns an empty queryset: `[]`

It looks like a list but is really a queryset

  type(ModelName.objects.all())

Create a new Model

  # Create model and set fields
  m = ModelName()
  m.title = "Setting Title"
  m.description = "The Description"
  m.save()

Can also be done in a single step

  ModelName(title="Setting Title", description="The Description").save()

But you can do this in a single step and return the saved instance (object)

  m = ModelName.objects.create(title="Set Another Title", description="hello")
