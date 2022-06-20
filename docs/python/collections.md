---
author: ''
category: Python
date: '2017-02-19'
summary: ''
title: Python collections
---
# Python: Collections and Containers

* List and strings are collections
* Lists are mutable
* Strings, tuples, floats and integers are immutable
* Are **iterable**

Strings are immutable _you cannot change them in place_ ... a new spot is needed in memory

## Adding things

You can use `.append()` but will put a list within a list

With the `+` sign they both have to be lists
```
favourite_things += ["new element"]
```

`extend()` - Extend list by appending elements from the iterable

    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    
    my_list
    >>> [1, 2, 3, 4, 5]

`insert(<index to insert>, <thing to insert>)` - add a element at specific index

## Delete an element

`del favourite_things[-1]`

Last item in a list is always index **-1**

## Deleting an element by value

Use `remove()` - only removes the first instance

my_list.remove(1)

sometimes doesn't exist it will return a `ValueError`

## To get the information you remove

Use `pop()`

Without arguments: `my_list.pop()` it returns the last item

Can have an index: `my_list.pop(0)` 

Can't pop an empty list, need a try and an except

## Slice

A list or string that is a portion of another list or string

```
favourite_things = ['a', 'b', 'c', 'd', 'e']

#Slice
favourite_things[1:5]
```

Remember the second parameter it exclusive, it does not include the last element

Always returns same type

No outofbounds error is thrown

Start slice as beginning: `favourite_things(:2)`
Start slice at end: `favourite_things(2:)`

## Sort

`my_list.sort()`

This **sorts in place**, it does not return a sorted list.

## Range

You can create a range with `range(10)`

Which you can cast to a `list` with: `my_list = list(range(10))`

The list will contain 0 to 9

## List steps slices

Format is: `my_list[<start>:<stop>:<step>]

For the whole list: `mylist[::2]`

Can apply to any ordered iterable: lists and strings
Eg. "Johannesburg"[::2]

Default step is `+1`

But you can use a negative step to move backwards:

So to reverse the entire list: `mylist[::-1]`

## Mutating a list

Lists are mutable so you can specify what a specific slice should be

eg. `my_list[2:4] = ["red", "blue"]`

Delete a portion

`del my_list[5:8]`

**Slices and replacements don't have to be the same size**

## Dictionary

* Lets you name data. In other languages known as hashes or associative array
* key-value pair
* they are mutable
* unsorted - cannot use an index
* keys dont have to be strings
* seperate more fields with `,`
* Can have a dictionary within a dictionary
* `+` concatenate is not supported (python does not know priority)

Usages: `my_dict = {"title": "Surfer190"}`

Can create with `dict` keyword: `a = dict([['Title', 'Surfer190']])` <- but clearly shit

### Get an element

`my_dict["title"]`

Can subditionary: `my_dict["teacher"]["title"]`

If you request an element that does not exist you get a `KeyError` because the key does not exist

### Create a new key / Update

`my_dict["new_val"] = 4`

### Updating several values at once

`my_dict.update({...})`

**duplicate keys, it will take the value of the last occurance**

### Packing

With argument to a function with `**` 

eg. `def packer(**kwargs):`

Python will pack all the arguments sent in, into a `dictionary`

`kwargs` stands for `keyword argument` eg. `name = "kenneth", grade=2`

You can exclude a certain key with:

`def packer(name=None, **kwargs)`

## Unpacking

Giving a dictionary to a function and the arguments to that function derived from the dictionary

```
def unpacker(first_name=None, second_name=None):
    if first_name and last_name:
        print("Hi {} {}".format(first_name, last_name))
    else:
        print("Hi no name!")

unpacker(**{first_name: "surfer", last_name: "190"})
```

Call function with single dictionary as the only argument

because of `**` python took each key from the dict and sent to function

### Iterating through Dictionaries

Can loop same as list, but will only get keys not values

get keys: `course_minutes.keys()` optimised to give keys

get values: `course_minutes.values()`

get items: `course_minutes.items()` returns a tuple

## Tuples

* Like lists, each element has an index and can be looped over and any data type.
* Cannot be changed n place - **immutable**
* More memory efficient - fixed size in memory

String: ''
Lists: [,] - brackets
Dictionaries: {:} - braces
Tuples: (,,) - parenthesis

But parenthesis don't make a tuple, the `,` does

That is why a tuple needs a `,` even if it is a single item

```
Eg. my_tuple = 1, 2, 3

or my_tuple = (1, 2, 3)

my_tuple = tuple([1, 2, 3])
```

Does not support `Item Assignment`
Can add, remove elements

But you can change the data inside of mutable tuple members

Tuples have `simulataneous assignment`

```
a = 5
b = 20

a, b = b, a

a = 20
b = 5
```

tuples unpacks into variable on left side of equal sign

single asterisk `*` to pack a tuple

mostly called: `*args` always before `**kwargs**` and after others

### Upack tuple from dictionary

```
for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))
```

`enumerate` takes an ordered iterable and returns a tuple for each item, with index

`enumerate("abc")`

`for index, letter in enumerate("abcdef"):`

enumerate takes a second argument which is where to start

## Sets

Set of unique items

* sets can be compared
* no indexes
* mutable - updates in place

Used to create with: `set([1,2,3])`

Can now create with: `{1, 3, 5}` (but has to atleast have 1 value)

python sorts the sets in the way it makes sense to python

`low_primes = {1, 3, 5, 7, 11}`

Adding: `low_primes.add(7)`

Remove: `low_primes.remove(15)`

Update (with mutiple sets): `low_primes.update({19, 23}, {2, 29})`

* Union - Combination of 2 or more sets
* Difference - Everything in first set that isn't in the second
* Symmetric difference - Unique to either set
* Intersection - Items in both sets

`set1.union(set2)` or `set1 | set2`

`set1.difference(set2)` or `set2 - set1`

`set2.symmetric_difference(set1)` or `set1 ^ set2`

`set1.intersection(set2)` or `set1 & set2`

## Sources

* [Lists: Mutable & Dynamic](https://realpython.com/lessons/lists-mutable-dynamic/)
* [Stackoverflow: Sorting in place](http://stackoverflow.com/questions/7301110/why-does-return-list-sort-return-none-not-the-list)