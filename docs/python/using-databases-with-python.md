---
author: ''
category: Python
date: '2017-04-18'
summary: ''
title: Using Databases With Python
---
# Databases

## ORM - Object Relational Mapper

Convert rows in tables into object (Models) in code

A simple lightweight one is called [peewee](https://github.com/coleifer/peewee)

> How to import everything

`from peewee import *`

### Working with Mysql

`sudo pip install pymysql`

then: 

`db = MySQLDatabase('peewee')`

from peewee import *

# make connection to db

                db = MySQLDatabase('peewee', user='root', password='pass')

                # classes inherit from model
                # always name models for singular name
                # represents a single item in db
                class Student(Model):
                    username = CharField(max_length=255, unique=True)
                    points = IntegerField(default=0)

                    # tell model what database it belongs to
                    # class inside of classs
                    class Meta:
                        database = db

                students = [
                    {'username': 'stephen', 'points':45},
                    {'username': 'squash', 'points':100},
                    {'username': 'pat', 'points':150},
                    {'username': 'matt', 'points':30},
                    {'username': 'casey', 'points':1345}
                ]

                def add_students():
                    for student in students:
                        Student.create(username=Student.username, points=Student.points)

                # if run directly and not imported
                if __name__ == '__main__':
                    db.connect()
                    db.create_tables([Student], safe=True)
                    add_students()

## Making queries

* `create()`
* `select()`
* `save()`
* `get()`
* `delete_instance()`

## Switches

Python intentionally does not have switches

Can use a dictionary but has no order

So can use an ordered dict

`from collections import OrderedDict`

Items must be added like a list