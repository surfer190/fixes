---
author: ''
category: Openshift
date: '2019-11-18'
summary: ''
title: Add User To Cluster Admin Role
---
## Add a user to cluster admin role

List all user

    oc get user

Add a user to `sudoers`:

    oc adm policy add-cluster-role-to-user cluster-admin <username>

### Source

* [Openshift Cluster Admin Add](https://docs.openshift.com/container-platform/3.3/admin_solutions/user_role_mgmt.html#creating-a-cluster-administrator)