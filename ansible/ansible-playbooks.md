# Ansible Playbooks

playbooks are a list of tasks

They are `yaml`

Playbooks may be included in other playbooks

#### How to Call an Ansible Playbook

```
ansible-playbook playbook.yml
```

Eg.

```
---
- hosts: all
tasks:
- name: Install Apache.
command: yum install --quiet -y httpd httpd-devel
- name: Copy configuration files.
command: >
cp /path/to/config/httpd.conf /etc/httpd/conf/httpd.conf
- command: >
cp /path/to/config/httpd-vhosts.conf /etc/httpd/conf/httpd-vhosts.conf
- name: Start Apache and configure it to run at boot.
command: service httpd start
- command: chkconfig httpd on
```

`>` sign following the `command:` tells YAML to quote the next set of indented lines as a single string.

For tasks with 1 or 2 parameters we use:
```
yum: name=apache2 state=installed
```

#### Limiting Playbooks to a particulalr hosts or Groups

```
ansible-playbook playbook.yml --limit webservers
```

Will run the playbook only on the `webservers` group, even if `hosts: all`

To see a list of would-be affected servers by a playbook:

```
ansible-playbook playbook.yml --list-hosts
```
