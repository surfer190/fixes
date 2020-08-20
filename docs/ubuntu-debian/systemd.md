---
author: ''
category: Ubuntu-Debian
date: '2019-05-31'
summary: ''
title: Systemd
---
# SystemD

All about systemD and more importantly how to use and create services that automatically start on system startup

SystemD is the main adopted system and service manager for Linux

## Common Commands

Show system status

    systemctl status

List failed units

    systemctl --failed

List installed unit files

    systemctl list-unit-files

List all running services

    systemctl

Start a service

    systemctl start <service_name>

Stop a service

    systemctl stop <service_name>

Restart a service:

    systemctl restart <service_name>

Show status of a service:

    systemctl status <service_name>

Enable a service on startup:

    systemctl enable <service_name>

Disable a service during startup:

    systemctl disable example1

## Creating or altering services

Units are defined by individual configuration files, called `unit files`

Unit files provided by debian are found in: `/lib/systemd/system`

An identically named unit file in `/etc/systemd/system`, takes precedence over those in `/lib/systemd/system`

System admins should put unit files in: `/etc/systemd/system`

## Example

Create this file

        [Unit]
        Description= kong service
        After=syslog.target network.target postgresql.service

        [Service]
        User=root
        Group=root
        Type=forking
        ExecStart=/usr/local/bin/kong start
        ExecReload=/usr/local/bin/kong reload
        ExecStop=/usr/local/bin/kong stop

        [Install]
        WantedBy=multi-user.target

Then run

        systemctl start kong
        systemctl stop kong
        systemctl enable kong


## Forking vs Simple

According to this post on the [SystemD Forking vs Simple](https://superuser.com/questions/1274901/systemd-forking-vs-simple/1274913) if a service does not return anything and can only be closed with `ctrl+c` you should use `simple`.

If it does daemonise itself, then you should use `forking`

If a service just does one thing, then `oneshot` is the right choice.

## Using a Python Virtualenv

> The virtualenv is "baked into the Python interpreter in the virtualenv"

For example an elastalert systemd service (Remember `ExecStart` needs an absolute path):

    [Unit]
    Description=elastalert
    After=elasticsearch.service

    [Service]
    Type=simple
    WorkingDirectory=/home/cent/elastalert/
    User=cent
    Group=cent
    Restart=on-failure
    ExecStart=env/bin/python -m elastalert.elastalert --config config.yaml --verbose

    [Install]
    WantedBy=multi-user.target

Enable and start it:

    systemctl daemon-reload
    systemctl enable elastalert.service
    systemctl start elastalert.service
    systemctl status elastalert.service



## Source

* [SystemD Debian Wiki](https://wiki.debian.org/systemd)
* [Virtualenv in SystemD](https://stackoverflow.com/questions/37211115/how-to-enable-a-virtualenv-in-a-systemd-service-unit)