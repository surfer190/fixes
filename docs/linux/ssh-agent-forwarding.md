---
author: ''
category: Linux
date: '2019-09-23'
summary: ''
title: Ssh Agent Forwarding
---
# SSH Agent Forwarding

## What is SSH Agent Forwarding

Method that allows us to chain ssh connections to forward key challenges back to the original agent.
So if your local user has access to a git repo, you can forward that agent for when you are logged into remote computers.

## Setup

To setup SSH agent forwarding

In `.ssh/config`:

    Host Server_Address
        ForwardAgent yes

Ensure your local key is added in the ssh-add list:

    ssh-add -L

If not add it to the SSH Agent (Apparently you have to do this after every reboot)

    ssh-add -K

Connect (SSH) to the remote machine

Check that forwarding is enabled with: `echo "$SSH_AUTH_SOCK"`

Ensure you can access what you want:

    ssh -T git@github.com




## Sources

* [SSH Agent Forwarding](http://www.unixwiz.net/techtips/ssh-agent-forwarding.html)
* [SSH Agent not working](https://stackoverflow.com/questions/21522081/ssh-agent-forwarding-not-working)