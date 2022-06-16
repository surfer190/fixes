---
author: ''
category: Gitlab-Ci
date: '2020-06-14'
summary: ''
title: Setup a Gitlab Runner on Openshift
---

# Setup a Gitlab Runner on Openshift

> Use this article at your own risk - openshift was difficult to work with. Perhaps looks at other projects that are downstream from kubernetes.

When you install openshift - you get an already running default docker registry.
You also get a default route...you get alot of things.

Unfortunately the dev experience can still be quite bad without your continuous integration hooked up.

So I'm going to attempt to explain how to link up your corporate gitlab environment to Openshift for easy building, testing and deploying.

There was a semi-decent video on [Deploying from gitlab to Openshift OKD](https://www.youtube.com/watch?v=EwbhA53Jpp4) however he missed the most important part...creating the template on OKD.

## Current Status

So what is the current status of your infrastructure:

* A gitlab enterprise edition 
* An Openshift OKD cluster

Usually if you have added a `.gitlab-ci.yml` to your project and there are no gitlab runners configured it will be in a paused state for an hour with a message like:

    There are no runners configured for your project

## Steps

The first thing you need to do is[install and register a gitlab runner](https://docs.gitlab.com/runner/install/)

Importantly if you are using the linux repo, you need to [install docker engine](https://docs.docker.com/install/) on the gitlab host before installing the gitlab runner.

Use the steps [here](https://docs.gitlab.com/runner/install/linux-repository.html#installing-the-runner):

    curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
    sudo apt-get install gitlab-runner
    apt-cache madison gitlab-runner
    sudo apt-get install gitlab-runner=10.0.0

You then need to [register the runner](https://docs.gitlab.com/runner/register/index.html):

To do this you need 2 things:
1. You need a seperate place other than gitlab to install the runner
2. You need to have obtained a token

#### Obtaining the Shared Runner Token

Grab the shared-Runner token on the `admin/runners` page

Then you need to create a new project on openshift using [openshift-examples](https://github.com/debianmaster/openshift-examples/tree/master/gitlab-ci-with-openshift)

    oc new-project gitlab
    # Allow the project to run as root
    oc adm policy add-scc-to-user anyuid -z gitlab-ce-user -n gitlab
    oc adm policy add-scc-to-user privileged -z gitlab-runner-user -n gitlab
    oc apply -f https://raw.githubusercontent.com/debianmaster/openshift-examples/master/gitlab-ci-with-openshift/gitlab-runner.yaml

Then go to the frontend and deploy the image

> This worked...until I commited to my project and the runner failed becasue the pod containing 3 containers to run the tests did not work.

    Running with gitlab-runner 12.3.0 (a8a019e0)
    on k8s_runner hR-xVAaf
    Using Kubernetes namespace: gitlab
    Using Kubernetes executor with image docker ...
    Waiting for pod gitlab/runner-hr-xvaaf-project-88-concurrent-08rlqg to be running, status is Pending
    ...
    Waiting for pod gitlab/runner-hr-xvaaf-project-88-concurrent-08rlqg to be running, status is Pending
    ERROR: Job failed (system failure): timed out waiting for pod to start







### Sources

* [OpenShift Origin template for GitLab Runner](https://github.com/oprudkyi/openshift-templates/tree/master/gitlab-runner)
* [Openshift examples: gitlab-ci-with-openshift](https://github.com/debianmaster/openshift-examples/tree/master/gitlab-ci-with-openshift)
* [deploy an Application on OpenShift with Gitlab CI](https://k33g.gitlab.io/articles/2019-07-26-OPENSHIFT.html)
