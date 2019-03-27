## The VMWare vSphere Rest API

There are physical ESXI nodes (bare metal hypervisors) where a VCSA (vCenter Server Appliance) sites on top of aggregating their resources.

Every ESXI node has a SOAP endpoint - for management and monitoring

There is a SOAP API endpoing on the vCenter Server allowing you to manage clusters and reporting

vSphere 6.0 introduced a REST API endpoint which was limited.
It also has a CIM API for system analytics

The vSphere Management SDK's were in Perl and Java.
Eventually the vmware team realeased open source SDK's for other languages:
* python (pyvmomi)
* ruby (rbvmomi)
* go (govmomi)

vSphere automation SDK's use the REST API were brought in with various languages

There is also the vRealise Orchestrator, PowerCLI, vCLI which talk to all the API's

So together all the ways to speak to vCenter is:
* vSphere Management SDKS (Perl, .net, Java) - Talks to Web Service API (SOAP)
* Open Source SDK's (pyvmomi, rbvmomi, govmomi) - Talks to the Web Service API (SOAP)
* vSphere Automation SDK (Perl, .Net, Java, Ruby, Python) - Talks to the REST API
* Automation operation Interfaces (PowerCLI, vCLI and vRealiseOrchestrator) - Talks to SOAP, REST and CIM API

More on the [CIM API](https://code.vmware.com/apis/207/cim)

> The SOAP API's could do pretty much everything

They were hard to use and the learning curve was steep - that is the reason for creating the Rest API

> The SOAP API is rock solid, ton of people are using it

## What can you do through the REST API

* Appliance Access
* Appliance User Accounts
* Check Application Health (Load, Memory, CPU, Storage)
* Monitoring
* Configure networking
    * Hostname
    * DNS
    * Network Interfaces
    * Firewall Rules
    * Routes
* Perform Backup and Recovery
* Configure System Settings
    * List and Resize Storage
    * NTP and Timesync
    * View System version and uptime
    * SNMP settings
    * Shutdown and Reboot
    * Update

## VM Management

* VM - Create, Get, List, Delete
* Power - Get, Start, Stop, Suspend, Reset
* Hardware - Get, Update, Upgrade

## API Explorere

On your vCenter instance fo to `/apiexplorer` that shows a swagger UI.

The API's:
* `appliance` - Won't show on windows
* `cis` - tagging
* `content` - content library
* `vapi` - talk to vapi - services, status
* `vcenter`

## VMWare Code API's

To view all the [VmWare API's available](https://code.vmware.com/apis/)








[Notes from the talk by KMRuddy on the vSphere API 6.5](https://www.youtube.com/watch?v=nr3pJovtbzM)