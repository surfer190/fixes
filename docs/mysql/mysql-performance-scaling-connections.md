---
author: ''
category: MySQL
date: '2022-06-22'
summary: ''
title: MySQL - Performance, Scaling and Connections
---
# MySQL: Performance, Scaling and Connections

This article is based on the information from [mysql's Connection Handling and Scaling article](https://dev.mysql.com/blog-archive/mysql-connection-handling-and-scaling/).

> A key takeaway from this article is that everything depends until you put it to the test. There is a database and system benchmarking tool called [`sysbench`](https://github.com/akopytov/sysbench) that can be used to put your mysql instance or cluster to the test - to find what the optimal configuration should be.

Mysql server `mysqld` executes as a single OS process, with multiple threads executing concurrent activities.

We can see this by running this command on a system with mysql running:

    ps -eo psr,pcpu,pmem,size,thcount,comm
    
    PSR %CPU %MEM  SIZE THCNT COMMAND
     0  3.8 23.8 993920   51 mysqld

From this we can see the processor is assigned to the core 0.
It is using 3.8% of CPU and 23.8% of RAM.
It needs `993920` of swap space for writeable pages to be swapped out - not really sure what that means.
`THCNT` is the thread count so it has 51 threads running.

Lets remind ourselves what a process and a thread is:

* A process is a computer program under execution - they are independent and isolated from other processes - and do not interrupt each others execution - context switching it expensive (heavy weight) - multithreaded processes contain multiple threads
* A thread is a lightweight process linked to a process - threads share memory space with the parent process and other threads within the process.

> When a user connects to the database a user thread is created inside `mysqld` and this user thread executes user queries,  sending results back to the user, until the user disconnects.

> Connections correspond to Sessions in SQL standard terminology. A client connects to the MySQL Server and stays connected until it does a disconnect

MySQL is good at connecting and disconnecting clients - it can handle 80000 connects/disconnects per second.

When you have many long running connections - that do not sleep but query as soon as getting results (busy connections). You can have 5000 Transactions Per Second with 200 Connections. Setting `max_connections` to 10000 - will not help the situation it will only use up more memory.

To check the optimal `max_connections` use:

> What is the maximum load? And how do I know that the server has reached maximum load? You have to test your workload, for example as follows: You can start with 2 busy clients and measure server TPS and Latency, and then continue step-wise by doubling the number of clients for each step. Initially, TPS will increase and latency will be constant for each step you take. At some point TPS will be the same as before and latency will start to increase, and this is the maximum load and the maximum number of (useful) clients.

The recommended maximum number of user threads is 4 times the number of CPU cores:

Eg. 48 cores x 4 = 196 user threads

There may be a point where you are waiting for reads from the disk - I/O.

There is a post about the [I/O issue by Dimitrick](http://dimitrik.free.fr/blog/posts/mysql-performance-1m-iobound-qps-with-80-ga-on-intel-optane-ssd.html)

## DML vs DDL

You can use SQL queries to achieve not only data reads, updates and deletes.
You can also use it to manipulate (`ALTER`) the schema and add indexes.

* DDL means Data Definition Language - which is the `CREATE`, `ALTER` and `ADD INDEX` functions. Works on the schema.
* DML means Data Manipulation Language - which is `INSERT`, `UPDATE` and `DELETE` functions. Works on the data.

## Limits to Thread Concurrency

* Mutex - shared internal data structure - only one thread can access at a time
* Locks
    - Data locks caused by DML SQL queries - usually a row lock
    - Meta-data locks by DDL SQL queries  - usually protects the whole schema - As a consequence, scalability bottlenecks caused by locks must often be resolved at the `OLTP` (Online Transaction Processing) application design level, e.g. a better database schema design combined with better query designs.
* Disk and Network IO - IO is something one tries to minimize whenever possible, and when not possible one tries to do it as efficiently as possible, e.g. pre-fetching, parallelizing, batching

## The Role of Application Developers

In some cases application developers are in control of the overall system architecture, the database schema, and database queries.

The classical use case for MySQL is Online Transaction Processing (OLTP) which typically has demanding response time requirements. Acceptable database response times are often specified in milliseconds and this will of course limit the type of queries which can be expected to run (perhaps combined with limitations on data volume and the structure of the database schema). This is often contrasted to  Online Analytical Processing (OLAP) where there are more complex queries, but the query frequency is lower and response time requirements may be more relaxed.

Especially for OLTP, the application developer must take care in designing queries that can execute within certain response time SLA and that can be executed in parallel.  It is not very hard to produce a workload which does not scale, for example many parallel clients doing nothing other than updating the exact same row in the same table (see alternative designs here).

## Horizontal Scaling Options

* [Vitess](https://vitess.io/)

## Source

* [MySQL Connection Handling and Scaling article](https://dev.mysql.com/blog-archive/mysql-connection-handling-and-scaling/)
* [Non-persistent Connection Performance in MySQL](https://yoshinorimatsunobu.blogspot.com/2012/12/non-persistent-connection-performance.html)
* [Threads vs Processes](https://www.baeldung.com/linux/process-vs-thread)
* [DML vs DDL](https://www.geeksforgeeks.org/difference-between-ddl-and-dml-in-dbms/)