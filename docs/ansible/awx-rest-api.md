---
author: ''
category: Ansible
date: '2020-05-28'
summary: ''
title: Awx Rest Api
---
# AWX: Rest API Docs

REST - Representation State Transfer

* Stateless
* Client - server
* Over HTTP using HTTP verbs and resources for crud operations
* Hypermedia - links

### Api Visualisers

To visualise the API calls being made use the built in network inspect in you browser's developer tools or one of these:

* https://www.charlesproxy.com/
* https://www.telerik.com/fiddler
* https://mitmproxy.org/
* https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/
* https://sourceforge.net/projects/paros/

## Browsabel API

AWX provides a browsable API (brought to you by DRF), it is at:

    http://<Tower server name>/api/

There are 2 versions, `v1` will be removed in future releases.

### Resources

The resources in `v2`:

    {
        "ping": "/api/v2/ping/",
        "instances": "/api/v2/instances/",
        "instance_groups": "/api/v2/instance_groups/",
        "config": "/api/v2/config/",
        "settings": "/api/v2/settings/",
        "me": "/api/v2/me/",
        "dashboard": "/api/v2/dashboard/",
        "organizations": "/api/v2/organizations/",
        "users": "/api/v2/users/",
        "projects": "/api/v2/projects/",
        "project_updates": "/api/v2/project_updates/",
        "teams": "/api/v2/teams/",
        "credentials": "/api/v2/credentials/",
        "credential_types": "/api/v2/credential_types/",
        "credential_input_sources": "/api/v2/credential_input_sources/",
        "applications": "/api/v2/applications/",
        "tokens": "/api/v2/tokens/",
        "metrics": "/api/v2/metrics/",
        "inventory": "/api/v2/inventories/",
        "inventory_scripts": "/api/v2/inventory_scripts/",
        "inventory_sources": "/api/v2/inventory_sources/",
        "inventory_updates": "/api/v2/inventory_updates/",
        "groups": "/api/v2/groups/",
        "hosts": "/api/v2/hosts/",
        "job_templates": "/api/v2/job_templates/",
        "jobs": "/api/v2/jobs/",
        "job_events": "/api/v2/job_events/",
        "ad_hoc_commands": "/api/v2/ad_hoc_commands/",
        "system_job_templates": "/api/v2/system_job_templates/",
        "system_jobs": "/api/v2/system_jobs/",
        "schedules": "/api/v2/schedules/",
        "roles": "/api/v2/roles/",
        "notification_templates": "/api/v2/notification_templates/",
        "notifications": "/api/v2/notifications/",
        "labels": "/api/v2/labels/",
        "unified_job_templates": "/api/v2/unified_job_templates/",
        "unified_jobs": "/api/v2/unified_jobs/",
        "activity_stream": "/api/v2/activity_stream/",
        "workflow_job_templates": "/api/v2/workflow_job_templates/",
        "workflow_jobs": "/api/v2/workflow_jobs/",
        "workflow_approvals": "/api/v2/workflow_approvals/",
        "workflow_job_template_nodes": "/api/v2/workflow_job_template_nodes/",
        "workflow_job_nodes": "/api/v2/workflow_job_nodes/"
    }

### Conventions

* Requests should end in `/` otherwise they are redirected with a `301`


### Querying

Getting data

    GET http://<Tower server name>/api/v2/groups/

Getting data in order

> Use `order_by` query parameter

    http://<Tower server name>/api/v2/groups?order_by={{ order_field }}

* To sort in reverse order prefix with a `-`
* Multiple sorting is seperated with a `,`

### Searching

> Use the `search` query parameter

    http://<Tower server name>/api/v2/groups?search={{ query_term }}

Search accross related fields with `related__search`

    http://<Tower server name>/api/v2/model_verbose_name?related__search={{ query_term }}

### Filtering

Contains: use `field__contains={{ term }}`

    http://<Tower server name>/api/v2/groups/?name__contains=foo

Exact match: use `field={{ term }}`

    http://<Tower server name>/api/v2/groups/?name=foo

Casting to integer

    http://<Tower server name>/api/v2/groups/?x__int=5

Related resources: All users that contain `kim` in name

    http://<Tower server name>/api/v2/users/?first_name__icontains=kim

Filter on multiple fields

    http://<Tower server name>/api/v2/groups/?name__icontains=test&has_active_failures=false

It uses the [django queryset filtering conventions](https://docs.djangoproject.com/en/dev/ref/models/querysets/)

Special characters should be url encoded:

    ?field=value%20xyz

fields (in the db) can span relationships:

    ?other__field=value

Exclude criteria

    ?not__field=value

Using `and` and `or`:

    ?or__field=value&or__field=othervalue
    ?or__not__field=value&or__field=othervalue

Chain related:

    ?chain__related__field=value&chain__related__field2=othervalue
    ?chain__not__related__field=value&chain__related__field2=othervalue

#### Field Lookups

    ?field__lookup=value


* `exact`: Exact match (default lookup if not specified).
* `iexact`: Case-insensitive version of exact.
* `contains`: Field contains value.
* `icontains`: Case-insensitive version of contains.
* `startswith`: Field starts with value.
* `istartswith`: Case-insensitive version of startswith.
* `endswith`: Field ends with value.
* `iendswith`: Case-insensitive version of endswith.
* `regex`: Field matches the given regular expression.
* `iregex`: Case-insensitive version of regex.
* `gt`: Greater than comparison.
* `gte`: Greater than or equal to comparison.
* `lt`: Less than comparison.
* `lte`: Less than or equal to comparison.
* `isnull`: Check whether the given field or related object is null; expects a boolean value.
* `in`: Check whether the given field’s value is present in the list provided; expects a list of items. (comma seperated)


Boolean values may be specified as `True` or `1` for true, `False` or `0` for false (both case-insensitive).
Null values may be specified as `None` or `Null` (both case-insensitive), though it is preferred to use the `isnull` lookup to explicitly check for null values.

Test filtering on a certain user's role level:

* `role_level`: Level of role to filter on, such as admin_role

### Pagination

Responses are paginated you get back something like this:

    {'count': 25, 'next': 'http://testserver/api/v2/some_resource?page=2', 'previous': None, 'results': [ ... ] }

To get the next page, make a query to the `next` link

Use `page_size=XX` to change the number of results for each request - with a defualt max of `200`. That max can be changed in config.

Retrieve a particular page with the `page` query parameter:

    http://<Tower server name>/api/v2/model_verbose_name?page_size=100&page=2

### Accessing Resources

In Tower 3.1 and 3.2 you could only access resources with their `pk`:

    /api/v2/hosts/2/

In newer versions you can access resources with their names:

    /api/v2/hosts/host_name++inv_name++org_name/

The configuration is accessible at:

    /api/v2/settings/named-url/

More info on [named resource configuration in the docs](https://docs.ansible.com/ansible-tower/latest/html/towerapi/access_resources.html#configuration-settings)

### API Reference

The [awx api reference](https://docs.ansible.com/ansible-tower/latest/html/towerapi/api_ref.html#/) is available

### Authenticating

THere are various methods for [authenticating on ansible tower / awx](https://www.ansible.com/blog/summary-of-authentication-methods-in-red-hat-ansible-tower):

1. Session Authentication
2. Basic Authentication
3. OAuth 2 Token Authentication
4. SSO (single sign on) - SAML, LDAP (SSO), github, Azure AD, Radius, Google oAuth

Under Oauth there is the following methods for obtaining an access token:

* Personal access tokens (PAT)
* Application Token: Password grant type
* Application Token: Implicit grant type
* Application Token: Authorization Code grant type

If another application is interfacing with Tower/AWX - but you want users in AWX/Tower to allow permission to the app - then you want to use OAuth and the authorization code flow.

To set that up look at the [admin docs on token based authnetication](https://docs.ansible.com/ansible-tower/latest/html/administration/oauth2_token_auth.html)

#### An B2B application using Ansible

Usually you would use the OAuth Client Credentials flow. However this flow is not Oauth.
It is simple personal access Tokens - token auth. Or am I wrong?

After creating a user on awx. Make a request for a token:

    http -a username:password POST https://<tower-host>/api/v2/tokens/

Response:

    HTTP/1.1 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Connection: keep-alive
    Content-Language: en
    Content-Length: 486
    Content-Security-Policy: default-src 'self'; connect-src 'self' ws: wss:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' *.pendo.io; img-src 'self' *.pendo.io data:; report-uri /csp-violation/
    Content-Type: application/json
    Date: Wed, 27 May 2020 10:22:33 GMT
    Location: /api/v2/tokens/1/
    Server: openresty/1.15.8.1
    Strict-Transport-Security: max-age=15724800; includeSubDomains
    Vary: Accept, Accept-Language, Origin, Cookie
    X-API-Node: awx-bd8bbc7-79rq5
    X-API-Time: 0.766s
    X-API-Total-Time: 1.206s
    X-Content-Security-Policy: default-src 'self'; connect-src 'self' ws: wss:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' *.pendo.io; img-src 'self' *.pendo.io data:; report-uri /csp-violation/
    X-Frame-Options: DENY
    {
        "application": null,
        "created": "2020-05-27T10:22:32.433229Z",
        "description": "",
        "expires": "3019-09-28T10:22:32.425120Z",
        "id": 1,
        "modified": "2020-05-27T10:22:32.499876Z",
        "refresh_token": null,
        "related": {
            "activity_stream": "/api/v2/tokens/1/activity_stream/",
            "user": "/api/v2/users/13/"
        },
        "scope": "write",
        "summary_fields": {
            "user": {
                "first_name": "",
                "id": 13,
                "last_name": "",
                "username": "api"
            }
        },
        "token": "MgsDkwXRP9bX4NQmh4cIoQomVn2ax9",
        "type": "o_auth2_access_token",
        "url": "/api/v2/tokens/1/",
        "user": 13
    }

Use the `token` in the response for further requests, like getting all jobs:

    http GET https://<tower>/api/v2/jobs/ Authorization:"Bearer MgsDkwXRP9bX4NQmh4cIoQomVn2ax9"

### Launching a Job

To [launch a job ](https://docs.ansible.com/ansible-tower/3.2.6/html/towerapi/launch_jobtemplate.html)

Get the specific job template launch:

    http GET https://<tower>/api/v2/job_templates/12/launch/ Authorization:"Bearer MgsDkwXRP9bX4NQmh4cIoQomVn2ax9"

Inspect the response for the required variables:

* `passwords_needed_to_start`: List of passwords needed
* `credential_needed_to_start`: Boolean
* `inventory_needed_to_start`: Boolean
* `variables_needed_to_start`: List of fields that need to be passed inside of the extra_vars dictionary
* `ask_variables_on_launch`: Boolean specifying whether to prompt the user for additional variables to pass to Ansible inside of extra_vars
* `ask_tags_on_launch`: Boolean specifying whether to prompt the user for job_tags on launch (allow allows use of skip_tags for convienience)
* `ask_job_type_on_launch`: Boolean specifying whether to prompt the user for job_type on launch
* `ask_limit_on_launch`: Boolean specifying whether to prompt the user for limit on launch
* `ask_inventory_on_launch`: Boolean specifying whether to prompt the user for the related field inventory on launch
* `ask_credential_on_launch`: Boolean specifying whether to prompt the user for the related field credential on launch
* `survey_enabled`: Boolean specifying whether to prompt the user for additional extra_vars, following the job template’s survey_spec Q&A format

Ensure that you have gathered all the required variables then launch the job:

    http POST https://<tower>/api/v2/job_templates/<your job template id>/launch/
    
with the required variables:

* `extra_vars`: A string that represents a JSON or YAML formatted dictionary (with escaped parentheses) which includes variables given by the user, including answers to survey questions
* `job_tags`: A string that represents a comma-separated list of tags in the playbook to run
* `limit`: A string that represents a comma-separated list of hosts or groups to operate on
* `inventory`: A integer value for the foreign key of an inventory to use in this job run
* `credential`: A integer value for the foreign key of a credential to use in this job run


### Source

* [AWX API Docs](https://docs.ansible.com/ansible-tower/latest/html/towerapi/index.html)