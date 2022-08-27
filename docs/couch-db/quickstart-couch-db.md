---
author: ''
category: Couch-Db
date: '2020-07-29'
summary: ''
title: Quickstart Couch Db
---
# Notes on Couch DB

* Couch DB is a database, a NoSQL database (non relational database)
* Documents are stored, uniquely named in the db
* It provides a Restful API for creating, reading, updating and deleting documents
* CouchDB is stored in semi-structured documents

Documents are the primary unit of data

The Couch DB update model is lockless and optimistic

Single document updates either succeed or fail

Documents are indexed in B-trees by their name (Doc id) and a sequence ID.
Each update generates a new sequential number

## Getting Started

Install couch db using one of the [installation guides](http://docs.couchdb.org/en/stable/install/index.html)

[Setup couch db](http://docs.couchdb.org/en/stable/setup/index.html#setup), I will be using the single node setup.

Visit [Fauxton](https://couchdb.apache.org/fauxton-visual-guide/index.html) (The Couch DB web interface) at: `http://127.0.0.1:5984/_utils#setup`

Ensure it is running by issuing a `GET` request to port `5984`

    $ http :5984
    HTTP/1.1 200 OK
    Cache-Control: must-revalidate
    Content-Length: 208
    Content-Type: application/json
    Date: Mon, 29 Apr 2019 08:16:53 GMT
    Server: CouchDB/2.3.1 (Erlang OTP/21)
    X-Couch-Request-ID: 3d97d2fecc
    X-CouchDB-Body-Time: 0

    {
        "couchdb": "Welcome",
        "features": [
            "pluggable-storage-engines",
            "scheduler"
        ],
        "git_sha": "c298091a4",
        "uuid": "d13db32f8059f98e73f8b88cd88b3cfa",
        "vendor": {
            "name": "The Apache Software Foundation"
        },
        "version": "2.3.1"
    }

Get a list of databases

    $ http :5984/_all_dbs
    
    [
        "_global_changes",
        "_replicator",
        "_users"
    ]

Create a database

    $ http -a couch:pass PUT :5984/cricket

    {
        "ok": true
    }

Delete a database

    $ http -a couch:pass DELETE :5984/whale
    
    {
        "ok": true
    }


Use Fauxton to create a database and a document

> When you write your first programs, we recommend assigning your own UUIDs. Generating your own UUIDs makes sure that you’ll never end up with duplicate documents.

### Running Queries

> Traditional relational databases allow you to run any queries you like as long as your data is structured correctly. In contrast, CouchDB uses predefined map and reduce functions in a style known as MapReduce.

* Map functions are called once with each document as the argument
* When writing CouchDB map functions, your primary goal is to build an index that stores related data under nearby keys

Example document:

    {
        "_id": "a611132e5c11476f1363ffdb35001b8a",
        "_rev": "1-be5d5870c9ef76734789df431d0ffe7b",
        "item": "apple",
        "prices": {
            "Fresh Mart": 1.59,
            "Price Max": 5.99,
            "Apples Express": 0.79
        }
    }

Map function:

    function(doc) {
        var shop, price, key;
        if (doc.item && doc.prices) {
            for (shop in doc.prices) {
                price = doc.prices[shop];
                key = [doc.item, price];
                emit(key, shop);
            }
        }
    }

> It’s important to check for the existence of any fields before you use them

## Couch DB Core API

* CouchDB is a database management system (DMS) - it can hold mutilple databases
* A database is a bucket that holds related data

### Create a DB

    $ http -a couch:pass PUT :5984/test
    {
        "ok": true
    }

If it fails a second time:

    http -a couch:pass PUT :5984/test
    {
        "error": "file_exists",
        "reason": "The database could not be created, the file already exists."
    }

> Couchdb stores each database in a single file

### Delete a db

    $ http -a couch:pass delete :5984/test

> Be careful with this, it is hard to bring your data back without a backup

### Documents

* Couch DB's central data structure
* Couch DB uses JSON to store documents
* Each document in CouchDB has an ID, unique per database.
* UUID's: UUIDs are random numbers that have such a low collision probability that everybody can make thousands of UUIDs a minute for millions of years without ever creating a duplicate.

#### Creating a document

    http PUT :5984/hello-world/6e1295ed6c29495e54cc05947f18c8af title='There is Nothing Left to Lose' artist='Foo Fighters'

    {
        "id": "6e1295ed6c29495e54cc05947f18c8af",
        "ok": true,
        "rev": "1-4b39c2971c9ad54cb37e08fa02fec636"
    }

#### Get a UUID

You can get a uuid with:

    http :5984/_uuids
    {
        "uuids": [
            "a611132e5c11476f1363ffdb350051c1"
        ]
    }

You can get more than 1 uuid with:

    http :5984/_uuids?count=10
    {
        "uuids": [
            "a611132e5c11476f1363ffdb35005cb4",
            "a611132e5c11476f1363ffdb350068d0",
            "a611132e5c11476f1363ffdb35006b23",
            "a611132e5c11476f1363ffdb3500787f",
            "a611132e5c11476f1363ffdb3500815f",
            "a611132e5c11476f1363ffdb35008d9a",
            "a611132e5c11476f1363ffdb350095fb",
            "a611132e5c11476f1363ffdb3500a5ad",
            "a611132e5c11476f1363ffdb3500b3cc",
            "a611132e5c11476f1363ffdb3500bc0c"
        ]
    }

#### Get a document

    $ http GET :5984/hello-world/6e1295ed6c29495e54cc05947f18c8af
    {
        "_id": "6e1295ed6c29495e54cc05947f18c8af",
        "_rev": "1-4b39c2971c9ad54cb37e08fa02fec636",
        "artist": "Foo Fighters",
        "title": "There is Nothing Left to Lose"
    }

`_rev` stands for revision

#### Revisions

Whenever you change a field in couch you load and save an entire new revision (or version) of the document

If you want to update or delete a document, couchdb expects you to include the `_rev` field of the revision you wish to change.
This prevents you from overwriting data you didn't know existed - or whoever changes the file first...wins.

If you don't pride a `_rev` field:

    $ http PUT :5984/hello-world/6e1295ed6c29495e54cc05947f18c8af title='There is Nothing Left to Lose' artist='Foo Fighters' year=1997
    {
        "error": "conflict",
        "reason": "Document update conflict."
    }

If you add the revision version

    $ http PUT :5984/hello-world/6e1295ed6c29495e54cc05947f18c8af title='There is Nothing Left to Lose' artist='Foo Fighters' year=1997 _rev=1-4b39c2971c9ad54cb37e08fa02fec636
    {
        "id": "6e1295ed6c29495e54cc05947f18c8af",
        "ok": true,
        "rev": "2-a0ecd0b4133f5d5824078835d510c231"
    }

> CouchDB accepted your write and also generated a new revision number. The revision number is the MD5 hash of the transport representation of a document with an `N-` prefix denoting the number of times a document got updated

This is called MVCC (Multi-Version Concurrency Control) - chosen because HTTP is stateless.

> CouchDB does not guarantee that older versions are kept around. Don’t use the `_rev` token in CouchDB as a revision control system for your documents.

### Documents in Detail

Get a UUID

    $ http :5984/_uuids

Create the document

    $ http PUT :5984/hello-world/a611132e5c11476f1363ffdb3500bcd0 title="Blackened Sky" artist="Biffy Clyro" year=2002
    HTTP/1.1 201 Created
    Cache-Control: must-revalidate
    Content-Length: 95
    Content-Type: application/json
    Date: Mon, 29 Apr 2019 10:12:29 GMT
    ETag: "1-c593a87983eabbc39bb70f04cb0e57a6"
    Location: http://localhost:5984/hello-world/a611132e5c11476f1363ffdb3500bcd0
    Server: CouchDB/2.3.1 (Erlang OTP/21)
    X-Couch-Request-ID: bd37be00af
    X-CouchDB-Body-Time: 0
    {
        "id": "a611132e5c11476f1363ffdb3500bcd0",
        "ok": true,
        "rev": "1-c593a87983eabbc39bb70f04cb0e57a6"
    }

An `ETag` is returned and is the same as `rev`

### Attachments

* Files attached to a document
* Attachments get their own URL where you can upload data

Adding an attachment:

    $ http put :5984/hello-world/a611132e5c11476f1363ffdb3500bcd0/chart.png?rev=1-c593a87983eabbc39bb70f04cb0e57a6 @~/Desktop/chart.png Content-Type:image/png
    {
        "id": "a611132e5c11476f1363ffdb3500bcd0",
        "ok": true,
        "rev": "2-3b33267677cceecb6c209ac2fb391abf"
    }

The attachment will be added to the document:

    $ http :5984/hello-world/a611132e5c11476f1363ffdb3500bcd0
    {
        "_attachments": {
            "chart.png": {
                "content_type": "image/png",
                "digest": "md5-y9V09vx/4l7/UWfzwTaDmw==",
                "length": 422288,
                "revpos": 2,
                "stub": true
            }
        },
        "_id": "a611132e5c11476f1363ffdb3500bcd0",
        "_rev": "2-3b33267677cceecb6c209ac2fb391abf",
        "artist": "Biffy Clyro",
        "title": "Blackened Sky",
        "year": "2002"
    }

`_attachments` a list of keys and values of JSON objects containing attachment data

A request with `?attachments=true` will return a base64 encoded attachment




## Source

* [Couch DB docs](http://docs.couchdb.org/en/stable/index.html)
