---
author: ''
category: Golang
date: '2015-06-07'
summary: ''
title: Getting Started With Golang
---
# Getting started with golang

[Getting Started with GoLang](http://golang.org/doc/code.html)

[Effective Go](https://go.dev/doc/effective_go)

Go has a rigid type system and greater performance (as it is compiled)
You can use `go` to build websites but the author prefers ruby and go.

There are no dependencies when running a compiled `go` program.
A good tool for command line interface programs.

## Installing

No Install playground: [Go Dev Playground](https://go.dev/play/)

Install precompiled binaries [Go DL](https://go.dev/dl/)

Go is designed to work when your code is inside a workspace.
The workspace is a folder composed of `bin`, `pkg` and `src` subfolders.
You might be tempted to force Go to follow your own style - don't.

### Compiling

1. Download the archive

    wget go1.18.darwin-amd64.tar.gz

2. Set up environment variables

    echo 'export GOPATH=$HOME/code/go' >> $HOME/.profile
    echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.profile

3. Check your go version

    go version
    go version go1.18 darwin/amd64

## 1. The Basics

It is a:

* compiled - convert source code into lower level machine code
* statically-typed language - variables must be defined as a specific type (the compiled can infer the type) - python is dynamically typed
* C-like syntax

Go's goal is to ensure fast compile times

> Compiled languages tend to run faster and the executable can be run without additional dependencies (at least, that's true for languages like C, C++ and Go which compile directly to assembly).

Semi-colon and parenthesis around conditions are removed:

    if name == "Leto" {
      print("the spice must flow")
    }

Parenthesis are still used in complicated cases:

    if (name == "Goku" && power > 9000) || (name == "gohan" && power < 4000)  {
      print("super Saiyan")
    }

Go has garbage collection:

> Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used.

In `main.go`:

    package main

    func main() {
        println("it's over 9000!")
    }

Compile with:

    go run main.go

> A temporary directory is created

    go run --work main.go

To just build the code:

    go build main.go

Then you can run it with:

    ./main.go

### Main

In Go, the entry point to a program has to be a function called main within a package main.

Compiling without a `main()` function might work and is common when developing a library - there is just no entrypoint to run it.

### Imports

Go has a few built-ins like `println`

We can't go far without making use of go's standard library.
The `import` keyword is used to declare packages used by the file.

    package main

    import (
      "fmt"
      "os"
    )

    func main() {
      if len(os.Args) != 2 {
        os.Exit(1)
      }
      fmt.Println("It's over", os.Args[1])
    }

Run:

    go run import.go

We are using `fmt` and `os`. 

> The argument at index 0 - is always the currently running executable

The go library is well documented eg. [fmt](https://pkg.go.dev/fmt#Println)

### Go Docs

Get the docs locally without internet:

    godoc -http=:6060

> I had to install it with: `go install golang.org/x/tools/cmd/godoc@latest` - it still did not work

### Variables and Declarations

Basic declaration is:

    var NAME TYPE

eg.

    var power int = 9000

or:

    func main() {
      power := getPower()
    }

    func getPower() int {
      return 9001
    }

or:

    name, power := "Goku", 9000

or:

    var power int
	power = 9000

> Go will not compile if you have unused variables

### Function Declarations

One with no return value:

    func log(message string) {
    }

One with one return value:

    func add(a int, b int) int {
    }

One with 2 return values:

    func power(name string) (int, bool) {
    }

Which is used like:

    value, exists := power("goku")
    if exists == false {
        // handle this error case
    }

If you only care about the first value:

    _, exists := power("goku")
    if exists == false {
      // handle this error case
    }

If parameters share the same type you can use this syntax:

    func add(a, b int) int {

    }

Inferred types and multiple return values - are a similarity with dynamically typed languages.

## 2. Structures

It is not Object oriented. It does not have objects or inheritance.
It doesn't have polymorphism or overloading.

Go does have structures.

> Composition over inheritance

    type Saiyan struct {
      Name string
      Power int
    }

### Declarations and Initialisations

    goku := Saiyan{
      Name: "Goku",
      Power: 9000,
    }

> The trailing `,` is required

You don't have to set everything:

    goku := Saiyan{}

or

    goku := Saiyan{Name: "Goku"}
    goku.Power = 9000

or

    goku := Saiyan{"Goku", 9000}

> Go passes arguments to functions as copies

    func main() {
      goku := Saiyan{"Goku", 9000}
      Super(goku)
      fmt.Println(goku.Power)
    }

    func Super(s Saiyan) {
      s.Power += 10000
    }

So the answer above would be `9000`

To pass the pointer:

    func main() {
      goku := &Saiyan{"Goku", 9000}
      Super(goku)
      fmt.Println(goku.Power)
    }

    func Super(s *Saiyan) {
      s.Power += 10000
    }

* The `&` operator gets the address of the value
* The type `*Saiyan` means the pointer to the `Saiyan`
* We still pass a copy but the copy is of the same address
* Copying a pointer is cheaper than the whole data structure
* Ruby, Python, Java and C# behave this way
* On a 64-bit machine, a pointer is 64 bits large.

### Functions on Structures





### Sources

* [The Little Go Book](https://www.openmymind.net/The-Little-Go-Book/)
