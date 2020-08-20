---
author: ''
category: Elasticsearch
date: '2019-05-30'
summary: ''
title: Logstash
---
# Logstash

Test logstash config

    sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash -t

Adding filters that use filebeat for input for other applications make sure the file names begin with: `02` to `30`

## Available Beats

* Filebeat: collects and ships log files.
* Metricbeat: collects metrics from your systems and services.
* Packetbeat: collects and analyzes network data.
* Winlogbeat: collects Windows event logs.
* Auditbeat: collects Linux audit framework data and monitors file integrity.
* Heartbeat: monitors services for their availability with active probing.

## Filebeat modules

Enable a module

    sudo filebeat modules enable system

List available modules

    sudo filebeat modules list

> By default, Filebeat is configured to use default paths for the syslog and authorization logs

Can view parameters at: `/etc/filebeat/modules.d/system.yml`

Load an index template

    sudo filebeat setup --template -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'

> Filebeat comes packaged with sample Kibana dashboards that allow you to visualize Filebeat data in Kibana



