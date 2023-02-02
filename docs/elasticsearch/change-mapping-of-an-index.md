---
author: ''
category: elasticsearch
date: '2022-12-12'
summary: ''
title: Change Mapping of an Index in Kibana
---

## Changing the Mapping of an Index in Kibana

Ever tried to create a visualisation in kibana and aggregation on a field that was not mapped?

Use Dev tools in kibana

First verify the index does no have the field mapped:

    GET <index_name>

Example:

    "mappings" : {
      "properties" : {
        "doc" : {
          "properties" : {
            "article_number" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "batch" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "catalogue_version" : {
              "type" : "long"
            },

> In this case we want catalogue_version to be keyword
## Solution

Delete and recreate the index pattern on Kibana

