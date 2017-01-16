# Fix uTorrent disconnecting the internet

This issue is cased by the MTU(Maximum Transmission Unit) as pointed out by [alex1911 on a private internet access forum](https://www.privateinternetaccess.com/forum/discussion/20296/torrenting-disconnect-s-my-internet). It should be changed from the 1500 default value.

1. Open CMD by clicking start icon Command Prompt(Admin) and paste this command:

    ping www.google.com -f -l 1500

    If you will see the message like: Packets need to be fragmented but DF set, drop the test packet size down (10 or 12 bytes) and test again, to 1490 - 1480 - ... Drop the test packet size down more and test again until your reach a packet size that does not fragment.

    Once you have a test packet that is not fragmented increase your packet size in small increments (1-2 bytes) and retest until you find the largest possible packet that doesn´t fragment.

    Take the maximum packet size from the ping test and add 28. You add 28 bytes because 20 bytes are reserved for the IP header and 8 bytes must be allocated for the ICMP Echo Request header.

    In my case the latest stable one was 1454 + 28 = 1482 < This is my optimal and workable MTU packets.

2. Apply settings to your ( VPN / LAN connection ). Open CMD as Admin and type:

    netsh interface ipv4 set subinterface "Your LAN NAME GOES HERE" mtu=PASTE HERE Optimal value store=persistent

    and press on Enter. Repeat with IPV6 the same command:

    netsh interface ipv4 set subinterface "YOUR LAN NAME GOES HERE" mtu=PASTE HERE Optimal value store=persistent

    Repeat all these operations with all network adapters that you have. If you are using PIA it should be called Ethernet2 and Ethernet re-check names in "Open network and sharing center" so these commands will sound something like this :

    netsh interface ipv4 set subinterface "Ethernet 2" mtu=1480 store=persistent
    netsh interface ipv6 set subinterface "Ethernet 2" mtu=1480 store=persistent
    netsh interface ipv4 set subinterface "Ethernet" mtu=1480 store=persistent
    netsh interface ipv6 set subinterface "Ethernet" mtu=1480 store=persistent


3. After these will be done, re-check if they set correctly by opening command prompt(CMD)as admin again
and post this:

    netsh interface ipv4 show subinterfaces
    netsh interface ipv6 show subinterfaces

Source:

[Alex1911's post on PIA](https://www.privateinternetaccess.com/forum/discussion/20296/torrenting-disconnect-s-my-internet)
