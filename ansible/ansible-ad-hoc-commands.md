# Running adhoc commands on multiple servers

#### Example host file

Using the following `/etc/ansible/hosts` file:

    [app]
    192.168.60.4
    192.168.60.5

    [db]
    192.168.60.6

    #Group `multi` with all servers
    [multi:children]
    app
    db

    #Variables that will be applied to all servers
    [multi:vars]
    ansible_ssh_user=vagrant
    ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key

#### Running commands

By default ansible will run your commands in parallel using multiple process forks.
To check the host name

    ansible multi -a "hostname"

#### To Run Commands in sequence (A single process fork)

    ansible multi -a "hostname" -f 1

It is rare that you will need to do that the number of forks will usually be around `-f 10` or `f -20`

#### Other Commands

Ping:

```
ansible [group-name] -m ping -u [username]
```

Show all facts:

```
ansible [host/group] -m setup -u [username] -i [inventory file]
```


Disk space:

```
ansible multi -a "df -h"
```

Free memory:

```
ansible multi -a "free -m"
```

Date and Time:

```
ansible multi -a "date"
```

Exhaustive list:

```
ansible multi -a setup
```

Make sure a package is installed
`-s` means run as `sudo`

    ## yum
    ansible multi -s -m yum -a "name=ntp state=installed"

    ## apt
    ansible multi -s -m apt -a "name=ntp state=installed"

Make sure a package is enabled on boot and currently running

    ansible multi -s -m service -a "name=ntpd state=started enabled=yes"

Make Sure time is synced closely to official time:

    ansible multi -s -a "service ntpd stop"
    ansible multi -s -a "ntpdate -q 0.rhel.pool.ntp.org"
    ansible multi -s -a "service ntpd start"

It is best to use the powers of ansible (abstraction and idempotency) when running commands

    ansible -m shell -a "date" multi

Although there is usually no need for a module when running adhoc.

### Configuring Appication Servers

For this example we will use `django`

`django` is not in many official repos so we can use pythons easy_install which comes as an ansible module

    ## Yum
    ansible app -s -m yum -a "name=MySQL-python state=present"

    # Apt
    ansible app -s -m apt -a "name=MySQL-python state=present"

    ansible app -s -m yum -a "name=python-setuptools state=present"
    ansible app -s -m easy_install -a "name=django"

`easy_install` doesn't allow uninstall like `pip` does. So you could have used `pip`.

Make sure django is installed and working

    ansible app -a "python -c 'import django; print django.get_version()'"

### Configuring the Database Server

Install `MariaDB`, start it and configure the firewall to allow access on port `3306`

    ansible db -s -m yum -a "name=mariadb-server state=present"
    ansible db -s -m service -a "name=mariadb state=started enabled=yes"
    ansible db -s -a "iptables -F"
    ansible db -s -a "iptables -A INPUT -s 192.168.60.0/24 -p tcp \ -m tcp --dport 3306 -j ACCEPT"

We still need to secure the install what about `mysql_secure_installation`

    ansible db -s -m yum -a "name=MySQL-python state=present"

    ansible db -s -m mysql_user -a "name=django host=% password=12345 \ priv=*.*:ALL state=present"

So at this point we can create a django application and poiint the db to the database server with:

username: `django`
password: `12345`

_The MySQL configuration used here is for example/development purposes only! There are
a few other things you should do to secure a production MySQL server, including removing
the test database, adding a password for the root user account, restricting the IP addresses
allowed to access port 3306 more closely, and some other minor cleanups_

### Make changes to just one server

Use limit `--limit <ip/blob>`

    ansible app -s -a "service ntpd restart" --limit "192.168.60.4"

    # with a blob
    ansible app -s -a "service ntpd restart" --limit "*.4"

    # withregex
    ansible app -s -a "service ntpd restart" --limit ~".*\.4"

Try to limit the usage of limit, if you find yourself using them alot it may be better to add a group in the `/etc/ansible/hosts` file

### Manage Users and Groups

Add an admin group

    ansible app -s -m group -a "name=admin state=present"

remove a group: `state=absent`

set the group id: `gid=[gid]`

indicate group is a system user: `system=yes`

Add a new user to a group and add a home folder:

    ansible app -s -m user -a "name=johndoe group=admin createhome=yes"

set the user id: `uid=[uid]`

set the user's shell: `shell=[shell]`

set the password: `password=[encrypted_password]`

Delete an account:

    ansible app -s -m user -a "name=johndoe state=absent remove=yes"

### Manage Files and Directories

###### Check info about a file:

    ansible multi -m stat -a "path=/etc/environment"

###### Copy files to servers:

    ansible multi -m copy -a "src=/etc/hosts dest=/tmp/hosts"

_The src can be a file or a directory. If you include a trailing slash, only the contents of the directory
will be copied into the dest . If you omit the trailing slash, the contents and the directory itself will
be copied into the dest ._

For many files use Ansibles `unarchive` or `synchronize` modules

###### Retrieve a file from the servers

    ansible multi -s -m fetch -a "src=/etc/hosts dest=/tmp"

Copying from a single host use `flat=yes`

###### Create a directory

    ansible multi -m file -a "dest=/tmp/test mode644 state=directory"

###### Create a Symlink

    ansible multi -m file -a "src=/src/symlink dest=/dest/symlink owner=root group=root state=link"

###### Delete Directories or Files

    ansible multi -m file -a "dest=/tmp/test state=absent"

###### Running Commands Asynchronously

Eg. `apt-get update && apt-get dist-upgrade`

Ansible will poll when the status is complete

* `-B <seconds>` : the maximum amount of time in seconds to let the job run
* `-P <seconds>` : amount of time to wait between polling servers

Example of Aynchronous:

    # yum
    ansible multi -s -B 3600 -m yum -a "name=* state=latest"

    #apt
    ansible <group> -s -B 3600 -m apt -a "upgrade=dist"


**Fire and Forget tasks**

    ansible multi -B 3600 -P 0 -a "/path/to/fire-and-forget-script.sh"

###### Checking log files

`tail, cat, grep, less, etc`

Continuously monitoring operations like `tail -f` won't as ansible only displays output after an operation is complete.
Also `Ctrl-C` won't be able to send.

if you want to filter the messages log with something like grep , you can’t
use Ansible’s default command module, but instead, shell

`ansible multi -s -m shell -a "tail /var/log/messages | \
grep ansible-command | wc -l"`

### Managing Cron Jobs

Periodic tasks run via cron are managed by a system’s crontab. Normally, to change cron job settings
on a server, you would log into the server, use crontab -e under the account where the cron jobs
reside, and type in an entry with the interval and job.

Ansible apparently makes it easier, if you want to run a cronjob everyday at 4.

    ansible multi -s -m cron -a "name='daily-cron-all-servers' \
    hour=4 job='/path/to/daily-script.sh'"

Ansible will assume * for all values you don’t specify (valid values are day , hour , minute , month ,
and weekday ). You could also specify special time values like reboot , yearly , or monthly using
special_time=[value] .

Deleting a cronjob

    ansible multi -s -m cron -a "name='daily-cron-all-servers' state=absent"

#### Deploy a Version-Controlled Application

Seems like you need to install git first:

    # yum
    ansible app -s -m yum -a "name=git state=installed"
    #apt
    ansible app -s -m apt -a "name=git state=installed"

The theory is you can specify a version which is a tag or branch.
To force an update use `update=yes`

    ansible app -s -m git -a "repo=git://example.com/path/to/repo.git \
    dest=/opt/myapp update=yes version=1.2.4"

### Ansible and SSH connection History

Ansible use no extra daemons or apps, nor does it use any proprietary protocol. It uses **SSH**.
The process is: `ansible` transfers a few files or _plays_ to the server, tuns them and the deletes the files.

Ansible used to use `paramiko` an open source SSH2 implementation for python. The problems were is didn't keep pace with
`openSSH` and performance is slightly worse.
OpenSSH is now the standard for all servers supporting `controlpersist`

_ControlPersist allows SSH connections to persist so frequent commands run over SSH don’t have
to go through the initial handshake over and over again_

Also there is something called `Accelerated Mode`, which connects with `SSH` initially then uses the `AES` key (on port `5099`) for future transfers.
There is an extra package required to use the accelerated mode called `python-keyczar`.

There are 2 exceptions:

* The `sudoers` files needs `requiretty` disabled
* must disable sudo passwords by setting `NOPASSWD` in sudoers file

    ---
    - hosts: all
      accelerate: true
      [...]

Need a port (default of `5099`) open or port specified by `accelerate_port`

Another improvement sends commands directly over ssh, only available in `ansible 1.5+` by setting:
`pipelining=True` under `[ssh_connection]` of `ansible.cfg`

##### Source

* [Ansible docs - Fathering facts](http://docs.ansible.com/ansible/intro_adhoc.html#gathering-facts)
