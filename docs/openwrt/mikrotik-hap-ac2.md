---
author: ''
category: OpenWRT
date: '2021-12-27'
summary: ''
title: Installing OpenWRT on a Mikrotik Hap AC2
---
## Installing OpenWRT on a Mikrotik Hap AC2

Router: MikroTik RouterBOARD hAP ac² (RBD52G-5HacD2HnD-TC)

You can follow the basic guide on [openwrt for mikrotiks](https://openwrt.org/toh/mikrotik/common)

> remember to [store your RouterOS license](https://openwrt.org/toh/mikrotik/common#saving_mikrotik_routerboard_license_key_using_winbox_and_windows)

If the default gateway of the device is `192.168.101.1` it may be preconfigured. In which case you should [reset it as described in this video](https://www.youtube.com/watch?v=OjLNA84ogUM&ab_channel=AtomicAccess)

The simplified version is:

1. Download the Snapshot and snapshot upgrade. It is important to note that the referenced version on the [hap_ac2](https://openwrt.org/toh/mikrotik/hap_ac2) page does not include the LuCi browser interface. So it is better to use the files from the [firmware selector](https://firmware-selector.openwrt.org/?version=21.02.1&target=ipq40xx%2Fmikrotik&id=mikrotik_hap-ac2)
2. Boot into a linux OS or Live CD and make sure `dnsmasq` is installed

    > `dnsmasq` is best [installed from source](https://thekelleys.org.uk/dnsmasq/docs/setup.html). But to use `ifconfig` you need `sudo apt install net-tools`. You also need to have `make` and `gcc` to compile. 

3. Create this script `loader.sh` (change the user and if your router defaults to `192.168.88.1` then this will work. Also change the file name to reflect your chosen.):

        #!/bin/bash
        USER=ubuntu
        IFNAME=enp1s0
        /sbin/ip addr replace 192.168.88.10/24 dev $IFNAME
        /sbin/ip link set dev $IFNAME up
        /usr/sbin/dnsmasq --user=$USER \
        --no-daemon \
        --listen-address 192.168.88.10 \
        --bind-interfaces \
        -p0 \
        --dhcp-authoritative \
        --dhcp-range=192.168.88.100,192.168.88.200 \
        --bootp-dynamic \
        --dhcp-boot=openwrt-21.02.1-ipq40xx-mikrotik-mikrotik_hap-ac2-initramfs-kernel.bin \
        --log-dhcp \
        --enable-tftp \
        --tftp-root=$(pwd)
    
    The above script is available at [openwrt mikrotik netboot](https://openwrt.org/toh/mikrotik/common#run_a_dhcpbootptftp_netboot_server)
    Make sure the file is in the same directory as both the init and upgrade file, ensure it is executable and run it:

        chmod +x loader.sh
        sudo bash loader.sh

4. Ensure your Mikrotik router is in DHCP boot mode

    * Connect the router, plug in ethernet into LAN port 2. Go to 192.168.88.1, login.
    * System → Routerboard → Settings → Boot device: Try ethernet once then NAND
    * System → Routerboard → Settings → Boot protocol: DHCP
    * System → Routerboard → Settings → Force Backup Booter: Checked (if supported by your routerboard - !IMPORTANT)
    * System → Shutdown. Power down the router.

    > Hit `Apply`

    If the above doesn't work use [method 1: reset](https://openwrt.org/toh/mikrotik/common#method_1_-_use_the_routerboard_reset_button_to_enable_tftp_netboot)

5. Put the ethernet cable into WAN port 1
6. Start up the router
7. The loader script will show a connection (you might need to re-run it). It will say sending file, then sent. Once complete it will output some data...then `sent size` and at the end it will say `server-identifier 192.168.88.10` or something like that. It takes about 10 minutes.
8. The router should be running openwrt now - note you must connect with ethernet wifi will not work.
9. Test you can ping to it: ping 192.168.1.1
10. You cannot telnet but should be able to ssh: `ssh root@192.168.1.1`
11. Also check if you can get to the Luci browser: `https://192.168.1.1`
12. Flash OpenWRT to permanently write openWRT to the device:

    * Go to System → Backup/Flash Firmware
    * Click on 'Choose File' under 'Flash new firmware image'. Select the sysupgrade .bin file you previously downloaded for your RouterBoard
    * Click on 'Flash image'. This will flash the sysupgrade .bin file into your RouterBoard and reboot it

You have successfully installed OpenWRT on the Mikrotik hap AC2. Now look at the [openwrt user guide](https://openwrt.org/docs/guide-user/start)

## Restoring RouterOS onto a Mikrotik OpenWRT

> I did this on ubuntu

Follow these [instructions](https://help.mikrotik.com/docs/display/ROS/Netinstall)

The important points to note:

* if you have installed openwrt on the device you will need the keyfile to reinstall:

    ./netinstall -r  -k <myfile>.key -a 192.168.88.3 routeros-7.1.1-arm.npk

* You must [download the image](https://mikrotik.com/download) and netinstall binary marked as `stable`

1. Set the static IP:

    1. Ubuntu -> wired connection -> settings
    2. Settings -> IPv4
        Address: 192.168.88.2
        Netmask: 255.255.255.0
        Gateway: 192.168.88.1
        DNS: 192.168.88.1 (Automatic off)
    3. Apply
    4. Turn the toggle on and off

2. Run the script

    sudo ./netinstall -r  -k <myfile>.key -a 192.168.88.3 routeros-7.1.1-arm.npk

3. Enable the Etherboot

    1. Put LAN Cable in ETH1 (Internet/PPPoe)
    2. take out the power cable
    3. Press `reset` in and hold
    4. put power cable back in
    5. Wait for the light to start flashing and then stop (about 20 seconds)
    6. Release the reset
    7. Script should start
    
4. When it is completed it should sat `Sent reboot command`

    Will reset config
    Using server IP: 192.168.88.2
    Starting PXE server
    Waiting for RouterBOARD...
    PXE client: B8:69:F4:83:F9:98
    Sending image: arm
    Discovered RouterBOARD...
    Formatting...
    Sending package routeros-7.1.1-arm.npk ...
    Ready for reboot...
    Sent reboot command


### Sources

* [Openwrt Mikrotik Common](https://openwrt.org/toh/mikrotik/common)
* [Restoring MikroTik (RouterOS) using NetInstall](https://help.mikrotik.com/docs/display/ROS/Netinstall)
