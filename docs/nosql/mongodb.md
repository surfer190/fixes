---
author: ''
category: NoSQL
date: '2022-06-25'
summary: ''
title: MongoDB Basics
---

## MongoDB Basics

### What is it?

* Mongodb is a general-purpose document database.
* Scale-out and sharding is a first class citizen
* Build for ease of development and scaling

### Key Aspects

#### Documents

* Data is stored as **JSON Documents**
* The fields in a JSON document can vary from document to document - unlike Relation Databases.
* Allows to work with complex, fast-changing and messy data.
* _It enables developers to quickly deliver new application functionality_

Advantages of documents:

* Documents correspond to native data types in many programming languages.
* Embedded documents and arrays reduce need for expensive joins.
* Dynamic schema supports fluent polymorphism.

#### Collections

* Group of documents
* Like a SQL table with no Schema
* Each collection is associated with one MongoDB database.

#### Replica Sets

* When you create a database in MongoDB, the system automatically creates at least two more copies of the data, referred to as a replica set.
* Continuously replicate data between them, offering redundancy and protection against downtime in the face of a system failure or planned maintenance

#### Sharding

* Modern systems: Big clusters of small machines
* MongoDB shards data at the collection level, distributing documents in a collection across the shards in a cluster.

#### Indexes

* Improve query speed
* Important to know what can speed up and what index to use

#### Aggregation Pipelines

* Data processing pipelines

#### Supported Languages

* [Drivers](https://www.mongodb.com/docs/drivers/)
* Python

### Install

There is a push to make you use the cloud versions to get started but it is a bit lower down in the docs how to run [community edition on mac](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/), [linux](https://www.mongodb.com/docs/manual/administration/install-on-linux/) or [windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)

> MongoDB 5.0 Community Edition supports macOS 10.14 or later.

Damn, perhaps I can use a container for it.

#### Run a Mongo Container with Docker

    mkdir local_mongo_data
    docker run --name mongodb -d -p 27017:27017 -v /my-abs-path/local_mongo_data:/data/db mongo

* `-p 27017:27017`: This exposes the port 27017 locally to the containers 27017 port
* `-v ./local_mongo_data:/data/db`: Persists data locally from the container

Enter the bash shell:

    docker exec -it mongodb bash

There are 2 mongo shells: `mongo` and `mongosh`

    mongo
    mongosh

### Docs

There are 3 versions of mongo:

* MongoDB Community: Open-source, community version
* MongoDB Enterprise
* Mongo DB Atlas: Managed Service

### Query API

Supports:

* Create
* Read
* Update
* Delete
* Data Aggregation
* Text-search and geospatial queries

There is a [mapping from SQL to mongo queries reference](https://www.mongodb.com/docs/manual/reference/sql-comparison/)

### High Performance

* Support for embedded data models reduces I/O activity on database system.
* Indexes support faster queries and can include keys from embedded documents and arrays.

### High Availability

Replica sets provide:

* automatic failover
* data redundancy

### Horizontal Scalability

* Sharding across clusters
* Zones

### Support for Multiple Storage Engines

* Wired tiger - encrypted at rest
* In-memory

## Getting Started

### Mongo DB Shell

* `db` - refers to current db
* `show dbs` - list dbs available
* `use db` - switch to another db (automatically created when you add data)

### Databases and Collections

MongoDB stores data records as documents - BSON documents - a binary representation of json.

Create a database:

    db.myNewCollection1.insertOne({ x: 1 })

> This creates the database, collection and document - if they don't already exist

You can explictly create a collection:

    db.createCollection()

In Mongo 3.2 and onwards you can enforce a schema / validation with **Document Validation** - ensuring al the documents have the same fields.

#### Unique Identifiers

Collections are assigned an immutable UUID.

Retrieve UUIDs for collections:

    db.getCollectionInfos()


    
## Sources

* [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/)