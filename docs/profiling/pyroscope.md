---
author: ''
category: profiling
date: '2022-12-20'
summary: ''
title: Pyroscope
---

## Create server

    docker run -it -p 4040:4040 pyroscope/pyroscope:latest server

## Add to App

    pip install pyroscope-io

Add code to your application:

    import pyroscope
    pyroscope.configure(
        application_name = "service_name.service",
        server_address   = "http://localhost:4040",
    )

