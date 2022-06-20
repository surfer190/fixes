---
author: ''
category: Ansible
date: '2022-03-15'
summary: ''
title: Awx - Get a List of Available Collections in your Execution Environment
---
# Awx - Get a List of Available Collections in your Execution Environment

Sometimes when building an execution environment image we aren't explicit about the version. Then later we want to know the actual version of a collection or python package the image is using.

To check the list of collections do the following

1. Pull and run the docker image locally and enter the shell:

        docker pull harbor.example.org/awx-execution-envs/ee-example:1.0.2
        docker run -ti harbor.example.org/awx-execution-envs/ee-example:1.0.2 /bin/sh

        > `-ti` tells docker to allocate a `tty` and indicates it is an interactive session

2. List out the collections with:

        ansible-galaxy collection list
        
        # /usr/share/ansible/collections/ansible_collections
        Collection            Version
        --------------------- -------
        ansible.netcommon     2.4.0  
        ansible.utils         2.3.1  
        community.general     3.6.0  
        junipernetworks.junos 2.5.0 

3. List out python packages and versions:

        sh-4.4# pip freeze
        ansible-core @ file:///output/wheels/ansible_core-2.11.4.post0-py3-none-any.whl
        ansible-pylibssh==0.2.0
        ansible-runner @ file:///output/wheels/ansible_runner-2.0.0.0a4.dev130-py3-none-any.whl
        asn1crypto==1.2.0
        attrs==21.2.0
        Babel==2.7.0
        bcrypt==3.2.0

## Sources

* [Listing collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#listing-collections)