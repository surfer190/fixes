---
author: ''
category: Ansible
date: '2015-09-20'
summary: ''
title: Ansible Local Inrastructure
---
# ansible locally

`Test-driven development` has given rise to `infrastructure testing`, so testing locally before going into live environments.

Which inherently creates documented and reversable infrastructure

### Tools

Vagrant - Server Priovisioning Tool
Virtualbox - A local virtualization environement

### Setting up Vagrant

Download [vagrant](http://www.vagrantup.com/downloads.html)

Download [virtualbox](https://www.virtualbox.org/wiki/Downloads)

Add a box From [Hashicorp atlas](https://atlas.hashicorp.com/boxes/search)

### Adding and Initializing

```
#Box management: add
vagrant box add <box_name> <box_url>

#Initializes new vagrant environments using VagrantFile
vagrant init <box_name>

#Booot up the Server
vagrant up
```
### Basic Vagrant Commands

`vagrant halt` : shut down the VM

`vagrant up` : bring back up

`vagrant ssh`: ssh into box

`vagrant ssh-coonfig`: get required SSH details

`vagrant destroy`: completely delete the machine from virtualbox

### Setting Ansible as the Provisioner

In `VagrantFile`:

```
# Provisioning configuration for Ansible.
config.vm.provision "ansible" do |ansible|
ansible.playbook = "playbook.yml"
end
```
