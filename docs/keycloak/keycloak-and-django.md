---
author: ''
category: Keycloak
date: '2020-02-14'
summary: ''
title: Keycloak And Django
---
## Keycloak and Django

Install Keyclooak locally

    docker run -d -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=pass jboss/keycloak

Follow the guide here: https://blog.jonharrington.org/static/integrate-django-with-keycloak

## Quickstart

[Full tutotual for using django with keycloak](https://number1.co.za/openid-connect-clients-for-python/)

1. Create a New Realm

2. Create a New Client

    * OpenID Connect
    * Root URL: `http://127.0.0.1:8000/`

3. Get your Client ID and Secret from the client page

4. Get the OpenID Info from the realm page or at:

    http://<keycloak-server>:5000/auth/realms/<realm>/.well-known/openid-configuration


### Sources

* [Connecting Django with Keycloak](https://number1.co.za/openid-connect-clients-for-python/)
* [Integrate Django with Keycloak](https://blog.jonharrington.org/static/integrate-django-with-keycloak)