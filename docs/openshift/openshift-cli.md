---
author: ''
category: Openshift
date: '2019-11-04'
summary: ''
title: Openshift Cli
---
# Openshift Command Line Tools

You can download the latest version of the cli tools at: https://github.com/openshift/origin/releases

Openshift command line tools info can be found on your instance at https://{openshift-url}:8443/console/command-line

Then copy the `oc` binary to your path:

    cp oc /usr/local/bin

Login with:

    oc login https://openshift.example.co.za:8443 --token=xxYY
    
Get all the nodes in the cluster:

    oc get nodes

Get image streams

    oc get is

> The `DOCKER REPO` is the internal registry

Check status:

    oc status

Ensure the registry and router pods are up and running:

    oc get pods -n default

    NAME                       READY     STATUS    RESTARTS   AGE
    docker-registry-2-7jv6h    1/1       Running   0          6d
    registry-console-2-5shlp   1/1       Running   0          6d
    router-3-rh7f5             1/1       Running   0          6d

In an application get pods and routes:

    oc get pods
    oc get routes
    
## Projects 

Createa a project

    oc new-project myproject --display-name 'My Project'

Get all projects

    oc get project

Change to a specific project

    oc project <project_name>

Get current project

    oc project

Run a single command against another project

    oc get templates --namespace openshift

### Registry

Get registry info

    oc registry info

### Scaling

Scale

    oc scale --replicas=3 dc/<my-project>

### Expose and get route info

Get the route

    oc get svc

Expose the route

    oc expose svc/<name>

Get the route info

    oc get routes/<name>

### Security

SCC - Security Context Constraints

Get a list of Scc's

    oc get scc

Describe the SCC

    oc describe scc anyuid

## Login

Get Login help

    oc login --help

Get current token

    oc whoami -t

Get the server

    oc whoami --show-server

## User Management

To add another edit user to a project:

    oc adm policy add-role-to-user edit <collaborator>

To remove a user from a project:

    oc adm policy remove-role-from-user edit <collaborator>

To view users that have access to a project:

    oc get rolebindings
    
## Templates

Get templates in a project

    oc get templates

Get templates in the global `openshift` context

    oc get templates --namespace openshift

Get images in the global `openshift` context

    oc get imagestreams --namespace openshift

View available templates and images

    oc new-app -L

## Types and Resources

    oc types

Get services

    oc get svc

Get all resources in a project

    oc get all

To get shorter output

    oc get all -o name --selector app=blog

Get a list of all available resources

    oc api-resources

Get an explanation of a resource

    oc explain routes

Get routes in a project

    oc get routes

## Exposing and Routes

Expose a service

    oc expose service/<name>

Check the status of projct

    oc status

## Environment variables

View the environment variables that can be set

    oc set env dc/<name> --list

To set a new env variable at runtime

    oc set env dc/<name> KEY=value
    oc set env dc/blog BLOG_BANNER_COLOR=green

To set env variables at build time

    oc new-app <appname> --name <name> --env KEY=value
    oc new-app openshiftkatacoda/blog-django-py --name blog --env BLOG_BANNER_COLOR=green



## Options

Get options

    oc options

> Most commands will accept `--dry-run`

## SSH Into a POD

Get the pods

    oc get pods

RSH into a pod

    oc rsh <pod-name>

Check the user it is running as:

    id
    uid=1020810000(1020810000) gid=0(root) groups=1020810000

## Create a new project

Create a new project:

    oc new-project <project-name> -e MARIADB_USER=my_user
    oc new-app --name=mariadb ALLOW_EMPTY_PASSWORD=yes MARIADB_USER=bn_ghost --docker-image=bitnami/mariadb
    oc new-app --name=ghost ALLOW_EMPTY_PASSWORD=yes --docker-image=bitnami/ghost 

    oc expose svc/ghost

## Sources

* [Basic CLI Operations](https://docs.okd.io/latest/cli_reference/basic_cli_operations.html#new-project)
* [OC Commandline for Newbies](https://blog.openshift.com/oc-command-newbies/)
