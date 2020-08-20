---
author: ''
category: Networking
date: '2019-07-27'
summary: ''
title: Find Local Devices Dhcp
---
# Find Local Devices on your Network

1. Find your ip on the network

    en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        ether a8:66:7f:11:12:08 
        inet6 fe80::aa66:7fff:fe11:1208%en0 prefixlen 64 duplicated scopeid 0x4 
        inet 192.168.0.103 netmask 0xffffff00 broadcast 192.168.0.255
        nd6 options=1<PERFORMNUD>
        media: autoselect
        status: active

In this case it is `192.168.0.103`

I think the netmask `ffffff00` means `255.255.255.0`

So our range is `192.168.0.0 - 192.168.0.255`

So that is `256` ip addresses which means a `/24` subnet

2. Use `nmap` to find devices

    $ nmap -sn 192.168.0.0/24

    Starting Nmap 7.40 ( https://nmap.org ) at 2019-07-27 19:49 SAST
    Nmap scan report for 192.168.0.1
    Host is up (0.0017s latency).
    Nmap scan report for 192.168.0.100
    Host is up (0.016s latency).
    Nmap scan report for 192.168.0.103
    Host is up (0.0028s latency).
    Nmap scan report for 192.168.0.104
    Host is up (0.076s latency).
    Nmap scan report for 192.168.0.105
    Host is up (0.076s latency).
    Nmap scan report for 192.168.0.107
    Host is up (0.077s latency).
    Nmap scan report for 192.168.0.114
    Host is up (0.073s latency).
    Nmap done: 256 IP addresses (7 hosts up) scanned in 2.97 seconds

`-sn` means (No port scan)

       -sn (No port scan)
           This option tells Nmap not to do a port scan after host discovery, and only print out the available hosts that responded to the host discovery
           probes. This is often known as a "ping scan", but you can also request that traceroute and NSE host scripts be run. This is by default one step
           more intrusive than the list scan, and can often be used for the same purposes. It allows light reconnaissance of a target network without
           attracting much attention. Knowing how many hosts are up is more valuable to attackers than the list provided by list scan of every single IP
           and host name.

           Systems administrators often find this option valuable as well. It can easily be used to count available machines on a network or monitor server
           availability. This is often called a ping sweep, and is more reliable than pinging the broadcast address because many hosts do not reply to
           broadcast queries.

           The default host discovery done with -sn consists of an ICMP echo request, TCP SYN to port 443, TCP ACK to port 80, and an ICMP timestamp
           request by default. When executed by an unprivileged user, only SYN packets are sent (using a connect call) to ports 80 and 443 on the target.
           When a privileged user tries to scan targets on a local ethernet network, ARP requests are used unless --send-ip was specified. The -sn option
           can be combined with any of the discovery probe types (the -P* options, excluding -Pn) for greater flexibility. If any of those probe type and
           port number options are used, the default probes are overridden. When strict firewalls are in place between the source host running Nmap and the
           target network, using those advanced techniques is recommended. Otherwise hosts could be missed when the firewall drops probes or their
           responses.

## Sources

* [Find devices connected to your network with nmap](https://vitux.com/find-devices-connected-to-your-network-with-nmap/)