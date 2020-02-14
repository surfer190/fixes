## Keycloak Multitenancy

Is it possible to have a realm that can see and manage other realms? Like submasters?

That is not possible directly.
However you can use the identity brokering to allow users from different realms to authenticate within a realm to manage it.
