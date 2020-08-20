---
author: ''
category: Network-Automation
date: '2020-05-28'
summary: ''
title: Sdn Nfv Openflow Whitebox Switching
---
## SDN, Openflow, NFV and Whitebox Switching

## Terminology

### Software Defined Networking (SDN)

Many definitions - the main thing is programmability and automation

* Physical seperation of network control plane from the forwarding plane - where the control plane controls several devices
* Connects application layer -> controler layer -> infrastucture layer 
* Open flow controller: ODL (Open daylight), Rewho and Onos
* Openflow, NETCONF, BGP-LS, SNMP are protocols

Vmware Nsx is an overlay SDN implementation - or network virtualisation implementation. A virtual network overlayed over a physical network.

SD-WAN: make better use of the internet - instead of sending traffic across an MPLS network we send some traffic over the internet from a centralised controller.

### NBI - North bound interface

Interface or API between the application and the control layer. A higher level interface.

### SBI - South bound interface 

Interface between the control layer and network devices - openflow, etc.
Often details of the southbound interface are abstracted - the way actions of the northbound are implemented isn't the concern.
