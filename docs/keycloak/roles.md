---
author: ''
category: Keycloak
date: '2020-02-14'
summary: ''
title: Roles
---
# Roles

* Simple roles
* Composite roles - add to a group of users 

## Create a role

1. Click `Roles` on the left side and `Create a role`

## Add a role to a user

1. Go to the user

2. Click on `Role Mappings` tab

3. Add that role to the user

## Access Token

Now if you check the applcation and view the access token, it will contain the roles.

> Important: The role is only added to the access token

In `JS Console` under scope you have `Full Scope Allowed` which gives hte client access to all scopes.

This is not something you would want to use in production.
You want minimum access given.

Only the roles of the user will be shown
