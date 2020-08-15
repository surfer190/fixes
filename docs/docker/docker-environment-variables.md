---
author: ''
category: Docker
date: '2019-10-14'
summary: ''
title: Docker Environment Variables
---
# Docker Environment Variables

## Docker Image Built-time Variables

To set build time variables - use the `Dockerfile`, these settings are baked into the **image**.


### Args

Args are to help you not repeat yourself in a Dockerfile

    ARG some_variable_name

That tells docker that it should expect `some_variable_name` to be passed in at build time.
You do that with:

    docker build --build-arg some_variable_name=a_value

ARG's are not available to running containers

### Envs

`ENV` can be used to define default environment variables

    ENV foo /bar

This environment variable is available to containers

You can set a dynamic build time variable, that will be available to the container with:

    ARG some_variable_name
    ENV env_var_name=$some_variable_name

You can override `ENV` variables when starting containers with:

    docker run -e "env_var_name=another_value" alpine env

## Docker Compose

> Environment stuff only applies to containers, not images

You can also specify a file to read values from


### Sources

* [Docker Environment Variables](https://vsupalov.com/docker-env-vars/)