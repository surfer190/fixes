# Nginx on CentOS

## Installation

    sudo yum install epel-release
    sudo yum install nginx
    sudo systemctl start nginx
    sudo firewall-cmd --permanent --zone=public --add-service=http 
    sudo firewall-cmd --permanent --zone=public --add-service=https
    sudo firewall-cmd --reload
    sudo systemctl enable nginx

Go to `http://server_domain_name_or_IP/`

## Configuration

The default server root directory is: `/usr/share/nginx/html`

This location is set in the default server block config file located at: `/etc/nginx/conf.d/default.conf`

Additional server blocks (known as virtual hosts in apache) can be added by creating new configuration files in `/etc/nginx/conf.d`

The nginx global configuration file is located at: `/etc/nginx/nginx.conf`


## Source

* [Install Nginx on CentOS](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-7)