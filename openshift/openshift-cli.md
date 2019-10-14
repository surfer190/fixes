# Openshift Command Line Tools

You can download the latest version of the cli tools at: https://github.com/openshift/origin/releases

Openshift command line tools info can be found on your instance at https://{openshift-url}:8443/console/command-line

Then copy the `oc` binary to your path:

    cp oc /usr/local/bin

Login with:

    oc login https://openshift.example.co.za:8443 --token=xxYY

Create a new project:

    oc new-project <project-name>


-e MARIADB_USER=my_user

    oc new-app --name=mariadb ALLOW_EMPTY_PASSWORD=yes MARIADB_USER=bn_ghost --docker-image=bitnami/mariadb
    oc new-app --name=ghost ALLOW_EMPTY_PASSWORD=yes --docker-image=bitnami/ghost 

    oc expose svc/ghost
