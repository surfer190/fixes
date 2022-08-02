---
author: ''
category: Python
date: '2022-05-10'
summary: ''
title: Common python Interview Questions
---

## Common Python Interview Questions

### What is a concrete class?

A class where all the methods have been implemented.

### What is a factory method?

A `Factory Method` provides a separate component with the responsibility to decide which concrete implementation should be used based on some specified parameter.
Used to make code simpler, more reusable and easier to maintain - ensures there is a single responsibility.

The factory method does not call the concrete method - it just decides returns the concrete method object (since everything in python is an object) to call.

For example an object can be serialised (converting objects to different representation)

    def _serialize_to_json(song):
        ...
    
    def _serialize_to_xml(song):
        ...

    def get_serializer(format):
        if format == 'JSON':
            return _serialize_to_json
        elif format == 'XML':
            return _serialize_to_xml
        else:
            raise ValueError(format)

#### Factory Method as an Object Factory

More flexibility for when requirements change.

`object_factory.py`:

    class ObjectFactory:
        def __init__(self):
            self._builders = {}

        def register_builder(self, key, builder):
            self._builders[key] = builder

        def create(self, key, **kwargs):
            builder = self._builders.get(key)
            if not builder:
                raise ValueError(key)
            return builder(**kwargs)

`music.py`:

    import object_factory

    # Omitting other implementation classes shown above

    factory = object_factory.ObjectFactory()
    factory.register_builder('SPOTIFY', SpotifyServiceBuilder())
    factory.register_builder('PANDORA', PandoraServiceBuilder())
    factory.register_builder('LOCAL', create_local_music_service)

`program.py`:

 In program.py
 
    import music

    config = {
        'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
        'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
        'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
        'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET',
        'local_music_location': '/usr/data/music'
    }

    pandora = music.factory.create('PANDORA', **config)
    pandora.test_connection()

    spotify = music.factory.create('SPOTIFY', **config)
    spotify.test_connection()

    local = music.factory.create('LOCAL', **config)
    local.test_connection()
    
[Source: Factory Method Real Python](https://realpython.com/factory-method-python/)

### What is a Meta class?

> metaprogramming refers to the potential for a program to have knowledge of or manipulate itself

* The type of a class is a class.
* The type is responsible for creating new instances. So if the type of a class is a class then we can write classes that create classes.
* Done by overriding the `__new__`

> metaclasses are to classes as classes are to instances

[Source: RealPython Meta Classes](https://realpython.com/python-metaclasses/)

### What is Inheritance and do you have an example?


### Read Committed vs Repeatable Read

Read committed is an isolation level that guarantees that any data read was committed at the moment is read. It simply restricts the reader from seeing any intermediate, uncommitted, 'dirty' read. It makes no promise whatsoever that if the transaction re-issues the read, will find the Same data, data is free to change after it was read.

Repeatable read is a higher isolation level, that in addition to the guarantees of the read committed level, it also guarantees that any data read cannot change, if the transaction reads the same data again, it will find the previously read data in place, unchanged, and available to read.

More on [Read Committed vs Repeatabe Read on this answer](https://stackoverflow.com/questions/4034976/difference-between-read-commited-and-repeatable-read)

### What is an Abstract method, static method and class method?

An abstract class is a blueprint for other classes.
A class which contains one or more abstract methods is called an abstract class.
An abstract method is a method that has a declaration but does not have an implementation.

    from abc import ABC, abstractmethod
    
    class Polygon(ABC):
        @abstractmethod
        def num_sides(self):
            pass
    
    class Triangle(Polygon):
        # overriding abstract method
        def num_sides(self):
            print("I have 3 sides")
    
    class Quadrilateral(Polygon):
        # overriding abstract method
        def noofsides(self):
            print("I have 4 sides")
    
    triangle = Triangle()
    triangle.num_sides()
    
    square = Quadrilateral()
    square.num_sides()

[Source: Abstract Methods geeksforgeeks](https://www.geeksforgeeks.org/abstract-classes-in-python/)

### What is a thread lock?



### What is REST?



### What and how is gRPC used?

* gRPC stands for gRPC Remote Procedure Calls.
* If is a client-server architecture - where you interact with remote objects as if they are local - using stubs / clients.
* It is used for interservice communication but can also be used as a api to mobile apps and web clients.
* It can be used with protocol buffers to allow for language agnostic remote procedure calls.
* Used in distributed system for low-latency calls.
* Can be used with serialisation schemas like protocol buffers - for forward and backward compatible messaging

### What are design patterns, can you name a few?

More detail on [design patterns](https://fixes.co.za/python/design-patterns/)

### If you are seeing bottlenecks in your Relational DB what can you do?

* Profile
* Check the number of connections
* Check slow queries
* Add Indexes
* Sharding
* Avoid complex queries for transactional data

### How does garbage collection work?

You have the address and size.

Mark and sweep alogorithm

1. Walk the heap and mark all places that are referenced - start with globals
2. Remove all places that are not marked

a memory leak - is when there is a ciruclar reference but nothing references the circle.

Generation scavaging?

### What is a bitmap database index and how is it implemented?

A bitmap is a mapping from some domain to bits.
Usually pixels.

### How does a Python Dict use hashing?

The complexity is O(1) - no matter the size of the dict - the lookup operation costs a constant amount.

1. The key is hashed
2. the keyspace is really big but the size of dict much smaller so to get the position in the dict - you modulo the keyspace by the size of the dict (dict space)
3. if there are collisions you increment to the next hash and keep incrementing

Ideally the dict remains under 80% filled as you will get lots of collisions and it is better to recreate the dict

Another way is using a linked list at the hashed position

If we decrease the portion of the key we hash to a smaller amount - we will have alot more of the same hash and more collisions

If we used microsectonds as the key - when retrieving the value we would not know where to look

### How is a singleton implemented in python?

A singleton is a class that ensures only a single instance can ever exist (or none)

### How do you implement a LRU cache?

### Flower garden

Given a number of positions a flower can be planted in eg. 46. Also given the spots at which flowers are planted. (7, 12, 14)

Knowing that flowers only grow well without an adjacent flower.

How can you calculate the maximum flowers that can be added.

....

### Big O-Notation

What is the big O for sorting?

Quicksort: `O(nlogn)` is divide and conquer. Take a random element put element bigger than it ahead and smaller below. When sorting you have to touch each of the items at least once. Therefore sorting is always `O(n)` or above. SPace complexity is `O(log(n))`

The act of splitting the dataset is `log n` as it reduces the operations in half in the long run.

Bubblesort: `0(n^2)` on the average case because you you have to make as many passes of the set as there are elements in the collection.

Mergesort: `O(nlogn)` Breaks a list into n sublists, merge them together to create a sorted sublist. It does not sort in-place - so memory space complexity is `O(n)`

Heapsort: `O(nlogn)` Project the collection onto a tree. Then it is converted into a max tree. Then you iterate and find the biggest item.

Insertion sort: Moving left to right we sort - ensure item is in the correct place of previous items
Worst case of `O(n^2)` big Oh of N squared.

> A heap is a binary tree - each node is greater or equal to its children (max heap) or smaller or equal to (min heap)

Timsort: A hybrid or mergesort and insertion sort

Binary search tree: ordered so always `O(logn)`

Hash table: average is `O(1)` worst case is `O(n)`

Sources:

* [HeapSort](https://www.happycoders.eu/algorithms/heapsort/#What_is_a_Heap)

### Different types of programming languages

* Compiled: converted into machine code for processors to execute - there is a build step and execute step. They create single binaries. They are faster and give the developer more control over cpu and mem. Examples: C, C++, Erland, Go, Haskell
* Interpreted: Execute and interpreted - line by line. Examples: PHP, Ruby, Python, JS. More flexible: dynamic typing, platform independent interpreter deals with it. Slower.
Functional

- functional: avoids state and mutable data to give deterministic outputs to inputs to functions
- object oriented: using object to represent things - allows for inheritance and to not repeat yourself
- procedural: based on a procedure call - derived from impertive
- imperitive: statements top to bottom of what the program must do
- declarative: state what the program must do without detailing how it does it

In python context?

### Concurrent and asynchronous programming

concurrency - simultaneous work.

process: a program. A process being blocked does not affect other processes. Have at least 1 thread - have seperate memory space.
thread: a segment of a process - context switching, creation and termination is faster. A thread blocked does affect other threads. Shared memory space.

global interpreter lock (GIL) - only one thread can hold the control of the python interpreter.
Even in multithreaded architectures - only a single thread can execute at a time.
A lock of its internal state in CPython.

Multitasking - Threading and `asyncio` all happen on a single processor.
`multiprocessing` - python creates a new process that can run on a different core. CPU bound work.

I/O bound tasks are sped up with prevnting of blocking - or overlapping the wait time.

synchronous code is better to write, test and debug.

`async def` tells python that the function needs to be called with `await`
`await` hands back control to the event loop

1. hold out until performance becomes an issue
2. determine the type of concurrency you need: I/O bound - multitasking, CPU bound - multiprocessing (asyncio is safer than pre-emptive multi-tasking/threading - race conditions from shared state)

> Use an atomic message queue

### Time and space complexity

see Big O

### Distributed systems

A group of computers working together to appear as a single computer.

* Shared state
* operate concurrently
* Can fail independently

Traditional databases are stored on the filesystem of one single machine
For us to distribute this database system, we’d need to have this database run on multiple machines at the same time.

Sharding the database - splitting the index or parts of a db - must be done manually on relational dbs.
Not so on NoSQL.
Relational dbs: are slow because of joins, difficult to horizontally scale, queries are unbounded
NoSQL dbs: do not allow joins, force you to segment data, puts bounds on your queries

Allows scaling horizontally - with tradeoffs of harder to debug, deploy and maintain.
Horizontal scaling is cheaper.
No cap on horizontal scaling. Allows for fault tolerance and low latency - a node in cities.

### Relational databases

SQL
Better for Online Analytical Processing (OLAP) - although OLTP is posssible.
NoSQL prevents you from doing actions that will slow down.
When designing the database you need to know the user cases of the frontend.

* Atomicity - either succeed or fail
* Consistency - not consistent with master - single valid state 
* Isolation - concurrent execution of transactions same state as done individually
* Durability - what is committed remains committed

Normalisation: 

* 1NF - each record unique, each cell has single value
* 2NF - has primary key
* 3NF - No transitive functional dependencies - Title on person - in seperate table

Most systems are distributed - centralised system - controlled by a single actor.

Eventual consistency is prefered.

You can choose 2 of 3: availability, consistency and partition tolerance

BASE:

* Basically Available
* Soft state
* Eventual consistency

Cassandra, mongo, dynamoDB

Map reduce  - map data and reduce it to what you need from database warehouse.
Problem was these jobs could take 2 hours and were not fault tolerant.
