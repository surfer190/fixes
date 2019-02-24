# Notes on the Oreilly book Network Programmability and Automation

## What is Network Automation?

* **Simplifying** tasks involved in configuring, managing and operating network equipment, network topologies, network services and network connectivity.
* Continuous Integration
* Configuration management
* Source code control

## Benefits of Reading this book

* Network Engineers -  fluent in network protocols, configuring network devices, operating and managing a network
* System Administrators - responsible for managing systems that conenct to the network
* Software Developers - Useful to see developer tools and lanugages in a networking context

# 1. Network Industry Trends

## The Rise of Software Defined Netoworks

Martin Casado - influencing large network incumbents that operations, agility and managability must change

### Openflow

* First major protocol for software defined networks
* Decoupled network device's control plane (brain's of device) from the data plane (hardware doing the packet forwarding)
* Hybrid mode - deployed on a given port, VLAN or a normal paket forwarding pipeline
* Low level and directly interfaces with hardware tables instructing how a network device should forward traffic
* Not intended to interact with the management plane - like authentication or SNMP
* Policy Based routing - forward traffic based on non-traditional attributes, like a packet's source address.
* Achieve same ganularity of packet forwarding but in a vendor-neutral way

#### Why Openflow?

* Network devices were closed (locked from installing third-party software) and only had a CLI
* CLI's although well known and even preferred by administrators - it did not offer the flexibility to manage, operate and secure a network
* The biggest change in the last 20 years is a move from telnet to SSH
* Management of networks has lagged behind other technology comparitively for both configuration management and data gathering and analysis
    * hypervisor managers, wireless controllers, IP PBX's, Powershell and DevOps Tools
* Question's openflow was based around:
    * Was it possible to redirect traffic based on the application
    * Did network devices have an API?
    * Was there a single point of communication to the network?

### What is Software Defined Networking (SDN)?

* SDN is similar to what cloud was a decade ago: IaaS, PaaS and SaaS.
* The definition is kind of up in the air
* Things in SDN:
    * Openflow
    * Network Functions Virtualisation
    * Virtual switching
    * Device API's
    * Network Automation
    * Bare-metal switching
    * Data centre network fabrics
    * SD-WAN
    * Controller Networking

#### OpenFlow

* Vendor independence from controller software - a NOS (Network Operating System)
* Vendors who use openflow (Big Switch Netowrks, HP, NEC) have developed extensions
* The use of openflow or any other protocol is less important than the business being supported

#### Network Functions Virtualisation (NFV)

* Deploying traditionally hardware functions as software
* Most common example is virtual machines that operate routers, firewalls, load balancers, IDS/IPS, VPN, application firewalls etc.
* Helps to issue of having to deploy expensive hardware to future proof and reducing complexity for future upgrades. 
* A software based NFV lets you pay as you grow and minimises the failure domain
* For example deploy many Cisco ASAv applicances instead of a single large Cisco ASA.
* Time needed to rack, stack, cable and integrate hardware is eliminated, it becomes as fast as deploying a virtual machine and an inherent advantage is being able to clone and backup environments.

Why hasn't NFV taken over:
* Requires a rethink on how the network is operated - for example a single big firewall as oppsed to many multi-tenant firewalls
* Or a single CLI or GUI, making the failure domain immense but streamlines tha administration.
* In modern network automation, it matters less what architecture is chosen as management of devices is becoming easier
* Vendors are delibrately limiting the performance of their virtual application-based technology

#### Virtual Switching

Common virtual switches:
* VMWare standard switch (VSS)
* VMWare distributed switch (VDS)
* Cisco Nexus 1000V
* Cisco Application Virtual Switch (AVS)
* Open vSwitch (OVS)

Software based switches that reside in the hypervisor kernel providing local network connectivity between virtual machines and containers.

Features:
* MAC Learning
* link aggregation
* SPAN
* sFlow

New access layer or edge within a datacentre. It is no longer the physical TOR (top-of-rack) switch
with limited flexibility

Makes it easier to distribute policy throughout the network

#### Network Virtualisation

Software-only overlay-based solutions

solutions:
* VMWare's NSX
* Nuage's Virtual Service Platform (VSP)
* Juniper's Contrail

An overlay based solution like Virtual Extensible LAN (VxLAN) is used to build connectivity between hypervisor based virtual switches.

> This connectivity and tunneling approach provides Layer 2 adjacency between virtual machines that exist on different physical hosts independent of the physical network, meaning the physical network could be Layer 2, Layer 3, or a combination of both.

The result is a virtual network that is decoupled from the physical network and that is meant to provide choice and agility.

* more than just virtual switches being stitched together by overlays
* comprehensive, offering security, load balancing, and integrations back into the physical network all with a single point of management
* offer integrations with the best-of-breed Layer 4–7 services companies
* No need to configure virtual switches manually, as each solution simplifies this process by providing a central GUI, CLI, and also an API where changes can be made programmatically

#### Device API's

* Vendors realised that using a CLI has severely held back operations
* Main issue is scripting does not return structured data - it is returned in raw text that had to be parsed
* If the output of `show` commands changed slightly the scripts would break
* Strucuted data returned eliminates the need to parse the text giving a cleaner interface to develop and test code

> `Test code` could mean testing new topologies, certifying new network features, validating particular network configurations, and more

The most popular API is by `Arista Networks` called `eAPI` - a JSON over HTTP Api.
`Cisco` brought out the `Nexus NX-API` and `NETCONF/RESTCONF`

> Nearly every vendor has some sort of API these days

#### Network Automation

Not just about automating the configuration of network devices but also acessing data in network devices:
* Flow level data
* routing tables
* FIB tables
* Interface statistics
* MAC tables
* VLAN tables
* serial numbers

Time to debug and troubleshoot is reduced

Streamlines the process of every network admin having their own bet practices

#### Bare Metal Switching

This is not SDN (Software defined Networking)

Network devices were always bought as a physical device - as hardware appliances, an operating system and features you can use on the system - all from the same vendor.

With white-box or bare metal network devices the device looks more like a x86 server - allowing you to pick and choose the vendor you want to use.

Companies solely focused on white box switching - software:
* Big Switch Networks
* Cumulus Networks
* Pica8

Whitebox hardware platforms:
* Quanta
* Super Micro
* Accton

In a bare metal device components: application, operating system and hardware and disaggregated

If there is a controller integrated with the solution using a protocol such as OpenFlow and is programmatically communcating with network devices that gives it a Software Defined Networking flavour.

If there is no controller requirements then it makes it a non-SDN based architecture

In short whitebox and baremetal switching gives flexibility to change designs, architecture and software without swapping hardware just changing the operating system

#### Data Centre Network Fabrics

Changes the mindset of network operators from managing individual boxes one at a time to managing the system in its entirety.
An upgrade is a migration from system to system, or fabric to fabric.

Examples:
* Cisco's Application Centric Infrastructure (ACI)
* Big Switch's Big Cloud Fabric (BCF)
* Plexxi's Fabric and Hyperconverged network

Attributes of data centre networking fabrics:
* A single interface to manage or configure the fabric - including policy management
* Distributed default gateways across the fabric
* Multi-pathing capabilities
* They use some form of SDN controller

#### SD-WAN

Software Defined Wide Area Networking

Vendors:
* Viptela
* CloudGenix
* VeloCloud
* Cisco IWAN
* Glue Networks
* Silverpeak

Offers more choice

#### Controller Networking

A characteristic to deliver modern solutions

OpenDayLight - popular SDN controlller - it is a platform not a product.
Can be used for network monitoring, visibility, tap aggregation etc. beyond fabrics, network virtualisatoin and SD-WAN

# 2. Network Automation

## Why Network Automation?

* Speed
* Simplified Artchitectures
* Deterministic Outcomes
* Business Agility

### Simplified Artictures

Most network devices are uniquely configured (as snowflakes) and network engineers take pride in solving transport and application issues with one off changes - is makes the network harder to maintain, manage and automate.

Network automation needs to be included from the outset of new architectures (not just an add-on)

Archiecture becomes simpler, repeatable, easier to maintain and automate.

> Still necessary to eliminate one-off changes

### Deterministic Outcomes

* The impact of typing the wrong command can be catastrophic
* Each engineer has their own way of making a particular change
* Using proven and tested network automation makes changes more predicatable

### Business Agility

Always understand existing manual workflows, document them and understand the impact they have to the business
Then deploying automation chnology and tooling becomes much simpler

## Types of Network Automation

### Device Provisioning

* Fastest way to get started is to automate the creatoin of device configuration files for initial device provisioning and push them to network devices
* Decouple the inputs from the vendor-proprietary syntax
* A seperate file for values of configuration parameters - a configuration template

### Data Collection

* Monitoring tools typically use the SNMP (Simple Network Management Protocol)
* Newer devices use a push model which streams telemetry to a server of your choosing

### Migrations

> The beautiful thing is that a migration tool such as this is much simpler to build on your own than have a vendor do it because the vendor needs to account for all features the device supports as compared to an individual organization that only needs a finite number of features. In reality, this is something vendors don’t care much about; they are concerned with their equipment, not making it easier for you, the network operator, to manage a multi-vendor environment.

> Only you, not the large networking vendors, have the motivation to make multi-vendor automation a reality.

It is important to think about the tasks and document them in human readable format that is vendor neutral

### Configuration Management

* Deploying, pushing and managing configuration state of a device

The great power comes with great responsibility - tests must always be performed before rolling out to production environments

### Compliance

It is easier to start with data collection, monitoring and configuration building which are _read only_ and _low risk_ actions

**A low risk use case is configuration compliance checks and configuration validations**

* Does it meet security requirements?
* Are the required networks configured?
* Is protocol XYZ disabled?

What happens when it fails compliance - is it logged, is anyone notified, does the system autocorrect?
Event-driven automation

It is always best to start simple with automation

### Reporting

* Custom and Dynamic Reports
* Data being returned becomes input to other configuration management tasks
* Reports can be produced in any format

## Troubleshooting

* Automated troubleshooting becmoing a reality
* Troubleshooting interrupts learning and improving work

The trick is how troubleshooting is done:
* Do you have a personal methodology?
* Is the method consistent with al members of the team?
* Does everyone check Layer 2 before troubleshooting Layer 3?
* What steps are taken?

Eg. Troubleshooting OSPF (A routing protocol used to connect with other routers)
* What does it take to form an OSPF adjecency between 2 devices?
* Can you say the same answer at 2 in the morning?
* Do you rmember that some devices need to be on the same subnet, have the same MTU and have consistent times and same OSPF network type?

Other examples:
* Can particular log messages correlate to known conditions on the network?
* BGP neightbour adjacencies, how is a neighbour formed?
* Are you seeing all the routes you think should be in the routing table?
* What about VPC and MLAG configurations?
* What about port-channels? Are there any inconsistencies?
* Do neighbours match the port-channel configuratoin (going down to the vSwitch)?
* Cabling - are cables plugged in correctly?

## Evolving the Management PLane from SNMP to Device API's

### API's (Application Programming Interfaces)

#### SNMP

* A protocol used to poll network devices for information about status, CPU, memory and interface utilisation
* There must be an SNMP agent on a managed device and a network managment station (NMS) - which acts as the server for managed devices.
* This SNMP data is described and modelled in MIB (Management Information bases)
* SNMP supports both Get Requests and Set Requests (PATCH/POST)
* Not many vendors offer full support for the configuration management via SNMP - they often used custom MIB's
* Some vendors are claiming the gradual death of SNMP - although it does exist on nearly every network device
* There are python libraries for SNMP

#### SSH/Telnet and the CLI

* The CLI was built for humans - not meant for machine-to-machine comms
* Raw text returned from a `show` command is not formatted or structured
* SSH/CLI makes automation extremely error prone and tedious

#### NETCONF

* A network management layer protocol - like SNMP to retrieve and change configuration
* Leverages SSH
* Data sent between a NETCONF client and NETCONF server is encoded in XML
* RPC's (Remote Procedure Calls) are encoded in the XML document using the `<rpc>` element
* RPC's map directly to NETCONF operations and capabilities on the device
* Supports transaction based exchanges - if any single change fails everything is rolled back

#### Restful API's

* Representational State Transfer
* Network controllers
* The web server is the network device or SDN controller
* You then send requests to that server with a client

### Impact of Open Networking

All things open:
* Open source
* Open networking
* Open API's
* OpenFlow
* Open Computer
* Open vSwitch
* OpenDaylight
* OpenConfig

* It improves consistency and automation
* Many devices support python on-box
* Meaning you can go into the python interpreter and run python scripts locally on the device
* More robust API's are supported (Netconf and REST instead of SNMP and SSH)
* Network devices are exposing more of the Linux Internals - use `ifconfig`, `apt` or `yum`

Network device API's that exist now that didn;t a few years ago:
* Cisco NX-API
* Arista eAPI
* Cisco IOS-XE
* RESTCONF/NETCONF

### Network Automatino in the SDN Era

* Even with controllers network automation is imortant
* Cisco, Juniper, VmWare, Big Switch, Plexxi, Nuage, Viptela offer controller platforms. Not to mention OpenDaylight and OpenContrail
* Important to avoid making error-prone changues with the GUI

# 3. Linux












## Source

* Network Programmability and Automation - Jason Edelman, Scott S. Lowe, Matt Oswalt