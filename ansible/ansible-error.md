# Common Ansible Error Messages and Common Solutions

### Error: Failed to lock apt for exclusive operation

```
failed: [default] => {"failed": true} msg: Failed to lock apt for exclusive operation
```

##### Solution

`apt` needs to be run as `sudo`

Add `sudo: yes` to top of playbook

```
- hosts: webserver
  sudo: yes
  tasks:
    - name: Updates apt cache
      action: apt update_cache=true
```

### Error: msg: No package matching 'XXXXX' is available

```
failed: [default] => (item=XXXXX) => {"failed": true, "item": "XXXXX"}
msg: No package matching 'XXXXX' is available
```

##### Solution

That package does not exist. Usually a type of missing a version

Eg. `php-mysql` => `php5-mysql`

### Error: XXXXX.co.za has an unknown hostkey. Set accept_hostkey to True or manually add the hostkey prior to running the git module

```
failed: [default] => {"failed": true}
msg: XXXXX.co.za has an unknown hostkey. Set accept_hostkey to True or manually add the hostkey prior to running the git module
```

##### Solution



Source: [Six Ansible Practices](http://hakunin.com/six-ansible-practices)
