---
author: ''
category: Docker
date: '2019-09-23'
summary: ''
title: Docker Systemd Script
---
# How to Enable SystemD script for docker Containers

In a file eg. `/etc/systemd/system/docker-praeco.service`

Example:

    [Unit]
    Description=Praeco Elastalert Docker Container
    Requires=docker.service
    After=docker.service

    [Service]
    Restart=always
    ExecStart=/usr/bin/docker container start -a praeco_elastalert_1
    ExecStop=/usr/bin/docker container stop -t 2 praeco_elastalert_1
    ExecReload=/usr/bin/docker container restart praeco_elastalert_1

    [Install]
    WantedBy=multi-user.target
    
Reload the daemon:

    sudo systemctl daemon-reload

Enable the service:

    sudo systemctl enable docker-praeco.service

Start the service:

    sudo systemctl start docker-praeco.service

## Sources

* [docker container as a systemd service](https://karlstoney.com/2017/03/03/docker-containers-as-systemd-services/)
