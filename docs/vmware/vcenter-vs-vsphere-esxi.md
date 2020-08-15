---
author: ''
category: Vmware
date: '2020-06-14'
summary: ''
title: Vcenter Vs Vsphere Esxi
---
## What is the difference between VCenter and VSphere ESXI?

### VMWare Vsphere Esxi

* Installed on bare metal like an operating system
* Type 1 hypervisor - purely for running virtual machines
* Basic creation of VM's and networking
* vSphere management interface provides access (web based)
* No GUI - when physical machine boots
* Can only manage a single host at a time
* Good if you aren't worried about backups and high availability


### VCenter

* Deployed as a virtual machine on top of an esxi host - vcenter server appliance
* Manage many esxi hosts at a time
* Flash and HTML management interface
* Advanced features: vm cloning, HA, fault tolerance
* fluid movement between hosts
* Automatically picks up underlying info and vms in esxi hosts
* `vMotion` is movement from one host to another
* Create templates for fast provisioning
* `DRS` - distributed resource scheduling (creates on host with least resources)
* distributed vswitches


> Basically when you want to scale up and provide more high availability and other services use vCenter





Minimum specs:

* 2 CPU Cores
* 4GB RAM
* 64-bit




### Source

* [What is VMware vSphere ESXi and vCenter?](https://www.youtube.com/watch?v=-Hltydu9PXk)