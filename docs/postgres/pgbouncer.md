---
author: ''
category: Postgres
date: '2022-12-05'
summary: ''
title: Postgres - PGBouncer
---

# PGBouncer

> lightweight connection pooler for PostgreSQL 

The aim of pgbouncer is to lower the performance impact of opening new connections to PostgreSQL.

Saving time when opening and closing connections.

Is this your bottleneck though?

What is a high number of connections in postgres?

* That all depends on your application, but generally when you get to the** few hundred connection** area in Postgres you’re in the higher end
* Generally a safe level for connections should be somewhere around **300-500 connections**
* By default postgres sets max connections at 100 (check this with `show max_connections;`)

> pgBouncer can not do anything about network usage when it comes to running queries – it's not a cache of data/query-results. So it will actually slow down queries a bit – because instead of sending the query to server, you will pass it to pgBouncer which, in turn, will send it to server.

## Connection basics in Postgres

* Each new connection to Postgres is a forked process
* This process comes with its own memory allocation of roughly 10 MB with at least some load for the query
* For 300 database connections this is 3 GB of memory going just to managing those connections—memory which could be better used for caching your data

Some frameworks grab a bunch of connections at startup - reducing the time needed to run a query as it does not need to first get a connection.

How do you check your idle connections (or all connections):

    SELECT COUNT(*)
    FROM pg_stat_activity
    WHERE state <> 'idle'

## Enter Connection Pooler

A connection pooler will do the hard work of maintaining a pool of connections and then give them out as your application needs them, which is when a transaction or query happens.
Django or rails doesn't need to handle that.

2 key settings of a connection pooler:

* A max amount of active connections
* A max on idle connections

> For Citus Cloud the limit is 300 active connections and 2000 idle connections.

## Setting Up PGBouncer

Two modes:

* session pooling - Most polite method - session for as long as a client stays connected (default method). When a client disconnects - the connection is put back in the pool.
* transaction pooling - A server connection is assigned to a client only during a transaction.
* statement pooling - Most aggressive method - The server connection will be put back into the pool immediately after a query completes.

> Transaction pooling will grant a connection when you run `BEGIN;` and return the transaction when you `COMMIT;`

> To connect to PgBouncer on citus-cloud, you can simply swap your port from 5432 to 6432 and you’ll be connected to PgBouncer

## Installing PG Bouncer on Ubuntu

[pgbouncer install](https://www.pgbouncer.org/install.html)

Using distro package maintainer:

    sudo apt install libevent-dev pgbouncer
    # Check status
    sudo systemctl status pgbouncer
    # Edit config
    sudo vim /etc/pgbouncer/pgbouncer.ini

> This will install the systemd service

From source:

    cd /opt
    sudo wget https://www.pgbouncer.org/downloads/files/1.18.0/pgbouncer-1.18.0.tar.gz
    sudo tar xzf pgbouncer-1.18.0.tar.gz
    cd pgbouncer-1.18.0
    sudo apt install libevent-dev
    sudo ./configure --prefix=/usr/local
    sudo make
    sudo make install

Edit the config then restart

    In config:
    
        * = host=localhost port=5432

    sudo systemctl restart pgbouncer

The log is found at `/var/log/postgresql/pgbouncer.log`

Get stats with:

    sudo tail -f /var/log/postgresql/pgbouncer.log | grep "stats"

## Setting up PG Bouncer for AWS RDS

Check out [Ankane.org: PGBouncer Setup](https://ankane.org/pgbouncer-setup)

## Inspecting PgBouncer

To connect to the pgbouncer instance:

    psql -p 6432 pgbouncer
    
    SHOW pools;
    
## Connection Routing

Pg bouncer can store a logical database name.
So when you connect on your app you only need to state the port and app name.

## Sources

* [What is the point of bouncing?](https://www.depesz.com/2012/12/02/what-is-the-point-of-bouncing/)
* [Github: pgbouncer](https://github.com/pgbouncer/pgbouncer)
* [Citusdata: Scaling Connections in Postgres](https://www.citusdata.com/blog/2017/05/10/scaling-connections-in-postgres)
* [Pgbouncer: FAQ](https://www.pgbouncer.org/faq.html)
* [Pgbouncer: Usage](https://www.pgbouncer.org/usage.html)
* [Youtube: Connection pooling routing and queueing with pgBouncer](https://www.youtube.com/watch?v=x_XpPbfomso)
* [Youtube: PgBouncer Connection Pooling and Routing](https://www.youtube.com/watch?v=a0SDogoPzss)
* [Scaleway: Installing PGbouncer](https://www.scaleway.com/en/docs/tutorials/install-pgbouncer/)
