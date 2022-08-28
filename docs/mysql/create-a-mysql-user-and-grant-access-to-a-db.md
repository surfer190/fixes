---
author: ''
category: MySQL
date: '2022-05-26'
summary: ''
title: Create a MySQL User and Grant Access to a Database
---

### Create a MySQL User and Grant Access to a Database

Login:

    mysql -u root -p

Create a user:

    CREATE USER 'user'@'%' IDENTIFIED BY 'password'

Grant the user access:

    GRANT ALL PRIVILEGES ON database.* TO 'user'@'%';

## Sources:

* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)