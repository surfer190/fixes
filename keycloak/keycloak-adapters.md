# Keycloak Adapters

## Built-ins (mostly EE)

There are built in adapters for:

\* Client side javascript (with cordova)
* Wildfly / Jetty / Tomcat
* Fuse
* Node.js
* Servlet filter
* Spring boot / spring security

## Generic Keycloak Adapter

Seperate process on the same host as the application and your service.
On one host is the application with the generic adapter.
On a different host is the application with the generic adapter.

All incoming requests from the user are sent to the generic adapter which deals with the authentication by redirecting it to keycloak.
Once authenticated the generic adapter will forward the request to the application.

For the service it checks the authorization headers in the request and makes sure the request is permitted before it goes to the service.

It can also intercept outgoing requests from the application to add the bearer token from openID connect onto the request so the applicaiton can securly invoke services without modifying the request.

## openshift

Using k8s - pods can have multiple containers.
So you can use a sidecar proxy - both a generic adapter and php adapter in a pod and they can communicate.

* [Keycloak gatekeeper](https://github.com/keycloak/keycloak-gatekeeper)


