---
author: ''
category: Sqlalchemy
date: '2022-10-25'
summary: ''
title: SQLAlchemy - Enable logging
---

## SQLAlchemy: Enable logging

The namespace of the logger for `sqlalchemy` is `sqlalchemy.engine`.

Get that, then add the handler and set the level.

    sqlhandler = logging.FileHandler('sql.log')
    sqllogger = logging.getLogger('sqlalchemy.engine')
    sqllogger.setLevel(logging.INFO)
    sqllogger.addHandler(sqlhandler)

