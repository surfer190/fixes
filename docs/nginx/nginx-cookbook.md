---
author: ''
category: nginx
date: '2022-12-19'
summary: ''
title: Nginx Cookbook
---

# Nginx Coookbook

## Basics

Check version:

    nginx -v
    nginx version: nginx/1.20.1

Check it is running:

    ps -ef | grep nginx
    root      270819       1  0 Nov06 ?        00:00:00 nginx: master process /usr/sbin/nginx -c /etc/nginx/nginx.conf
    www-data  353025  270819  0 Nov11 ?        00:19:26 nginx: worker process
    www-data  353026  270819  0 Nov11 ?        00:16:39 nginx: worker process

> Nginx will always have 1 master and 1 or more worker processes. The master is running as `root` as nginx needs elevated privileges to function properly.

### Directories

* `/etc/nginx/` - configuration
* `/etc/nginx/nginx.conf` - global settings: worker process, tuning, logging and dynamic modules. A top level `http` block.
* `/etc/nginx/conf.d/` - HTTP server configuration files. Files ending in `.conf` are included in the top level `http` block. In some distros the `sites-enabled` and `sites-available` folders are used - but this convention is deprecated.
* `/var/log/nginx/` - default log location

### Commands

* `nginx -h` - help
* `nginx -v` - nginx version
* `nginx -V` - build and conf info
* `nginx -t` - test the nginx configuration
* `nginx -T` - tests and prints validated info
* `nginx -s signal` - sends a signal to the nginx master process. Eg. `stop, quit, reload, reopen`
* `nginx -s reload` - graceful reload

### Serving Static Content

Overwrite `/etc/nginx/conf.d/default.conf` with:

    server {
        listen 80 default_server;
        server_name www.example.com;
        
        location / {
            root /usr/share/nginx/html;
            index index.html index/htm;
        }
    }

* This shares static content over port 80 from `/usr/share/nginx/html`
* The `server` block defines a new context for nginx to listen for.
* `listen` directs nginx to listen on port 80.
* `server_name` defines the hostname to server requests from - if not `default_server` nginx would only direct requests here if the HTTP host heads matched the `server_name`.
* `location` block defines a configuration based on the path in the url.
* `root` tells nginx where to look for static files

More info on location matching in the [nginx docs](https://nginx.org/en/docs/http/ngx_http_core_module.html)

* `location = /` is an exact match - speeds up processing if it happens frequently
* `~*` and `~` precede regular expressions (case-insensitive and sensitive)
* `^~` if the longest matching prefix location modifier the reg ex is not checked


## 2. High-Performance Load Balancing

* Share the load among multi upstreams from horizontal scaling
* Intelligence is required to keep a tracking cookie or routing for clients for a session
* Load balancer should be smart enough to detect upstream failure
    * active vs passive health checks

### HTTP Load Balancing

Distribute load between 2 or more HTTP servers

    upstream backend {
        server 10.10.12.45:80   weight=1;
        server app.example.com:80 weight=2;
        server spare.example.com:80 backup;
    }
    server {
        location / {
            proxy_pass http://backend;
        }
    }

* This config balances load across 2 HTTP servers on port 80 and defines 1 `backup` - for when the primaries are not available.
* `upstream` - controls the load balancing for HTTP. A pool of destinations.
* `weight` defines the weight in the balancing algorithm.

### TCP Load Balancing

Distribute load between 2 or more TCP servers

    stream {
        upstream mysql_read {
            server read1.example.com:3306 weight=5;
            server read2.exmaple.com:3306;
            server 10.10.12.34:3306 backup;
        }
        server {
            listen 3306;
            proxy_pass mysql_read;
        }
    }

* `server` block directs nginx to listen on port `3306` and balance traffic between 2 MySQL read replicas.
* This config must not be added to `conf.d` as that is added to the `http` block. You would create a folder called `stream.conf.d` and use `incluse` in `nginx.conf`

    stream {
        include /etc/nginx/stream.conf.d/*.conf;
    }

then in `/etc/nginx/stream.conf.d/mysql_reads.conf`:

    upstream mysql_read {
        server read1.example.com:3306   weight=5;
        server read2.example.com:3306;
        server 10.10.12.34:3306 backup;
    }
    
    server {
        listen 3306;
        proxy_pass mysql_read;
    }

* `http` and `stream` operate at different layers of the OSI model.
* The `http` context operates at `layer 7` and `stream` operates at transport `layer 4`.

### UDP Load Balancing

Distribute load between 2 or more tcp servers

    stream {
        upstream ntp {
            server ntp1.example.com:123 weight=2;
            server ntp2.example.com:123;
        }
        server {
            listen 123 udp;
            proxy_pass ntp;
        }
    }

* set udp load balancing using `udp` on the `listen` directive
* If the service requires multiple packets to be sent back and forth use `reuseport` on the `listen` directive. Eg. OpenVPN, VOIP, Virtual desktop and DTLS (Datagram Transport Later Security)

### Load Balancing Discussion

Why does one need a load balancer when multiple hosts in a DNS A or SERV (service) record can be used?

1. Alternate balancing algorithms
2. Allowing load balancing over DNS servers themselves

UDP is relied upon with: DNS, NTP, QUIC, HTTP/3 and VOIP

### Load Balancing Methods

Round Robin load balancing does not fit your requirement as heterogenous workloads and server pools are used

Use one of: least connections, least time, generic hash, random or IP hash

    upstream backend {
        least_conn;
        server backend1.example.com;
        server backend2.example.com;
    }

* round robin: default load-balancing method
* `least_conn` - least connections new requests for to the upstream server with the least connections
* `last_time` - (only nginx plus) favours servers with lower response time
* `hash` - generic hash a hash is generated to direct traffic
* `random`
* `ip_hash` - uses client ip as a hash

> Lots of Nginx Plus stuff - seems the book's main purpose is to upsell...

### Passive Health Checks

Active health checks are only available with Nginx Plus

    upstream backend {
        server backend1.example.com:1234 max_fails=3 fail_timeout=3s;
        server backend2.example.com:1234 max_fails=3 fail_timeout=3s;
    }

* watches for failed and timed out connections

## 3. Traffic Management

...

## Source

* [Oreilly: Nginx Cookbook](https://www.nginx.com/resources/library/complete-nginx-cookbook/)
