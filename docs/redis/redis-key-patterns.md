---
author: ''
category: Redis
date: '2022-06-14'
summary: ''
title: Redis Key Patterns
---
# Redis Key Patterns

    {namespace}.{version}.{data-category}.{identifier}

Eg.

    vi.v1.connections.us1

* Don't spoil the keyspace with collisions
* Control key space in multi-tenant systems

components:

* namespace - common root identifier eg. vi (voice insights)
* version - version underlying key eg. v1
* data-category - denote collection or type of data. A database table. Plural. eg. collections
* identifier - identify a subset in a data-cateogry or an individual record

Better key searching:

    KEYS *

or:

    KEYS vi.v1.*


## Connections

    message Connection {
        unit64 created        = 1;
        string uuid           = 2;
        ConnectionGroup group = 3;
        DeviceType device     = 4;
        GeoPoint geo          = 5;
    }

    Connection.newBuilder.setCreated(12524365462345).setUuid("j6sd67adfjhdsfadiou424").setConnectionGroup(zone.us1).build()

    # redis - zadd - add to a sorted set
    zadd vi.v1.connection.{cg_zone} {created} {uuid}

* Rebuild the protobuf data by extracting data
* Encode protobuf directly into sorted set - byte array - the down side is not being able to easily make changes to the underlying protobuf type

    set vi.v1.connections.$uuid {bytes} EX {seconds}

or by zone:

    set vi.v1.connections.$zone.$uuid {bytes} EX {seconds}







## Sources

* [Youtube: The Happy Marriage of Redis and Protobuf - RedisConf 2020](https://www.youtube.com/watch?v=HBtScr7MQxU)
