# Python Code Smells

## Initialisation of an empty list outside a for loop

Search for `= []`

Example:

    results = []
    for item in data:
        result = my_func(item)
        if result:
            results.append(result)

Can become:

    results = [
        my_func(item) for item in data
        if my_func(item)
    ]

Using the `:=` (walrus) it can become:

    results = [
        y for item in data
        if (y := my_func(item))
    ]

## Potentially Simpler with Walrus (Might be harder to read or understand)

    chunk = file.read(8192)
    while chunk:
        process(chunk)
        chunk = file.read(8192)

becomes:

    while chunk := file.read(8192):
        process(chunk)

Why do this:

* Fewer lines are better ? (you sure?)
* 

## Simplifying a two line check

    match = re.match(data)
    group = match.group(1) if match else None

can be made into a single line:

    group = re.match(data).group(1) if re.match(data) else None

with walrus:

    group = match.group(1) if (match := re.match(data)) else None

### The Walrus operator is nothing like the equals operator

# you can!
x = y = z = 0

# you can't!
(z := (y := (x := 0 )))

# you can!
a[i] = x

# you can't!
a[i] := x

# you can!
self.rest = []

# you can't!
self.rest := []

## Problems with the Walrus Operator PEP572

* Backwards compatibility
* Teachability - named expression operator





    