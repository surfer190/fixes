# Keycloak

> Make security easy for application developers

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

## The Problem

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

* OpenID Connect
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










## Questions and Answers

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

## Sources

* [Beyond Basic Auth: Logins for Apps and APIs - Stian Thorgersen](https://vimeo.com/138736740)
* [Floss Weekly: Keycloak](https://twit.tv/shows/floss-weekly/episodes/488)