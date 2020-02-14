## Kata Containers

* Virtual machines - bigger, slower with more isolation. Boot time of minutes.
* Containers - quick, simple but less isolation

kata containers is a blending of the two. Security and isolation of virtual machines without the bloat of virtual machines.

> It is a vm

### How do you use Kata Containers

It looks like `runc` an OCI compatible runtime

`runC` is the universal container runtime

### History

Before kata there was Intel Clear Containers

### Traditional Containers

You have a host and a kernel. Your containers run within namespaces on that host.
All good until somebody breaks out of a container - which you have access to all containers.

### Traditional containers in a VM

A Vm within a VM with containers in it

> Kata has lightweight virtual machines

### Kata Containers

* Every Container / Pod gets it's own virtual machine
* Container doesn't know it is a vm - same deployment process

## Architeture and Integrations

Components:
* QEMU - KVM
* Runtime (Kata Runtime)
* Kernel - to sit inside VM
* rootfs image - vm has to boot something (rootfs sets up the container)
* Agent - work to happen: mount points, networks, memory resources and cgroups
* Shim
* Proxy

### CRI-O and Kata

Kubelet -> CRI (Container Runtime Interface) -> CRI-o/ContainerD    -> runc
                                                                    -> kata-runtime -> vm

Can choose which you want - if you don't trust it run it in a kata container

Fairly seemless

### Networking and Storage

Containers run at layer 3 but vm's run at layer 2

Storage:
* 9pfs (overlay) - easy to use network based file system with plan9 (just works) - default. Not a full POSIX unix filesystem.
* Block devices (device mapper) - vm can find block device , map and mount to virtual machine (not going over network connection)
* Network (ceph, gluster) - Network storage works as you expect

### Overhead

* 50MB per container
* Boot in less than a second

### Road Map

Primarily around security and isolation

Security, in container: `seccomp`
Security, on host: `cgroup isolation`, `more namespace isolation`, `root-less QEMU` and `SELinux` policy


## Source

* [Kata Containers An introduction and overview](https://www.youtube.com/watch?v=4gmLXyMeYWI)






