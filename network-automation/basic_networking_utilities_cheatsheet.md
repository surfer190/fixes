# Basic Network Utilities Cheatsheet on Linux / Unix

## Display Information about your connection interfaces

    ifconfig -a

## Examine ARP table

    $ arp -a
    ? (192.168.0.1) at d4:6e:e:87:a8:8a on en0 ifscope [ethernet]
    ? (192.168.0.100) at 2:f:b5:8d:a5:2f on en0 ifscope [ethernet]
    ? (192.168.0.101) at 78:32:1b:ac:8d:5b on en0 ifscope [ethernet]
    ? (192.168.0.123) at 94:53:30:46:aa:3c on en0 ifscope [ethernet]
    ? (192.168.0.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
    ? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
    broadcasthost (255.255.255.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
    
## Clear ARP table

    $ sudo arp -a -d
    192.168.0.1 (192.168.0.1) deleted
    192.168.0.100 (192.168.0.100) deleted
    192.168.0.101 (192.168.0.101) deleted
    192.168.0.123 (192.168.0.123) deleted
    192.168.0.255 (192.168.0.255) deleted
    224.0.0.251 (224.0.0.251) deleted
    255.255.255.255 (255.255.255.255) deleted

## Traceroute

    $ traceroute -m 4 fixes.co.za
    traceroute to fixes.co.za (37.139.28.74), 4 hops max, 52 byte packets
    1  192.168.0.1 (192.168.0.1)  1.115 ms  0.777 ms  0.722 ms
    2  * * *
    3  196.38.75.109 (196.38.75.109)  9.340 ms  8.033 ms  8.117 ms
    4  196.38.75.110 (196.38.75.110)  7.573 ms  8.247 ms  5.953 ms

## Ping (ICMP echo)

    $ ping -c 4 fixes.co.za
    PING fixes.co.za (37.139.28.74): 56 data bytes
    64 bytes from 37.139.28.74: icmp_seq=0 ttl=50 time=226.616 ms
    64 bytes from 37.139.28.74: icmp_seq=1 ttl=50 time=245.647 ms
    64 bytes from 37.139.28.74: icmp_seq=2 ttl=50 time=264.032 ms
    64 bytes from 37.139.28.74: icmp_seq=3 ttl=50 time=284.747 ms

    --- fixes.co.za ping statistics ---
    4 packets transmitted, 4 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 226.616/255.261/284.747/21.560 ms
