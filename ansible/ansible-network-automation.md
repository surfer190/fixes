# Ansible for Netowrk Automation

## Why Ansible for Network Automation?

* Automate repetitive tasks
* Use the same tool for network, operations and development
* Seperate the tasks (playbook) from the execution layer (ansible modules) for multi-vendor devices
* Benefit from community and vendor generated scripts
* Communicate securely with network hardware over ssh and https

Ansible can be used to configure hubs, switches, routers, bridges and other network devices.

## Basic Concepts

* control node - Any computer with python on it (but not Windows) that has `ansible` and `ansible-playbook` installed on it
* managed nodes - Network devices and servers you manage with ansible. Sometimes called `hosts`
* inventory - a list to organise managed nodes. Sometimes called `hostfile`
* modules - Units of code that ansible executes. 
* tasks - units of action in ansible
* playbook - ordered list of tasks. Can include variables, tasks and roles. Written in `yaml`.

## How Network Automation is Different

* Unlike most ansible modules, network modules do not run on managed nodes.
* The majority of network devices cannot run python
* Ansible network modules are executed on the control node (where ansible commands are called)
* Use the control node for backup files
* Network modules do not update configuration files on managed nodes, because network configuration is not written in files

### Multiple Communication Protocols

* communication protocol - XML over SSH, CLI over SSH, API over HTTPS
* Depends on platform and purpose
* Most common is `CLI over SSH`
* You can set the protocol with the `ansible_connection` variable
    * `network_cli` == `CLI over SSH`
    * `netconf` == `XML over SSH`
    * `httpapi` == `API over HTTP/HTTPS`
    * `local` == `depends`
    
### Prefixes of Network Platform

* Arista: `eos_`
* Cisco: `ios_`, `iosxr_` or `nxos_`
* Juniper: `junos_`
* VyOs: `vyos_`

### Privilege Escalation

* On network devices the equivalent of `sudo` is `enable` mode
* As of ansible 2.6 you can use `become: yes` with `become_method: enable`

Example of a group vars/host_vars file:

    ansible_connection: network_cli
    ansible_network_os: ios
    ansible_become: yes
    ansible_become_method: enable

> Be aware there are ansible 2.5 and 2.4 issues

## Run your First Command and Playbook

### Requirements

1. Ansible (>=2.5) installed
2. One or more network devices compatible with ansible



#### Sources

* [Getting Started with Ansible for Network Automation](https://docs.ansible.com/ansible/latest/network/getting_started/index.html#network-getting-started)
