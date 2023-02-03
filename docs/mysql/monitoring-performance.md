---
author: ''
category: MySQL
date: '2022-12-15'
summary: ''
title: Monitoring Performance
---

### Global Status

    SHOW GLOBAL STATUS;
    
### Performance Schema

    SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
       WHERE TABLE_SCHEMA = 'performance_schema';

### Query Stats

> Closest to Pg Stat Statments

    SELECT *
       FROM performance_schema.events_statements_summary_by_digest
       ORDER BY avg_timer_wait DESC
       LIMIT 20

### Sys Schema

    SELECT * FROM sys.statement_analysis;

    SELECT * FROM sys.statements_with_runtimes_in_95th_percentile;

> Looks like time is measured in picoseconds. 1000 pico seconds is a nanosecond. 1000 nanoseconds is a microsecond, 1000 microseconds is a millisecond, 1000 milliseconds is a second.

Sections:

* [Schema Progress Reporting](https://dev.mysql.com/doc/refman/8.0/en/sys-schema-progress-reporting.html) - long running processes
* [SYs Schema Object reference](https://dev.mysql.com/doc/refman/8.0/en/sys-schema-object-index.html)

### Reset Stats

    CALL sys.ps_truncate_all_tables(FALSE);

[Mysql: How to flush performance_schema stats without restarting MySQL?](https://stackoverflow.com/questions/42758188/how-to-flush-performance-schema-stats-without-restarting-mysql)

## Sources

* [merticfire.com: modern guide to mysql performance monitoring](https://www.metricfire.com/blog/a-modern-guide-to-mysql-performance-monitoring/)
* [MySQL docs: Using the Sys Scherma](https://dev.mysql.com/doc/refman/8.0/en/sys-schema-usage.html)