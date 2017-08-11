# Django ORM

## Recap

Using the `Course` model

### All records in database

    Course.objects.all()

### No records but an empty queryset

    Course.objects.none()

### Get a single course

    Course.get()

or

    get_object_or_404()

### Creating records

New Instance

    Course.create()

Save existing

    Course.save()

## Queryset

Queryset - collection of records returned from the database

* Anything that can return from a SQL query can be in a queryset
* They are lazy, they won't do the work until it is needed - they are in memory and don't hit the dtabase until they are consumed

### User Model

Useful but not required features are in `django.dontrib`

So `from django.contrib.auth.models import User`