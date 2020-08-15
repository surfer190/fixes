---
author: ''
category: Composer
date: '2016-09-26'
summary: ''
title: Bus Error Core Dumped
---
# Composer Bus error (core dumped) Error

How to Fix this error? That may happene when you run composer.

```
Bus error (core dumped)
```

### Solution

Delete the `/home/{ user }/.composer` folder

`rm -R ~/.composer`

This will remove the messed up composer packages

##### Source:

[Stackoverflow remove composer](http://stackoverflow.com/questions/30396451/remove-composer)
