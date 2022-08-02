---
author: ''
category: Postgres
date: '2022-07-22'
summary: ''
title: Postgres Connections and Load
---

## Postgres Connections and Load

Database statistics and performance information are typically stored in the database themselves.

In mysql there is performance schema you can enable - with a bit of a resource consumption cost - that can be used to benchmark and verify performance.

You can also look at the process itself on the host with:

    ps -eo psr,pcpu,pmem,size,thcount,comm

It is important to know how the database system uses processes and threads - and how that relates to connections.

### Active Connections

To check Active connections on postgres:

    SELECT * FROM pg_stat_activity;

> pg_stat_activity is a view in the pg_catalog schema.

* `pg_stat_activity` does not expose information about back-end memory use. You need to use operating-system level facilities for that. However it does tell you the process ID, active user, currently running query, activity status, time the last query started, etc. It's good for identifying long-running idle in transaction sessions, very long running queries, etc.
* More info on the postgres [statistics collector](https://www.postgresql.org/docs/current/monitoring-stats.html)

The columns:

* datid - OID (Object ID) of the database this backend is connected to
* datname - Name of the database this backend is connected to
* pid - Process ID of this backend
* usesysid - OID of the user logged into this backend
* usename - Name of the user logged into this backend
* application_name - Name of the application that is connected to this backend
* client_addr - IP address of the client connected to this backend (If null then it is a unix socket or autovacuum)
* client_hostname - Host name of the connected client (rdns)
* client_port - TCP port number that the client is using for communication with this backend (`-1` for unix socket)
* backend_start - Time when this process was started. For client backends, this is the time the client connected to the server.
* xact_start - Time when this process' current transaction was started, or null if no transaction is active.
* query_start - Time when the currently active query was started or last query
* state_change - Time when the state was last changed
* wait_event_type - The type of event for which the backend is waiting [wait event types](https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-TABLE) - `Client` means the server process is waiting for activity on a socket connected to a user application.
* wait_event - Wait event name if backend is currently waiting [wait events](https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-ACTIVITY-TABLE) - `ClientRead` - Waiting to read data from the client
* state - Current overall state of this backend.
    - `active`: The backend is executing a query.
    - `idle`: The backend is waiting for a new client command.
    - `idle in transaction`: The backend is in a transaction, but is not currently executing a query.
    - `idle in transaction (aborted)`: This state is similar to idle in transaction, except one of the statements in the transaction caused an error.
    - `fastpath function call`: The backend is executing a fast-path function.
    - `disabled`: This state is reported if track_activities is disabled in this backend.
* backend_xid - Top-level transaction identifier of this backend
* backend_xmin - Identifier of this backend's most recent query - if `Active` it is the corrent identifier
* query - Text of this backend's most recent query
* backend_type - Type of current backend

## Top Tip

When connecting to postgres set the [`application_name`](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-APPLICATION-NAME) so it knows who the client is and and you can view the applciations and connections in the `pg_stat_activity` table.

## Sources

* [Postgres Monitoring](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW)
* [How to use pg-stat activity](https://stackoverflow.com/questions/17654033/how-to-use-pg-stat-activity)
