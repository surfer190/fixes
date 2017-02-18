# Collections or Containers in Python

List and strings are colelction

Are **iterable**

Strings are immutable _you cannot change them in place_ ... a new spot is needed in memory

## Adding things

You can use `.append()` but will put a list within a list

With the `+` sign they both have to be lists
```
favourite_things += ["new element"]
```

`extend()`

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

This **sorts in place**, it does not return a sorted list. [Source](http://stackoverflow.com/questions/7301110/why-does-return-list-sort-return-none-not-the-list)