---
author: ''
category: Linux
date: '2019-10-07'
summary: ''
title: Lxd
---
# LXD and LXC

LXC - Linux Containers, a userspace interface using the host's kernel
LXD - An extension to LXC adding a Rest API - an alternative to LXC's tools

> The lightervisor

A System container manager, offering a similar user experience to virtual machines but using linux containers instead.

* Image based with pre-made images for a wide number of linux distributions
* Built around a REST API
* Designed to run full machine containers - as opposed to docker and rocket that run process based containers
* High density - number of containers you can run
* Feels the same as a full machine
* Security focus - all processes not run as root

> The LXD daemon only works on Linux but the client tool (lxc) is available on most platforms

## Commands

View loaded images

    lxc image list

You can also view [available images on their website](https://us.images.linuxcontainers.org/)

There are 3 default image servers:

* ubuntu
* ubuntu-daily
* images

List stable ubuntu images

    lxc image list ubuntu: | less

Launch an image

    lxc launch ubuntu:18.04 first

View current server configuration

    lxc config show

The new image will be visible in the list now

    lxc list

Get running details

    lxc info first
    lxc config show first

### Limiting Resources

By default your container comes with no resource limitation and inherits from the parent environment

    free -m
    lxc exec first -- free -m

To apply a memory limit to a container

    lxc config set first limits.memory 128MB

Confirm it has been applied

    lxc exec first -- free -m

### Snapshots

LXD supports snapshotting and restoring container snapshots

Make a snapshot called `clean`:

    lxc snapshot first clean

Restore everything to the snapshotted state:

    lxc restore first clean

Confirm everything is back to normal

    lxc exec first -- bash

### Creating Images

To publish an existing container

    lxc publish first/clean --alias clean-ubuntu

Delete the initial contains

    lxc stop first
    lxc delete first

Launch a container from the existing image

    lxc launch clean-ubuntu second

Stop and delete

    lxc delete --force second

### Accessing files from the container

Pull a file from the container

    lxc file pull second/etc/hosts .

Push a file to the container

    lxc file push hosts second/etc/hosts

Access log files

    lxc file pull second/var/log/syslog - | less

### Use a remote image server

List available images

    lxc image list images: | less

Spawn a centos container

    lxc launch images:centos/7 third

Confirm it is centos

    lxc exec third -- cat /etc/redhat-release

Delete it

    lxc delete -f third

List all configured remotes

    lxc remote list

List remote container images

    lxc list tryit:

List images

    lxc image list tryit:

Launch a local image on a remote LXD

    lxc launch clean-ubuntu tryit:fourth

Spawn a shell inside the remote

    lxc exec tryit:fourth bash

Copy that container

    lxc copy tryit:fourth tryit:fifth

Move it back to our local lxd

    lxc move tryit:fifth sixth

## NC-LXD

Drop in replacement for libVirt KVM driver - to manage LXD containers in an Openstack cloud.

## LXD vs KVM

In KVM the virtual machine has all the same things as bare metal - bios, bootloader, linux kernel, host OS then can you only run your workload.
In LXD there is none of that, containers run as processes directly on the host - no bios, no device drivers.

### Density

Intel server 4 core, 16 Gb and setup ubuntu on it.
Launch KVM instances with an ubuntu image until we run out of hypervisor resources and do the same thing with LXD.

The VM's were 512mb.

KVM launched 36.
LXD launched over 600, of the same image. A much lower memory footprint.

> LXD is frugal with memory

### Startup Time

How fast the instances are created

LXD - 1.5 seconds
KVM - 25 seconds

* 37 KVM instances launched in 943 seconds
* 536 LXD guests in 828 seconds

### Network Latency

KVM packet through networking layer into host, to bridge and wake up other host etc.
With LXD with the same test, there is not as much to go through so apps communicate 50% faster

Even local latency with 2 threads needing to be scheduled and context switched between, LXD was 50% faster.

### OS Limitations

You can run a windows or mac VM on a KVM instance. Only something that runs on a linux container will work on LXD.
You could run centOS but you will get the ubuntu kernel.

### Limitations

On LXD cannot `mount` within a guest instances, you have to ask `lxd` to mount it.

Fits with OpenStack to provide the networking and storage components

### Security

If you are not in a privileged container you won't be able to create another `lxc` instance inside that container.

    lxc config set myvm2 security.privileged true
    lxc config set myvm2 security.nesting true

or with profile:

    lxc profile edit customer

* security.nesting - 
* security.privileged - 

## Source

* [LXD Tutorial](https://linuxcontainers.org/lxd/try-it/?id=308fdf4e-1c85-4918-9064-e119cc3b62c5#first-container)
* [LXD vs KVM](https://www.youtube.com/watch?v=90oxad2r8_E)
* [LXD Readthedocs](https://lxd.readthedocs.io/en/latest/)
* [LXD Five Easy Pieces](https://ubuntu.com/blog/lxd-5-easy-pieces)
