# API Contract Testing

Contract testing - a type of integration testing that is well-suited to microservice architectures

* Consumer - application that uses the API
* Provider - application that publishes the API
* Contract - a file describing the expected consumer/provider behaviour (in the form of an OpenAPI spec)
* Consumer-driven test - A test where the consumer side of a contract is used to create a simulated consumer, used to test a provider.
* Provider-driven test - A test where the provider side of a contract is used to create a simulated provider, used to test a consumer.

### Traditional Integration Testing

* Test using mock or simulated services
* Test using the real dependencies

### API Contract

An API contract can be created as an OpenAPI spec by both the provider and consumer teams - a single file.

Simulated consumer or provider is created from the spec

### Provider

* Serves data and functionality to the consumer
* API publisher

Provider's contract should include:
* Available endpoints
* Possible responses
* Expected inputs

### Consumer

* Accepts funtionality and responses from the provider

A Consumer's contract should include:
* What endpoints it needs
* The type of data it can send
* The responses it can accept


Usually the providers will give the contract - it is however more useful to find out how a calling service will use the api.

> Let the consumers call the shots

The onus is on the provider to give the functionality to the consumer.

### Advantages of Rest API Contract Testing

* The provider only supplies what is necessary - "You aren't going to need it"
* Consumer doesn't need to worry about fucntionality it doesn't need
* Provider is notified quickly if they are implementing unnecessary - quick feedback loop
* Ensures feedback for all teams involved

### When should we use Contract Testing

* When we need to test quickly
* When we don't want to spend too much time setting up environments
* On mission critical systems that use APIs
* To make sure *implementation* matches the *specification*

### Who benefits from Contract Testing

* Integration testers
* Automation testers
* Manual testers
* Anyone who needs to make sure their microservices are doing what they are supposed to be doing

### How do we do it

* Write your contract - OpenAPI Spec or Swaggerhub
* Take the specification into SoapUI Pro to generate your consumer / provider tests
* Use `ServiceV` to mock the consumer / provider 

### Demo

You would have an OpenAPI spec now and then use ServiceV pro - that creates a virtual service from your spec.

You can then use SoapUI Pro to send requests to that virtual / simulated service


