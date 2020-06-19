# Concurrency

> Concurrency is simultaneous occurrence

In python they are a sequence of instructions that run in order

Only `multiprocessing` actually runs of the trains of thought at the same time.
`threading` and `asyncio` both run on a single processor and therefore only run one at a time - they find ways to take turns and speed up the overall process.

With `threading` the operating system knows about each thread and can interrupt it at any time to start a different thread - called **pre-emptive multitasking**

With `asyncio` the task must announce when it is ready to be switched out - called **co-operative multitasking** - the benefit is that you know when your task will be swapped out.

With `multiprocessing` python creates new processes - different processes can run on different cores.

> Side note: Threads of the same process run in a shared memory environment, while processes run in a seperate memory space and have at least 1 thread.

## When is concurrency useful

* I/O-bound problems - cause your program to slow down because it frequently must wait for input/output (I/O) from some external resource (file system and network connections). Speeding them up involves overlapping the times spent waiting for these devices
* CPU-bound problems - resource limiting the speed of your program is the CPU, not the network or the file system. Speeding it up involves finding ways to do more computations in the same amount of time.


> Adding concurrency to your program adds extra code and complications, so you’ll need to decide if the potential speed up is worth the extra effort.

Synchronous versions of code is easier to write and debug, it is more straight forward and predictable.

> Being slower isn’t always a big issue, however. If the program you’re running takes only 2 seconds with a synchronous version and is only run rarely, it’s probably not worth adding concurrency. You can stop here.

## IO Synchronous (non-concurrent) version

    import requests
    import time


    def download_site(url, session):
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")


    def download_all_sites(sites):
        with requests.Session() as session:
            for url in sites:
                download_site(url, session)


    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds")


With a synchronous version of IO wait I got:

* `Downloaded 160 in 46.06626296043396 seconds`
* `Downloaded 160 in 45.65080380439758 seconds`

When using threading I got:

* `Downloaded 160 in 9.745933055877686 seconds`
* `Downloaded 160 in 9.325814008712769 seconds`

With 10 workers instead of 5:

* `Downloaded 160 in 5.143216133117676 seconds`
* `Downloaded 160 in 5.229079008102417 seconds`

With 15 workers:

* `Downloaded 160 in 4.0589759349823 seconds`
* `Downloaded 160 in 3.7838428020477295 seconds`

With 20 workers:

* `Downloaded 160 in 3.064251184463501 seconds`
* `Downloaded 160 in 3.208624839782715 seconds`

With 30 workers:

* `Downloaded 160 in 2.629977226257324 seconds`
* `Downloaded 160 in 2.3986380100250244 seconds`

It allows multiple open requests to the website at the same time, allowing your program to overlap the waiting times and get the final result faster.

## Threading version

    import concurrent.futures
    import requests
    import threading
    import time

    thread_local = threading.local()

    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session

    def download_site(url):
        session = get_session()
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_site, sites)

    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds")

You need to use a `ThreadPoolExecutor`. The thread is the train of though, the pool is the pool of threads for the concurrent processes and the `Executor` is the part that’s going to control how and when each of the threads in the pool will run.

You can use the `ThreadPoolExecutor` `.map()` function, which runs the passed in function.

Lower level control of threads like `Thread.start()`, `Thread.join()` and `Queue` are still there, but the `Executor` handles the details for you if you don't need fine grained controls.

Each thread needs to create its own `requests.Session()`. This is one of the interesting and difficult issues with threading because the operating system is in control of when your task gets interrupted and another task starts, any data that is shared between the threads needs to be protected, or thread-safe. Unfortunately `requests.Session()` is not thread-safe.

You can make threads safe by using a thread-safe data structure like a `Queue`. They use `threading.Lock` to ensure that only 1 thread can access a block of code or a bit of memory at the same time.

Another strategy is thread local storage: `Threading.local()`, creating an object specific to each thread.

    threadLocal = threading.local()

    def get_session():
        if not hasattr(threadLocal, "session"):
            threadLocal.session = requests.Session()
        return threadLocal.session

Create one `Threading.local()`, not one for each thread.

You can play around with the number of threads to find what the optimal amount is - this will differ between systems.

The problem with the threading version is it takes more code, more complexity and you have to give thought to what is shared between threads. Threads can work in mysterious ways that are hard to detect.

## AsyncIO

The general concept is that a single python object, called the event loop controls when and how each task is run and knows what state it is in.
For this example lets assume 2 states, the ready state and the waiting state.

A task is started and during that time the task has complete control over that task. When it is done it hands back control to the event loop. The event loop puts the task onto the ready or waiting list.

The tasks are never interrupted, they must give back control. So you don't need to worry about making your code thread safe.

For more details check this [stackoverflow question on asyncio](https://stackoverflow.com/questions/49005651/how-does-asyncio-actually-work/51116910#51116910)

    import asyncio
    import time
    import aiohttp

    async def download_site(session, url):
        async with session.get(url) as response:
            print("Read {0} from {1}".format(response.content_length, url))

    async def download_all_sites(sites):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in sites:
                task = asyncio.ensure_future(download_site(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} sites in {duration} seconds")


### Async and await

* `await` is the keyword used to hand back control to the event loop
* `async` is the keyword to tell python that the function about to be defined uses `await`

> Any function that calls `await` needs to be marked with `async`

> One of the cool advantages of asyncio is that it scales far better than threading. Each task takes far fewer resources and less time to create than a thread, so creating and running more of them works well. This example just creates a separate task for each site to download, which works out quite well.

In python3.7 you can do `asyncio.run()` instead of `asyncio.get_event_loop().run_until_complete()`

Problems with `asyncio`:

* You need special sync versions of libraries to gain the full advantage of `asyncio`
* `requests` is not designed to notify the event loop that it is blocked
* If one task does not cooperate, the advantages of cooperative multitasking get thrown out the window.
* A minor mistake in code can cause a task to run off and hold the processor for a long time, starving other tasks that need running. There is no way for the event loop to break in if a task does not hand control back to it.

## Multiprocessing Version

Up until now all examples of concurrency ran on a single CPU. The reason for this is the design of `cpython` and the `GIL - Global Interpreter Lock`.

`multiprocessing` in the standard library was designed to break down the barrier and let you run your code across multiple CPU's. It does this by creating a new instance of the python interpreter to run on each CPU and then farming out part of your program to run on it.

> Bringing up a separate Python interpreter is not as fast as starting a new thread in the current Python interpreter, it is a heavyweight operation that comes with restrictions.

By default `multiprocessing.Pool()` will determine the number of CPUs in your computer

> For this problem, increasing the number of processes did not make things faster. It actually slowed things down because the cost for setting up and tearing down all those processes was larger than the benefit of doing the I/O requests in parallel.

Each process in our Pool has its own memory space meaning they cannot share things like a `Session` object.

The `initializer` function is used to create one `Session` per process.

    import requests
    import multiprocessing
    import time

    session = None


    def set_global_session():
        global session
        if not session:
            session = requests.Session()

    def download_site(url):
        with session.get(url) as response:
            name = multiprocessing.current_process().name
            print(f"{name}:Read {len(response.content)} from {url}")

    def download_all_sites(sites):
        with multiprocessing.Pool(initializer=set_global_session) as pool:
            pool.map(download_site, sites)

    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds")

Advantages:

* Takes full advantage of the CPU power of your computer

Problems:

* Have to spend time thinking which variables will be accessed in which process
* Slower than threading

First run:

* `Downloaded 160 in 15.047489166259766 seconds`
* `Downloaded 160 in 12.240269899368286 seconds`

> That’s not surprising, as I/O-bound problems are not really why `multiprocessing` exists

## How to Speed up a CPU bound program

In CPU bound problems the overall execution time is a factor of how fast it can process the required data

The synchronous version:

    import time

    def cpu_bound(number):
        return sum(i * i for i in range(number))

    def find_sums(numbers):
        for number in numbers:
            cpu_bound(number)

    if __name__ == "__main__":
        numbers = [5_000_000 + x for x in range(20)]

        start_time = time.time()
        find_sums(numbers)
        duration = time.time() - start_time
        print(f"Duration {duration} seconds")

Results:

* `Duration 10.749261856079102 seconds`
* `Duration 10.40693187713623 seconds`

This is running on a single CPU with no concurrency.

### Threading and Async Versions

The benefits of threading and ayncio are that we can overlap the times we are waiting of IO, instead of doing them sequentially.

On a CPU bound problem however there is no waiting.
The CPU is going as fast as it can. When async or threading are added it is doing more unnecessary work - setting up threads or tasks.

You can see the results here, the non-concurrent version is faster than the one with threading:

Threading: `Duration 11.09269094467163 seconds`
Non-concurrent: `Duration 10.33004903793335 seconds`
Multiprocessing: `Duration 5.9047300815582275 seconds`

### Multiprocessing

> multiprocessing is explicitly designed to share heavy CPU workloads across multiple CPUs

    import multiprocessing
    import time

    def cpu_bound(number):
        return sum(i * i for i in range(number))

    def find_sums(numbers):
        with multiprocessing.Pool() as pool:
            pool.map(cpu_bound, numbers)

    if __name__ == "__main__":
        numbers = [5_000_000 + x for x in range(20)]

        start_time = time.time()
        find_sums(numbers)
        duration = time.time() - start_time
        print(f"Duration {duration} seconds")

Code changes:

* `import multiprocessing`
* change from looping through the numbers to creating a multiprocessing.Pool object and using its .map() method to send individual numbers to worker-processes as they become free
* the multiprocessing.Pool code is built upon building blocks like `Queue` and `Semaphore`

Results for multiprocessing:

* `Duration 6.079997301101685 seconds`
* `Duration 5.983830690383911 seconds`

Advantages of multiprocessing:

* Easy to setup and requires little extra code
* Takes full advantage of CPU power - faster with CPU load

Disadvantages:

* Splitting up processes can be difficult
* Many solutions require communication between processes - adding complexity

## When to Use Concurrency

Concurrency always adds more complexity and often results in hard to find bugs

[Use an atomic message queue](https://www.youtube.com/watch?v=Bv25Dwe84g0) as Raymond Hettinger says.

Hold out on adding concurrency until you have a known performance issue and then determine which type of concurrency you need

Figuring out whether your program is IO-bound or CPU-bound is important.

> CPU-bound problems only really gain from using multiprocessing. threading and asyncio did not help this type of problem at all.

For IO bound problems:

> Use asyncio when you can, threading when you must

## Source

* [Real Python Concurrency](https://realpython.com/python-concurrency/)