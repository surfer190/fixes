---
author: ''
category: Centos
date: '2019-05-30'
summary: ''
title: Firewall Cmd
---
# Firewall CMD Basics

List all rules

    sudo firewall-cmd --list-all

Check state

    sudo firewall-cmd --state

Add permanent rule

    sudo firewall-cmd --permanent --zone=public --add-service=http 
    sudo firewall-cmd --permanent --zone=public --add-service=https
    sudo firewall-cmd --reload

View the default zone

> Zones are pre-constructed rulesets for various trust levels

    sudo firewall-cmd --get-default-zone

List all zones

    sudo firewall-cmd --list-all-zones

View all services

    sudo firewall-cmd --get-services

Add a nonstandard port:

    sudo firewall-cmd --zone=public --add-port=3030/tcp --permanent
    sudo firewall-cmd --reload

## Sources

* [Stackoverflow open port on CentOS](https://stackoverflow.com/questions/24729024/open-firewall-port-on-centos-7)
* [Introduction to FirewallD on Cent](https://www.linode.com/docs/security/firewalls/introduction-to-firewalld-on-centos/)

