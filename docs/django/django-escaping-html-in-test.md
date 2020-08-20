---
author: ''
category: Django
date: '2018-01-29'
summary: ''
title: Django Escaping Html In Test
---
# Django Escaping HTML in Test

Import django's escpae it is different from `html.escpae`

    from django.utils.html import escape
    escape("'")

### Source

[Stackoverflow escaping](https://stackoverflow.com/questions/1946281/in-django-how-do-i-get-escaped-html-in-httpresponse)
