---
author: ''
category: Django
date: '2017-07-19'
summary: ''
title: Django Models
---
# Django models

Model names should be **singular**

It is a class inheriting from `django.db.models.model`

`models.py`:

    from django.db import models

    class Course(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        title = models.CharField(max_length=255)
        description = models.TextField()

## Attributes

Adding attributes to our class adds columns to our table

## Migrate

After adding the model columns you need to migrate

    ./manage.py makemigrations
    ./manage.py migrate

## Exploring the model

Enter the shell

    >>> from courses.models import Course
    # Get all instances
    >>> Course.objects.all()
    # Get an empty querySet
    >>> c = Course()
    >>> c.title = 'Python basics'
    >>> c.description = 'Learn the basics of Python'
    >>> c.save()
    >>> Course.objects.all()

    or

    >>> Course(title="hello", description="hello").save()

    or

    >>> Course.objects.create(title="Hello", description="Learn about classes")


## Sting representation

You can specify how django prints out the reference to the model instance

Using dunder str: `def __str__(self):`

Eg.

  def __str__(self):
    return self.title

## Find all model records

    Course.objects.all()

## Adding a foreign key

    field_name = models.ForeignKey(Modelname)

If the asscoated model comes after the model declaration it must be in quotes

Example:

    writer = models.ForeignKey('Writer')

    course = models.ForeignKey(Course)