---
author: ''
category: Magento2
date: '2017-02-01'
summary: ''
title: Set Up Mail Magento2
---
# Setting Up Mail and SMTP settings Magento 2 Server

1. Install Sendmail

    apt install sendmail

2. config sendmail

    sudo sendmailconfig

3. Edit hosts file

    127.0.0.1 localhost localhost.localdomain your_domain_name_here.com

4. Restart nginx

    sudo service nginx restart

### Note: Disable other mail modules

Like Ebizmarts..

### Source

* [Getting the PHP Mail Function to work on Ubuntu](http://lukepeters.me/blog/getting-the-php-mail-function-to-work-on-ubuntu)
