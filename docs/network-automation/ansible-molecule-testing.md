---
author: ''
category: Network-Automation
date: '2019-03-14'
summary: ''
title: Ansible Molecule Testing
---
# Ansible Molecule Testing

Molecule aids in the development and testing of Ansible roles.

> Red Hat took over development of Molecule in September 2018d 

## Installation

See the [ansible molecule installation](https://molecule.readthedocs.io/en/latest/installation.html) notes

    pip install --user molecule

## Getting Started

Generate a new role

    molecule init role -r my-new-role

> To initialise molecule within an existing role

    molecule init scenario -r my-role-name

The following folders are generated:

    $ ls
    README.md  defaults/  handlers/  meta/      molecule/  tasks/     vars/

* `molecule/` - contains various scenarios - test suites for created roles. You can have as many scenarios as you want and run one after the other

The scenario `default` contains:

    $ ls
    Dockerfile.j2  INSTALL.rst    molecule.yml   playbook.yml   tests/

* `Dockerfile.j2` is the jinja template file used to create a docker image to test your role against
* `INSTALL.rst` install instructions on additional software or steps for molecule to interface with the driver
* `molecule.yml` central configuration entry point
* `playbook.yml` the playbook run against the driver
* `tests/` is the test directory as molecule uses `test infra` as the default verifier. Allowing you to run specific tests about the state of a container after the playbook is run.

### Molecule.yml

Configures the components

* `dependency` - dependency manager (ansible galaxy)
* `driver` - the provider of the instance to test against (docker, azure, ec2, linode)
* `lint` - enforce best practices when writing yaml
* `platforms` - name (distrribution) and the group it belongs to
* `provisioner`
* `scenario` - control scenario sequence order
* `verifier` - package that is doing the state tests (TestInfra)

### Running a test sequence

> Using a virtual env in benefitial

Ensure you have everything you need installed in:

    test-role/molecule/default/INSTALL.rst

Check docker is running with a sanity check:

    docker run hello-world

Tell molecule to create the instance

    molecule create

Verify that the instance has been created with

    molecule list

Add a task to `test-role/tasks/main.yml`:

    - name: Molecule Hello World!
      debug:
        msg: Hello, World!

Tell molecule to test the role against the instance:

    molecule converge

To manually inspect the instance afterwards:

    molecule login

Destroy the instance with:

    molecule destroy

> The `--debug` option can be used to get more verbose output

### Full Test Suite

To run the full sequence of tests:

    molecule test

> Tell molecule not to destroy if the test fails: `--destroy=never`

### Source:

* [Molecule: Read the docs](https://molecule.readthedocs.io/en/latest/index.html)


