## Set/Switch the Default namespace when using kubectl

First get all the namespaces available:

    > kubectl get ns
    NAME              STATUS   AGE
    cattle-system     Active   53d
    default           Active   53d
    development       Active   52d
    heptio-sonobuoy   Active   33d
    ingress-nginx     Active   53d
    kube-node-lease   Active   53d
    kube-public       Active   53d
    kube-system       Active   53d
    wordpress         Active   33d

To set the default namespace when using kubectl:

    kubectl config set-context --current --namespace=ingress-nginx


### Sources

* [Switch namespace in k8s](https://stackoverflow.com/questions/55373686/how-to-switch-namespace-in-kubernetes)
