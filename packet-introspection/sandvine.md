sandscript
sandvine - dpi manages traffic for internet customers

radius authenticates + accounting information (packet with all session data)
sandvine responsible - 

telkom (openserve) -> isp radius servers (username and password) -> check against ldap -> authenticated -> 
on telkom -> provider is know based on location / ip address -> radius gives ip pool and dns servers to use -> telkom then assigns that ip to the customer (with dhcp) and give a generated start packet

username, client ip address, packet status -> start, stop, interim

radius proxy / forwards accounting packages to 

sandvine

Subscriber mapping on both SDE and SPB

* SDE - manages quotas: map ip address to username, manages policy quotas and usage management - small db - generates UDR files
* SPB - subscriber policy broker - main database = postgres - another interface to log int to `svcli` (Has a rest API) - view traffic flow
* PTS - Policy Traffic Switch - after assigning ip - pts just knows ip address (links ip address to specific customer and assign specific policy) - recording up, down (usage management) [Stores mothing only temporary] - managing of traffic

some business and normal internet customers go via sandvine

udr - usage data records - files go to elastic
prioritise voice, web browsing is prioritised

svftp server - udr rte (real time entertainment) traffic uploaded
sent to svlogparser - filebeat installed on it

filebeat -> logstash -> elastic

LTIP - Loadable traffic identification protocol

NDS - network demographic - low level
NA - network analytics - higher level



/usr/local/sandvine - root sandvine directory
rc.conf

network dev
network must configure a realm to reroute all traffic from realm via cape town lab to the internet - create an account on production ldap and authenticate and reroute traffic to dev.
replicate accounting data from radius to dev

sandscript

PSC Vmware specific to do LDAP authentication
