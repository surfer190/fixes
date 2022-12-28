---
author: ''
category: postgres
date: '2022-12-21'
summary: ''
title: Create a Postgres User and Grant Access to a Database
---

### Create a Postgres User and Grant Access to a Database

Login:

    sudo su postgres
    psql

Create a database:

    CREATE DATABASE <db_name>;

Create a user:

    # create user <username> with encrypted password '<password>';
    CREATE USER <username> WITH PASSWORD '<password>';

Grant the user access on a database (includes create on schema - not table):

    grant all privileges on database <db_name> to <username>;
    
Grant the user access on the public schema:

> May get: permission denied for schema public

    psql
    \c <db_name>
    GRANT USAGE, CREATE ON SCHEMA public TO <username>;

> You may get an error `FATAL:  Peer authentication failed for user "pali_canon"` when attempting to login with `psql -U <username> -W`

This is due to [Postgres host based authentication (hba)](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).

Get the [file locations](https://www.postgresql.org/docs/current/runtime-config-file-locations.html) with:

    SHOW config_file;
    SHOW hba_file;

You can view the rules for auth.

Typically this would result from authenticaiton where the host is not specified.
If you set the `host` it would work:

    psql -U <username> -W -h 127.0.0.1

### Delete the user

    REVOKE ALL PRIVILEGES ON database <db_name> from <username>;
    DROP user <username>;

## Sources:

* [gist: read-access.sql ](https://gist.github.com/oinopion/4a207726edba8b99fd0be31cb28124d0)
* [ubiq.co: How to create a user in postgres](https://ubiq.co/database-blog/create-user-postgresql/)
* [postgres: config file locations](https://www.postgresql.org/docs/current/runtime-config-file-locations.html)
* [Postgres: Why is a new user allowed to create a table?](https://dba.stackexchange.com/questions/35316/why-is-a-new-user-allowed-to-create-a-table)
