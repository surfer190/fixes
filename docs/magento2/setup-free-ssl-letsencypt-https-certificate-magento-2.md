---
author: ''
category: Magento2
date: '2017-04-08'
summary: ''
title: Setup Free Ssl Letsencypt Https Certificate Magento 2
---
# How to Setup a Free SSL Letsencrypt HTTPS certificate Magento 2

    root $MAGE_ROOT/pub;

    index index.php;
    autoindex off;
    charset UTF-8;
    error_page 404 403 = /errors/404.php;
    #add_header "X-UA-Compatible" "IE=Edge";

    location ~ /\.well-known\/acme-challenge {
        allow all;
    }

The key part is allowing the `.well-known/acme-challenge`

## Step 2

Then make sure to point `letsencypt` to the `pub` directory

    sudo letsencrypt certonly -a webroot --webroot-path=/var/www/root_html/pub -d example.co.za -d www.example.co.za

Any issues follow this tutorial [nginx letencrypt on ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)
