## Firecracker

Virtual Machine Manager

Uses KVM (Linux Kernel based virtual Machine)

* Security and isolation of traditional vm's
* Speed and density of containers
* Low Resource overhead
* Developed at Amazon

## Benfits of Firecracker

* Security
* Startup Time - < 125ms to launch 150 microVM'sper second/host
* Utilisation (scale and efficiency) - < 5MB memory footprint

Also has rate limiter - to distribute vm's inside a single host

So you have to use the kata container runtime on Firecracker? Still integrating with container-d.

What is the difference between runC, containerD and docker?
* Docker is an OCI image format

Alternate to QEMU - an established VMM (Virtual Machine Manager)

## Design Principles

* Multitenancy - hardware virtualisation based security
* Any vCPU and Memory combination
* Oversubscription permissable
* Steady mutation - Can launch 100 microvm's per host per sceond (4 microVM's per physical core)
* Host facing Rest API

## Architecture

* Runs in Userspace

Bare Metal -> KVM -> Firecracker (userspace)

Customer Code (In container) -> Guest OS (Kernel on VM) -> Hypervisor (KVM) -> Host OS -> Hardware

Guest OS is linked to a single customer account
Hypervisor and Host OS has many customer accounts (multitenenacy)

Firecracker sits on the hupervisor and Host OS part

## Firecracker and Containers

* Management - Deployment and scheduling (Amazon ECS, Amazon EKS)
* Hosting - Amazon EC2, AWS Fargate (just give container - all monitorng and debugging you must handle)
* Image Regstry - You don't want to think about the registry

Fargate - run container with this much vCPU and this much Memory

Essentially you can move the Guest VM's around on bare metal hosts belonging to different customers

Firecracker reduces costs for customers

## Firecracker and ContainerD

* Use Containerd to manasge contianers as firecracker MicroVMs
* Multi-tenant Hosts
* OCI Image format

Make it work with kubernetes and k8s distro's like Rancher etc.

## Firecracker integration with Opensource

### Kata Containers

Lightweight VM for running containers. Seemlessly plugs into containers.
Firecracker is more lightweight VMM than Qemu.

In k8s you can set to use katacontainers:

    spec:
      template:
        spec:
          runtimeClassName: kata-fc

### Weave Ignite

* Open source VMM with a container UX
* Combines Firecracker microVMs with OCI images
* GitOps Continuous Integration - quick testing

### Getting Started with Firecracker

Just like `kubectl` there is `firectl`

    firectl --kernel=hello-vmlinux.bin --root-drive=hello-rootfs.ext4

* UniK - take application source / container and run on firecracker
* OSv


## Source

* [Firecracker: A Secure and Fast microVM for Serverless Computing](https://www.youtube.com/watch?v=PAEMGa-i2lU)











