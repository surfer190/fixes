# LXD Cluster

## Planning

There are three main dimensions we need to consider for our LXD cluster:

* The number of compute node
* The type and quantity of available storage
* The container networking.

> A minimalistic cluster necessitates at least three host nodes

We may choose to use bare-metal servers or virtual machines as hosts. In the latter case, it would be beneficial for the VMs to reside on three different hypervisors for better fault tolerance

Storage - LXD has a powerful driver back-end enabling it to manage multiple storage pools both host-local (zfs, lvm, dir, btrfs) and shared (ceph)

Networking - VXLAN-based overlay networking as well as “flat” bridged/macvlan networks with native VLAN segmentation are supported

> It’s important to note that the decisions for storage and networking affect all nodes joining the cluster and thus need to be homogenous

## Walkthrough

1. [Create 3 VM's using MAAS and KVM Pods](https://tutorials.ubuntu.com/tutorial/create-kvm-pods-with-maas#0)
2. Create 2 local storage volumes: (1) 8GB for the root filesystem (2) 6GB for the LXD storage pool
3. Configure each vm with [bridged interface (`br0`)](https://old-docs.maas.io/2.3/en/nodes-commission#bridge-interfaces) and [auto-assign ip mode](https://old-docs.maas.io/2.3/en/nodes-commission#post-commission-configuration)
4. Deploy Ubuntu 16 on all the VM's
5. Install ZFS for our storage pools
6. Install LXD 3.0 from snaps and intialise lXD interactively





## Sources

* [Ubuntu: LXD Clusters a Primer](https://ubuntu.com/blog/lxd-clusters-a-primer)