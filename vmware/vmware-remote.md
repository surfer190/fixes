# VMWare Tools for Remote Access

## VDI (Virtual Desktop) vs Terminal Server

First let understand the difference between terminal server and virtual desktop remote access.

### VDI (Virtual Desktop Infrasturcture)

* No local pc required
* custom version of software per user
* designed for multimedia and desktop functionality
* local atttached storage is available on the remote desktop
* resources are individual to the user

### TS (Terminal Server)

* local pc is required
* all users share the same software
* all resources are shared
* struggles with multimedia - graphics and audio

## VmWare Remote Access Options

* VMware Workstation
* Mware Remote Console (VMRC)
* VMWare Horizon


### VMware Remote Console (VMRC)

* Standalone windows, mac and linux application. It provides console access to the vm on a remote.
* You can only launch VMware Remote Console (VMRC) from within the web client - "Launch Remote Access"
* VMRC is supported by all vSphere 5.1 and ESX configurations, and by all vCloud Director 5.1 configurations.


#### Using VMRC in VCloud Director

According to the [vcloud direcctor vmrc docs](https://docs.vmware.com/en/VMware-Cloud-Director/9.1/com.vmware.vcloud.tenantportal.doc/GUID-860CFD1A-2B80-4E90-95F5-1D3E1FB6B47A.html)

You log into the tenant portal, select `Action` then select `Launch VM Remote Console`

#### Accessing VMRC via the API

Docs on [accessing vmrc via the api](https://code.vmware.com/docs/143/vmware-remote-console--vmrc--sdk)



### VMWare Horizon

* A tool to create a virtual desktop infrastructure and uses the vSphere for hosting virtual desktops
* All data lives in the data center, not on the endpoint, there are significant security benefits of VDI
* Easier to scale





### Sources

* [The VM Remote Console changed to VMware Workstation instead of VMRC](https://be-virtual.net/the-vm-remote-console-changed-to-vmware-workstation-instead-of-vmrc/)
* [What is VMware Remote Console and how do you run it?](https://searchvmware.techtarget.com/answer/What-is-VMware-Remote-Console-and-how-do-you-run-it)
* [VMware Horizon Architecture and how it differs from VDI](https://www.vembu.com/blog/know-difference-vmware-horizon-virtual-desktop-infrastructure/)