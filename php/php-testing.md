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
