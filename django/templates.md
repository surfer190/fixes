# Templates

HTML with special tagsfor data, loops and conditions

Templates are also extendable

## Where

Templates looks for `templates` directory inside the app directory by default

Also expects a folder inside `templates` with the same name as the `app`

Call the template `my_file.html`

### Better Way

* Is add global templates, in the root of the project add a `templates` folder
* then add it to the `DIRS` in `settings.py`

### Use Render

    from django.shortcuts import render

    return render(request, 'home.html', {context: context})

## Template tags

`{%` and `%}` that allow you to write python within

Use `{{ var_name }}` to print out a variable

## Inheriting

* Extending a parent template allows overridable `blocks`
* Name a block `<title>{% block title %}{% endblock %}</title>`
* Extends: `{% extends "layout.html" %}`
* Then set block content