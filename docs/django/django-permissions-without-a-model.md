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
            codename='delete_domain_association',
            name='Can Delete Fortimail Domain Associations'
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


## Source

* [Stackoverflow: Can I use Django Permissions without defining a content type](https://stackoverflow.com/questions/13932774/how-can-i-use-django-permissions-without-defining-a-content-type-or-model)
* [Add a permission to a user](https://stackoverflow.com/questions/20361235/django-set-user-permissions-when-user-is-automatically-created)
