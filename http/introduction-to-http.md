# HTTP

Hyper-text transfer protocol

* Rules about how to communicate - conventions
* Standards for device communication
* plaintext protocol

## Request

#### Request line

        [verb] [uri] HTTP/[version]

        GET /xml HTTP/1.1

#### Headers

        [Header Name]: [Header Value]

        Host: httpbin.org
        User-Agent: telnet
        Accept-Language: en-US

#### Blank Line

#### Request Body

        data (optional)

## Response

#### Status Line

        HTTP/[version] [status code] [status message]

        HTTP/1.1 200 OK

#### Headers

        [Header Name]: [Header Value]

        Server: nginx
        Date: ...
        Content-Type: application/xml

#### Blank line

#### Response body / Payload

        html, json etc..

## Stateless

* No record of previous interaction
* Can't remember previous requests

Cookies and sessions is part of application that uses HTTP, not part of http itself

## Querystring

Only works in a `GET` request
Can add data in uri with `?firstname=Stephen&language=English`

Helps server give accurate response, should not change any resource

A `POST` is used to make a change on the server

## Content-Length

If there is data in a response body the `Content-Length` will give response in `bytes`

