# How do you transform a legacy app into one that uses K8s

## Preparing your Application for Migration

These tasks:

* Extract Configuration Data
* Offload Application State
* Implement Health Checks
* Instrument code for Logging and Monitoring
* Build Administration Logic into API

### Extract Configuration Data

Any information that varies across deployments should be removed.

* service endpoints
* database addresses
* credentials
* various parameters and options

So these things should be in a `settings.py` file  or in the environment variables.

Your app becomes more portable and secure - not bound to a code change or environment.

for example:

    from flask import Flask

    DB_HOST = 'mydb.mycloud.com'
    DB_USER = 'sammy'

over:

    import os

    from flask import Flask

    DB_HOST = os.environ.get('APP_DB_HOST')
    DB_USER = os.environ.get('APP_DB_USER')

Before running the app set the environment variables:

    export APP_DB_HOST=mydb.mycloud.com
    export APP_DB_USER=sammy
    flask run

### Offload Application State

Applications must be designed in a stateless fashion.
They don't store persistent client and application data locally - that way if containers restart they are not lost.

Application cache and session should also be available no matter the node that is hit - like redis cache.

It can be achieved with persistent block storage volumes to containers

> To ensure that a Pod can maintain state and access the same persistent volume after a restart, the StatefulSet workload must be used

### Implement Health Checks

The control plain can repair broken applications. It does this by checking health.

* Readiness probe - lets k8s know your application is ready for traffic
* Liveness probe - Lets k8s know when the app is healthy and running

Methods of probing:

* HTTP - kubelet makes an HTTP request
* Container command - runs a command on container - if exit code is 0 it succeeds.
* TCP - If it can establish a TCP connection

For example a flask health check:

    @app.route('/health')
    def return_ok():
        return 'Ok!', 200

then in your pod specification manifest:

    livenessProbe:
        httpGet:
          path: /health
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 2

### Instrument code for Logging and Monitoring

Error Logging and performance metrics are important.

Remember 12 factor app - `Treat logs as event streams` - output to `STDOUT` and `STDERR`

Use prometheus and the prometheus client to get performance logs.
Ensure that your logs settings send out to `STDOUT` and `STDERR`

Use the RED method:

* R - Rate - number of requests received
* E - Errors
* D - Duration - time to respond

Check what to [measure in the Google SRE Site reliability book](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/#xref_monitoring_golden-signals)

The container orchestrator will catch the logs and send it to EFK (Elasticsearch, Fluentd, and Kibana) stack.

### Build Administration Logic into API

With your app in k8s, you no longer have shell access to your app.

> Taking action beyond restarting and redeploying containers may be difficult

For quick operational and maintenance fixes like **flushing queues** or **clearing a cache**, you should implement the appropriate API endpoints so that you can perform these operations without having to restart containers or exec into running containers and execute series of commands

## Deploying on Kubernetes

After containerising and publishing to a registry...

* Write Deployment and Pod Configuration Files
* Configure Pod Storage
* Injecting Configuration Data with Kubernetes
* ConfigMaps and Secrets
* Create Services
* Logging and Monitoring

### Write Deployment and Pod Configuration Files

> Pods typically consist of an application container (like a containerized Flask web app), or an app container and any “sidecar” containers that perform some helper function like monitoring or logging

Containers in a Pod share storage resources, a network namespace, and port space

### Configure Pod Storage

> Kubernetes manages Pod storage using Volumes, Persistent Volumes (PVs) and Persistent Volume Claims (PVCs)

> When a Pod gets restarted or dies, so do its Volumes, although if the Volumes consist of cloud block storage, they will simply be unmounted with data still accessible by future Pods

> To preserve data across Pod restarts and updates, the PersistentVolume (PV) and PersistentVolumeClaim (PVC) objects must be used

> If your application requires one persistent volume per replica, which is the case with many databases, you should not use Deployments but use the StatefulSet controller

### Injecting Configuration Data with Kubernetes

Kubernetes provides `env` and `envFrom` fields.
This example pod spec sets `HOSTNAME` to `my_hostname`

    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
        env:
        - name: HOSTNAME
          value: my_hostname

> This allows you to move configuration out of Dockerfiles and into Pod and Deployment configuration files

The advantage of this is that you can now modify these Kubernetes workload configurations without needing to test, rebuild and push the image to a registry.

You can also version these configurations

### ConfigMaps and Secrets

> ConfigMaps allow you to save configuration data as objects that you then reference in your Pod 

so you can avoid hardcoding configuration data and reuse

Create a configmap with:

    kubectl create configmap hostname --from-literal=HOSTNAME=my_host_name

To reference it from the Pod configuration file, we use the the `valueFrom` and `configMapKeyRef` constructs

    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
        env:
        - name: HOSTNAME
          valueFrom:
            configMapKeyRef:
              name: hostname
              key: HOSTNAME

You can also use the `--from-file` flag

> Secrets provide the same essential functionality as ConfigMaps, but should be used for sensitive data like database credentials as the values are base64-encoded

### Create Services

> a stable IP address that load balances requests across its containers

4 types:

* `ClusterIP` - grants the Service a stable internal IP accessible from anywhere inside of the cluster
* `NodePort` - expose your Service on each Node at a static port, between 30000-32767 by default. When a request hits a Node at its Node IP address and the NodePort for your service, the request will be load balanced and routed to the application containers for your service.
* `LoadBalancer` - Using cloud provider’s load balancing product
* `ExternalName` - map a Kubernetes Service to a DNS record

> To manage routing external requests to multiple services using a single load balancer, you can use an Ingress Controller

### Logging and Monitoring

Parsing through individual container and Pod logs using `kubectl logs` and `docker logs` can get tedious as the number of running applications grows

> To help you debug application or cluster issues, you should implement centralized logging

In a standard setup, each Node runs a logging agent like `Filebeat` or `Fluentd` that picks up container logs created by Kubernetes.
The application should be a DaemonSet - running on all nodes.

Then use prometheus and grafana to view the data.

> For added resiliency, you may wish to run your logging and monitoring infrastructure on a separate Kubernetes cluster, or using external logging and metrics services

### Task queues and Sending Emails


#### Sources

* [Modernizing Applications for Kubernetes](https://www.digitalocean.com/community/tutorials/modernizing-applications-for-kubernetes)