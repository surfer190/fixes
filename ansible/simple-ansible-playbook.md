#Simple Ansible Playbook

First Line - Shows Rest of document is in YAML

```
---
```

Telling ansible which hosts to use - `all` works here because Vagrant uses its own inventory file instead of one in `/etc/ansible/hosts`

```
- hosts: all
```

Tasks

```
-name: Ensure NTP daemon is installed
 apt: name=ntp state=installed
```



