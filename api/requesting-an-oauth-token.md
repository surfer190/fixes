## Requesting an Oauth token for API calls

Ever tried to request an oauth token and receive this error

    {'error': 'unsupported_grant_type'}

Yet you are sending `password` as the auth type?

    response = requests.post(
        'https://{base_url}/token',
        json={'grant_type':'password', 'username': 'my_user', 'password': 'my_password'},
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        verify=False
    )

THe problem is: **It is part of the oauth spec that you use `application/x-www-form-urlencoded` as the content type of your token request**

Here is a link to a [draft oauth spec](https://tools.ietf.org/id/draft-ietf-oauth-v2-12.xml)

So if we change the above request from using `json` to `application/x-www-form-urlencoded`:

    response = requests.post(
        'https://{base_url}/token',
        data={'grant_type':'password', 'username': 'my_user', 'password': 'my_password'},
        headers={'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
        verify=False
    )

The [full OAuth Authorization framework spec RFC](https://tools.ietf.org/html/rfc6749)
