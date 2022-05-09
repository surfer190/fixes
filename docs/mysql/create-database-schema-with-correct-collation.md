---
author: ''
category: MySQL
date: '2022-02-14'
summary: ''
title: Create a database schema with the Correct Collation
---

# Create a MySQL database schema with the Correct Collation

In < MySQL 8.0:

    CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

In > MySQL 8.0:

    CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

## Sources

* [DBA Overflow](https://dba.stackexchange.com/questions/76788/create-a-mysql-database-with-charset-utf-8)
* 