---
author: ''
category: API
date: '2022-05-30'
summary: ''
title: Graphene GraphQL Library for Python
---

## Graphene GraphQL Library for Python

### What is GraphQL?

* GraphQL is a query language for your API, and a server-side runtime for executing queries using a type system you define for your data
* A GraphQL service defines types and fields on those types - then functions for each type on each field

A graphQL service that tells you who the logged in user is and the username of that user:

    type Query {
      me: User
    }

    type User {
      id: ID
      name: String
    }

Along with functions for each field on each type:

    function Query_me(request) {
      return request.auth.user;
    }

    function User_name(user) {
      return user.getName();
    }

Once the service is running - it can receive graphQL queries to validate and execute.

    {
      me {
        name
      }
    }

Could return:

    {
      "me": {
        "name": "Luke Skywalker"
      }
    }

### What is Graphene?

* Graphene is a library that provides tools to implement graphQL in python
* Uses a _code first approach_
* Works with most frameworks and ORMs
* Instead of writing GraphQL Schema Definition Language (SDL) - we write python code

Install Graphene:

    pip install "graphene>=3.0"

Create a basic schema:

    from graphene import ObjectType, String, Schema

    class Query(ObjectType):
        # this defines a Field `hello` in our Schema with a single Argument `name`
        hello = String(name=String(default_value="stranger"))
        goodbye = String()

        # our Resolver method takes the GraphQL context (root, info) as well as
        # Argument (name) for the Field and returns data for the query Response
        def resolve_hello(root, info, name):
            return f'Hello {name}!'

        def resolve_goodbye(root, info):
            return 'See ya!'

    schema = Schema(query=Query)

> The schema defines each field and type. Along with any arguments. Each field must have a resolver.

In the GraphQL schema definition language it would look like:

    type Query {
      hello(name: String = "stranger"): String
      goodbye: String
    }

Example request:

    {
      hello(name: "friend")
    }

Example response:

    {
      "data": {
        "hello": "Hello friend!"
      }
    }

Querying:

    # we can query for our field (with the default argument)
    query_string = '{ hello }'
    result = schema.execute(query_string)
    print(result.data['hello'])
    # "Hello stranger!"

    # or passing the argument in the query
    query_with_argument = '{ hello(name: "GraphQL") }'
    result = schema.execute(query_with_argument)
    print(result.data['hello'])
    # "Hello GraphQL!"

Integrations:

* [graphene-django](https://docs.graphene-python.org/projects/django/en/latest/)
* [graphene_sqlalchemy + flask](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/)
* [graphene-mongo + flask-graphql](https://graphene-mongo.readthedocs.io/en/latest/)
* [graphQL FastAPI Integrations](https://fastapi.tiangolo.com/advanced/graphql/)


## Sources

* [GraphQL Docs](https://graphql.org/learn/)
