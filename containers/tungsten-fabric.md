## Tungsten Fabric

Open Source SDN

THe open source version of juniper networks Contrail

### What can you do with it

* Enable platform as a service with Openstack
* Virtual networking with k8s or red hat openshift
* Virtual networking between vm's on vCenter
* Connect to physical networks with gateway routers and BGP peering

### Components

* Controller - software services keeping the model or network and policies on many servers
* vRouter - Installed on each of hosts that run workloads and perform packet forwarding. Enforcing policies.

Tunsten fabric acts as the first hop forwarder in vm and container solution - they plug directly into the vRouter.
Control flow of traffic and apply security policies.

# Sources

* [Tungsten Fabric: Out of the Box Network Developers June 20 Meet Up](https://www.youtube.com/watch?v=xVJhD_INHuc)
* [ntroduction to Tungsten Fabric & the vRouter](https://www.youtube.com/watch?v=5seP3HKBhAI)
