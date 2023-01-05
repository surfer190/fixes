---
author: ''
category: postgres
date: '2022-11-07'
summary: ''
title: Upgrading Postgresql on Ubuntu
---

## Upgrading Postgresql on Ubuntu

When you install a new major version of postgres, it does not automatically switch over.
The new version will be isntalled but the old version will still be running.

You can confirm this by running in psql:

    SELECT VERSION();

For details from the maintainers see:

    /usr/share/doc/postgresql-common/README.Debian.gz

### The Gist of the Docs

> Since the on-disk data format of all major PostgreSQL versions are incompatible to each other, Debian's PostgreSQL packaging architecture is designed to maintain clusters of different major versions in parallel.

> This `postgresql-common` package provides the common infrastructure and all
frontend programs that users and administrators use. The version specific
server and client programs are shipped in `postgresql-*-<version>` packages.

### Check the Versions Installed

    dpkg -l | grep postgresql

    rc  pgdg-keyring                           2018.2                             all          keyring for apt.postgresql.org
    ii  postgresql                             12+214ubuntu0.1                    all          object-relational SQL database (supported version)
    ii  postgresql-10                          10.21-0ubuntu0.18.04.1             amd64        object-relational SQL database, version 10 server
    ii  postgresql-11                          11.12-1.pgdg16.04+1                amd64        The World's Most Advanced Open Source Relational Database
    ii  postgresql-12                          12.12-0ubuntu0.20.04.1             amd64        object-relational SQL database, version 12 server
    rc  postgresql-13                          13.3-1.pgdg16.04+1                 amd64        The World's Most Advanced Open Source Relational Database
    ii  postgresql-14                          14.6-1.pgdg20.04+1                 amd64        The World's Most Advanced Open Source Relational Database
    ii  postgresql-client-10                   10.21-0ubuntu0.18.04.1             amd64        front-end programs for PostgreSQL 10
    ii  postgresql-client-11                   11.12-1.pgdg16.04+1                amd64        front-end programs for PostgreSQL 11
    ii  postgresql-client-12                   12.12-0ubuntu0.20.04.1             amd64        front-end programs for PostgreSQL 12
    ii  postgresql-client-14                   14.6-1.pgdg20.04+1                 amd64        front-end programs for PostgreSQL 14
    ii  postgresql-client-common               246.pgdg20.04+1                    all          manager for multiple PostgreSQL client versions
    ii  postgresql-common                      246.pgdg20.04+1                    all          PostgreSQL database-cluster manager
    ii  postgresql-contrib                     12+214ubuntu0.1                    all          additional facilities for PostgreSQL (supported version)

You can also go the the `postgres` user's root directory `/var/lib/postgresql` and see the version folders:

    ls
    10  11	12  13	14

You can run `pg_lsclusters` to show information about all clusters:

    pg_lsclusters
    
    Ver Cluster Port Status                Owner    Data directory              Log file
    10  main    5432 online                postgres /var/lib/postgresql/10/main /var/log/postgresql/postgresql-10-main.log
    11  main    5433 online                postgres /var/lib/postgresql/11/main /var/log/postgresql/postgresql-11-main.log
    12  main    5434 online                postgres /var/lib/postgresql/12/main /var/log/postgresql/postgresql-12-main.log
    13  main    5435 down,binaries_missing postgres /var/lib/postgresql/13/main /var/log/postgresql/postgresql-13-main.log
    14  main    5436 online                postgres /var/lib/postgresql/14/main /var/log/postgresql/postgresql-14-main.log

### Common Programs

### Common programs

* `/usr/share/postgresql-common/pg_wrapper`: environment chooser and program selector
* `/usr/bin/program`: symbolic links to pg_wrapper, for all client programs
* `/usr/bin/pg_lsclusters`: list all available clusters with their status and configuration
* `/usr/bin/pg_createcluster: wrapper for `initdb`, sets up the necessary configuration structure
* `/usr/bin/pg_ctlcluster`: wrapper for `pg_ctl`, control the cluster postgres server
* `/usr/bin/pg_upgradecluster`: upgrade a cluster to a newer major version
* `/usr/bin/pg_dropcluster`: remove a cluster and its configuration

### Install Procedure and creating a user

1. When installing `postgresql-*` on ubuntu - this will automatically create a default cluster 'main' with the database superuser 'postgres'

2. Become the superuser

        sudo -u postgres bash

3. Create a user with the same name as your unix user

        createuser -DRS staging
        
4. Create a database owned by the new user:

        createdb -O staging staging_db

5. One can connect to the db with:

        psql staging_db

### Upgrade Procedure

> Upgrading from Postgres 10 to Postgres 14 on Ubuntu 20.04

In this example currently running is:

    SELECT version();
    PostgreSQL 10.21

Due to this default cluster, an immediate attempt to upgrade an
earlier 'main' cluster to a new version will fail and you need to
remove the newer default cluster first. E. g., if you have
postgresql-9.6 installed and want to upgrade to 11, you first install
postgresql-11:

    apt-get install postgresql-11

Then drop the default 11 cluster that was just created:

    pg_dropcluster 11 main --stop

    # Ubuntu recommends to do: sudo systemctl stop postgresql@11-main then run the above

> also stopped the others:

* `sudo systemctl stop postgresql@12-main`
* `sudo systemctl stop postgresql@13-main`
* `sudo systemctl stop postgresql@14-main`

> There was an issue with pg13 (binaries missing) - so reinstalled: `apt-get install postgresql-11`. This turned them all on again.

Only the running cluster will be shown:

    pg_lsclusters
    Ver Cluster Port Status Owner    Data directory              Log file
    10  main    5432 online postgres /var/lib/postgresql/10/main /var/log/postgresql/postgresql-10-main.log

And then upgrade the 10 cluster to the latest installed version (e. g. 11):

    pg_upgradecluster 10 main

When one run the above it gave:

    Error: The locale requested by the environment is invalid:
    LANG: en_US.UTF-8
    LANGUAGE: en_US:
    LC_CTYPE: UTF-8
    Error: Could not create target cluster

This is fixed with running:

    sudo update-locale LC_CTYPE=en_US.UTF-8

Then logging out and logging back in.

Then run again:

    pg_upgradecluster 10 main

After Upgrade it says:

    Success. Please check that the upgraded cluster works. If it does,
    you can remove the old cluster with
        pg_dropcluster 10 main


Version 14 was running:

    Ver Cluster Port Status Owner    Data directory              Log file
    14  main    5432 online postgres /var/lib/postgresql/14/main /var/log/postgresql/postgresql-14-main.log

> Check that everything is working then run...

    postgres=# select version();
    PostgreSQL 14.6 (Ubuntu 14.6-1.pgdg20.04+1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0, 64-bit
    (1 row)

    pg_dropcluster 10 main

The application was broken with:

    peewee.OperationalError: SSL connection has been closed unexpectedly

> after restarting the application it was fine

 and there was an error on pg_admin 4:

    invalid literal for int() with base 10: 'None'

> after restarting pg_admin it was fine

    sudo apt-get purge postgresql-10 postgresql-client-10
    sudo apt-get purge postgresql-11 postgresql-client-11
    sudo apt-get purge postgresql-12 postgresql-client-12
    sudo apt-get purge postgresql-13 postgresql-client-13

## Sources

* [Paulox.net: Upgrading Postgresql](https://www.paulox.net/2019/05/28/upgrading-postgresql-from-version-10-to-11-on-ubuntu-19-04-disco-dingo/)
* [Stackoverflow: Fix locale error on pg_upgrade](https://stackoverflow.com/questions/40692507/how-to-fix-error-the-locale-requested-by-the-environment-is-invalid-during-po)
* [Stackoverflow: Perl fails to set locale even though it is installed](https://stackoverflow.com/questions/49089099/perl-fails-to-set-locale-even-though-it-is-installed)
