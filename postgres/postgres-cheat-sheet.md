# Postgres Cheatsheet 

A quick reference for  quick and dirty postgres commands

### Change databases

When you connect to postgres it is always on a specific db

to change databases, close the old connection and reconnect on the new database:

    \c name_database

[Copy data from table in one schema to another](https://stackoverflow.com/questions/39890502/how-to-copy-certain-tables-from-one-schema-to-another-within-same-db-in-postgres)

    insert into schema2.the_table
    select * 
    from schema1.the_table;

### View schemas in a db

    select nspname from pg_catalog.pg_namespace;

[Alter or change  the public schema name](https://stackoverflow.com/questions/24080832/postgres-best-way-to-move-data-from-public-schema-of-one-db-to-new-schema-of-an)

    alter schema public rename to original_public;
    create schema public;

[Add superuser privilege to a user](https://stackoverflow.com/questions/10757431/postgres-upgrade-a-user-to-be-a-superuser)

In psql:

    ALTER USER my_user WITH SUPERUSER;

[List all databases](https://dba.stackexchange.com/questions/1285/how-do-i-list-all-databases-and-tables-using-psql)

In psql:

    \l

[View the users of a postgres instance](https://unix.stackexchange.com/questions/201666/command-to-list-postgresql-user-accounts)

In psql:

    \du 

[View the scemas in a postgres database](https://dba.stackexchange.com/questions/40045/how-do-i-list-all-schemas-in-postgresql/40051)

In psql:

    \dn

[Reset a postgres user password](https://stackoverflow.com/questions/12720967/how-to-change-postgresql-user-password)

In psql:

    ALTER USER user_name WITH PASSWORD 'new_password';

[Postgres connection strings](https://stackoverflow.com/questions/3582552/postgresql-connection-url)

## Dump (Backup) and Restore

Dump a remote database

    pg_dump -U <username> -h <ip> -p 5432 <database_name> > <backup_name>.bak

Create a database and user for access to it:

    sudo -u postgres psql
    create database <db_name>;
    create user <username> with encrypted password '<password>';
    grant all privileges on database <db_name> to <username>;

Restore the database:

    sudo -u postgres psql <db_name> < <backup_name>.bak

## PSQL Cheatsheet

Select a database

    \c <db_name>

list tables

    \dt



