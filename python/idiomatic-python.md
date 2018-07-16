# Idiomatic Python

Here are a few things you can watch out for to improve how obvious and fast your code is.
Oftentimes people coming from other programming language don't take advantage of the python way.

## Looping

    colours = ['red', 'green', 'blue', 'orange']

    for colour in colours:
        print(colour)

    # Not

    for i in range(len(colours)):
        print(colours[i])

# Reversing a loop

    for colour in reversed(colours):
        print(colour)

    # Not

    for i in  range(len(colours) -1, -1, -1):
        print(colours[i])
    
# USing Indices

Use `enumerate`

    for i, colour in enumerate(colours):
        print(i, '-->', colour)

## Looping over 2 collections

Use `zip`

    colours = ['red', 'green', 'blue', 'orange']
    names = ['raymond', 'rachel', 'matthew']

    for name, colour in zip(names, colours):
        print(name, colour)

Problem with zip is they use alot of memory so can use `izip` instead

