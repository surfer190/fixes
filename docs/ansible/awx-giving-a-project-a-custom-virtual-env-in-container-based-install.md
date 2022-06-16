---
author: ''
category: Ansible
date: '2020-05-13'
summary: ''
title: Awx - Give a Project a Custom Virtual Env
---
## AWX How to give a Project a Custom VirtualEnv in the container based Install

When you create a new project on AWX you get the following screen

![AWX new project no custom environments](/img/awx/awx-new-project-no-custom-environment.png){: class="img-fluid" }

It does not have the `Ansible Environment` field as no custom environments are setup.

Sometimes certain playbooks need extra dependencies that don't make sense to setup in the default ansible virtual environment

So let us try and set it up. I will be using the [AWX documentation on setting up custom venvs](https://github.com/ansible/awx/blob/devel/docs/custom_virtualenvs.md)

Our AWX instance was installed with the docker compose method and hence it is running in containers.
 
You will see the following contianers:

    docker ps

    CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                                                 NAMES
    351190a1796b        postgres:9.6                 "docker-entrypoint.s…"   11 months ago       Up 24 hours         5432/tcp                                              postgres
    eaaa7c833053        ansible/awx_task:3.0.1       "/tini -- /bin/sh -c…"   11 months ago       Up 24 hours         8052/tcp                                              awx_task
    dfa79d5a48d7        ansible/awx_web:3.0.1        "/tini -- /bin/sh -c…"   11 months ago       Up 24 hours         0.0.0.0:80->8052/tcp                                  awx_web
    517f39e0d8d0        memcached:alpine             "docker-entrypoint.s…"   11 months ago       Up 24 hours         11211/tcp                                             memcached
    f16b15845a94        ansible/awx_rabbitmq:3.7.4   "docker-entrypoint.s…"   11 months ago       Up 24 hours         4369/tcp, 5671-5672/tcp, 15671-15672/tcp, 25672/tcp   rabbitmq

The one we are focused on is `ansible/awx_task`

So let's get into that docker container:

    docker exec -it awx_task /bin/bash

we are in the `/var/lib/awx` folder and can see the `venv` folder in this directory

    [root@awx awx]# pwd
    /var/lib/awx

The recommendation is to create the `venv` in `/opt`

So lets go there and create the folder:

    cd /opt
    mkdir custom_venvs

You then need to tell awx the directory to look in for custom `venvs`:

    HTTP PATCH /api/v2/settings/system/ {'CUSTOM_VENV_PATHS': ["/opt/custom_venvs/"]}

Now create the venv in that folder

    cd /opt/custom_venvs
    python3 -m venv vdc_venv

Now install dependencies

    source /opt/custom_venvs/vdc_venv/bina/activate
    pip install psutil
    pip install -U "ansible == 2.9.1"
    pip install -r requirements.txt
    
**Oops** You can't actually install stuff because the container doesn't have `gcc`

    distutils.errors.CompileError: command 'gcc' failed with exit status 1

So what you have to [do is install `yum install -y gcc` in the container - like a maniac](https://stackoverflow.com/questions/52371437/how-to-configure-awx-for-using-an-unreleased-version-of-ansible). 
Whoops...it still does not work.

So tried without `psutils`:

    pip install -U "ansible == 2.7.6"

Finally found that the way to do it was add the `venv` to both the `awx_task` and `awx_web` containers in the `/var/lib/awx/venv` folder and then they will just pick up.

Thanks to this [stackoverflow answer for that](https://stackoverflow.com/questions/55462012/awx-custom-virtual-environments-not-showing-up)

It is still a fuckup though...cause my playbook needed a python 3 interpreter and it errored out woth:

    Traceback (most recent call last):
    File "/usr/local/bin/ansible", line 30, in <module>
        import shutil
    File "/usr/lib64/python3.6/shutil.py", line 10, in <module>
        import fnmatch
    File "/usr/lib64/python3.6/fnmatch.py", line 14, in <module>
        import re
    File "/usr/lib64/python3.6/re.py", line 142, in <module>
        class RegexFlag(enum.IntFlag):
    AttributeError: module 'enum' has no attribute 'IntFlag'

when I set 

    ansible_python_interpreter: /usr/bin/python3

on the host

Maybe we can create the environment on the host and mount it into the container (just need to ensure the python version is correct)

    Python 3.6.6 (default, Aug 13 2018, 18:24:23) 
    
> On second thought - fuck it....too much work

I'm just going to install the dependencies on the local env

Now you are done

> Please note this does not have persistence. If you destroy your container the venv will disappear and you have to recreate.

Ideally the custom venv setup should be part of the deployment process

## Update: Use the custom_venv_dir Variable

In your awx deployment inventory there is a variable called: `custom_venv_dir`

If you set that (only works on a local install)...the custom venv directory will be created on the host and bind mounted into the relevant docker containers:

Eg.

    custom_venv_dir: '/opt/awx-custom-venvs/'

Now you can createa an manage your venv on the host and it will be mirrored into the containers.

You still need to [assign the virtualenv to the org](https://github.com/ansible/awx/blob/devel/docs/custom_virtualenvs.md#assigning-custom-virtualenvs)

Easiest to do form the browsable API:

Go to `v2/settings/system/` and patch:

    {"CUSTOM_VENV_PATH":["/opt/awx_venvs"]}

Actually the easiest is to jsut go to Setting -> System on the frontend and set it.
