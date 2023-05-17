---
author: ''
category: SQLite
date: '2022-09-01'
summary: ''
title: SQLite and Python
---

## SQLite and Python

Python users do not need to install anything to get started working with SQLite, as the standard library in most distributions ships with the [sqlite3](https://docs.python.org/3/library/sqlite3.html) module.

### Database Authorization and Access Control with Python

SQLite's python driver has a hook for setting what data can be accessed or returned by a connection: [`set_authorizer`](https://docs.python.org/3.6/library/sqlite3.html#sqlite3.Connection.set_authorizer)

This hook will set what can be accessed by a a connection.

* SQLite databases are embedded in the same process as your application, so there is no master server process to act as a gatekeeper for the data stored in your database.
* Additionally, SQLite database files are readable by anyone with access to the database file itself
* Restricting access to a SQLite database, once a connection has been opened, is only possible through the use of an _authorizer callback_.

#### Authorizer Callback

A function written and registered with the SQLite connection object - which is subsequently called for each operation on the db.
The autorizer only last for the duration of the connection.

It accepts 5 parameters and return 1 of 3 values.

Parameters:

* action (a constant defined in sqlite3.h)
* argument 1 — value depends on action
* argument 2 — value depends on action
* database name
* trigger name (if action is result of a trigger)

The return value is one of:

* `SQLITE_OK (0)` — allow operation
* `SQLITE_DENY (1)` — do not allow and raise a DatabaseError.
* `SQLITE_IGNORE (2)` — treat the column as NULL (for granular column access).

Example actions and parameters:

* `SQLITE_CREATE_INDEX`: Index name, Table name
* `SQLITE_CREATE_TABLE`: Table name, NULL
* `SQLITE_CREATE_VIEW`: View name , NULL
* `SQLITE_DELETE`: Table name, NULL
* `SQLITE_READ`: Table name, Column name

[Full list of constants and codes](https://gist.github.com/coleifer/864de812c1564668c5762c28e47a3ffc)
#### Examples

Prevent a user's password from being read by replacing the password with NULL. (`SQLITE_READ`)

Create the table:

    import sqlite3

    db = sqlite3.connect('/tmp/auth-demo.db')
    db.execute('CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT)')
    db.execute('INSERT INTO users (username, password) VALUES (?, ?), (?, ?)',
            ('huey', 'meow', 'mickey', 'woof'))

Next we write an autorizer function:

    def authorizer(action, arg1, arg2, db_name, trigger_name):
        if action == SQLITE_DELETE and arg1 == 'users':
            return SQLITE_DENY  # 1
        elif action == SQLITE_READ and arg1 == 'users' and arg2 == 'password':
            return SQLITE_IGNORE  # 2
        return SQLITE_OK  # 0

> This denies attempts to delete a user and ignores requests to read a users password

Then register the autorizer:

    db.set_authorizer(authorizer)

    cursor = db.execute('SELECT * FROM users;')
    for username, password in cursor.fetchall():
        print(username, password)  # Password will be None (NULL).

    db.execute('DELETE FROM users WHERE username = ?', ('huey',))

Output with the autorizer set:

    huey None
    mickey None
    sqlite3.DatabaseError: not authorized

Output without the authorizer set:

    huey meow
    mickey woof

### Going Fast with SQLite and Python

#### Transactions, Concurrency, and Autocommit

* By default, pysqlite will open a transaction when you issue your first write query 
* The transaction is commited when you run `Connection.commit()` or any other query that is not `CREATE`, `INSERT`, `UPDATE` and `DELETE` (eg. CREATE TABLE or PRAGMA)

> This makes it very easy to issue a write, which acquires the global SQLite write lock, and then unnecessarily hold that lock while you issue SELECT queries, etc, which have no need of the write lock.

* SQLite only allows a single writer per database
* Best interest to keep write transactions as short as possible
* gives a false impression that SQLite is completely unsuitable for any application that requires concurrent database access

There are a couple ways to address the problematic interaction of the global write lock:

- **Use the write-ahead-logging (WAL) `journal_mode` option** - multiple readers co-exist with a single writer. Ordinarily, when one connection is holding the write lock, no other connection can write or read until the lock is released. WAL-mode relaxes these restrictions by allowing readers to operate while another connection writes to the database.
- **Using pysqlite in autocommit mode and explicitly managing transactional state in your application** - ensure you are not holding a write lock longer than you have to. Unless you explicitly issue a BEGIN statement, opening a transaction, all statements will be executed independently, in their own transactions.

> Writes occur very quickly, so it is possible for many connections to write to the database in a performant manner even though the writes occur one-at-a-time.

#### Examples

Open database in autocommit mode by setting isolation_level to None:

    conn = sqlite3.connect('app.db', isolation_level=None)

Set journal mode to WAL.

    conn.execute('pragma journal_mode=wal')

Default vs `WAL`:

    import sqlite3

    writer = sqlite3.connect('/tmp/scratch.db', isolation_level=None)
    reader = sqlite3.connect('/tmp/scratch.db', isolation_level=None)

    writer.execute('create table foo (data)')
    reader.execute('select * from foo;')  # No problem.

    writer.execute('begin exclusive;')
    reader.execute('select * from foo;')  # OperationalError: database is locked

    ### WAL-mode.

    writer = sqlite3.connect('/tmp/wal.db', isolation_level=None)
    writer.execute('pragma journal_mode=wal;')

    reader = sqlite3.connect('/tmp/wal.db', isolation_level=None)
    reader.execute('pragma journal_mode=wal;')

    writer.execute('create table foo (data)')
    reader.execute('select * from foo')  # No problem.

    writer.execute('begin exclusive')  # Acquire write lock.
    reader.execute('select * from foo')  # Still no problem!

#### User-defined Functions

SQLite runs embedded in memory alongside your application, allowing you to easily extend SQLite with your own Python code.

#### Useful PRAGMAs

* `journal_mode = wal` - enabling write-ahead-logging means that multiple readers can coexist with a single writer
* `cache_size = -size in KiB` - the default cache size is `~2MB`. Typically you will want your cache to be large enough to hold your working data in memory, so size up accordingly. _positive values are treated as number of pages, negative values are treated as KiB._
* `mmap_size = size in bytes` - may be more performant for I/O intensive applications, and may also use less RAM since pages can be shared with the OS cache
* `synchronous = 0` - use with caution! Disabling syncs can cause data corruption in the event of operating system crash or sudden power loss.

> Non-persistent PRAGMA queries should be executed whenever a new connection is opened. Of the above only `journal_mode` is persisted.

#### Compilation Flags

Many distributions ship with an old-ish version of SQLite that does not include some of the cool extension modules.

This is how Charles compiles sqlite:

    SQLITE_ALLOW_COVERING_INDEX_SCAN=1 -- enable cover index optimization
    SQLITE_DEFAULT_CACHE_SIZE=-8000 -- more sane default
    SQLITE_DEFAULT_SYNCHRONOUS=0 -- faster, corruption only possible due to power failure or os crash.
    SQLITE_DEFAULT_WAL_SYNCHRONOUS=0
    SQLITE_DISABLE_DIRSYNC -- small optimization to reduce syncs when files deleted
    SQLITE_ENABLE_FTS3 -- enable all the full-text search extensions!
    SQLITE_ENABLE_FTS3_PARENTHESIS
    SQLITE_ENABLE_FTS4
    SQLITE_ENABLE_FTS5
    SQLITE_ENABLE_JSON1 -- enable native JSON support
    SQLITE_ENABLE_STAT4 -- enable the statistics extension
    SQLITE_ENABLE_UPDATE_DELETE_LIMIT -- allow LIMIT clause on UPDATE and DELETE queries.
    SQLITE_STMTJRNL_SPILL=-1 -- do not spill the statement journal to disk
    SQLITE_TEMP_STORE=3 -- never use disk for temporary storage
    SQLITE_USE_URI -- allow URI connection strings

For debugging and profiling:


    SQLITE_ENABLE_COLUMN_METADATA -- make additional metadata available.
    SQLITE_ENABLE_DBSTAT_VTAB -- more statistics! Check out the docs.
    SQLITE_ENABLE_EXPLAIN_COMMENTS -- adds additional info to EXPLAIN output.
    SQLITE_ENABLE_IOTRACE -- adds .iotrace command to shell for low-level I/O logging.
    SQLITE_ENABLE_STMT_SCANSTATUS -- see [docs](https://sqlite.org/c3ref/stmt_scanstatus.html).

To compile the latest:

    fossil clone http://www.sqlite.org/cgi/src sqlite.fossil
    mkdir sqlite-src
    cd sqlite-src/
    fossil open ../sqlite.fossil

    export CFLAGS="-DSQLITE_ENABLE_FTS3 -DSQLITE_ENABLE_JSON1..."  # etc...
    export CFLAGS="$CFLAGS -fPIC -O2"
    export PREFIX="$(pwd)"
    LIBS="-lm" ./configure --enable-static --enable-shared --prefix="$PREFIX"
    make && make install


## Sources

* [Going Fast with SQLite and Python - //charlesleifer.com](https://charlesleifer.com/blog/going-fast-with-sqlite-and-python/)
* [SQLite Database Authorization and Access Control with Python](https://charlesleifer.com/blog/sqlite-database-authorization-and-access-control-with-python/)