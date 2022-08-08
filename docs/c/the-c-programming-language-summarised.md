---
author: ''
category: C
date: '2015-09-13'
summary: ''
title: The C Programming Language Summarised
---
# The C Programming Language Summarised

### Running Code

* Program must end in `.c`
* Compile the file using `cc file.c`
* run the resulting `.out` file with `./a.out`

** The `cc` command is really using `gcc - GNU C Compiler`. Read more about this by tying `man cc`**

### Consistancy of programs

* Functions - Computing operations
* Variables - Store Values

### The main function

* The `main` function indicates where the program starts and hence al c programs must have a `main` function

### Including Libraries

```
#include <stdio.h>
```

Tells the compiler to include information about the standard input/output library

### Functions and Communicating to functions

```
//defining the function
myfunc(char c){
  //function contents
}

//calling the function
char mychar = 'p';
myfunc(mychar);
```
To send information to functions we use `arguments`.

Using the standard io library:

```
printf("Hello, World\n");

function: printf()
argument: "Hello, World\n"
```
### Varaiables and Declaraions

All variables must be declared before they are used
A `declaration` anounces: type and name

```
int fahr, celsius;
int lower, upper, step;
```

### Data types

The range of variables depends on the machine you are using.

`int`    : integers

`float`  : floating point (fractions)

`char`   : a single byte

`short`  : short integer

`long`   : long integer

`double` : double-precision floating point


##### Escape Sequence

An escape sequence are single characters that are hard to type, such as new lines and spaces.

```
\n - new line
\t - tab
\b - backspace
\" - quote
\\ - backslash
```

### Comments

Comments are to enchance programmer understanding and are ignored and stripped out by the c compiler

```
//single line comment
/*  A
    Multi-Line
    Comment */
```

### Loops

###### While Loop

```
while (fahr <= upper) {
...
}
```

1. The condition in parentheses is tested.
2. If it is true (fahr is less than or equal to upper ), the body of the loop (the three statements enclosed in braces) is executed.
3. Then the condition is re-tested, and if true, the body is executed again.
4. When the test becomes false ( fahr exceeds upper ) the loop ends, and execution continues at the
statement that follows the loop. There are no further statements in this program, so it
terminates.

####### Single Line while

```
while (i < j)
    i = 2 * i;
```
###### For loop

`for (fahr = 0; fahr <= 300; fahr = fahr + 20)`

Three parts:
1. The initialisation
2. Test or condition
3. Increment

### Coding Style

* Proper indentation and spacing are critical
* One statement per lines
* Blanks around operators
* Don't bury `magic numbers` in programs, use constants

### Arithmentic

* Integer division truncates: any fractional part is discarded

```
    5/9 = 0
    5.0/9 = 0.555556
    5/9.0 = 0.555556
    5.0/9.0 = 0.555556
```
### Printf Text formatting

`printf` is not part of the c language, it is part of the standard library.

```
printf("%d\t%d\n", fahr, celsius);
```

Each `%` indicates a placeholder for a variable to replace it.

`%d` indicates an integer replacement, `%f` indicates a floating point replacement.

### Symbolic constants

`#define LOWER 0 `

### Character Input and Output

```
//get a character from keyboard
c = getchar();

//put a character on output
putchar(c);
```

###### Fle Copying

Given getchar and putchar , you can write a surprising amount of useful code without
knowing anything more about input and output.

```
int c;
c = getchar();
while (c != EOF) {
  putchar(c);
  c = getchar();
}
```
**What appears to be a character on the keyboard or screen is of course, like everything else,
stored internally just as a bit pattern**
The type char is specifically meant for storing such
character data, but any integer type can be used

`c` must be big enought to hold all poosible `chars` + EOF

`EOF` is an integer is `<stdio.h>`, doesn't matter as long as it is not a char value

The left hand side of an assignment can appear in a larger expression:

```
while ((c = getchar()) != EOF)
```
###### Precedence

The precedence, the order of operation, of `!=` is higher than that of `=`
