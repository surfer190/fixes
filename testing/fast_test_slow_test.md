# Fast Test, Slow Test

[A talk by Gary Bernhart](https://www.youtube.com/watch?v=RAxiiRPHS9k)

## Goals

### Prevent Regression

The reason you start writing test is you realise your software is breaking and you don't want it to break so much.
Release no bugs.

### Prevent Fear

Being able to change things minute to minute and have tests verify changes, requiring speed. Enable Refactoring.

### Prevent Bad Design

Way test your test is written makes it hard to write bad code.

## System Test

Most django tests are system tests as the are dependent on django code, libraries and method signatures.

What this does is create a binary test suite, so you have many tests that fail and you have to dig through stack traces to figure out what is wrong.

This also leads to people saying: "Everytime we change the code we have to update all the tests!"

Often said by the guy that thinks tests are stupid and argues against his teams ability to test effectively.

With these fragile system tests we get specific Regression protection. Protection against layers intergrating incorrectly, not the fine grained elements.

No help with refactoring as it is slow.

Not interacting with small components and not enhacing design.

## How to Fail

* If you use selenium as your primary testing tool you will fail. It can't be run before commiting cause it is so slow.
Broken all the time.
* Unit tests that are too big. Run time of test grows linearly.
* Writing fine-grained tests around legacy code. Tight tests that bake the badness in forever.

## How to Pass

* Test one object behaviour only
* Do one action
* Other classes can't break it
* Dependencies must be intrinsic to the test

At 40 seconds you can't do the thing called `TDD`

System test tests boundaries, whereas unit tests between components.

## Goal

The goal should be 90% unit, 10% system.



