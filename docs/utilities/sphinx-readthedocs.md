---
author: ''
category: Utilities
date: '2019-09-23'
summary: ''
title: Sphinx Readthedocs
---
# Sphinx and Read the docs

## What to Write

* Tutorials
* Topical guides
* Reference Material

More info:

* [https://jacobian.org/2009/nov/10/what-to-write/](https://jacobian.org/2009/nov/10/what-to-write/)
* [http://stevelosh.com/blog/2013/09/teach-dont-tell/](http://stevelosh.com/blog/2013/09/teach-dont-tell/)
* [https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)

## Reasons for Documentation

### You will be using your code in 6 months

The context in your brain can be put on paper. It is hard to know who will be maintaining that code 6 months from now.

### You want people to use your code

Have to onboard people. If there is a repo with no readme, you won't use that project.

### Makes your code better

Thinking about how your code is going to be used and the problems you are solving are a fundamental way to build better API's. Writing things from a user perspective is important.

### You want to be a better writer

Github issues, email, code comments and commit messages are fundamental to the job. 80% of our jobs.

## Tech Overview

* reStructuredText - markup language similar to markdown - solving a harder / complex problem
* docutils - python implementation of restructured texts
* Sphinx - wrapper for documenting software using Rst - extends tool to work with software contents
* Readthedocs - hosts sphinx projects - continuous integration for documentation

## ReStrucutedText

Lightweight markup language

* base format for other formats -> creates html, pdf etc.
* readable as plain text
* Works well with programming tools
* whitespace sensitive
* powerful, but slightly awkward

### Semantic HTML

HTML Bad:

    <b>issue 72</b>

HTML Good:

    <span class="issue">issue 72</span>

CSS:

    . issue { text-format: bold; }

### RST example

Bad:

    <font color="red">Warning: Don't do this!</font>

Good:

    <span class="warning">Don't do this!</span>

Best:

    .. warning:: Don't do this

### Markdown vs Rst

Markdown does not have semantic meaning.
Semantic is the meaning behind the words.

* Markdown is just HTML, not for semantics
* reStructuredText does more, more complex
* reStructuredText is ugly, not only because of its complexity

## Basic Sphinx Layout

    * project/
        * docs/
        * conf.py
        * MakeFile
        * index.rst
        * tutorial.rst

How to built docs

    make html

## Sphinx

[Sphinx Quickstart](https://sphinx-tutorial.readthedocs.io/start/)

* Best documenation the owner knows
* Search built-in - JS style
* Multiple formats: HTML, PDF, zipper HTMl and ePub

## ReadTheDocs

* Webservice for automatic documentation building for sphinx documentation
* Always up to date
* Different versions of docs
* localisation
* search via elasticsearch

## RST Getting Started

Every Sphinx document has multiple level of headings. Section headers are created by underlining the section title with a punctuation character, at least as long as the text

    Title
    =====

    Section
    -------

    Subsection
    ~~~~~~~~~~



## Source

* [Eric Holscher - Documenting your project with Sphinx & Read the Docs - PyCon 2016](https://www.youtube.com/watch?v=hM4I58TA72g)