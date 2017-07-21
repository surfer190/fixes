# How to increase the file size limit for magento 2 import

## Ubuntu

1. `sudo vim /etc/nginx/sites-available/my-server.conf`

Add this line in `server` group:

            client_max_body_size 5M;

2. Change PHP Max upload

            sudo vim /etc/php/7.0/fpm/php.ini 


Add:

            upload_max_filesize = 5M

3. Restart `php-fpm` and `nginx`

            sudo service php7.0-fpm restart
            sudo service nginx restart

## Mac


1. `sudo vim /usr/local/etc/nginx`

Add this line in `server` group:

            client_max_body_size 5M;

2. Change PHP Max upload

            sudo vim /usr/local/etc/php/7.0/php-fpm.conf 


Add:

            upload_max_filesize = 5M

3. Brew restart `nginx` and `php-fpm`

            brew services restart nginx
            brew services restart php70

