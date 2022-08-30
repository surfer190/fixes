---
author: ''
category: Azure
date: '2016-09-27'
summary: ''
title: Azure Command Line
---
# Azure has a command line

### Installing the Azure Command Line

`sudo npm install -g azure-cli`

### Login to your account

1. `azure login`
2. Go to the url specified in a browser
3. Login and **bob's your uncle**

### Quick create a vm

```
azure vm quick-create -g { resource_group } -n { name } -l { location } -y { os-type } -u { username } -M { path to public key } -Q { image URN in the form publisherName:offer:skus:version }
```

But you can also just:

`azure vm quick-create` and then fill out steps

## Using help

`azure {command} help`

## List all locations

`azure location list`

## List all os-types available

**Don't think it is possible**

### Sources:

* [Microsoft install azure cli](https://azure.microsoft.com/en-us/documentation/articles/xplat-cli-install/)
