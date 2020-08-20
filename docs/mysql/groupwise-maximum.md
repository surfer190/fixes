---
author: ''
category: Mysql
date: '2019-10-24'
summary: ''
title: Groupwise Maximum
---
## MySQL Groupwise Maximum

A common problem, it seems is getting the most recent field/record along with every parent or related record in a dataset.

### Most Recent Record

So let us break it down and do it just for the table containing the maximum's we want:

    SELECT
      user_id, MAX(created_at)
    FROM
      orders
    GROUP BY
      user_id

I tried this, but unfortunately I got an error from mysql:

    Lost connection to MySQL during query



### Sources

* [Ordering within a sql group by clause](https://thoughtbot.com/blog/ordering-within-a-sql-group-by-clause)
* [Show only the most recent](https://stackoverflow.com/questions/1368331/show-only-most-recent-date-from-joined-mysql-table)
* [Groupwise Max](http://mysql.rjweb.org/doc.php/groupwise_max)
* [Groupwise Max](http://jan.kneschke.de/projects/mysql/groupwise-max/)
* [SQL join: selecting the last records in a one-to-many relationship](https://stackoverflow.com/questions/2111384/sql-join-selecting-the-last-records-in-a-one-to-many-relationship)
