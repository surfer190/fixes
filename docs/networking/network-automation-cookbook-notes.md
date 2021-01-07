---
author: ''
category: Networking
date: '2021-01-07'
summary: ''
title: Network Automation Cookbook Notes
---
## Network Automation Cookbook Notes

## 1. Building Blocks of Ansible

Ansible is an automation framework / platform. It is written in python and relies on SSH mainly.
Started network device support in Ansible 1.9.

* Decent learning curve: builds on yaml and jinja2 templates
* Agentless: Does not need an agent installed on the remote device
* Extensible
* Idempotent: Has a desired state and no matter how many times a play is run it maintains that state (In theory)

### Installing Ansible

1. Install python from [python.org](https://www.python.org/downloads/)
2. Install ansible

    pip install ansible

Verify it is installed with:

    ansible --version
    ansible 2.9.7
    config file = /etc/ansible/ansible.cfg
    configured module search path = ['/Users/stephen/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/ansible
    executable location = /Library/Frameworks/Python.framework/Versions/3.8/bin/ansible
    python version = 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) [Clang 6.0 (clang-600.0.57)]

> You can see it is using python 3, you always want to use python3 as python2 is end of life

Run an ad-hoc command to ping the local machine

    $ ansible -m ping localhost
    [WARNING]: No inventory was parsed, only implicit localhost is available
    localhost | SUCCESS => {
        "changed": false,
        "ping": "pong"
    }

### Building Ansible Inventory

Inventory is a file defining the nodes/hosts ansible will manage, and how to connect to them.

Example: `hosts`

    [cisco]
    csr1 ansible_host=172.10.1.2
    csr2 ansible_host=172.10.1.3

    [juniper]
    mx1 ansible_host=172.20.1.2
    mx2 ansible_host=172.20.1.3

    [core]
    mx1
    mx2

    [edge]
    csr[1:2]

    [network:children]
    core
    edge

The hosts in the above are `csr1`, `csr2`, `mx1` and `mx2`.
They are assigned to group specified by `[]`

They can be grouped by vendor (juniper or IOS) or function (core or edge)

> You can also specify an inventory in yaml

## Using Ansible's Variable

Variables relating to the hosts can be declared in many places.

The best practise is making use of `host_vars` and `group_vars`.
`group_vars` apply to all hosts within that group, `host_vars` are host specific.

    mkdir group_vars
    mkdir host_vars
    
In `group_vars/cisco.yml`:

    os: ios

In `group_vars/juniper.yml`:

    os: junos
    
In `host_vars/csr1.yml`:

    hostname: edge-csr1

In `host_vars/csr2.yml`:

    hostname: edge-csr2

In `host_vars/mx1.yml`:

    hostname: core-mx1

In `host_vars/mx2.yml`:

    hostname: core-mx2

> There are other ways to define variables, using the `vars` keyword in the playbook

In addition to use defined variables, ansible creates default variables it builds dynamically.

* `inventory_hostname` - name of the host in the inventory
* `play_hosts` - a list of all hosts included in the play
* `group_names` - a list of all the groups a host is part of

### Building Ansibles Playbook

A playbook declares the tasks we want to perform on a set of hosts.

Create a file `playbook.yml`:

```
---

  - name: Initial playbook
    hosts: all
    gather_facts: no
    tasks:
      - name: Display Hostname
        debug:
          msg: "Router name is {{ hostname }}"
      - name: Display OS
        debug:
          msg: "{{ hostname }} is running {{ os }}"
```

Run the playbook with:

    ansible-playbook -i hosts playbook.yml

> `all` is a group name built-in to ansible that dynmaically constructs a group for all hosts in the inventory

### Ansible's Conditionals

Ansible uses the `when` statement to decide whether to run a given task. If the when statement (a python conditional) evaluates to `True` it runs, if it evaluates to `False` it will be skipped.

A single conditional can be given or a list of conditionals, eg:

      - name: Do X
        ....
        when:
          - ip == '192.167.0.1'
          - connected

In `conditional_playbook.yml`:

```
---

  - name: Conditional playbook
    hosts: all
    gather_facts: no
    tasks:
      - name: Display Hostname
        debug:
          msg: "Router name is {{ hostname }}"
        when: "'edge' in group_names"
      
      - name: Display OS
        debug:
          msg: "{{ hostname }} is running {{ os }}"
        when:
          - inventory_hostname == 'mx1'
```

> The conditional must be enclosed in a string when it starts with a string

[More info on ansible conditionals](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html)

### Ansible Loops

The `loops` keyword is used to loop over a list.
The `with_dicts` keywork is used to loop over dictionarties, with `item.key` being the dictionay key and `item.value` bing the dicitonary value.

Add to `groups_vars/cisco.yml`:

```
os: ios
snmp_servers:
  - 10.1.1.1
  - 10.2.1.1
```

Add to `groups_vars/juniper.yml`:

```
os: junos
users:
  admin: admin123
  oper: oper123
```

Now the play to loop over the above variables:

```
---

  - name: Loops over list
    hosts: cisco
    gather_facts: no
    tasks:
      - name: Loop over SNMP servers
        debug:
          msg: "Router {{ hostname }} with snmp server {{ item }}"
        loop: "{{ snmp_servers }}"
      
  - name: Loops over a dictionary
    hosts: juniper
    gather_facts: no
    tasks:
      - name: Loop over a dictionary
        debug:
          msg: "Router {{ hostname }} with user {{ item.key }} password {{ item.value }}"
        with_dict: "{{ users }}"
```

[Ansible looping docs](https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html)

### Securing Secrets with Ansible Vault

Passwords shouldn't be stored in plain text. Ansible vault is used to encrypt and decrypt the secrets when the play is running.

The vault is encrypted with a key file specified by `--vault-id`. 

Create a file with the vault password, `vault_pass`:

    secret_password

Create a secrets file with `ansible-vault`:

    ansible-vault create --vault-id=vault_pass secrets

Add the following secrets (with vim):

    ospf_pass: ospf_P@ssword
    bgp_pass: bgp_P@ssword

Create this playbook using the `secrets` file as a `vars_file` input:

```
---

  - name: Ansible vault playbook
    hosts: all
    gather_facts: no
    vars_files:
      - secrets
    tasks:
      - name: Output OSPF Password
        debug:
          msg: "Router {{ hostname }} ospf password {{ ospf_pass }}"
        when: inventory_hostname == 'csr1'
      
      - name: Output BGP Password
        debug:
          msg: "Router {{ hostname }} bgp password {{ bgp_pass }}"
        when: inventory_hostname == 'mx1'
```

Running the play with the `vault_id`:

    ansible-playbook --vault-id=vault_pass ansible_vault.yml -i hosts

The `secrets` file can be committed to source control as the contents are AES256 encrypted:

    $ANSIBLE_VAULT;1.1;AES256
    37306566336133323037613765333835383565396536366263643839366339323264653264346635
    3836656237643461653637323534623533636261343838610a376537346534333932323365323132
    65353035326364656639363230366436613339613532306338626264663233346432633036353539
    6431366438343037300a653334636664383663663733623832623837646335336661633863343235
    39626438383334306464353462623338626538393735333233316237333636316339396531333961
    63363131663632646636646463366365363735626337386562613361626365636362396633396162
    663666393637653766653633656662306538

> Do not commit the `vault_id` file

One can also enrypt without a file and rather use a memorised password with the `--ask-vault-pass` switch. 

If no vault password or vault_id is given you will get an error:

> ERROR! Attempting to decrypt but no vault secrets found

### Using Jinja2 with Ansible

Jinja2 is a powerful templating engine for python.
We can utilise jinja to generate custom configuration files for network devices.

A `network.yml` group var stored the network config applicable to all devices.
Two jinja tempaltes are then created, one for cisco devices and one for juniper to llop over the `ntp_servers`.

Ansible's `template` module takes 2 parameters:

* `src`: the jinja2 template
* `dest`: specifies the output file

The `inventory_hostname` is used to make a unique output.

By default the `template` module creates the file on the remote managed node, however this is not possible as they are network devices.
Hence we use `delegate_to` to run the task locally on the ansible control node.

Add `group_vars/network.yml`:

```
ntp_servers:
  - 172.20.1.1
  - 172.20.2.1
```

Create a new `templates` directory and create `ios_basic.j2`:

```
hostname {{ hostname }}
!
{% for server in ntp_servers %}
ntp {{ server }}
{% endfor %}
!
```

And a `tempaltes/junos_basic.j2`:

```
set system host-name {{ hostname }}
{% for server in ntp_servers %}
set system ntp server {{ server }}
{% endfor %}
```

Create a playbook `jinja_playbook.yml`:

```
---
  - name: Generate Cisco config from Jinja2
    hosts: localhost
    gather_facts: no
    tasks:
      - name: Create Configs Directory
        file: path=configs state=directory

  - name: Generate Cisco config from Jinja2
    hosts: cisco
    gather_facts: no
    tasks:
      - name: Generate Cisco Basic Config
        template:
          src: "templates/ios_basic.j2"
          dest: "configs/{{inventory_hostname}}.cfg"
        delegate_to: localhost

  - name: Generate Juniper config from Jinja2
    hosts: juniper
    gather_facts: no
    tasks:
      - name: Generate Juniper Basic Config
        template:
          src: "templates/junos_basic.j2"
          dest: "configs/{{inventory_hostname}}.cfg"
        delegate_to: localhost
```

Generate the config with:

    ansible-playbook -i hosts jinja_playbook.yml

The first play creates the configs diredctory locally.
The second play creates the cisco configs for each host.
The third play create the juniper configs for each host.

Examples of the config created:

csr1.cfg:

```
hostname edge-csr1
!
ntp 172.20.1.1
ntp 172.20.2.1
!
```

mx1.cfg:

```
set system host-name core-mx1
set system ntp server 172.20.1.1
set system ntp server 172.20.2.1
```

> The routers should never be the source of truth. The source data for your routers should reside elsewhere. (My opinion)

[More on the Ansible template module](https://docs.ansible.com/ansible/latest/modules/template_module.html)

## Ansible Filters

Filters are used to transform and manipulate data. Ansible filters are derived from jinja2 filters.

> You might need python's `netaddr` package for network filters

Create a new play `filters_playbook.yml`:

```
---
  - name: Ansible Filters
    hosts: csr1
    gather_facts: no
    vars:
      interfaces:
        - { port: FastEthernet0/0, prefix: 10.1.1.0/24 }
        - { port: FastEthernet1/0, prefix: 10.1.2.0/24 }
    tasks:
      - name: Generate Interface Config
        blockinfile:
          block: |
            hostname {{ hostname | upper }}
            {% for intf in interfaces %}
            !
            interface {{ intf.port }}
              ip address {{intf.prefix | ipv4(1) | ipv4('address') }} {{intf.prefix | ipv4('netmask') }}
            !
            {% endfor %}
          dest: "configs/csr1_interfaces.cfg"
          create: yes
        delegate_to: localhost
```

Output of `csr_interfaces.cfg`:

    # BEGIN ANSIBLE MANAGED BLOCK
    hostname EDGE-CSR1
    !
    interface FastEthernet0/0
    ip address 10.1.1.1 255.255.255.0
    !
    !
    interface FastEthernet1/0
    ip address 10.1.2.1 255.255.255.0
    !
    # END ANSIBLE MANAGED BLOCK

`blockinfile` is similar to template but uses text in the file as the source, not a file.

> Remeber to set `gather_facts: no` otherwise ansible will attempt to log into the device and gather facts first

* `{{ hostname | upper }}` - uppercase
* `{{ intf.prefix | ipv4(1) | ipv4('address') }}` - `ipv4(1)` prints the first ip in the prefix, `ipv4('address')` gets only the address portion of the prefix
* `{{ intf.prefix | ipv4('netmask') }}` - get the netmask for the prefix

### Ansible Tags

Tool to tag specific tasks in a large ansible playbook. 
So we can choose what tasks are run based on the tags.

This allows us to run the same playbook for different scenarios.

> With no tags specified - all tasks will be run

Create `tags_playbook.yml`:

```
---
  - name: Using Ansible Tags
    hosts: cisco
    gather_facts: no
    tasks:
      - name: Print OSPF
        debug:
          msg: "Router {{ hostname }} will Run OSPF"
        tags: [ospf, routing]

      - name: Print BGP
        debug:
          msg: "Router {{ hostname }} will Run BGP"
        tags:
          - bgp
          - routing

      - name: Print NTP
        debug:
          msg: "Router {{ hostname }} will run NTP"
        tags: ntp
```

Run the play with different tags:

    $ ansible-playbook tags_playbook.yml -i hosts --tags ospf

    PLAY [Using Ansible Tags] ***********************************************************************

    TASK [Print OSPF] *******************************************************************************
    ok: [csr1] => {
        "msg": "Router edge-csr1 will Run OSPF"
    }
    ok: [csr2] => {
        "msg": "Router edge-csr2 will Run OSPF"
    }

    PLAY RECAP **************************************************************************************
    csr1                       : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    csr2                       : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

and routing:

    $ ansible-playbook tags_playbook.yml -i hosts --tags routing

    PLAY [Using Ansible Tags] ***********************************************************************

    TASK [Print OSPF] *******************************************************************************
    ok: [csr1] => {
        "msg": "Router edge-csr1 will Run OSPF"
    }
    ok: [csr2] => {
        "msg": "Router edge-csr2 will Run OSPF"
    }

    TASK [Print BGP] ********************************************************************************
    ok: [csr1] => {
        "msg": "Router edge-csr1 will Run BGP"
    }
    ok: [csr2] => {
        "msg": "Router edge-csr2 will Run BGP"
    }

    PLAY RECAP **************************************************************************************
    csr1                       : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    csr2                       : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 

[More on tags](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html)

### Customising Ansible Settings

Settings can be adjusted with `ansible.cfg` file. 

Create a `ansible.cdfg` file in the same directory as you are working.

    [defaults]
    inventory=hosts
    vault_password_file=vault_pass
    gathering=explicit

The default config file is at `/etc/ansible/ansible.cfg` but this will affect every playbook on the control machine. It is better to include a `ansible.cfg` in the project directory.

* `inventory`: sets the default inventory so you can stop using `-i hosts`
* `vault_password_file`: sets the vault password so we needn't use `--vault-id`
* `gathering = explicit`: By default ansible runs the `setup` module to gather facts of the managed nodes. It is not compatible with network nodes as they need `python`. This disables `gather_facts` by default.

[More on Ansible Config](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings)

### Using Ansible Roles

Ansible role is collected package of tasks, templates, handlers. It promote code re-use.

    mkdir roles
    cd roles
    ansible-galaxy init basic_config

This creates a default role layout.

In `roles/basic_config/vars/main.yml`:

```
---
config_dir: basic_config
```

In `roles/basic_config/tasks/main.yml`:

```
---
- name: Create config directory
  file:
    path: "{{ config_dir }}"
    state: directory
  run_once: yes

- name: Generate Cisco basic config
  template:
    src: "{{ os }}.j2"
    dest: "{{ config_dir }}/{{ inventory_hostname }}.cfg"
```

In `roles/basic_config/templates/ios.j2`:

    hostname {{ hostname }}
    !
    {% for server in ntp_servers %}
    ntp {{ server }}
    {% endfor %}

In `roles/basic_config/tempaltes_junos.j2`:

    set system host-name {{ hostname }}
    {% for server in ntp_servers %}
    set system ntp server {{ server }}
    {% endfor %}

Create a new playbook in the chapter root `role_playbook.yml`:

```
---
  - name: Build basic config using Roles
    hosts: all
    connection: local
    roles:
      - basic_config
```

Run the play:

    ansible-playbook role_playbook.yml

This does the same as our previous work but in a more reusable way where we can import the role.

Ansible looks for roles:

* In the current working directory `roles` folder
* `/etc/ansible/roles`

[More on roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)

## 2. Managing Cisco iOS devices using Ansible

Get the book if you want more info on this, I might revisit it but I'm more interested in the Juniper info for now...

## 3. Automating Juniper Devices in Service Providers using Ansible





## Source

* [Network Automation Cookbook - Karim Okasa](https://www.packtpub.com/product/network-automation-cookbook/9781789956481)
