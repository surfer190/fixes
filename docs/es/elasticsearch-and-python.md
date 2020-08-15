---
author: ''
category: Es
date: '2019-12-10'
summary: ''
title: Elasticsearch And Python
---
## Python Clients

What is the python client to use?

* Low level client (close to http) - [elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/#)
* High level client (abstracted into models) - [elasticsearch-dsl](https://elasticsearch-dsl.readthedocs.io/en/latest/index.html)


### Create an Index

    # Define a default Elasticsearch client
    connections.create_connection(hosts=['localhost'])

    # Create index
    test_index = Index(name='test')
    test_index.create()


## Checking things with HTTP

[List all indices](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html)

    https://{host}:{port}/_cat/indices
