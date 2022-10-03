---
author: ''
category: MySQL
date: '2022-05-23'
summary: ''
title: How to Delete a MySQL User
---

### How to Delete a MySQL User

Login:

    mysql -u root -p
    use mysql;

List users:

    SELECT User,Host FROM mysql.user;

Show grants for a user:

    SHOW GRANTS FOR 'helloworld'@'localhost';

Revoke grants for a user:

    REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'helloworld'@'localhost';

Delete (Drop) the user:

    DROP USER 'helloworld'@'localhost';

## Sources:

* [How to delete or remove a MySQL/MariaDB user account on Linux/Unix](https://www.cyberciti.biz/faq/how-to-delete-remove-user-account-in-mysql-mariadb/)