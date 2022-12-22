---
author: ''
category: peewee
date: '2022-11-24'
summary: ''
title: Enable Logging peewee
---

Enable logging of SQL with peewee

    import logging
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

You can also run `ModelSelect.sql()`

### Source:

* [Peewee orm docs: Relationships](https://docs.peewee-orm.com/en/latest/peewee/relationships.html)
