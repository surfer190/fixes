---
author: ''
category: Openshift
date: '2019-11-18'
summary: ''
title: Internal Registry
---
Get the Internal registry url:

    oc registry info

or apparently you can do:

    oc get svc -n default | grep registry
    docker tag localimage 172.30.43.173:5000/test/localimage
    docker login -p WTmRhkFBQS9WD1PzzUDpp_JPygROAOMZa8R67j586P8 -e unused -u unused 172.30.43.173:5000
    docker push 172.30.43.173:5000/test/localimage
    c new-app test/localimage --name=myapp

could also login with:

    docker login -u `oc whoami` -p `oc whoami --show-token` 172.30.43.173:5000

## Sources

https://github.com/debianmaster/Notes/wiki/How-to-push-docker-images-to-openshift-internal-registry-and-create-application-from-it.