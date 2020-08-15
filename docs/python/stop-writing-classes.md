---
author: ''
category: Python
date: '2019-07-22'
summary: ''
title: Stop Writing Classes
---
# Stop Writing Classes

As per the Zen of Python:

The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Key points:

* Simple is better than complex
* Flat is better than nested
* Readability counts
* If the implementation is hard to explain, it's a bad idea
* If the implementation is easy to explain, it may be a good idea

So:

> Don't do hard things in the first place

## Obfuscated function call

When you have a class with 2 methods and one is `__init__`, you should have just written a function.

    class Greeting(object):
        def __init__(self, greeting='Hello')
            self.greeting = greeting

        def greet(self, name):
            return '{}! {}'.format(self.greeting, name) 

    greeting = Greeting('hola')
    print(greeting.greet('Stephen'))

This can be written as:

    def greet(greeting, target):
        return '{}! {}'.format(greeting, target)

If you find that you are sending the same arg (`Hello`) too often, then use `functools`:

    import functools
    
    greet = functools.partial(greet, 'Hello')
    greet('Bob')

### Classes are good in theory

* Separation of concerns
* Decoupling
* Encapsulation
* Implementation Hiding

> I haven't use those words in 15 years, whenever you hear someone use those words they are trying to pull a fast one on ya - Jack Diederich

> Lots of times people think they might need something later - you don't! Or you can just do it later...if it comes up - Jason Diederich

## Evolution of an API (v1)

You are using a python library, so you should read through the code.

`MuffinHash.py` is a module containing 2 lines:

    class MuffinHash(dict):
        pass

Someone thought they were going to specialise a dictionary later

But everywhere their might be a dict, the is used:

    d = Muffinail.MuffinHash.MuffinHash(foo=3)

> Another sign that you don't need this, is that you have to type `Muffin` 3 times

## Evolution of an API (v2)

They brought a guy in who knew what he was doing:

    class API:
        def __init__(self, key):
            self.header = dict(apikey=key)
        
        def call(self, method, params):
            request = urllib2.Request(
                self.url + method[0] + '/' + method[1],
                urllib.urlencode(params),
                self.headers
            )
            try:
                response = json.loads(urllib2.urlopen(requesst).read())
                return response
            except urllib2.HTTPError as error:
                return dict(Error=str(error))

Unfortunately this class also just has 2 methods (1 being `__init__`)

Using this API:

    MuffinAPI.API(key='SECRET-KEY').call(('Mailing', 'Stats'), {'id': 1})

or:

    muffin_request = MuffinAPI.API(key='SECRET-KEY').call
    muffin_request(('Mailing', 'Stats'), {'id': 1})

> Whenever you see these things, thats when you know you should be using a class

## Evolution of an API (v3)

    MUFFIN_API = 'https://scrt.co.za/{first}/{second}'
    MUFFIN_API_KEY = 'SECRET-KEY'

    def request(noun, verb, **params):
        headers = {'apikey': MUFFIN_API_KEY}
        request = urllib2.Request(
            MUFFIN_API.format(first=noun, second=verb),
            urllib2.urlencode(params),
            headers
        )
        return json.loads(urllib2.urlopen(request).read())

## Namespaces are there to help

* Namespaces are for preventing name collisions
* Not for creating taxonomies - the science of classifying things

> It doesn't help if you have to remember the package it is in, the package it is in and then the module name. You just want to know the module name. (Structure would be flat)

`LookupError()` is just as good as any other error, if you get a stacktrace you have to read it anyway and it doesn't matter what the exception was named. - I kind of disagree with that point.

* Let callers know there is a problem with the usage of the API
* If an exception is not caught properly it will propagate all the way up to an except
* They help find bugs in your API code (Non-root exceptions are one's you did not intend to raise)

Adding the word `Exception` to the end of the name of the class, doesn't help

Use the python standard library as the example:

* 200k SLOC (Source lines of code)
* 200 top level modules
* averages 10 files per package
* defines 165 exceptions

Only 165 Exceptions for 200k lines of code. Whenever you think you need to write an exception, you probably don't.

## How to Write a Function

### Function Structure

Input

* Gather the info you need
* Throw out everything you don't
* Early errors are good errors - abort if you don't have the information you need
* Asserts add information - eg. expecting a single config `assert len(results) == 1`

Transform

* Do the actual work
* Exceptions should be exceptional
* The reader should be bored

Output

* Pretty print your results
* Exceptions should be really surprising
* Format our information in the way the caller expects it



## Source

* [Stop Writing Classes](https://pyvideo.org/pycon-us-2012/stop-writing-classes.html)
* [How to Write a fucntion](https://pyvideo.org/pycon-us-2018/howto-write-a-function.html)

