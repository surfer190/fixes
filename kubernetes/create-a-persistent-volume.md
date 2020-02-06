# Create a Persistent Volume for Kubernetes

So you have just setup your k8s cluster but now you need persistent storage for your databases etc. (Not for your ephemeral application pods)

There are seemingly infinite options to choose from of storage classes we didn't even know exist.

* awsElasticBlockStore
* azureDisk
* azureFile
* cephfs
* cinder
* configMap
* csi
* downwardAPI
* emptyDir
* fc (fibre channel)
* flexVolume
* flocker
* gcePersistentDisk
* gitRepo (deprecated)
* glusterfs
* hostPath
* iscsi
* local
* nfs
* persistentVolumeClaim
* projected
* portworxVolume
* quobyte
* rbd
* scaleIO
* secret
* storageos
* vsphereVolume

Usually we just persistent our data to the SSD of the server.
So let us try create a local persistent volume first.

## Persistent Volumes

Just as a refresher:

> A persistent volume (PV) is a piece of storage in the Kubernetes cluster, while a persistent volume claim (PVC) is a request for storage.

There is a tutorial on how to [create the PV with k3s](https://rancher.com/docs/k3s/latest/en/storage/) and using longhorn, but I digress lets just get some empty space.

### Get Some Empty

So for a start let us simply get some empty space for our k8s cluster that is not shared with other things.

So the persistent volume bankend we will use is `hostPath` - A hostPath volume mounts a file or directory from the host node’s filesystem into your Pod.

1. Log into your node

2. View disk space usage

    [root@st2 home]# df
    Filesystem              1K-blocks     Used Available Use% Mounted on
    /dev/mapper/centos-root  52403200 13602876  38800324  26% /
    devtmpfs                  5023824        0   5023824   0% /dev
    tmpfs                     5035684        0   5035684   0% /dev/shm
    tmpfs                     5035684   223216   4812468   5% /run
    tmpfs                     5035684        0   5035684   0% /sys/fs/cgroup
    /dev/mapper/centos-home  46172132    33112  46139020   1% /home
    /dev/sda1                 1038336   185224    853112  18% /boot

2. List block devices

    [root@st2 home]# lsblk
    NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda               8:0    0  100G  0 disk 
    ├─sda1            8:1    0    1G  0 part /boot
    └─sda2            8:2    0   99G  0 part 
    ├─centos-root 253:0    0   50G  0 lvm  /
    ├─centos-swap 253:1    0    5G  0 lvm  [SWAP]
    └─centos-home 253:2    0 44.1G  0 lvm  /home
    sr0              11:0    1 1024M  0 rom 
    
2. Display info about volume groups

    [root@st2 home]# vgs
    VG     #PV #LV #SN Attr   VSize   VFree
    centos   1   3   0 wz--n- <99.00g 4.00m
    
    dev/mapper is physical disk
    /home is the mount point
    
    you can mount a physical anywhere
    on physical disk a volume group creates a logical volume 

`fstab` file system table a erfence of all disks

    [root@st2 /]# cat /etc/fstab 

    #
    # /etc/fstab
    # Created by anaconda on Wed Sep 11 16:42:48 2019
    #
    # Accessible filesystems, by reference, are maintained under '/dev/disk'
    # See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
    #
    /dev/mapper/centos-root /                       xfs     defaults        0 0
    UUID=59791677-1abf-422c-a183-6186b6117ccf /boot                   xfs     defaults        0 0
    /dev/mapper/centos-home /home                   xfs     defaults        0 0
    /dev/mapper/centos-swap swap                    swap    defaults        0 0

If not mounted it won't show in `df`

Check if there are any processes using files in that path: `lsof /home`

Unmount: `umount /home`

REduce: `lvreduce -L 4G /dev/mapper/centos-home`

Grow: `xfs_growfs /home`

Mount again: `mount -av`

But now the superblock is broken:

    [root@st2 ~]# mount -av
    /                        : ignored
    /boot                    : already mounted
    mount: /dev/mapper/centos-home: can't read superblock
    swap                     : ignored

CHeck amount free

    vgs

Create logical volume

    lvcreate -L 40G -n persist centos

> Name is persist (from `centos` volume group)

Lists logical volumes

    lvs

Make filesystem:

    mkfs.xfs /dev/mapper/centos-persist 

Mount:

    mount /dev/mapper/centos-persist /persist

Ensure filesystem loads at bootime:

    vi /etc/fstab
    /dev/mapper/centos-persist /persist             xfs     defaults        0 0


3. Let us create a new volume by shrinking `/home` and creating a new volume and path


I don't know what the difference is between a persistent volume and a storage class.

A `StorageClass` is a way to dynamically provision volumes.
They can be referred to in a persistent volume claim.

A `PersistentVolume` is an independent storage volume.

Get the config of the resource:

    kubectl get pv my-persistent-volume -o yaml
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      annotations:
        field.cattle.io/creatorId: user-kmmwg
      creationTimestamp: "2020-01-14T08:36:54Z"
      finalizers:
      - kubernetes.io/pv-protection
      labels:
        cattle.io/creator: norman
      name: my-persistent-volume
      resourceVersion: "7088911"
      selfLink: /api/v1/persistentvolumes/my-persistent-volume
      uid: ed8c625b-5930-4459-b2fc-34e379168c48
    spec:
      accessModes:
      - ReadWriteOnce
      capacity:
        storage: 10Gi
      hostPath:
        path: /persist
        type: Directory
      persistentVolumeReclaimPolicy: Retain
      volumeMode: Filesystem
    status:
      phase: Available

Put now out application needs a persistent volume claim - it is what the app or deployment uses.
It will figure out which persistent volume to us.

One `PersistentVolume` will be bound to one claim

    