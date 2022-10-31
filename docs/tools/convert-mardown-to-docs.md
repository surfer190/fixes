---
author: ''
category: Tools
date: '2019-10-24'
summary: ''
title: Convert Mardown To Docs
---
# Convert Markdown to Word Docx

To Convert Markdown to Word Docx or ODT (OpenDocument Text) format for google sheets, you need to install [pandoc](https://pandoc.org/).

Run for word:

    pandoc <myfile>.md -f markdown -t docx -s -o <myfile>.docx

Run for odt:

    pandoc <myfile>.md -f markdown -t odt -s -o <myfile>.odt

## Sources

* [Pandoc](https://pandoc.org/)
* [Pandoc - converting a file](https://pandoc.org/getting-started.html#step-6-converting-a-file)
