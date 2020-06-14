# Designing Great Web API's

## What is an API?

Application programming interface, is the specification of how one piece of software can interact with another.
A contract between software and the developer using it.

API's have always been part of software development. Operating systems offer API's so developers can build things for it.

Modern API's aren't just built to integrate systems within an organisation. They also allow businesses to share capabilities and data, build community and foster innovation.

## The API Economy

Growth of revenue and brand engagement as a result of offering public API's

* Higher Demand - modern browser, mobile devices and IoT
* Simplicity - SOAP and XML-RPC which required specs above just HTTP. Modern API's abandon this complex standard. Easier integration.
* Lower cost - Avoid money for complex proprietary software stacks
* New business models - Software as a service

## Business Advantages of Web API's

### Consuming API's

Allow businesses to leverage the hard work of other developers
Look for longevity and documentation

### Exposing your API to other Devs

* Allow customers to innovate
* Additional revenue streams by productizing your services
* Create partner networks

> API's are a business asset - it speaks about what the organisation cares about

### Marketing to Developers

* Developers demand an intuitive easy to use API

> The API is a competetive advantage

## Guidelines for Developing Great API's

Developer Experience (DX) for both internal and external developers

Internal developers can create business value faster
External developers benefit by integrating your well designed API quickly, faster than your competitor.

### 1. Treat your API as a Product

* Internal innovation
* Marketing channels
* Business development
* Lead generation
* User acquisition
* Upsell opportunity
* Device and mobile support
* Increased customer retention

Even if it is internal to a business it needs to be treated as a product

1. Clear communication to all lines of business
2. Implementing API governance to encourage consistency
3. Monitoring API usage, key metrics and performance
4. Evangelizing the API to internal and external developers through online resources and partner programs

### 2. Take an outside in approach

Web API's tend to reflect 2 things: organisational and database structure.
Rather take an outside in approach.

When the organisational structure leaks, it announces that it is not a product.
Creating inconsistent design.

Important to note:
1. API's should not be designed in isolation from other teams
2. They should be designed around external needs, not internal systems.

When database structure leaks, it is under the assumption that external developers want to use your API like accessing your database

> Developers don't care how you store your data as long as it is stored correctly and reliably

Focus on how an API will be used, rather than how it is built

### 3. Write Great Documentation

Developers don't have access to your source code.

Great documentation:

* format - professional and current documentation - not pdf, hosted on website available at all times (swagger)
* completeness - A contract with developers, need to be trusted. 
* discoverability - interactive and discoverable - using browser to interact with API (swagger)

### 4. Have an Intuitive Consistent Design

 Make it easier for a developer to know how to use it effectively, by lowering the learning curve.

> Developers must experience successes early and often

* Make data easily available (not hidden and hard to find)
* Require only information necessary to complete the desired task
* Offer both lower level and higher level ways of accomplishing workflows in fewer calls
* Use hypermedia links to inform clients of available actions
* Offer only 1 way to accomplish a task

Naming should be consistent:

* avoid abbreviations
* be consistent with resource names
* refrain from referencing internal systems - requiring insider knowledge

Consistent resource URLs

> Ontology - technique in information science for naming and typing entities and their relationships

* Use plural for many, singular for 1
* Use nested resources to indicate relationships
* avoid one off urls eg. `/users/current`

Consistent payload formats

Payloads should be of a consistent format

* Reuse field names: `user_first_name` and `user_last_name`, don't interchange them with `user_full_name`
* avoid abbreviations in field names
* Keep consistent casing rules
* Ensure all error messages are consistent across the API

As an API provider it is important to look for usage patterns of how your API is used, across different developers.
Then build higher level API's to save time for user's.

### What is Hypermedia?

* Hypermedia API's inform the clients about actions possible after a given request.
* next steps, related resources and other parts of the API
* This mimics how we use the web
* makes clients more flexible, reduces business logic
* Rest purists require it to call your API restful

### 5. Design for Security at the Start

* Nearly every API provides access to internal business systems, sensitive and personal information and/or public data.
* Security must be part of the design phase

#### Authentication

Verifying the identity of a consumer

* Password-based authentication
* API-key based authentication - key identifies teh API client
* Delegation based encryption - Connecting to an API on someone else's behalf - OAuth

#### Authorization

Authorising access to appropriate data and functional access rules.

#### Data Leakage

> Even with the proper authentication and authorization mechanism, your API design can still have security leaks. While this can happen for a variety of reasons, the most common is that APIs are designed for internal consumption only and are eventually promoted to partner or public developers

**Always use TLS - Transport Layer Security**

### 6. Share Great Code Examples

Provide guidance for developers

Understand the developer journey:
1. First success - reduce boilerplate make it very easy for a caller
2. Workflow support - clarity, clear intent
3. Production ready integration - Help developer understand how to catch errors, let them check rate limiting

### 7. Provide Helper Libraries

A client library to help clients make calls

## The Design-first API Process

Web API's are more social in nature.
They require collaboration.
They only have the API design and documenation to guide them.

Goals for API design:

* Simplicity
* Clarity

### Wireframing

Use Wireframes to focus on key goals of end users

### API Modelling

Great API design begins with modelling.
Translate product requirements into a high level API design.

Steps:
1. Identify participants, actors
2. Identify activities that participants wish to achieve
3. Seperate activites into steps that the participants will perform
4. Create a list of API elements from the steps (grouped into resource groups)
5. Validate the API by using requirements artifacts to test the completeness of the API

Actors: system admin, account administrators, users of system, internal and external software
Activities: 

## API Design Details

### HTTP Primer

* A request / response protocol
* HTTP is stateless - every request must provide all the details

URLS - Uniform Resource Locators - provide the address of where to lcoate a resource

* Scheme - how we connect secure or unsecure (`https://`)
* Hostname - server to contact (`api.example.com`)
* Post - 0 to 65535 (defaults to 80 for http and 443 for https)
* Path - (`/projects`)
* Query string - (`page=1&per_page=10`”

HTTP verbs:

* `GET` - Retrieve a collection or individual resource
* `POST` - Create a new resource or request a custom action
* `PUT` - Update existing resource
* `DELETE` - Delete existing resource or collection

HTTP request contains:

* VERB
* URL
* Request Header
* Request Body

#### Example

    GET http://www.oreilly.com/ HTTP/1.0
    Proxy-Connection: Keep-Alive
    User-Agent: Mozilla/5.0 [en] (X11; I; Linux 2.2.3 i686)
    Host: oreilly.com
    Accept: image/gif, image/x-xbitmap, image/jpeg, */*
    Accept-Encoding: gzip
    Accept-Language: en
    Accept-Charset: iso-8859-1, *, utf-8

HTTP Responses:

* Server response code (status code)
* Response header
* Response body

    HTTP/1.1 200 OK
    Date: Tue, 26 May 2015 06:57:43 GMT
    Content-Location: http://oreilly.com/index.html
    Etag: "07db14afa76be1:1074"
    Last-Modified: Sun, 24 May 2015 01:27:41 GMT
    Content-Type: text/html
    Server: Apache

    <html>...</html>

HTTP Response codes:

* 200 OK - Request succeeded
* 201 Created - Request fulfilled, a new resource has been created
* 202 Accepted - Request accepted for processing, but processing is no complete
* 204 No Content - Request fulfilled but does not need to return a body (common for delete)
* 400 Bad Request - Request not understood, malformed syntax
* 401 Unauthorized - Request requires user authentication
* 403 Forbidden - Server understood request, but is refusing to process
* 404 Not Found - Server has not found anything matching the requested URI
* 500 Internal Server Error - Server encountered an unexpected condition preventing it from fulfilling that request

Add your resource ontology to the top of your url structure

### Defining URL's through relationships

Relationships:

* Independent - standalone, usually top level
* Dependent - Cannot exist without a parent.
* Associative - Relationship contains additional properties to describe it, either nested or dependent

Independent: `/projects`, `/tasks` - can exist without each other
Dependent: `/projects/{id}/tasks` - must belong to a project
Associative: `projects/{id}/collaborators` - user's assigned to a project become collaborators

> An important decision is whether tasks exist outside a project. If they can, then both resources are independent and both become top level.

> “Understanding and applying resource relationships is critical to a great API design”

### Mapping Resource Lifecycle to Verbs

Review your API model and notice verbs: `search`, `create`, `read`, `update` and `delete`

Some resources might not need `update` or `delete`

Common modelling of HTTP verbs:

* list, Search, Match, View All = `GET` collection
* show, retrieve, view = `GET` resource
* create, add = `POST` create a new resource
* replace = `PUT` collection
* update = `PUT` update a resouce instance
* Delete all, remove all, clear, reset = `DELETE` a resource collection
* Delete, remove = `DELETE` a resource instance
* Other verbs = `POST` custom action on a resource instance

If there is no mapping, you should revisit the lifecycle or consider a custom action to a particular resource eg. `POST /projects/{id}/approve`

### Mapping Response Codes

For each API endpoint you will need to consider the response code to return for success and failure.

### Validating Design through Documentation and Prototyping

> By documenting your API design early, it will encourage the team to focus on documentation throughout the development process

> It will also encourage validation through feedback from internal or external developers by sharing your API design with them early rather than waiting until launch.

You can document with these API definition formats:

* Swagger
* RAML
* Blueprint
* IO Docs

Prototyping:

* static prototype - method of returning resource representations in one or more formats, such as XML or JSON - on local file system or served via a webserver
* working prototype - allow for more functionality - to simplify more complex interactions like third party integrations, connecting to existing SOAP services or legacy systems - can take shortcuts and flatten data structures

## Source

* James Higginbotham. [“Designing Great Web APIs.”](https://www.oreilly.com/library/view/designing-great-web/9781492048251/?intcmp=il-web-free-product-lgen_designinggreatapis)
