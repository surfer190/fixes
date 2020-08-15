---
author: ''
category: Python
date: '2017-09-10'
summary: ''
title: Object Oriented
---
# Object Oriented Python

Everything in python is an Object

* Usually 1 class per file

## Declaration

        class Monster:
            hit_points = 1
            color = 'yellow'
            weapon = 'sword'

## importing a class

`from monster import Monster` - means bring Monster class from inside the monster library

**Every file is a library**

## Using attributes

eg. `Monster.hit_points`

## Creating an instance of a class

Use `()`

eg. `jubjub = Monster()`

## Methods

Functions that are part of a class are called `methods`

Every method at the very least **takes the self** argument

Eg. `def battlecry(self):`

`self` always represents the instance you are calling the method on (doesn;t have to be called self)

Can use self variable to get info about the current instance

## Dunder Init (__init__)

Runs when a new instance is created

a pythonic `construcutor`

eg.

        class Monster:
            def __init__(self, hit_points, weapon, color, sound):
                self.hit_points = hit_points
                self.weapon = weapon
                self.color = color
                self.sound = sound

            def battlecry(self):
                return self.sound.upper()

        slimey = Monster(5, 'Sword', 'blue', 'GLUG')

Can set **defaults**:

        def __init__(self, hit_points=5, weapon='Sword', color='yellow', sound='roar'):

Or dictionary unpacking:

`**` means handle as _dictionary_

        def __init__(self, **kwargs):
            self.hit_points = kwargs.get('hit_points', 1)
            # Can still set the default

## Delete an instance

        jubjub = Monster()
        del jubjub

## Setting attributes

Usually used in `__init__(self, **kwargs)`

       for key, value in kwargs.items():
            setattr(self, key, value)

Usage: `jabber = Monster(color='blue', hit_points=500, sound='whiffling', adjective='manxsome')`

## Inheritance

Showing a subclass = Inheriting all attribute of parent class:

        class Goblin(Monster):
            pass

Every class inherits from default `object` class 

so `class Monster:` === `class Monster(objecy)`

**pass** keyword tells python to keep going as though nothing has happened

## __Str__

`__str__` a magic method called when class is converted to a string / string representation

`self.__class__.__name__` - class name and string representation of that class

        def __str__(self):
            return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                                self.__class__.__name__,
                                                self.hit_points,
                                                self.experience)

        from monster import Monster
        my_mon = Monster()
        print(my_mon)


**Will print the dunder str**

## DRY

Don't repeat yourself

* group common operations into Functions
* group common functionality into classes

## Override

You can override an inherited class simply by writing the method in the subclass

## None

Special variable only ever equa to itself

It is `falsey`

`sys.exit()`..`sys` is a library to exit the interpreter