## Setting up and Accessing the Openshift Registry

Log in to Openshift.

Find the ip address of the registry:

Apparently you get it with defaults:

    oc get svc -n default | grep registry

If you explicitly enable it you get it without defaults:

    $ oc adm registry
    --> Creating registry registry ...
        serviceaccount "registry" created
        clusterrolebinding.authorization.openshift.io "registry-registry-role" created
        deploymentconfig.apps.openshift.io "docker-registry" created
        service "docker-registry" created
    --> Success

    $ oc get svc
    NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
    docker-registry   ClusterIP   172.30.154.81   <none>        5000/TCP   18m

You can also get it with:

    oc get svc/docker-registry -o yaml | grep clusterIP:
      clusterIP: 172.30.154.81

Openshift works on routes so it had actually set everything up for me, and you can use the frontend for it.

## Pushing an Image to the registry

Ensure you have `https` it is at the correct TLS version 1.2+

Get your token (assuming you have logged into the cli)

    oc whoami -t

Log into the registry using your token

    docker login -u <username> -p <token_value> <registry_ip>:<port>

Tag the container:

> A fully qualified docker image name should conform to the following format: `<registry>/<repo>/<image>:<tag>`

> When mapping to OpenShift: `<registry>/<project>/<imagestream>:<tag>`

    docker commit c16378f943fe my-api
    docker tag my-api registry.example.co.za:5000/my-project/my-api-image

Tag the remote repo in the image

    docker tag my-api registry.example.co.za:5000/my-project/my-api-image

Push the image to openshift

    docker push registry.example.co.za:5000/my-project/my-api-image

> Important to note that `my-project` need not be created already

Key here is if you are using the openshift docker repo - you need to follow the specifications of that repo.
For example the default docker repo does not require the `my-project` part.

    oc new-project <my-project>

It seems like the project needs to exist


* [Pushing an image to Openshift private Repo](https://github.com/debianmaster/Notes/wiki/How-to-push-docker-images-to-openshift-internal-registry-and-create-application-from-it.)
* [Logging into the registry](https://docs.okd.io/latest/minishift/openshift/openshift-docker-registry.html#login-to-registry)
* [Remotely push and pull container images](https://blog.openshift.com/remotely-push-pull-container-images-openshift/)

