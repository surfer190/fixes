---
author: ''
category: Ansible
date: '2021-08-24'
summary: ''
title: Awx Moving Custom Venvs to Execution Environments
---
## Ansible Execution Environments

> The only constant is change

AWX version 18.0 (ansible tower 3.8) introduced exeuction environments as a drop in replacement of the custom venvs....

For my AWX instance we moved from AWX 13.0.0 to 19.2.2. AWX releases frequently.

On the project level there will be a warning saying:

    custom virtual environment /opt/xxx must be replaced by an execution environment
    
Well what the hell is a execution enviornment...

### Execution Environments

> As with most things the source of truth for awx is the [awx docs folder](https://github.com/ansible/awx/tree/devel/docs)

The [awx execution environments](https://github.com/ansible/awx/blob/devel/docs/execution_environments.md) docs is not that great...it doesn't really guide you and it introduces you to `awx-manage` a utility that is unknown to me.

For a better explanation I went to the [ansible-runner docs](https://ansible-runner.readthedocs.io/en/latest/execution_environments.html#):

> Execution Environments are meant to be a consistent, reproducible, portable, and sharable method to run Ansible Automation jobs in the exact same way on your laptop as they are executed in Ansible AWX. This aids in the development of automation jobs and Ansible Content that is meant to be run in Ansible AWX, Ansible Tower, or via Red Hat Ansible Automation Platform in a predictable way.

> More specifically, the term Execution Environments within the context of Ansible Runner refers to the container runtime execution of Ansible via Ansible Runner within an OCI Compliant Container Runtime using an OCI Compliant Container Image that appropriately bundles Ansible Base, Ansible Collection Content, and the runtime dependencies required to support these contents. The base image is the Red Hat Enterprise Linux Universal Base Image and the build tooling provided by Ansible Builder aids in the creation of these images.

> All aspects of running Ansible Runner in standalone mode (see: Using Runner as a standalone command line tool) are true here with the exception that the process isolation is inherently a container runtime (podman by default).

[Ansible builder docs](https://ansible-builder.readthedocs.io/en/latest/index.html) also has a decent definition:

> Execution Environments are container images that serve as Ansible control nodes. Starting in version 2.0, ansible-runner can make use of these images

An Execution Environment is expected to contain:

* Ansible
* Ansible Runner
* Ansible Collections
* Python and/or system dependencies of:
    - modules/plugins in collections
    - content in ansible-base
    - custom user needs

An important part, of the AWX docs, it mentions is about migrating from custom environments:

    awx-manage list_custom_venvs
    awx-manage custom_venv_associations
    awx-manage export_custom_venv

`awx-manage export_custom_venv -q` .. command can be a starting point for writing an ansible-builder definition file

The problem for me is:

    $ awx-manage
    -bash: awx-manage: command not found

Where must this be run if awx is running on containers in kubernetes...

### AWX Manage

Perhaps it is talking about the [AWX cli](https://github.com/ansible/awx/blob/devel/INSTALL.md#installing-the-awx-cli)

I create an env and install it:

    python3 -m venv env
    source env/bin/activate
    pip3 install awxkit

But this only installs `awx`, we want the `awx-manage` binary...

I read on a github issue that:

> awx-manage is an executable that's available inside awx containers

To get the list of containers you can't just ask kubernetes for them...you have to use some jsonpath trickery:

    kubectl get po --namespace=awx-dev -o jsonpath={.items[*].spec.containers[*].name}
    redis awx-dev-web awx-dev-task awx-dev-ee

The docs on the [awx-manage](https://docs.ansible.com/ansible-tower/latest/html/administration/tower-manage.html) utility don't say which container it is available in.

I am guessing it is in `awx-dev-web`...and after entering the shell of that container - it is.
However there are no `venvs` found.
So I try `awx-dev-task` and get the same error:

    awx-manage list_custom_venvs
    2021-08-24 09:53:52,511 WARNING  [-] awx.conf.settings The current value "['/opt/awx_venvs']" for setting "CUSTOM_VENV_PATHS" is invalid.
    ....
    rest_framework.exceptions.ValidationError: [ErrorDetail(string='/opt/awx_venvs is not a valid path choice.', code='path_error')]
    No custom virtual environments detected in:
    /var/lib/awx/venv

On AWX 13.0.0, the `list_custom_venvs` command does not exist.

## How to set an execution environment for a project in AWX

In AWX you can set the `default execution environment` for a project, it will popup with this window:

![AWX default execution environment](/img/awx/awx-default-execution-environments.png){: class="img-fluid" }

You can add a new execution environment from the `Administration tab`:

![AWX add execution environment](/img/awx/awx-add-execution-environment.png){: class="img-fluid" }

At the core - the execution environment is just a container with the components listed above in the builder docs - Ansible, Ansible Runner, Ansible Collections, Python modules/plugins in collections, content in ansible-base, custom user needs

![AWX execution environment is an OCI compliant image](/img/awx/awx-new-execution-environment.png){: class="img-fluid" }

So all we need to do is create a new container image with ansible, ansible runner, our required collections and python modules are push it to a registry. 

### Creating the Image

Going through the `ansible-builder` docs:

1. Install

    python3 -m venv env
    source env/bin/activate
    pip install ansible-builder

2. Create the execution environment definition schema:

    ---
    version: 1

    build_arg_defaults:
    EE_BASE_IMAGE: 'quay.io/ansible/ansible-runner:stable-2.10-devel'

    ansible_config: 'ansible.cfg'

    dependencies:
    galaxy: requirements.yml
    python: requirements.txt
    system: bindep.txt

    additional_build_steps:
    prepend: |
        RUN whoami
        RUN cat /etc/os-release
    append:
        - RUN echo This is a post-install command!
        - RUN ls -la /etc

    * The EE_BASE_IMAGE build arg specifies the parent image for the execution environment.
    * When using an ansible.cfg file to pass a token and other settings for a private account to an Automation Hub server, listing the config file path here (as a string) will enable it to be included as a build argument in the initial phase of the build.
    * The `galaxy` entry points to a valid requirements file for the `ansible-galaxy collection install -r `... command.
    * The `python` entry points to a valid requirements file for the `pip install -r` ... command.
    * The `system` entry points to a bindep requirements file.
    * Additional commands may be specified in the `additional_build_steps` section, either for before the main build steps (prepend) or after (append).

3. Create a file `my_env/execution-environment.yml`

    ---
    version: 1
    
    build_arg_defaults:
        EE_BASE_IMAGE: 'quay.io/ansible/ansible-runner:stable-2.10-devel'
    
    dependencies:
        galaxy: requirements.yml
        python: requirements.txt

4. The contents of `my_env/requirements.yml`

    ---
    collections:
    - name: awx.awx `my_env/requirements.txt`

5. The contents 

    jmespath==0.9.4
    netaddr==0.7.19
    pyvcloud==21.0.1

5. Build it:

    ansible-builder build --tag=my-custom-ee

> The base image is 301.8 MB and has 45 Medium at the time of writing  - `stable-2.9-devel`

6. Tag and push to your registry

7. Create the execution environment on awx

### Sources

* [AWX 18.0.0 with Containerised Execution Environments](https://www.linkedin.com/pulse/awx-1800-containerised-execution-environments-phil-griffiths)
* [AWX Manage issue](https://github.com/ansible/awx/issues/1889)
* [Ansible-builder docs](https://ansible-builder.readthedocs.io/en/latest/definition.html#execution-environment-definition)