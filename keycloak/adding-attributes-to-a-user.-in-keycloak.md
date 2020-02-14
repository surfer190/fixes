Often you want to store some information about the user.

Sometimes it makes sense to store that on the application (client) itself - in it's own db.
However when the information is needed by many clients, then it makes sense to add this information on keycloaks database for the user.

## User Attributes

You do this by adding user attributes.

1. Go to `Manage -> Users`
2. Click on the user
3. Click the `Attributes` tab
4. Add a ket value pair.

![Adding User Attributes to Keycloak User](/assets/keycloak/user-attributes.png)

## Client Scopes

At this point keycloak knows about this attribute.

The application does not see the attribute though.

It needs to be mapped into the token for the client, that is done with a **Client Scope**.
A client scope lets you add a reusable scope that can be used by many clients.

1. Go to `Configure -> Client Scopes` and click `Create`
2. Set the name, protocol and consent screen text

Now you have an empty scope, you need to add mappers to map things in keycloak into the token.

1. On the scope, click the `Mappers` tab and click `Create`
2. Make the mapper type a `User Attribute`
3. Set the `User Attribute` to the same as the attribute you created
4. Change the JSON type accordingly
5. Choose where you want the token issued

> You must specify the `Token Claim Name` for it to show up in the token data on the client

Give the client access to the client scope

1. Go to the `Client`
2. Go to the `Client Scopes` tab
3. View the `Available Client Scopes` and Add it to `Assigned Scopes`
