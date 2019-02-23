# Intro to Ansible Network Automation

> Network infrastructure is still managed today the same way it was many years ago

* collection of scripts
* node by node
* handcrafted and CLI driven

### Why Ansible?

1. It is similar to how network people work already - Same cli and config commands
2. Agentless - No need for third party services
3. Simplicity

## Configuration Automation

* Multi-vendor networks - ansible abstracts the device specific implementation away
* gathering of facts - discovering devices, operating systems and capabilities of the devices
* Only changes whet needs to be changed
* Don't have to get bogged down in vendor speak, focus on roles and tasks

## Test-driven Deployment

How do network operators test today?

* CLI commands like `show`
* Device specific utilities
* Homegrown and one-off scripts

The test driven deployment is essentially a playbook that is verifying certain responses from the cli.
It then has a when clause to do certain things when there is a speicfic response.

## Continuous Compliance

Continually monitoring the network configuration network and state

Eliminate configuration drift

* validate that configuration statements are correct
* state is correct

1. playbooks can be scheduled to run
2. it will find network devices that are out of compliance

#### Source

* [Ansible Network Automation](https://www.ansible.com/overview/networking)
