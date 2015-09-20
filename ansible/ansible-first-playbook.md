# Ansible your First Playbook

```
---
- hosts: all
sudo: yes
tasks:
- name: Ensure NTP (for time synchronization) is installed.
yum: name=ntp state=installed
- name: Ensure NTP is running.
service: name=ntpd state=started enabled=yes
```
