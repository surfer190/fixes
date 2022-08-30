---
author: ''
category: System Architecture
date: '2022-05-09'
summary: ''
title: Databases, Events and Scale
---
## Databases, Events and Scale

- horizontally scaling vs vertical
- Sharding database (splitting index eg. A - H, I - Z) with MySQL, PostgreSQL must be done manually - whereas noSQL and some cloud provider give automatic sharding.
- Cluster proxy / load balancer in front of shards
- Availability - through replication 
- Issues of consistency - sacrifice instantaneous consistency for eventual consistency
- NoSQL databases were designed with scale in mind - automatic scaling (cassandra) - shards in nosql are equal - shards in SQL are not
- gossip protocol controls communication between nodes
- NoSQL: availability prioritized over consistency
- DynamoDB is built for scale - it won't let you write a query that won't scale

Problems with relational databases at scale:

1. Slow output of SQL Joins - CPU intensive - linear time - as db grows performance drops
2. Difficulty horizontal scaling - vertical vs horizontal (limits for vertical) - horizontal scaling means each node only handles a portion of the data - tricky with relational dbs as there is no clear way to split the data. Horizontal scaling works best when a single request can be handled by a single node.
3. Unbounded nature of queries - get all records (SELECT * FROM table) - scans/reads entire db. Grouping and ordering is also expensive. Aggregations are ready to take down your db at scale.

How NoSQL fix these problems:

1. Do not allow joins - RDBMS use normalisation (do not repeat) benefits are storage efficiency and data integrity.. NoSQL you must know how your data must be read and written up front to avoid the need for flexibility. Data integrity is now the concern of the application - sometimes allowing duplicates easier for fields that do not change. Storage is now less expensive.
2. Forces you to segment your data
3. Puts explicit bounds on your queries

> Cloud providers want you using noSQL as it is storage inefficient

NoSQL requires you split up the data into smaller pieces and that you run your queries just with each piece. A partition key or segment key.

For example a userID:

Ids 0 - 3333: Node 0
Ids 3333 - 6666: Node 1
Ids 6666 - 9999: Node 2

> All queries must include the partition key

> Most nosql dbs hash the partition key before assigning it to a node

Then there is a router or cluster proxy

> This sharding mechanism is what allows for NoSQL’s essentially infinite scale without performance degradation

NoSQL puts a 1MB limit on the query and scan
If there are more than 1MB results the resturned query will have a `LastEvaluatedKey` to handle pagination on the client side.

To guarantee single digit millisecond response.

3 operations:

1. find node for partition tree - hash table: O(1)
2. find starting value for sort key - B-tree: O(log n)
3. read values - sequential read to max 1MB

> No support for `MIN`, `MAX`, `AVG`

It is likely better for tha application to store aggregations in a summary item collection.

Problems with NoSQL is paginating - fix on application side - just get the most recent. Also hot keys - frequently queries data - tricky to find when designing db. Can scale to 3000 read capacity units (RCU) and 1000 write capacity units (WCU) per second.

OLAP - Online analytical processing
OLTP - Online transaction processing

Moving from OLTP to OLAP is done with an ETL process - extracting, transforming, and loading data.

Hash table: A key value store - During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. the hash function is O(1).

### Event-driven

Eg. When a file is uploaded to s3 a lambda function is called

Is it for your use case?

1. Are you passing around self contained transactions
2. Are useful events available for free? Eg. S3 to lambda
3. Do you strongly decouple your microservices? when one service gets a spike in traffic - do the others have to follow suit? Perhaps other services use different programming languages in different offices in different departments

What is an event?

* can have some generic fields at the top level - standard envelope
* then event-detail
* have a source field
* similar to awx - cloudevents.io
* difficult to change after shipping events
* Why should you even care what it is - the software doesn't care.
* filtering, routing and storing is important
* Some events - the order matters (FIFO) requires a single source and single destination. Sometimes only the single user session needs order.
* duplication? suppose your service crashes - you didn't get the message so the infrastructure sends it again. To detect this - backends all have transactional databases and detect. Another way is to make api idempotent. Eg. Create queue - if it exists it does nothing
* kafka - broadcast an event and everything gets to see it (pub/sub)
* Getting the events: push or pull. Pushing events is promising you can process them as fast as we send them. Polling is better - only process when you have the capacity.
* Serveless approach - over http, broker/cluster - rabbitmq or kafka - have to be managed and have a flat top scaling cruve, advantages - don't use http - use tcp/ip with ampq - lower latency solved with http2, http3 (QUIC) - U is UDP
* Filters - allow you to only subscribe to certain events
* json vs binary format? in kakfa and grpc alot of people use binary formats: avro, thrift, protocol buffers...bottleneck is not usually here
* heterogenous vs uniform events - majority are lots of different events - allowing strongly typed schemas

### Insights

Reporting - push that information down to the client (clients have enough cpu to figure it out)

workflow:

1. Entity relationship diagram - tables
2. table defining access patterns - table, gsi to query, filter conditions
3. Look at what data is changing and what is immutable

NoSQL workbench for DynamoDB

### Sources:

* [Scaling SQL and NoSQL](https://betterprogramming.pub/scaling-sql-nosql-databases-1121b24506df)
* [SQL, NoSQL, Scale and DynamoDB](https://www.alexdebrie.com/posts/dynamodb-no-bad-queries/)
* [DynamoDB paper](https://www.dynamodbguide.com/the-dynamo-paper/)
* [Amazon Dynamo DB](https://www.youtube.com/watch?v=6yqfmXiZTlM&t=1581s)
* [Moving to event driven architectures](https://www.youtube.com/watch?v=h46IquqjF3E)
