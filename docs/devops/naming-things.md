---
author: ''
category: Devops
date: '2022-04-01'
summary: ''
title: Naming Things
---
## Naming things

> More care must be taken around the naming of things

### Naming things as a Cloud Architect

When you architect a system you might build and configure it but not be involved in day-to-day operations.
But a host of other people are: automations, operations, implementations, Managed IT services and Service Centre staff.

If we can save just a few seconds of confusion and frustration - making things more obvious - then we would have saved everyone hours and days of time and customers even more when things get resolved faster.

It may take a lot longer to think of a meaningful name but you could be saving days for other people.

Names should be:

* Consistent
* Obvious

Adding features across new regions becomes easier when names of things are consistent across regions.

> You want to give the minimum to make it distinct.

Things to avoid:

* Unnecessary large name
* Inconsistent naming.
* Knowing the difference between display names and ids. Automation teams will use the `id` or `uuid` while frontend users will use the _display name_. Don't mix the display name with the id
* Case - keep the same case
* Spaces - no spaces - if possible for api related stuff

## Know who is using your system

Users should know where to go - in an obvious way and not require a lookup.

For example to go to ovirt management console:

    ovirt.example.com

Is obvious. xkm65099vm.example.com is not.


## Sources

* [Naming things is hard](https://greggigon.com/2019/11/25/naming-things-is-hard-and-very-important/)