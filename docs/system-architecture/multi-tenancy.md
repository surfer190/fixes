---
author: ''
category: System-Architecture
date: '2018-08-10'
summary: ''
title: Multi Tenancy
---
# Architecting Multi-tenant Applications

In building a Saas (Software-as-a-service) product, an essential ingredient is the ability to have multiple tenants or customers especially when the target fo the product is a team, group or organisation.

There are three options:

* One database per tenant
* One schema per tenant
* Have all tenants share the same tables

According to [citrusdata](https://www.citusdata.com/blog/2016/10/03/designing-your-saas-database-for-high-scalability/) your choice comes down to:

* If you are building for scale, have tenants share the same tables. (1000's of tenants)
* If you are building for isolation, create one database/schema per tenant. (5 - 50 tenants)

## Resources

When doing any job, always use the right tool for the job. You don't use a hammer for a screw, so you should use a database for what it is for - storing large amounts of data.

When you split up the databases, the database shared buffers, operating system cache, connection count, background processes and logs may be an issue.

If you are using a single table, keep in mind that most transactins and joins will have the `tenant_id` dimension, so you should shard your database on this key so all related records are co-located.

## Ease of Maintenance

Another issue is changes to the schema and adding of indexes. If you have multiple schemas or databases, then you have to apply changes to all schemas and what if an error occurs mid way.

But what about tenants requiring different fields. Well there is the [salesforce custom columns implementation](http://www.developerforce.com/media/ForcedotcomBookLibrary/Force.com_Multitenancy_WP_101508.pdf) but more recently databases support semistructured data like [Hstore, json and jsonb](https://www.citusdata.com/blog/2016/07/14/choosing-nosql-hstore-json-jsonb/).

The difficulty lies in the ORM (Object Relational Mapper) of your framework of choice and how easily the tenant dimension can be included.

### Google F1 Paper

This google paper explains some challenges faced when [scaling adwords for multi-tenancy](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41344.pdf)



