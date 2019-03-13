# AWX Ansible Best Practices

AWX is a web-based user interface, REST API, and task engine for ansible.
It is an upstream project for tower, a commercial derivative of AWX.

* AWX manages your inventory
* [molecule](https://molecule.readthedocs.io/en/latest/) can be used for testing of ansible roles

Pointers:
* Never manually edit stuff in docker containers
* Playbooks should reference tested roles
* Playbooks and roles should be stored in git
* Playbooks should almost exclusively use roles

## AWX project structure

* `*.yml` playbooks in the root
* `roles` folder with a `requirements.yml` pointing to the roles used in your playbook
* `host_vars` folder for host variables
* `group_vars` folder for group variables
* `files` folder (optional) containing SSH keys and certificate files

Dependencies can be isntalled with `local_action` or `deletegate_to`

