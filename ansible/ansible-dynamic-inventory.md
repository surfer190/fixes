# Ansible Dynamic Inventory

When is this needed:
* Inventory fluctuates over time starting up and shutting down
* Tracking hosts from different sources

Then you most probably have a dynamic external inventory system

The way ansible integrates with them in 2 ways:
* inventory plugins
* inventory scripts

Plugins are recommended over scripts

Ansible tower is a GUI for handling dynamic inventory, ithe nventory database syncs with all your dynamic inventory sources.

## Run an ad hoc command

You need to be able to ssh with no password

    ansible -i root@10.10.10.204, all -a 'uname -a'

To do this for multiple hosts:

    ansible -i "root@10.10.10.93, root@10.10.10.92, root@10.200.1.94" all -a 'uptime'

To run a module for multiple hosts:

    ansible -i "root@10.10.10.93, root@10.10.10.92, root@10.10.10.94" all -m setup

> I have noticed that if one host requires a password, it will fail. Then if you set the `-k` to ask for the ssh password, they all fail.

    $ ansible -i "root@10.10.10.93, root@10.10.10.92, root@10.10.10.94" all -m setup
    root@10.10.10.92 | UNREACHABLE! => {
        "changed": false,
        "msg": "Failed to connect to the host via ssh: root@10.10.10.92: Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).\r\n",
        "unreachable": true
    }

Ensure that jenkins is started:

    ansible -i "root@10.10.10.94," all -m service -a "name=jenkins state=started"


## Inventory scripts

You can run a (python) script to get your hosts.
This can be done by passing in the script as the `inventory` parameter: `-i openstack_inventory.py`

If you want to do this implictly - _Explicit is better than implicit._

You can place the script at `/etc/ansible/hosts`

There are existing integrations to [checkout as scripts](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html) for:
* [Cobbler](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html#inventory-script-example-cobbler)
* [AWS EC2](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html#inventory-script-example-aws-ec2)
* [OpenStack](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html#inventory-script-example-openstack)

There are other [existing inventory scripts](https://github.com/ansible/ansible/tree/devel/contrib/inventory)

Or you can create your own [inventory script](https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#developing-inventory)

### Using Inventory Directories and Multiple Inventory Sources

Using a directory can let ansible use mutliple inventories at the same time
This also allows mixing of static and dynamic inventories

Files ending in `~, .orig, .bak, .ini, .cfg, .retry, .pyc, .pyo` will be ignored

Which you can change to your own with the `inventory_ignore_extensions` entry in `ansible.cfg`

More info on using [multiple inventory sources](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#using-multiple-inventory-sources)



## Source

* [Intro to dynamic inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html)
* [Ansible adhoc inventories](https://gist.github.com/alces/f7e3de25d98a19550a4e4f97cabc2cf4)
