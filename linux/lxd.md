# LXD

A System container manager, offering a similar user experience to virtual machines but using linux containers instead.

* Image based with pre-made images for a wide number of linux distributions
* Built around a REST API

## Commands

View loaded images

    lxc iamge list

There are 3 default image servers:

* ubuntu
* ubuntu-daily
* images

List stable ubuntu images

    lxc image list ubuntu: | less

Launch an image

    lxc launch ubuntu:18.04 first

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


## Source

* [LXD Tutorial](https://linuxcontainers.org/lxd/try-it/?id=308fdf4e-1c85-4918-9064-e119cc3b62c5#first-container)

