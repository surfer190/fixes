---
author: ''
category: Postgres
date: '2018-09-10'
summary: ''
title: psql
---
# Psql

[Psql](https://www.postgresql.org/docs/current/app-psql.html) is postgreSQL's interactive terminal

## Connecting to a database

    psql testdb

## Meta-Commands

Anything you enter in psql that begins with an unquoted backslash (`\`) is a psql meta-command that is processed by psql itself

* `\d` - Describe. List objects in the database.
* `\d <table>` - describe a given (shows columns)
* `\c <db_name>` - change to a different db
* `\l` - list dbs
* `\q` - quit

## Find the Data Directory

    SHOW data_directory;
    /Library/PostgreSQL/14/data

## Find the Config File

    show config_file;
    /Library/PostgreSQL/14/data/postgresql.conf

## Manually installed postgres mac restart

    sudo -u postgres pg_ctl -D /Library/PostgreSQL/14/data stop
    sudo -u postgres pg_ctl -D /Library/PostgreSQL/14/data start

## Psqlrc

Postgres's startup file / startup config:

    ~/.psqlrc

Sensible options:

    -- Automatically format output based on result length and screen
    \x auto 


    -- Prettier nulls
    \pset null '#'

    -- Save history based on database name
    \set HISTFILE ~/.psql_history- :DBNAME

    -- Turn on automatic query timing
    \timing

## Sources

* [Exploring a New Postgres Database](https://www.craigkerstiens.com/2020/11/14/exploring-a-new-postgres-database/)
* [Postgres PSQL docs](https://www.postgresql.org/docs/current/app-psql.html)
