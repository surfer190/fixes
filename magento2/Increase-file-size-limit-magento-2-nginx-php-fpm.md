# How to increase the file size limit for magento import

1. `sudo vim /etc/nginx/sites-available/my-server.conf`

Add this line in `server` group:

            client_max_body_size 5M;

2. Change PHP Max upload

```
sudo vim /etc/php/7.0/fpm/php.ini 


Add:

upload_max_filesize = 5M
```