---
author: ''
category: Django
date: '2017-10-02'
summary: ''
title: Django Testing Admin
---
# Django Testing Admin

The admin section of django is part of your site too. Why should it not be tested?

> Every part of your site should be able to be tested

## Authenticating

1. Create a file called `test/test_admin.py` in your test folder that is a module (ie. it has a `__init__.py`)

2. Create the test class, create a super user and [log the user in](https://docs.djangoproject.com/en/1.11/topics/testing/tools/#django.test.Client.login)

        class PasswordChangeTests(TestCase):
            '''Check that changing the password on admin side works
            '''
            def setUp(self):
                self.super_user = get_user_model().objects.create_superuser(
                    email='testsuper@testsuper.co.za',
                    password='1234test'
                )
                self.client.login(
                    username='testsuper@testsuper.co.za',
                    password='1234test'
                )

3. Now how do we get anywhere, well we need to know the [names of urls to reverse](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#admin-reverse-urls) in the docs but we can find this in the `django.contrib.auth` package as well

4. Use the `reverse` method to test the response

        def test_password_change_link_exists(self):
            '''Test on the user change page a password change button exists
            '''
            response = self.client.get(
                reverse(
                    'admin:users_user_change',
                    args=(self.super_user.id,)
                )
            )
            self.assertContains(response, 'Change user')
            self.assertContains(
                response, 
                "Raw passwords are not stored, "
                "so there is no way to see this user's password,"
                " but you can change the password using this form."
            )

5. The imports needed are

        from django.test import TestCase
        from django.contrib.auth import get_user_model
        from django.core.urlresolvers import reverse
