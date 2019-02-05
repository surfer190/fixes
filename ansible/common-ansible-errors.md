# Common Ansible Error Messages and Solutions

#### Error: Failed to lock apt for exclusive operation

    failed: [default] => {"failed": true} msg: Failed to lock apt for exclusive operation

**Solution**

`apt` needs to be run as `sudo`

Add `become: yes` to top of playbook


    - hosts: webserver
      become: yes
      tasks:
        - name: Updates apt cache
          action: apt update_cache=true

#### Error: msg: No package matching 'XXXXX' is available

  failed: [default] => (item=XXXXX) => {"failed": true, "item": "XXXXX"}
  msg: No package matching 'XXXXX' is available

**Solution**

That package does not exist. Usually a type of missing a version

Eg. `php-mysql` => `php5-mysql`

#### Error: XXXXX.co.za has an unknown hostkey. Set accept_hostkey to True or manually add the hostkey prior to running the git module

  failed: [default] => {"failed": true}
  msg: XXXXX.co.za has an unknown hostkey. Set accept_hostkey to True or manually add the hostkey prior to running the git module

##### Solution

  Add the host key manually

### ERROR! template error while templating string: expected token 'end of print statement', got 'key'

```
fatal: [localhost]: FAILED! => {"failed": true, "msg": "ERROR! template error while templating string: expected token 'end of print statement', got 'key'"}
```

This is usually an issue with a variable containing a space

`ssh_pub_key={{ public key }}`

Should be:

`ssh_pub_key={{ public_key }}`

Source: [Stackoverflow](http://stackoverflow.com/questions/31295662/ansible-copy-fails-template-error)

#### Sources

* [Six Ansible Practices](http://hakunin.com/six-ansible-practices)
