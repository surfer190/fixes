---
author: ''
category: Es
date: '2020-03-05'
summary: ''
title: Queries
---
# Do a SQL Query
POST /_xpack/sql?format=txt
{
  "query": "select * from user_mapping",
  "fetch_size": 10
}

# Translate SQL to ES Query Language
GET /_xpack/sql/translate
{
  "query": "select Name, Result, Type from veeam_job"
}

# Read only mode Kibana
PUT .kibana/_settings
{
  "index": {
    "blocks": {
      "read_only_allow_delete": "false"
    }
  }
}

PUT veeam_repo/_settings
{
  "index": {
    "blocks": {
      "read_only_allow_delete": "false"
    }
  }
}
