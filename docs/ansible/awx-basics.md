---
author: ''
category: Ansible
date: '2020-06-14'
summary: ''
title: Awx Basics
---
# Ansible AWX Fundamentals

Ansible AWX is basically the open source version of Ansible tower.

It is a web console and REST API for operating ansible across your team, organisation and enterprise.

Some features:

* Role basec access control (RBAC) and auditing
* Sync inventories with the cloud
* Powerful multi playbook workflows
* Logs all jobs
* Browsable Rest API
* Real-time Playbook Output and Exploration
* “Push Button” Automation
* Run-time Job Customization
* Secrets management systems

## TL;DR

Basic Flow

1. Create a credentials for git (SCM)
2. Create a project linked to a repo on git
3. Create an inventory


## Annoying things

* You can't put vault encrypted variables into an inventory on AWX - it must be JSON or YAML

## User Guide

View the activity stream in the top right -> you can expand the actvity stream object and see more info.

* Dashboard

`My View` is a certain users or teams to do specific tasks - `Pressing the launch button beside a job in My View launches it, potentially asking some survey questions if the job is configured to do so`

### Organiszations

A logical collection of `Users`, `Teams`, `Projects` and `Inventories`

* Create a new organization with the `+` button

Adding a user to an organisation adds them as a member only, the `permissions` tab actually gives them permissions.
You can then set permissions and add notifications to the organisation

Remember system administrators have access to all organisations

### Users

Types of Users:

* Normal User - read and write access to limited resources - inventory, projects, job templates that they have permission for
* System Auditor - Read only capability for all objects
* System Administrator - Super user, has full read and write privileges over entire tower install.

> One superuser must always exist

> You can see when a user last logged in on their edit page

When you edit your own user you have the `Tokens` section which are associated with an application.
Applications allow `ServiceNow` or `jenkins` to integrate with ansible tower.

You can change a users type, organisations, teams and permissions a user belongs to on the user edit screen.

### Teams

A Team is a subdivision of an organization with associated projects, crednetials and permissions.
They allow for role based access control within an orgnanization.

> Create a team, then set users and permissions for the team

### Credentials

Credentials are used by tower to authenticate against machines, synchronize ith inventory sources and import project content from git - fuck scm. SCM is GIT.

> tower encrypts passwords and key info and never makes it available via the API

#### How Credentials Work

Ansible tower uses SSH to connect to remote hosts. To pass the key from Tower to SSH - the key must be decrypted before it can be written a named pipe. TOwer then uses that pipe to send the key to SSH (it is never written to disk)

If passwords are used, asnsible handles those by responding directly to the password prompt.

> Credentials added to a Team are made available to all members of the Team, whereas credentials added to a User are only available to that specific User by default.

#### Creating a Credential

Set the name and type

Credential Type:

* Amazon Web Services - IAM STS (Security Token Services) - temporary limited privileges
* Ansible Tower - Access another tower instance
* GitHub Personal Access Token
* GitLab Personal Access Token
* Google Compute Engine
* Red Hat Insights
* Machine - like ansible on the command line - SSH username, SSH key and password or even have tower prompt for the password at run time. Network connections `httpapi`, `netconf` and `network_cli` use the Machine credential type. Machine/SSH credentials do not use environment variables.
* Microsoft Azure Resource Manager
* Network - Use only if you are using a `local` connection with a `provider` to connect to network devices.
* OpenShift or Kubernetes API Bearer Token
* OpenStack - synchronize cloud inventory with openstack
* Red Hat CloudForms
* Red Hat Satellite 6
* Red Hat Virtualization (Ovirt Virtualization) - allow tower to access `oVirt4.py` dynamic inventory plugin.
* Source Control - Clone or update local course code repos from git
* Vault - Synchronization with an inventory with ansible vault - it requires the `vault` password which can be prompt on launch
* VMware vCenter - requires `guest_tools` to be running to get the ip

**Vault** is not hashicorp vault for the credentials - if you are looking for hasicorp vault - then check the next section `Secret Management System`

Machine credentials `password` can be set to **Prompt on Launch**

> Credentials which are used in Scheduled Jobs must not be configured as “Prompt on launch”.

You can create a [custom credential types](https://docs.ansible.com/ansible-tower/latest/html/userguide/credential_types.html#custom-credential-types)

### Secret Management System

You can use your own secrets management system and let ansible tower  use it.

Supported secrete management systems:

* CyberArk Application Identity Manager
* CyberArk Conjur
* HashiCorp Vault Key-Value Store (KV)
* HashiCorp Vault SSH Secrets Engine
* Microsoft Azure Key Management System (KMS)

Creentials will be fetched before running the playbook that needs them

More info in the [ansible tower docs on secret management systems](https://docs.ansible.com/ansible-tower/latest/html/userguide/credential_plugins.html)

### Applications

Allow external integration into ansible tower like `jenkins` and `ServiceNow`

Authorization Code grant type is the preferred way

you have to setup all the details for the oauth flow

### Project

Logical collection of ansible playbooks

You can either place them manually under the Project Base Path on your Tower server or place your playbooks into a source code management (SCM) system supported by Tower

By default the project base path is `/var/lib/awx/projects`

For each project you can:

* Get the latest SCM revision
* Copy project attributes
* Delete the project

Status :

* `Pending` - source control update has been created but not queued or started
* `Waiting` - source code update is queued
* `Running` - source code update is in progress
* `Successful` - last update succeeded
* `Failed` - Last source control update failed
* `Cancelled`
* `OK` - not configured with source code
* `Mssing` - Projects are absent from the path `/var/lib/awx/projects`

To Add a new project set:

* Name
* Description
* Orgnization
* Ansible Environment - The virtualenv to run your playbook from - this will only show up if you have [set a virtual environment up](https://docs.ansible.com/ansible-tower/3.6.3/html/upgrade-migration-guide/virtualenv.html#upgrade-venv)
* SCM Type

The [AWX docs for setting up a virtual environment](https://github.com/ansible/awx/blob/devel/docs/custom_virtualenvs.md)

#### Manually deploying playbooks

Ensure that the playbook directory and files are owned by the same UNIX user and group that the Tower service runs as

#### Manging Projects with Source Control

Ansible Tower has a system-wide setting that allows roles to be dynamically downloaded from a `requirements.yml` file for SCM projects. You may turn this off by setting `Enable Role Download` to Off.

You can set permissions on the proejct level

Roles:

* `Admin` -  allows read, run, and edit privileges (applies to all resources)
* `Use` -  allows use of a resource in a job template (applies all resources except job templates)
* `Update` -  allows updating of project via the SCM Update (applies to projects and inventories)
* `Ad Hoc` - allows use of Ad Hoc commands (applies to inventories)
* `Execute` - allows launching of a job template (applies to job templates)
* `Read` - allows view-only access (applies to all resources)

Set the **Notifications** for the project.

The `Job Templates` tab lets you view and manage any associated job templates.

You can also set schedules for the project.

If settings are ever edited you will need to restart `awx` with `ansible-tower-service restart`

### Inventories

Collection of hosts that a job can run against.

The cloud means inventory sync - to external services

#### Smart Inventories

A collection of hosts defined by a stored search. 

`kind` is set to `smart` and `host_filter` is set

To update smart inventories more often you can set `AWX_REBUILD_SMART_MEMBERSHIP` to `True`, which will update membership when:

* a new host is added
* an existing host is modified (updated or deleted)
* a new Smart Inventory is added
* an existing Smart Inventory is modified (updated or deleted)

#### Inventory Plugins

* Google Compute Engine
* Microsoft Azure Resource Manager
* OpenStack
* Ansible Tower

#### Adding an Inventory

Enter:

* Name
* Description
* Organization
* smart Host Filter
* Variables

Set permissions

Add Groups or Hosts

Wow [hosts must be in `yaml` or `json` ](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)

Adding a host is just the `hostname` and the variables. The hostname can be the ip or dns hostname.

You can also source an inventory from the SCM project you are using:

1. Create the inventory
2. Select `Sources` -> `Add`
3. Set the name and description and set the name Source to `Sourced from Project`
4. Set the `Project` and type the path of the `Inventory file`
5. Optionally set environment variables

You can also source from `vmware vcenter`, `red hat virtualisation` or other places

#### Running Ad Hoc Commands on an inventory

1. Open the Inventory
2. Go to `Hosts`
3. Check the hosts you want to run ad hoc commands against
4. Select `Run Command`

Very Important, for a local connection (to not go over ssh) ensure that in the `host variables` you set:

    ansible_connection: local

### Job Templates

A definition and set of parameters for running an Ansible job - they are useful for running the same job many times

> Job templates can be used to build a workflow template

Add a job template:

* Name, description
* Job type: run - execute, check - dry run
* Inventory
* Project
* Branch
* Playbook - Playbook to be launched (automatically populated)
* Credentials
* Fork - number of simulataneous processes for playbook execution
* Limit - constrain number of hosts affected by the playbook
* Verbosity - control the level of output
* [Tags](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html)
* Labels - group and filter in ansible tower
* Options
    * Enable privilege escalation - run as administrator
    * Enable provisioning callacks - 
    * Enable Webhook
    * Enable concurrent jobs
    * Enable fact cache
* Extra variables

Add permissions

Setup notifications

View completed jobs of the template

Schedule a job

#### Surveys

Surveys set extra variables for the playbook similar to ‘Prompt for Extra Variables’ - but in a user friendly way.
They also allow for validation of user input

Add a survey

> A survey can consist of any number of questions

* Name, description
* Answer Variable Name - variabel name to store the user response in (cannot contain spaces)
* Answer Type
    * Text - single line of text - can set max and min chars
    * Textarea - multi-line text field
    * Password
    * Multiple choice answers (single select)
    * multiple choice (mutiple select)
    * integer
    * float
* Default answer
* Required

You can reorder the questions in the survey

##### Launching

You can just push a button to launch the job

You may be prompted for:

* Credentials
* A survey
* Extra Variables

##### Variables automatically added by Ansible Tower /AWX

* `tower_job_id`: The Job ID for this job run
* `tower_job_launch_type`: The description to indicate how the job was started:
    * `manual`: Job was started manually by a user.
    * `relaunch`: Job was started via relaunch.
    * `callback`: Job was started via host callback.
    * `scheduled`: Job was started from a schedule.
    * `dependency`: Job was started as a dependency of another job.
    * `workflow`: Job was started from a workflow job.
    * `sync`: Job was started from a project sync.
    * `scm`: Job was created as an Inventory SCM sync.
* `tower_job_template_id`: The Job Template ID that this job run uses
* `tower_job_template_name`: The Job Template name that this job uses
* `tower_project_revision`: The revision identifier for the source tree that this particular job uses (it is also the same as the job’s field scm_revision)
* `tower_user_email`: The user email of the Tower user that started this job. This is not available for callback or scheduled jobs.
* `tower_user_first_name`: The user’s first name of the Tower user that started this job. This is not available for callback or scheduled jobs.
* `tower_user_id`: The user ID of the Tower user that started this job. This is not available for callback or scheduled jobs.
* `tower_user_last_name`: The user’s last name of the Tower user that started this job. This is not available for callback or scheduled jobs.
* `tower_user_name`: The user name of the Tower user that started this job. This is not available for callback or scheduled jobs.
* `tower_schedule_id`: If applicable, the ID of the schedule that launched this job
* `tower_schedule_name`: If applicable, the name of the schedule that launched this job
* `tower_workflow_job_id`: If applicable, the ID of the workflow job that launched this job
* `tower_workflow_job_name`: If applicable, the name of the workflow job that launched this job. Note this is also the same as the workflow job template.
* `tower_inventory_id`: If applicable, the ID of the inventory this job uses
* `tower_inventory_name`: If applicable, the name of the inventory this job uses

> They are also given an `awx` prefix

#### Copy a Job Template

A job template can be copied

#### Fact Caching

Store and retrieve facts on a per-host basis

Benefits of fact caching
* Gathering facts for 1000 hosts and forks can take a long time (10 minutes)

Note that you need to run `meta: clear_facts` task to clear facts

#### Utilisating Cloud Credentials

* Openstack
* Amazon web services
* Rackspace
* Google
* Azure
* VMWare

### Provisioning Callbacks

> Provisioning callbacks are a feature of Tower that allow a host to initiate a playbook run against itself, rather than waiting for a user to launch a job to manage the host from the tower console

What?...

More info on [provisioning callbacks](https://docs.ansible.com/ansible-tower/latest/html/userguide/job_templates.html#provisioning-callbacks)

### Extra Variables

`extra_vars` passed to the job launch API are only honored if one of the following is true:

* They correspond to variables in an enabled survey
* `ask_variables_on_launch` is set to True

> When you pass survey variables, they are passed as extra variables

This can be tricky, as passing extra variables to a job template can override other variables being passed from the inventory and project.

Example of extra vars in `yaml`:

    launch_to_orbit: true
    satellites:
    - sputnik
    - explorer
    - satcom

Example of extra vars in `json`:

    {
    "launch_to_orbit": true,
    "satellites": ["sputnik", "explorer", "satcom"]
    }

#### Relaunching Job Templates

The relaunch behavior deviates from the launch behavior in that it does not inherit `extra_vars`

## Job Slicing

A sliced job is a distributed job - used for running a job across a very large number of hosts - to run a playbook on a subset of hosts.

A job template field `job_slice_count` specified the number of jobs to slice into. If the number is greater than 1 tower generates a worfkflow from the job template.

* A sliced job creates a workflow job, and then that creates jobs.
* A job slice consists of a job template, an inventory, and a slice count

> Any job that intends to orchestrate across hosts (rather than just applying changes to individual hosts) should not be configured as a slice job

When jobs are sliced they can run on any tower node - some may run at the same time.

By default, jobs can run simulataneously: `allow_simultaneous`

## Workflows

Workflows allow you to configure a sequence of disparate job templates that may or may not share inventory, playbooks, or permissions.

Linked together in a graph like structure

### Scenarios

* Root node is set to always and is not editable
* A node can have multiple parents - linked to `success`, `failure` or `always`
* Removing a node removes later nodes that are connected
* Prompts for credentails or surveys apply to workflow nodes

> If you use the set_stats module in your playbook, you can produce results that can be consumed downstream by anot

### Workflow States

* Waiting
* Running
* Success (Finished)
* Cancel
* Error
* Failed

### Access and Roles

* To edit and delete a workflow job template, you must have the admin role
* To create a workflow job template, you must be an organization admin or a system admin

## Workflow Job Templates

Links together many resources

* Job templates
* Workflow templates
* Project syncs
* Inventory source syncs

### Create a workflow template

1. Click "New Workflow Template"
2. Enter details:
    * Name, description
    * Organisation
    * Inventory
    * Limit
    * Labels
    * etc.
3. Save - the workflow visualiser will pop up

Add permissions, notifications, view completed jobs and add a survey

Use the [worflow visualiser](https://docs.ansible.com/ansible-tower/latest/html/userguide/workflow_templates.html#workflow-visualizer) to setup the workflow

## Instance Groups

Give the avility to group instances in a clustered environment.
Policies dictate how groups behave and how jobs are executed.

[More info on the docs on Instance Groups](https://docs.ansible.com/ansible-tower/latest/html/userguide/instance_groups.html)

## Jobs

A job is an instance of Tower launching an Ansible playbook against an inventory of hosts.

You can view the status and output of jobs

### Job statuses

* `Pending` - The playbook run has been created, but not queued or started yet. Any job, not just playbook runs, will stay in pending until it’s actually ready to be run by the system. Reasons for playbook runs not being ready include dependencies that are currently running (all dependencies must be completed before the next step can execute), or there is not enough capacity to run in the locations it is configured to.
* `Waiting` - The playbook run is in the queue waiting to be executed.
* `Running` - The playbook run is currently in progress.
* `Successful` - The last playbook run succeeded.
* `Failed` - The last playbook run failed.

[More detailed info on jobs in the docs](https://docs.ansible.com/ansible-tower/latest/html/userguide/jobs.html)

### WebHooks

More info in the [docs on Webhooks](https://docs.ansible.com/ansible-tower/latest/html/userguide/webhooks.html)

You can [setup webhooks on gitlab to do deploys](https://docs.ansible.com/ansible-tower/latest/html/userguide/webhooks.html#gitlab-webhook-setup)

## Notifications

Lots of info on [notifications in the docs](https://docs.ansible.com/ansible-tower/latest/html/userguide/notifications.html)

## Schedules

[Schedules on AWX](https://docs.ansible.com/ansible-tower/latest/html/userguide/scheduling.html)

## Security in AWX

It is important to take note of certain [security implications with AWX](https://docs.ansible.com/ansible-tower/latest/html/userguide/security.html)

* All playbooks are executed by `awx` file system user
* Ansible Tower defaults to offering job isolation via Linux namespacing and chroots
* jobs can only access playbooks and roles from the Project directory for that job template and common locations such as `/opt`

* Tower’s multi-tenant security prevents playbooks from reading files outside of their project directory
* In awx `3.1` and later: bubblewrap is used to isolate jobs - by default job isolation is enabled

Process Isolation is used for the following job types:

* Job Templates
* Ad-hoc Commands

By default process isolation hides:

* `/etc/tower` - to prevent exposing Tower configuration
* `/var/lib/awx` - with the exception of the current project being used (for regular job templates)
* `/var/log`
* `/tmp` (or whatever the system temp directory is) - with the exception of the processes’ own temp files.

Alot of info about [RBAC role based access controls in the documentation](https://docs.ansible.com/ansible-tower/latest/html/userguide/security.html#role-based-access-controls)







## AWX Ansible Best Practices

AWX is a web-based user interface, REST API, and task engine for ansible.
It is an upstream project for tower, a commercial derivative of AWX.

## Documented Best Practices

[AWX documented best practices](https://docs.ansible.com/ansible-tower/latest/html/userguide/best_practices.html)

* Use Source Control
* Use [Ansible file and directory structure](http://docs.ansible.com/playbooks_best_practices.html)
* Use Dynamic Inventory Sources
* Variable Management for Inventory
* Autoscaling
* Larger Host Counts
* Continuous integration


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

Dependencies can be installed with `local_action` or `deletegate_to`

## Source

* [Ansible Tower Install and Reference Guide](https://docs.ansible.com/ansible-tower/latest/html/installandreference/index.html)
* [Ansible Tower User Guide](https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html)
* [Ansible Tower Admin Guide](https://docs.ansible.com/ansible-tower/latest/html/administration/index.html)
* [Ansible Tower API Guide](https://docs.ansible.com/ansible-tower/latest/html/towerapi/index.html)
* [AWX Command Line Interface](https://docs.ansible.com/ansible-tower/latest/html/towercli/index.html)