---
author: ''
category: Network-Automation
date: '2021-12-24'
summary: ''
title: Netbox Extensability Overview
---
## Netbox Extensability Overview

* Core features in netbox to enhance way you use netbox
* Allow team and org to integrate

### Expertise required

From easiest to hardest

* NAPALM
* Custom Fields
* Custom Links
* Webhooks
* Export Templates
* REST Api
* Reports
* Custom Scripts
* Plugin Framework

### NAPALM

* feature is exposed in REST API - API proxy for napalm library
* Interface connection LLDP Neighbours
* device status and config

Usage:

1.

    pip install napalm

2. Create Platform and specify NAPALM driver
3. Assign platform to device with primary IP
4. Access NAPALM related tabs

### Custom Fields

* User defined fields added to primary fields
* Something to store on each device
* Works same in UI and Rest API
* Created in the `admin section`
* Select the primary object type to add to

`Extras -> Custom Fields...`

> Not sure if this is a thing in netbox 3.0

### Custom Links

* Dynamically generated buttons
* Link netbox data to other systems

`Extras -> Custom Links..`

Link to network management system, change management or monitoring

### Webhooks

* Event data occuring in netbox sending to other systems - on object update, create or delete
* deprovisioning automation
* Template out a custom request body

`Extras -> Webhooks..`

### Export Templates

Custom CSV exports

`Extras -> Export Templates...`

### REST Api

* Programmatically interact with netbox
* Browsable API
* swagger api: /api/docs

clients:

* pynetbox
* go-netbox

### Reports

* user created validation of data
* boilerplate to execute script
* Validate that device hostnames conform to a naming convention

### Custom Scripts

* python scripts for generic actions
* similar to reports but gets user input
* business logic within netbox

* Allow provisioning
* Can do dry run
* Can do a naming convention - with user input

### Plugins Framework

* Developer centric
* Packaging functionality on top of netbox
* Can crete new models, views and APIs
* Can extend primary object views

* List views
* No burden of forking the project and maintaining the intergration and upstream

## Sources

* [Network to Code - Netbox Extensability Overview](https://www.youtube.com/watch?v=FSoCzuWOAE0)
* [NetBox Custom Scripts & Plugins, Interop 2020](https://www.youtube.com/watch?v=mjyEJHUDpfk)
