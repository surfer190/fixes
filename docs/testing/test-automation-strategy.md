---
author: ''
category: Testing
date: '2020-11-08'
summary: ''
title: Test Automation strategy Notes
---

# Designing a Test Automation Strategy

* Reduce Regressions test cycle - reduce manually effort of regression tests and focus on new features.
* Reduce technical debt - new tests
* continuous testing as part of build - confidence of what has been added does not reduce quality

## What?

Always ask **What is the reason for test automation?**

## Who?

* Who is writing the scripts?
* Who is monitoring results?
* Who is updating tests when application changes?

> Testing is a software development initiative by itself...

Be realist about the learning curve - helps if person wants to test

## How?

Are all regression tests run, or only certain ones for risk and value.
Time and maintenance to start automation should not be taken lightly.

Actions and expected results clearly defined in scenarios?

Execution - multiple times a day in its own CI job or integrated into CI whenever new code is checked in.

* Running locally - manual intervention.
* Running in CI job - faster feedback - tests must be written with more care
* Running as part of development CI - requires fast and reliable test that only fail when provoked

> Automated tests need to be maintained

## Source

* [Test Automation University: Foundation for Successful Testing](https://testautomationu.applitools.com/setting-a-foundation-for-successful-test-automation/chapter1.html)