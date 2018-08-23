# PostGres - Up and Running

A few notes I took from the excellent book" __PostgreSQL: Up and Running, Third Edition by Regina Obe and Leo Hsu”__

## Basics

### Why PostgreSQL

PostgreSQL is a relational detabase management system. It is not just a database it is also an application platform.

It is fast.

Prepackaged languages for stored procedures and functions: `C`, `SQL` and `PL/pgSQL`. Additional support for Python, R and Javascript (PL/V8) - boo!

It has a larger set of datatypes than most and allows definition on custom data types.

It bridges between the relational world and the object world. If you create a dog table with creed, colour, size; `postgres` will maintain a dog datatype for you.

> With a robust database, everything else is eye candy

PostgreSQL is fundementallly relational, there are non-relational facilities:

* `ltree` supports graphs
* `hstore` for key value pairs
* `json` and `jsonb` for documents (we've already learnt that jsonb is preferential in most cases)

It has been around for 20 years (from changing to PostgreSQL from Postgres95), the code base started in 1986.

### Why Not PostGresSQL

It is large (more than 100mb) so rule out use on small devices and for small cache stores.

Security managed at applcation level doesn't need postgres' role and permissions, a single user database such as `sqlite` or `firebird` may be better suited.

It can be combined with other db types like `redis` or `memchache` to cache query results. Or woith sqlite for the offline db.

### Installation

Install from [Postgres core Distribution](https://www.postgresql.org/download/)

#### Ubuntu

On Ubuntu you can intall with:

    sudo apt install postgresql postgresql-contrib

Log into psql:

    sudo -u postgres psql

Get out:

    \q

From command prompt create a user:

    sudo -u postgres createuser --interactive

Create a database:

    createdb crowdminder

**This will only install postgres 9.5**

### Installing Latest on Ubuntu

Follow the steps in [Installing postgres on ubuntu core](https://www.postgresql.org/download/linux/ubuntu/)

The installer will tell you to login as `postgres` and run:

    /usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -l logfile start

but it didn't work for me so I just started it with:

    sudo service postgres start

Wierdly it started the previous install I had of postgres:

    postgres=# select version();
                                                        version                                                      
    ------------------------------------------------------------------------------------------------------------------
    PostgreSQL 9.5.13 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609, 64-bit
    (1 row)

I had to purge the old one with:

    sudo apt purge postgresql-9.5

then install with:

    sudo apt install postgresql-10 postgresql-client-10

Use `select version();` inside `psql` to check the version.

### Administration tools

* psql - postgreSQL's command line interface that comes with the core distribution
* pgAdmin - a popular, free GUI tool for Postgres. It is the `postgres` version of MySQLWorkbench. Although I have found MySQL workbench superior to use. That being said administration and monitoring can be done on pgAdmin as it is open source. pgAdmin does not have a desktop app is is used through a browser.
* phpPgAdmin - Postgres version of PHPMyAdmin. Don;t use this thing it is shit.
* Adminer - Useful if you are manging postgres and other databases together. A lightweight PHP application. It has a nice relational diagrammer (which makes up for PgAdmin's lack of one). It is a lowest common denominator package.

### Postgres Databse Objects

Postgres has more database objects than most other systems. You will probably never touch most of these objects.

* Database - Each postgres service houses many databases
* Schema - Next level organisation within each database. When you create a new database, postgres automatically creates a schema called `public` which is fine if you have a few tables. YThousands of tables should be split into schemas.
* Table - Tables are first citizens of schemas. They are __inheritable__ which saves time in db creation and querying. Postgres creates an accompanying custom data type for each table.
* View - Views are offered by most db's and offer a level of abstraction from tables. You can do caluclations, derive columns, hide columns. Generally they are read-only but can be updated in postgres even with derived columns with a trigger.


#### Extension 

Allow developers to package, functions, data types, casts, custom index types, tables, attribute variables. 

Only enable extensions you need. Also create a seperate schema for them to reside in like `extensions`.

`search_path` variable of the database so you can refer to the function without having to prepend the schema name

Some extensions rely on other extensions, with `9.6` dependent extensions will be installed when required when using `CASCADE`:

    CREATE EXTENSION postgis_tiger_geocoder CASCADE;

#### Functions

Functions can be created for data manipulation, complex calculations. Other databases refer to functions that manipulate data as stored procdeures. Postgres does not make that distinction.

#### Languages

You can create functions using a `PL` a procedural language. 

There are 3 by default: `SQL, PL/pgSQL, and C`

You can add more from framework or with `CREATE PRODCEDURAL LANGUAGE`

#### Operators

Symbolically names aliases: `=` or `&&`. You can create your own.

#### Foreign Tables and Foreign Data Wrappers

Foreign tbles are virtual tables linked to data outside of postgres. They could be a CSV file or another external db, a webservice or redis that can be queries like another table.

Foreign Data Wrappers (FDW's) handle the mapping and handschake between the services. 

#### Triggers and Trigger Functions

Triggers detect and run on data change events. Trigger functions have access to info before and after a trigger event for complex validation and reversal. In `9.4` you can create triggers for foreign tables.

#### Catalogs

Catalogs are system schemas that store Postgres built-in functions and metadata. Every database contains:

* `pg_catalog` - holds tables, functions, system views from PostGres
* `information_schema` - Metadata for exposing ANSI SQL standard

Settings to configure the db are stored within the db. Although best not to mess with variables in `pg_catalog`

You will find `information_schema` in MySQL as well and it lists: `columns`, `tables` and `views` giving info about the structure of tables.

#### Types

Short for `data type` 

#### Full Text Search

FTS, Full text search, is a natural language based search. It can search based on semantics (the meaning behind the words) not just on syntactical (structural) make up.

Eg. Searching for `runnning` may return: **run, runner, running, sprint, dash**

#### Casts

Prescribe how to convert one data type to another. 

#### Sequences

Gives control of an autoincrement serial class

#### Rules

Instructions to rewrite SQL before execution which have fallen out of favour to triggers.

### Database Drivers

* PHP - `pdo_pgsql`
* Java - `JDBC`
* .net - `Npgsql`
* Microsoft Office - `Postgres ODBC drivers`
* Python - `psycopg2` 
* Ruby - `pg`

## Database Administration

Basic Administration: managing roles and permissions, creating databases, installing extensions, backing up and restoring data.

### Configuration Files

* `postgresql.conf` - General settings: memory allocation, defautl sotrage locations, ip addresses, posts, location of logs.
* `pg_hba.conf` - Controls access to server, indicating which users and ip's can login and connect.
* `pg_ident.conf` - Maps authenticated OS login to a postgres user. Some may a server's `root` user to `posrtgres` user.

> Postgres refers to `users` as `roles`. Not all `roles` need to have login privileges (group roles)

Finding tho location of configuration files:

    SELECT name, setting FROM pg_settings WHERE category = 'File Locations';

#### Changing Settings

Some config changes require restarting the service and closing existing connections. Other changes just require a reload. 
Look under the context setting associated with a configuration:

* `postmaster` = `restart` required
* `user` = `reload` required

#### Reloading

1. Console `pg_ctl`, in a console:

    pg_ctl reload -D your_data_directory_here

2. Installed as a service:

    service postgresql-9.5 reload

3. Via a query:

    SELECT pg_reload_conf();

#### Restarting

1. Console `pg_ctl`, in a console:

    pg_ctl restart -D your_data_directory_here

2. Installed as a service:

    service postgresql-9.5 restart

#### Postgresql.conf

Never edit it directly, rather make use of `postgresql.auto.conf` which overrides settings in the `postgres.conf`.

You can check settigs with:

    SELECT
        name,
        context ,
        unit ,
        setting, boot_val, reset_val 
    FROM pg_settings
    WHERE name IN ('listen_addresses','deadlock_timeout','shared_buffers',
        'effective_cache_size','work_mem','maintenance_work_mem')
    ORDER BY context, name;

Remember `context` shows the scope. `user context` means a user can change settings in their session. `superuser` sets it as default for all users. `user` cannot override a `superuser` set setting. `postmaster` settings affect the entire server.

Settings can be set per role, database, session and funciton level.

> Make sure to check the `unit` of the setting.

Remember you can check the data type label display with `SHOW`:

    SHOW shared_buffers;

#### File Settings

You can check settings from files:

    SELECT name, sourcefile, sourceline, setting, applied
    FROM pg_file_settings
    WHERE name IN ('listen_addresses','deadlock_timeout','shared_buffers',
        'effective_cache_size','work_mem','maintenance_work_mem')
    ORDER BY name;

Important settings that require a restart and may prevent clients from connecting:

* `listen_addresses` - Tells PostgreSQL what IP address to listen on. This defualt to localhost. Most people change to `*` for all ip's.
* `port` - Defaults to `5432`
* `max_connections` - The max number of concurrent connections
* `log_destination` - misnomer, it specifies the log format, reather than location.

Settings that affect performance:

* `shared_buffers` - Amount of memory shared between all connections. This affects the speed of your queries. Generally this should be set to **25%** of available RAM. After 8Gb there are diminishing returns.
* `effective_cache_size` - An estimate postgres expects the OS to devote to it. Set this to **half of avialable RAM** for a dediated server.
* `work_mem` - Controls max memory for each operation: sorting, hash join and table scans. 
* `maintenance_work_mem` - Memory allocated for house keeping activities (Nevr set more than 1Gb)
* `max_parallel_workers_per_gather` - Parallelism which is off by default. If you have more than 1 core you will want to increase this. should be lower than `max_worker_processes` - which defaults to 8. 

Changin settings

It is better to use a query `ALTER SYSTEM` instead of editing the files directly:

    ALTER SYSTEM SET work_mem = '500MB';

then reload:

    SELECT pg_reload_conf();

#### Server not starting after editing file

If this happens check the log at the root of the data folder or in `pg_log`.

Most common is a `shared_buffers` set too high or an ols `postmaster.pid` left from a failed shutdown which will need to be deleted.

### pg_hba.conf

Determines who can connect. Changes to this file require a reload. 

The authentication method: `ident`, `trust`, `md5`, `peer` and `password`. 

> Remember users and devices still need to satisfy role and database access restrictions.

* `trust` - least secure authentication. No password is needed as long as user is from the ip range.
* `md5` - required an MD5 encrypted password to connect
* `password` - uses clear text password authentication
* `ident` - uses `pg_ident.conf` to check if local user is mapped to a postgres account.
* `peer` - uses OS name of the user from the kernel.
* `cert` - stipulate that connections use SSL. 

### Managing Connections

The responsibility is on the client to stop queries from taking ver long to complete. Although queries can be cancelled or connections terminated.

All running queries should be stopped and connectins terminated before making backups and restoring backups.

#### Cancelling running queries and terminating connections

1. Retrieve a list of active connections:

    SELECT * FROM pg_stat_activity;

2. Cancel active queries on a connection with PID 1234

    SELECT pg_cancel_backend(1234);

3. Terminate the connection

    SELECT pg_terminate_backend(1234);

This is especially important prior to a database restore. If you don’t terminate the connection, the client may immediately reconnect after restore and run the offending query anew.

`pg_terminate_backend` and `pg_cancel_backend` only work on one pid at a time, you can cancel all with the use of SQL:

    SELECT pg_terminate_backend(pid) FROM pg_stat_activity 
    WHERE usename = 'some_role';

You can set some defaults so the server automatically cancels or kills:

* `deadlock_timeout` - how long a deadlocked query should wait before giving up
* `statement_timeout` - time a query can run before it is forced to cancel. This default to 0 (ie. never timeout)
* `lock_timeout` - time to wait on a lock before giving up. Default is 0.
* `idle_in_transaction_session_timeout` - Amount of time a transaction can stay in idle before timing out.

[More info on wait event types in postgres Docs](https://www.postgresql.org/docs/9.6/static/monitoring-stats.html#WAIT-EVENT-TABLE)

### Roles

Roles can belong to other roles (group roles). 

#### Creating

Postgres creates a login role called `postgres`. After installing postgres you should login as _postgres_ and create another role. Either with PgAdmin or:

    CREATE ROLE leo LOGIN PASSWORD 'king' VALID UNTIL 'infinity' CREATEDB;

`VALID UNTIL` is optional, defualts to infinity. `CREATEDB` grants database creation privileges to the new role.

Creating a superuser:

    CREATE ROLE regina LOGIN PASSWORD 'queen' VALID UNTIL '2020-1-1 00:00' SUPERUSER;

Creating a group role:

    CREATE ROLE royalty INHERIT;

`INHERIT` means any member of royalty will inherit privileges of royalty role.

Adding members to a group role:

    GRANT royalty TO leo;

View Postgres golbal variables:: `session_user` and `current_user`

    SELECT session_user, current_user;

> `SET ROLE` changes the `current_user`, while `SET SESSION AUTHORIZATION` changes both the `current_user` and `session_user variables`.


### Database Creations

    CREATE DATABASE mydb;

a Template Databse is a skeleton for new databases. If you don't specify a template `template1` is used. 

Creating a database from a template:

    CREATE DATABASE my_db TEMPLATE my_template_db;

> You can also mark any database as a template database. Once you do, the database is no longer editable and deletable.

    UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'mydb';

> If ever you need to edit or drop a template database, first set the datistemplate attribute to FALSE

### Using Schemas

Schemas organise your data into logical groups. If you have more than 24 tables in your database consider moving them out into schemas.

> Another common way to organize schemas is by roles. We found this to be particularly handy with applications that serve multiple clients whose data must be kept separate.

Prepend the schema name onto the table in a query to tell postgres what schema to use:

    SELECT * FROM customer1.dogs

Another method is to set the search_path variable to be something like `customer1`, `public`.

It will search the non-public schema first.

Finding the currently logged in user:

    SELECT user;

an alias for `current_user`

So if customer schemas are named the same as their login roles you can do:

    search_path = "$user", public;

Importantly all SQL queries remain the same.

**Create new schemas per extension**

    CREATE SCHEMA my_extensions;

then add the new extension to the `search path`:

    ALTER DATABASE mydb SET search_path='$user', public, my_extensions;

* Requires a reconnect

### Privileges

Privileges or permissions are tricky to administer. It can even go to row and column level.
You can achieve most privilege audmin in `pgAdmin`.

Most privileges have a context (a target acted upon), the only 2 with no context are `CREATEDB` and `CREATE ROLE`

#### Getting Started

After installing postgres

Create a role that will ownt he db:

    CREATE ROLE mydb_admin LOGIN PASSWORD 'something';

Create the database and set the owner:

    CREATE DATABASE mydb WITH owner = mydb_admin;

### Grant

Primary way to assign privileges:

    GRANT some_privilege TO some_role;

> Some privileges always remain with the owner of an object and can never be granted away. These include DROP and ALTER.

> The owner of an object retains all privileges. Granting an owner privilege in what it already owns is unnecessary

Giving another role ability to give others the permission, use `OPTION`:

    GRANT ALL ON ALL TABLES IN SCHEMA public TO mydb_admin WITH GRANT OPTION;

To grant a privilege on all roles, use `PUBLIC`:

    GRANT USAGE ON SCHEMA my_schema TO PUBLIC;

> Unlike in other database products, being the owner of a PostgreSQL database does not give you access to all objects in the database. Another role could conceivably create a table in your database and deny you access to it! However, the privilege to drop the entire database could never be wrestled away from you.

> After granting privileges to tables and functions with a schema, don’t forget to grant usage on the schema itself.

## Backup and Restore

3 utilities:

* `pg_dump` - backup specific database
* `pg_dumpall` - backup all databases (as superuser)
* `pg_basebackup` - system level disk backups

If your db is >= 500Gb then you should use `pg_basebackup` as part of your backup strategy - but that requires settings turned on for replication.

> pg_dump can selectively back up tables, schemas, and databases

### Create a compressed, single database backup

    pg_dump -h localhost -p 5432 -U someuser -F c -b -v -f mydb.backup mydb

A plain text backup can be created with:

    pg_dump -h localhost -p 5432 -U someuser -C -F p -b -v -f mydb.backup mydb

(Jeepuz, lots of options) `-C` means `CREATE DATABASE`

Create a dump of tables whose name starts with `pay*`:

    pg_dump -h localhost -p 5432 -U someuser -F c -b -v -t *.pay* -f pay.backup mydb

A backup of all objects in the `hr` and `payroll` schemas:

    pg_dump -h localhost -p 5432 -U someuser -F c -b -v \
    -n hr -n payroll -f hr.backup mydb

Create a compressed backup of all objects in all schemas including public:

    pg_dump -h localhost -p 5432 -U someuser -F c -b -v -N public \
    -f all_sch_except_pub.backup mydb

#### Directory

To crate the backup as a directory and getting around file size limitations:

    pg_dump -h localhost -p 5432 -U someuser -F d -f /somepath/a_directory mydb

#### System wide backup

A server wide backup using `pg_dumpall` puts everything into a plain text file, including server globals.
It is recommended to prefer inidividual backups though as restoring from a huge text file can be slow.
`pg_basebackup` is the fastest option when restoring from a major issue.

To backup all globals and tablespace definitions:

    pg_dumpall -h localhost -U postgres --port=5432 -f myglobals.sql --globals-only

Backing up specific global settings:

    pg_dumpall -h localhost -U postgres --port=5432 -f myroles.sql --roles-only

### Restoring Data

From `pg_dump` and `pg_dumpall` use:

1. `psql` for plain-text
2. `pg_restore` for compressed, tar and directory backups

#### Psql

Restore a backup and ignore errors:

    psql -U postgres -f myglobals.sql

Restore, stopping when error found:

    psql -U postgres --set ON_ERROR_STOP=on -f myglobals.sql

Restore a specific database:

    psql -U postgres -d mydb -f select_objects.sql

#### Pg_restore

* You can perform parrallel restores with `-j` or `--jobs=3`. Restoring a table per thread. 
* You can review what is being restored before starting
* You can sleectively restore: table or schema

To restore:

1. First create the databsae anew:

    CREATE DATABASE mydb;

2. Restore:

    pg_restore --dbname=mydb --jobs=4 --verbose mydb.backup

If the name of the db is the same as the backup, you can do the above in one step:

    pg_restore --dbname=postgres --create --jobs=4 --verbose mydb.backup

With the `--create` option, the database name is always the same as the one you backed up.

A restore will not recreate objects, so you need to use the `--clean` switch.

To restore just the structure with no data:

    pg_restore --dbname=mydb2 --section=pre-data --jobs=4 mydb.backup

### Tablespaces

Postgres uses table spaces to map logical names ot physical locations on disk.
Defaults: `pg_default` (user data) and `pg_global` (system data)

Creating a tablespace:

For unix, firt create the folder and `fstab` location, then:

    CREATE TABLESPACE secondary LOCATION '/usr/data/pgdata94_secondary';

Moving objects to another tablesapce:

    ALTER DATABASE mydb SET TABLESPACE secondary;

To move a single table:

    ALTER TABLE mytable SET TABLESPACE secondary;

To move all objects from defualt to secondary (db will be locaked):

    ALTER TABLESPACE pg_default MOVE ALL TO secondary;

### Important SysAdmin Points

* Always check the logs when something goes wrong
* You can clear your `pg_log` folder (not any others, `pg_xlog` and `pg_clog` are very important - renamed in postgres 10 to stop people thinking they were log files)



