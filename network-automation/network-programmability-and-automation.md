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

## Linux in the Network Automation Context

* Several network operating systems are based on Linux
* Some are bringing full Linux distributions targeted at network equipment
* Open Network Linux - Big Switch's Switch Light is an example built on Open Network Linux
* Many tools have origins in Linux
* You will often use anisble from a computer using Linux

## Brief History of Linux

* 1980's Richard Stallman launched the GNU Project to provide a free Unix-like operating system - GNU
* A wide collection of Unix utilities and applications were created but the kernel "GNU Hurd" never gained momentum
* Linus Torvald tried to create a MINIX clone in 1991 - the start of Linux
* GNU/Linux is the OS utilities and the kernel

## Linux Distributions

### Red Hat, Defora and CentOS

* Red Hat offered Red Hat Enterprise Linux (RHEL) along with technical support
* The fast pace of Linux development is often at odds with slowed and more methodical pace required for stability and reliability by the Red Hat paltform
* Fedora is the upstream distribution of RHEL - so Fedora has all the stuff new
* To avoid the RHEL costs, an open source clone was made called CentOS (Community Enterprise Linux)
* These distributions share a common _package format_ - RPM

Many distributions replaced the `rpm` package manager with `yum` (Yellowdog updater) and are now moving to a tool called `dnf` (Dandified YUM)

Other distributions also use the RPM format: `Oracle Linux`, `Scientific Linux` and `Suse derivatives`

### Debian, Ubuntu and others

* Debian GNU/Linux is a distribution produced and maintained by the Debian project
* Founded in 1993 by Ian Murdock
* Three branchesL stable, testing and unstable
* Ubuntu Linux started in 2004 - funded by canonical by Mark Shuttleworth
* Has desktop, server and mobile focused versions
* Stick to LTS (Long term support) releases for best practice
* They use teh `.deb` package and use the `dpkg` tool
* Recently `apt`, `apt-get` and `aptitude` are used

## Interacting with Linux

* Receive IP addresses via a Linux based DHCP server
* Access a linux powered web server like apache
* Utilise DNS to resolve domain names to IP addresses
* The most common shell is `bash` - bourne again shell

### Navigating the File System

* A single-root filessytem - all drives and directories fall into a single namespace
* Linux treats everything as a file - even storage devices, ports, IO
* Every file has a unique path to its location


`ping` is found in `/bin/ping`

`arp` is found in `/usr/sbin/arp`

`~` is a shortcut to a user's home directory

The prompt: `ubuntu@backup:~$`

Denotes ubuntu user on the jessie hostname currently in the home directory.
The `$` at the end means that the currect user does not have root permissions

* `pwd` - print working directory - prints the full path of the directory you are in
* `cd x` - change directory. A leading slash indicated from teh root, otherwise it is relative to the current location. Use `cd ..` to move up one directory in the hierachy.
* `.` - the currect directory

> Top tip: `cd -` tells bash to switch back to the last directory you were.

> Top tip: `cd` shortcuts to the home directory

The _search path_ are places linux automatically searches when you type a command. Typical locations inlcude `/bin`, `/usr/bin` and `/sbin`. Being specific about which file to run using the absolute path `./myfile.sh` is important.

### Manipulating Files and Directories

* `touch x` - create files
* `mkdir x` - make directory
* `rm x` - remove a file
* `rm -R x` - remove a directory
* `cp x y` - copy file
* `cp -R x y` - copy a directory

> There is no recycle bin or trash can. Be vary careful with `rm`, `cp` and `mv`. Overwritten files are gone.

> You can always get your own help using man pages: eg. `man cp`

### Permissions

* permissions are assigned based on the user, group and others
* permissions are based on action (read, write, execute)

Each action has a value:
* `4` is read
* `2` is write
* `1` is execture

To allow for multiple actions add the underlying values

The values are assigned to user, group and others.

* `644`: user read and write, group read, others read
* `755`: user read, write and execute; group read and execute; others read and execute
* `620`: user read and write, group write, others none

A line like `rxwr-xr-x` breaks down `read`, `write` and `execute` into `user`, `group` and `other`

* `ls -l` - view files and permissions in a directory
* `chmod` - change permissions
* `chown` - change ownership of a file

Eg:

    chmod 755 bin # sets bin directory to 755
    chmod u+rw config.txt # adds read and write permission to the user that owns the file
    chmod u+rw, g-w /opt/share/config.txt # adds read and write for the user, remove write for the group

### Running Programs

What makes an executable file? It could be binary, compiled from C or C++
It could also be an executable text file, such as a bash shell script or a python script

The `file` utility can help to tell you what file of file it is

    ubuntu@backup:~$ file backup.log 
    backup.log: UTF-8 Unicode text
    ubuntu@backup:~$ file remove_old.sh 
    remove_old.sh: Bourne-Again shell script, ASCII text executable

> The shebang - the first line in a text-based script and starts with `!followed by the path to the interpreter`. Eg. `!/usr/bin/python` - tells bash which program to use

You can view your _search path_ with:

    echo $PATH
    
> The search path is controlled by the environment variable: `PATH`

To find where to absolute path to an executable is:

    which uptime

### Working with Daemons

* In the linux world the term `daemon` refers to a process that runs in the background. Also sometimes called a `service`
* Daemons are most often encountered when dealing with network related services
* Working with daemons used to vary depending on the distribution
* Startup scripts callen `init scripts` were used to start, stop and restart a daemon.

On some systems the `service` utility is used - behind the scenes this utility is calling distributino specific command - `initctl` on ubuntu and `systemctl` on centOS

In recent years major linux distro's have converged on the use of `systemd` as teh init system.

Prior to debian 8, it used `System V init`

#### Working with Daemons on Debian 8

* Using the `systemctl` utility
* Debian does not provide a user friendly wrapper

Start a service:

    systemctl start service-name
    
Stop a service:

    systemctl stop service-name

Restart:

    systemctl restart service-name

Reload (config) - less disruptive than restarting:

    systemctl reload service-name

View status of daemon:

    systemctl status service-name

View all the services:

    systemctl list-units

#### On Ubuntu

Similar to the above except using `initctl`

#### Background services on CentOS 7.1

* Same as debian core `systemctl` commands
* `centOS` includes the `service` wrapper script

#### Other daemon-related commands

Show the network connections to a daemon, use `ss`. To **show listening network sockets** to ensure that **network configuration is working properly**

    ss -lnt # tcp sockets
    ss -lnu # udp sockets

Information about currently running proccesses:

    ps
    
## Networking in Linux

### Working with Interfaces

* Physical interfaces
* VLAN interfaces
* Bridge interfaces

Configured using the CLI or config files

#### Interface configuration via command line

Most linux distributions have configured on a single set of command line utilities for working with network interfaces

Part of the `iproute2` set of utilities (On centos it is known as `iproute`)
These utilities use `ip` to replace the functionality of the deprecated `ifconfig` and `route`

For interface config 2 sub commands to the `ip` command will be used:
* `ip link` - view or set interface link status`
* `ip addr` - view or set ip addressing configuration on interfaces

Listing interfaces:

    ip link list
    ip addr
    id link

Eg.

    stephen@web:~$ ip addr
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host 
        valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 04:01:29:7e:44:01 brd ff:ff:ff:ff:ff:ff
        inet 37.139.28.74/24 brd 37.139.28.255 scope global eth0
        valid_lft forever preferred_lft forever
        inet6 fe80::601:29ff:fe7e:4401/64 scope link 
        valid_lft forever preferred_lft forever
        
Output shows:
* the current list of interfaces
* the current maximum transmission unit (MTU)
* the current administrative state (UP)
* ethernet media access control (MAC) address

The `status` in the angled brackets `<>` can be:
* `UP` - Indicates the interface is enabled
* `LOWER_UP` - Indiciates the interface link is up
* `NO_CARRIER` - The interface is enabled but there is no link (THe interface is "down")
* `DOWN` - THe interface is administratively down

To filter for a specific interface:

    ip link list interface
    
eg.

    stephen@web:~$ ip link list eth0
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 04:01:29:7e:44:01 brd ff:ff:ff:ff:ff:ff
    
> Listing is the default. Ie. `ip route` will list all the routes

> CentOS assigns different names to the interfaces than Debian and Ubuntu

Disabling an interface:

    ip link set <interface> down

    [vagrant@centos ~]$ ip link set ens33 down
    [vagrant@centos ~]$ ip link list ens33
    3: ens33: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT
        qlen 1000
        link/ether 00:0c:29:d7:28:21 brd ff:ff:ff:ff:ff:ff
    
The `state DOWN` and lack of `NO_CARRIER`, tells you the interface is administratively down and not just down used to a link failure

Enabling an interface

    ip link set <interface> up

Eg.

    [vagrant@centos ~]$ ip link set ens33 down
    [vagrant@centos ~]$ ip link list ens33
    3: ens33: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT
    qlen 1000
    link/ether 00:0c:29:d7:28:21 brd ff:ff:ff:ff:ff:ff

Setting the MTU of an interface

    ip link set mtu <number> <interface>

Eg.

    [vagrant@centos ~]$ ip link set mtu 9000 ens33
    
> This change is immediate but not persistent

Assigning an IP address to an interface

    ip addr add address dev interface

Eg.

    vagrant@jessie:~$ ip addr add 172.31.254.100/24 dev eth1

> If an interface already has an IP address assigned, the ip addr add command simply adds the new address, leaving the original address intact.

Remove an ip address:

    ip addr del address dev interface

    vagrant@jessie:~$ ip addr del 172.31.254.100/24 dev eth1

> We have been modifying the running configuration we haven’t made these configuration changes permanent. In other words, we haven’t changed the startup configuration. To do that, we’ll need to look at how Linux uses interface configuration files.

#### Interface configuration via configuration files

> interface configuration files across different Linux distributions can be quite different

On RHEL, CentOS and Fedora configuration filess are found at: `/etc/sysconfig/network-scripts`

The configuration files are named: `ifcfg-<interface>`

An example may look like this:

    NAME="ens33"
    DEVICE="ens33"
    ONBOOT=yes
    NETBOOT=yes
    IPV6INIT=yes
    BOOTPROTO=dhcp
    TYPE=Ethernet

* NAME: A friendly name for users
* DEVICE: Name of physical device being configured
* IPADDR: Ip address to be assigned (if not using DHCP or BootP)
* PREFIX: Network prefix for the assigned IP addres (an use `NETMASK`)
* BOOTPROTO: How the ip address will be assigned, a value of `dhcp` can be used. `none` means statically defined.
* ONBOOT: `yes` will activate the device at boot time. Setting `no` will not.
* MTU: Specifies default MTU for the interface
* GATEWAY: Specifies gateway to be used

For full detauls you can check: `/usr/share/doc/initscripts-<version>/sysconfig.txt` on a CentOS system.

On debian and derivatives, interface configuration is handled at `/etc/network/interfaces`

We can use `cat` to show the contents on the screen:

    cat /etc/network/interfaces
    
Eg.

    stephen@web:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).

    # The loopback network interface
    auto lo
    iface lo inet loopback

    # The primary network interface
    auto eth0
    iface eth0 inet static
            address 37.139.28.74
            netmask 255.255.255.0
            gateway 37.139.28.1
            dns-nameservers 8.8.4.4 8.8.8.8 209.244.0.3

> Debian and Ubuntu use a single file to configure all the network interfaces

For more info run: `man 5 interfaces`

You can also break configuration into seperate files with:

    source /etc/network/interfaces.d/*
    
Per interface configuration files give additional flexibility when using Chef, Puppet, Ansible or Salt

To put the configuration changes into effect you need to restart the network interface

Restarting the network interface:
* ubuntu: `initctl restart network-interface INTERFACE=interface`
* CentOS: `systemctl restart network`
* Debian: `systemctl restart networking`

> The same way linux treats many things as files, lnux treats many things as interfaces. 

### Using VLANS

The interface is the basic building block of Linux Networking

> VLAN interfaces are logical interfaces that allow an instance of Linux to communicate on multiple virtual local area networks (VLANs) simultaneously without having to have a dedicated physical interface for each VLAN

Create a VLAN (an extension of the `ip link` command):

    ip link add link parent-device vlan-device type vlan id vlan-id

* `parent-device` - physical adapter the logical VLAN interface is associated eg. `eth1`
* `vlan-device` - name to be given to the logical VLAN interface (`name of the parent device`, `a dot` and then the `VLAN ID` eg. `eth1.100`
* `vlan-id` - the 802.1Q VLAN ID value assigned to this logical interface

eg. This logical interface is to be associated with the physical interface named eth2 and should use 802.1Q VLAN ID 150

    vagrant@jessie:~$ ip link add link eth2 eth2.150 type vlan id 150

 Verify that the logical VLAN interface was added using `ip link list`.
 To verify (aside from the name) that the interface is a VLAN interface, add the `-d` parameter
 
    vagrant@jessie:~$ ip -d link list eth2.150
    7: eth2.150@eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noqueue state DOWN
       mode DEFAULT group default
       link/ether 00:0c:29:5f:d2:15 brd ff:ff:ff:ff:ff:ff
       vlan protocol 802.1Q id 150 <REORDER_HDR>

Finally the VLAN must be enabled:

    ip link set eth2.150 up
    ip addr add 192.168.150.10/24 dev eth2.150

> Just like physical interfaces, a logical VLAN interface that is enabled and has an IP address assigned will add a route to the host’s routing table

    vagrant@jessie:~$ ip route list
    default via 192.168.70.2 dev eth0
    192.168.70.0/24 dev eth0  proto kernel  scope link  src 192.168.70.243
    192.168.100.0/24 dev eth1  proto kernel  scope link  src 192.168.100.10
    192.168.150.0/24 dev eth2.150  proto kernel  scope link  src 192.168.150.10

To delete a VLAN interface

First disable the interface then remove the interface:

    vagrant@jessie:~$ ip link set eth2.150 down
    vagrant@jessie:~$ ip link delete eth2.150

> VLAN interfaces will be tremendously useful anytime you have a Linux host that needs to communicate on multiple VLANs at the same time and you wish to minimize the number of switch ports and physical interfaces required

### Routing as an End Host

A whole lot more stuff...

# 4. Learning Python in a Network Context

The network industry is fundamentally changing, there has never been a better time to learn to automate and write code

> Things are starting to move in the right direction and the barrier to entry for network automation is more accessible than ever before

* network device APIs
* vendor- and community-supported Python libraries
* freely available open source tools

Meaning less code, faster development and fewer bugs

### Why Python?

* Dynamically typed - create and use variables where needed where and when needed, no need to specify the data type.
* It reads like a book
* Many open source libraries and projects

## Python

In the book, the essentials of working with python is looked at.
Most of this will be common to you if you have read any python tutorials or books.

One topic I needed a refresher on was: Passing Arguments to a Python Script

### Passing Arguments to a Python Script

There is a module in python's standard library to pass arguments from the command line into a python script.
The module is called `sys`.
Specifically we are using an attribute of the module called `argv`.

    $ python send-command.py 
    ['send-command.py']

`sys.argv` is a list of strings passed in from the Linux command line.

Contents of `send-command.py`:

    #!/usr/bin/env python
    import sys
    if __name__ == '__main__':
        print(sys.argv)

Using `argv` we need to implement error handling. Additionally the user needs to know the precise order of inputs.

> Python's `argparse` module provides a way for user's to enter arguments with flags.

### Tips and Tricks

You should read through the tips and tricks available to you

One good one was `python -i send-command.py`. Which runs the script but then lets you interact with variable.
Although `import pdb; pdb.set_trace()` was not discussed.

# 5. Data Formats and Data Models

> In the same way that routers and switches require standardized protocols in order to communicate, applications need to be able to agree on some kind of syntax in order to exchange data between them...for this standard data formats are used like XML and JSON

Data models define how data in a format is structured

> The goal of this chapter is to help you understand the value of standardized and simplified formats

XML: Not easy on the eye, but programmatically it is perfect

## Types of Data

* String - sequence of letter, numbers and symbols
* Integer - a whole number (positive or negative)
* Boolean - True or False
* Advanced Data Structures - array, list, dicitonary.

## YAML

* Human Friendly
* Represents data similar to XML and JSON but in a human readable way

Example: Represent a list of network vendors

    ---
    - Cisco
    - Juniper
    - Brocade
    - VMware

The `---` at the top is a `.yml` convention indicating that the file is `yaml`.

In yaml you usually don't need single quotes or double quotes to indicate a string.
It is usually automatically discovered by the YAML parser (`PyYaml`)

Each item having a `-` in front of it. Meaning it is a list of 4 elements (as they do not have any under it)

YAML very closely mimics python data structures. A good example is mixing data types in a list:

    ---
    - CoreSwitch
    - 7700
    - False
    - ['switchport', 'mode', 'access']

In this example the the first item in the list is a string, the second is an integer, the third is a boolean and the fourth is a list.
The first nested data structure!

Enclosing the `7700` in quotes: `"7700"` helps the parser figure out the data type. It is important to also enclose in quotes if the string contains a yaml special character like a `:`

Key value pairs:

    ---
    Juniper: Also a plant
    Cisco: 6500
    Brocade: True
    VMware:
      - esxi
      - vcenter
      - nsx

`Keys` are the short strings to the left of the colons, the `value` is on the right.

YAML dictionaries can also be written in python like ways:

    ---
    {Juniper: Also a plant, Cisco: 6500, Brocase: True, VMware: ['esxi', 'vcenter', 'nsx']}

Most parsers will see the above 2 as the same, yer the first one is much more readable

If you want it more human readable, use the more verbose options.
With an API reabability is irrelevant so JSON or XML is preferred.

**Comments**

A `#` hash sign indicates a comment

    ---
    - Cisco    # ocsiC
    - Juniper  # repinuJ
    - Brocade  # edacorB
    - VMware   # erawMV

#### Reading Yaml with python

Install `pyyaml`:

    pip install pyyaml

For example we create a file with the previous yaml content: `example.yml`:

    import yaml

    with open('example.yml', 'r') as file_:
        result = yaml.load(file_)
        print(result)
        print(type(result))
        
The output will be:

    {'Juniper': 'Also a plant', 'Cisco': 6500, 'Brocase': True, 'VMWare': ['esxi', 'vcenter', 'nsx']}
    <class 'dict'>

> The `with` part is a contezt manager, that ensures the file is closed after use and it only available for the part of the program you need to use it for

#### Data Models in Yaml

The data model is the type of data expected, the blueprint for the data types.

Say we expected a key-value of manufacturer and device as strings:

    ---
    Juniper: vSRX
    Cisco: Nexus
    Brocade: VDX
    VMWare: NSX

However, we got a different data model:

    ---
    Juniper: Also a plant
    Cisco: 6500
    Brocade: True
    VMware:
      - esxi
      - vcenter
      - nsx

> Valid Yaml, but invalid Data

* Yaml does not have a built in data model description or validation mechanism
* A reason why `yaml` is good for human to machine communication but not machine-to-machine

## XML

Comes with schema enforcement, transformations and advanced queries

[lxml](https://github.com/lxml/lxml) is the library of choice for dealing with xml with python

### XML Basics

* Hierachical by nature

    <device>
        <vendor>Cisco</vendor>
        <model>Nexus 7700</model>
        <osver>NXOS 6.1</osver>
    </device>

* `<device>` is called the root node
* spacing and indentatino do not matter
* children of `<device>` are `<vendor>`, `<model>`, `<osver>`

XML elements or nodes can also have attributes

    <device type="datecenter-switch">

Namespaces can be used in xml to designate noes of the same name with different content and purpose

The `xmlns` designation is used for this:

    <root>
        <e:device xmlns:c="http://example.org/enduserdevices">Palm Pilot</e:device>
        <n:device xmlns:m="http://example.org/networkdevices">
            <n:vendor>Cisco</n:vendor>
            <n:model>Nexus 7700</n:model>
            <n:osver>NXOS 6.1</n:osver>
        </n:device>
    </root>

### Using XML Schema Definition(XSD) for Data models

The XML Schema definition ensures the right kind of data is in a specific element

For the following example:

    <device>
        <vendor>Cisco</vendor>
        <model>Nexus 7700</model>
        <osver>NXOS 6.1</osver>
    </device>

We would write a schema to define what was expected:

    <?xml version="1.0" encoding="utf-8"?>
    <xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/
    XMLSchema">
        <xs:element name="device">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="vendor" type="xs:string"/>
                <xs:element name="model" type="xs:string"/>
                <xs:element name="osver" type="xs:string"/>
            </xs:sequence>
        </xs:complexType>
        </xs:element>
    </xs:schema>

* We define that each `<device>` element can have 3 children and each of these must contain a string
* Some elements can be set as required

A python package called `pyxb` can be used to create a python file to represent this schema:

    pip install PyXB

    pyxbgen -u schema.xsd -m schema
    
* pyxb still uses sourceforge for issues which is horrendous

I got this message, but the `schema.py` was created:

    Python for AbsentNamespace0 requires 1 modules

`schema.py` is an unreadable mess, but I think the point is how to use it (not how to read it):

    In [1]: import schema
    In [2]: device = schema.device()
    In [3]: device.vendor = 'Cisco'
    In [4]: device.model = 'Nexus'
    In [5]: device.osver = '6.1'
    In [10]: device.toxml(encoding='utf-8')
    Out[10]: b'<?xml version="1.0" encoding="utf-8"?><device><vendor>Cisco</vendor><model>Nexus</model><osver>6.1</osver></device>'

More [Info from w3c on schema defition](https://www.w3.org/standards/xml/schema)

You can also use [generateDS](https://pypi.org/project/generateDS/) instead of pyxb

### Tranforming XML with XSLT

> Extensible Stylesheet Language Transformations (XSLT)

* A template format.
* A language for applying transformations to XML data

[More info on XSLT from w3c](https://www.w3.org/TR/xslt-30/)

It is primarily used to convert XML into XHTML

Given this xml:

    <?xml version="1.0" encoding="UTF-8"?>
    <authors>
        <author>
            <firstName>Jason</firstName>
            <lastName>Edelman</lastName>
        </author>
        <author>
            <firstName>Scott</firstName>
            <lastName>Lowe</lastName>
        </author>
        <author>
            <firstName>Matt</firstName>
            <lastName>Oswalt</lastName>
        </author>
    </authors>

we want to create an `html` table with the data, this is done with an XSLT document

    <?xml version="1.0" encoding="UTF-8"?>

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output indent="yes"/>
    <xsl:template match="/">
    <html>
    <body>
    <h2>Authors</h2>
        <table border="1">
        <tr bgcolor="#9acd32">
            <th style="text-align:left">First Name</th>
            <th style="text-align:left">Last Name</th>
        </tr>
        <xsl:for-each select="authors/author">
        <tr>
            <td><xsl:value-of select="firstName"/></td>
            <td><xsl:value-of select="lastName"/></td>
        </tr>
        </xsl:for-each>
        </table>
    </body>
    </html>
    </xsl:template>
    </xsl:stylesheet>


* There is a `for-each` loop
* The loop specifies the coordinate: `authors/author` of the XML document (called the `xpath`)
* The `value-of` statement to dynamically insert a value as text from our xml data

So how do we get the HTML output:

    In [1]: from lxml import etree
    In [4]: xsl_root = etree.fromstring(open('table.xsl', 'rb').read())
    In [5]: transform = etree.XSLT(xsl_root)
    In [6]: xml_root = etree.fromstring(open('authors.xml', 'rb').read())
    In [7]: trans_root = transform(xml_root)
    In [9]: print(etree.tostring(trans_root))
    b'<html><body><h2>Authors</h2><table border="1"><tr bgcolor="#9acd32"><th style="text-align:left">First Name</th><th style="text-align:left">Last Name</th></tr><tr><td>Jason</td><td>Edelman</td></tr><tr><td>Scott</td><td>Lowe</td></tr><tr><td>Matt</td><td>Oswalt</td></tr></table></body></html>'

### Additional XSLT logic statements

* `<if>` - only output if condition is met
* `<sort>` - sorts before writing
* `<choose>` - Advanced if statement (allows else if)

### Network Configuration Example

XML data of interface data:

    <?xml version="1.0" encoding="UTF-8"?>
    <interfaces>
        <interface>
            <name>GigabitEthernet0/0</name>
            <ipv4addr>192.168.0.1 255.255.255.0</ipv4addr>
        </interface>
        <interface>
            <name>GigabitEthernet0/1</name>
            <ipv4addr>172.16.31.1 255.255.255.0</ipv4addr>
        </interface>
        <interface>
            <name>GigabitEthernet0/2</name>
            <ipv4addr>10.3.2.1 255.255.254.0</ipv4addr>
        </interface>
    </interfaces>

XSLT for the router configuration:

    <?xml version="1.0" encoding="UTF-8"?>
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.example.org/routerconfig">

    <xsl:template match="/">
        <xsl:for-each select="interfaces/interface">
        interface <xsl:value-of select="name"/><br />
            ip address <xsl:value-of select="ipv4addr"/><br />
        </xsl:for-each>
        </xsl:template>
    </xsl:stylesheet>

Generates:

    interface GigabitEthernet0/0
    ip address 192.168.0.1 255.255.255.0
    interface GigabitEthernet0/1
    ip address 172.16.31.1 255.255.255.0
    interface GigabitEthernet0/2
    ip address 10.3.2.1 255.255.254.0

It is good but also a bit **cumbersome**

#### Searching XML with XQuery

XQuery helps extract data from an XML document

[Further reading on XQuery can be found on w3c](https://www.w3.org/TR/xquery-31/)

## JSON

* Combines the strengths of XML and YAML...apparently
* Importing a Yaml document is effortless (with PyYAML) however with XML there are a few more steps
* JSON (Javascript Object Notation) introduced in 2000, tried to be a lightweight XML

XML:

    <authors>
        <author>
            <firstName>Jason</firstName>
            <lastName>Edelman</lastName>
        </author>
        <author>
            <firstName>Scott</firstName>
            <lastName>Lowe</lastName>
        </author>
        <author>
            <firstName>Matt</firstName>
            <lastName>Oswalt</lastName>
        </author>
    </authors>
    
JSON:

    {
        "authors": [
            {
                "firstName": "Jason",
                "lastName": "Edelman"
            },
            {
                "firstName": "Scott",
                "lastName": "Lowe"
            },
            {
                "firstName": "Matt",
                "lastName": "Oswalt"
            }
        ]
    }

* Contained in `{}` - braces
* keys are always `string`s
* A list of zero or more values is indicated by `[]` - brackets

Data types:
* number
* string
* boolean
* Array
* object (In `{}`)
* Null - `null`

> Ensure that you don't have extra commas after elements

    {
        "hostname": "CORESW01",
        "vendor": "Cisco",
        "isAlive": true,
        "uptime": 123456,
        "users": {
            "admin": 15,
            "storage": 10
        },
        "vlans": [
            {
                "vlan_name": "VLAN30",
                "vlan_id": 30
            },
            {
                "vlan_name": "VLAN20",
                "vlan_id": 20
            }
        ]
    }
    
### Using JSON with Python

    In [1]: import json
    In [2]: with open('json-example.json') as f: 
    ...:     data = f.read()
    In [7]: json_dict = json.loads(data)
    In [8]: type(json_dict)
    Out[8]: dict
    In [9]: for k, v in json_dict.items(): 
    ...:     print(f'{ k } contains a { type(v) } value') 
    ...:                                                                                                                               
    hostname contains a <class 'str'> value
    vendor contains a <class 'str'> value
    isAlive contains a <class 'bool'> value
    uptime contains a <class 'int'> value
    users contains a <class 'dict'> value
    vlans contains a <class 'list'> value


### Using JSON Schema for Data Models

* JSON has a mechanism for schema enforcement called `JSON schema`
* It is available at [json-schema.org](http://json-schema.org/specification.html)
* A python implementation of json schema exists called [jsonschema](https://github.com/Julian/jsonschema)

> Is there a way to describe a data model that can be used with both XML and JSON?

Yes, it is called `YANG`

## YANG

Data models:
* Describe a constrained set of data in a schema language
* Use well defined types and parameters
* Do not transport data and don't care about the underlying transport protocol

### Yang Overview

* focussed specifically on network constructs
* models configuration, operational state data and generic RPC data
* Can enforce more specific values

The are vendor and platform neutral models for YANG from: IETF and OpenConfig

There are also vendor specific models as every vendor has their own solution for multi-chassis link aggregation (VSS, VPC, MC-LAG, Virtual Chassis)

### Deep Dive

Yang includes a `leaf` statement which allows you to define an object that is a single intance, has a single value and no children

    leaf hostname {
        type string;
        mandatory true;
        config true;
        description "Hostname for the network device";
    }

* The `leaf` statement is defining the construct to hold the value of the hostname on the network.
* `hostname` is a required, configurable string.

This leaf can be represented in XML with:

    <hostname>NYC-R1</hostname>

or in JSON with:

    {
        "hostname": "NYC-R1"
    }

#### Leaflist

Multiple instances

    leaf-list name-server {
        type string;
        ordered-by user;
        description “List of DNS servers to query";
    }

represented with XML:

    <name-server>8.8.8.8</name-server>
    <name-server>4.4.4.4</name-server>

with JSON:

    {
        "name-server": [
            "8.8.8.8",
            "4.4.4.4"
        ]
    }

#### List

Allows you to create a list of leafs or leaf-lists

    list vlan {
        key "id";
        leaf id {
            type int;
            range 1..4094;
        }
        leaf name {
            type string;
        }
    }

IN XML:

    <vlan>
        <id>100</id>
        <name>web_vlan></name>
    </vlan>
    <vlan>
        <id>200</id>
        <name>app_vlan></name>
    </vlan>

In JSON:

    {
        "vlan": [
            {
                "id": "100",
                "name": "web_vlan"
            },
            {
                "id": "200",
                "name": "app_vlan"
            }
        ]
    }

#### Container

A container for elements

    container vlans {
        list vlan {
            key "id";
            leaf id {
                type int;
                range 1..4094;
            }
            leaf name {
                type string;
            }
        }
    }

IN XML:

    <vlans>
        <vlan>
            <id>100</id>
            <name>web_vlan></name>
        </vlan>
        <vlan>
            <id>200</id>
            <name>app_vlan></name>
        </vlan>
    </vlans>

In JSON:

    {
        "vlans": {
            "vlan": [
                {
                    "id": "100",
                    "name": "web_vlan"
                },
                {
                    "id": "200",
                    "name": "app_vlan"
                }
            ]
        }
    }

* `XSD`'s are not network smart

# 6. Network Configuration Templates

* Much of a network engineers job involves the cli and entering specific phrases
* It becomes ineffcient and error prone

Network automation bring consistency, predictability and repeatability
The best way to do this is by creating templates for all automated interation with the network
You can standardise those configurations for the standard of your network
Allowing network engineers and consumers (Help Desk, NOC, IT engineers) to dynamically fill in values where needed

## Rise of Modern Templating Languages

Templating languages are perfect for dynamic content

Example using Django:

    <h1>{{ title }}</h1>

    {% for article in article_list %}
    <h2>
    <a href="{{ article.get_absolute_url }}">
        {{ article.headline|upper }}
    </a>
    </h2>
    {% endfor %}

The `title` and `article_list` contains data that will populate real data

Python has some templating languages:
* Django templating language
* [Jinja](http://jinja.pocoo.org/)
* [Genshi](https://genshi.edgewall.org/)
* [Mako](https://www.makotemplates.org/)

### Use of Templating in Network Automation

Say a new data center is created and you are in charge or rolling out configurations. Each switch will have its own unique configuration but a large portion of the config will be similar between devices.
Eg. SNMP community strings, admin password, VLAN configuration

* Templates allow us to standardise the base configuration and make it less error prone
* Saves a lot of time

## Jinja for Network Configuration

Jinja is closely aligned with python, it is also heavily aligned with ansible and salt

Example of single switch interface

interface GigabitEthernet0/1
 description Server Port
 switchport access vlan 10
 switchport mode access
 
Choose which content is dynamic and which is static, in this case the dynamic part is `GigabitEthernet0/1`

interface {{ interface_name }}
 description Server Port
 switchport access vlan 10
 switchport mode access

This can be further simplified as a file: _template.j2_:

interface {{ interface.name }}
 description {{ interface.description }}
 switchport access vlan {{ interface.vlan }}
 switchport mode access

The actual package is called `jinja2`

Using `jinja2`:

    from jinja2 import Environment, FileSystemLoader

    ENV = Environment(loader=FileSystemLoader('.'))
    template = ENV.get_template("template.j2")

    interface_dict = {
        "name": "GigabitEthernet0/1",
        "description": "Server Port",
        "vlan": 10,
        "uplink": False
    }

    print(template.render(interface=interface_dict))

> interface needn't be a dict, it can be a python object

### Conditionals 

Use:

    {% if ... %}
    {% else %}
    {% endif %}

> some switchport interfaces will be VLAN trunks, and others will be in “mode access.

    interface {{ interface.name }}
    description {{ interface.description }}
    {% if interface.uplink %}
    switchport mode trunk
    {% else %}
    switchport access vlan {{ interface.vlan }}
    switchport mode access
    {% endif %}

You can use any of the following to get a variable:

    {{ interface['vlan'] }}
    {{ interface.vlan }}
    {{ interface.get('vlan') }}

With jinja, filters can be used to transform the data: 

    {{ interface.desc|upper|reverse }}

You can also create your own custom filters...which are available in the book

Templates can be included from other files:

    {% include 'vlans.j2' %}

    {% for name, desc in interface_dict.items() %}
        interface {{ name }}
        description {{ desc }}
    {% endfor %}

And inherit from one another:

    {% extends "no-http.j2" %}
    {% block http %}
        ip http server
        ip http secure-server
    {% endblock %}

Variable creation in jinja:

    {% set int_desc = switch01.config.interfaces['GigabitEthernet0/1']['description'] %}
    {{ int_desc }}
    
### Parting Thoughts on Templates

* Keep templates simple
* Leverage inheritance
* Syntax and data should be handled seperately
* Use version control to store templates

# 7. Working with Network API's

## Understanding Network API's

2 most common types:
* HTTP based API's
* NETCONF based API's

### HTTP based API's

* Client (python script) - service (network device or controller)
* Receive data back as XML or JSON, as opposed to HTML

[RESTFul API's architectural constraints](https://restfulapi.net/rest-architectural-constraints/):
* Client - server
* Stateless - all data required is in a single request (in contrast to a persistent connection)
* Uniform interface - individal resource scope, resources should be mapped consistently and have create, modify and delete actions
* Cacheable - caching should be applied to resources
* Layered system - Not sure why this is a requirement
* Code on demand - free to return executable code (optionally)

I also thought to be called restful you need hypermedia (ie. browsable)

### HTTP request types

* GET - retrieve a resource
* PUT - create or replace a resource
* PATCH - create or update a resource object
* POST - create a resource object
* DELETE - delete a resource

### HTTP Response Codes

* 2XX - Successful
* 3XX - Redirection
* 4XX - Client error
* 5XX - Server error

### Non-restful API's over HTTP

* Most commonly sit above CLI's
* In a REST based system a change would never be made when doing a `GET` however no-restful API's could use the same verb for every API call
* URL's will change
* Not as flexible as REST api's

## NETCONF API

* A network management protocol
* for config management, retrieving config state and operational state from network devices

> Netconf is not new, it was written in 2005

* Utilises different configuration data stores
* running, startup and candidate configurations
* candidate configurations are only applied on a commit

Full implementations:
* Juniper Junos
* Cisco IOS-XR

> Different vendors suport different things

* All config changes are commited as a transaction - all commands must succeed or they are not applied

### NetConf Protocol Stack

* Transport - SSHv2, SOAP, TLS
* Messages - `<rpc>`, `<rpc-relay>`
* Operations - `<get-config>`, `<get>`, `<copy-config>`, `<lock>`, `<unlock>`, `<edit-config>`, `<delete-config>`, `<kill-session>`, `<close-session`
* Content - `XML` representation of data models (YANG, XSD)

> Netconf only supports XML

#### Messages

Messages are made by RPC (Remote Procedure Call)

    <rpc message-id="101">
        <!-- rest of request as XML... -->
    </rpc>

Every `<rpc>` includes a `message-id`, the server reuses this in the response

An `rpc-reply`:

    <rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <data>
        <!-- XML content/response... -->
        </data>
    </rpc-reply>

#### Operations

Two primary operations: `<get>` and `<edit-config>`

`<get>` - retrieves running configuration and device state information

    <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <get>
            <!-- XML content/response... -->
        </get>
    </rpc>

There are optional filters: `subtree` and `xpath` to get certain parts of the config

    <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <get>
            <filter type="subtree">
                <native xmlns="http://cisco.com/ns/yang/ned/ios">
                    <interface>
                    </interface>
                </native>
            </filter>
        </get>
    </rpc>

We can narrow it down further:

    <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <get>
            <filter type="subtree">
                <native xmlns="http://cisco.com/ns/yang/ned/ios">
                    <interface>
                        <GigabitEthernet>
                            <name>1</name>
                        </GigabitEthernet>
                    </interface>
                </native>
            </filter>
        </get>
    </rpc>

`<edit-config>` loads configuration into a specific data store: running, startup or candidate

The target datastore is set with `<target>`, if not specified it defaults to the _running_configuration

They are usually enclosed in a `<config>` element

    <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <edit-config>
            <target>
            <running/>
            </target>
            <config>
            <configuration>
                <routing-options>
                <static>
                    <route>
                    <name>0.0.0.0/0</name>
                    <next-hop>10.1.0.1</next-hop>
                    </route>
                </static>
                </routing-options>
            </configuration>
            </config>
        </edit-config>
    </rpc>

edit-config Operations:
* merge - default, as create will raise an error if it already exists
* replace
* create
* delete
* remove

NETCONF Operations:
* `<get-config>` - retrieve all or part of a configuration
* `<copy-config>` - Create or replace contents of one datastore with another
* `<delete-config>` - delete a datastore (running config cannot be deleted)
* `<lock>` - lock to ensure no other systems can make a change
* `<unlock>` - unlock previous locked datastore
* `<close-session>` - Request a graceful termination of a NETCONF session
* `<kill-session>` - Forcefully terminate a NETCONF session

NETCONF servers may also allow `<commit>` and `<validate>` options.

### Exploring API's

Alot of info here on exploring REST API's and NETCONF API's

**tl;dr: Use curl and postman to explore API's, use python's request library to consume API's**

Alot more stuff on vendor specific API's

Also info on `netmiko` in the book

# 8. Git Version Control

If you are not well versed in version control, best to go through this chapter

Some tips I found:

## Terms

* index - directory structure and content at a point in time
* working directory - where files will be modified in the repository
* repository - database containing project information and history
* blobs - contents of files in the repo
* trees - file and directory structure in the repo
* commits - point in time snapshot of the repo, its structure and contents
* HEAD - pointer pointing to the last commit

## Branching

* Branch - pointer to a commit (referenced by their SHA-1 hash)
* HEAD

## Examining the difference between commits

    git diff 9547063..679c41c sw1.txt

For all files

    git diff 9547063..679c41c

Viewing difference between the working tree and the index

    git diff
    
View the difference between the index and the last commit (HEAD)

    git diff --cached

## Delete remote branches that no longer exist

    git fetch --prune

...Lots of info in the book

# 9. Automation Tools

Traditionally ansible, chef, puppet, stackstorm and salt have been more focused on the server automation space.
As these tools had their roots in automating server operating systems and applicatin configuration.
Companies have now started enchancing the network automation ability of their products.

## Major Architectural Differences

#### Agent based vs agentless

* Some tools require an agent to run on the device being managed. Not every NOS (network operating system) supports running agents on  network device.
* Agentless tools are more applicable in the network automation case

#### Centralised vs Dentralised

* Agent-based architectures often require a master server

#### Custom Protocol vs Standard Protocol

* Some tools use custom protocols
* Tools leveraging SSH may be better suited due to their ubiquity

#### Language Extensibility

#### Push versus Pull vs Event Driven

* push - information is pushed from one place to the device being managed
* pull - pulling configuration information and instructions
* event-driven - Perform an action in response to an event or trigger

## The tools

### Ansible

* decentralised
* agentless
* Push mode
* leverages python and jinja templating
* Originally used for ad-hoc commands but has since been used in playbooks written with yaml

### Salt

* Can run agentless (ssh) or agent-based (message bus)
* Uses python and jinja
* Salt states written in yaml
* a platform for event driven automation

### Stackstorm

* Focusses solely on event driven automation
* tasks are performed in response to events
* Uses python to build sensors that emit events to start tasks
* Uses yaml to provide meta data and define a workflow

## Ansible

* Open source platform by Red Hat
* Red Hat sells Ansible Tower that sits on Ansible core has role based access controls, ecure storage of credentials and a restful API

### How Ansible Works

Automating linux servers - operates in a distributed fashion - the control host (local machine) connects to all other machines via ssh - copies python code and executes.

Automating network devices - operates in a local centralised fashion - the control host runs in `local` mode...connecting and running the python code locally. It might connect via SSH, API , Telnet or SNMP.
CLI commands are simply sent over the network.

> For network devices to support non-local mode - evice must permit SSH, copy python files to a temp directory and then execute those files with python. Cumulus Linux, Cisco IOS-XR and Arista EOS support this

### Constructing an Inventory File

    10.1.100.10
    10.5.10.10
    nyc-lf01

You can use hostname (fully qualified) or ip addresses
The inventory file can be more complex with different parts of the network (data center, DMZ, WAN or access)

> 2 regions: AMERS region has Cisco routers being used as CPE edge devices and Nexus switches. The EMEA region has Juniper routers as edge devices and Arista switches.

Start by splitting into groups of devices, the AMERS region has 2 `amers-dc` and `amers-cpe`, each group has 2 devices:

    [amers-cpe]
    csr1
    csr2
    
    [amers-dc]
    nxos-spine1
    nxos-spine2

The `[]` brackets create `groups`

You can created nested groups:

    [amers:children]
    mers-cpe
    amers-dc

    [amers-cpe]
    csr1
    csr2

    [amers-dc]
    nxos-spine1
    nxos-spine2

You need to use the `:children` keyword for nested groups. There are now 3 clear groups: `amers`, `amers-cpe` and `amers-dc`

For the `EMEA` region

    [emea:children]
    emea-cpe
    emea-dc

    [emea-cpe]
    vmx1
    vmx2

    [emea-dc]
    eos-spine1
    eos-spine2

You can then create a group for all cpe devices of all dc devices:

    [all-cpe:children]
    amers-cpe
    emea-cpe

    [all-dc:children]
    amers-dc
    amers-cpe

> You can define variables in your inventory file

### Using Variables in Ansible

#### Group Variables

Assigned at group level, for example the NTP server IP for different regions:

[amers:vars]
ntp_server=10.1.200.1

[emea:vars]
ntp_server=10.10.200.1

Group variables can be created from a new section in the inventory file with keyword `:vars`

when referencing `{{ ntp_server }}` the devices in teh `emea` region will use a different value to those in the `amers` region

> No requirement for ordering of groups and variables in ansible

#### Host Variables

Put the variable on the same line as the host

For example the `nxos-spine1` host must have a specific `ntp_server`:

    [amers-dc]
    nxos-spine1  ntp_server=10.1.200.200
    nxos-spine2


Adding `variable=value` on the same line as the host

You can add multiple values on the same line:

    [amers-dc]
    nxos-spine1  ntp_server=10.1.200.200  syslog_server=10.1.200.201
    nxos-spine2

> More specific variables are given priority

**all**

There is an implicit group called `all`

This keyword is used to automated all devices in an inventory file.

YOu can define group variables for `all`:

    [all:vars]
    ntp_server=10.1.200.199
    syslog_server=10.1.200.201

Variables in the `all` group end up being defaults

> The inventory is not the proper place for variables, there are specific files for that

It is important to specify the `os` of a given device:

    [nxos]
    nxos-spine1
    nxos-spine2

    [nxos:vars]
    os=nxos

    [eos]
    eos-spine1
    eos-spine2

    [eos:vars]
    os=eos

    [iosxe]
    csr1
    csr2

    [iosxe:vars]
    os=ios

    [junos]
    vmx1
    vmx2

    [junos:vars]
    os=junos

> The inventory file is the simplist way to get started however if you have an existing CMDB or large network management system ansible can integrate with that. **Ansible supports dynamic inventory scripts**. The script queries your CMDB, normalises the data, returns valid JSON (as per the docs) 

### Ansible Playbook

* Contains automation instructions
* Tasks and workflows to automate your network
* Written in `yaml`

Eg.

```
---

- name: PLAY 1 - issue snmp commands
  host: iosxe
  connection: local
  gather_facts: no
  
  tasks:
  - name: TASK 1 - deploy snmp commands
    ios_command:
      commands:
        - show run | inc snmp
      provider:
        username: ntc
        password: ntc123
        host: "{{ inventory_hostname }}"

  - name: TASK 2 - deploy snmp commands
    ios_config:
      commands:
        - snmp-server community public RO
      provider:
        username: ntc
        password: ntc123
        host: "{{ inventory_hostname }}"
```

* A single play with 2 tasks

**playbook:**

* `name` - names the play
* `hosts` - the device to automate. Can be a host, group or a combination (seperated by a comma)
* `connection` - defines the connection type a play uses. Most networking devices require this to be `local`
* `gather_facts` - since we are running in local mode, we are telling ansible not to collect facts on the local machine

**tasks**

* Each task runs an ansible module
* `name` - names the tasks, to better identify tasks
* `ios_command` and `ios_config` are ansible modules - in this case they issue exec level and configuration-level commands to Cisco IOS devices

> Ansible has over 700 modules

```
  - name: TASK 1 - deploy snmp commands
    ios_command:
      commands:
        - show run | inc snmp
      provider:
        username: ntc
        password: ntc123
        host: "{{ inventory_hostname }}"
```

* Under `ios_command` are the words `commands` and `provider`, these are parameters passed to the module.
* `commands` accepts a list, `provider` accepts a dictionary
* The jinja variable is referenced as `{{ inventory_hostname}}`
* Variable referenced must be enclosed in quotes

To execute a playbook you need an inventory file so you can call this playbook with:

    ansible-playbook -i inventory snmp-intro.yml

### Using Variable Files

* Inventory files is not the correct place for variables, you should use variable files (when not using a CMDB)
* Stored in yaml files

#### Group Based Variable Files

* Must be stored in a folder called `group_vars`
* `yaml` files within this directory must have the same name as those that appear in the inventory
* For groups: `emea`, `amers`, `iosxe` and `all`....files will be called `emea.yml`, `amers.yml`, `iosxe.yml` and `all.yml`

Eg. `group_vars/amers.yml` can contain:

```
snmp:
  contact: Joe Smith
  location: AMERICAS-NJ
  communities:
    - community: public
      type: ro
    - community: public123
      type: ro
    - community: private
      type: rw
    - community: secure
      type: rw”
```

Sometimes you want to split up variables into seperate files, in which case a directory is created with the group name and files within are all variable files that relate to that group:


```
ntc@ntc:~/testing/group_vars$ tree
.
├── all.yml
├── amers.yml
├── apac
│   ├── aaa.yml
│   ├── interfaces.yml
│   └── ntp.yml
└── emea.yml

1 directory, 6 files”
```

> Cool linux command for a tree view of a directory: `tree`

#### Host based variable files

Exactly like using group variables except the folder is called `host_vars` and files and directories need to match the device names in the inventory file

### Ansible for Network Automation

* Creating multi-vendor configuration templates and autogenerating configurations
* Deploying configurations and ensuring they exist
* Gathering data from network devices
* Performing compliance checks
* Generating Reports

#### Core Network Modules

* `command` - send exec level commands to network devices (eg. `xos_command`, `ios_command`, `junos_command`)
* `config` - send configuration commands to network devices (eg. `ios_config`, `nxos_config`, `junos_config`)
* `facts` - Gather information such as OS version, hardware platform, serial number, hostname, neighbours(eg. `ios_facts`, `xos_facts`)

> To see parameters of a given module use: `ansible-doc <module_name>`

### Idempotency

* Only make the change if it is needed
* Commands are only sent when it is needed to get to a desired state

**Check Mode**

Ability to run playbooks in a dry run mode - to know if changes will occur.
It does everything except make the given change.
Use the `--check` flag when executing the playbook

**Verbosity**

* Every module returns json data - containing meta data about the task at hand.
* You can use the `-v` command (up to 4: `-vvvv`)

**Limit**

Use `--limit` to set the hosts to run on (a single device or multiple). The device must be in the groups on the original `hosts` key.

    ansible-playbook -i inventory snmp.yml --limit eos-spine1 --check -v

> If you are running a fully idempotent playbook for the second or more time, you’ll always have changed=0 as no changes would occur.

### Gathering and Viewing Network Data

* Automate collection of data from network devices
* Methods: Using the `facts` module and issuing arbitrary `show` commands

#### Core facts module

Returns the following as json:

* `ansible_net_model` - The model name returned from the device
* `ansible_net_serialnum` - Serial number of the remote device
* `ansible_net_version` - Operating system running on the remote device
* `ansible_net_hostname` - The configured hostname of the device
* `ansible_net_image` - The image file the device is running
* `ansible_net_filesystems` - Filesystems on the device
* `ansible_net_memfree_mb` - Free memory on the remote device
* `ansible_net_memtotal_mb` - Total memory on the remote device
* `ansible_net_config` - Current active config
* `ansible_net_all_ipv4_addresses` - All IPV4 addresses on the device
* `ansible_net_all_ipv6_addresses` - All IPV6 addresses on the device
* `ansible_net_interfaces` - A hash of all interfaces
* `ansible_net_neighbors` - List of LLDP neighbors

These facts can be accessed in a playbook or jinja template just like another other variable

**Using debug mode**

Run in `debug` mode with the `var` parameter

Eg.

```
tasks:
    - name: COLLECT FACTS FOR IOS
      ios_facts:
        provider: "{{ base_provider }}"


    - name: DEBUG OS VERSION
      debug:
        var: ansible_net_version

    - name: DEBUG HOSTNAME
      debug:
        var: ansible_net_hostname
```

> Using the debug module with `var` parameter is one of the few times you do not use brace notation `{{`

**Saving JSON Output**

To save json output from an ansible module you use the `register` task attribute.
The `register` key is used on the same indent level as the module name.
The json object returned is stored in that registered variable

```
- name: ISSUE SHOW COMMAND
  ios_command:
    commands:
      - show run | inc snmp-server community
    provider: "{{ base_provider }}"
  register: snmp_data
```

Using `register` along with `debug` can be powerful

If you want to debug the actual string (not the dict) you would use:

    - name: DEBUG COMMAND STRING RESPONSE WITH JINJA SHORTHAND SYNTAX
      debug:
        var: snmp_data.stdout.0

    - name: DEBUG COMMAND STRING RESPONSE WITH STANDARD PYTHON SYNTAX
      debug:
        var: snmp_data['stdout'][0]

Or for use in a template:

    {{ snmp_data['stdout'][0] }}

> Every module returns json

### Performing Compliance Checks

Compliance checks are often done manually (SSH) in order to satisfy a network or security requirement
Automating this process is good.

Lets cover 2 more things:
* `set_fact` - a module that create an ad hoc variable out of some other complex set of data. Set fact lets you worry about a single key-value.
* `assert` - Use assert to test whether a given condition is `True` or `False`

1. Gather VLAN data.
2. Save VLAN data as vlan_data.
3. Print (debug) all VLAN data to see what’s being returned.
4. Extract just the VLAN IDs from the full response.
5. Print just the VLAN IDs (validate that the extraction worked as expected).
6. Finally, perform the assertion that VLAN 20 is in the list of VLANs.

Can be done with:

```
---

  - name: PLAY 1 - ISSUE SHOW COMMANDS
    hosts: eos
    connection: local
    gather_facts: no

    tasks:

      - name: RETRIEVE VLANS JSON RESPONSE
        eos_command:
          commands:
            - show vlan brief | json
          provider: "{{ base_provider }}"
        register: vlan_data

      - name: DEBUG VLANS AS JSON
        debug:
          var: vlan_data

      - name: CREATE EXISTING_VLANS FACT TO SIMPLIFY ACCESSING VLANS
        set_fact:
          existing_vlan_ids: "{{ vlan_data.stdout.0.vlans.keys() }}"

      - name: DEBUG EXISTING VLAN IDs
        debug:
          var: existing_vlan_ids

      - name: PERFORM COMPLIANCE CHECKS
        assert:
          that:
            - "'20' in existing_vlan_ids"
```



## Source

* Network Programmability and Automation - Jason Edelman, Scott S. Lowe, Matt Oswalt