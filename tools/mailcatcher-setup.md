# Mailcatcher Setup

For setting up mail catcher, check the link below

[Mailcatcher setup](http://fostermade.co/blog/email-testing-for-development-using-mailcatcher)

http://lukepeters.me/blog/getting-the-php-mail-function-to-work-on-ubuntu

## With Sendmail using PHP-fpm

It is important to use the **absolute path** to `catchmail`

`vim /etc/php/7.0/fpm/pool.d/www.conf`

Contents:

`php_admin_value[sendmail_path] = /usr/bin/env /usr/local/bin/catchmail -f catch@mymail.com`

`vim fpm/php.ini`

Contents:

`sendmail_path = /usr/bin/env /usr/local/bin/catchmail -f catch@mymail.com`
