# Set Up Monitoring on your k8s cluster with the Helm and Prometheus Operator

A monitoring system usually consists of:

* a time-series database holding metrics
* a visualization layer
* an alerting layer

One popular monitoring solutions is:

* Prometheus - A time series database and monitoring tool that works by polling metrics endpoints and processing the data from them
* Grafana - A data analytics and visualisation tool to build dashboards for your metrics
* AlertManager - Usually deployed alongside Prometheus - deduplicating, grouping, and routing alerts

On the kubernetes side - these expose cluster and machine level metrics:

* [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
* [node_exporter](https://github.com/prometheus/node_exporter)

Deploying all of this can be tricky but we can make use of Helm (package manager) with the [Prometheus Operator](https://github.com/coreos/prometheus-operator) and [kube-prometheus](https://github.com/coreos/kube-prometheus).

The prometheus-operator chart is used.

...This is a bit too advanced to dig into for now...too much complexity

https://www.digitalocean.com/community/tutorials/how-to-set-up-digitalocean-kubernetes-cluster-monitoring-with-helm-and-prometheus-operator





### Sources

* [How to Set Up DigitalOcean Kubernetes Cluster Monitoring with Helm and Prometheus Operator](https://www.digitalocean.com/community/tutorials/how-to-set-up-digitalocean-kubernetes-cluster-monitoring-with-helm-and-prometheus-operator)