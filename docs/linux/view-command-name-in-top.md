---
author: ''
category: Linux
date: '2022-08-30'
summary: ''
title: How to View the Command Name in Top
---

Top is a command line tool / binary that is used in unix-like environments to display process information.

On mac, `man top`:

    top – display sorted information about processes

On ubuntu, `man top`:

    top - display Linux processes

### Running Top

To run top:

    top

to exit:

    Ctrl + c

### Show the command used to run the program

Sometimes you will run top and see the process and the name under `command`.
But this will show the top-level process. So if you are using `python`, `node` or a webserver like `gunicorn` - you won't see more detailed info about the command used to run the process.

To do that simply press `c` when you are in `top`

> I tested this on Ubuntu OS only

### Source

[Show full process name in top](https://serverfault.com/questions/139632/show-full-process-name-in-top)