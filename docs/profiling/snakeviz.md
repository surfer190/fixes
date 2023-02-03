---
author: ''
category: profiling
date: '2023-01-04'
summary: ''
title: Snakeviz
---

## Snakeviz

Snakeviz is a browser absed visualizer of python [`cProfile`](https://docs.python.org/3/library/profile.html#module-cProfile) output.

    pip install snakeviz

Example usage:

    python -m cProfile -o expiring_dict_test expiring_dict_test.py
    snakeviz expiring_dict_test

It can be seen as more user friendly than the python stats module:

    import cProfile
    from pstats import Stats

    profiler = cProfile.Profile()
    profiler.runcall(test)
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()

## Source

* [Snakeviz: Info and Interpreting Results](https://jiffyclub.github.io/snakeviz/)
