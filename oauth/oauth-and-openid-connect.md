## OAuth 2.0 and OpenID Connect

There is a lot of wiggleroom with the Oauth spec - it is not like HTTP in that there is only 1 way to use it.
You are not alone it is very confusing espescially researching it online.

Identity UseCases pre-2010:
* Simple login (forms and cookies)
* Single sign-on across sites (SAML)
* Mobile app login
* Delegated authorization

SAML has a bad reputation as being even more dense and obscure than OAuth.

The pattern of having an app connect to your master account - delegated authorization. That is **Oauth**.

![Yelp Infamous OAuth Fail](/assets/yelp-infamous-oauth-fail.png)

This is the OAuth Use Case - the problem.

## The Flow

I trust them enough to do certain things.

Oauth redirects to the actual master domain...eg. accounts.google.com so you are only putting in your password on their domain and then asks to extend permissions to original requester.

Must explicitly give permission - so you are not tricked.

Once permission is given, a redirect goes to the original application/requester...it does some magic and now it can access contacts.google.com.

## OAuth 2.0 Terminology

Bunch of terms that renames things we already have names for

* Resource owner - Owner of the account (holding the data) [Me]
* Client - The application that wants the data [Yelp!]
* Authorization server - System used to give permission [accounts.google.com]
* Resource server - System that holds the data the client wants [contacts.google.com] _sometimes authorization and resource server are the same thing_
* Authorization grant - Proves user has given permission
* Redirect URL / Callback - Where to redirect to after authorization granted [callback.yelp.com]
* Access Token - Key used to gain access to content on the resource server [used by Yelp!]

## Authorization flow

An authorization code is returned to Yelp with an **authorization code** on the `redirect_url` page.
Yelp must then make a request to the authorization server Google to get an **access token**. The authorizaton server will return the access token - if the authorization code is still valid.

Finally Yelp with use the access token to attach it to the request.

## Channels

Why do we need 2 tokens (Authorization code and Access token)? Why can't we just do it in one?

* Back channel - highly secure channel [HTTPS] backend server to another API
* Front channel - less secure channel [Browser] certain things can leak from browser

Browser is secure but has loop holes - you can view things in the html or js. Someone could also be looking over your shoulder.

The authorization code is transmitted though the browser (front channel) - you can see the code in the query parameters of the request.

The next step in gaining the access token is done on the back channel. 

A person logging network requests could see the requests - they could try and beat you to get the access token - but that can only happen on the back channel.
It is posted along with a secret key that only the server knows.

Communication with the resource server using the access token is only done on the back channel.

## Scope

**How does the client (application) specify what it wants to do?** Like just read contacts and not delete contacts.

We need granular permission.

> These are called Scopes

The list of scope is used by the authorization server to present the consent screen.

Facebook only had the `can you connect` not more granular permission.

The initial request from the client to the authorization server contains a scope.

## In Depth

The link to start the process `connect with google` or login with google.
It would point to an address on the authorization server:

    https://accounts.google.com/o/oauth2/v2/auth?
    client_id=abc123
    &redirect_uri=https://yelp.com/callback
    &scope=profile
    &response_type=code
    &state=foobar

You would need a one step to create a client, you get a:

* client_id
* client_secret

That identifies you to the authorization server

Client_id is not sensitive it is transferred in the front channel

You can use: [Oauthdebugger.com](https://oauthdebugger.com/) to test

You get an authorization code from the callback in the querystring

You can then get the access token on the back channel

    https://yelp.com/callback?code=xXxyYy&state=foobar

Exchange for access token:

    POST www.googleapis.com/oauth2/v4/token
    
    code=xXxyYy&client_id=abc123&client_secret=secret123&grant_type=authorization_code

Response would be:

    {
        "access_token": "aAabBb",
        "expires_in": 3920,
        "token_type": "Bearer"
    }

You then use the access token bu attaching HTTP Authorization header...with the `Bearer xxxyyy`

## Flows

There are various flows:

* Authorization flow (front + back channel)
* Implict (front channel only) like a Single Page Application
* Resource owner password credentials (back channel only) - make older applications work correctly
* Client credentials (back channel only) - service communication

> Take not that [Resource owner credential grants does not support SSO](https://keycloak.discourse.group/t/one-client-always-prompts-for-username-and-password-oidc/249)

Implicit flow:

Set `response_type=token`

Less secure and no assurance that exchange step happened on the back channel and Token is exposed to the browser.
Can make sense in certain situations.

## Authentication Problem

The problem is that OAuth 2.0 got over-adopted, it started getting used for:

* Simple login [Authentication]
* Single sign-in across sites [Authentication]
* Mobile app login [Authentication]
* Delegated authorization [Authorization]

_Oauth 2.0 was originally designed for authorization_

> You shouldn't use OAuth for Authentication

Oauth doesn't care who you are, it cares about scopes - what you can do.
Is your access token allowed to do this.

There is nothing in the Oauth Protocol to get the user info - so companies added other hacks - seperate implementations.

So they invested **OpenID Connect** as an extension to Oauth.

It isn't even a seperate protocol, it is a little bit extra on OAuth 2.0.

It adds:
* ID Token - has users information
* User Info Endpoint
* Standard set of scopes
* standardised implementation

### OpenID Connect

You get same stuff with Oauth 2.0 except you also get `access_token` and `id_token`

The access token can then call the user info endpoint

Check the [Oidcdebugger](https://www.youtube.com/watch?v=996OiexHze0)

ID Token is a `JWT` - JSON Web Token (Jot)

A tool that can decode it: [jsonwebtoken.io](https://www.jsonwebtoken.io/)

Has a header, claims (payload) and signature portion.

Signature verifies that the ID token has not been changed in flight.

## Updated Identity Use Cases

Identity UseCases:
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

## What Flows to Use?

* Web application with server backend: **Authorization Code Flow** - abstract authentication away from rest of the app
* Native mobile app: **Authorization code flow with PKCE**
* Javascript app SPA with API backend: **implicit flow**
* Microservices and API's: **client credentials flow**

SSO with third party services




