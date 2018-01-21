# Django Adding default data After Migrations

So we are talking `RunPython` here not fixtures

Create an empty migration (remember to have already created the migrations for the table you are adding default data for)

        ./manage.py makemigrations <app_name> --empty -n <name_of_migration>

It will probably already have a dependency of the previous migration

Acquire the model with:

    ModelName = apps.get_model("<app_name>", "<model_name>")

Then do actions on it much like in the docs:

        from django.db import migrations

        def forwards_func(apps, schema_editor):
            # We get the model from the versioned app registry;
            # if we directly import it, it'll be the wrong version
            Country = apps.get_model("myapp", "Country")
            db_alias = schema_editor.connection.alias
            Country.objects.using(db_alias).bulk_create([
                Country(name="USA", code="us"),
                Country(name="France", code="fr"),
            ])

        def reverse_func(apps, schema_editor):
            # forwards_func() creates two Country instances,
            # so reverse_func() should delete them.
            Country = apps.get_model("myapp", "Country")
            db_alias = schema_editor.connection.alias
            Country.objects.using(db_alias).filter(name="USA", code="us").delete()
            Country.objects.using(db_alias).filter(name="France", code="fr").delete()

        class Migration(migrations.Migration):

            dependencies = []

            operations = [
                migrations.RunPython(forwards_func, reverse_func),
            ]

### Sources

* [Simple Better than Complex](https://simpleisbetterthancomplex.com/tutorial/2017/09/26/how-to-create-django-data-migrations.html)
* [Django Migration Docs](https://docs.djangoproject.com/en/2.0/ref/migration-operations/#django.db.migrations.operations.RunPython)