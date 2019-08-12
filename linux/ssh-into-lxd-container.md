# How to SSH into your LXD container

Get a list of containers:

    vagrant@ubuntu-bionic:~/.config/lxc$ lxc list
    +---------------------+---------+------+------+------------+-----------+
    |        NAME         |  STATE  | IPV4 | IPV6 |    TYPE    | SNAPSHOTS |
    +---------------------+---------+------+------+------------+-----------+
    | apache-web          | RUNNING |      |      | PERSISTENT | 0         |
    +---------------------+---------+------+------+------------+-----------+
    | first               | RUNNING |      |      | PERSISTENT | 0         |
    +---------------------+---------+------+------+------------+-----------+
    | last                | RUNNING |      |      | PERSISTENT | 0         |
    +---------------------+---------+------+------+------------+-----------+
    | rainbows-web-centos | RUNNING |      |      | PERSISTENT | 0         |
    +---------------------+---------+------+------+------------+-----------+
    | redis-app-db        | RUNNING |      |      | PERSISTENT | 0         |
    +---------------------+---------+------+------+------------+-----------+
    | second              | RUNNING |      |      | PERSISTENT | 0         |
    +---------------------+---------+------+------+------------+-----------+
    | third               | RUNNING |      |      | PERSISTENT | 0         |
    +---------------------+---------+------+------+------------+-----------+

If you have not setup networking yet, you can open a shell in your container with:

    lxc exec third -- /bin/bash

Then check the OS:

    root@first:~# lsb_release -a
    No LSB modules are available.
    Distributor ID:	Ubuntu
    Description:	Ubuntu 18.04.2 LTS
    Release:	18.04
    Codename:	bionic

Checking another:

    lxc exec rainbows-web-centos -- /bin/bash

gets:

    [root@rainbows-web-centos ~]# cat /etc/os-release
    NAME="CentOS Linux"
    VERSION="7 (Core)"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="7"
    PRETTY_NAME="CentOS Linux 7 (Core)"
    ANSI_COLOR="0;31"
    CPE_NAME="cpe:/o:centos:centos:7"
    HOME_URL="https://www.centos.org/"
    BUG_REPORT_URL="https://bugs.centos.org/"

    CENTOS_MANTISBT_PROJECT="CentOS-7"
    CENTOS_MANTISBT_PROJECT_VERSION="7"
    REDHAT_SUPPORT_PRODUCT="centos"
    REDHAT_SUPPORT_PRODUCT_VERSION="7"

