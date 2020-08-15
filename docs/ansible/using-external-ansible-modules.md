---
author: ''
category: Ansible
date: '2020-05-13'
summary: ''
title: Using External Ansible Modules
---
# How do you use External Ansible Modules

I have been using an ansible module developed for [vmware VcloudDirector](https://github.com/vmware/ansible-module-vcloud-director).
It is a great module and really helps speed up and maintain consistency when provisioning - over a human user.

So I created the playbooks within the directory and tested it out like that.

But now it is ready I just want to keep the relevant stuff in the library and import the module for where I am running the scripts.

The information to do that is in the [ansible docs - adding a module locally](https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html#adding-a-module-locally)

### Check that you have access to a module

The `ansible-module-vcloud-director` repo has a number of modules under the `modules/` folder:

* vcd_catalog
* vcd_external_network
* vcd_roles
* vcd_vapp_network
* vcd_vapp_vm_nic
* vcd_vdc_network
* vcd_catalog_item
* vcd_org
* vcd_user
* vcd_vapp_vm
* vcd_vapp_vm_snapshot
* vcd_disk
* vcd_org_vdc
* vcd_vapp
* vcd_vapp_vm_disk
* vcd_vdc_gateway

To check if you module is available use:

    ansible-doc -t module vcd_org

If it is found you will get the documentation.
If it does not exist you get a warning: 

    [WARNING]: module vcd_org not found in: /Users/xxx...

### Adding the module Locally

To add the module locally you need to add it to one of these places

* any directory added to the `ANSIBLE_LIBRARY` environment variable (`$ANSIBLE_LIBRARY` takes a colon-separated list like `$PATH`)
* `~/.ansible/plugins/modules/`
* `/usr/share/ansible/plugins/modules/`

You can also add a `ansible.cfg` to your directory (or in the `/etc/ansible` or `~/.ansible.cfg` directory) and then you can set the default module path:

    [defaults]
    library = ./<my-module-folder>

You can also put the modules in your project folder (like you would when running on something like AWX) and then put an `ansible.cfg` into that folder specifying the module name:

    [defaults]
    library = modules
    module_utils = module_utils



### Sources

* [Adding a module locally](https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html#adding-a-module-locally)
* [Location of Custom Ansible Modules](https://stackoverflow.com/questions/53750049/location-to-keep-ansible-custom-modules)