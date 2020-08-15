---
author: ''
category: Api
date: '2020-07-29'
summary: ''
title: Api Security
---
# API Security

## 1. Introduction to API Security

* Similar threats to traditional web applications
* API's are more transparent - exposing the structure

API Audience:

* Public API - external developers
* Private API - Internal developers + inhouse
* Partner API

### API security Domain

* End user - uses _apps_ which use the API
* Developer - Builds the _apps_ and gets crentials from the developer _portal_
* Admin 

Attack surface is increased

### Common Web Attacks

* Cross site scripting (XSS) - Malicious script injected into trusted website
* Denial of service - Making a service unavailable by increasing load on the server
* Man in the middle - intercepts communication between systems
* Cross site request forgery (CSRF) - forces a user to do unwanted actions on a website they are authenticated on - trick the user
* SQL Injection - making maliscous SQL through application form
* Overflow

Check the [OWASP Top 10 Security Risks](https://owasp.org/www-project-top-ten/)

### Case Studies

#### Snapchat

Snapchat official application was decompiled and the API key was retrieved.
Unofficial or fake app was created to control the calls.
Calls were made and answers were linked to accounts.

#### Verizon

CSRF attack - cookie based authentication. Users logged in and got a session cookie.
Users were tricked to click external link to access a maliscous website - sharing the cookie.
The maliscous site made a request to verizon with the solen cookie.

#### Nissan Leaf Iphone App

User accessing the API anonymously.
Was possible to access other people's cars by setting the VIN number in the request.

### Mitigating API Threats

* Rate Limiting - prevent Denial of Service attacks (DoS), keep API available for legitimate users
* Message Validation - schema based validationn - change schema without breaking clients
* Encryption and Signing - prevents spoofing and Man-in-the-middle attacks
* Access Control - Restricts usage based on user identity. 
    * Authentication - you are who you say you are?
    * Authorizaiton - you are allowed to do what you want to do (access resource)

### 2008: API Security

* Mostly SOAP
* Applciation Layer: SAML, XACML, Basic Auth, Custom HMAC
* Transport layer: SSL/TLS, Non-secure

### 2020: API Security

* OAuth and OpenID Connect - enable delegated authorization
* Transport Layer: TLS 1.3

### TLS Trust Attacks

* Certificate authority vulnerabilities - CA compromised issuing maliscous 
* Human vulnerabilities - visual cue of the lock
* Man-in-the-middle - impersonation

### HTTP Access control

* Basic Authentication - username and password in request header with every request- base64 encoded (not encrypted)
* Digest Authentication - password is encrypted and server can downgrade to basic

vulnerable to man-in-the-middle attack

### API Security best practices

* Security: authorization and authentication
* check OWASP
* rate limiting
* Continuous API monitoring and API access
* Don't return too much data
* Prevent applications fropm sending traces in error messages

## 2. Introduction to OAuth 2.0

Oauth 2.0 - authorization protocol that permits a user to grent (or delegate) an application access to a protected resource without exposing the user password credential

An OAuth Access token is issued at the API endpoint

A user does not trust the app enough to give it login credentials to another service.

### Analogy

Buying something from a shop using a credit card.
You do not tell the cashier your pin number - you enter it directly into the bank's device.
You protect your resources.

In the API world, an app wants access to your resource you need to grant that app access to the resource.

### Authorization flow - Authorization code 

* User, app and API

1. Register the App with the API: give the api the app name, resource scope and callback url, API returns with client id and secret.
    * Authorization server - Identity provider (keycloak or social login)
    * Resource server - API owner the resources
2. User logs into app -> App makes request to bank's authorization server
3. It redirects the user's browser to the authorization screen of the authorization server
4. Jane logs in and authorizes the app to her resources on the API
5. Authoization server gives the app an `Authorization code`
6. The application then exchanges the authorization code for an access token on the back channel (using the client id and secret)
7. Access token contains the scopes (mechanism limiting an apps access to user account)
8. Application uses access token to access resources on the resource server

**Oauth is not an authnetication protocol**

> Oauth is a deletegated authorization framework

### OAuth 2 Grant Types

* Authorization code - web application needing scoped access on behalf of end user. resource owner credentials are never shared with the client. Most secure grant type - but complex.
* Implicit - Javascript Single Page Application, no authorization code - client gets access token directly.
* Resource owner password credentials - High degree of trust between end user and app. Rarely used.
* Client credentials - client acting on its own behalf via CLI or daemon - doesn't require interaction with the end user. Use for confidential clients.

Oauth2.0 is a framework - it does not tell you exactly how to implement.

### Things not Defined in the Specification

* Token scopes can allow delegated application it does not cover the identity of the end user - covered by OpenID Connect
* How resource server and authorization server communicate
* How client registers with the authorization server
* How the authorization endpoints are discovered
* The semantics of authorization scope

### Pros and Cons

#### Cons

* Leaving open ended decisions opens security holes

#### Pros

* Open for creating now specifications on top of - eg. OpenID Connect

## 3. OpenID Connect Overview

> OAuth 2 was built for authorization - delegated authorization - it doesn't need to know who you are

No way of verifying they are who they say they are - they are considered authneticated

### OpenID Connect Identity

* A set of attributes
* One person can have multiple identities

Each identity has it's own set of attributes - each client has its own attributes it is interested in.

Additional `id_token` is generated along with the access token - an encrypted fingerprint.
Can be decoded to show user information.

The client application can ask for specific innformation -> `claims` as part of authentication.
Any additional information can be defined in the `scope` paramters.

Basic scope parameters:

* email
* profile
* address
* phone

profile parameter has the most variety of claims:

* name
* family_name
* given_name
* middle_name
* nickname
* preferred_username
* profile
* picture
* website
* gender
* birthdate
* zoneinfo
* locale
* updated_at

### Authentication Code Flow

* Similar to authorization code flow but the resource server returns a `access_token` and an `id_token`. Refresh token is also issued.
* Application then exchanges access token and id token

**userinfo endpoint**: is an oauth 2 protected resource that lives in the authorization server - it returns claims about an already authenticated user.

### JWT - Json Web Token

* ID token - a new token that contains claims about authentication status of an end user and auth status
* ID Tokens carry information and are used to retrieve information
* Access tokens are not intended to carry information

### Levels of OpenIDC

* Minimal (Core) - id token, authentication, third pary logins, claims
* Dynamic - discovery request (`.well-known/openidconnect`), 
* Complete - session management, form post response node

## 4. JSON Web Tokens

Token format for securely transmitting information between parties using JSON Objects

Javascript object signing and encryption

* JWT - Json Web Token
* JWS - Json Web Signature
* JWE - Json Web Encryption
* JWA - Json Web Algorithms
* JWK - Json Web Key

When a JWT is signed it verifies the claims made within it. Encryption hides those claims from other parties.

### Anatomy of JWT

* Header - identifies algorithm
* Payload - claims like the issuer, subject, JWT id
* Signature - encoding algorithm specified in the header

### Why use a JWT?

* Proof of identiy and authorization
* Portable
* Can be stored on client
* Message level encryption

SAML uses XML tokens

JSON is less verbose than the XML in a SAMl token - smaller when encoded.

### Stateful vs Stateless?

In SAML Bearer token scenario - server must maintain application state.
Server stores token in token registry.

JWT's are stateless - server validates the client request and generates the JWT ecrypts and signs using private key.
Returns JWT to client. Client makes request to resource server with the JWT. Server validates the token with the private key.

CORS is not an issue as the process does not use cookies

### JWT as an ID Token

* static claims: issuer, subject and audience
* Custom claims

### JWT as an Access Token

* `JTI` - JWT ID Standard claim - unique identifier from the JWT

### JWT as refresh token

* When access token expires can be used to get a new access token

### JWT Advantages

* Signed and encrypted
* statelss and self contained
* compact
* HTTP header or url parameter
* common data format
* ease for HTTP API's

### Challenges

* Token revocation - harder with stateless - setting shorter timeout - setting token refresh and token recreation or revocation list (makes it stateful)
* Data stored in JWT can be viewed in client - anyone who has the signing key can create JWTs

*  Never let the JWT header alone drive verification
* Use custom claims
* Use appropriate key size
* Set appropriate timeout

## 5. Addressing OAuth 2 Threats

* General threat models and best practices:
    * [RFC 6819 - OAuth 2.0 Threat Model and Security Considerations](https://tools.ietf.org/html/rfc6819)  
    * [ID 15 - OAuth 2.0 Security Best Current Practice](https://tools.ietf.org/html/draft-ietf-oauth-security-topics-15)
* Client threats:  
    * [RFC 7591 - OAuth 2.0 Dynamic Client Registration Protocol](https://tools.ietf.org/html/rfc7591)
* Endpoint threats:  
    * [RFC 8414 - OAuth 2.0 Authorization Server Metadata](https://tools.ietf.org/html/rfc8414)  
    * [RFC 7469 - Public Key Pinning Extension for HTTP](https://tools.ietf.org/html/rfc7469)  
    * [RFC 7636 - Proof Key for Code Exchange by OAuth Public Clients](https://tools.ietf.org/html/rfc7636)
* Token threats:  
    * [RFC 7662 - OAuth 2.0 Token Introspection](https://tools.ietf.org/html/rfc7662)  
    * [RFC 7009 - OAuth 2.0 Token Revocation](https://tools.ietf.org/html/rfc7009)  
    * [RFC 8693 - OAuth 2.0 Token Exchange](https://tools.ietf.org/html/rfc8693)  
    * [RFC 8471 - The Token Binding Protocol](https://tools.ietf.org/html/rfc8471)  
    * [RFC 8473 - Token Binding Over HTTP](https://tools.ietf.org/html/rfc8473) (includes JWT Token Binding)  
    * [RFC 7800 - Proof-of-Possession Key Semantics for JWTs](https://tools.ietf.org/html/rfc7800)

Application access control:

* Credential validation should happen server side.
* Implement monitoring and detection
* Establish credentials during client registration

Endpoint threat models:

* Phishing with Couterfeit authorization server
* Interception of traffic
* User unintentionally grants too much access
* Maliscous client obtainng existing authorization
* Open redirection

MITM attack - mitigate with certificate pinning

client saves certificate and key from first transaction

Redirection hijack - implicit grant or authorization code. After successful authnetication redirected somewhere other than the client. Redirect URL's must be whitelisted before hand.

* PKCE - Proof Key for Code Exchange: This implementation can help address the threat of redirect hijacks. In this implementation, the client generates a hashed secret and hashing method and sends them to the authorization server on code request. The secret is then used by the authorization server to verify a subsequent token request. As it requires both the client and server to participate, it helps address vulnerabilities, particularly in mobile apps.

### Token threat models

* Eavesdropping access tokens
* Obtaining access tokens from authorization server db
* Disclosure of client credentials during transmission
* Obtaining client secret from authorisation db
* Obtaining client secret by online guessing

Token binding






















### Sources

* [API Security Architect](https://apiacademy.learnupon.com/enrollments/55559074/details)
