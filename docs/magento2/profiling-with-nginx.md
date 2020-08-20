---
author: ''
category: Magento2
date: '2017-05-24'
summary: ''
title: Profiling With Nginx
---
## Adding magento 2 profiling in Nginx

Add to `/var/www/html/nginx.conf` (If required):

fastcgi_param  MAGE_PROFILER $MAGE_PROFILER;

Add to server: `/etc/nginx/sites-enabled/mysite.cnf`

set $MAGE_PROFILER "2";

## Disabling magento 2 profiling on Nginx

After disabling/removing directives you might have to `force-reload` on nginx