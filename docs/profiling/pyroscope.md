---
author: ''
category: Profiling
date: '2022-11-13'
summary: ''
title: Pyroscope profiling
---

# Pyroscope

Pyroscope is an open source continuous profiling platform

Profiling is an effective way of understanding which parts of your application are consuming the most resources.

Continuous Profiling adds a dimension of time that allows you to understand your systems resource usage (i.e. CPU, Memory, etc.) over time and gives you the ability to locate, debug, and fix issues related to performance.

Use cases:

* Find performance issues in your code
* Resolve issues with high CPU utilization
* Locate and fix memory leaks
* Understand the call tree of your application
* Track changes over time

Overhead: ~2-5%

## How does Pyroscope work?

* Pyroscope server - Processes, aggregates, and stores data from agents
* Pyroscope agent - Records and aggregates what your application has been doing

## Storage Efficiency

The problem with storing profile data:

* Too much data to store efficiently
* Too much data to query quickly

Solved by:

* Using a combination of [tries](https://en.wikipedia.org/wiki/Trie) and trees to compress data efficiently
* Using segment trees to return queries for any timespan of data in Olog(n) vs O(n) time complexity

1. Turning the profiling data into a tree - less duplication
2. Adding tries to store individual symbols more efficiently
3. Optimizing for fast reads using Segment Trees - reads turn from O(n) to Olog(n)




## Sources

* [Pyroscope docs](https://pyroscope.io/docs/)