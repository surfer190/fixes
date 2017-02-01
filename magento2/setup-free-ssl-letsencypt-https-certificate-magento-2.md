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

THen follow this (nginx letencrypt on ubuntu 16.04)[https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04]
