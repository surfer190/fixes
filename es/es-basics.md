## Basics of Ecmascript

1. Right Click -> Inspect element -> Open the `console` tab

## Strings

A string of characters that start and end with `' or "`

## Values

Values are the simplest components in JavaScript.
- `1` is a value
- `true` is a value
- `"hello"` is a value
- `function() {}` is a value

## Variables

Variables **can change**

Assigning a value to a variable

`var dogSentence = 'Dogs are the bane of my existence.'`

Only use `var` once, then you can refer to it a `dogSentence` unless you want to reinitialise it

## functions

Take `any number (0 to many)` of values in parenthesis and perform an action

Below is a `function` of the `string variable` that replaces text.

`dogSentence.replace('dogs', 'those blasted dogs')`

Note that the variable `dogSentence` does not actually change because _most_ JavaScript functions takes the value we give it and returns a new value, without modifying the value we passed in.

#### Writing functions

Make use of the `function` keyword, parenthesis `()`, a space and then enclosing brackets `{}`
The contents of the parenthesis should `return` something, if you want, else assigning a variable to the result of the function won't work.

```
function makeMoreExciting(string) {
  return string + '!!!!'
}
```

#### Using the function

`makeMoreExciting("hello")`

Returns: `"hello!!!!"`

#### Built-in functions (Standard Library)

So what functions are built into ecmascript? [Answer is here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)

#### Third party libraries

There are also a lot of third party libraries like: jQuery, ReactJs, underscore, angular...

## Arrays

Arrays are things you can keep multiple things in, like a list of things. An 'element' is a single item.

`var myCatFriends = ["bill", "tabby", "ceiling"]`

Note: Arrays **preserve ordering** so an array will stay in a particular order if new elements are added or removed

##### Specifying an element:

`myCatFriends[0]` returns `'bill'`

##### Adding to the array

`myCatFriends.push('super hip cat')`

##### Count how many elements in an array

`myCatFriends.length`

## Objects

Arrays are good for lists, but if you want more rich data so asking for the `address` of `bill` an object is better for that. It is basically an association of `keys` and `values`

`var firstCat = { name: "bill", lastName: "the cat", address: "The Alley" }`

Note: objects **do not preserve orgering** and **keys are not in quotes**

You can create an array of objects:

```
var moodLog = [
  {
    date: "10/20/2012",
    mood: "catnipped"
  },
  {
    date: "10/21/2012",
    mood: "nonplussed"
  }
]
```
Or an object of arrays:

```
var favorites = {
  treats: ["bird sighting", "belly rub", "catnip"],
  napSpots: ["couch", "planter box", "human face"]
}
```

## Callbacks

Callbacks are just functions that call other functions after some asynchronous task

Synchronous code like:

```
var photo = download('http://foo-chan.com/images/sp.jpg')
uploadPhotoTweet(photo, '@maxogden')
```

the second line / task cannot run until the first task has completed

If the download takes really long, all other ecmascript is blocked on the page until it completes.
We should just want to `block` the second task.

**Blocking execution should be avoided at all costs**

If you want a task `b()` to run after `a()` has completed.

`a(b)`, `b` is a callback to `a`

#### Callback Syntax

```
function a(done) {
  download('https://pbs.twimg.com/media/B4DDWBrCEAA8u4O.jpg:large', function doneDownloading(error, png) {
    // handle error if there was one
    if (err) console.log('uh-oh!', error)

    // call done when you are all done
    done()
  })
}
```




Sources:
- [Js for Cats](http://jsforcats.com/)
- [Essential JS Links](https://github.com/ericelliott/essential-javascript-links)
