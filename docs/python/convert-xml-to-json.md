---
author: ''
category: Python
date: '2020-10-07'
summary: 'This post shows a brief summary of how to convert xml to json with python.'
title: Convert XML to JSON
---
# Convert XML to JSON

Python's standard library has several modules for parsing XML (including DOM, SAX, and ElementTree).
As of Python 2.6, support for converting Python data structures to and from JSON is included in the json module.

So the `json` module can actually dump the `xml`.

For example you a variable `router_config`:

    >>>> type(router_config)
    <class 'lxml.etree._Element'>

To dump into a variable:

    config_json = json.dumps(router_config)
    
To dump into a file:

    json.dump(router_config, fs)

## Source

* [Dan Lenski Stackoverflow](https://stackoverflow.com/questions/191536/converting-xml-to-json-using-python/10201405)