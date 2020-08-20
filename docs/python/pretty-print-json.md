---
author: ''
category: Python
date: '2019-07-22'
summary: ''
title: Pretty Print Json
---
# How to Pretty Print JSON

**Update: This might be bad advice, when you `json.dump()` you print actually json (ie. with the javascript true, false and null values)**

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