# How to Pretty Print JSON

Say you have:

    MY_JSON = {'Hello': [{'World': 'Coruscant'}, {'World': 'Tatooine', 'People': 'Humans'}]}

and you want to print it nicely:

    >>> import json
    >>> print(json.dumps(MY_JSON, indent = 4))
    {
        "Hello": [
            {
                "World": "Coruscant"
            },
            {
                "World": "Tatooine",
                "People": "Humans"
            }
        ]
    }

## Source

* [Pythoncircle pretty print json](https://www.pythoncircle.com/post/576/python-script-3-validate-format-and-beautify-json-string-using-python/)