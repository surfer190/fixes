---
author: ''
category: Oauth
date: '2020-08-13'
summary: ''
title: Difference Between Grant And Scope
---
## Oauth: Difference between Grant and Scope

I have been using Oauth and OpenIDC for some time now but still can't wrap my head around the permissions.

It seems as though group based permissions and fine grained permissions you find in the native django auth package is significantly different from the `django-oauth-toolkit` scopes.
They don't appear to integrate with each other at all - which is a shame.

Also grants and scopes...what is the difference?

### Grants vs Scopes?

#### Grants

Grants are flows. They are used interchangable. The various authorization flows allowed in Oauth.

There are 4:

* `Authorization code Grant` - web application needing scoped access on behalf of end user. resource owner credentials are never shared with the client. Most secure grant type - but complex.
* `Implicit Grant` - Javascript Single Page Application, no authorization code - client gets access token directly.
* `Resource owner password credentials` - High degree of trust between end user and app. Rarely used.
* `Client credentials` - client acting on its own behalf via CLI or daemon - doesn’t require interaction with the end user. Use for confidential clients. Primarily for server to server communication.

#### Scopes

[Scope](https://oauth.net/2/scope/) is a mechanism in OAuth 2.0 to limit an application's access to a user's account

This is what the user gives consent to the application to access.

In the client credentials flow - it does not make as much sense - as there is no delegation of authorization happening.





