# Regular Expressions

Match patterns against text

## Reading a file

Use `open()`

```
names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()
```

a better way:

```
with open("some_file.txt") as open_file:
    data = open_file.read()
```

## Get the regex library

`import re`

## Match

Matches from beginning of string

The `r` tells python it is a **raw string** (no escape character)

`re.match(r'Love', data)`

## Search

Match anywhere in string

`re.search(r'Kenneth', data)`

## Findall

Finds all places where it doesn't overlap

## Escape characters

* `\w` - any unicode word character
* `\W` - anything that isn't unicode
* `\s` - whitespace
* `\S` - non-whitespace
* `\d` - any number 0 - 9
* `\D` - anything that isn't a number
* `\b` - word boundary (edges of a word)
* `\B` - anything not edges of a word

Parenthesis define a group in regular expressions

You have to escpae them with `\(`

## Frequency

* `{3}` - exactly 3 times
* `(,3)` - 0 to 3 times
* `{3,}` - 3 or more times
* `{3,5}` - 3 to 5 times
* `?` - optional (0 or 1 time)
* `*` - occurs at least 0 times
* `+` - occurs 1 or more times

eg.

```
re.search(r'\w+')
re.search(r'\(?\d{3}\)?')
```

## Sets

* `[aple]` - Matches `apple`
* `[a-z]` - any lowercase letter (ranges)
* `[^2]` - anything that is not 2

Email address example:

`print(re.findall(r'[-\w\d+.]+@[-\w\d.]*, data))

## Flags

* Ignore case: re.findall(r'[trehous]+\b', data, re.IGNORECASE)

Shorthand for `re.IGNORECASE` is `re.I`

* Muliple lines (Mulitpline regex)

Use `re.VERBOSE` or `re.X`

Add multiple flags with pipe symbol:

`re.VERBOSE|re.I`

Treat each multiline as a string: `re.MULITLINE` or `re.M`

## Beginning and End

Beginning: `^`
End: `$`

## Named Groups

Use `(?P<name>{your-expression-here})`

## Making a dictionary out of a list

        line = re.search(r'''
            ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # last and first names
            (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
            (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
            (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
            (?P<twitter>@[\w\d]+)?$ # twitter
        ''', data, re.X|re.M)

        print(line)
        print(line.groupdict())

## Compile a pattern to an object

Get it ready for use `re.compile()`

Remove `data` as it wont have been run against anything at that stage

Allows returning an iterable of Matches

        line = re.compile(r'''
            ^(?P<name>(?P<first>[-\w ]*),\s(?P<last>[-\w ]+))\t  # last and first names
            (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
            (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
            (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
            (?P<twitter>@[\w\d]+)?$ # twitter
        ''', re.X|re.M)

        print(re.search(line, data).groupdict())

        print(line.search(data).groupdict())

        for match in line.finditer(data):
            print('{first} {last} <{email}>'.format(**match.groupdict()))

