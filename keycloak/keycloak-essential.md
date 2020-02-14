# Keycloak

> Make security easy for application developers

* Open source
* Identity and Access Management

2 options for securing you applications:
* heavyweight idp solutions
* build your own using frameworks and libraries

## How did it Start

There was a team in JBoss a division of redhat that needed something else to look at.
So they decided to do identity as a service.
It didn't go far as selling it as a product - but traction was acquired in the community.
The open source project got a alot of popularity.

## Authentication the Old Way

A monolithic web app would have a username and password, it would verify credential against a table. A security context is then associated with the HTTP session. The session would then be used for further HTTP requests.
If you wanted to log the person out you need to invlaidate the HTTP session.

## Main Features

* Authentication for the web and applications
* SSO - connect many applications to keycloak server - automatically logged in
* Single sign-out
* Import and Export from a JSON file

## The Problem

> You wouldn't implement a database would you. So why are you implementing your own IAM.

* Have many different applications
* Many versions of systems
* We want to expose these services to public internet
* Make app available to mobile users

Multiple services, multiple user databases, multiple logins outside firewalls.

Often you have copies of users in multiple locations - making users log in to different applications.

These days a password is no longer sufficient - multi-factor auth is required

* Something a user knows
* Something a user has

Many types of apps:

* Web applications
* Mobile
* API's and services

Mobile presents issues because users don't want to log in. It is not good to store the username and password on the phone.

With so many different applications you need **single-sign on**

* Quite hard to get right
* Even worse with different programming languages deployed to different domains
* Also need single sign out
* Also allow remotely sign out - ie. lost phone

Things to manage:
* Apps
* Services
* Users
* Devices
* Permissions
* Session and Logs

Allow for self-service:
* Users can manage their own accounts
* Recover password
* Update profile
* Enable 2-factor auth
* Manage sessions
* Account history

Integration with:
* Third party apps - LDAP, database
* Existing Infrastructure (or new users after an acquisition)
* External Users- give access to users at a partner company
* Social Networks

Also vulnerabilities

> You don't want to build this yourself - it is too complex and is very risky

### Delegate your Security

* Stay DRY (Don't repeat yourself)
* You are not a security expert

[Researchers asked 43 developers to code a user registration for their web app - 26 devs chose to leave the password as plain text](https://www.reddit.com/r/programming/comments/ayoo0q/researchers_asked_43_freelance_developers_to_code/)

You need to create a login screen, you need to manage users - if you do it yourself there are a lot of thing to do:
* New login form
* let user manage profile
* Backend way to check credentials
* Store passwords securely
* Have to manage authorization flows

and you have to do that all over again with a different project - so can't even reuse code for a different programming language

### The Solutions

Use an IAM (Identity and Access Management)

How does a central authentication server work?
It relies on tokens as opposed to sessions and cookies.

1. When a user clicks a login button they are redirected to a login screen on the authentication server
2. The user then enters the username and password - it is submited to the authentication server
3. If two-factor auth is enabled - the authentication server handles this
4. If the credentials are valid the authentication server returns a token to the application

> Credentials are never exposed to applications - they won't be leaked

> Applications also don't need to worry about authentication

It will include the token with the request to the service, the token is signed by the authentication service so the application can verify the request offline (no need to send to the authentication service)

Services can include this token in any request it makes - so services can aggregate and invoke other services.

### Protocols

Keycloak is based on:

* OpenID Connect (Heavy)
* SAML 2.0

#### OpenID Connect

* Built on Oauth 2
* Restful
* Json
* Easy to Use

There are many flows of how users obtain tokens

#### SAML 2.0

* XML
* Harder to use and understand
* SOAP

#### Tokens

* Decouple authentication mechanism from application
* Work well cross domain
* Stateless - all the info you need is embedded in the token itself
* Tokens are only sent in requests that need authntication - not a cookie

### HTML5 Example

All you need to do to log into a HTML 5 application is include the javascript adapter and add:

    <button onclick="keycloak.login()">Login</button>

The JS can be found at:

    https://{{my_keycloak_server}}/auth/js/keycloak.js

### Integration

* Keycloak client adapters (SDK's)
* Keycloak proxy - if no client adapter available - wraps existing services
* Standard OpenID connect or SAML service provider libraries
* Many third party applications have built in support for one of these protocols so you can enable auth with your single-sign on solution

### Keycloak Admin Console

Realm - an encapsulation - you have clients (applications) and users. Each realm's clients and users are isolated from another realms - same for settings.

You can enable different features:

* User registration
* Edit Username
* Forgot Password
* Remember Me
* Verify Email
* Login with Email
* Require SSL

You can configure your email server to send emails to users

Clients: Manage what applications are available

* Manage scope - what permissions an application is allowed - it has a reduced set of permissions it is allowed to ask for
* Can view active sessions

Users: You can manage users

* Impersonate a user
* Set the attributes of the user
* Reset the user's password

Session: Manage sessions

Events: Manage and view events (audit logging)

* Audit admins changing settings

There is also a user login and management interface.

### SSO (Single sign-on)

Keycloak makes it easy to achieve a single signon experience for web applications

* Enterprise/Desktop single sign on bridge - for desktop users logging in using kerberos with an LDAP service or active directory domain.
* Employees log in 1 time a day

Single-sign on demo - opening 2 applications - logging into 1 automatically logs into the other.

#### Other settings

* You can change the theme for users
* Built-in Internationalisation
* Required actions - ensure users do certain things for first login - like accepting terms and conditions
* Set password policies

### Verfication

With a request we send the access token

* Online Verficcation - the keycloak server is called to check the token and say yes or no
* Offline verification with signature - service retrieves the public key from keycloak (in cache) and use this to verify that the token is valid by checking the signature with the public key.

Offline has a window of being disabled or logged out - it does not take immediate effect.

OpenID connect has an access token and a refresh token - usually just a few minutes until the tokens become invalid.
Online approach takes immediate effect but that adds more load on the keycloak and applciation server.



### User Federation

Handy for existing databases

* Sync users from existing directories into keycloak database
* Keycloak will store additional fields
* You can synchronise multiple sources into a single realm
* Performance improvement - keycloak caches

LDAP configuration is a bit cryptic - built in support for various members

Can setup a sync or manually sync

### Identity Brokering

Allow external users to sign in

If your partner has a OpenID connect server they can log into your service with their existing credentials - how?

You set up an identity provider on another realm or another server - when you click login with that provider you will use that provider's theme.

### Mappers

* Specify exactly what goes into a token
* Can remove fields if your application doesn't need it
* Can map attributes from LDAP

# Questions and Answers

**Question**: Can I use keycloak to offer sign in using google?

No. You integrate with keycloak using openID connect - so you are moving your whole authentication to keycloak.
You can include users from your existing database or support from your custom user stores - LDAP or db.

**Question**: Is keycloak a full authentication solution itself or is it just a gateway to use some external authentication service like OpenID or a corporate SAML.

It is a full IDM, a full openID and SAML server.

**Question**: So when someone leaves the company I just delete them off keycloak, I don't need to go and delete them off the external services?

Exactly.

**Question**: What about setting up authorization profiles? Setting up administrator groups or people that have access to personal information.

Yes, we have a complete administration console where you can setup groups and roles.
It also has rest endpoints to automate it.

**Question**: It is important to audit this information...do you have auditing tools?

By default you can turn on our event listener and you can choose what you want to listen to.

**Question**: Is it available as a service on Openshift to use in red hat's cloud?

It is not available as a Saas. You have to self manage it. We do have a product called Single-sign on Openshift and docker containers for Keycloak and all the templates to run keycloak on openshift - in that case it is self-managed.

**Question**: How smart do I have to be to integrate this into a new app?

Not that smart, we strive to make it as simple as possible.
We are going to create an easier getting started experience.

**Question**: Is it set to scale?

We have clustering capabilities from the start, it is built on the wildfly application server which is a full fledged Java EE webserver. We use all the non-EE parts. That let us focus on the identity part.

**Question**: Say I have an existing system, how hard would it be to integrate this into the auth system of mediaWiki?

If it supports OpenID connect or supports SAML or plugin does either of those then you can secure it with keycloak.
The difficulty depends. OpenID connect has more traction, it has a well known discovery endpoint - a single url to get all the metadta of an openID provider.

**Question**: We have systems, we need IAM.We are using LDAP, could we put Keycloak in front of LDAP as an easy way to migrate to a more lightweight solution.

Yes, that works depending on your LDAP provider. LDAP has strange behaviour that differs from vendor to vendor.

> If you have an LDAP with keycloak is the perfect solution to do a slow migration.

Keycloak will mask the complexity. Your app will be speaking to keycloak and you will obtain a JOT token from OpenID connect - which is json.

**Question**: Suppose I want to remove my old LDAP servers? Can keycloak emulate an LDAP server for legacy apps?

No, we want to avoid feature creep.
If you want LDAP you migrate from old LDAP to something like Apache DS. Then keycloak can use 2 LDAPS.

**Question**: Security as a Service?

There is not enough money in it to get value back.

**Question**: Do you do anything to stop companies storing passwords in clear text?

Yes. We decide how you store your password. Secure hashing is done by keycloak.

## Architecture

You have the keycloak server then for each application you secure you have to install a small library - called an adapter to speak to the leycloak server.

Common use case is using it to redirect to the keycloak login screen, you then login and get a token and redirect back to the app. You can then use this token for any service secured with keycloak.

# Tutorial

## Create a Client

A client is created to allow that application to authenticate with keycloak.

You can't log in, if there are no users in your realm

You can add a new user as an admin, but we can also let users self register to the application.

You can allow user registrations in the realm settings

We want them to verify their email

You can create additional attributes on the user but it needs to be mapped to the token.
We do that by creating a client scope.
A client scope lets you create elements to your token shared between multiple clients.

Create the scope then click `Mappers` at the top.
Create a protocol mapper that lets you map things into the token.

Can choose to add it just to the access token or just to the id token

You can then go to the `Client` and choose the `Client scopes` available to that client.

> You should limit the number of client scopes in a token

Tokens might become very large and token contains more claims than application can see - compromised client.

The application can take the avatar url out of the token and display it on the page

You can require consent from the user to access certain scopes

Roles: simple and composite roles

A default role added to all registered users you can then add other roles to this composite role for all users.

Can map the role to the user

On the client we don't want `Full scoped allowed` - meaning client has access to all the roles a user has.
No knowledge of roles in the token.
Frontend service will invoke backend services to check.

Groups - allows to add attributes and roles to users. Can also use groups directly.

Can assign roles - so all users part of a group get a specific role.

Also all users part of that group have specific attributes.
Ensure the user is part of that group.
Keycloak is aware but it must also be mapped into the token.

Add a group membership protocol mapper - to map group memberships to the token.

## How to Get Users in from another source

Use an `ldap` or `kerberos` server.

Edit mode: `WRITABLE` edit the users and have it written back to the LDAP server.
Could also choose `READ_ONLY`.
`UNSYNCED` - keycloak keeps the changes but does not write them back to LDAP.

Vendor: `other` - prefills alot of settings

Set and Test the connection url
Tell keycloak where in the diretory to find users
Tell keycloak how to authenticate - Test that authentication works
Save it.

You can have users loaded on demand or you can synchronize it all in one go.
You can also synchronize only the changed users.

Users will now be in the system and the federation link will point to LDAP.

## Identity Brokering

Keycloak allows authentication via an external SAML v2.0 or OpenID Connect provider (as well as social networks)

There is now an option to log in via one of those options

Identity Provider Mappers lets you map an attribute from github into the user on keycloak

## Login Screen

It is styled to match the keycloak styling, you want to change it to match your corporate branding.
Go to `Realm Settings -> Theme`

## Token Signature Algorithm

You can change the client signature algorithm on a per client basis.

## Session

Each token issued by keycloak are associated with an SSO session.
You can logout a logged in user.

## Events

Auditing events.
Can create your custom event listeners.

# Keycloak and webservice security

Logging in to keycloak server you get 3 tokens:

* ID Token
* Access Token - lasts 5 minutes
* Refresh Token - used to obtain a fresh access token

User logs into application and now has JwT access token.
JWT - token contains payload (Json Web Tokens)
With that token he can call any token and service will verify the token

Keycloak has a private key that it uses to sign your token
Your service has access to the public. With the public key it can verify the token.

It can verify offline or in a less trusted environment you can always ask keycloak to verify the token. Many requests to keycloak verification.

Microservices - when your service needs to call another service 

## Keycloak Gatekeeper

Not all applications support OpenID Connect, gatekeeper is a OIDC compatible reverse proxy.

## Use Cases

### Give the user an image

On keycloak add a new attribute to the `user`:

    avatar_url=https://my-image.org

Now keycloak knows the `avatar_url` but the client does not. You can let the client know with a client scope.

1. Create a new client scope

2. Create a mapper to map keycloak attributes into the token

`Mapper Type` is `User Attribute`

It also lets you decide where to put the token - in access or id.

3. Give the client scope access to the new mapper

> You can also add attribute to groups

### Only Allow users to login with an email link

1. On the authentication page remove the Username and password form

2. Add a new method `Magic Link` and mark it as required

3. Set the new approach as the one for browser logins

### Authorization

You want to allow a user to authenticate, but not to do admin tasks.

1. Do not grant that user the admin role


## Sources

* [Beyond Basic Auth: Logins for Apps and APIs - Stian Thorgersen](https://vimeo.com/138736740)
* [Floss Weekly: Keycloak](https://twit.tv/shows/floss-weekly/episodes/488)