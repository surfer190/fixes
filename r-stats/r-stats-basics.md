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

The rlang interpreter works much like many others in that you can do basic maths with it.

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

Replicate a vector 10 `times`

```
> rep(c(0,1,2), times=10)
 [1] 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2
 ```

Create 10 of `each` in sequence

```
rep(c(0, 1, 2), each = 10)
[1] 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2
```

 ## Vectors

 The simplest and most common data structure

 * atomic vectors - single data type
 * lists - contain multiple data types

 Logical vectors contain the values `TRUE`, `FALSE` and `NA` (Not Available)


        num_vect <- c(0.5, 55, -10, 6)

        tf <- num_vect < 1

        tf
        [1]  TRUE FALSE  TRUE FALSE


#### Logical operators:

Exact equality: `>`, `<=`, `==` 
Inequality: `!=`
Or (Union): `A | B`
And (intersection): `A & B`
Not (Negation): `!A`


Character vectors

        my_char <- c("My", "name", "is")

Concatenate into svector of length 1

        paste(my_char, collapse = " ")

Append a value:

        my_name <- c(my_char, "stephen")

Adding an integer and character vector of length 3 together:

        paste(1:3, c("X", "Y", "Z"), sep="")

If they are not of equal kength there is `vector recycling`

Printing letters with `vector recycling`:

        > paste(LETTERS, 1:4, sep="-")
        [1] "A-1" "B-2" "C-3" "D-4" "E-1" "F-2" "G-3" "H-4" "I-1" "J-2" "K-3" "L-4" "M-1"
        [14] "N-2" "O-3" "P-4" "Q-1" "R-2" "S-3" "T-4" "U-1" "V-2" "W-3" "X-4" "Y-1" "Z-2"

## Missing values

Missing values play an important role in statistics and data analysis. Often,
missing values must not be ignored, but rather they should be carefully studied
to see if there's an underlying pattern or cause for their missingness.

In `R`, `NA` is used to represent any value that is 'not available' or 'missing' 
(in the statistical sense).

Any operation involving `NA` generally yields `NA` as the result

    > x <- c(44, NA, 5, NA)
    > x
    [1] 44 NA  5 NA
    > x * 3
    [1] 132  NA  15  NA

Create a vector with 1000 draws from standard distribution

    y <- rnorm(1000)

Then a vector of 1000 `NA`'s

    z <- rep(NA, 1000)

Select 100 at random from both:

    my_data <- sample(c(y,z), 100)

Check which are NA in a new vector using `is.na()`

    my_na <- is.na(my_data)

Camparing with `my_data == NA` returns all `NA`

> The reason you got a vector of all NAs is that NA is not really a value, but just a
> placeholder for a quantity that is not available. Therefore the logical expression is
> incomplete and R has no choice but to return a vector of the same length as my_data
> that contains all NAs.

    > 5 == NA
    [1] NA

> The key takeaway is to be cautious when using logical expressions anytime NAs might creep in

Tota number of true values

    > sum(my_na)
    [1] 45

#### Not a Number

There is another missing value

    > 0 / 0
    [1] NaN

In `R`, `Inf` stands for `infinity`

    > Inf - Inf
    [1] NaN

## Subsetting Vectors

Selecting first 10 elements of a vector

    > x[1:10]
    [1]  3.0949871  0.1960158  0.2084758         NA -0.2614606         NA -0.4809142
    [8]         NA         NA  0.6007584


Getting all results that are not `NA`:

    y <- x[!is.na(x)]

Get a vector of all positive values

    y[y > 0]

> Since NA is not a value, but rather a placeholder for an unknown quantity, the expression NA > 0 evaluates to NA

Only values of x that are both non-missing AND greater than zero.

    > x[!is.na(x) & x > 0]
    [1] 3.09498711 0.19601584 0.20847579 0.60075844 1.72316551 0.87532455 0.27598833
    [8] 0.58037652 0.10702578 0.08164542 1.65696398

Many programming languages use what's called **zero-based indexing**, which means that the first element of a vector is considered element 0. R uses **one-based indexing**,  which (you guessed it!) means the first element of a vector is considered element 1

Get the 3rd, 5th and 7th elements of vector

    x[c(3, 5, 7)]

But you can still ask for the `0th element` (No error thrown, nothing)

    > x[0]
    numeric(0)

Getting an element that does not exist:

    > x[3000]
    [1] NA

Getting elements except a few needs to use `negative` indices

    x[c(-2, -10)]

The shorthand for the above is:

    x[-c(2, 10)]

Named vector

    vect <- c(foo = 11, bar = 2, norf = NA)
    > vect
    foo  bar norf 
    11    2   NA 

Get just the names of a named vector

    > names(vect)
    [1] "foo"  "bar"  "norf"

You can give names to elements retrospectively

    vect2 <- c(11, 2, NA)
    names(vect2) <- c("foo", "bar", "norf")

Checking if 2 vectors are the same use `identical()`

    > identical(vect, vect2)
    [1] TRUE

Get a named element

    vect["bar"]

## Matrices and Data Frames

Both represent *rectangular* data types, meaning that they are used to store tabular data, with rows and columns.

* matrices: can only contain a single class of data
* data frames: can consist of many different classes of data

Find the dimensions of a variable

`dim()` function tells us how many dimensions an object has

    > my_vector <- 1:20
    > my_vector
    [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
    > dim(my_vector)
    NULL

A vector does not have a dimension so it is `NULL`

Get length:

    > length(my_vector)
    [1] 20

> The `dim()` function allows you to get OR set the `dim` attribute for an R object.

You can also use `aatributes`:

    > attributes(my_vector)
    $dim
    [1] 4 5

Now it is a `matrix`: rows and columns

    > my_vector
        [,1] [,2] [,3] [,4] [,5]
    [1,]    1    5    9   13   17
    [2,]    2    6   10   14   18
    [3,]    3    7   11   15   19
    [4,]    4    8   12   16   20

Check the class of the element

    > class(my_vector)
    [1] "matrix"

Open docs for matrix:

    > ?matrix()

Create the matrix

    > my_matrix2 = matrix(1:20, 4, 5)

Column combine for named rows

    > patients <- c("Bill", "Gina", "Kelly", "Sean")
    > cbind(patients, my_matrix)
        patients                       
    [1,] "Bill"   "1" "5" "9"  "13" "17"
    [2,] "Gina"   "2" "6" "10" "14" "18"
    [3,] "Kelly"  "3" "7" "11" "15" "19"
    [4,] "Sean"   "4" "8" "12" "16" "20"

This makes all the data to now be of type string / character

So we need a `data frame`

    my_data <- data.frame(patients, my_matrix)
    > my_data
    patients X1 X2 X3 X4 X5
    1     Bill  1  5  9 13 17
    2     Gina  2  6 10 14 18
    3    Kelly  3  7 11 15 19
    4     Sean  4  8 12 16 20

Confirm the class:

    > class(my_data)
    [1] "data.frame"

Add column names

    > cnames <- c("patient", "age", "weight", "bp", "rating", "test")
    > colnames(my_data) <- cnames
    > my_data
    patient age weight bp rating test
    1    Bill   1      5  9     13   17
    2    Gina   2      6 10     14   18
    3   Kelly   3      7 11     15   19
    4    Sean   4      8 12     16   20

## Logic

