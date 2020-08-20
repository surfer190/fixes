---
author: ''
category: Ruby
date: '2015-11-03'
summary: ''
title: How To Add Gem To Gemfile With Commandline
---
# How to Add a Gem to your Gemfile from Command Line

Many Package managers like composer and npm automatically add packages to their respective package files (`composer.json`, `package.json`)

`composer require phpunit`

`npm install grunt-cli`

However the `gem` and `bundle` utilities do not.

Thankfully there is a `gem` to do this created by [Dru](https://github.com/DruRly/gemrat)

```
gem install gemrat
gemrat mysql
```

Source: [Stackoverflow](http://stackoverflow.com/questions/8005277/add-gem-to-gemfile-with-bundler-from-command-line)
