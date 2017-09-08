# Django Social Authentication

OAuth - Open standard of authentication between systems

First we need to generate oauth tokens on the source of truths site (in our case github)

Callback URL is the url the user is sent to after a user has been authorized

For `all-auth` it is:

        http://127.0.0.1:8000/github/login/callback/

Client ID: bcefd842ae02f725686e
Client Secret: 04dd2f3b170af8cdb11a5cde9f8ecc4bf7fc98db

## Installing AllAuth

        pip install django-allauth

## Add Settings

But better to just [read the docs](https://django-allauth.readthedocs.io/en/latest/installation.html#django)

Add `AUTHENTICATION_BACKENDS` to `settings.py`:

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.authbackends.AuthenticationBackend'
    )

Add the following apps to `INSTALLED_APPS`:

        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialauth',
        'allauth.socialauth.providers.github',

Set `SITE_ID` to share authentication across domains:

        SITE_ID = 1

Add `allauth` url's:

        url(r"^accounts/", include("allauth.urls")),

Migrate

## Do

Login to the django admin section and add a site with correct domain name

Add a social applciation

Add client is and client secret

## Tempalte

Add tempalte tags: `{% raw %}{% import socialaccount %}{% endraw %}`

Add provider login: 

        <li><a href="{% raw %}{% provider_login_url 'github' %}{% endraw %}" class="btn btn-simple">Your Account</a></li>

## Ensure email is verified and given

Add to `settings.py`:

        ACCOUNT_EMAIL_REQUIRED = True

        ACCOUNT_EMAIL_VERIFICATION = True

        ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

We will need to add some templates though