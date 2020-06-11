## Keycloak Single Sign Out

How do you provide single sign out or log out with keycloak?

What this means is when you issue a log out from one application or client that is logged in with keycloak, all other open sessions will be terminated.

According to the [mozzila-oidc-django package](https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html#log-user-out-of-the-openid-connect-provider), support for ending a session is not part of the OpenID Connect specification.

However the flow would work something like this:

1. Be a logged in user on the client
2. Click logout on the client
3. Client sends logout request to keycloak
4. Keycloak terminates all open sessions
5. You are now logged out on all clients

### How the signout happens on the client

In the docs on [admin url configuration](https://www.keycloak.org/docs/latest/securing_apps/#admin-url-configuration).
This url is where keycloak sends backchannel requests to achieve certain things like logout.

The steps for logout are:

1. User sends logout request from one application
2. The application sends logout request to Keycloak
3. The Keycloak server invalidates the user session
4. The Keycloak server then **sends a backchannel request to application with an admin url that are associated with the session**
5. When an application receives the logout request it invalidates the corresponding HTTP session

> This process is done for all the linked clients with an admin url - I believe.

### Sending the Logout Request on Keycloak

The [keycloak documentation on logout](https://www.keycloak.org/docs/latest/securing_apps/index.html#logout) says you must should redirect the browser to:

    http://auth-server/auth/realms/{realm-name}/protocol/openid-connect/logout?redirect_uri=encodedRedirectUri

So ensure to redirect the browser to that address.

### Example Code for Django

urls:

    urlpatterns = [
        ...
        path('logout', views.keycloak_logout, name='logout'),
    ]

view:

    from django.conf import settings
    from django.contrib import auth
    from django.http import request
    from django.http import HttpResponseRedirect

    from mozilla_django_oidc.utils import is_authenticated

    def get_logout_url(request):
        '''
        Return the url of the logout for keycloak
        '''
        keycloak_redirect_url = settings.OIDC_OP_LOGOUT_ENDPOINT or None
        return keycloak_redirect_url + "?redirect_uri=" + request.build_absolute_uri("/")
        

    def keycloak_logout(request):
        '''
        Perform the logout of the app and redirect to keycloak
        '''
        django_logout_url = settings.LOGOUT_REDIRECT_URL or '/'

        if is_authenticated(request.user):
            logout_url = get_logout_url(request)

            # Log out the Django user if they were logged in.
            auth.logout(request)

            return HttpResponseRedirect(logout_url)
            
settings:

    OIDC_OP_LOGOUT_ENDPOINT = "http://{{ my-realm }}/auth/realms/my-realm/protocol/openid-connect/logout"
    OIDC_OP_LOGOUT_URL_METHOD = "portal.views.keycloak_logout"

## Single Sign Out Not Working

If single sign out is not working, make sure the certificates of the hosts you are using are valid

You will get an error in the keycloak logs if they do not work:

    08:18:22,410 WARN  [org.keycloak.protocol.saml.SamlProtocol] (default task-27) failed to send saml logout: javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target

