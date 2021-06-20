---
author: ''
category: Django
date: '2020-02-01'
summary: ''
title: Django How to get the Root Path
---
# Django: How to get the Root Path

You may need to create or use a file in the root path of your django project.
From any file included in your django project you can run:

    import os
    os.path.dirname(os.path.realpath(__name__))

That will give

    ~/projects/my-django-project

## How to get the Path of the file you are in

To get the path of the file you are currently in use:

    import os
    os.path.dirname(os.path.realpath(__file__)) 

## Source

* [django project root self discovery](https://stackoverflow.com/questions/4919600/django-project-root-self-discovery)