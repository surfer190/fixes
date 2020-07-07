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

The basic of logic will not be mentioned here.

In `R`:

* `&` evalautes to `AND` for the entire vector
* `&&` evaluates to `AND` just for the first element for vector

    > TRUE & c(TRUE, FALSE, FALSE)
    [1]  TRUE FALSE FALSE

and

    > TRUE && c(TRUE, FALSE, FALSE)
    [1] TRUE

* `|`  evaluates to OR across the entire vector
* `||` version of OR only evaluates the first member of a vector

**All AND operators are evaluated before OR operators**

There is a `isTRUE` function

* `isTRUE()` will only return TRUE if the statement passed to it as an argument is TRUE

    > isTRUE(NA)
    [1] FALSE
    > isTRUE(3)
    [1] FALSE

`xor()` function stands for exclusive OR

    > xor(TRUE, TRUE)
    [1] FALSE

Get a random sample of `ints` 1 to 10

    > ints <- sample(10)
    > ints
    [1]  4  6  8  7  2  9 10  5  3  1

`which()` function takes a logical vector as an argument and returns the indices of the vector that are TRUE

Finding which ints are greater than 7

    > which(ints > 7)
    [1] 3 6 7

* `any()` function will return TRUE if one or more of the elements in the logical vector is TRUE
* `all()` function will return TRUE if every element in the logical vector is TRUE

    > any(ints < 0)
    [1] FALSE
    > all(ints > 0)
    [1] TRUE

## Functions

    > Sys.Date()
    [1] "2018-03-16"

Get the `mean()`

    > mean(c(2, 4, 5))
    [1] 3.666667

Writing a function:

    function_name <- function(arg1, arg2){
        # Manipulate arguments in some way
        # Return a value
    }

Use the function:

    function_name(value1, value2)

> Note: There is no `return`. The last expression evaluated will be returned! 

John Chambers the creator of `R` said:

> To understand computations in R, two slogans are helpful:
> 1. Everything that exists is an object.
> 2. Everything that happens is a function call.

You can view a function's source code by just typing the function name

Setting default arguments

    remainder <- function(num, divisor=2) {
    num %% divisor
    }

You can use named parameters:

    remainder(divisor = 11, num = 5)

Check what arguments a function expects with:

    > args(remainder)
    function (num, divisor = 2)

You can pass functions as arguments

    evaluate <- function(func, dat){
        func(dat)
    }

Running it:

    > evaluate(sd, c(1.4, 3.6, 7.9, 8.8))
    [1] 3.514138

Anonymous functions:

    > evaluate(function(x){x + 1}, 6)
    [1] 7

`paste` function: Concatenate vectors after converting to character

The first argument is an `...` meaning it allows an indefinite number of arguments to be passed into a function. Any number of strings can be passed to function and a concatenated string will return.

> Strict rule in R programming: all arguments after an ellipses must have default values.

Unpacking arguments:

    args <- list(...)

    alpha <- args[["alpha"]]
    beta  <- args[["beta"]]

`+, -, *, and /` symbols. These symbols are called binary operators because they take two inputs, an input from the left and an input from the right.

#### User defined Binary Operators

    "%mult_add_one%" <- function(left, right){ # Notice the quotation marks!
    left * right + 1
    }

I could then use this binary operator like `4 %mult_add_one% 5` which would
evaluate to 21.

# Lapply and Sapply

`loop` functions

Used for implementing the `Split-Apply-Combine strategy for data analysis`

We will be using the [uci flag dataset(http://archive.ics.uci.edu/ml/datasets/Flags)

View the first 6 lines of a dataset:

        head(flags)

Dimensions:

        > dim(flags)
        [1] 194  30

194 rows and 30 columns

> To open a more complete description of the dataset in a separate text file, type `viewinfo()`

Class type:

        > class(flags)
        [1] "data.frame"

But what is the `class` of each variable or column in the dataset?

`lapply()` takes a list as input and applies a function to each element of the list.
A dataframe is really just a list of vectors: `as.list(flags))`

Remember to only give the name of the function you want to call (don't call it with the results):

    > cls_list <- lapply(flags, class)

    > cls_list
    $name
    [1] "factor"

    $landmass
    [1] "integer"

    $zone
    [1] "integer"

    $area
    [1] "integer"

    $population
    [1] "integer"

    $language
    [1] "integer"

    $religion
    [1] "integer"

    $bars
    [1] "integer"

    $stripes
    [1] "integer"

    $colours
    [1] "integer"

    $red
    [1] "integer"

    $green
    [1] "integer"

    $blue
    [1] "integer"

    $gold
    [1] "integer"

    $white
    [1] "integer"

    $black
    [1] "integer"

    $orange
    [1] "integer"

    $mainhue
    [1] "factor"

    $circles
    [1] "integer"

    $crosses
    [1] "integer"

    $saltires
    [1] "integer"

    $quarters
    [1] "integer"

    $sunstars
    [1] "integer"

    $crescent
    [1] "integer"

    $triangle
    [1] "integer"

    $icon
    [1] "integer"

    $animate
    [1] "integer"

    $text
    [1] "integer"

    $topleft
    [1] "factor"

    $botright
    [1] "factor"

The `l` in `lapply` stands for `list`

Simpified to a character vector:

    > as.character(cls_list)
    [1] "factor"  "integer" "integer" "integer" "integer" "integer" "integer" "integer"
    [9] "integer" "integer" "integer" "integer" "integer" "integer" "integer" "integer"
    [17] "integer" "factor"  "integer" "integer" "integer" "integer" "integer" "integer"
    [25] "integer" "integer" "integer" "integer" "factor"  "factor" 

`sapply` stands for `simplify` apply. It converts to a character vector.

    > cls_vect <- sapply(flags, class)
    > class(cls_vect)
    [1] "character"

> if the result is a list where every element is of length one, then sapply() returns a vector. If the result is a list where every element is a vector of the same length (> 1), sapply() returns a matrix. If sapply() can't figure things out, then it just returns a list, no different from what lapply() would give you.

See number of flags that has `orange`:

    > sum(flags$orange)
    [1] 26

Get only certain columns but keep all the rows:

    > flag_colors <- flags[, 11:17]

    > lapply(flag_colors, sum)
    $red
    [1] 153

    $green
    [1] 91

    $blue
    [1] 99

    $gold
    [1] 91

    $white
    [1] 146

    $black
    [1] 52

    $orange
    [1] 26

Using `sapply`:

    > sapply(flag_colors, sum)
   red  green   blue   gold  white  black orange 
   153     91     99     91    146     52     26

    > sapply(flag_colors, mean)
      red     green      blue      gold     white     black    orange 
    0.7886598 0.4690722 0.5103093 0.4690722 0.7525773 0.2680412 0.1340206

The `range()` function returns the minimum and maximum of its first argument

    > shape_mat <- sapply(flag_shapes, range)
    > shape_mat
     circles crosses saltires quarters sunstars
    [1,]       0       0        0        0        0
    [2,]       4       2        1        4       50

`unique()` returns a vector of only the 'unique' elements

    > unique(c(3, 4, 5, 5, 5, 6, 6))
    [1] 3 4 5 6

Use with anonymous functions:

    > lapply(unique_vals, function(elem) elem[2])

## vapply and tapply

`vapply()` allows you to specify format of result explicitly

Alows you to be mroe strict and will throw an error when data does not a single numeric value

    > vapply(flags, unique, numeric(1))
    Error in vapply(flags, unique, numeric(1)) : values must be length 1,
    but FUN(X[[1]]) result is length 194

To explicitly get the data types as a single element character vector

    > vapply(flags, class, character(1))

> As a data analyst, you'll often wish to split your data up into groups based on the value of some variable, then apply a function to the members of each group.

See amount in each group based on landmass:

    > table(flags$landmass)
    1  2  3  4  5  6 
    31 17 35 52 39 20 

Aplitting data into groups by landmass and running stats on it:

    > tapply(flags$animate, $flags$landmass, mean)
    See mean of animate flags per landmass

Get summary of popualtion for flags with/without red in:

    > tapply(flags$population, flags$red, summary)
    $`0`
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   0.00    0.00    3.00   27.63    9.00  684.00 

    $`1`
    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
        0.0     0.0     4.0    22.1    15.0  1008.0 

## Looking at Data

> Whenever you're working with a new dataset, the first thing you should do is look at it! What is the format of the data? What are the dimensions? What are the variable names? How are the variables stored? Are there missing data? Are there any flaws in the data?

List variables in your workspace: `> ls()`

Check strucute of data:

    > class(plants)
    [1] "data.frame"

> It's very common for data to be stored in a data frame. It is the default class for data read into R using functions like read.csv() and read.table(), which you'll learn about in another lesson.

Check rows and columns:

    > dim(plants)
    [1] 5166   10
    > nrow(plants)
    [1] 5166
    > ncol(plants)
    [1] 10

Size in memeory:

    > object.size(plants)
    644232 bytes

Get column names:

    > names(plants)
    [1] "Scientific_Name"      "Duration"             "Active_Growth_Period"
    [4] "Foliage_Color"        "pH_Min"               "pH_Max"              
    [7] "Precip_Min"           "Precip_Max"           "Shade_Tolerance"     
    [10] "Temp_Min_F"

By defulat `head()` shows you the first 6 lines you can get the first 10 with:

    > head(plants, 10)

Same for tail:

    > tail(plants, 15)

Get a summary of the dataset and missing values:

    > summary(plants)

> Categorical values are called factors in R

Sometimes number of categories is truncated by saying `Other` in that case use:

    > table(plants$Active_Growth_Period)

The best is casting to `str()`

`str()` can be used on many other datastructures

## Simlulation

Creating random numbers

    sample(x, size, replace = FALSE, prob = NULL)

Roll 4 dice (6 sided):

    > sample(1:6, 4, replace=TRUE)
    [1] 6 2 3 3

Choose 4 numbers, from 1 to 6, each number is replaced after selection so it can show up more than once

Get 10 numbers from 1 to 20 that won't appear again:

    > sample(1:20, 10)
    [1]  1  7 20 14 13 10  6  2 15 18

`LETTERS` is a predefined variable in R containing a vector of all 26 letters of the English alphabet

permute a sample of letters:

    > sample(LETTERS)
    [1] "I" "L" "B" "R" "F" "S" "Q" "J" "G" "M" "A" "H" "W" "U" "O" "P" "K" "T" "Y" "X" "E"
    [22] "D" "Z" "N" "C" "V"

If `size` is not given, `R` takes a sample equal in size.

Get an unfair coin with 100 flips:

    flips <- sample(c(0, 1), 100, replace=TRUE, prob=c(0.3, 0.7))

### Rbinom

Random binomial distribution: `rbinom`

> Each probability distribution in R has an r*** function (for "random"), a d*** function (for "density"), a p*** (for "probability"), and q*** (for "quantile").

Binomial distribution - Number of successes

Only specify the number of successes

To see number of successes:

    > rbinom(1, size = 100, prob = 0.7)

To store number of flips:

    > flips2 <- rbinom(100, size = 1, prob = 0.7)

### RNorm

The standard normal distribution has mean 0 and standard deviation 1

10 random numbers in a normal distribution:

    > rnorm(10)
    [1]  0.53665009 -2.39624561 -1.50745602 -1.27852621 -0.85378324 -0.04011113  0.49547350
    [8] -0.21447406 -0.81949348  0.75271073

### RPois

Poisson Distribution - Expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant rate and independently of the time since the last event.[1] The Poisson distribution can also be used for the number of events in other specified intervals such as distance, area or volume.

Generate 5 numbers with mean on 10:

    > rpois(5, lambda=10)
    [1]  9  7  6 12  6

TO get that 10 times use:

    > my_pois <- replicate(100, rpois(5, 10))

Get the column means:

    > cm <- colMeans(my_pois)

Plot a histogram of column means:

    > hist(cm)

All the other standard probability distributions are built into R: 

* Exponential: `rexpr()`
* Chi-squared: `rchisq()`
* Gamma: `rgamma()`

## Dates and Times

Timeseries data or temporal information

```
Dates are represented by the 'Date' class and times are represented by the 'POSIXct' and 'POSIXlt' classes. Internally, dates are stored as the number of days since 1970-01-01 and times are stored as either the number of seconds since 1970-01-01 (for 'POSIXct') or a list of seconds, minutes, hours, etc. (for 'POSIXlt').
```

    > d1 <- Sys.Date()
    > d1
    [1] "2018-03-19"
    > class(d1)
    [1] "Date"

See internal look of class

    > unclass(d1)
    [1] 17609

The total number of days since: `1970-01-01`

Create a date before epoch:

    > d2 <- as.Date("1969-01-01")
    > unclass(d2)
    [1] -365

System time:

    > t1 <- Sys.time()
    > t1
    [1] "2018-03-19 12:16:16 SAST"
    > class(t1)
    [1] "POSIXct" "POSIXt"

coerce the result to `POSIXlt` (Not sure why though)

    > t2 <- as.POSIXlt(Sys.time())
    > t2
    [1] "2018-03-19 12:17:49 SAST"

    > unclass(t2)
    $sec
    [1] 49.87161

    $min
    [1] 17

    $hour
    [1] 12

    $mday
    [1] 19

    $mon
    [1] 2

    $year
    [1] 118

    $wday
    [1] 1

    $yday
    [1] 77

    $isdst
    [1] 0

    $zone
    [1] "SAST"

    $gmtoff
    [1] 7200

    attr(,"tzone")
    [1] ""     "SAST" "SAST"

    > str(unclass(t2))
    List of 11
    $ sec   : num 49.9
    $ min   : int 17
    $ hour  : int 12
    $ mday  : int 19
    $ mon   : int 2
    $ year  : int 118
    $ wday  : int 1
    $ yday  : int 77
    $ isdst : int 0
    $ zone  : chr "SAST"
    $ gmtoff: int 7200
    - attr(*, "tzone")= chr [1:3] "" "SAST" "SAST"

Just get minutes:

    > t2$min
    [1] 17

Return day of the week:

    > weekdays(d1)
    [1] "Monday"

Similarly with months and quarters:

    > months(t1)
    [1] "March"

    > quarters(t2)
    [1] "Q1"

> `strptime()` converts character vectors to POSIXlt. In that sense, it is similar to `as.POSIXlt()`, except that the input doesn't have to be in a particular format (YYYY-MM-DD).

    > t3 <- "October 17, 1986 08:24"
    > t4 <- strptime(t3, "%B %d, %Y %H:%M")
    > t4
    [1] "1986-10-17 08:24:00 SAST"

    > class(t4)
    [1] "POSIXlt" "POSIXt"

Comparison of time:

    > Sys.time() > t1
    [1] TRUE

Time difference:

    > Sys.time() - t1
    Time difference of 9.086724 mins

Find time difference in specific unit:

    > difftime(Sys.time(), t1, units = 'days')
    Time difference of 0.006632809 days

## Base Graphics

Not covered are more advanced graphics:

* lattice
* ggplot2
* ggvis

Load dataset `cars`:

    data(cars)

Get help page for cars:

    `?cars`

Create basic chart:

    > plot(cars)

If dataset has 2 columns it assumes what you want to plot. Since we do not provide labels for either axis, R uses the names of the columns

> `plot` is short for scatterplot

Can be plotted with:

    > plot(x = cars$speed, y=cars$dist)

Setting labels:

    > plot(x = cars$speed, y=cars$dist, xlab='Speed', ylab='Stopping Distance')

Plot so points are `red`:

    > plot(cars, col = 2)

PLot and limit x-axis:

    > plot(cars, xlim=c(10, 15))

PLot with triangles:

    > plot(cars, pch=2)

#### Boxplot

You can pass the entire data frame

> `boxplot()`, like many `R` functions, also takes a "formula" argument, generally an expression with a tilde ("~") which indicates the relationship between the input variables. This allows you to enter something like `mpg ~ cyl` to plot the relationship between `cyl` (number of cylinders) on the x-axis and `mpg` (miles per gallon) on the y-axis.

    > boxplot(formula=mpg ~ cyl, data = mtcars)

A histogram can be used for a single vector:

    > hist(mtcars$mpg)

