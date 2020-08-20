---
author: ''
category: R-Stats
date: '2018-03-19'
summary: ''
title: Setting Up R On Macos
---
# Setting Up R on Mac OS

`Failed to setup default locale`

Type the following in an `R` terminal:

    system('defaults write org.R-project.R force.LANG en_US.UTF-8')

Then restart

# Intalling stuff with R

Use

    install.packages("<package name>")

Eg.

    install.packages("swirl")


### Sources:

https://stackoverflow.com/questions/3907719/how-to-fix-tar-failed-to-set-default-locale-error