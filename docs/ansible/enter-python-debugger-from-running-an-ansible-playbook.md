---
author: ''
category: Ansible
date: '2020-05-13'
summary: ''
title: Enter Python Debugger From Running An Ansible Playbook
---
# Enter the python debugger from Running an Ansible Playbook

I don't think you can.
I think ansible basically throws execution somewhere else so breakpoints aren't accessible to the caller.

Actually you can but it depends on your play `strategy`.

### Debug Strategy

Set

    - hosts: all
      connection: local
      strategy: debug

It will then brek on a failing task:

    [localhost] TASK: create org (debug)>

You can then get the output of the json args sent to a module or task. Get the task arguments as JSON with:

    {
        'org_name': 'TEST0002',
        'full_name': 'Test VCD ORG',
        'is_enabled': 'true',
        'state': 'present',
        '_ansible_check_mode': False,
        '_ansible_no_log': False,
        '_ansible_debug': False,
        '_ansible_diff': False,
        '_ansible_verbosity': 0,
        '_ansible_version': '2.9.7',
        '_ansible_module_name': 'vcd_org', '_ansible_syslog_facility': 'LOG_USER', '_ansible_selinux_special_fs': ['fuse', 'nfs', 'vboxsf', 'ramfs', '9p', 'vfat'], '_ansible_string_conversion_action': 'warn', '_ansible_socket': None,
        '_ansible_shell_executable': '/bin/sh', '_ansible_keep_remote_files': False,
        '_ansible_tmpdir': '/Users/stephen/.ansible/tmp/ansible-tmp-1588670617.1317708-64312-102300914438839/', '_ansible_remote_tmp': '~/.ansible/tmp'
    }

More things you can do is avaialable in the [ansible debugger docs](https://docs.ansible.com/ansible/latest/user_guide/playbooks_debugger.html)


### Module Utils

Module utils can be accessed via the `ansible.module_utils.<your_name_here>`

The problem is when runnign the module directly the module utils won't be in the python path and you will get an error

    python modules/vcd_org.py ./test_args.json
    Traceback (most recent call last):
    File "modules/vcd_org.py", line 102, in <module>
        from ansible.module_utils.vcd import VcdAnsibleModule
    ModuleNotFoundError: No module named 'ansible.module_utils.vcd'

> how to get the ansible search path when running module directly

You can find the path with:

    ansible-config dump| grep MODULE_UTILS_PATH

However it looks to be a limitation of ansible to bring in the custom ansible `module_utils` as per the [google forum](https://groups.google.com/forum/#!topic/ansible-devel/A2oIPUx9jFY)

## Hacky solution

Copy the files from module utils into your module library and then just update the references of `from ansible.module_utils.<package>.` to `from <package>`

### Sources

* [Debug ansible playbooks](https://blog.codecentric.de/en/2017/06/debug-ansible-playbooks-like-pro/)
* [Ansible Docs: Developing Module Utilities](https://docs.ansible.com/ansible/latest/dev_guide/developing_module_utilities.html)
* [Writing an Ansible Module](https://dev.to/drewmullen/how-to-run-simple-tests-against-custom-ansible-modules-4875)
