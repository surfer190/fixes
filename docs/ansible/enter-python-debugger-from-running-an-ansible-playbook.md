---
author: ''
category: Ansible
date: '2020-05-13'
summary: ''
title: Enter Python Debugger From Running An Ansible Playbook
---
# Enter the python debugger from Running an Ansible Playbook

I have some other strategies below but when we really want to do it do get access to `pdb` or `ipdb` when running a play.
The ansible [developer guide has a section on debugging](https://docs.ansible.com/ansible/latest/dev_guide/debugging.html).

Ansible modules don't work like any other python files.
They are wrapped up with a script and put into a zip file. _Why?_

The article mentions [Simple Debugging using epdb](https://docs.ansible.com/ansible/latest/dev_guide/debugging.html#simple-debugging)

**Simple is better than complex** so let us try it

## Simple Debugging

Apparently all you need to do is:

    pip install epdb

Into your virtual env.

Then add this line anywhere in the module where you have an issue.

    import epdb; epdb.serve()

The line where you have the issue can usually be found by running your playbook in verbose mode `-vvvv`

From the [epdb docs](https://pypi.org/project/epdb/):

> To debug code that is either running on a remote system, or in a process that isn’t attached to your tty you can use epdb in server mode

Now run your playbook and it should hang at a point. So now you can connect to the server with:

    ipython
    import epdb
    epdb.connect()

It worked for me but I couldn't control it...by stepping through. Ie `c`, `s` and `n` did not work.
Not even `h` (help) so I don't think it ever got into `epdb`

What you can do is debug by outputing to the terminal - but not `print()` statements do not work in modules so it is better to use:

    raise Exception(some_value)




### Debug Strategy

It depends on your play `strategy`.

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
* [Ansible developer guide: Debugging](https://docs.ansible.com/ansible/latest/dev_guide/debugging.html)