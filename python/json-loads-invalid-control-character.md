# How to load json from a file and not get the json loads invalid control character

Ever tried to load json from a file:

    with open('myfile.json') as table:
        data = json.load(table)

and you get this error:

    json.decoder.JSONDecodeError: Invalid control character at: line XXX column XXX (char XXXX)

The reason you get this error is highlighted in the python docs about the [JSONDecoder](https://docs.python.org/3/library/json.html#encoders-and-decoders):

> If strict is false (True is the default), then control characters will be allowed inside strings. Control characters in this context are those with character codes in the 0–31 range, including `\t` (tab), `\n`, `\r` and `\0`.

So to fix this we can set the `strict` kwarg to `False`:

    with open('myfile.json') as table:
        data = json.load(table, strict=False)

otherwise you could also attempt to replace the control characters

    table.read().replace('\t', '')

but that doesn't feel as good.

The best solution would be to export the json without the control characters.
