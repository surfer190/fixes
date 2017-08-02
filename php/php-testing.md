# PHP Testing

A catastrophic failure is usually the indicator for using automated testing

### TDD Test driven development

1. Write a test for a small module of code
2. Write the code to pass the test
3. Repeat until you have a test for every unit of code

The tests are just an outcome of TDD as a design pattern

Little building blocks

## Types of Tests

#### Unit Tests

Verify individual modules of code run correctly

* small
* run quickly
* don't talk to real things (Don't talk to API and db)

Long tests means more likely tests will not be run

#### Integration Tests

Verifying all individual blocks fit together

* slow
* units of code talk to each other
* talk to real things

Need to refresh test server with decent data

#### Functional Tests

Verify application is behaving correctly

* very slow
* Not all tests can be automated

Only write for parts of the website that are mission critical

## Testing Tools

You should always use `phpunit` for unit tests

First test: `assertTrue(false)`

In php: `$this->assertTrue(false);`

### PHP Unit

It won't write your tests for you

Tests can be automated

Is flexible in how you organise tests

It isn't going anywhere

Great for documenting and finding out what code is and what it isn't

## Installing PHPUnit

* packagist: Repo of PHP packages
* composer: Managing packages for PHP project

```
composer require phpunit/phpunit
```

Global state and preserved for entire length of request, so in same scope it persists.

### Configuration

`phpunit.xml`:

```
<phpunit processIsolation="false">
  <testsuites>
    <testsuite name="Foo">
      <directory>tests/unit</directory>
    </testsuite>
  </testsuites>
</phpunit>
```

Can organise into test suites

#### Change test runner

Change `printerFile` and `printerClass` because the default test runner is pretty bland

#### Working with frameworks

It uses a `front controller` method, which sets up stuff.

To write tests for this you need to set up environments

So use the `bootstrap` node which tells phpunit to load this file before running tests

#### Writing a test

## What needs to be tested

* Every conditional statement needs at least 1 test
* You will need to refactor code for your tests to run - remove conditional dependencies

[Mockery](https://github.com/mockery/mockery) makes it easier to make duplicate calls than built in PHPunit mocks

Another good tool is [HTML purifier](http://htmlpurifier.org/) which can be used to strip out unwanted characters

PDO objects have some functionality internally that PHP's Reflection API doesn't handle properly so the built-in test double features of PHPUnit can't create doubles of them

## Princliples

* Every testcase has at least 1 assertion

Explicit is better than implicit, so multiple assertions are probably the best way to go

## Acceptance Tests

Unit tests - inidividual modules of code working in the way you expect, using dependencies and doubles for a consistent state.

Acceptance tests - Ensure individual modules of code are speaking to each other correctly a.k.a integration tests, no need to worry about test doubles.

### Data Provider

Making multiple assertions can be done with the use of a `DataProvider`

### DB Unit Tests

> Thou shalt not use a real database, and create test doubles

Fast running tests that work even if database is not there

On the other hand there are those that advocate using `DB_unit` that requires a live database to run tests

A tool that phpunit can use to create database connections

Need to extend from a different test class:

`PHPUnit_Extensions_Database_Testcase`

**2 methods** have to be implemented: `getConnection()` and `getDataSet()`

A `dataset.xml` is imported but there is a caveat for `null` values

If you are using `db_unit` you won't be using mocks

**DB Unit will delete everything** before adding data from seed files

Unit tests are not supposed to talk to databases or 3rd party, use test doubles as standins.


