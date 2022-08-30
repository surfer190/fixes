---
author: ''
category: Mysql
date: '2019-08-27'
summary: ''
title: Turn On Mysql General Log
---
### How to turn on Mysql General Log

Add the log settings in `/etc/mysql/my.cnf`

    [mysqld]
    general_log_file = /var/log/mysql/mysql.log
    general_log = 1

Or in Mysql cli (`mysql -u <username> -p`) run

    > SET GLOBAL general_log=1;

Restart the service:

    sudo systemctl restart mysql

#### Source

* [AskUbuntu MySQL](https://askubuntu.com/questions/699964/how-to-activate-mysql-general-log-in-version-5-6)