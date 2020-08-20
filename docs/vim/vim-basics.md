---
author: ''
category: Vim
date: '2016-07-28'
summary: ''
title: Vim Basics
---
# Basics of Vim

## Two modes:

* `insert`
* `normal`

## Move around

You can use the cursor arrows, but there is also: `h`, `j`, `k`, `l`

## Navigating words

`w` - Moves to the start of next word

`e` - Moves to the end of the word

`b` - Moves to the beginning of a word

## Inserting text repeatedly

Formula: `<Num>i<character>` then `Esc`

30 hyphens: `30i-` then `Esc`

## Find matching parenthesis

Use `%` to go to the matching bracket

`{}` - Braces
`[]` - Brackets
`()` - Parenthesis

## Beginning and End of Line

`0` - go to the beginning of the line
`$` - go to the end of a line

## Find the Next occurance of a word under cursor

`*` - next
`#` - previous

## Navigating to beginning and End of File

`gg` or `H` - Go to the beginning of a file
`G` - Go to the end of a file

## Go to a specific line

Go to 4th line:

* `:4` then `Esc`
* `4G`

## Searching for text

Press `/` and then the text you are searchng for

`n`: Go to next occurance
`N`: Go to previous occurance

## Insert text on a new line

`o`: Insert and go to new line after
`O`: Insert and go to new line before

## Remove a character udner the cursor

`x`: Removes character under the cursor
`X`: Removes character before the cursor

## Deleting

`d` + ... : Deleting with movement
`dw`: delete to the start of the next word

## Visual mode

`v` enters visual mode

## Undo and Redo

`u` to undo
`ctrl + r` to redo

## get help

`:help`

## Repeat the previous command

`.` : Repeats the previous command

## Copy

`yy` - yank(copy) a line

## Paste

`p`: paste after current position
`P`: paste after current position

# Sources:

* [Parenthesis, brackets and braces](https://www.cis.upenn.edu/~matuszek/General/JavaSyntax/parentheses.html)
* [OpenVim: Interactive Tutorial for vim](http://www.openvim.com/)
