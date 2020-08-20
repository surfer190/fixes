---
author: ''
category: Mac
date: '2019-10-24'
summary: ''
title: How To Stop Mysql On Mac Os
---
## How to Stop a Runaway MySQL process on MacOS

I had this issue where a query was left running and burning up my pc resources.
I saw this in the activity monitor application.

To stop it I eventually had to:

    sudo mysqladmin -u root -p shutdown

You should be able to start it again by going:

    cd /
    sudo find . -name 'mysql.server'

then using the output

    sudo /usr/local/mysql-5.7.21-macos10.13-x86_64/support-files/mysql.server start

it didn't work...it took ages:

    Starting MySQL
    .................................................................................................... ERROR! The server quit without updating PID file (/usr/local/mysql/data/stephen-mbp.local.pid).

Ya damn it!!!!

## Sources

* [Stop MySQL on a MAC](https://stackoverflow.com/questions/100948/how-do-you-stop-mysql-on-a-mac-os-install)