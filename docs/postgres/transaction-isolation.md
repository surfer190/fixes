## Transaction Isolation

> The most strict is Serializable, which is defined by the standard in a paragraph which says that any concurrent execution of a set of Serializable transactions is guaranteed to produce the same effect as running them one at a time in some order.

> The Repeatable Read mode provides a rigorous guarantee that each transaction sees a completely stable view of the database

phenomena between concurrent transactions:

* `dirty read` - A transaction reads data written by a concurrent uncommitted transaction
* `nonrepeatable read` - A transaction re-reads data it has previously read and finds that data has been modified by another transaction
* `phantom read` - A transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction.
* `serialization anomaly` - The result of successfully committing a group of transactions is inconsistent with all possible orderings of running those transactions one at a time.

| Isolation Level |	Dirty Read |	Nonrepeatable Read |	Phantom Read |	Serialization Anomaly |
| --------------- | ---------- | --------------------- | --------------- | ---------------------- |
| Read uncommitted |	Allowed, but not in PG |	Possible |	Possible |	Possible |
| Read committed |	Not possible |	Possible |	Possible |	Possible |
| Repeatable read |	Not possible |	Not possible |	Allowed, but not in PG |	Possible |
| Serializable |	Not possible |	Not possible |	Not possible |	Not possible |

[Read commited is the default isolation level](https://www.postgresql.org/docs/current/transaction-iso.html) in postgres.

### Isolation Levels

* `READ COMMITED` - a `SELECT` query sees only data committed before the query began; it never sees either uncommitted data or changes committed during query execution by concurrent transactions. However `SELECT` does see the effects of previous updates executed within its own transaction, even though they are not yet committed. Two successive SELECT commands can see different data, even though they are within a single transaction, if other transactions commit changes after the first `SELECT` starts and before the second `SELECT` starts. `UPDATE`, `DELETE`, `SELECT FOR UPDATE`, and `SELECT FOR SHARE` work in the same way - if a target row is updated or deleted by the time it is found it will wait for the other transaction to complete.
* `REPEATABLE READ` - The Repeatable Read isolation level only sees data committed before the transaction began; it never sees either uncommitted data or changes committed during transaction execution by concurrent transactions. The snapshot is seen at the start of the transaction not of the current transaction statement. Applications using this level must be prepared to retry transactions due to serialization failures. The repeatable read transaction will be rolled back if anotehr transaction affects the rows and commits with a message `ERROR:  could not serialize access due to concurrent update`. The current transaction should be aborted and retried from the beginning. 
* `SERIALIZABLE` - the strictest isolation level. Sequential execution - one after the other. The same as repeatable read except that it monitors for conditions which could make execution of a concurrent set of serializable transactions behave in a manner inconsistent with all possible serial executions of those transactions.


### Isolation Levels and Django

With django, the [default isolation level on postgres](https://docs.djangoproject.com/en/4.1/ref/databases/#optimizing-postgresql-s-configuration) is:

    default_transaction_isolation: 'read committed'

If you need `repeatable read` or `serializable` use:

    import psycopg2.extensions

    DATABASES = {
        # ...
        'OPTIONS': {
            'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
        },
    }

Serializable is good for finance stuff.

> Under higher isolation levels, your application should be prepared to handle exceptions raised on serialization failures
