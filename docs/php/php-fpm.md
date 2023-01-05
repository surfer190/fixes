---
author: ''
category: php
date: '2022-12-23'
summary: ''
title: PHP FPM
---

PHP-FPM stands for PHP FastCGI Process Manager

## Check PHP FPM Config

    sudo php-fpm8.1 -t

    [22-Dec-2022 20:34:01] NOTICE: configuration file /etc/php/8.1/fpm/php-fpm.conf test is successful

## Systemctl

Check status:

    sudo systemctl status php8.1-fpm.service

Restart:

    sudo systemctl restart php8.1-fpm.service

## Get Running Info / Config

    sudo php-fpm8.1 -tt

## Source

* [Tecmint: PHP FPM Status monitoring](https://www.tecmint.com/enable-monitor-php-fpm-status-in-nginx/)
* [Stackoverflow: Get a list of PHP FPM Pools](https://stackoverflow.com/questions/45762059/how-do-i-get-a-list-of-all-php-fpm-pools-from-command-line)
