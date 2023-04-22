---
author: ''
category: Python
date: '2023-04-20'
summary: ''
title: 10 Python Performance Tips
---

## DRAFT

> Readability counts

Use discretion. Oftentimes code being obvious to the reader is a greater gain than nanoseconds of performance. Not always.

IO bound performance bottlenecks are usually several orders of magnitude greater than CPU bound bottlenecks.

1. **Use tuples over lists where the data does not change after creation**. Tuples store less data in memory than lists and use resource caching - so can be instantiated quicker. Where the number of elements is 1 to 20 - the garbage collector does not give the data back to the system. So the addresses can be reused without a system call.
2. **Allocate lists with a list comprehension over use of append**. Using `append` overallocates memory.
3. **Use sets when unique data is needed**
