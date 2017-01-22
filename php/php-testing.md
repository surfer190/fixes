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
