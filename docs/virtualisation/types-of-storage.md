---
author: ''
category: Virtualisation
date: '2021-11-23'
summary: ''
title: Types of Virtualisation Storage
---

# Types of Virtualisation Storage

The different storage types hold, organise and present data in different ways.

## File storage (File-level or file-based storage)

* Organised as a hierachy of files
* Data is stored in a folder
* The path is required
* Oldest and most widely used
* Scaling out by most systems not more capacity

## Block Storage (Block-level or block-based storage)

* Organised into chunks of evenly sized volumes
* Each block has a unique identifier
* Decouples data and puts across multiple environments
* Usually in SAN (Storage Area Network) environments and must be tied to a functioning server
* No single path to data - can be accessed quickly
* Efficient, reliable, easy to manage
* Better for lots of data
* Expensive
* Cannot handle lots of metadata

## Object Storage (Object-level or object-based storage)

* Manages data and links to associated metadata
* flat structure
* files broken into pieces and spread among hardware
* Meta data is important
* requires an HTTP Api
* Scales well
* Objects cannot be modified
* Writing objects is slow

### Source

* [File vs Block vs Object Storage](https://www.redhat.com/en/topics/data-storage/file-block-object-storage)