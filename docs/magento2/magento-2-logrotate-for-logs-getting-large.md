---
author: ''
category: Magento2
date: '2017-06-30'
summary: ''
title: Magento 2 Logrotate For Logs Getting Large
---
# Implementing Logrotate for large log files

The magento logs are created in `/my-site-root/var/log/*.log`

They are:

        -rwxrwxr-- 1 www-data www-data  19M Jun 26 08:05 debug.log
        -rwxrwxr-- 1 www-data www-data 1.1M Jun 26 08:05 exception.log
        -rwxrwxr-- 1 www-data www-data 1.6M Jun 26 08:08 magento.cron.log
        -rwxrwxr-- 1 www-data www-data 1.6M Jun 26 08:08 setup.cron.log
        -rwxrwxr-- 1 www-data www-data 228K Jun 26 08:05 system.log
        -rwxrwxr-- 1 www-data www-data 1.1M Jun 26 08:08 update.cron.log
        -rwxrwxr-- 1 www-data www-data 3.1M Jun 26 08:08 update.log

The problem is that magento 2 does not manage the deletion of these things.
So the `debug.log` and `update.log` can grow really big, in order of magnitude of Gigabytes.

## Implementing Logrotate

So let us deal with this issue so we don't have to remind ourselves to delete them from time to time

Create a file in `/etc/logrotate.d/` called `magento2`

Add the following contents and save:

        /var/www/shooting/var/log/*.log {
            size 10M
            missingok
            rotate 50
            compress
            delaycompress
            notifempty
            dateext
            dateformat -%Y-%m-%d-%s
        }

## Explanation

* `size` - when any of the `*.log` files become larger than 10M they are rotated
* `missingok` - if there are no logs there, do not panic
* `rotate` - Number of rotations to keep
* `compress` + `delaycompress` - compress the log after rotation, but keep the most recent uncompressed.
* `notifempty` - Do not logrotate if empty
* `create` - Not needed as magento handles log creation
* `dateext` - Add a date extension to rotated files
* `dateformat` - Sets the dateformat of the `dateext`

#### Sources

* [Rackspace logrotate](https://support.rackspace.com/how-to/understanding-logrotate-utility/)
* [Servers for hackers](https://serversforhackers.com/managing-logs-with-logrotate)
* `man logrotate`
