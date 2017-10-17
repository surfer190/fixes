# Django Migrations

Migrating in django is sometimes tricky and a bit less intuitive if youhave come fromsomething like `yii` or `laravel`

## The workflow

1. Create the model class in `models.py`

2. Make sure the `app` is added to `INSTALLED_APPS`

3. Create the migration

    ./manage.py makemigrations

4. Migrate

    ./manage.py migrate

## RunPython

RunPython is a way to initialise data or run operations during migrations.
They are tightly coupled with migrations and can be viewed here: [RunPython docs](https://docs.djangoproject.com/en/1.11/ref/migration-operations/#runpython)

## Reversing all migrations to Zero

    ./manage.py migrate <app_name> zero


### Sources

* [Reverting last migration](https://stackoverflow.com/questions/32123477/django-revert-last-migration)