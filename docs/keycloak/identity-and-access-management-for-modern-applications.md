---
author: ''
category: Keycloak
date: '2021-12-23'
summary: ''
title: Notes on Keycloak - Identity and Access Management for Modern Applications
---

# Notes on Keycloak - Identity and Access Management for Modern Applications

## 1. Getting Started with Keycloak

> Keycloak is an open source Identity and Access Management tool with a focus on modern applications such as single-page applications, mobile applications, and REST APIs.

Started in 2014

Features:

* Fully customizable login pages
* Strong authentication
* Various flows: Recovery of passwords
* Requiring users to regularly update the passwords
* Accepting terms and conditions

By delegating authentication to Keycloak, your applications do not need to worry about different authentication mechanisms, or how to safely store passwords. This approach also provides a higher level of security as applications do not have direct access to user credentials; they are instead provided with security tokens that give them only access to what they need.


### Sources 

* [Stian Thorgersen. Keycloak - Identity and Access Management for Modern Applications](https://www.packtpub.com/product/keycloak-identity-and-access-management-for-modern-applications/9781800562493)
