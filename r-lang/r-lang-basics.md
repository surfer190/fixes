# R Language Basics

R-lang is a free software environment for statistical computing and graphics.

## Install R

[Download R](https://www.r-project.org/)

[Download R Studio - An application to write R programs on](https://www.rstudio.com/products/rstudio/download/)

## Use Swirl

[Swirl](https://github.com/swirldev/swirl_courses) is an interactive prompt based way to learn about R and other data science topics

To start open r in terminal with `r` or open r studio

Install swirl

```
install.packages("swirl")
```

Load the swirl library

```
library(swirl)
```

Then start with swirl()

```
swirl()
```

Everything else will be guided

## R Language

The rlang interperirator works much like many others in that you can do basic maths with it.

### Syntax

Assignment: `<-` Assigning a value to a variable is done with `<-`

#### Data Structures

Any object containing data is a data structure

The simplest data structure is a vector. A single number is a vector of length 1.

A vector is created with the `c()` **concatenate** of **combine** method

`z = c(1.1, 4.5, 6)`

You can concatenate vectors with `c`:

`c(z, 255, z)`

Numberic operations on vectors are applied to all elements in the vector.
When arithmetic is done to vectors of the same length, each operation is applied element by element.
If they are not the same length, the shorter vector is recycled to the same length.

Behind the scenes `R` converts single vectors into multiple.

```
z <- c(5, 10, 15)
z * 2 + 100

# same as

z * c(2,2,2) + c(100,100,100)
```

#### Artihmetic Operators

* `+`, `-`, `/`, `*`
* `^`: to power of
* `sqrt()`: square root
* `abs()`: absolute value

#### Getting Help

To get help on a function type: `?` and the function name without calling it

Eg. `?c`

#### Dollar Operator

Grab specific items from output with the `$` operator

eg `file.info("mytest.R")$mode`

## Workspace and Files

Get working directory `getwd()`

List all objects in local workspace `ls()`

List all files in directory: `dir()` or `list.files()`

Find what arguments a function takes: `args(list.files)` 
Remember to not call the function

Create a directory: `dir.create('testdir')`

Set the working directory: `setwd('testdir')`

Create a file: `file.create('mytest.R')`

Check if a file exists: `file.exists("mytest.R")`

File info: `file.info("mytest.R")`

Rename a file: `file.rename('mytest.R', 'mytest2.R')`

Copy a file: `file.copy('mytest2.R', 'mytest3.R')`

Get relative path to a file: `file.path('mytest3.R')`

Create a path to a folder or file: `file.path('folder1', 'folder2')`

Create directory with recursive folders: `dir.create(file.path('testdir2', 'testdir3'), recursive = TRUE)`

> Top tip: It is often helpful to save the settings that you had before you began an analysis and then go back to them at the end. This trick is often used within functions; you save, say, the par() settings that you started with, mess around a bunch, and then set them back to the original values at the end. This isn't the same as what we have done here, but it seems similar enough to mention.

## Sequences

Create a sequence of numbers `:`: 1:20

Get a sequence of real numbers

```
pi:10
[1] 3.141593 4.141593 5.141593 6.141593 7.141593 8.141593 9.141593
```
It stops before it goes greater than 10, incrmeenting by 1 each time

Returns a `vector`

Go back / decrement: `15:1`

### Help on special chars

Use backticks

```
?`:`
```

Use `seq()` for more control

```
seq(1,20)
[1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
```

Get 30 items equally between 2 numbers

```
seq(5, 10, length=30)

 [1]  5.000000  5.172414  5.344828  5.517241  5.689655  5.862069  6.034483
 [8]  6.206897  6.379310  6.551724  6.724138  6.896552  7.068966  7.241379
[15]  7.413793  7.586207  7.758621  7.931034  8.103448  8.275862  8.448276
[22]  8.620690  8.793103  8.965517  9.137931  9.310345  9.482759  9.655172
[29]  9.827586 10.000000
```

Check the length of a vector

```
length(my_seq)
[1] 30
```

Make a sequence of numbers of length of another vector

```
1:length(my_seq)
```

> There are often several approaches to solving the same problem, particularly in R. Simple approaches that involve less typing are generally best. It's also important for your code to be readable, so that you and others can figure out what's going on without too much hassle.

Replicate with `rep()`

A vector of 40 zeroes

```
rep(0, times = 40)
 [1] 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
[40] 0
```

Replicate a vector

```
> rep(c(0,1,2), times=10)
 [1] 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2
 ```

Create 10 of each in sequence

```
rep(c(0, 1, 2), each = 10)
[1] 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2
```

 