# Rest API

## API

Application Programming Interface

API lets other devices or apps interact with out app over HTTP.

## REST

Representational State Transfer

Client remembers state, server will not maintain state as HTTP is stateless

Nouns - Resources (Model in the application) eg. Player, Score, Match. Retrieved, created, modified and deleted. 
Verbs - Actions taken on resources. Represented by the type of request:

* GET - fetching a single or multple
* POST - create a new resource
* PUT - When updating a record
* DELELTE - when deleting a record

Endpoints - represent a single resources, or multiple of same resources

**Resource Name** should be plural

Keeping uri and resource names consistant goes a long way towards **maintainability** and **usability** of the API

## Querystring

Early API's used the querystring to set additional parameters for the request

        /api/v1/games?order=desc&sort=points

But it is better the use `HTTP Headers`

* Accept - specifies the file format
* Accept-Language - specifies human readable language
* Cache-Control - from cache or not

`Accept: application/json`

Post requests encode data as `form-data` or `x-www-encoded`, whereas `GET` request data is all in the `uri` or `querystring`

## Version

You should always add a version and keep the old API around as long as possible
`v1`

## HTTP Response

A response also has headers

Specify content type extension

        Content-Type: text/javascript

* Last-Modified - see when last modified
* expires - how long data can be trusted
* status - status codes tell us the state of the content and tell us the state of the request

