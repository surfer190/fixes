---
author: ''
category: OpenWRT
date: '2022-02-03'
summary: ''
title: Openwrt Userguide Notes
---
# Openwrt Userguide Notes

## Base Config

The Luci Interface can be accessed at `http://192.168.1.1/` or `http://openwrt.lan/`

## CLI

You can `ssh` onto the device - telnet is disabled.

    ssh root@192.168.1.1

Info on [Using the CLI](https://openwrt.org/docs/guide-user/base-system/user.beginner.cli)

## DNS and DHCP configuration /etc/config/dhcp

OpenWrt uses `dnsmasq` and `odhcpd` to serve DNS/DHCP and DHCPv6 by default.

> Dnsmasq serves as a downstream caching DNS server advertising itself to DHCP clients. This allows better performance and management of DNS functionality on your local network. Every received DNS query not currently in cache is forwarded to the upstream DNS servers.

There are alot of [dhcp options](https://openwrt.org/docs/guide-user/base-system/dhcp)

## Dropbear 

Dropbear is a replacement of OpenSSH for embedded devices with low memory etc

## Network basics /etc/config/network

[Basic and Advanced CLI Network setup](https://openwrt.org/docs/guide-user/base-system/basic-networking)

## Luci Interface

### Installing luci-app-statistics

    opkg update
    opkg install luci-app-statistics
    opkg list | grep collectd-mod
    opkg install collectd-mod-ethstat collectd-mod-ipstatistics collectd-mod-irq collectd-mod-load collectd-mod-ping collectd-mod-powerdns collectd-mod-sqm collectd-mod-thermal collectd-mod-wireless
    /etc/init.d/collectd enable

## Networking

### Integrating a OpenWRT device into your Network

> If you want to have an OpenWrt-powered network infrastructure, there are good chances you will need to reconfigure (or replace) the device the ISP gave you to access Internet. In case you wonder what an ISP is, it's the company you pay for your Internet access. 

> The main reason is that daisy-chaining routers is not a good idea. Depending on the type of Internet access equipment you have or have been given by your ISP, you may encounter a situation known as double NAT, which isn't good.
While double NAT doesn't generally have any ill effects on run-of-the-mill network connectivity – Web browsing, e-mail, IM, and so forth – it can be a major impediment when you need remote access to devices on your network, preventing you from connecting to your OpenWrt device's webinterface, ssh, VPN, ftp, http, Nextcloud, Seafile, and whatever else service you might want to install on your devices to be accessible from outside of your own local network.

#### What is NAT?

In a typical home network, you are allotted a single public IP address by your ISP, and this address gets issued to your router when you plug it into the ISP-provided gateway device (e.g. a cable or DSL modem). The router's Wide Area Network (WAN) port gets the public IP address, and PCs and other devices that are connected to LAN ports (or via Wi-Fi) become part of a private network, usually in the 192.168.x.x address range. NAT manages the connectivity between the public Internet and your private network, and either UPnP or manual port forwarding ensures that incoming connections from the Internet (i.e. remote access requests) find their way through NAT to the appropriate private network PC or other device. 

### IPv4/IPv6 Transitioning Technologies

[IPv4/IPv6 Transistioning Technologies](https://openwrt.org/docs/guide-user/network/ipv6_ipv4_transitioning)

## Enabling WIFI

[Enable Wifi on OpenWRT](https://openwrt.org/docs/guide-quick-start/basic_wifi)

## Enabling Internet (WAN) with PPPoe

Go to `Network -> Interfaces`

Edit `WAN`

Change the Protocol to `PPPoe`

## Adblocks

[Adblocking](https://openwrt.org/docs/guide-user/services/ad-blocking)

## Sources

* [OpenWRT Userguide](https://openwrt.org/docs/guide-user/start)