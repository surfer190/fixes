# Django Format, Localization, Translation and Internationalization

## Overview

The goal of internationalization and localization is to allow a single Web application to offer its content in languages and formats tailored to the audience

How does django help with this?

1. Allows developers to set which parts of the app need to be translated or formatted locally
2. It uses this info to localize users according to their **preference**

> Translation depends on the target language, and formatting usually depends on the target country

This information is provided by browsers in the `Accept-Language` header. However, the time zone isn’t readily available.

* Internationalization: Preparing the software for localization (Done by developers)
* Localization: Writing the translations and local formats (Done by translators)
* locale name: Language and/or country specification (eg. `it`, `de_AT`, `es`, `pt_BR`)
* language code: Represents the name of a language. Browsers send this with `Accept-Language` (eg. `it`, `de-at`, `es`, `pt-br`)
* message file: a plain-text file, representing a single language, that contains all available translation strings and how they should be represented in the given language (They have a `.po` extension)

## Translation

To make a project translatable you need to add a few hooks into your code. These hooks are called `translation strings`. They tell django that the following text should be translated into the end user's language. This is the developers responsibility.

The translations are held in message files, which are compiled using GNU's `gettext`

Internationalization is on be default and you should turn it off if you are not going to use it with `USE_I18N = False`

### Activating Translation

So you have prepared your translations or you just want to use django's built in translations.

To set an installation-wide preference set the `LANGUAGE_CODE` setting. Django uses this language as the default translation.

Make sure the corresponding message files and their compiled versions (.mo) exist

If you want each user to set their language preference you need to use `LocaleMiddleware`. `LocaleMiddleware` enables language selection based on data from the request

To use `LocaleMiddleware`, add `'django.middleware.locale.LocaleMiddleware'` to your `MIDDLEWARE` setting. 

It should be ordered after `SessionMiddleware` and `CacheMiddleware` and before `CommonMiddleware`

### How LocaleMiddleware figures out what language you want

1. It checks in the [url](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#url-internationalization)
2. It looks for the [`LANGUAGE_SESSION_KEY`](https://docs.djangoproject.com/en/2.0/ref/utils/#django.utils.translation.LANGUAGE_SESSION_KEY)
3. It looks for a cookie: [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-LANGUAGE_COOKIE_NAME)
4. It looks at the `Accept-Language` on the browser request
5. It then uses `LANGUAGE_CODE`

Only languages in the global `LANGUAGES` can be selected

[Learn how django discovers translations](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#how-django-discovers-translations)

[Adding translations in javscript](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#internationalization-in-javascript-code)

Django makes the general assumption that the original strings in a translatable project are written in English

### Internationalization: in Python code

We use `_` to save typing and import `gettext()`

`ugettext()` was used to distinguish between unicode and ascii utf-8

    from django.utils.translation import gettext as _

    output = _("Welcome to my site.")

translation works on variables and computed values like string literals above

The caveat with computed and variables is that `django-admin makemessages` won't be able to find these strings

You can use placeholders but `f-strings` are not yet supported

    def my_view(request, m, d):
        output = _('Today is %(month)s %(day)s.') % {'month': m, 'day': d}
        return HttpResponse(output)

### Pluralization

Use the function `django.utils.translation.ngettext()` to specify pluralized messages.

`ngettext()` takes three arguments: the singular translation string, the plural translation string and the number of objects.

        from django.utils.translation import ngettext

        page = ngettext(
            'there is %(count)d object',
            'there are %(count)d objects',
        count) % {
            'count': count,
        }

### Lazy Translation

These functions store a lazy reference to the string – not the actual translation. The translation itself will be done when the string is used in a string context, such as in template rendering

This is something that can easily happen when defining models, forms and model forms, because Django implements these such that their fields are actually class-level attributes

#### Model fields and relationships verbose_name and help_text

    from django.utils.translation import gettext_lazy as _

    class MyThing(models.Model):
        name = models.CharField(help_text=_('This is the help text'))

#### Model verbose names values

    from django.db import models
    from django.utils.translation import gettext_lazy as _

    class MyThing(models.Model):
        name = models.CharField(_('name'), help_text=_('This is the help text'))

        class Meta:
            verbose_name = _('my thing')
            verbose_name_plural = _('my things')

#### Model methods short_description attribute values

### Internationalization: In template

#### Trans template tag

{% raw %}
    <title>{% trans "This is the title." %}</title>
    <title>{% trans myvar %}</title>
{% endraw %}

If the `noop` option is present, variable lookup still takes place but the translation is skipped. This is useful when “stubbing out” content that will require translation in the future:

{% raw %}
    <title>{% trans "myvar" noop %}</title>
It’s not possible to mix a template variable inside a string within `{% trans %}`
In that case use `{% blocktrans %}`

    {% blocktrans %}Back to '{{ race }}' homepage{% endblocktrans %}
{% endraw %}

Blocktrans with objet attributes or template filters:

{% raw %}
    {% blocktrans with amount=article.price %}
    That will cost $ {{ amount }}.
    {% endblocktrans %}

    {% blocktrans with myvar=value|filter %}
    This will have {{ myvar }} inside.
    {% endblocktrans %}
{% endraw %}

Multiple expressions

{% raw %}
    {% blocktrans with book_t=book|title author_t=author|title %}
    This is {{ book_t }} by {{ author_t }}
    {% endblocktrans %}
{% endraw %}

{% raw %}
Other block tags (for example `{% for %}` or `{% if %}`) are not allowed inside a blocktrans tag.
{% endraw %}

Retrieve translated string but do not display

{% raw %}
    {% trans "This is the title" as the_title %}

    <title>{{ the_title }}</title>
    <meta name="description" content="{{ the_title }}">
{% endraw %}

[Much more info on translations](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/)

## Format Localization

Django’s formatting system is capable of displaying dates, times and numbers in templates using the format specified for the current locale.

What is a locale?

A __locale name__, either a language specification of the form `ll` or a combined language and country specification of the form `ll_CC`. Examples: `it`, `de_AT`, `es`, `pt_BR`. The language part is always in lower case and the country part in upper case. The separator is an underscore.

When it’s enabled, two users accessing the same content may see dates, times and numbers formatted in different ways, depending on the formats for their current locale.

To enable format localization add:

`USE_L10N = True`

to your settings file

> If you want to enable translation add ` USE_I18N = True`

### Local Input in forms

Django can use localized formats when parsing dates, times and numbers in forms. So based on the current locale django can guess the format that the user entered.

> Remember django uses different formats for display and form input. `%a`, `%A`, `%b`, `%B` and `%p`can't be used when parsing dates.

To enable a form fields input and output use **localize**:

    class CashRegisterForm(forms.Form):
        revenue = forms.DecimalField(max_digits=4, decimal_places=2, localize=True)

### Controlling localization in templates

Django will try to use a locale specific format when outputting to a template. Sometimes you may want to send unlocalized values to the template (js).

To control this we have some template tags:

{% raw %}
        {% load l10n %}

        {% localize on %}
            {{ value }}
        {% endlocalize %}

        {% localize off %}
            {{ value }}
        {% endlocalize %}
{% endraw %}

Also per variable localization:

Force no localization

        {{ value|unlocalize }}

Force localization

        {{ value|localize }}

### Creating custom format files

Sometimes a format file does not exist for your locale or you want to overwrite some values.

First tell django where the format files will be placed in `settings`:

    FORMAT_MODULE_PATH = [
        'mysite.formats',
        'some_app.formats',
    ]

Then you would need to create the file:

    `mysite/formats/en/formats.py`

both `formats` and `en` folders need an `__init__.py`

### Limitations

Django cannot do context sensitive formats automatically. Like swiss german using commas and points depedning on whether money or number.

## Timezones

When support for time zones is enabled, Django stores datetime information in **UTC** in the database, uses time-zone-aware datetime objects internally, and translates them to the end user’s time zone in templates and forms.

Even if your website is available in only one time zone, it’s still good practice to store data in UTC in your database.

The solution to this problem is to use UTC in the code and use local time only when interacting with end users

To enable timezone support add `USE_TZ = True` to your settings

[Go through some frequently asked questions about timezone](https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/#time-zones-faq)

The same datetime has a different date, depending on the time zone in which it is represented

A datetime represents a **point in time**. It’s absolute: it doesn’t depend on anything. On the contrary, a date is a **calendaring concept**

Generally, you should avoid converting a datetime to date

If you really need to do the conversion yourself, you must ensure the datetime is converted to the appropriate time zone first

    >>> from django.utils import timezone
    >>> timezone.activate(pytz.timezone("Asia/Singapore"))
    # For this example, we just set the time zone to Singapore, but here's how
    # you would obtain the current time zone in the general case.
    >>> current_tz = timezone.get_current_timezone()
    # Again, this is the correct way to convert between time zones with pytz.
    >>> local = current_tz.normalize(paris.astimezone(current_tz))
    >>> local
    datetime.datetime(2012, 3, 3, 8, 30, tzinfo=<DstTzInfo 'Asia/Singapore' SGT+8:00:00 STD>)
    >>> local.date()
    datetime.date(2012, 3, 3)

Get local time in the current timezone

    >>> from django.utils import timezone
    >>> timezone.localtime(timezone.now())

### Naive and aware datetime objects

Python’s `datetime.datetime` objects have a `tzinfo` attribute that can be used to store time zone information, represented as an instance of a subclass of `datetime.tzinfo`. When this attribute is set and describes an offset, a datetime object is **aware**. Otherwise, it’s **naive**.

You can use `is_aware()` and `is_naive()` to determine whether datetimes are aware or naive.

When timezone is disabled, datetime is in localtime:

    import datetime
    now = datetime.datetime.now()

When time zone support is enabled (`USE_TZ=True`), Django uses time-zone-aware datetime objects. If your code creates datetime objects, they should be aware too.

    from django.utils import timezone
    now = timezone.now()

### Interpreting Native datetime objects

When `USE_TZ` is True, Django still accepts naive datetime objects, in order to preserve backwards-compatibility. When the database layer receives one, it attempts to make it aware by interpreting it in the default time zone and raises a warning

### Default timezone and current timezone

The default time zone is the time zone defined by the `TIME_ZONE` setting

The current time zone is the time zone that’s used for rendering

You should set the current time zone to the end user’s actual time zone with `activate()`. Otherwise, the default time zone is used.

You should always work with aware datetimes in `UTC` in your own code. For instance, use `fromtimestamp()` and set the `tz` parameter to `utc`

### Selecting the current time zone

The current time zone is the equivalent of the current `locale` for translations. However, there’s no equivalent of the `Accept-Language` HTTP header that Django could use to determine the user’s time zone automatically

> Most websites that care about time zones just ask users in which time zone they live and store this information in the user’s profile

> For anonymous users, they use the time zone of their primary audience or UTC

### Time zone aware input in forms

When you enable time zone support, Django interprets datetimes entered in forms in the current time zone and returns aware datetime objects in `cleaned_data`.

### Time zone aware output in templates

When you enable time zone support, Django converts aware datetime objects to the current time zone when they’re rendered in templates.

### Controlling template localtime

{% raw %}
    {% load tz %}

    {% localtime on %}
        {{ value }}
    {% endlocaltime %}

    {% localtime off %}
        {{ value }}
    {% endlocaltime %}
{% endraw %}

Time zone setting

{% raw %}
    {% timezone "Europe/Paris" %}
        Paris time: {{ value }}
    {% endtimezone %}

    {% timezone None %}
        Server time: {{ value }}
    {% endtimezone %}
{% endraw %}

Get current timezone

{% raw %}
    {% get_current_timezone as TIME_ZONE %}
{% endraw %}

##### Template Filters

Localtime

{% raw %}
    {% load tz %}

    {{ value|localtime }}
{% endraw %}

UTC

{% raw %}
    {% load tz %}

    {{ value|utc }}
{% endraw %}

timezone

{% raw %}
    {% load tz %}

    {{ value|timezone:"Europe/Paris" }}
{% endraw %}


[Implementing selection of a user's timezone](https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/#selecting-the-current-time-zone)



Sources:

* [Django Formatting](https://docs.djangoproject.com/en/2.0/topics/i18n/formatting/)
* [Internationalisation](https://docs.djangoproject.com/en/2.0/topics/i18n/)
* [Timezones](https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/)