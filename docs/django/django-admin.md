---
author: ''
category: Django
date: '2017-08-19'
summary: ''
title: Django Admin
---
# Django Admin

Create a super user

    ./manage.py createsuperuser

Go to `<your-django-ip>/admin`

## Registering our model

    admin.site.register(models.Course)

## Changing Administration Name

Add a template in `<root>/template/admin/base-site.html` - that is the a template with a namespace for the `admin` app.

The `base-site.html` file ships with the django source code in `django.contrib.admin.templates.admin`

We override the django file and change the title

This can be done with any django base templates

## Reordering Fields

Django always puts fields it displays in the order from the model

In `admin.py`:

        class QuizAdmin(admin.ModelAdmin):
            fields = ['course', 'title', 'description', 'order', 'total_questions']

        admin.site.register(models.Quiz, QuizAdmin)

## List and Detail View

List view shows all objects in a list
Detail view shows details of a single object

If a list grows so big we can add a `search_fields` attribute to the `ModelAdmin` class

### Search

This adds a search box to the listview

    class CourseAdmin(admin.ModelAdmin):
        search_fields = ['title', 'description']

    admin.site.register(models.Course, CourseAdmin)

### Filters

You can add filters to a model to quickly filter data with `list_filter`

    list_filter = ['created_at', 'is_live']

Filters can also be stacked

## Custom Filters

Inherit from `SimpleListFilter`

    class YearListFilter(admin.SimpleListFilter):
        # title is what comes after "by"
        title = 'year created'

        # what shows in url
        parameter_name = 'year'

        # creates clickable links in sidebar
        # first element is what shows on front, second element shows in url
        def lookups(self, request, model_admin):
            return (
                        ('2015', '2015'),
                        ('2016', '2016'),
            )

        # returns data
        def queryset(self, request, queryset):
            if self.value() == '2015':
                return queryset.filter(created_at__gte=date(2015, 1, 1),
                                        created_at__lte=date(2016, 12, 31),
                )
            if self.value() == '2016':
                return queryset.filter(created_at__gte=date(2016, 1, 1),
                                        created_at__lte=date(2017, 12, 31),
                )

Then add this filter to the filters for model

    list_filter = [YearListFilter]

## Show fields instead of __str__

Use the `list_display` variable

List also becomes sortable

Add to admin model class

        list_display = ['title', 'created_at']

### Making Listview Editable

Can only make editable, attributes that are in the `list_display`

## Recursive import

Sometimes if you add the import to the top of a file that is importing a different file you get recursive import

To get around that you can do the import within a classes function

## Adding more calculated / computed fields

If you add a function to a model,then that actually becomes an attribute of the model instance or record

So you can created computed fields and then just add the function name to `list_display` to have it display

        list_editable = ['title', 'description']

Careful could cause a `race condition` where 2 people are editing at the same time

### Adding sections to the detail view

In a `ModelAdmin`:

    class TextAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields': ('course', 'title', 'order', 'description')
            }),
            ('Add Content', {
                'fields': ('content',),
                'classes': ('collapse',)
            })
        )

The tuple first attribute has the name of the section.
`classes` sets the class and allows to be collapsed initially

### Make a field a radio button instead of select

    radio_fields = {
        'quiz': admin.HORIZONTAL
    }

## TabularInline and StackedInline

    class AnswerInline(admin.TabularInline):
        model = models.Answer

## A custom edit and update template

Make a copy of contents of `env/lib/python3.6/site-packages/django/contrib/admin/templates/admin/change_form.html` and put that into `templates/admin/<app_name>/<model_name>/change_form.html`

Do the same for `env/lib/python3.6/site-packages/django/contrib/admin/templates/admin/includes/fieldset.html` into `templates/admin/<app_name>/<model_name>/includes/fieldset.html`

In `change_form.html` change the path to the new fieldset

To this: `{% include "admin/courses/course/includes/fieldset.html" %}`

## Custom Bulk Custom Admin Actions

Define a function in the root of `admin.py` that does the action

    def make_published(modeladmin, request, queryset):
        queryset.update(status='p', is_live=True)

Add a `short_desription` for that function

    make_published.short_description = "Mark selected courses as published"

Then add it to the `ModelAdmin` action:

    class CourseAdmin(admin.ModelAdmin):
        actions = [make_published]
