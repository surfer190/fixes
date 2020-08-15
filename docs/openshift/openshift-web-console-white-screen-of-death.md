---
author: ''
category: Openshift
date: '2019-11-04'
summary: ''
title: Openshift Web Console White Screen Of Death
---
## Openshift Troubleshooting: White screen of death

If you are getting the white screen of death usually there is a problem in the `openshift-web-console` project.

Ensure the pods are running:

    oc project openshift-web-console
    oc get pods

If you see something like this you need to investigate further:

    NAME                          READY     STATUS             RESTARTS   AGE
    webconsole-777564d747-q48l5   0/1       CrashLoopBackOff   40         21d

Get the logs for the pod

    oc logs webconsole-777564d747-q48l5

I saw this issue:

    W1029 13:34:48.100641       1 start.go:93] Warning: config.clusterInfo.loggingPublicURL: Invalid value: "": required to view aggregated container logs in the console, web console start will continue.
    Error: AssetConfig.webconsole.config.openshift.io "" is invalid: [config.clusterInfo.metricsPublicURL: Invalid value: "hawkular/metrics": must contain a scheme (e.g. https://), config.clusterInfo.metricsPublicURL: Invalid value: "hawkular/metrics": must contain a host]
    
That is an issue with the `configmap` of the project, so to edit it, do:

    oc edit configmap/webconsole-config -n openshift-web-console

and add the `metricsPublicURL`.

To redeploy you need to scale up and then down again:

    oc scale --replicas=0 deployment.apps/webconsole
    oc scale --replicas=1 deployment.apps/webconsole
    
    watch oc get pods -n openshift-web-console


## Sources

* [Openshift Customizing the Web Console](https://docs.openshift.com/container-platform/3.9/install_config/web_console_customization.html)
* [How to restart pod in OpenShift?](https://stackoverflow.com/questions/49562433/how-to-restart-pod-in-openshift)