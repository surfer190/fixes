# Django Signals

Well what are they? They are **hooks** that you can listen for in your application and do a specific task when they occur.

You can check the [Signal Docs](https://docs.djangoproject.com/en/1.11/topics/signals/) for a more detailed explanation

There are alot of [built-in signals](https://docs.djangoproject.com/en/1.11/ref/signals/)

## Using Signals Example with User Authentication Signals

In this example we will be catching the user logout signal with the `django.contrib.auth.signal.user_logged_out` and adding a django message

**NB First thing to do is make sure the app knows about the signals**

1. Create a `signals.py` file

2. You need to import your signals into `<app_label>/apps.py`

        from django.apps import AppConfig


        class UsersConfig(AppConfig):
            name = 'users'

            def ready(self):
                import users.signals

3. In `signals.py` create your signal receiver

    Remember the parameters available are specified in [built-in signal](https://docs.djangoproject.com/en/1.11/ref/signals/)

        from django.contrib.auth.signals import user_logged_out
        from django.dispatch import receiver

        @receiver(user_logged_out)
        def add_message_on_logout(sender, request, user, **kwargs):
            messages.info(request, 'You have been logged out.')

Alternatively you can connect to signals without the `decorator`:

        def add_message_on_logout(sender, request, user, **kwargs):
            messages.info(request, 'You have been logged out.')

        user_logged_out.connect(add_message_on_logout)


### Source

[Stackoverflow Signals](https://stackoverflow.com/questions/7115097/the-right-place-to-keep-my-signals-py-files-in-django/21612050#21612050)