# Meteor.js

### Single Page App?

Yes, similar to ember and angular. The difference is that those frameworks are used for single use applications.
Meteor owns the entire stack.
Server: Node
DB: Mongo
Middle: ShadowDom
DDP (Rest for Web Sockets) [supports pubsub] and Html

When you change a value in the browser, mini-mongo synchronises that change to the db with ddp, called Latency Compensation.

### In Production

Yes. Subdomain actual app, wit front-end actually a cms like jekyll.

### Testability

Built in testing.

### Deployments

[MeteorUp](https://github.com/arunoda/meteor-up)

### SEO

Install [spiderable](https://atmospherejs.com/meteor/spiderable)


### Packages

[Atmosphere](https://atmospherejs.com/) is a package site

### Scalability

Scales fine. 
