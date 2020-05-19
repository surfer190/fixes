

    kubectl create -f namespace-dev.json

    kubectl create namespace <namespace>

Create a project

Create a deployment, then create pods then finally create a service so they can be accessible

Get existing deployments from `development` namespace

    kubectl get deploy -n development

