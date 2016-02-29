#Ansible Ad-hoc command

#### Ping

```
ansible [group-name] -m ping -u [username]
```

#### Show all facts

```
ansible [host/group] -m setup -u [username] -i [inventory file]
```

Source: [Ansible docs - Fathering facts](http://docs.ansible.com/ansible/intro_adhoc.html#gathering-facts)
