# View Routes

View all routes

    netstat -rn

Will return an ip routing table

    Kernel IP routing table
    Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
    0.0.0.0         10.200.0.1      0.0.0.0         UG        0 0          0 ens192
    10.200.0.0      0.0.0.0         255.255.254.0   U         0 0          0 ens192
    172.17.0.0      0.0.0.0         255.255.0.0     U         0 0          0 docker0
    172.18.0.0      0.0.0.0         255.255.0.0     U         0 0          0 br-62f2cfd34d85

Try to telnet or ping a host

    telnet 196.41.6.162 389

Add a route

    route add -net 196.41.6.162 netmask 255.255.255.255 gw 10.200.1.249

Delete a route

    route del -net 196.41.6.162 netmask 255.255.255.255 gw 10.200.1.249

