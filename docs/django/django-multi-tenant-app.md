---
author: ''
category: Django
date: '2020-06-14'
summary: ''
title: Django Multi Tenant App
---
# Django Multi-tenant Applications

## What is a Multi-tenant app

A single application that serves multiple customers, each customer's data is completely seperate and is called a tenant.

## Common Approaches to Multi-tenancy

#### Shared Database with shared schema

A single schema in a single db, the `ForeignKey` identifies the tenant.

Negatives:

* Weak separation of tenant data
* Tenant isolation code is intermixed with app code

#### Shared Databse with isolated schema

A single database keeps the tenant's data. Each tenants data is in a seperate schema within a single db.

#### Isolated databse with shared App Server

Database identifies the tenant

#### Completely isolated tenants using Docker

A new set of docker containers are launched for each tenant. A set of containers identifies the tenant.

#### Sources

* [Django Multi Tenant Book](https://books.agiliq.com/projects/django-multi-tenant/en/latest/index.html)
