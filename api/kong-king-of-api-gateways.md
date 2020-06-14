# Kong king of API Gateways

## 1: Microservices Architecture

> Any one part can be replaced without breaking the entire system

There are many small subsystems in a process. When adding a new subsystem, you have to ensure other subsystems are not affected and that the entire system stays online

With Microservices, you don't need to test the entire system and you don't need to take it offline.

### Monolith Patterns

#### Three tier architecture

1. Data access layer - entities and relationships, the core layer
2. Business logic layer - business policies, workflows and events
3. Presentation layer - upper layer that the end user interacts with

In microservices, the data access and business logic layer is the service level and the presentation layer at the client level

#### MVC: Model-view-controller

Model represents the data access layer, controller the business processes and the view - the presentation layer.

### Microservices answer

Bounded context - breaking down things systems into smaller contexts

Example: Movie Cinema

* Movie service - Detailed nfo about movies
* Show Time Service - Handles schedules and Price
* Booking Service - Booking and reserving seats
* User service - Information about users - employee, customer, name etc.

Characteristics:

* Small in size
* Various platforms
* Y Axis scaling

### Ideal Environment for Microservices

> Microservices are not an answer to every problem

1. Big Systems
2. Services are goal oriented
3. Replaceability

### Use of an API Gateway

1. Should a web app know all the addresses of our service? Should it make a request for each piece of information needed?

We can wrap data from various services into one response in one request and protect our services addresses from the outside world.
Eg. Instead of calling `http://users.mycinemas.com/details/me` and `http://showtime.mycinemas.com/lists`, you can just call: `http://kongcinemas.com/movies/lists`

2. Is it okay to expose our interface to all frontends?

An API gateway also works as an authentication and authorization layer, it can also log all requests. The API can make differences between requests from different sources - ie. Android App and web

3. Should a client get all the data, when only some data is needed?

An API gateway allows you to transform and limit the data you need. Saving bandwidth and preventing maliscous and fake calls.

### Using single or multiple gateways

* Single API Gateway - 
* Multiple backends (Backends for Frontends) - 

## 2: API Gateway a rapidly changing landscape

### What is an ESB?

ESB (Enterprise Service Bus) - implements a communication system between mutually interacting applications in a SOA (Service Oriented Architecture)

An ESB is a central platform for integrating applications in an enterprise.
It allows communication via a common communication bus of point to point connections between providers and users.

An ESB promotes agility and flexibility

An ESB routes messages between services, monitor and control routing, control versioning, data transformation and security

### What is an API gateway?

A glorified reverse proxy
An API frontend that:

* orchestrates requests
* enforces traffic policies (caching, throttling)
* security (authorization, authentication)
* Analytics on traffic
* Orchestrates transformation engines

> An entrypoint between external requests and internal services

### Is an API a new ESB?

It provides alot of the functionality but it does it in an orchestrated way and not a point to point (or broadcast) way.

> The equivalent of an ESB to animals is the nervous system combined with the circulatory system. When an organ needs to communicate with another specific organ, it uses the nervous system to send a point-to-point message. When an organ needs to broadcast a message to other organs that might be interested, it releases a hormone into the bloodstream to send a multicast message. When a message comes into the brain from anywhere in the body, the brain tells the body how to react. For example, if you accidentally touch a hot stove, the nerves in your skin shoot a message of pain to your brain. The brain then sends a message back telling the muscles in your hand to pull away. The API Gateway is equivalent to the brain in the way that it orchestrates interaction.

    A reverse proxy is a type of proxy server that retrieves resources on behalf of a client from one or more servers. These resources are then returned to the client, appearing as if they originated from the proxy server itself

Evolution:

* Houses - HTTP Servers
* Tribes - Reverse Proxies
* Villages - ESB's
* Towns - API Gateways

API Gateways:

* Kong
* APIGEE
* KrakenD
* Tyk.io
* IBM API Connect (previously Strongloop)

Each one of these offerings has their advantages and disadvantages, from price, maintainability, scalability and customization.

### API Gateway Future

Serverless - Your function (Faas) hosted on someone else's pc

Service Meshes - Containerization has become abused.

> This problem of every app as its own container spawned companies to have several thousand containers running at any given time”

> During a conference a speaker mentioned that in production they had over 4000 containers, but only 400 engineers, meaning that each engineer was responsible for 10 production systems. This would be considered a problem for an API Gateway, since in the current stance most gateways are hand registering each service it communicates with and how to handle the requests to each service (security and traffic policies)

Service mesh is often used to describe the network of microservices that make up such applications and the interactions between them
* [isitio.io](https://istio.io/)
* [envoy](https://www.envoyproxy.io)

There is some overlap between service meshes and API gateways

Service meshes are for external service to service communication

Sidecar Gateways - Component based software engineering (alright take it easy...)

### API First: Weathering the Storm

A strategy that puts the target developer's interests first and then buikd the product on top of it.
It allows the product to enable flexibility in how users utilise the product.
Allowing adding new functionality without disregarding the original intent.

If no discipline is applied to API design and depenedencies and integrations are managed poorly, it becomes a nightmare.

## 3: API Gateway Disruptor

It is a Lua application running in nginx, integrated with OpenResty instead of directly compiling against an Nginx module.
Openresty is a set of libraries to extend nginx.

* It has a pluggable architecture with Lua scripts / plugins
* Database abstraction
* Plugin management
* routing

> Seperation of concerns

It is:

* scalable - scales horizontally
* modular - extended by adding new modules
* any infrastructure - runs anywhere

### API Centric

* tyk.io - only ships with a dashboard
* krakenD - an application to craft configuration
* IBM API Connect and APIGEE - have both but lack simplicity

Kong lets you leverage what you have already.
It decouples some concerns away - eg. service discovery is already coupled with a provider in other API gateways
So many things itnegrate well with kong, like konga (frontend) and plugins.

Service discovery:

* etcd
* isitio
* linkerd
* consul

It is open source: cost, flexibility, freedom, security and accountability

It is _free as in kittens_ not _free as in beer_....it requires maintenance, configuration and ongoing support.

Configurable as it is using nginx, so existing nginx conf can be used

Plugins out the box:

* Basic auth
* Key uthentication
* OAuth2.0 authentication
* HMAC authnetication
* JWT
* LDAP
* ACL
* CORS
* Dynamic SSL
* IP Restriction
* Bot Detection
* Request Size Limiting
* Rate Limiting
* Response Rate Limiting
* Request Termination
* AWS Lambda
* OpenWhisk
* Galileo
* Datadog
* Runscope
* Request transformer
* Response transformer
* Correlation ID
* TCP
* UDP
* HTTP
* File
* StatsD
* Syslog
* Loggly

What Kong EE (Enterprise Edition) has:

* OpenID Connect
* OAuth 2.0 Introspection
* Canary releases - slowly rollout to a subset of users
* Forward Proxy - If kong sits in internal network to forward to outside
* Proxy caching
* Enhanced rate limiting
* Request transformer enhanced
* Developer Portal
* Management portal - Role based access control, for non technical management

> There are many open source solutions to display documentation, but the management portal and cohesion between the gateway and documentation is generally lacking

KongHQ has embedded their developer portal software with the EE of their API Gateway

Allowing features to be developed against the gateway

### Disrupting

Innovation creating a new market and value network that disrupts existing markets and networks.

* Cost - determines whether it is used inhouse or only for external services
* API Configuration - How configurable is the API? file, environment, API. How are configurations enabled?
* Installation - requirements, dependencies and difficulty
* Customizability - How easy does it dolve problems?
* Community - Is there a community or is it hidden behind a py wall or in horrible proprietary docs?

#### Kong

* Cost: Open source or paid enterprise
* Configuration: Simple REST API with almsot immediate results
* Installation: 14 methods of installation - needs cassandra and postgres
* Customizability: Custom nginx, custom plugins are encouraged

Minimal dependencies, many installation options, customizable, free/cheap, 

### Setting up Kong

To setup kong use the [Install page](https://konghq.com/install/)

I chose to use ubuntu and postgres as my db (cassandra is not fun to set up)

1. Create a local kong user for the db (and service)

    sudo adduser kong

2. Create the kong role and database

    sudo su postgres -
    psql
    CREATE USER kong; CREATE DATABASE kong OWNER kong;
    
or

    createuser --interactive --pwprompt
    createdb -O kong kong

3. Install kong

4. Change the configuration

    sudo mv /etc/kong/kong.conf.default /etc/kong/kong.conf

5. Change the config...just `database` and `admin_listen`

6. Run the migrations

    kong migrations bootstrap

7. Start kong

    kong start

8. Check it is working

    sudo apt install httpie
    http :8001

### Adding a service to kong via the API

1. Use `httpie` to add a service:

    http POST :8001/services/ name=mockbin url=http://mockbin.org

Eg.

    ubuntu@db:/etc/kong$ http POST :8001/services/ name=mockbin url=http://mockbin.org
    HTTP/1.1 201 Created
    Access-Control-Allow-Origin: *
    Connection: keep-alive
    Content-Length: 262
    Content-Type: application/json; charset=utf-8
    Date: Tue, 23 Apr 2019 07:11:43 GMT
    Server: kong/1.1.0

    {
        "connect_timeout": 60000, 
        "created_at": 1556003503, 
        "host": "mockbin.org", 
        "id": "8c203e99-1c80-48d9-a414-9277a1762909", 
        "name": "mockbin", 
        "path": null, 
        "port": 80, 
        "protocol": "http", 
        "read_timeout": 60000, 
        "retries": 5, 
        "tags": null, 
        "updated_at": 1556003503, 
        "write_timeout": 60000
    }

2. Add a route to the service

    http POST :8001/services/mockbin/routes hosts:='["example.com"]'

    Eg.

    ubuntu@db:/etc/kong$ http POST :8001/services/mockbin/routes hosts:='["example.com"]'
    HTTP/1.1 201 Created
    Access-Control-Allow-Origin: *
    Connection: keep-alive
    Content-Length: 360
    Content-Type: application/json; charset=utf-8
    Date: Tue, 23 Apr 2019 07:19:14 GMT
    Server: kong/1.1.0

    {
        "created_at": 1556003954, 
        "destinations": null, 
        "hosts": [
            "example.com"
        ], 
        "id": "d039a07a-1d5d-464a-9075-9d9801ec9ef0", 
        "methods": null, 
        "name": null, 
        "paths": null, 
        "preserve_host": false, 
        "protocols": [
            "http", 
            "https"
        ], 
        "regex_priority": 0, 
        "service": {
            "id": "8c203e99-1c80-48d9-a414-9277a1762909"
        }, 
        "snis": null, 
        "sources": null, 
        "strip_path": true, 
        "tags": null, 
        "updated_at": 1556003954
    }

3. Test it is proxying requests

    http GET :8000 Host:example.com

### Create a plugin via the API

1. Add the `key-auth` plugin

    http POST :8001/services/mockbin/plugins/ name=key-auth

2. Test that it is working

    ubuntu@db:/etc/kong$ http GET :8000 Host:example.com
    HTTP/1.1 401 Unauthorized
    Connection: keep-alive
    Content-Length: 41
    Content-Type: application/json; charset=utf-8
    Date: Tue, 23 Apr 2019 07:29:12 GMT
    Server: kong/1.1.0
    WWW-Authenticate: Key realm="kong"

    {
        "message": "No API key found in request"
    }

### Create a consumer via the API

1. Create a consumer

    http POST :8001/consumers/ username=example

Eg.

    HTTP/1.1 201 Created
    Access-Control-Allow-Origin: *
    Connection: keep-alive
    Content-Length: 119
    Content-Type: application/json; charset=utf-8
    Date: Tue, 23 Apr 2019 07:39:31 GMT
    Server: kong/1.1.0

    {
        "created_at": 1556005171, 
        "custom_id": null, 
        "id": "e5e40ba9-e704-4116-ab67-5bbc326c6f7b", 
        "tags": null, 
        "username": "example"
    }

2. Give that user key credentials

    http POST :8001/consumers/example/key-auth key='Examnlek276%sggj'

Eg.

    ubuntu@db:~$ http POST :8001/consumers/example/key-auth key='Examnlek276%sggj'
    HTTP/1.1 201 Created
    Access-Control-Allow-Origin: *
    Connection: keep-alive
    Content-Length: 151
    Content-Type: application/json; charset=utf-8
    Date: Tue, 23 Apr 2019 07:41:19 GMT
    Server: kong/1.1.0

    {
        "consumer": {
            "id": "e5e40ba9-e704-4116-ab67-5bbc326c6f7b"
        }, 
        "created_at": 1556005279, 
        "id": "a60f971e-6ce0-4452-9426-42c742d53441", 
        "key": "Examnlek276%sggj"
    }

3. Try it with the key

    http GET :8000 Host:example.com apikey:Examnlek276%sggj

Eg.

    ubuntu@db:~$ http GET :8000 Host:example.com apikey:Examnlek276%sggj
    HTTP/1.1 200 OK
    
### Check Listening ports on your kong server

    sudo netstat -plnt

    tcp        0      0 0.0.0.0:8443            0.0.0.0:*               LISTEN      37818/kong -c nginx
    tcp        0      0 127.0.0.1:8444          0.0.0.0:*               LISTEN      37818/kong -c nginx
    tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      37818/kong -c nginx
    tcp        0      0 127.0.0.1:8001          0.0.0.0:*               LISTEN      37818/kong -c nginx

### More Reading and References

* [Kong Clustering](https://docs.konghq.com/1.1.x/clustering/)
* [Kong Configuration file Reference](https://docs.konghq.com/1.1.x/configuration/)
* [Kong CLI Reference](https://docs.konghq.com/1.1.x/cli/)
* [Kong Proxying Reference](https://docs.konghq.com/1.1.x/proxy/)
* [Kong Admin API](https://docs.konghq.com/1.1.x/admin-api/)

### Exporting your configuration to Yaml

Sometimes you want to have a db-less instance

You can export your configuration to a `.yml` file using [deck](https://github.com/hbagdi/deck)

You can install it from their [releases ](https://github.com/pantsel/konga/releases)

Then run:

    deck dump

### Installing Konga (The Kong Frontend)

1. Install [Node](https://nodejs.org/en/download/) on the server

2. Install the package

    git clone https://github.com/pantsel/konga.git
    cd konga
    npm i

3. Create a postgres user

4. Create the `.env` file in the root directory

5. Migrate the db

    node bin/konga.js prepare

5. Open port `1337` on the firewall

6. Run konga in production:

    npm run production

### Setting up Kong and Konga systemd service

1. Create the kong service

    sudo vim /etc/systemd/system/kong.service
    
2. With the following

    [Unit]
    Description=Kong service
    After=syslog.target network.target postgresql.service

    [Service]
    Type=forking
    LimitAS=infinity
    LimitRSS=infinity
    LimitCORE=infinity
    LimitNOFILE=4096
    User=root
    Group=root
    ExecStart=/usr/local/bin/kong start
    ExecReload=/usr/local/bin/kong reload
    ExecStop=/usr/local/bin/kong stop

    [Install]
    WantedBy=multi-user.target

3. Create the konga service

    sudo vim /etc/systemd/system/konga.service 

4. With the following content

    [Unit]
    Description=Konga service
    After=kong.service
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=always
    RestartSec=1
    User=ubuntu
    Group=ubuntu
    ExecStart=/usr/bin/node --harmony app.js --prod
    WorkingDirectory=/var/www/konga
    StandardOutput=syslog

    [Install]
    WantedBy=multi-user.target

### Setting listen port for production

Kong listens on `8000` and `8443` by default.

When you are ready to go production, set the following [proxy_listen](https://docs.konghq.com/1.1.x/configuration/#proxy_listen) in the configuration file:

    proxy_listen = 0.0.0.0:80, 0.0.0.0:443 ssl

Remmeber to allow these ports and disable the old ones:

    sudo ufw allow 80
    sudo ufw allow 443

Use `sudo ufw status` to check the old firewall rules

    sudo ufw deny 8001
    sudo ufw deny 8000
    sudo ufw deny 8443
    sudo ufw deny 8444
    
### Kong Log folder Locations

The log locations for kong are: `cd /usr/local/kong/logs`

## 4. Kong Architecture

Black box - takes requests as input, routes them to the right service and gives you a response back.
Kong gets full access and control over the request: transforming and analysing its attributes.

Common features can be refactored into one seperate and single layer.
No need to reimplement your Json Web Tokens in python on your paymetn API and in scala on your JWT server.
Remove duplicate boilerplate.
No more rate limiting.

Kong is 99.8% Lua scripts

### HTTP Server Blocks

Kong sits on Open Resty which sits on Nginx, on the shoulders of giants.

Nginx is one of the most popular event-based web servers and load balancers. Its behavior is defined by a configuration-based construct, which means it doesn’t support dynamically programmable configurations

OpenResty enables this feature with the lua-nginx-module. This module enables developers to extend their Nginx with custom behavior written in Lua. Openresty wraps Nginx and lua-nginx-module into one package.

### Database blocks

Scenarios where data is stored in dbs:

* API's managed through the admin interface
* Kong internals and clustering
* Custom plugin behaviour

> When Kong is used in a multi-region, multi data-center, high-availability environment, Cassandra is usually the preferred choice, because a distribute setup is built into its core

### Request / response path

> Kong uses a cache in memory to minimise access to the database

> All the entities such as APIs, Plugins or Consumers are cached in memory

> Now, Kong uses a completely different strategy. All nodes perform a periodic background job to check if configuration changes have been received and processed by other Kong nodes.

## 5. Meet the Kong

### Customize Nginx

Can tweak or extend nginx by adding a new `server_block`

When `kong start` 's it creates a runtime nginx configuration: `/usr/local/kong/nginx-kong.conf`

Which can be copies and changed to run your own configuration with:

    kong start -c kong.conf --nginx-conf custom_nginx.template

### Play with Kong

* Kong as a proxy - passes requests to backend services
* kong as a middleware - extends services with transformations, rate-limiting
* kong as a resource manager - manage users and services with authentication

### Kong Load Balancing

1. DNS Based load balancing

* No kong based settings
* Upstream services are registered with a DNS service provider, kong only receives results 
* Mutliple A records for different IP addresses (with a straight round robin)
* SRV records cantain weight and port information

2. Dynamic ring-balancer based load balancing

* Managed by kong as a service registry
* `upstream` and `target` entities are used for configuring the ring balancer
    * `upstream`: virtual hostname in an upstream url
    * `target`: IP or hostname with a port that directs service

More in the book

#### Health Check your API

* Active Health Check: Periodically request a specific HTTP endpoing
* Passive Health Check (Circuit breaker): Monitor the ongoing traffic to each service and determine a healthy response of traffic

Load balancers are able to keep traffic stable without any errors

#### Clustering

To handle much more traffic you need more instances - kong nodes pointing to the same database and sharing configurations. TO make it work you need lots of kong nodes and a load balancer in front.

#### Caching

Cached data are APIs, Consumers, Plugins, Credentials
Kong avoids database calls.
In a cluster the config changes need to be propagated

## 6. Extending Kong

You can extend it with:

* Lua Language
* Open Resty
* Lapis Framework
* Kong DAO Factory

If you want to learn lua and extend kong read this section

## 7. Integrating with Others

* Kong excels at managing API's but can't cover all of DevOps by itself

### Docker

* Linux container based on an open source virtualization platform
* Make more efficient use of resources compared to VM's
* Isolated from the host OS - more portable
* Shares the linux kernel
* Easy to build, run and ship distributed applications

### Kubernetes

* A container orchestration tool for automating deployments, scaling and management of containerized applications
* Grouping containers into logical units - managing containers becomes easier
* Container deployment with multiple hosts by decoupling resources and networking from the user
* Auto places containers in a suitable host, auto restarts the container in an unstable situation
* Scaling, replication, rolling update, rollback

> A Kubernetes cluster is constructed with multiple nodes, which is another host, and nodes are constructed with lots of `pods`, which is a logical group of container applications. `pods` are deployed through `deployment`, and these deployed containers are accessible through `service`, which helps the container to be exposed publicly

The book shows you how to deploy your services and kong with docker and kubernetes...

### Monitoring and Analysis

Without kong, you have to add a logging module to each service

#### Datadog

A monitoring and analytics service for cloud applications

Details on how to set it up are in the book...

#### ELK stack

* Elasticseach - Open source, distributed, RESTful JSON-based search engine
* Logstash - Data processing pipeline that ingests data from multiple sources and sends to elasticsearch
* Kibana - Visualise data with charts and graphs

Workflow:

    Log -> Logstash (Collect and Transofrm) -> Elasticsearch (Search and Analyse) -> Kibana (Visualise and Manage)

There is info in the book on how to set this up

#### Konga

A GUI for the Kong Admin API

* Backup, restore and migrate kong nodes using snapshots
* Monitor node and API states with health checks
* Email/Application notifications
* Multiple users

Lots of info in the book about setting up

## 8. API Gateway Techniques

API Gateway is more like an API interface or middleware.
API Management has a bigger scope - process of generating and publishing API's.

### Multi Consumer Management

How many consumers and how many requests per consumer
Differentiating between which consumers can access (authentication), and what consumers can access (authorization).

### Versioning Management

* The consumers of an API will invest a significant amount of time and resources building client applications
* Must guarantee that an API will be in service for a long period of time
* Differentiating consumers can then let you point old consumers to an old api version

#### Changes that break backward compatibility

* Removing resources (paths) or verbs (methods)
* Add mandatory input fields
* Convert input fields from optional to mandatory
* Modify the name or type of a parameter
* Adding pagination

### Features

* Logging for failure or error
* lear data origin
* Notification for failure or errors
* Caching Criteria
* Rate limiting
* Limit the amount of requests consumers may have
* Allocate more for higher priority requests
*

### HTTP CORS Issue

* If your API Gateway makes an HTTP request to a different domain, it needs to be CORS-friendly
* If you use cross domain requests, you need to add the Access-Control-Allow-Origin header to your responses in your handlers

Kong has a CORS plugin to do this for you

#### HTTP Methods

* GET — For returning resources
* POST — For creating a new resource
* PUT — For replacing a resource
* PATCH — For updating a resource with versions
* DELETE — For deleting a resource

#### Business Authorization in the API gateway

The API gateway may authenticate users but does not mean it can always authorize users.
What if a user can view movies but not book one...should this authoization logic sit on the gateway level.
A user's scope can be very specific and it can change the core of the system.
It is better to put the user's authorization, espescially business authorization for a user in the level of service.

### Composing Data in an API gateway

To make responses more consumer focused **transformers** are used.

1. Collaborating 2 or more services to respond to a single request
2. Remove, rename, replace, add, or even append a request and/or response

Combining requests can be done at gateway level

### Transforming API requests and responses

The book does not tell you how to do this...

### Doing Workflow in the API gateway

Say for example you have a flow:

1. Customer books 2 tickets for watching a movie in a booking service
2. Service generates an invoice in the booking service
3. System sends an invoice to email using a 3rd party service

These relationships are common, but important not to have them at the gateway level (or service level for that matter).
Apart from the high memory usage issue, it causes high dependences between services at the gateway level.
Which is like doing it like a monolith.

> There are options to do event driven processes in a microservices way that use a message broker.

## 9. API Security

In a Microservices architecture the API gateway acts as the security endpoint

It is crucial to protect the access to those microservices so only authorized applications (clients) can interact with those services.
It is required to provide end users, or resource owners, a mechanism to protect their data from unwanted access.

### Key Authentication

Usually there is an onboarding proces to sign contracts with the users of the API. Then the third party will be given a secret token to interact with the api.
That token will only identify the client application, not the resource owner.

A resource owner - an entity capable of granting access to a protected resource. When the resource owner is a person, it is referred to as an end-user.

To protect the resource owner, a different method called Oauth2 is used.

You can create reports that track each consumer.
So you can bill and see if a consumer is using the API.

### Creating Consumers

The company wanting access to the api will be added as a consumer on kong.

After creating the consumer we will need to install the `key-auth` plugin


