## Helm Overview

Deploying applications on k8s can be complex.
Setting up a single application involves creating multiple interdependent k8s resources: deployments, pods, services and replicasets. Each requires you to write detailed `yaml`.

**Helm** is a package manager for k8s. Making it easier to package, configure and deploy applications on k8s.

> Most every programming language and operating system has its own package manager to help with the installation and maintenance of software - Helm has similar features.

Helm can:

\* Install software
* install dependencies
* Upgrade software
* Configure software deployments
* Fetch software packages from repos

It has the following components: 
* CLI tool
* Tiller (not a thing since 3.0.0) a server component listening for changes from helm
* Charts - the helm packaging format
* An [official chart repository](https://github.com/helm/charts)

### Charts

Helm packages are called charts.

The basic structure of a chart:

    package-name/
        charts/
        templates/
        Chart.yaml
        LICENSE
        README.md
        requirements.yaml
        values.yaml

* `charts/` - Manually managed chart dependencies (it is better to use `requirements.txt`)
* `templates/` - template files that are combined with `values.yaml` and rendered into k8s manifests - templates use the go programming language template format.
* `Chart.yaml` - Metadata about the chart - version, maintainer info
* `LICENSE` - plaintext licence
* `requirements.yaml` - dependencies
* `values.yaml` - configuration for the templates for the chart

`helm` can install from a local directory or a `.tar.gz`

### Chart Repositories

> A Helm chart repo is a simple HTTP site that serves an index.yaml file and .tar.gz packaged charts

The default `stable` chart repo is `https://kubernetes-charts.storage.googleapis.com`

More repos can be added with `helm repo add`

### Chart Configuration

A chart usually comes with a default config in `values.yaml` - some applications can be fully deployable with default values.

Eg.

    service:
      type: ClusterIP
      port: 3306

To dump the config for a chart:

    helm inspect values chart-name

The values can be overridden with your own and then installed with:

    helm install

> A Helm chart deployed with a particular configuration is called a _release_

### Releases

Helm combines the defaults with the user provided vars.
These are rendered into k8s manifests and deployed vie the k8s api.

Important cause you may want to deploy the same application more than once.

### Creating Charts

Use:

    helm create chart-name

Fill out `Chart.yaml` and then put your manifests into the `templates` directory.
Extract the relevant info out of the manifest and into your `values.yaml` file - then include them with the [templating system](https://golang.org/pkg/text/template/).

### Using Helm

Install the kubernetes dashboard from the stable repo

    helm install stable/kubernetes-dashboard --name dashboard-demo

Oops it complained:

    Error: could not find tiller

Cause I was still on v2:

    $ helm version
    Client: &version.Version{SemVer:"v2.16.0", GitCommit:"e13bc94621d4ef666270cfbe734aaabf342a49bb", GitTreeState:"clean"}

So ensure to:

    brew upgrade helm

List repos:

    $ helm repo list
    Error: no repositories to show

Add a repo:

    helm repo add stable https://kubernetes-charts.storage.googleapis.com/

Search:

    helm search repo stable

The new way to install a helm chart:

    helm install dashboard-demo stable/kubernetes-dashboard

Get a list of releases on the cluster:

    helm list

It will now be on the k8s cluster:

    kubectl get services

Update the release by changing the name:

    helm upgrade dashboard-demo stable/kubernetes-dashboard --set fullnameOverride="dashboard"

That changed it:

    $ kubectl get services
    NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
    dashboard    ClusterIP   10.101.89.209   <none>        443/TCP   16s
    kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   10h

Apparently you can proxy to the dashboard (hardly works for me)

    kubectl proxy
    http://localhost:8001/api/v1/namespaces/default/services/dashboard/proxy/

List the releases:

    $ helm list
    NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                           APP VERSION
    dashboard-demo  default         2               2020-01-07 11:13:12.959096 +0200 SAST   deployed        kubernetes-dashboard-1.10.1     1.10.1    

we are now going to rollback to the previous version

    helm rollback dashboard-demo 1
    Rollback was a success! Happy Helming!

The service name has rolled back

    $ kubectl get services
    NAME                                  TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
    dashboard-demo-kubernetes-dashboard   ClusterIP   10.98.80.137   <none>        443/TCP   2m
    kubernetes                            ClusterIP   10.96.0.1      <none>        443/TCP   10h

Delete a release:

    helm delete dashboard-demo
    release "dashboard-demo" uninstalled

Helm still keeps the revision info, even for deleted releases. (I think this was only version 2)

So it is better to uninstall I think now:

    helm uninstall dashboard-demo

and then list the uninstalled items with:

    helm list --all

### More Info

For more info check the [Helm Docs](https://helm.sh/docs/)

#### Sources

* [Helm Overview Digitalocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-helm-the-package-manager-for-kubernetes)
* [Helm gets rid of Tiller](https://devclass.com/2019/11/14/helm-maintainers-push-tiller-overboard-en-route-to-3-0-0/)
* [How To Install Software on Kubernetes Clusters with the Helm Package Manager](https://www.digitalocean.com/community/tutorials/how-to-install-software-on-kubernetes-clusters-with-the-helm-package-manager)

