---
author: ''
category: profiling
date: '2022-12-02'
summary: ''
title: Profiling Memory
---

Check out [memray on github](https://github.com/bloomberg/memray)

    memray run my_script.py
    memray run -m my_module

View the flamegraph:

    memray flamegraph my_script.2369.bin

Is the bottleneck memory?

Filling up and then having to use disk?
thrashing - using virtual memory and not just physical memory - slow reads and writes from and to disk.
