---
author: ''
category: Oauth
date: '2020-05-28'
summary: ''
title: Oauth And Openid Connect
---
# OAuth 2.0 and OpenID Connect

## What is Oauth 2?

> The pattern of having an app connect to your master account - delegated authorization. That is **Oauth**.

Forces users to only enter sensitive information (username and password) in one place, the oauth server.
Key that there is a seperation of authorization, keeping user's safe as they never enter their password into the application directly.

## When should you use Oauth2 (and when shouldn't you)

* When you are creating an app in the middle. An app that will use the end user's permissions to preform actions on another app - but will not have any control or access to credentials. The end user will maintain that control and can revoke it at any time.
* It is never used for authentication or identity - although people try to make it work in this scenario. In this case use OpenID Connect.
* When you just want to allow someone to use your api directly, you would not want to use OAuth2.0 - as there is already a trust relationship.

## When should you provide oAuth 2 registration for apps?

* When you want to allow end user's of an app - to give permission to use your API on the user's behalf.
* When that app has user's that have permission / identity on your API
* Allow secure integrations into your API

## What is OpenID Connect?

It is an extension to OAuth that provides Identity.

## When should you use OpenID Connect (and when shouldn't you)

* Centralising Logging in (Authentication)
* Making identity / account available in other systems (Single sign on)
* When you just need authorization / permission and not identity access - you do not need OpenID Connect
* Advantages after centralising auth is that there is no only 1 place to go to add multi-factor authentication. Instead of on each application platform.

## OAuth 2.:  History and the Problem

There is a lot of wiggleroom with the [Oauth spec](https://tools.ietf.org/html/rfc6749) - it is not like HTTP in that there is only 1 way to use it.
You are not alone it is very confusing especially researching it online.

Identity UseCases pre-2010:

* Simple login (forms and cookies)
* Single sign-on across sites (SAML)
* Mobile app login
* Delegated authorization

SAML has a bad reputation as being even more dense and obscure than OAuth.

![Yelp Infamous OAuth Fail](/img/yelp-infamous-oauth-fail.png){: class="img-fluid" }

This is the OAuth Use Case - the problem.

### The Oauth 2.0 Flow

* I trust this app enough to do certain things with my account on another platform.
* Oauth redirects to the actual master domain...eg. accounts.google.com so you are only putting in your password on their domain and then asks to extend permissions to original requester.
* The user must explicitly give permission - so they are not tricked.
* Once permission is given, a redirect goes to the original application/requester...it does some magic and now it can access contacts.google.com. (When registering your app you give it a `redirect_url`)

### OAuth 2.0 Terminology

Bunch of terms that renames things we already have names for

* Resource owner - Owner of the account (holding the data) [Me]
* Client - The application that wants the data [Yelp!]
* Authorization server - System used to give permission [accounts.google.com]
* Resource server - System that holds the data the client wants [contacts.google.com] _sometimes authorization and resource server are the same thing_
* Authorization grant - Proves user has given permission
* Redirect URL / Callback - Where to redirect to after authorization granted [callback.yelp.com]
* Access Token - Key used to gain access to content on the resource server [used by Yelp!]

### Clients

2 Types of clients:

* Confidential: web applciation running in a web server - can protect the client key, client secret
* Public: mobile apps or Single Page Applications (JS) - cannot protect the client secret

### Flows / Grant Types

There are various flows:

* Authorization code flow (front + back channel) - 3 legged flow
* Implict (front channel only) like a Single Page Application - 2 legged flow
* Resource owner password credentials (back channel only) - make older applications work correctly - 2 legged flow
* Client credentials (back channel only) - service communication - 2 legged flow

> Take note that [Resource owner credential grants does not support SSO](https://keycloak.discourse.group/t/one-client-always-prompts-for-username-and-password-oidc/249)

Implicit flow:

Set `response_type=token`

Less secure and no assurance that exchange step happened on the back channel and Token is exposed to the browser.
Can make sense in certain situations.

### Grant type: Authorization code Flow

* The most popular (and secure) OAuth Flow. 
* Used to delegate authorization to an applciation to the master sercer on a user's behalf.
* Used when their is no trusted business relationship between the client application and authorization server
* Optimized for confidential clients
* Best when consent is needed and authorization server does not trust the client application

1. Resource owners performs an action on the client app requiring authorization
2. Client redirect the user to the authorization end point
1. An authorization code is returned to Yelp (client app) from the authorization server with an **authorization code** on the `redirect_url` page. (On the front channel)
2. Yelp (client app) must then make a request to the authorization server (Google) with the authorization code to get an **access token**. (On the back channel)
3. The authorizaton server will return the access token - if the authorization code is still valid.
4. Finally Yelp with use the access token to attach it to the request (and optional refresh token)

### Grant type: Implicit Flow

* Similar to Authorization code flow. Instead of a code an access token is expected.
* Reduces number of round trips need to get the access token
* Dangerous cause the access token might be exposed on the client side
* Used bu Public client because it does not include a client secret or authorization code
* Mobile or single page application

### Grant type: Client Credentials

* Provides a client application a way to access it's own service account
* Used for making backend service calls
* Only used by confidential clients
* Best for Business to Business transactions (no resource owner)

1. Client credentials used to request an access token (POST with `grant_type=client_credentials`)
2. Server returns an access token
3. Further requests are done with the access token, a JWT - in Bearer

example of access token response:

    {
        "token_type": "bearer",
        "expires_in": 3600,
        "access_token": "abcde..."
    }

### Grant type: Resource owner password credentials

* a.k.a Username-password authnetication flow
* when user (resource owner) has a trust relationship with the client application - ie. the client must be able to obtain the user's credentials via a form on the front channel
* maintains backward compatability with OAuth 1.0
* Preferred when you trust the client app - as it handles the resource owner credentials

1. User providers username and password on the client application
2. Client makes a POST to authentication server (`grant_type=password`)
3. Server return access token (with optional refresh token)

### Channels

Why do we need 2 tokens (Authorization code and Access token)? Why can't we just do it in one?

* Back channel - highly secure channel [HTTPS] backend server to another API. direct communication between the app client and authorization server - uses HTTP POST.
* Front channel - less secure channel [Browser] certain things can leak from browser. Happens between users and authorization endpoint - based on HTTP redirects - uses HTTP GET.

The browser is secure but has loop holes - you can view things in the html or js. Someone could also be looking over your shoulder.
The authorization code is transmitted though the browser (front channel) - you can see the code in the query parameters of the request.

The next step in gaining the access token is done on the back channel. 

A person logging network requests could see the requests - they could try and beat you to get the access token - but that can only happen on the back channel.
It is posted along with a secret key that only the server knows.

Communication with the resource server using the access token is only done on the back channel.

### Scope

**How does the client (application) specify what it wants to do?** Like just read contacts and not delete contacts.

Scopes are _granular permissions_.

The list of scope is used by the authorization server to present the consent screen.

Problems through history was that Facebook only had the `can you connect` not more granular permission.
Naturally this lead to apps you gave permission to doing more than they needed.

The initial request from the client (middle app) to the authorization server contains a scope.

### An In Depth Example

1. The first step is always to register your app - with the authorization server (master account).
Where you set the `redirect_url` your app is expecting to receive. YOu get the `client_id` and `client_secret`. `client_id` is not sensitive it is transferred in the front channel - It identifies you to the client server.
2. You then provide a link on your app to start the process like: `connect with google`. That would point to an address on the authorization server:

    https://accounts.google.com/o/oauth2/v2/auth?
    client_id=abc123
    &redirect_uri=https://yelp.com/callback
    &scope=profile
    &response_type=code
    &state=foobar

3. Then receive the authorization code from the OAuth Server with a webhook on your app or using: [Oauthdebugger.com](https://oauthdebugger.com/) to test. You get an authorization code from the callback in the querystring: eg. `https://yelp.com/callback?code=xXxyYy&state=foobar`
4. You can then get the access token on the back channel by making a POST on the back channel for the `access_token`

Exchange for access token:

    POST www.googleapis.com/oauth2/v4/token
    
    code=xXxyYy&client_id=abc123&client_secret=secret123&grant_type=authorization_code

Response would be:

    {
        "access_token": "aAabBb",
        "expires_in": 3920,
        "token_type": "Bearer"
    }

You then use the access token by attaching HTTP Authorization header...with the `Bearer xxxyyy`

## OpenID Connect: History  and the Authentication Problem of OAuth 2.0

The problem is that OAuth 2.0 got over-adopted, it started getting used for:

* Simple login [Authentication]
* Single sign-in across sites [Authentication]
* Mobile app login [Authentication]
* Delegated authorization [Authorization]

_Oauth 2.0 was originally designed for authorization_

> You shouldn't use OAuth for Authentication

Oauth doesn't care who you are, it cares about scopes - what you can do.
Is your access token allowed to do this?

There is nothing in the Oauth Protocol Spec to get the user info - so companies added other hacks - seperate implementations.

So they invested **OpenID Connect** as an extension to Oauth.

It isn't even a seperate protocol, it is a little bit extra on OAuth 2.0.

It adds:

* ID Token - has users information
* User Info Endpoint
* Standard set of scopes
* standardised implementation

### OpenID Connect

* You get same stuff with Oauth 2.0 except you also get `access_token` and `id_token`
* The access token can then call the user info endpoint
* Check the [Oidcdebugger](https://oidcdebugger.com)
* ID Token is a `JWT` - JSON Web Token (Jot)
* A tool that can decode a JWT: [jsonwebtoken.io](https://www.jsonwebtoken.io/)
* Has a header, claims (payload) and signature portion.
8 Signature verifies that the ID token has not been changed in flight.

## Updated Identity Use Cases

Identity Use Cases:

* Simple login (OpenID Connect)
* Single sign-on across sites (OpenID Connect)
* Mobile app login (OpenID Connect)
* Delegated authorization (OAuth 2.0)

OAuth 2.0 is for authorization (delegation):

* Granting access to API
* granting access to user data in other systems

OpenID Connect:

* Logging the user in
* Making account available in other systems

### OpenID Connect: What Flows to Use?

* Web application with server backend: **Authorization Code Flow** - abstract authentication away from rest of the app
* Native mobile app: **Authorization code flow with PKCE**
* Javascript app SPA with API backend: **implicit flow**
* Microservices and API's: **client credentials flow**

SSO with third party services

### Sources

* [Oracle Learning: Oauth Grant Types](https://www.youtube.com/watch?v=1ZX7554l8hY)
* [What is OAuth and why does it matter?](https://www.youtube.com/watch?v=KT8ybowdyr0)
* [Oauth in plain english](https://www.youtube.com/watch?v=996OiexHze0)