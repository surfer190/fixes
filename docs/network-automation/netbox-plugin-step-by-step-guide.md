---
author: ''
category: Network Automation
date: '2021-11-25'
summary: ''
title: Step by step guide developing a netbox plugin
---

## A Step-by-Step Guide to Developing a Netbox Plugin

You are on this page so you know why you are using netbox and why you want to develop a plugin.
I will dispense with the excess and jump right in to the steps.

For a real world scenario - I want to create a system plugin to store various systems in the company and link it to a number of vms that make up the system.

> [TTL255](https://ttl255.com/developing-netbox-plugin-part-1-setup-and-initial-build/) has a decent tutorial but uses non-standard library tools `poetry` and `invoke` - so I didn't want to have to learn yet another tool.

### Steps

> Ensure you have a locally running netbox instance - to test on. You will need a local redis and  postgres, then you can clone the repo, create a virtual environment, install `requirements.txt` copy the `configuration.py` file and complete it and then migrate and run the project with `./manage.py runserver`

1. Create project folder, plugin folder

    mkdir netbox_systems_plugin
    cd netbox_systems_plugin
    mkdir netbox_systems
    
    > don't enter the `netbox_systems/` dir yet...

2. Create the `setup.py`

        vim setup.py

    write:
    
        from setuptools import find_packages, setup

        setup(
            name='netbox_systems',
            version='0.1',
            description='A systems plugin for netbox',
            author='Surfer190',
            license='Apache 2.0',
            install_requires=[],
            packages=find_packages(exclude=["tests"]),
            include_package_data=True,
            zip_safe=False,
        )
    
    exit vim

3. Create the `__init__.py` file

        cd netbox_systems
        vim __init__.py
        
    write:
    
        from extras.plugins import PluginConfig

        class SystemsConfig(PluginConfig):
            name = 'netbox_systems'
            verbose_name = 'Systems Plugin'
            description = 'Netbox plugin to group vms and other resources into systems'
            version = '0.1'
            author = 'Surfer190'
            author_email = 'surfer190@fixes.co.za'
            base_url = 'systems'
            required_settings = []
            default_settings = {
            }
        
        config = SystemsConfig

4. Initialise the git repo and commit the code (also create a `.gitignore`)

        cd ..
        vim .gitignore
    
    write:
    
        env/
    
    then exit vim
    
        git init
        git add .
        git commit -m "Setup systems plugin"

5. Create virtual env and make your netbox instance path available to your plugin's virtual environment (this assumes you have netbox somewhere on your dev machine)

        python3.9 -m venv env
        
        cd env/lib/python3.9/site-packages/
        echo /path/to/netbox/netbox > netbox.pth
        cd ../../../../
        source env/bin/activate
    
    > How do you test that netbox is available?
    
        python
        >>> import sys
        >>> print(sys.path)
        [..., '/path/to/netbox/netbox']
        >>> from netbox import configuration
        >>> print(configuration.PLUGINS)
        []

6. Install the plugin into your development environment (creates symbolic links)

    python setup.py develop

7. Create a model

        cd netbox_systems
        vim models.py
    
    write:
    
        from django.db import models

        from netbox.models import ChangeLoggedModel
    
        class System(ChangeLoggedModel):
            name = models.CharField(max_length=50)
            vms = models.ManyToManyField(
                'virtualization.VirtualMachine',
                blank=True
            )

            def __str__(self):
                return self.name
    
    exit vim

8. Make migrations (but first you need a `manage.py` file and minimal settings for a django project)

    > This is where it is tricky, the tutorial just says run `./manage.py makemigrations <plugin_name>`

    The problem is that there is no `manage.py` in the current directory...
    
    As suggested by Ben Lopatin in _Django Standalone Apps_, you must create your own minimal `manage.py` file that lives in the plugin project root (not the plugin itself). It should look like this:
    
    Go to the project root and create a `manage.py`:
    
        cd ..
        vim manage.py
        
    and write:
    
        #!/usr/bin/env python
        import os
        import sys
        import django
        from django.conf import settings

        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
        django.setup()

        if __name__ == '__main__':
            from django.core.management import execute_from_command_line
            execute_from_command_line(sys.argv)
    
    Then you need a minimal settings file, that I put in `tests/test_settings.py`
    
        mkdir tests
        touch __init__.py
        vim test_settings.py
        
    and write:
    
        from pathlib import Path

        SECRET_KEY = 'something'

        BASE_DIR = Path(__file__).resolve().parent.parent

        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / 'db.sqlite3',
            }
        }

        ROOT_URLCONF="netbox_systems.urls"
        DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            
            "extras",
            
            "netbox_systems",
        ]

        # Netbox

        ALLOWED_URL_SCHEMES = (
            'file', 'ftp', 'ftps', 'http', 'https', 'irc', 'mailto', 'sftp', 'ssh',
            'tel', 'telnet', 'tftp', 'vnc', 'xmpp'
        )
    
    You can then create and name the migration:
    
        ./manage.py makemigrations netbox_systems -n create_base_systems_model

9. Then add the model to admin

        cd netbox_systems
        vim admin.py
    
    and write:
    
        from django.contrib import admin
        from .models import System

        @admin.register(System)
        class SystemAdmin(admin.ModelAdmin):
            list_display = (
                'name', 'service', 'environment_name', 'responsible_team',
                'platform_owner', 'secondary', 'customer_data'
            )

10. Add tests

        cd ..
        cd tests
        vim test_models.py
    
    and write:
    
        from django.test import TestCase
        from django.core.management import call_command

        from netbox_systems.models import Service


        class TestMigrations(TestCase):
            def test_no_missing_migrations(self):
                call_command("makemigrations", check=True, dry_run=True)


        class TestServiceModel(TestCase):
            def test_service_str_representation(self):
                service = Service.objects.create(
                    name='DNS'
                )
                self.assertEqual(str(service.name), 'DNS')

    then test with:
    
        cd ..
        ./manage.py test

11. 

Adding a reference to a netbox model I got `ModuleNotFoundError: No module named 'mptt'`

So I had to install the netbox requirements into my plugin env...is that good or bad?

Also be

`RuntimeError: Model class extras.models.change_logging.ObjectChange doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.`

because I did:

    class System(ChangeLoggedModel):
        ...
        vms = models.ManyToManyField(
            'virtualization.VirtualMachine'
        )




## netbox plugin with many-to-many field with netbox model

## Netbox reusable plugin how to test admin


    

## Sources

* [Netbox Plugin Development](https://netbox.readthedocs.io/en/stable/plugins/development/)
* [TTL255 Developing Netbox Plugin](https://ttl255.com/developing-netbox-plugin-part-1-setup-and-initial-build/)
* [Netbox-bgp plugin](https://github.com/k01ek/netbox-bgp)
