

## Make a Dump

    pg_dump dbname > dumpfile

[Postgres docs: SQL Dump](https://www.postgresql.org/docs/12/backup-dump.html)

## Restore the dump

    psql dbname < dumpfile

## Create password based user and db

    CREATE ROLE myuser LOGIN PASSWORD 'mypass';
    CREATE DATABASE mydatabase WITH OWNER = myuser;