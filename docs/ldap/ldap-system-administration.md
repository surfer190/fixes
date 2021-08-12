---
author: ''
category: LDAP
date: '2021-08-05'
summary: ''
title: LDAP System Administration
---
# LDAP System Administration

## 1. LDAP Basics

DNS - most successful dirctory services ever implemented on the internet

Five characteristics of directory services:

* Highly optimised for reads
* distributed model for storing information
* Can extend types of info it stores
* Advanced search capanbilities
* Loosely consistent replication

### Lightweight Directory Access Protocol

The potencial of LDAP to consolidate existing services into a single directory.
Reducing data redundancy.
Administrative saving on creating and deleting users.

* Lightweight - compared to X.5000 directory services. LDAP uses low overhead TCP over 389.
X.500 had alot more baggage.
* Directory - different from a database as it is designed to be read more than written. Transaction and write locks are not necessary. LDAP is just a protocol it says nothing about where the data is stored. Made for general directories not specialised ones - filesystems and DNS.
* Access Protocol - LDAP is asynchronous. 

### LDAP Models

Present the services provided by a server.

#### Information Model

An entry is the basic unit of a directory.
An entry contains informaiton about one or more `objectClasses`

#### Naming Model

How entries and data are uniquely referenced.
Each entry has an attribute unique among all sibling called the RDN - Relative Distinguished Name.

The string created by combining RDN's for a unique name is called the Distinguished Name (DN)

Eg. RDN (includes attribute name and value)

    cn=geraldcarter

The DN (distinguished name) for the node would be

    cn=geraldcarter,ou=people,dc=plainjoe,dc=org

#### Functional Model

Protocol itself. Authentication operations (bindings), query operations (searches and reads) and update operations (writes)

#### Security Model

Mechanism for clients to prive their identity (authnetication) and control authenticated clients access to data (authorization)


## 2. LDAPv3 Overview

