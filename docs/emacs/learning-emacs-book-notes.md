---
author: ''
category: Emacs
date: '2020-09-03'
summary: ''
title: Learning Emacs - Book Notes
---
## Learning Emacs

> Emacs is the most powerful text editor available today

It served as a complete windowing system before `x` and `microsoft windows`

There are 2 main versions of Emacs:

* GNU Emacs
* XEmacs - made for GUI

> If you know GNU Emacs, you will be able to adapt to any other Emacs implementation with no trouble

The basic commands don't really change from one editor to another

eg. `C-n (for Ctrl-n)` almost always means go to the next line

This book covers `Emacs 21.3.5`

### History

* In 1975, Richard Stallman wrote the first Emacs editor
* Name stands for `Editing Macros`
* Emacs became prominent in the birth of the Free Software Foundation (FSF) and the GNU Project in 1984

> Free does not necessarily mean cheap (you may have to pay a fee to cover the cost of distribution); it most definitely does mean liberated from restrictions about how it can be used and specifically how it can be shared.

    Free == Liberated

### The Meta key

* Emacs commands uses a modifier (`Ctrl`)
* `Control-x Control-s` saves a file
* The other modifier Emacs uses is the `Meta` key
* The key immediately to left and right of the spacebar - `alt` on pc and `command` on mac
* You can use the `Esc` key - but it must not be held down

> The meta key will improve your speed

### Conventions

* `C-g` means hold `ctrl` and `g`
* `M-x` means hold `meta` and `x`
* `Meta -` means hold `meta` and `-`
* `S-right` means hold shirt and click the right mouse button
* `C-S-right` means hold down shift and control and click the right mouse button

All emacs commands have a full name
Eg. `forward-word` is equalvalent to `M-f` and `forward-char` is equivalent to `C-f`

Tying a command to a keystroke is a `key binding`

If you ever see `(none)` it means a command is not bound to a particular keystroke.
To use a command like this type: `M-x` followed by the commands full name then press `Enter`.

Eg. `M-x pong Enter`

## 1. Emacs Basics

### Files and buffers

You don't edit files with emacs. Emacs copies file contents into a temporary buffer that you edit.
The file on disk does not change until you save the buffer.

Some buffers `*scratch*` and `*help*` don't have associated files.

### Modes

There are modes for writing and writing in specific programming languages.

A buffer can only be in onne major mode at a time.

Major modes:

* Fundamental mode - default
* Text mode
* View mode
* Shell mode
* Outline mode
* Indented mode -  for indenting text automatically
* Paragraph mode
* Picture mode - creating ascii drawings
* HTML mode
* Latex mode
* Compilation mode
* cc mode  - writing C, C++  and java
* Java mode - for writing java programs
* perl mode
* SQL mode
* Emacs Lisp mode
* Lisp mode
* Lisp interaction mode

Emacs attempts to put you in the correct mode for what you are editing.

Eg. File ends in `.c` = C mode or `.el` = Lisp mode

Minor modes - aspects of emacs that can be turned on or off

* Autofill mode - enables wordwrap
* Overwrite mode - replaces chars as you type
* Auto-save mode
* Isearch mode
* Flyspell mode - spell checker
* Abbrev mode - use word abbreviations
* Paragraph indent text mode - Indenting first line of a paragraph
* Refill mode - fills paragraphs
* info mode - for emacs docs
* Others in the book...

### Starting emacs

Type `emacs`

> You will see some info (a splash screen) it dissapears when you type putting you in `*scratch*`

> Mac OS X comes with a version of GNU Emacs installed in `/usr/bin`

### Emacs Display

Large display to edit. Cursor (or point) marks your position.

Unlike `vi`, emacs does not have seperate modes for inserting and giving commands.

If you get stuck press `C-g` - to get out.

Toolbar is a new thing in emacs - similar to word toolbar.

### The mode line

The second last line

It shows the encoding of the file buffer, whether you have unsaved changes, what buffer you are editing, position relative to the rest of the file. If entire contennt is visible it prints `ALL` if not a percentage of where you are in the file.

Then the mode, in this case `Lisp Interaction` mode.

### Minibuffer

Below the mode line is the minibuffer. Where emacs echoes the commands tou enter.

It is also where emacs displays error messages.
Press `C-g` if you get stuck.

### Emacs Commands

Each command has a formal name - the name of a Lisp routine.

Commands are abbreviated.

Regular keys are bound to `self-insert-command`

#### Opening a File

    emacs myfile.txt

or

    C-x C-f 

If you typed wrong then `find-alternate-file`: `C-x C-v`

#### Append a file into another file

Go to end of the file

    M->

Then insert it with

    C-x i

#### Saving files

Save with:

    C-x C-s

It will notify you with `Wrote filename`, if nothing changed it will say nothing needs to be saved.

Save as.. (write-file):

    C-x C-w

#### Leaving Emacs

Quit Emacs:

    C-x C-c

> if you have unsaved changes it will ask you and if you are disgarding you must say `yes` not just `y`

#### Getting Help

    C-h ?

for tutorial:

    C-h t

To find the meanting of a keystroke use:

    C-h k { key stroke}

example:

    C-h k C-x i

gives you the meaning of `C-x i`

To search in a reverse way use:

    C-h f find-file




### Source

* [Learning GNU Emacs, 3rd Edition - Debra Cameron, James Elliot, Marc Loy, Eric S Raymond, Bill Rosenblatt](https://www.oreilly.com/library/view/learning-gnu-emacs/0596006489/)