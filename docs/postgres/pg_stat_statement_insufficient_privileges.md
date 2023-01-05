---
author: ''
category: postgres
date: '2022-10-15'
summary: ''
title: GIve a user access to read stats
---

Allowing a user access to stats

    GRANT pg_read_all_stats TO <username>;

eg.

    GRANT pg_read_all_stats TO local;

## Sources

* [Stackoverflow: postgresql insufficient privilege](https://stackoverflow.com/questions/50550182/postgresql-insufficient-privilege)
