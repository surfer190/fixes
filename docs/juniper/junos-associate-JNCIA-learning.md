---
author: ''
category: Juniper
date: '2021-02-04'
summary: ''
title: Juniper associate JNCIA Learning Notes
---
# Juniper associate JNCIA Learning Notes

## 2. JunOS Fundamentals

Common language across routing, switching and security device.

* Modular design.
* One process failing does not break other processes.
* Build on open source: modified FreeBSD or Linux

All platforms use the same source code base.
Core features work consistanly on all platforms running Junos OS.

Single Operating system - with a singel release track.

Some junos code bases release at a faster rate - the `X` releases that have service enhancements for security devices - the SRX.
The `R` release are bug fixes with no new enhancements.
The `F` release has bug fixes and new features.

Format is `m.NZB`

* m: major
* N: minor
* Z: Release type
* B: Build Number

### Seperation of Control and Forwarding Plane

* Control plane: routing engine (RE)
* Forwarding plane: packet forwarding engine

RE:

* x86 or PowerPC Architecture
* maintains routing table, bridging table and primary forwrding table
* Connects to Packet Forwarding Engine (PFE) using internal link
* contains JunOS
* brain of the platform (protocol updates and system management)
* Chassis, system and usermanagement
* sits on top of Junos kernel

PFE:

* runs on seperate hardware
* uses ASICs (Application specific integrated circuits)
* Recieves the forwarding table from the RE via internal link - has a copy
* forwards frames and packets

Other services provided by the PFE:

* policers- rate limiting
* stateless firewall filters
* class of service

Makes possible:

* GRES - Graceful routing engine switchover
* NSR - Non-stop Active Routing
* ISSU - In-service Software Upgrades

Transit traffic

* all traffic entering ingress network port is compared against the forwarding table entries and is forwaredd out an egress network port
* Never sent to or passes through the control plane
* Can be:
    - unicast: enters one ingress and sent out 1 egress
    - multicast: enters one ingress and sent out multiple egress

Exception traffic

* does not pass through local device - needs to contract the RE
* packets addresses to the chassis - telnet sessions, pings, traceroutes
* IP packets with IP Options set
* traffic that requires ICMP (Internet Control Message Protocol) message generation - no entry present for destination in routing table, TTL expired

Traffic sent to RE is rate limited to prevent denial of service attacks
Gives preference to local and control traffic
Built-in rate limiter is not configurable

Simplified:
* transit traffic - forwarded through PFE
* exception traffic - processed locally by RE or PFE
* protocol and management traffic - sent directly to the RE

### Devices

Routing devices:

* PTX - packet transport routers up to 460Tbps (super core)
* MX - up to 80 Tbps, provider edge services and aggregation
* ACX - simplified end-to-end provisioning

Switching devices:

* EX - Up to 13.2 Tbps - access, aggregation and core
* QFX - layer 2/3 with 10, 25, 40 or 100 GbE

Security devices:

* SRX - Up to 2Tbps firewall 

SDN (software defined networking) products

* NFX - customer premises equipement
* Contrail cloud - utilises openstack for cloud storage and networking
* Northstar controller - automates traffic engineering paths increases utilisation
* WANDL IP/ MPLS view - network management system, simulates large MPLS networks and design

JunOS can be run as a VM:

* Run on top of VMware or KVM (kernel-based virtual machine)
* vSRX
* vMX - ASICS are compiled into x86 instructions - carrier grade

Disaggregated JUNOS - seperating RE and PFE into their own VM:

* Improves performance
* Better use of CPU cores

Core functions of legacy OS attached to FreeBSD kernel - have been designed to run independently of the kernel

## 3. User Interface Options - Junos CLI

2 Interfaces provided:

* Junos CLI - text based command shell - an out-of-band serial option of in-band with telnet or ssh
* J-web itnerface - web based GUI

Logging in requires a username and password - default is `root` with no password

If a hostname has not been setup the system will show `Amnesiac`

Two modes of the cli:

* configuration mode - shown by `#`. Configure the device.
* operational mode - shown by `>` character. Monitor and troublesheet (`monitor`, `ping`, `how`, `test`, `traceroute`)

> Getting help: just type `?`

Getting help for a specific command `clear ?` will display possible options

In depth help:

* `help topic ?` - usage guidelines for the statement
* `help reference ?` - summary information
* `help apropos ?` - displays `set` commands that reference a specific variable - relevant to your current configuration hierachy

Command completion - press `<space>` to complete commands

press `<tab>` to complete commands and variables...gives a list of possible completions

Turn off with:

    set-cli complete-on-space off

Editing command lines:

* `ctrl + b` - back one
* `ctrl + f` - forward one
* `ctrl + a` - beginning on command
* `ctrl + e` - end of command

Using Pipe `|`:

    re0> show route | ?    
    Possible completions:
    append               Append output text to file
    count                Count occurrences
    display              Show additional kinds of information
    except               Show only text that does not match a pattern
    find                 Search for first occurrence of pattern
    hold                 Hold text without exiting the --More-- prompt
    last                 Display end of output only
    match                Show only text that matches a pattern
    no-more              Don't paginate output
    refresh              Refresh a continuous display of the command
    request              Make system-level requests
    resolve              Resolve IP addresses
    save                 Save output text to file
    tee                  Write to standard output and file
    trim                 Trim specified number of columns from start of line

Available filters (in config mode):

* `compare <filename>` or `compare rollback n` - compares changes
* `display changed` - show changed lines only
* `display detail` - additional info
* `display inheritance` - show inherited config
* `display omit` - omit statements with omit
* `display set` - show set commands only

Available filters:

* `count` - number of lines in output
* `display commit-scripts`
* `display xml` - show output of XML/Netconf format
* `except <regular-expression>` - 
* `find <regular-expression>` or `match <regular-expression>` 
* `hold` - hold text without exiting the `--More --` prompt
* `last` - displays the last screen of information
* `no-more` - displays output all at once
* `request message` - display output to multiple users
* `save <file>` - save the output to a file or url
* `trim` - trims number of columns from start of line

CLI operational mode is hierachical - from less specific to more specific

1. `clear`, `configure`, `help`, `monitor`, `set` ...
2. `arp`, `configuration`, `ospf`, `version` ...
3. `database`, `interface`, `neighbour` ...

Operational capabilities:

* moving in and out of config mode
* Monitor and troubleshoot
* copy files
* restart software processes
* perform system level operations

### Active vs Candidate Configuration

Configuration changes do not take effect immediately - allowing you to group changes and apply in a batch.

* active configuration - currently running config
* candidate configuration - temporary config - created from active config + configure

The `configure` command populate the candidate configuration from the active config. You then modify the candidate config with your changes - then you `commit` - junOS checks syntax then applies to active config.

You can retrieve previous configurations with `rollack n` command.
A maximum of 50 configurations are saved.
`rollback 0` is the current active configuration.
Only after a `commit` will the the `rollback` be applied.

### Entering configuration command

Use:

    configure

If you enter it while someone else is in it - it will display.

Use the `configure exclusive` to ensure only you can enter it.

Uncommited changes are discarded when you exit.

You can change configuration privately with `configure private`.
When users issue a `commit` it is applied to the global config - `rollback 0` discards only the private user's changes.

2 users in private mode both making a change on teh same config - only the first change will be commited.
It will only be applied if user 2 `commit` again.

### Configuration Hierachy

THe configuration hierachy is indepenent of the operation model hierachy.

1. `edit`
2. `bgp`, `isis`, `mpls`, `vrrp` ...
3. `area`, `graceful-restart`, `overload`
4. `area-range`, `interface`, `nssa`

`show` commands will show the condidate configuration

Terminating statements are shown with a trailing `;`, the hierachy is shown with the `{}`

    # set services ssl traceoptions level brief

    # show services

    ssl {
        traceoptions {
            level brief;
        }
    }

### Moving Between Levels

* `edit` - function like change directory - sets the current hierachy level you want to move to
* `up` - move 1 level up in the hierachy
* `up n` - move up `n` number of times in teh hierachy
* `top` - move to the top of the configuration hierachy
* `exit` - return to most recent level

### Modify Configuraiton

Use the `set` command to modify configuration

    set ftp

Use `delete` to remove statements:

    delete telnet

You can `wildcard delete`:

    wildcard delete interfaces ge-1/*

Deactivating:

    deactivate interfaces <interface-name>
    activate interfaces <interface-name>


* `rename` - `rename interface ge-0/0/10 to ge-0/0/11`
* `replace` - `replace pattern ge-0/0/10 to ge-0/0/11`
* `copy` - `copy interfaces ge-0/0/10 to ge-0/0/11`
* `insert` - `insert term before term two`
* `annotate` - `annotate name-server "adding new name servers"`

### Showing Config

Configuration mode `show` command shows candidate configuration

    show system services 

is the same as:

    edit system services
    show

View set commands to build a configuration

    show system services | display set

### Commiting config

Use `commit`

For `configure private` - `commit` needs to be issued at the `top` hierachy

On devices with redunant routing engines you can do a

    commit synchronize

Alternatively make it default

    set system commit synchronize

validate the syntax of a candidate configuration with:

    commit check

For remote setup where you might make the device inaccessible use a `commit confirmed` to temporarily rollback the config if another `commit` is not issued within 10 minutes

### Scheduled Commits

Schedule a commit at a specific time

    commit at 21:00:00

Add a comment to a commit

    commit comment "Change BGP config"

Commit and exit configuration

    commit-and-quit

### Comparing Configuration

Compare candidate and active

    show | compare

Compare active and archive

    show configuration | compare rollback n
    show configuration | compare file

Arbitrary file compare

    file compare files file1 file2

Rollback

    rollback ?

Change amount of rollbacks on smaller junos devices

    set-max-configurations-on-flash ?

Save a candidate configuration (only at current hierachy and below)

    save filename

> Saves to users home directory by default

Loading complete or partial configuration

    load ?

    re0# load ? 
    Possible completions:
    factory-default      Override existing configuration with factory default
    merge                Merge contents with existing configuration
    override             Override existing configuration
    patch                Load patch file into configuration
    replace              Replace configuration data
    set                  Execute set of commands on existing configuration
    update               Update existing configuration

Run oeprational commands in config mode:

    re0# run ping 1.1.1.1

### Lab Exercsies

Find the down interfaces

    show interfaces | match down 

Count the number of interfaces that are down

    show interfaces | match down | match Physical | count 

Get detailed info about a system hostname

    help reference system host-name

Navigate to interfaces part of hierachy

    configure
    edit interfaces

Move to protocols ospf

    top edit protocols ospf

Get chassis hardware (it is operational)

    run show chassis hardware

Just changing to different hierachies creates the empty stanza meaning - configuration has changed

## 4. User Interface Options: J-web Interface

Web-based gui access with http or https

* Dashboard tab - glance at system status, ports, alarms, security information
* Configure tab - configure system with point and click or text config
* Monitor tab - view results of config entries - like routing table
* Reports tab - generate reports on demand
* Administration tab - network tools (ping, traceroute), software upgrades

Same authnetication as CLI - remote access http and https must be enabled. Can use external authnetication like radius.

    edit systems services

> Is pre-installed on SRX adn vSRX devices

Wizard to setup device

    Configure -> Device settings -> Basis settings

* Identity details - hostname, root password, configure DNS servers

### Management Access Configuration

* Configure ip and maangement port
* Access methods
* Systems services enabled - telnet, SSH, Netconf etc.
* Ports for HTTP and HTTPs

### Date and Time Details

* NTP servers (recommended)

Press Commit after changing

### Gettings Started

* Interfaces configuration
* Security Zone Creation
* Configure Firewall Policies
* Network Address Translation policies
* License Management

### Packet Capture

* Packet capture lets you capture traffic destined for or originating from routing engine
* Does not capture transit traffic
* You can capture control traffic
* Find specific traffic `monitor traffic`

    Administration -> Tools -> Packet Capture Start

### Upgrade JunOS

    Administartion -> Device -> Software -> Uplaod Package

### New USers

Use the user management page

    Configure -> Users -> User Management

> Login name, password and class must be added

### Interface Configuration

Add interface, edit on fast logical interfaces on fast ethernet or gigabet ethernet interfaces

    Configure -> Intefaces -> Ports -> Edit logical Interface

### Lab

View routing engine information

    Monitor -> Device -> Chassis Information

View Alarms

    Monitor -> Alarms -> Alarms

Examine routes

    Monitor -> Routing -> Route Information

View logins for the system:

    configure
    show system login

## 5. Initial Configuration

All Junos devices have a factory default configuration, with a `root` account with no password.
Setting a password is required.

    set system root-authentication plain-text-password
    commit

System logging is enabled to track events

View default logging configuration

    # show system syslog

Switches (like EX series) operate at layer 2 out of the box RSTP (Rapid Spanning Tree Protocol) and LLDP (Link Layer Discovery Protocol)

### Return a device to factory default configuration

    load factory-default

You must set the root password

    set system root-authentication plain-text-password

    commit

### Powering on a Device

* Follow safety guidelines
* The device will always power back up when power is lost

Always gracefully shutdown

    request system halt ?

To schedule at a time

For device with multiple routing engines

    request system halt both-routing-engines

For ex switches halting all members:

    request system halt all-members

### Initial Configuration Checklist

* Hostname
* System time
* System services (remote access)
* Management interface and static route for management

Steps:

1. Login as root - initially `root` with no password (`Amesiac` indicates factory-default)
2. Start cli - start in unix shell - type `cli` (only root user has this)
3. enter config mode - type `configure`
4. set identification params - set root password (the password is always encrypted in config)

    edit system
    set host-name router
    set root-authentication plain-text-password

5. set time params

    set time-zone Africa/Johannesburg
    
6. set management access params - using a default static route for management traffic is discouraged

    set services ssh
    set cli idle-timeout 0 # disable idle timeout
    set login message "Warning..."
    commit
    
7. set mangement network params

    > Using a default static route for management traffic is highly discouraged - you should be as specific as possible and use `no-readvertise`
    
    > The `no-readvertise` marks the route as inelligible for advetisement through the routing policy
    
    Static route configuration is only available when routing process is running (rpd) - ensure a backup router is directly connected to the primary on the same subnet.
    
    A backup router is needed

8. activate configuration

    commit and-quit


View the full configuration with the operation command:

    show configuration

### Rescue Configuration

Designed to restore basic connectivity in the event of configuration problems. Recommended to contain the minimum needed for basic connectivity.
It must include a root password.
By default - no rescue configuration is defined.

Save the active configuration using oepration mode:

    request system configuration rescue save

> If a rescue already exists - it replaces it

Manually delete a rescue

    request system configuration rescue delete

To rollback (in configuration mode):

    rollback rescue
    commit

### Interfaces

Interfaces are primarily used to connect a device to a network

Some interfaces are used to provide a service or a function for the system it operated

On `junOS` serveral types exist:

* management interfaces - connect junos device to a management network eg. `fxp0` and `me0`
* internal interfaces - control and connect the forwarding plane eg. `fxp1` and `em0`
* network interfaces - media specific network connectivity eg. `Ethernet`, `SONET`, `ATM`, `T1` and `DS3`
* services interfaces - more user-configurable services (encryption, tunneling, etc.)
* loopback interfaces - hardware independent interface eg. `lo0`

service interfaces:

* `es` - encryption interface
* `gr` - generatic route encapsulation tunnel
* `ip` - IP-over-Ip encapsulation tunnel
* `ls` - link services interface
* `ml` - multilink interface
* `mo` - passive monitoring interface
* `mt` - multicast tunnel interface
* `sp` - adaptive services interface
* `vt` - virtual loopback tunnel interface

#### Interface Naming

* Interface media type: `ge`, `so`, `at`
* Line card (FPC slot number)

In typical port numbering the slot begins with 0 and increments based on the system hardare configuration.

    ge-0/2/3 = physical port 4 of a gigabit ethernet PIC in slot 3
    
    type - FPC Slot / PIC / Port

Examples:

* `lo0` - loopback
* `ae` - aggregated ethernet interface (physical interfaces are aggregated for max traffic reasons)
* `as` - aggregated SONET
* `vlan` - vlan interface
* `irb` - intergrating routing and bridging

Internally generated non-configurable:

* `gre`
* `mtun`
* `ipip`
* `tap`

#### Logical Units

Each physical interface descriptor can contain 1 or more interface descriptors.
Map virtual interfaces to a single physical device. (Similar to subinterfaces of other vendors)

Useful in ATM and frame relay networks

A logical unit is always required

Some encapsulations support only 1 logical unit (and unit must be 0):

* PPP (Point to point protocol)
* HDLC Cisco

Some support multiple logical interfaces:

* frame relay
* ATM
* Tagged Ethernet

Unit number vs Circuit Identifier

* circuit identifier - identifies the logical tunnel or circuit
* unit - identified logical partician of physical interface

> best practice to keep both the same

#### Multiple Devices

Junos devices can have more than 1 address on a single logical interface

Issuing a second set command does not overwrite the previous address:

    set family inet address 10.1.1.1


The `rename` command is used to address this mistake

    rename family inet address 10.1.1.1/32 to address 10.1.1.1/24

#### Interface Properties

Everything under the `interface-name` are the _physical properties_ of that interface

`unit-number` indiciates a logical unit / sub interface

    interfaces {
        {{ interface-name }} {
            physcial properties;
            unit {{ unit-number }} {
                logical properties;
            }
        }
    }

> A single logical unit does support mulitple protocol families - such as `inet` and `inet6` - you cannot configure another protocol with the `ethernet-switching`family

`preferred` is used when multiple ip addresses belonging to the same subnetonthe ame interface. this options lets you set which will be used as the source address.By default the numerically lowest address is chosen.

    family inet {
        address 172.19.102.1/24
        address 172.19.102.2/24 {
            preferred;
        }
    }

`primary` is used by default as the local address for broadcast and mulitcast sourced locally. Useful for selecting the local address used for packets sent out on numbered interfaces with multiple 127 addresses are configured on `lo0`. By default the numberically lowest address on the interface is used.

    lo0 {
        unit 0 {
            family inet {
                address 192.168.100.1/32;
                address 192.168.200.1/32 {
                    primary;
                }
            }
        }
    }

`show interfaces lo0.0 | find addresses`

Will flag the second as primary

#### tracking Interface State

    show interfaces terse

For a specific interface

    show interfaces ge-0/0/2 terse

Physcial properties:

* Maximum Transmission Unit (MTU)
* Link Mode
* Clocking

Logical properties:

* Protocol family
* Virtual Circuits
* Addresses

### Lab

Load factory defaults:

    configure
    load factory-default

View the configuration:

    show
    commit

Edit root authnetication:

    edit system root-authentication
    set plain-text-password
    top
    commit and-quit

List the files:

    file list /var/tmp

Set the hostname:

    set system host-name vSRX-1

Set the time-zone (in config mode):

    set system time-zone Africa/Johannesburg

Set date:

    run set date YYYYMMDDhhmm.ss

Create a rescue config:

    request system configuration rescue save

Show rescue config:

    file show /config/rescue.conf.gz

Delete system services:

    configure
    delete system services
    commit

Show and rescue:

    show system services
    rollback rescue

Delete rescue:

    request sytem services rescue delete
    file show /config/rescue.conf.gz

Configure interfaces: unit 0 on ge-0/0/4 which is to be vlan tagged to vlan 300:

    configure
    edit interfaces
    set ge-0/0/4 vlan-tagging
    set ge-0/0/4 unit 0 vlan-id 300 family inet address 172.18.1.2/30
    set ge-0/0/3 unit 0 family inet address 172.20.66.1/30
    set ge-0/0/2 unit 0 family inet address 172.20.77.1/30
    set lo0 unit 0 family inet address 192.168.1.1/32
    set lo0 unit 0 description "Loopback interface for main routing instance of vSRX-1"
    commit and-quit

Show interfaces

    show interfaces terse

## 6. Secondary System Configuration

### User Authentication

* Local password authentication
* RADIUS
* TACAS+

### Local Password auth

* local username and password
* home directory is generated
* `set cli directory <directory>` - change directory

### RADIUS and TACAS+

* Distributed client and server systems

### Authentication Order

    show system authentication-order
    inactive: authentication-order [ tacplus password ];

* If there is no response from the other auth methods - local authentication is used
* If there is responses and rejected - local authentication is not used

### Authorization

* Each command is subject to authorization
* applied to all non-root users

Hierachy

Users -> class -> permissions -> allow / deny overrides

* users - defines authorization parameters
* class - named container with permissino flags: `super-user`, `operator`, `read-only`, `unathorized`
* permissions - pre-defined set of related commands: `access`, `access-control`, `all`, etc
* allow / deny overrides - exceptions for commands `deny-commands`, `deny-configuration`

### System Logging

* Unix syslog mechanism
* In `/var/log`
* syslog: `/var/log/messages`
* remote logging is available

hierachy: `[edit system syslog]` or `[edit routing-options options syslog]`

#### Interpreting Syslog Messages

    Jan 05 10:48:23 host mgd[4350]: UI_DBASE_LOGOUT_EVENT: User 'User' ....

* `timestamp`: when the message was logged
* `name`: configured system name
* `pid` (process name): name of process
* `message-code`: general nature of error
* `message-text`: 

See message codes:

    help syslog
    
    Syslog tag                       Help
    AAA_DUP_INSTANCE                 Duplicate request
    AAA_HA_EVENT                     Switch over event
    AAA_INFRA_FAIL                   Infra failure
    AAA_INIT_FAIL                    aaad intialization failed
    AAA_RADIUS_SERVER_STATE_CHANGE   State of the radius server has changed
    AAA_TASK_CREATE_FAIL             AAA task creation failed
    AAA_UNAUTH_USER                  Authorization failure
    AAA_USAGE_ERR                    aaad usage error
    ACCT_ACCOUNTING_FERROR           Error occurred during file processing
    ACCT_ACCOUNTING_FOPEN_ERROR      Open operation failed on file
    ACCT_ACCOUNTING_SMALL_FILE_SIZE  Maximum file size is smaller than record size
    ACCT_BAD_RECORD_FORMAT           Record format does not match accounting profile
    ACCT_CU_RTSLIB_ERROR             Error occurred obtaining current class usage statistics
    ACCT_FILECOPY_ERR                Error copying file
    ACCT_FORK_ERR                    Could not create child process

### Tracing

* Debugging
* stored in `/var/log/` or remote logging

    [edit system tracing]
    destination-override syslog host 1.1.1.1;

> You can enable tracing without a drop in performance due to JunOS design - but always remember to turn it off

Trace a specific protocol

    [edit protocols <protocol>]
    traceoptions {
        file bgp_trace replace size 128k files 10 no-world-readable;
        flag event detail;
        flag error detail;
    }
        
* `files` - max number of tracefiles - logrotate

Use `no-stamp` for no timestamp

Can also add tracing to an interface

    [edit interface <interface-name>]

* Kernel does the logging so you cannot specify a file in this case - it goes to `/var/log/messages`

### Analysing log and trace files

Show log files

    show log

Show file contents

    show log 

Press `h` to show help

Use a pipe for better search:

    show log messages | match "support info"

    show log message | match "error|kernel|panic"

Monitor log realtime

    monitor start <filename>

See files being monitored

    monitor list

    monitor start messages | match fail
    
Stop monitoring

    monitor stop

Disable all tracing at a hierachy

    delete traceoptions

Truncate files

    clear log <filename>

Delete a file

    file delete <filename>

### NTP Clock Synchronization

* Use a common accurate time source

    configure
    edit system ntp
    show

If time diff between local device and remote is more than 128 ms - the clocks are slowly synchronised
More than 1000 seconds - a `boot-server` is used

Set a `boot-server`

    > set date ntp <address>

Show synchronizations

    show ntp associations

Further sync details

    show ntp status

### Archiving configuration files

backing up to remote device

    edit system archival

* ftp or scp
* `transfer-interval` statement specifies how often backups happen (15 to 2880 minutes)
* `transfer-on-commit` backup on each commit

Before sending the config is saved at `/var/transfer/config` directory

### SNMP

* JunOS work as SNMP agents
* Exchanges network informatation with a network managemetn system

Message types:

* get, getbulk, getnext - request info
* set requests - changing values
* notifications - informs management of significant notifications

Version 3 of SNMP has a user based security model and a view based access control

#### Management information base

* defines managed objects
* hierachical

#### JUNOS OS Supports

* Supports 1, 2c and 3

    configure
    edit snmp
    
    description ""
    location ""
    community {
        
    }
    trap-group {
        
    }

Monitoring SNMP monitoring

### Lab

Create a login class with `view`, `view configuration` and `reset` permissions

    configure
    edit system login
    set class juniper permissions [view view-configurations reset]

Create a read only uswr

    set user nancy class read-only
    set user nancy authentication plain-text-password

    set user walter class juniper
    set user walter authentication plain-text-password

Restart the routing process as walter

    restart routing

Add clear permissions to read-only

    set class read-only permissions clear

Set radius

    set system radius-server xx.xxx.xx secret Juniper
    set system authentication-order radius
    commit

Rename the radius server

    rename system radius-server 173... to 10.1.1.1

View current logging info

    show system syslog

Log config changes in config-log with info severity and set the severity for default messages as any

    edit system syslog
    set file config-changes change-log info
    set file messages any any

Configure to send to a remote

    set host 172.25.11.254 authorization info
    commit

View created log

    run file list /var/log

Set the ntp server

    set system ntp server 172.25.11.254
    set system ntp boot-server 172.25.11.254
    commit

View the log config-changes

    > show log config-changes

Manually force synchronisation

    set date ntp

Show ntp associations and uptime

    show ntp associations
    show system uptime

Enable snmp using a community value of junos

    configure
    set snmp community junos clients 172.25.11.254

Configure a trap group to send to the nms server - send when an interface goes down

    set snmp trap-group interfaces targets 172.25.11.254
    set snmp trap-group interfaces categories link
    commit

Disable an interface to test

    set interfaces ge-0/0/2 disable
    commit

    run show interfaces ge-0/0/2 terse

Reenable

    delete interfaces ge-0/0/2 disable
    commit and-quit

Verify a trap was issued

    show log messages | match ge-0/0/2 | match snmp

    show snmp statistics

> The `Traps` value should not be 0

Perform an snmp walk

    show snmp mib walk jnxOperatingDescr

Configure an archive

    configure
    edit system archival configuration
    set archive-sites "ftp://ftp@172.25.11.254/archive" password ftp
    set transfer-on-commit
    commit and-quit

Verify a successful transfer

    show log messages | match transfer

## 7. Operational Monitoring and Maintenance

Monitoring Tools:

* Junos CLI
* Junos Space
* SNMP
* Hardware LEDs
* Front panel LCD
* JWeb

### System Level Operations

    show system <keyword>
    
* `alarms` - current system alarms
* `boot-messages` - messages seen during last system boot
* `connections` - status of local TCP and UDP connections
* `statistics` - protocol statistics
* `storage` - current storage space

> Do `show system ?`

### Monitoring Chassis

    show chassis <keyword>

* `alarms` - chassis alarms
* `environment` - environmenal status
* `hardware` - inventory of hardware
* `routing-engine` - operational status

> `show chassis ?`

### Monitoring Interfaces

    show interfaces ge-0/0/0 ?

Terse output

    show interfaces terse
    Interface               Admin Link Proto    Local                 Remote
    ge-1/0/0                up    up
    
> for verifying state information

Extensive output

    show interfaces ge-1/0/0 extensive

> Best for troubleshooting interfaces

Monitor an interface

    monitor interface <interface-name>

Monitor all interfaces

    moinitor interface traffic

### Network Utilities

General reachability and path packets take

    traceroute <ip>

and

    ping <ip>
    ping <ip> count 5

> ICMP - Internet Control Message Protocol

Monitor packets - decode packets and access to `tcpdump` originates or terminates on local RE

> if you do not specify an interface - the management interface is used

Diagnose problems at layer 2 with `layer2-headers`

> Caution with `write-file` it could file the space of the device

    monitor traffic interface ge-1/0/0 layer2-headers no-resolve

There is also `telnet`, `ssh` and `ftp`

    file copy ftp://ftp@..../myfile.tar.gz /var/.

### Display release

    show version
    Junos: 19.1R3-S3.2

### Junos Naming Convention

* prefix: `jinstall*` (M, T, MX series), `junos-srx*` (SRX series)
* release: `19.1R3-S3.2` - major.minor[Release type] R - Standard, X- faster cadence, S- service
* edition: domestic or export

    junos-srxsme-15.1X49-D70.3-deomestic.tgz

### Upgrading JunOS

1. Download correct image
2. From [Junos Support](https://support.juniper.net/support/)

    request system software add <path / image name>

System will need to reboot

All binaries are digitally signed - protect system integrity and prevent unauthorised software

    request system software add /var/tmp/image-name reboot

Check storage capacity before `show system storage`

### Unified ISSU (in Service Software Update)

* No disruption on control plain
* minimal disruption on operations
* GRES (Graceful Routing Engine Switchover) and NRS (Nonstop Active Routing)

1. Enabled GRES and NSR - verify REs and protocls are synchronised
2. Download new software package and copy to router
3. `request system software in-service-upgrade`

### Password Recovery Process

> only using Console

Disable password recovery by setting:

    edit system ports
    show
    
    console insecure;

1. reboot: press `<space>` and `boot -s`
2. enter recovery mode: `<enter>` and `recovery`
3. reset root password and commit change: `configure` and `set system root-authentication plain-text-password`
4. exit configuration mode

### Storage Cleanup

    request system storage cleanup

or

    request system storage cleanup dry-run

### Prepare for redeployment

> Remove existing stuff

    request system zeroize

Scrub and make unrecoverable

    request system zeroize media

### Lab

View the system processes and find the `rpd` (routing protocol process)

    show system processes extensive

and:

    show system processes extensive | match "pid | rpd" 

View packets sent

    show system statistics

Show space on a directory

    show system storage

See uptime

    show system uptime

See current users

    show system users

Force a user to logout

    request system logout user <name>

Check the CPU utilisation of the routing engine

    show chassis routing-engine

See the location

    show chassis location

Set options

    set system location ?     
    Possible completions:
    altitude             Feet above (or below) sea level
    + apply-groups         Groups from which to inherit configuration data
    + apply-groups-except  Don't inherit configuration data from these groups
    building             Building name
    country-code         Two-letter country code
    floor                Floor of the building
    hcoord               Bellcore horizontal coordinate
    lata                 Local access transport area
    latitude             Latitude in degree format
    longitude            Longitude in degree format
    npa-nxx              First six digits of phone number (area code plus exchange)
    postal-code          Zip code or postal code
    rack                 Rack number
    vcoord               Bellcore vertical coordinate

Set the datacenter location

    set system location building "Data Centre #3" floor 3

View chassis hardware

    show chassis hardware

Verify interfaces are up

    show interfaces terse
    show interfaces fxp0 extensive

Clear interface statistics and view traffic

    clear interfaces statistics fxp0
    show interfaces fxp0 extensive | find "traffic"

Ping an ip with 500 bytes

    ping 172.... size 500

Monitor `fxp0`:

    monitor traffic interface fxp0

Just ICMP traffic:

    monitor traffic interface fxp0 matching icmp

## 8. Interface COnfiguration Examples

### Interface properties

Each interface has:

* physical properties - data link layer protocol and keepalives, link mode, speed, MTU (maximum transmission Unit), Clocking , scambling, FCS (Frame Check Sequence) and Diagnostic Characteristics
* logical properties - protocol family (iso, mpls, inet, inet6), addresses, virtual circuits (VPI, VCI, vlan-tag), inverse arp and traps

All directly under the interface name - is the physical properties.
All directly udner the unit number - as the logical properties

IPv4 routing:

* `vlan-tagging` physical property gives way to `vlanid 100;` logical properties
* `encapsulation frame-relay` physical property gives way to `dlci 202;` logical properties
* `atm-options` gives way to `vci 100;`
* `encapsulation ppp` gives way to `family iso` - for isis routing protocol and `family mpls` - traffic engineering

2 serial interfaces bundled as a multilink PPP: `family mlppp`

### logical aggregated interface (lag) configuration: `ae`

> Creation of the physical aggregated interface is required

by default no aggregated interfaces exist:

    run show interfaces terse | match ae
    edit chassis
    set aggregated-devices ethernet device-count 1
    commit
    
    run show interfaces terse | match ae

Needs at least 1 logical unit and interface

LACP - link aggregation control protocol - if LACP at least 1 side must be configured in active mode

### Configuration Groups

Enable groups containing config statements and direct inherititance

* smaller more logically constructed configuration files

wildcards can be used in groups - for inheritance

    show groups

### Display Inherited Configuration

Need `| display inheritance`

    show interfaces ge-1/0/0 | display inheritance 

Without the `##`

    show interfaces ge-1/0/0 | display inheritance | except 

## 9. Routing Fundementals

Routing - moving data between layer 3 (l3) networks

Routers are used to perform routing operations (some switches and security devices do routing)

The internet is a collection of many networks (not a single network)

requirements:

1. an end-to-end communication path (physical path)
2. all l3 devices within the communication path have the required routing information - must have gateway configured (router connecting to networks as well as the internet) - must determine the correct next hop for transit traffic

JunOS uses the forwarding table (a subset of routing table contents)

For any device to connect with another device outside of its directly connected subnet - a gateway is required (the ip address of the gateway) - the datacenter also needs a gateway

The router (the gateway device) requires sufficient routing informatino to determine the next hop
The router learns the information - by way of the interface configuration - the router adds the networks to the routing and forwarding tables.
The router consults the forwarding table to get the next hop.

### The Routing Table

Consolidates routes from:

* static routes
* routing protocols
* directly connected routes

Only a single route is selected at the _active route_

> Junos OS supports multiple equal cost routes

The active route from the routing table is used to popualte the **forwarding table**

for each packet forwarded - this is determined:

* outgoing interface
* layer 2 read and write information

The primary routing table `inet.0` stores IPv4 unicast routes
`inet6.0` for IPv6 routing

* `inet.0` - IPV4 unicast 
* `inet.1` - multicast forwarding cache
* `inet.2` - Multicast Border Gateway Protocol (MBGP) for Reverse Path Forwarding (RPF) Checks
* `inet.3` - Multipath Packet Label Switching (MPLS)
* `inet.4` - Multicast Source Discovery Protocol (MSDP)
* `inet.6` - IPV6 Unicast routes
* `mpls.0` - MPLS next hops

### Route Preference

* Differentiate routes from different protocols or sources
* Criterion for selecting active route

Default preference values:

* Direct: 0
* Local: 0
* Static: 5
* OSPF Internal: 10
* RIP: 100
* OSPF AS External: 150
* BGP (iBGP and eBGP): 170


route prefernce can range from: 0 to 4,294,...,...

Eg.

    show route 192.168.36.1 exact

0.0.0.0/0          *[Static/5] 12w2d 12:22:54
                    >  to 192.168.200.1 via ge-1/0/0.200
                    [BGP/170] 12w1d 22:18:44, localpref 200, from 192.168.48.1
                      AS path: I, validation-state: unverified
                    >  to 192.168.200.3 via ge-1/0/0.200, Push 0

Static is `5` whereas `BGP` is `170`

You can modify route preference based on source (excpt direct and local)

> If equal cost paths exist for the same destination - the `rpd` randomly selects the available path (load distribution)

Layer 2 switches do not have forwarding tables

### View Routing table

    show route

* All active routes are marked with `*`
* Each route entry displays the source
* Shows summary of active (for forwarding traffic), holddown (pending state) and hidden routes (routes system cannot use - invalid next hop or route policy)

Can filter for protocol

    show route protocol bgp

### The forwarding table

    show route forwarding-table

Kernel adds some permanent forwarding entries - for example the `default` forwarding - if a packet matches it - the router discards the packet sending a ICMP unreachable

route types:

* `dest` - directly reachable through interface
* `intf` - result of configurating an interface
* `perm` - installed by kernel at init
* `user` - installed by routing protocol

next hop types:

* `bcst` - broadcast
* `dscd` - discard without ICMP
* `hold` - next hop waiting to resolve
* `locl` - local address on an interface
* `mcst` - wire multicast
* `recv` - receive
* `rjct` - reject
* `ucst` - unicast
* `ulst` - list of unicast next hops

### Determining Next Hop

When a packet enters a device running Junos - it compares packet against entries in forwarding table.

* If it is destined to the local device - junOS processes packet locally
* destined to remote device - JunOS forwards to next hop
* if multiple destinations match - the most specific entry (longest match) is used
* If no matching entry exists - a destination unreachable is returned

For example:

    172.19.0.0/16
    172.19.52.0/24
    172.19.52.16/28

The most specific destination to `172.19.52.101` is `172.19.52.0/24`  -check the `Netif` column it must go there.
The most specific to `172.19.52.101` is `172.19.52.16/28`

### Overview of Routing Instances

* Junos OS logically groups routing tables, interfaces and routing protocol paramters to creating routing instances.
* Logic is kept apart.
* A single device can imitate multiple devices.

The Junos OS creates a default routing isntances called `master` containing the `inet.0` routing table.

    show route instance

User defined routing instances

    edit routing-instances

Uses of user defined routing interface

* fitler based forwarding (FBF)
* l2 and l3 VPN
* System virtualisatsion

Routing instance types:

* `forwarding` - filter based forwarding
* `l2vpn` - layer 2 VPN
* `no-forwarding` - seperate large networks into smaller
* `virtual-routers` - non-VPN applications (system virtualisation)
* `vpls` - point to multipoint LAN implementations
* `vrf` - layer 3 VPN implementations

Once the routing instance and device learns routing informations - Junos OS automatically generates a routing table.

Reference the table from a given instance:

    show route table <instance-name>.inet.0

Test from a given instance:

    show interfaces terse routing-instnace <instance-name>

    traceroute 192.168.0.1 routing-instance <instance-name>

### Static Routes

Ideal for small networks

Manually configure the routing information on each router or switch in the network.
All done at `edit routing-options`

* default route for AS (Autonomous System)
* Routes in customer networks

> Must have a valid next hop defined - often the neighboring router headed to ultimate destination

On PPP (Point to point protocol) interfaces you can specify the egress name instead of the ip address

The next hop value is teh bit-bucket (dropping the apcket off the network `rjct` or `dscd`)

By default the next hop must be reachable using a direct route (it does not perform recursive lookups like cisco by default) - static routes remains in the routing table until they are removed or made inactive.
When the ip address used becomes unreachable.

## Configuring Static routes

    [edit routing-options]
    rib inet6.0 {
        static {
            route 0::/0 next-hop 3001::1;
        }
    }
    static {
        route 172.28.102.0/24 {
            next-hop 10.210.11.190;
            no-readvertise;
        }
    }

> `no-readvertise` prevents directing routing out dynamically (on management)

### Monitoring Static Routing

    show route protocol static

Use ping to check reachability

Junos OS needs next hop to be reachable using a direct route by default - no recursive lookups of next hops

    {
        next-hop 172...;
        resolve;
    }

The `resolve` and route to the next hop is also required

    {
        next-hop 172.30.25.1;
        qualified next-hop 172... {
            preference 7;
        }
    }

enables independent preferences - if next hop becomes unreachable - _floating static route_

### Dynamic Routing

* Best for large networks
* Configure network interfaces to participate in routing protocol
* dynamically learning routing

Benefits:

* lower administrative overhead - routes learnt automatically
* increased network availability - reroute failure automatically
* Greater network scalability - dynamically learning routes and best path

IGP (interior Gateway Protocols) - operate within the same autonomous system. (RIP, ISIS and OSPF)
EGP (Exterior gateway protocols) - current EGP used is BGP (operates among different AS's)

### OSPF Protocol

* IGP
* link-state routing protocol within an AS
* LSA (Link State Advertisements)
* LSDB (Link state database) - stores LSA's as records (shortest path determination)
* Dijstra (SPF) - shortest path algorithm
* Each area has a LSDB - backbone area is 0.0.0.0 - all other areas must connect to backbone

Provide connectivity among connected subnets and loopbacks - and no adjascencies are created.

    show ospf neighbor

routes

    show route protocol ospf

> Routes installed as direct routes

### Configuring IPv6

* IPv6 Already enabled
* Must enabled IPv6 packet processing on an interface with `family inet6`
* Automatically configures link-local address (can be overriden)

    [edit interface ge-1/0/0 unit 0]
    set family inet6 address xxxx:xxxx...

    set family inet6 address xxxx:xxxx... eui-64 # automatically generate interface id

* `/64` - multi-access networks
* `/127` - pt-pt links
* `/128` - loopback addresses

### IPv6 Static Routes

* Same as IPv4 static routes
* configured at `[edit routing-options]`
* Specify `rib inet6.0`

### OSPF(v3) for IPv6

* Graceful restart and authentication

### Lab

View route table then show all route tables

> `inet.0` is displayed with `show route`

    show route
    show route all

Configure interfaces and loopbacks

    edit interfaces
    set lo0 family inet address 192.168.1.1/32
    set ge-0/0/1 unit 0 family inet address 172.20.77.1/30
    set ge-0/0/2 unit 0 family inet address 172.20.66.1/30
    set ge-0/0/3 unit 0 family inet address 172.18.1.2/30
    set ge-0/0/4 unit 0 family inet address 172.20.101.1/30

Verify the current state

    show interace terse

Use ping to verify reachability

    ping 172.18.1.1 rapid count 25
    ping 172.20.77.2 rapid count 25
    ping 172.20.66.2 rapid count 25
    ping 172.20.101.10 rapid count 25

Configure ipv6

    edit interfaces
    set lo0 family inet6 address fda9::1/128
    set ge-0/0/1 unit 0 family inet6 address fda1::1/126
    set ge-0/0/2 unit 0 family inet6 address fda2::1/126

Check connectivity

    ping fda9::1 rapid count 25
    ping fda1::1 rapid count 25
    ping fda2::1 rapid count 25

Ensure they are up

    show interface terse

Show securty

    configure
    show security

Set forwarding in packet mode

    edit security
    set forwarding-options family inet6 mode packet-based

Define a static route

    configure
    edit routing-options
    set static-route 0/0 next-hop 172.18.1.1

Run show route

    run show route 172.31.15.1

Check reachability

    run ping 172.31.15.1 rapid count 25

![juniper-static-routes-network-diargram](/img/juniper/juniper_static_routing_diagram.png){: class="img-fluid" }

Add static route to loopback address

    set static route 192.168.1.2/32 next-hop 172.20.101.10













