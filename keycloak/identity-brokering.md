## Identity Brokering

You use some other systems identity provider - that is SAML or OpenID Connect.

Ie. You can use the Azure AD identity provider or a social identity provider.

You will need to do some setup on the identity providers side.

You get the `client_id` and `client_secret`

You can then use a mapper to map stuff from the identity provider into the user on keycloak.

Now there is an option to login with the identity provider.

