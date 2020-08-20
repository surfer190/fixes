---
author: ''
category: Python
date: '2020-03-05'
summary: ''
title: Jinja Append To List
---
## Append to a List with Jinja

To append to a list you need to use display brackets `{{` and `}}` and then use a hack to not actually display anything
    {% set policy_list = [] %}
    {% for ip in host_ip  %}
        {{ policy_list.append(ip) or "" }}
> So lame

### Source

* [how to append to a list in jinja2 for ansible](https://stackoverflow.com/questions/49619445/how-to-append-to-a-list-in-jinja2-for-ansible)