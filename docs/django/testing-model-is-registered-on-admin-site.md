---
author: ''
category: Django
date: '2018-01-21'
summary: ''
title: Testing Model Is Registered On Admin Site
---
# Django - How to test a model is registered on the admin site

        from django.contrib import admin
        from django.test import TestCase

        from ..models import Account


        class ModelAdminTests(TestCase):

            def test_account_model_admin(self):
                '''Ensure the account is extended from model admin'''
                registry = admin.site._registry
                self.assertTrue(
                    isinstance(registry[Account], admin.ModelAdmin)
                )

# Source:

* [Daniel RoseMan Admin Answer](https://stackoverflow.com/questions/2955667/django-check-for-modeladmin-for-a-given-model)

