---
author: ''
category: sqlalchemy
date: '2023-12-12'
summary: ''
title: Remove and add indexes programmatically
---

Indexes can made insert and update operations slow.
One may want to remove them - do the inserts/updates - then add them back once complete for performance reasons.

To do that programmatically with sqlalchemy:

### Removing Indexes

    # Remove indexes
    logger.info("START: Removing catalogue indexes")

    with session() as db_session:
        db_session.execute("COMMIT")
        db_session.execute("DROP INDEX CONCURRENTLY IF EXISTS ix_catalogue_store_code;")

    logger.info("COMPLETE: Removing catalogue indexes")

### Adding Indexes

        # Add Indexes
        logger.info("START: Adding catalogue indexes back")

        with session() as db_session:
            db_session.execute("COMMIT")
            db_session.execute("CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_multi_catalogue_version_store_code ON public.catalogue USING btree (catalogue_version, store_code);")

        logger.info("COMPLETE: Adding catalogue indexes back")

### Avoiding a Situation where the Index is not added Back

To avoid the situation where an index is not added back. Make use of a `finally` clause in python's `try...except...finally`.