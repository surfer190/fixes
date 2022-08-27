---
author: ''
category: Django
date: '2019-09-23'
summary: ''
title: Django Permissions Without A Model
---
# Django Permissions without a Model

Sometimes you will have a case where you need to add [django permissions](https://docs.djangoproject.com/en/2.2/topics/auth/default/#permissions) for reasons.
However when your API is used to call other API's then there won't be a model.
In that case you might want to create a dummy model - via a dummy ContentType.

You might also want to create the content type and permission in a migration.

Create an [empty migrations](https://docs.djangoproject.com/en/3.1/topics/migrations/#data-migrations) with:

    ./manage.py makemigrations --empty yourappname

Then in `<your_migration>.py`:

    from django.db import migrations


    def create_permission_class(apps, schema_editor):
        Permission = apps.get_model("auth", "Permission")
        ContentType = apps.get_model("contenttypes", "ContentType")
        db_alias = schema_editor.connection.alias
        my_content_type = ContentType.objects.using(db_alias).create(
            app_label='my_content_type',
            model='test'
        )
        create_car = Permission.objects.using(db_alias).create(
            codename='create_car',
            name='Create car',
            content_type=my_content_type
        )


    def delete_permission_class(apps, schema_editor):
        Permission = apps.get_model("auth", "Permission")
        ContentType = apps.get_model("contenttypes", "ContentType")
        db_alias = schema_editor.connection.alias
        Permission.objects.using(db_alias).filter(
            codename='create_car',
            name='Create car'
        ).delete()
        ContentType.objects.using(db_alias).filter(
            app_label='my_content_type',
            model='test'
        ).delete()


    class Migration(migrations.Migration):

        dependencies = [
        ]

        operations = [
            migrations.RunPython(create_permission_class, delete_permission_class),
        ]

### Protecting a Django Rest Framework View with your Permission

We want to use `permissions.DjangoModelPermissions` however, since there is no backing model we will need to inherit from this class and change the `perms_map` setting and also change the `queryset` on the view.

What `perms_map` looks like originally:

    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

First create the permission class:

    from rest_framework.permissions import DjangoModelPermissions

    class CreateCarModelPermissions(DjangoModelPermissions):
        perms_map = {
            'POST': ['my_content_type.create_car'],
        }

        authenticated_users_only = True

Set the view to use a [sentinel queryset](https://www.django-rest-framework.org/api-guide/permissions/#using-with-views-that-do-not-include-a-queryset-attribute).
Also use the permission class you just created.

    queryset = User.objects.none()

Now your permissions should work - remember to give the user the permission.

## Source

* [Stackoverflow: Can I use Django Permissions without defining a content type](https://stackoverflow.com/questions/13932774/how-can-i-use-django-permissions-without-defining-a-content-type-or-model)
* [Add a permission to a user](https://stackoverflow.com/questions/20361235/django-set-user-permissions-when-user-is-automatically-created)
