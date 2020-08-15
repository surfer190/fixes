---
author: ''
category: Magento
date: '2015-01-18'
summary: ''
title: Permissions Mcrypt Gd Must  Be Loaded
---
#Permission of the /media folder

- `chown -R www-data:www-data /var/www/magento`
- `chmod -R 775 /var/www/magento`

#mcrypt extension
- `sudo apt-get install php5-mcrypt`
- `php5enmod mcrypt`

#gd extension
- `sudo apt-get install php5-gd`
- `php5enmod gd`

##remember to restart
- `service apache2 restart`