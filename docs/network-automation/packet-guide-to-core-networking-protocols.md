---
author: ''
category: Network-Automation
date: '2020-07-07'
summary: ''
title: Packet Guide To Core Networking Protocols
---
# Packet Guide to Core Network Protocols

* Many books are too focused on a single technology or too broad
* Network basic building blocks: routers, switches, access points and hosts
* These building blocks have a set of rules when forwarding bets of info to eachother
* Bits are wrapped in neat packages called **packets**
* If a packet is present, it is there because some device or network host put it there

# 1. Networking Models

Architectures are based on a model showing how protocols and functions fit together

Historical models:

* Systems Network Architecture (SNA-IBM)
* Appletalk
* Novell Netware (IPX/SPX)
* Open System Interconnection (OSI)

These have gone away due to the popularity of `TCP/IP`

> TCP/IP stands for Transmission Control Protocol / Internet Protocol

This is the language of the internet

## What is a Model?

* Organisation of functions and features to define its structural design
* Compared to a postal system: each part has its own rules to obey but ultimately are there to deliver mail
* The job of each device is determined by the hierachy or layer it is on
* An email application on user pc should not be responsible for choosing the encoding sequence and signal type between client and server
* The Network Interface Card (NIC) is not in the business of message header construction
* Each layer has a function to perform and protocols associated with each layer
* The protocols are collectively known as the _protocol suite_
* Lower layers are linked with hardware and upper layers are linked with software
* HTTP (Hypertext Transfer Protocol) -> TCP (Transmission Control Protocol) -> IP (Internet Protocol) -> Ethernet II

## Why use a Model?

* Even a simple communication system is a complicated environment
* Interconnected systems are considerably more complex
Models provide the starting point for determining what what needs to be done to enable communication or how systems might connect to each other.
* If different systems used a different set of models and protocols programming and maintaining the communcation between them becomes difficult

> One would not start looking at the routing protocols if teh link light was dark

## OSI Model

* A Reference Model
* A method to compare standards and protocols for connectivity and consistency
* Is standardised in ISO/IEC (International Standards Organisation/International Electrotechnical Commission)
* Craeted in collaboration with ITU-T (International Telecommunications Union)

ISO/SEC 7498:
1. The Basic model
2. Security Architecture
3. Naming and Addressing
4. Management Framework

### The Basic Model

Has seven Layers:

* Application
* Presentation
* Session
* Transport
* Network
* Data Link
* Physical

> An open system is one that adheres to this architecture

Goal is to improve standards, flexibility and openness (mutually accepted standards for info exchange)

#### Application Layer (Layer 7)

* sole access to OSI environment
* Connection mode: has Qos (Quality of Service), Security, identification, mode of dialog and error control
* Connectionless has all the above except error control and some security

#### Presentation Layer (Layer 6)

* Representaiton and preservation of data provided by the application layer
* Focused on syntax for layers above and below

#### Session Layer (Layer 5)

* Full duplex and half-duplex modes
* The means (setup and teardown) of communicating nodes to synchronise and manage data between them
* Mapping is provided between the transport layer and session layer
* mainly connection-oriented transmission

#### Transport Layer (Layer 4)

* End-to-end between OSI nodes
* deal with low cost and reliable data transfer
* transport connectoin establishment, release, data transfer and Qos
* **Not responsible for routing**, but does map to network layer addressing
* Handle error control

#### Network Layer (Layer 3)

* Means for managing network connections between open systems
* Negotiates Qos settings
* Focusses on routing between networks and subnetworks
* Network layer addresses uniquely identify transport entities

#### Data Link Layer (Layer 2)

* Reponsible for conneciton of data link between network layer entities
* Addresses are unique within the open system set of devices

#### Physical Layer (Layer 1)

* Electrical, mechanical and functional means to establish connection between layer-2 devices

### OSI Beyond Layers

* Communication between peer entities
    * modes of communication
    * relationship between services provided at each adjacent layer boundary
    * Mode conversion funcions (transport and network layers)
* Identifiers (N-Addresses) - unambiguous names to identify access points at a particular layer
* Properties of service access points
* Definitions and descriptions of data units
* Elements of layer operation:
    * Connections to and from
    * Multiplexing
    * Flow Control
    * Segmenation
    * Sequencing
    * Acknowledgement
    * Protocol Selection
    * Negotiation mechanisms
    * Connection establishment and release
    * Quality of service
    * Error Detection

### OSU/ITU-T Protocols

* Guidelines for developing protocols

Interesting that the 2 layer 4 protocols used today: TCP (Tranmission Control Protocol) and UDP (User Datagram Protocol) are differentiated from each other in the exact same way.
* UDP - Connectionless, not concerned if packets arrive or not
* TCP - Connection oriented, concerned that packets arrive at destination

Practically OSI/ITU-T Protocols are not seen as often as the TCP/IP model, although VoIP still uses it.

## Introducting TCP/IP

* The Language of the Internet
* Applications are built around this protocol suite
* At Layer 4 there are 2 protocls both UDP and TCP but the model shares its name with the later.
* Layers 1 and 2 are government by the Local Area Network Protocol
* Layer 3 belongs to IP with ICMP (Internet Control Message Protocol) and IGMP (Internt Group Membershp Protocol)

Historically networks have been built on many technologies: FDDI (Fibre Distributed Data interface), Localtalk, Token ring, Ethernet and Wireless protocols like 802.11. Today **only Ethernet and 802.11** have survived

In a typical network, decision from layers 1 - 4 are made for you and the variation is the applciations you choose to deploy.

The dominance of TCP/IP can be seen in Wireshark
* Almost 100% of layer 3 traffic is IPv4 (a small amount IPv6)
* At layer 4: TCP and UDP dominate. ARP and 802.1x contribute.

The TCP/IP model layers do not seperate apllication, pesentation and session; they are merged into a single layer called **application layer**

TCP Model:
1. Physical layer
2. Link/Network Layer
3. Internetwork layer
4. Transport layer
5. Application layer

## TCP/IP and RFC's

**Major requirements** of each layer according to TCP/IP RFC's

#### Application Layer

* Support flexible hostnames
* Map domain names appropriately
* Handle DNS Errors
* More specific requirements: Telnet, FTP, SMTP, DNS

#### Transport Layer

* End-to-end communication based on TCP or UDP
* Pass IP and ICMP to the application layer
* Handle and manipulate checksums
* Support IP addresses, local and wildcard
* etc

#### Internet Layer

IP, ICMP and IGMP

* Handle remote multihoming
* Meet gateway specification
* Discard improper IP and ICMP packets
* Maintain packet IDs

#### Link Layer

Network interface, framing and media access

* Clear ARP cache
* Prevent ARP floods
* Receive IP Tos values

#### Physical Layer

The network interface cardor port

### The Practical Side of TCP/IP

From a typical wireshark packet:

* `Ethernet II` as a protocol exists on layers 1 and 2. Layer 2 defines the frame )error control and addressing) and Ethernet network interface defining the physical layer characteristics.
* Layer 2 LAN is either logical link control (LLC) or media access control (mac) - sublayers.
    * LLC - frame contruction, error control and addressing
    * MAC - line discipline and network transmission (which node can communicate and for how long)

### Encapsulation

How layers interact and pass information up and down
On a sending node the places packaging around a message describing it - the header.
Each layer does its own encapsulation, by the time it reaches the bottom of the protocol stack it has several of these wrappers.

The receiving node does the same process but in reverse. Stripping off layer by layer.
**de-encapsulation**

* Ethernet uses the code 0800 to indicate that IP is encapsulated
* IP uses code 17 to show that it has UDP encapsulated
* UDP uses port numbers to direct rhe data to the proper process or application

### Addressing

* Some protocols require addresses as part of their basic operation
* Eg. an ethernet switch processes layer-2 frames which contain MAC addresses.
* The IP protocol uses IP addresses (at layer 3)
* Both TCP and UDP communicate via port numbers to the application

If port scanning is done on layer 4 then the solution is probably not going to be found at layer 2

### Equipment

* Each device has a specific task
* Applying layers to equipment the capabilities and traffic on a device is easier to understand
* **Routers and switches** form the building blocks of almost any network
* **They all provide the same basic services when you plug them in, regardless of the vendor**.
* Switches oeprate at level 2 and forward LAN frames based on MAC addresses in those frames, they also perform error checking on each frame and provide network segmentation through network traffic control from MAC addresses.
* Switches use SNMP (Simple Network Management Protocol) and VLAN's (Virtual Local Area Networks)
* Routers process IP packets with the main function to get IP packets to the proper destination
* The router checks Qos and fragmentation information
* Many routers support firewalling, virtual private networks terminati, authentication and Network Address Translation (NAT)
* The term gateway has several meanings
* Routers and network hosts are configured with a default gateway - but this is actually a router
* It is called a default gateway because this is the network path to the rest of the world
* The traditional gateway on layer 4 are used to convert between systems that do not share the same networking model
* With VoIP the gateway is making a comeback - a gateway is required for a TCP/IP and SS7 (signaling system 7) to communicate with a regular telephone.
* An _access point_ is sometimes referred to as a wireless hub because it broadcasts certain kidnds of traffic everywhere. However it (like an ethernet switch) uses MAC addresses to make forwarding decisions.
* Multi-layer switching has blurred the line between processing frames at Layer 2 and higher level functions like routing

#### Layers vs Equipment

* Application layer  = N/A (Device)  = N/A (Addressing)
* Transport layer    = Gateway       = TCP/UDP Ports
* Internet layer     = Router        = IP Addresses
* Link/Network layer = Switch        = MAC Addresses
* Physical layer     = Hub           = Bits

# 2. Ethernet

> Computers cabled together in a network are almost certainly going to be connected via ethernet

It is the technology describing the rules used i ncommunication between LAN-based systems and is considered Layer 2.

It is ubiquitous and has forced desktop and laptop products to include ethernet cables

* shared communication
* broadcast packet switching
* extension vie repeaters
* distributed control for packet transmission
* controlled behaviour in instance of interference or collisions
* aggregation
* multiple speeds
* full/half duplex operation

## The model

* Governs the physical and network layers
* Layer 2 is subdivided into LLC(Logical Link control) and MAC (media access control)
* MAC sublayer detects the carrier, transmits and receives the media and passes the frame to/from the LLC sub layer

> A DHCP packet is encapsulated in UDP then IP. The packet is then placed in a LAN frame.

## Structure

An ethernet frame contains:

* Preamble (8 bytes) - provide timing (invisible to packet analysers)
* Destination MAC Address (6 bytes) - when transmitting outside the local network the default gateway is placed in the destination field
* Source MAC Address (6 bytes)
* Control (2 bytes) - hex: 0x0800 indicates IPv4, 0x0806 indicates ARP (Address resolution protocol), 0x06DD is IPv6
* Data (46 - 1500 bytes) - higher layers of the protocol (payload)
* FCS (4 bytes) - used for error checking, only error detection not correction, the CRC calculation is done when it is created and anything receiving the frame also calculates it.

## Ethernet Type II vs 802.3

* Network Interface Cards (NIC) know these 2 variations exist
* Ethernet type II is used for IP based packets
* IEEE 802.3 is used for management protocols such as spanning tree

More on 802.3 frame in the book

## Mac Addresses

Mac Addresses:

* three-byte vendor code
* three-byte host id

Eg. 00:09:11:2a:b8:00 
* 00:09:11 is the vendor code (cisco)
* 2a:b8:00 is the host id


* Unicast MAC Address - assigned to single nodes and first byte is always 00 (source address is always a unicast address)
* Broadcast frames are sent by a single node to everyone on the local network (always ff which is 255 in base 10) - read by all nodes and forwarded everywhere by layer-2 networking equipment - switches will forward to every port, routers will not forward broadcast frames
* Routers are the boundary of the broadcast domain - stated another way no network other than your own will ever see the MAC addresses on your network
* Multicast frames are created by a single host but destined for a subset of the entire network (have 01 as the first byte of the MAC address)
* For example sending to a specific vendor code.

## Ethernet Operations

How do you know:

* What is the correct destination for the transmission?
* How fast or slow you were supposed to send the data
* How would you decide which computers had permission to speak / transmit?

1. Ethernet uses MAC addresses to identify source and destination
2. data rate is a function of the Network interface card usually capable of 2 or 3 speeds (10Mbps, 100 Mbps or 1Gbps) so either the NIC neogtiates the rate or will use the frame's preamble to sync the incoming connection
3. The medium must be clear for transmission, handled with CSMA/CD along with a truncated binary exponential random backoff algorithm. - Geez

First the node will listen for other transmissions, hearing None it will begin its own transmission. If the line is not clear the node waits for the transmission to complete then sends its own frame

## Shared Media

Early ethernet operated on a bus topology meaning every node on the network can hear what you transmitted and vice versa

* 10Base5 and 10Base2 - connected nodes with coavial cables into the central shared conductor
* 10Base-T - dropped coaxial and used Unshielded Twisted Pair (UTP), still a bus
* 

> Ethernet collisions are just like vehicle collisions...bad. The two nodes involved must back off and try again later.

To detect collisions we have rules that govern the frame size, bit rate and maximum network diameter.

Nodes capable of detecting a collision is a member of the same _collision domain_
Hubs will forward collisions but switches and routers will not

More stuff like this in the book...

## Physical Layer

The physical layer is the voltage levels, encoding schemes and connectors
Connectors are almost always RJ45 terminations for UTP

### Cabling

UTP is the most common network media type and is used for VoIP phones, token ring, FDDI, Ethernet and many others.
R45J is the standard Jack

A whole lot of info on cabling...which is beyond me for now

### Encoding

#### 10Base-T

* Connector type and media: RJ45, UTP
* Encoding: Manchester

#### 100Base-T

* Cennector type and media: RJ45, UTP
* Encoding: NRZI

#### 1000Base-T

* connector type and media: RJ45, UTP
* Encoding: 4D, five-level Pulse Amplitude Modulation (PAM5)

Other types of signaling and topologies are discussed in the book...

## Final Thoughts on Ethernet

* Anyone can build an Ethernet network
* Most configuration is made without configuration from us
* Most network admins can just take a switch out the box and the network works instantly
* The real work is trying to understand what is hppening when things go wrong - optimising performance or improving security

# 3. Internet Protocol

* The language of the internet
* "Best Effort" - very little in the way of connection or error control
* All applications running on the network have 1 thing in common they all use IP

## protocol description

> Protocol for transmitting blocks of data called datagrams from source to destination

* Today packets and datagrams are used interchangeably
* Device responsible for getting packets to the correct destination is the router

## Structure

* IP packets are encapsulated in any layer-2 protocol running
* Most commonly Ethernet or 802.11
* Ethernet header -> IP header -> IP packet payload

IP Packet:

* Version - IPv4 or IPv6
* Header Length - Number of 4 byte words at the beginning of the IP packet
* ToS (Type of Service) - indicates priority, delay, throughput, reliability
* Total Length - size of the data in bytes (max IP packet is 65535 bytes)
* Identification - to aid reassemly of packets
* Flags - How packet fragmentation is to be handled
* Fragment offset - determines fragment position when assembling again
* Time to live - protection from routing loops and remove continuously circulating datagrams the TTL is used (number of hops it can make - each device subtracts 1)
* Protocol - eight-bit field specifying what is being carried [0x01 - ICMP, 0x11 - (17) UDP, 0x06 (6 - TCP)]
* Header checksum
* Source and destinatino IP addresses
* Options 

## Addressing

* IP address are written in dotted quad four-byte addressing
* Eg. 192.168.15.103
* Each IP address has a network portion and a host portion determined by the mask

The network ID must be calculated because it makes forwarding decisions for hosts and routers based on the network ID

Reserved IP addresses:

* 0.0.0.0 : All zeroes, used for DHCP to obtain a working IP address
* 129.21.0.0: Network portion all zeroes, specifies a particular network
* 129.21.255.255: Network portio all ones, broadcast packet to a particular network
* 255.255.255.255: All ones, limited boradcast to current network
* 127.x.x.x: loopback, used for testing and identifying localhost

Also: 192.168.1.1, an IP used for network address translation

Also: 169.254.0.0 - 169.254.255.255: IETF Zero confirugation standard, used for networks in the absense of DNS and DHCP.

## Sample Host Configuration

Requied numbers:

* IP Address
* mask
* default gateway (router)
* DNS

These values are mostly acquired from a DHCP server

## Operation

They no little about the pathway to the endpoint, error control and nothing to ensure delivery.

> The internet protocol treats each internet datagram as an independent wntity unrelated to any other internet datagream, There are no connections or logical circuits.

The key is that all routers and hosts follow the same set of rules.
Amazingly they are run by humans who typically do not follow the rules.

1. When a host initiates a communication via an application some data is inserted into a TCP or UDP datagram
2. This datagram is placed inside an IP packet
3. The IP packet is created after examing the host routing table - determine if sending to node in local network or outside
4. Packets destined for local  network go via local forwarding on MAC addresses and ARP (ARP maps IP addresses to MAC Addresess)
5. Header checksums calculated and sent
6. If the packet is snt off the current network the packet must be routed via the host's default gateway. A router interface reachable by the host - packets are sent to the local router for forwarding to the next router

The router's routing table contains information about other networks (not the local)

## Security Warning

* It is easy to change your ip to match a target - called spoofing an address
* It is used to pass your system off as a valid node - bypassing security
* The IP header is almost always clear text, even in a system deploying VPN's - IPsec, SSL or the elderly PPTP
* There is no distinction between good traffic and bad traffic.

## Assigning Names and Addresses

IANA (Internet Assigned Numbers Authority):

* Responsible for DNS - root zone, .int and .arpa
* IP addreses
* maintaining codes and numbers

IANA is operated by ICANN (Inernet Corporation for Assigned Names and Numbers) - which is a nonprofit partnership that organises the public IP address space for the entire world.

# 4. Address Resolution Protocol

## The Problem

* The vast majority of IP packket-based data transmission begins and ends on a LAN
* With ethernet the sender's MAC address and IP address is the source for layer 2 and layer 3 respectively.
* The destination IP address is usually known, so what is the destination MAC address.

## Techniques

Methods for destination MAC address:

* table lookup
* closed-form computation
* message exchange

### Closed-form Computation

* Calculates the unknown MAC address from the known IP address
* Quick and does not require outside resources or communication
* Requires configurable MAC addresses and some level of management as all addresses need to be assigned a host

### Table Lookup

* Provides each host with a list of MAC addresses and corresponding IP addresses
* Very fast, sender needs to check the table before building the ethernet frame

### Message exchange

* Requires much less heavy management oversight
* Uses ARP (Address resolution protocol)
* Adds extra traffic and is slower than the other methods
* Completely automated - attractive

## Protocol Description

* ARP request and ARP reply
* An ARP asks for the MAC addresss, the hosts never say no if they can help it

## Structure

ARP request:

* Hardware type - type of MAC address sought
* Protocol type - Layer-3 protocol in use
* Hardware size - Length of the MAC address
* Protocol size - length of the protocol address
* OpCode - type of ARP message - request or reply
* Sender MAC Address
* Sender IP address
* Target MAX address
* Target IP Address

## Addressing in the ARP Request

ARP Request destination MAC address is a broadcast address, ensuring all nodes pay attention - so if the node asked for is powered up it responds
ARP messages are not routable and routers will not pass ARP traffic on ot another network
Therefore the MAC address of a node not on the source node's LAN cannot be determined

The ARP (0x0806) lacks an IP header

## Addressing in the ARP reply

Sender and target addresses are reversed
Instead of broadcast destination, both MAC addresses are now unicast

Upon receiving the reply:
1. The data frame is built using the newly determined MAC address
2. Populate the local ARP table

    $ arp -a
    ? (192.168.0.1) at d4:6e:e:87:a8:8a on en0 ifscope [ethernet]
    ? (192.168.0.101) at 78:32:1b:ac:8d:5b on en0 ifscope [ethernet]
    ? (192.168.0.123) at 94:53:30:46:aa:3c on en0 ifscope [ethernet]
    ? (192.168.0.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
    ? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
    broadcasthost (255.255.255.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]

* Dynamic ARP table entry means it is not permanent
* Most operating systems remove these entries in the matter of minutes

## Operation

1. Sender and Target on same LAN

* ping target IP as proof of life - sends a ICMP echo request encapsulated in an IP packet, encapsulated in an ethernet frame
* Same ARP would have been needed with Telnet, FTP or HTTP

2. Semder and Target on Seperate LAN's

* The destination node is on a remote LAN
* Since Layer-2 MAC addressing is restricted to the local network, assistance is required from the designated **default gateway** that will route the frame to the destination network.
* Router ARP behaviour is similar to that of the hosts
* In this case the MAC address for the degault gateway is used but the IP address for the distant node

## Additional Operations

### The Return ARP

* Routers are aggressive and will generate their own ARP requests to populate their tables
* Increases routing efficiency

### Gratuitous ARP

* When a host boots up it either receives an IP address via DHCP or has one statically configured.
* But it needs to ensure no other network node is uding the same address - so it ARP's itself.
* If a device answers, the sender is alerted - it knows there is a device with the same IP.

## Security Warning

* Hosts should only populate their tables with information they have requested
* Older stuff received unsolicited ARP traffic to fill the host's cache
* Allowing attackers to add bogus data
* An attacker could also provide an answer for every address on the network
* So all network traffic goes through the attacked - a man-in-the-middle attack
* Inserting bad data into the Host ARP tables is called ARP poisoning
* Multiple entries in ARP tables will expose

## IPv6

* ARP is absent in IPv6. Instead networks hosts use a series of messages called redirects, solicitations and 
advertisements in a process called neighbour discovery
* It tries to disvocer network info before it is needed

## Summary

* ARP can add alot of traffic to the network
* The beginning of a work day can be a problem with all hosts concurrently discovering
* The routers and next hop routers also need to do ARP discovery
* IPv6 also sends multicast messages

# 5. Network Equipment

* Hubs (repeaters), switches (bridges), routers, access points (AP's) and gateways
* New equipment can cross layer boundaries

## Tables and Hosts

* Nodes have IP and MAC addresses
* Devices use these addresses to forward packets or frames
* Everything in a network follows a step-by-step process

Hub - physical layer (layer 1) - Ethernet, 802.11 [Bits]
Switch - physical layer and link/network layer (layer 2) - Ethernet, 802.11 [Frame]
Router - physical, link and internetwork layer (layer 2) - IP [Packet]


* ARP table [on router and host] - Maps IP addresses to MAC addresses
* Source address table [on switch] - Maps MAC addresses to switch ports
* Routing table [router and host] - Determines correct interface and next hop
* AP Forwarding database [access point] - collection nodes managed by the AP

Process of a Node A sending data to Node B:
1. Node A checks host routing table to determine if packet is destined for the local network
2. Node A builds a frame for Layer-2 destination by pulling the proper MAC address from its ARP table
3. Frame is sent from Node A to router via a switch
4. Switch A consults its source address table (SAT) to determine the proper port for the destination
5. Router A received the switch and examines the IP header to determine the destination network
6. Router processes its routing table to determine the correct interface for the the destination
7. Router builds a frame for the Layer-2 destination by using its ARP table or sending an ARP request
8. Frame is sent from router to Node B via Switch B
9. Switch B consults its SAT to determine the destination
10. The Access point receives the frame and checks for node B in its forwarding database and sends the frame out to the wireless network to Node B

All network transmission follows a similar process

## Hubs or Repeaters

> Repeating - the means used to connect segments of the network medium together, thus allowing larger topologies and a larger MAU base than the rules governing individual segments

* Signal degrades over distance
* A repeater is a point where the signal is cleaned and retransmitted

> Hubs perform the basic functions of restoring signal amplitude and timing, collision detection and notification and signal broadcast to lower level hubs and DTE's

A DTE is Data Terminal Equipment - devices generating or terminating transmissions (in this case nodes)

In reality:
1. You don't buy repeaters anymore, you buy hubs (hubs are thought as multiport repeaters)
2. We don't like to buy hubs

> Hubs do not possess a great deal of intelligence

Hubs forward traffic out all ports except the source, any transmission is sent to anyone connected to the same collision domain. Making it a **security concern**.

Positively hubs are very fast, they will outperform a switch in some scenarios. But as the number of nodes increases you start getting collisions which destroys performance.

> Hubs do not _scale_ well

This is why hubs have been replaced with switches

## Switches and Bridges

> Switches are the workhorses of the modern network

* Switches are used to extend the network and add more nodes
* Collisions on switches are not allowed to propagate
* They also filter out traffic that should not be forwarded
* Switches are considered newer, high-powered versions of bridges


Features of switches (that hubs and early bridges do not possess):

* Changes to forwarding behaviour
* Support for Virtual LAN's (VLAN's)
* Basic port security
* 802.1x

A switch forwards based on MAC addresses (a hub just forwards to everywhere except the source)
To do this a switch consults a SAT - Source address table - before sending a frame to the destination
A significant portion of traffic only goes to the proper destination

How do switches work:

* receive a frame, read addresses, error check and forward to the correct port
* Switches keep track of nodes with a SAT - source address table
* Each node in a network has a unique MAC address and each ethernet frame has a source and destination MAC address

Switch procedure:
1. Frame received: buffer the frame and perform the frame error check - discard the frames if there are problems
2. Copy the cource address and port number into the SAT
3. Look in the SAT for the destination MAC address
4. If address is known, forward to the correct port. If the address is not known, send the frame everyhwere except the source port (called _flooding_)
5. If the destination is a broadcast address (ff:ff:ff:ff:ff:ff) send the frame everywhere except the source

> Switches will continue forwarding broadcast frames until it reaches a layer-3 boundary (a router)

A switch is _transparent_ because it learns which ports are assigned to which MAC address
Allowing a switch to filter network traffic, prevent errors and stop the propagation of collisions

Switches read ethernet frames but do not change them in any way

## Access Points

Often called wireless hubs, because the medium is shared.
Ap's broadcast traddic to anyone capable of hearing it (just like hubs)

What is an Access Point supposed to do:

* Notify network users of its presence and negotiate connections
* Forward traffic between wired and wireless sections of the network
* Handling traffic for all of the wireless nodes currently connected
* Encrypting data traffic
* Handling nodes in opwer save mode


Nodes connecting to a wireless network:
1. Network is found with an active or passive scan
2. Node must authenticate with the network
3. Node is associated with the network

Actually a node associates with an Access Point possessng the service set identifier (SSID) for thedesired network

* An AP will not foreward traffic for nonassociated nodes
* An 802.11 dataframe contains a destination MAC, source MAC and BSSID
* The destination and source MAC addresses are the same as an ethernet frame.
* The BSSID is the MAC address of the Access Point, allowing the access point to determine which frames to process

* 802.11 frames are larger and have more control fields
* That is why an AP is a network device that must modify the Layer-2 Frame
* Like a switch an AP does not care about layer-3 addresses or headers

## Routers

> Routers live in Layer 3 and cares about layer 3 addesses

Routers will forward traffic between IP based networks after ecaming the layer-3 header

* Routers require IP addresses in order to operate - switches and AP's do not
* They use and respond to ARP messages
* They listen to but will not forward all broadcast frames
* A router not only forwards traffic for hosts, it can be contacted directly
* Also known as _default gateway_
* The router will receive transmission from the network nodes when sending traffic offsite
* Routers change Layer-2 frames

Operations on a router:

* Routing process - movement of IP packets from one port to another
* Routing protocols - RIP / OSPF are used to communicate with other routers
* Routing table - holds information used by the routing process

## Another Gateway

A _gateway_ unlike a router or default gateway, refers to a device that understands and converts between two different networking models: eg: IPX/SPX and TXP/IP and appletalk networks together.

## Multilayer switches and home gateways

Single use switches and routers are also fading away

* A single device will do both routing and switching
* A single device can route between VLAN's

A topolgy can be built with less network devices, less power outets, less network ports and use less cooling

A home gateway consists of:

* four switch ports
* a wireless interface
* DHCP server
* router
* NAT - Network Address Translation
* Firewall

## Security

* A layer-1 hub operate in a shared medi and do not filter traffic
* A layer-2 switch filter traffic based on the MAC address but they are willing to forward broadcast frames everywhere - an attacked can eavesdrop
* Wireless security (WEP and WPA-PSK) have been cracked. WPA2-PSK should be used
* Routers provide the greatest inherent filtering and will not forward anything unless the packets are destined for another network - but routers have IP address and can be connected to the outside world

# Internet Control Message Protocol (ICMP)

* ICMP provides error messages and feedback during network operations
* They give insight into the current state of the network and make it simpler to  troubleshoot connectivity problems
* Ask for network information
* Exists within Layer 3 (Internetwork layer) - in a TCP/IP datagrame
* ICMP error messages are not created about other ICMP error messages and only the first of a fragment
* No security as messages are clear text
* Most devices repsond to ICMP requests without hesitation

## Structure

* No TCP or UDP header
* Payload type / protocol: 01

### Type

* 0 - Echo reply
* 3 - DEstinatino unreachable
* 4 - Source quench
* 5 - Redirect
* 8 - Echo request (ping)
* 9 - Router Advertisement
* 10 - Router solicitation message
* 11 - Time exceeded
* 12 - Parameter problem
* 13 - Timestamp
* 14 - Timestamp reply
* 15 - Information request
* 16 - Information reply

* code
* checksum
* identifier - reference for matching echo reply
* sequence number - matching requests and replies
* internet header + 64 bits of data datagrame - response contains copy of original IP header
* payload - data from the ICMP process

## Operations and Types

### Echo Request (Type 0) and Echo Reply (Type 8)

* ping
* responder function
* Entire conversation includes: ARP request, ARP reply, ICMP echo requests and corresponding echo replies
* Whatever is sent is returned (WIth windows characters a to w are sent in hex)

### Redirect (Type 5)

* Inform a host their is a better path to the destination than the one already tried

Pretty complicated

### Time to Live Exceeded (Type 11)

* A TTL (Time to live) is the number of hops or router interfaces the packet is permitted to traverse before it is removed from the network
* An ICMP "time to live exceeded" message is generated indicating the packet was dropped
* Type 11
* Help to identify loops in topologies
* A common example is when neighnouring routers are configured with each other as the forwarding router
* A less obvious rpbolem is a link or route going down resulting in a path being removed from a routing table

#### Tracing a route

* You can use time exceeded messages for diagnostic purposes
* With path discovery programs: Tracert (traceroute for linux and cisco)
* the TTL is incremented by 1 in subsequent packets

### Destination Unreachable (Type 3)

* Tells a source host that the path to a destinatino is unknown
* Common when a router does not have a default route - gateway of last resort
* It will not be able to forward traffic to any network not configured via directly connected, static or dynamic routes
* When a default gateway is not configured the operating system returns "destinatino unrachable"

#### Codes

* 0 - Net unrachable
* 1 - Host unreachable
* 2 - Protocol unreachable
* 3 - Port unreachable
* 4 - Fragmentation needed and DF
* 5 - Source route failed

A router or firewall can generate type 3 with a code of 13, which means that the packet has been administratively filtered or actively blocked

The operating system without a default gateway set will return:

    Destination host unreachable
    
The operating system with a default gateway set but host can't be found:

    Replying from 192.168.3.253: Destination host unreachable

### Router Solicitation (Type 10) and Router Advertisements (Type 9)

* Not as common as they have been supplanted by the DHCP (Dynamic host configuration protocol)
* They are used to request or provice information regarding routers on the LAN
* If a host has an IP address but does not have a default gateway it can ask the network for an answer by sending an ICMP router solicitation
* Some routers periodically advertise themselves
* Router solicitationa nd advertisements are still useful in wireless applications
* A mobile device is not assigned an IP address when it arrives, instead in contacts a device called a _foreign agent_ found via this type of ICMP message

## IPv6

* IP _next header_ changes from a value of 1 to a value of 58

Types:

* Type 1 - Destinatino unreachable
* Type 2 - packet too big
* Type 3 - Time exceeded
* Type 4 - Parameter problem
* Type 128 - Echo request
* Type 129 - Echo reply

* IPv6 Nodes take a very active role in learning about their local topology
* ARP is not a part of IPv6

## Summary

Most common:

* Echo request and reply
* Time exceeded
* Destination unreachable
* redirect messages

# 7. Subnetting and Other Masking Acrobatics

* A network is a group of nodes that all share the same IP addressing scheme

A device requires the following for connectivity:

* IP address - logical location
* network mask - determines the network
* gateway - router providing a pathway off the current network
* DNS address - converts huamsn friendly addresses to IP addresses

## How do we use the Mask?

3 classes

#### A Class

Address range: 0 - 127
Mask: 255.0.0.0
Possible networks: 128
Number of possible hosts: 16777216

#### B Class

Address range: 128-191
Mask: 255.255.0.0
Possible networks: 16364
Number of possible hosts: 65536

#### C Class

Address range: 192 - 223
Mask: 255.255.255.0
Possible networks: 2097152
Number of possible hosts: 256

* Generally a network can be identified by its IP address and corresponding mask

Smaller organisations are given a class C network
Larger ones are given a class A or B

Take a host with IP address: 200.150.100.95 and a mask of 255.255.255.0

1. Convert the host address to binary

    11001000.10010110.01100100.01011111
    
2. Convert the mask to binary

    11111111.11111111.11111111.00000000
    
3. Perform a bitwise AND to get the network address

    1100100.10010110.01100100.00000000
    
4. Convert back to base 10

    200.150.100.0

* This is the network address
* Hosts are no assigned this address

In a network mask the ones (1) represent the network portion, zeroes (0) indicate the host portion

Counting the number of bits (1's) show class A networks have 8-bit masks, class B have 16-bit masks and class C have 24-bit masks


loopback (itsself): 127.x.x.x
200.150.100.255: directed broadcast address - to  reach all hosts on a network

Hosts in this network (computer, routers, printers) will all use addresses between 200.150.100.1 and 200.150.100.254

## What is a subnet?

work exactly like classful networks in that they require a router to get to other networks and have a netwrok address, a directed broadcast address and a specific set of hosts.

> Logically visible subsections of a single internet network

Used to seperate departments or interconnect different LAN technologies

The address space of 0 - 255 given by the classful network need to be further broken down.

The mask now has a subnet field in addition to the network and host portions

Bits are stolen from the host address space equal to the number of subnets required

Weird calcualtions follow in the book...stealing successive bits?

### Subnet Patterns

* The number of subnets and the numbe rof hosts will always be a power of 2

### Shorthand Technique

You are given the classful address space 200.150.100.0 and 255.255.255.0, and musdt divide the network into 4 equal parts.

256 / 4 = 64

Start counting at 0:

200.150.100.0 - 63
200.150.100.64 - 127
200.150.100.128 - 191
200.150.100.192 - 255

### Effect on address space

* each subnet also needs an address for the router, the network itself and the brodcast address.
* So creating 4 subnets, loses 8 addresses.

Masks are not present in packets traveling on the network - that is why network admins are advised to refrain from using subnets that include all 1 and all 0 subnets.

Eg:

200.150.100.0 - 200.150.100.31: Not allowed
200.150.100.224 - 200.150.100.255: Not allowed

## Supernetting

* Combines chunks of address space together
* A large number of nodes may be grouped together because they are not simultaneously active, network load is small or out of a derire for route aggregation

Instead of hosts stolen from the hosts portion, bits are stolen from the network portion

* Supernetting increases the size of the network in terms of the number of hosts

More calcuation related stuff in the book

## Classless Inter-domain Routing (CIDR)

* Classful addressing did not have much of a future, as the number of network attached to the internet passed 10000 it became apparent every organisation wanted its own network.
* It wouldn't take long to run out of possible network addresses
* The entire IPv4 address space would be used up as it is 32bit
* It was inefficient as well as an organisaiton with 300 nodes would be given a class B network - supernetting helped that
* Every small home network should not be granted its own network - it is not possible
* Routing tables would grow until performance for routers on interconnected networks was severly hampered
* It takes time to construct and maintain a routing table
* 

Aggregation is a technique which reduces the number of routing table entries that can be used to forward traffic to downstream routers

...Alot of this stuff flew over my head













