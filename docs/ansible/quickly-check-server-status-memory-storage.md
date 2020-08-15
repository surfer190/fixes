---
author: ''
category: Ansible
date: '2019-02-05'
summary: ''
title: Quickly Check Server Status Memory Storage
---
#How to do quick server status checking on your servers

Check memory usage on all your servers
```
ansible [group] -a "free -m" -u [username]
```

Check storage usage on all your servers
```
ansible [group] -a "df -h" -u [username]
```
