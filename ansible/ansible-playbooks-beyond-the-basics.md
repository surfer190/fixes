# Ansible Playbooks: Beyond the Basics

### Using Handlers

    handlers:
        - name: restart apache
          service: name=apache2 state=restarted

    tasks:
        - name: Enable Apacherewrite module
          apache2_module: name=rewrite state=present
          notify: restart apache

##### Notify Multiple Handlers

  - name: Rebuild application configuration.
    command: /opt/app/rebuild.sh
    notify:
      - restart apache
      - restart memcached

##### Have one Notifier Notify Another

  handlers:
    - name: restart apache
      service: name=apache2 state=restarted
      notify: restart memcached

      - name: restart memcached
        service: name=memcached state=restarted

##### Considerations

* Skipped Tasks do not run Handlers
* Handlers run once, and only once, at the end of a play.
* If a play fails before handlers ate notified, the handlers will never run.

### Environment Variables

Adding line to remote user account in `.bash_profile`:

  - name: Add an environment variable to the remote user's shell.
    lineinfile: dest=~/.bash_profile regexp=^ENV_VAR= line=ENV_VAR=value

_Only available to the shell command_

##### Using the `register`

  - name: Add an environment variable to the remote user's shell.
    lineinfile: dest=~/.bash_profile regexp=^ENV_VAR= line=ENV_VAR=value

  - name: Get the value of the environment variable we just added.
    shell: 'source ~/.bash_profile && echo $ENV_VAR'
    register: foo

  - name: Print the value of the environment variable.
    debug: msg="The variable is {{ foo.stdout }}"

##### Adding to Linux Environment Variables

  - name: Add a global environment variable.
    lineinfile: dest=/etc/environment regexp=^ENV_VAR= line=ENV_VAR=value
    sudo: yes

##### Per Play Environment Variables

Use the `environment` option for a file download url for example.

  - name: Download a file, using example-proxy as a proxy.
    get_url: url=http://www.example.com/file.tar.gz dest=~/Downloads/
    environment:
      http_proxy: http://example-proxy:80/

That can become quite cumbersome so sometimes it is better to use a `vars` section

##### `vars` Section

  vars:
    var_proxy:
      http_proxy: http://example-proxy:80/
      https_proxy: https://example-proxy:443/
      [etc...]
    tasks:
    - name: Download a file, using example-proxy as a proxy.
      get_url: url=http://www.example.com/file.tar.gz dest=~/Downloads/
      environment: var_proxy

##### Set a System wide Proxy (For Corporate Firewalls)

in `/etc/environment`:

# In the 'vars' section of the playbook (set to 'absent' to disable proxy):

  proxy_state: present
    # In the 'tasks' section of the playbook:
    - name: Configure the proxy.
      lineinfile:
      dest: /etc/environment
      regexp: "{{ item.regexp }}"
      line: "{{ item.line }}"
      state: "{{ proxy_state }}"
    with_items:
      - { regexp: "^http_proxy=", line: "http_proxy=http://example-proxy:80/" }
      - { regexp: "^https_proxy=", line: "https_proxy=https://example-proxy:443/" }
      - { regexp: "^ftp_proxy=", line: "ftp_proxy=http://example-proxy:80/" }

####### Testing a Remote Variable

  ansible test -m shell -a 'echo $TEST'

### Variables

variables same as `python` but better to use jsut smalls and avoid numbers.

##### Assignments

In an **inventory** file:

  foo=bar

In a **playbook**:

  foo: bar

##### Playbook Variables

Passing in with command line:

  ansible-playbook example.yml --extra-vars "foo=bar"

Pass in a `json` or `yaml` file:

-extra-vars "@even_more_vars.json"

In Playbook:

  ---
  - hosts: example
    vars:
      foo: bar
    tasks:
      # Prints "Variable 'foo' is set to bar".
      - debug: msg="Variable 'foo' is set to {{ foo }}"

Or with a file `vars_files`:

  ---
  # Main playbook file.
  - hosts: example
    vars_files:
      - vars.yml
    tasks:
      - debug: msg="Variable 'foo' is set to {{ foo }}"

Variables in `vars.yml`:

    ---
    # Variables file 'vars.yml' in the same folder as the playbook.
    foo: bar

##### Conditionally importing a vars file

Say you have `centOS` which uses `httpd` and `debian` that uses `apache2`:

`apache_CentOS.yml`

`apache_-default.yml`

    ---
      - hosts: example
        vars_files:
          - [ "apache_{{ ansible_os_family }}.yml", "apache_default.yml" ]
        tasks:
          - service: name={{ apache }} state=running

##### Inventory Variables

Example of entire setting variables inline and for a group:

  # Host-specific variables (defined inline).
  [washington]
  app1.example.com proxy_state=present
  app2.example.com proxy_state=absent
  # Variables defined for the entire group.

  [washington:vars]
  cdn_host=washington.static.example.com
  api_version=3.0.1

####### Best Practice

_Ansible’s documentation recommends not storing variables within the inventory. Instead, you can use group_vars and host_vars YAML
variable files within a specific path, and Ansible will assign them to individual hosts and groups
defined in your inventory_

For a host `app1.example.com`, create:

```
/etc/ansible/host_vars/app1.example.com
```

and add variables as normal:

```
---
foo: bar
baz: qux
```

For a group of hosts, create:

```
/etc/ansible/group_vars/washington
```

####### Magic Vars in Host and Group Vars

If you ever need to retrieve a specific host’s variables from another host, Ansible provides a magic
hostvars variable containing all the defined host variables.

```
# From any host, returns "jane".
{{ hostvars['host1']['admin_user'] }}
```

### Registered Variables

Ansible allows you to use register to store the output of a particular command in a variable at runtime

Eg.

```
- name: "Node: Check list of Node.js apps running."
  command: forever list
  register: forever_list
  changed_when: false

- name: "Node: Start example Node.js app."
  command: forever start {{ node_apps_location }}/app/app.js
  when: "forever_list.stdout.find('{{ node_apps_location}}/app/app.js') == -1"
```
### Accessing Variables

Simple variables (gathered by Ansible, defined in inventory files, or defined in playbook or variable
files) can be used as part of a task using syntax like `{{ variable }}` .

```
- command: /opt/my-app/rebuild {{ my_environment }}
```

##### Lists
A list is defined:

```
foo_list:
- one
- two
- three
```

Accessing the first element:

```
foo[0]      #python
foo|first   #jinja
```

##### Retrive info of large object

To Retrieve info about `eth0` network interface:

```
# In your playbook.
tasks:
  - debug: var=ansible_eth0
```

Knowing the structure of the variable you can now access elements:

```
{{ ansible_eth0.ipv4.address }}
{{ ansible_eth0['ipv4']['address'] }}
```

### Facts - Variables derived from system information

Get a list of Facts

```
ansible <host> -m setup
```

### Variable Preference

1. Command line always wins
2. Connection variables in the inventory file
3. Normal varialbles
4. Other Inventory Variables
5. Local facts with `gather_facts`
6. Role default variables `defaults/maain.yml`

_roles should provide sane defaults_
_playbooks should rarely define variables_
_command line variables should be avoided where possible_
