---
author: ''
category: Openshift
date: '2019-11-04'
summary: ''
title: Autoscaling In Openshift
---

So you have scaled pods up manually using the web interface or:

    oc scale --replicas=3 dc/<my-project>

but now you want to ensure that this autoscales for when you aren't around and will increase and decrease based on load

### HorizontalPodAutoscaler

A `HorizontalPodAutoscaler` object needs to be added to your project

> The horizontal pod autoscaler computes the ratio of the current metric utilization with the desired metric utilization, and scales up or down accordingly

You should ensure your pods has gone through [readiness checks](https://docs.openshift.com/container-platform/3.9/dev_guide/application_health.html#dev-guide-application-health) to ensure it is ready for scaling

You should know the max and min pods to run beforehand:

    oc autoscale dc/<project> --min 1 --max 10 --cpu-percent=80

Get the horizontal pod autoscalers

    oc get hpa

It should show you min, max, target and current

    $ oc get hpa
    NAME      REFERENCE               TARGETS         MINPODS   MAXPODS   REPLICAS   AGE
    blog      DeploymentConfig/blog   <unknown>/80%   1         10        3          1m

More detailed info:

    oc describe hpa/blog

If you get errors like:

    ScalingActive  False   FailedGetResourceMetric  the HPA was unable to compute the replica count: unable to get metrics for resource cpu: unable to fetch metrics from resource metrics API: the server could not find the requested resource (get pods.metrics.k8s.io)
    ...failed to get cpu utilization: unable to get metrics for resource cpu

then you should request that your [Openshift cluster admin enable cluster metrics](https://docs.openshift.com/container-platform/3.9/install_config/cluster_metrics.html#install-config-cluster-metrics)

Once you have set that up by modifying the [metrics cluster install configuration](https://docs.openshift.com/container-platform/3.11/install_config/cluster_metrics.html)

    oc adm diagnostics MetricsApiProxy --loglevel 10

### Debugging no access to the metrics API

To check the deployed services use:

    kubectl get apiservices

We are looking for `metrics.k8s.io` in the output, if it is not there then it might not be [registered](https://github.com/kubernetes/kubernetes/issues/44540)

Get the metrics related pods with:

    kubectl get pods -n kube-system

To check resource consumption you should be able to:

    kubectl top

but in my case it would just give help info and this message

    This command requires Heapster to be correctly configured and working on the server.

### Using the docs

You can verify the metrics were installed correctly with:

    oc adm top node
    oc adm top pod

You can also get all the apis with

    oc get --raw /apis/

which I think is the same as

    kubectl get apiservices

I decided to redeploy the metrics API with ansible and didn't set a specific hostname

    oc adm diagnostics MetricsApiProxy

I still get this error:

    ERROR: [DClu4003 from diagnostic MetricsApiProxy@openshift/origin/pkg/oc/cli/admin/diagnostics/diagnostics/cluster/metrics.go:89]
        Unable to access the metrics API Proxy endpoint /api/v1/proxy/namespaces/openshift-infra/services/https:heapster:/api/v1/model/metrics:
        (*errors.StatusError) the server could not find the requested resource
        The Horizontal Pod Autoscaler is not able to retrieve metrics to drive scaling.

You can check that you can get the metrics for a pod with:

    oc adm top pod --heapster-namespace='openshift-infra' --heapster-scheme='https' -n demo

you don't need those flags though:

    oc adm top pod -n demo

> Configure a 80 milicore limit for CPU requests

    oc patch dc/guestbook -p '{"spec":{"template":{"spec":{"containers":[{"name":"guestbook","resources":{"limits":{"cpu":"80m"}}}]}}}}'
    oc autoscale dc/guestbook --min 1 --max 3 --cpu-percent=20

Get the object like any other openshift object

    oc get hpa guestbook -o yaml -n myproject

In the pod artificial stress is added with:

    seq 3 | xargs -0 -n1 timeout -t 60 md5sum /dev/zero

This [reddit post](https://www.reddit.com/r/kubernetes/comments/ah952t/horizontal_pod_autoscaling_not_working_unable_to/) describes the same issue and answers declare that it is insecure certs

To view the logs on openshift I used:

    kubectl logs hawkular-metrics-ks6sb --namespace=openshift-infra

It seems to still be the [api aggregation issue](https://github.com/kubernetes-incubator/metrics-server/issues/249)...that it was not setup correctly.

    metrics.k8s.io

Can check diagnostics of the entire cluster with:

    oc adm diagnostics

Get metrics pods with:

    oc get pods -n openshift-infra

Checking the pod:

    oc describe pod hawkular-metrics-ks6sb -n openshift-infra

Gave me a bunch of errors:

    Type     Reason     Age   From                              Message
    ----     ------     ----  ----                              -------
    Normal   Scheduled  1h    default-scheduler                 Successfully assigned openshift-infra/hawkular-metrics-ks6sb to openshift.example.co.za
    Normal   Pulled     1h    kubelet, openshift.example.co.za  Container image "docker.io/openshift/origin-metrics-hawkular-metrics:v3.11.0" already present on machine
    Normal   Created    1h    kubelet, openshift.example.co.za  Created container
    Normal   Started    1h    kubelet, openshift.example.co.za  Started container
    Warning  Unhealthy  1h    kubelet, openshift.example.co.za  Liveness probe failed: Failed to access the status endpoint : <urlopen error [Errno 111] Connection refused>.
    Traceback (most recent call last):
    File "/opt/hawkular/scripts/hawkular-metrics-liveness.py", line 48, in <module>
        if int(uptime) < int(timeout):
    ValueError: invalid literal for int() with base 10: ''
    Warning  Unhealthy  1h (x3 over 1h)  kubelet, openshift.example.co.za  Readiness probe failed: Failed to access the status endpoint : <urlopen error [Errno 111] Connection refused>. This may be due to Hawkular Metrics not being ready yet. Will try again.
    Warning  Unhealthy  1h               kubelet, openshift.example.co.za  Readiness probe failed: Failed to access the status endpoint : timed out. This may be due to Hawkular Metrics not being ready yet. Will try again.
    Warning  Unhealthy  1h (x3 over 1h)  kubelet, openshift.example.co.za  Readiness probe failed: The MetricService is not yet in the STARTED state [STARTING]. We need to wait until its in the STARTED state.

So I try to [access heapster directly](https://github.com/openshift/origin-metrics#accessing-heapster-directly) with:

    curl -X GET https://${KUBERNETES_MASTER}/api/v1/proxy/namespaces/openshift-infra/services/https:heapster:/api/v1/model/metrics

And I get back:

    {
        "kind": "Status",
        "apiVersion": "v1",
        "metadata": {
            
        },
        "status": "Failure",
        "message": "services \"https:heapster:\" is forbidden: User \"system:anonymous\" cannot proxy services in the namespace \"openshift-infra\": proxy verb changed to unsafeproxy\nno RBAC policy matched, proxy verb changed to unsafeproxy",
        "reason": "Forbidden",
        "details": {
            "name": "https:heapster:",
            "kind": "services"
        },
        "code": 403
    }

The redhat forums also [highlight this issue](https://access.redhat.com/solutions/3679171) and give the following diagnosis steps:

    oc adm top pod -n hooks
    oc get --raw="/api/v1/proxy/namespaces/openshift-infra/services/https:heapster:/api/v1/model/metrics" 
    oc get --raw="/api/v1/namespaces/openshift-infra/services/https:heapster:/proxy/api/v1/model/metrics" 

The second request works, furthermore the [bugzilla report](https://bugzilla.redhat.com/show_bug.cgi?id=1571176) notes that the incorrect url is used.

So the solution is to upgrade to a later version, use this [guide](https://docs.openshift.com/container-platform/3.11/upgrading/automated_upgrades.html) and ensure to reboot the host:

    ansible-playbook playbooks/byo/openshift-cluster/upgrades/v3_11/upgrade.yml -e openshift_certificate_expiry_warning_days=30

So now it works.

    oc describe hpa

Now gives successful

        Type            Status  Reason            Message
    ----            ------  ------            -------
    AbleToScale     True    ReadyForNewScale  the last scale time was sufficiently old as to warrant a new scale
    ScalingActive   True    ValidMetricFound  the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)
    ScalingLimited  True    TooFewReplicas    the desired replica count is increasing faster than the maximum scale rate

and the hpa now shows the current cpu usage:

    [root@openshift ~]# oc get hpa
    NAME      REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
    blog      DeploymentConfig/blog   0%/50%    1         10        1          2d

You need to set `CPU request` and `CPU Limit`.

### Sources

Remember to get the correct version of the documentation  - the same as the system you are running

* [Pod Autoscaling](https://docs.openshift.com/container-platform/3.9/dev_guide/pod_autoscaling.html)
* [Metrics Install Configuration](https://docs.openshift.com/container-platform/3.11/install_config/cluster_metrics.html)
* [Katacoda Openshift Metrics](https://www.katacoda.com/openshift/courses/introduction/using-metrics)

