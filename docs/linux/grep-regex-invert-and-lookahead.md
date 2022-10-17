---
author: ''
category: Linux
date: '2022-10-13'
summary: ''
title: Grep Regex Invert and Lookahead
---
# Grep Regex Invert Match and Lookahead

## Invert Match

When one wants to match lines not containing a specific pattern you can use `-v`:

     -v, --invert-match
             Selected lines are those not matching any of the specified patterns.

Given a text file:

    xxxxhhods osd ds  hook sdkjchslkdfjnscasd
    ab..............abc..............abc
    craaaxy hook 181818
    329847209fwfkjsdnfasdf

and wanting to match all lines that do not contain `hook`:

    $ grep -v hook test.txt 

    ab..............abc..............abc
    329847209fwfkjsdnfasdf

## Regex Look Ahead

However there may be situations where the `-v` flag cannot be used.
In those instances a [negative lookahead](https://www.regular-expressions.info/lookaround.html) can be used within the regex expression.

A _lookahead_ means followed by - it means how it is said. It looks ahead.
A _negative lookahead_ means you want to match something that is not followed by a certain pattern.

A negative lookahead is a question mark followed by a exclamation: `(?!xxx)`
A positive lookahead is a question mark followed by a equals sign: `(?=xxx)`

So to achieve the same result as above, excluding the `hook` matches this can be used:

    grep -P '^(?:(?!hook).)*$' test.txt 

    ab..............abc..............abc
    329847209fwfkjsdnfasdf

The `-P` means use perl-style regex syntax

* The `?:` is for clustering - breaking the source into groups and then running the expression over it

## Sources

* [Regular Expressions Lookaround](https://www.regular-expressions.info/lookaround.html)
* [Stackoverflow match pattern that does not contain](https://stackoverflow.com/questions/28652581/regular-expression-match-pattern-that-does-not-contain-a-string/28652625#28652625)
* [Perl re](https://perldoc.perl.org/perlre)
