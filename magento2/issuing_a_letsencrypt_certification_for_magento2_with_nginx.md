# How to Issue a Certificate for Magento 2 on Nginx

1. Follow these [instructions](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)

2. Add to the `nginx.conf.example` file the `location bit`

3. Run the following command, take note of the `/pub` directory

    sudo letsencrypt certonly -a webroot --webroot-path=/var/www/magento2/pub -d example.com -d example.com
