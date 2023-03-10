---
author: ''
category: Python
date: '2023-01-10'
summary: ''
title: High Performance Python
---

# High Performance Python: Book Notes

## 1. Performant Python

> Programming computers can be thought of as moving bits of data and transforming them in special ways to achieve a particular result.

There is what real hardware does - the efficient way and what python does.

### The fundamental computer system

* Computing units: CPU - operations that can be done a second
* Memory units: memory - how much data it can hold, how fast are reads and writes
* Connections between: communication layers - buses

#### CPU

Ability to transform bits into other bits

* Number of operations in a cycle - IPC (Instructions per cycle)
* Number of cycles in a second - clock speed

> Amdahl’s law is this: if a program designed to run on multiple cores has some subroutines that must run on one core, this will be the limitation for the maximum speedup that can be achieved by allocating more cores.

A major hurdle with utilizing multiple cores in Python is Python’s use of a global interpreter lock (GIL).
The GIL makes sure that a Python process can run only one instruction at a time, regardless of the number of cores it is currently using.

#### Memory

Used to store bits.

Read and write speeds impacted by:

* How it is read: sequential read vs random - sequential reads are fast
* Latency: the time it takes to read

1. L1/L2 cache - extremely fast, small amount of data - all data in cpu goes here
2. RAM - stores application code fast (64 GB range)
3. SSD - Solid state drive - faster read/write speeds than HD
4. Spinning disk HD - slow (large volume)

Speed increases - size decreases.

#### Communication Layers

* Fronside bus connects RAM and L1/L2 Cache
* External buses connect devices to CPU and memory

Drawback of GPUs is they are usually on a PCI bus which is slowed than a frontside bus

Network can also be seen as a bus.

Most important part of communication is speed of the communication

### Idealised Computing

> Avoid moving data around as much as possible

### Python's Virtual Machine

The Python interpreter (virtual machine) does a lot of work to try to abstract away the underlying computing elements that are being used.
No thought is needed as to the amount of memory to reserve for an array - or the sequence it is sent to cpu.

What is hurting perofrmance:

* Pythons objects not layed out in the optimal way in memory due to garbage collection
* it is interpreted with dynamic types - algorithmic optimisations cannot happen before hand at compile time.
* The Global Interpreter Lock (GIL) - only a single core can be used at a time

## 2. Profiling to find Bottlenecks

Profiling lets us find the biggest gains from the least amount of work.

> You could, of course, skip profiling and fix what you believe might be the problem—but be wary, as you’ll often end up “fixing” the wrong thing.

Verify, don't trust.

Extract a test case and isolate the piece of the system under test.

Used tools:

* `%timeit`
* `time.time()`
* a timing decorator

Always profile - get evidence.

> [`timeit`](https://docs.python.org/3.7/library/timeit.html) temporarily turns off the garbage collector

### Simple Approaches to Timing

Print statements:

    $ python3.7 julia1.py 
    Length of x: 1000
    Total elements: 1000000
    calculate_z_serial_purepython took 7.012973070144653 seconds
    300.0

At the core of the timing:

    import time
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    print(
        f"{calculate_z_serial_purepython.__name__} took {end_time-start_time:.5f} seconds"
    )

### Using TImeit

With python module:

    $ python -m timeit -n 2 -r 1 -v -s "import julia1_nopil; julia1_nopil.calc_pure_python(desired_width=1000, max_iterations=300)"
    Length of x: 1000
    Total elements: 1000000
    calculate_z_serial_purepython took 6.698742866516113 seconds
    raw times: 2.96 usec

    2 loops, best of 1: 1.48 usec per loop

> Not giving the expected results of 6.69s per loop

Or with ipython:

    ipython
    %timeit julia1.calc_pure_python(desired_width=1000, max_iterations=300)

> By default, if we run `timeit` on this function without specifying `-n` and `-r`, it runs 10 loops with 5 repetitions

### Using Unix time

    $ /usr/bin/time -p python julia1_nopil.py
    Length of x: 1000
    Total elements: 1000000
    calculate_z_serial_purepython took 6.756645202636719 seconds
    real         7.40
    user         7.22
    sys          0.09

* `real` - wall clock or elapsed time
* `user` - amount of time cpu spent on task outside kernel functions
* `sys` - time spent in kernel level functions

To get an idea of the time spent in I/O (waiting for I/O) - subtract the real time from the user and sys cpu time.

    io_wait = real - (user + sys)
    io_wait = 7.4 - (7.22 + 0.09) = 7.4 - 7.31 = 0.09

> Could also indicate the system running other tasks

There is a `--verbose` flag on some `time` implementations

### Using cProfile

> A good practice when profiling is to generate a hypothesis about the speed of parts of your code before you profile it.

    python -m cProfile -s cumulative julia1_nopil.py

Results:

    Length of x: 1000
    Total elements: 1000000
    calculate_z_serial_purepython took 10.79547381401062 seconds
            36221995 function calls in 11.581 seconds

    Ordered by: cumulative time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000   11.581   11.581 {built-in method builtins.exec}
            1    0.030    0.030   11.581   11.581 julia1_nopil.py:1(<module>)
            1    0.619    0.619   11.551   11.551 julia1_nopil.py:23(calc_pure_python)
            1    8.396    8.396   10.795   10.795 julia1_nopil.py:9(calculate_z_serial_purepython)
    34219980    2.400    0.000    2.400    0.000 {built-in method builtins.abs}
    2002000    0.130    0.000    0.130    0.000 {method 'append' of 'list' objects}
            1    0.006    0.006    0.006    0.006 {built-in method builtins.sum}
            3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
            4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
            2    0.000    0.000    0.000    0.000 {built-in method time.time}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Results interpreted:

* 36221995 function calls in 11.581 seconds (can see increase in time from adding profiling - adds 5 seconds)
* `julia1_nopil.py:1` is executed once and takes a total of `11.581` seconds
* The call to `calculate_z_serial_purepython` consumes `8.396` seconds
* `34219980` calls to `abs` take `2.4` seconds
* `lsprof` - is the original name of the tool that became `cProfile`

> Figuring out what is happening on a line-by-line basis is very hard with cProfile, as we get profile information only for the function calls themselves, not for each line within the functions.

### Visualizing cProfile Output with SnakeViz




## Source

* [High Performance Python, 2nd Edition](https://www.oreilly.com/library/view/high-performance-python/9781492055013/)