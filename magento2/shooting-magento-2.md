## Local Dev Setup

When developing we will use vagrant to mimick the staging and live environments as close as possible

**Install NFS first** to speed up vagrant: `sudo apt-get install nfs-kernel-server`

1. Install [https://www.vagrantup.com/downloads.html](vagrant 1.8.6 or later)

2. In the root folder `vagrant up`

3. Ansible will break because there is no python so you need to `vagrant ssh` and run:

```
sudo apt-get install python-minimal
```

4. `vagrant provision`

5. Add this to `/etc/hosts`:

    192.168.33.121 shootingstuff.dev


6. Install the site `vagrant ssh`

  **todo: automate**

    bin/magento setup:install --db-name=shootingstuff --db-user={{ username }} --db-password={{ pass }} --admin-firstname={{ firstname }} --admin-lastname={{ lastname }} --admin-email={{ admin_email }} --admin-user={{ username }} --admin-password=Abc1234#

7. Fix the nginx config:

  **It should look like this**

    server {
    listen 80;
    server_name "shootingstuff.dev";
    access_log /var/log/nginx/shootingstuff-access.log;
    error_log /var/log/nginx/shootingstuff-error.log;
    include /var/www/shootingstuff/nginx.conf.sample;
    set $MAGE_ROOT "/var/www/shootingstuff";
    }

    upstream fastcgi_backend {
    server   unix:/var/run/php/php7.0-fpm.sock;
    }

8. Change your web user to same as vagrant (Only for dev)

  Fixes: **PHP message: PHP Fatal error:  Uncaught Zend_Cache_Exception: cache_dir "/var/www/shootingstuff/var/page_cache" is not writable in**


        sudo vim /etc/nginx/nginx.conf

        user              ubuntu  ubuntu;

        sudo vim /etc/php/7.0/fpm/pool.d/www.conf

        user = ubuntu
        group = ubuntu
        listen.owner = ubuntu
        listen.group = ubuntu
        listen.mode = 0660

9. Add magento2 tool to the path `.bashrc`

    export PATH=$PATH:/var/www/html/magento2/bin

#### Things to Change

    * Import Demo 2 Static blocks and settings
    * Disable the  newsletter popup
    * Change footer logo image: `Config -> Porto -> Porto (Settings Panel)`
    * Footer: Ribbon Text
    * Disable product radius - Doesn;t really work
    * Category View: Show Rating Stars (False)
    * Remove - product sideblock in settings: `porto_product_side_custom_block`
    * Product Tabs Style - Product View: `vertical`

    Some of the html content for blocks is kept in this repo in `html-content`

    * Header - contact info : Edit the block `porto_custom_block_for_header`
    * Footer - first block : `porto_footer_links`
    * Footer - bottom block: `porto_footer_bottom_custom_block`
    * Category View sidebar - disabled: `porto_category_side_custom_block.html`

    * Porto: Design Panel - change colours of header search box and all that other stuff

    #### Customisation

    The theme will be customised so we created `porto_child` in the folder.

    `Stores -> Configuration -> General -> Design -> Porto Child`
