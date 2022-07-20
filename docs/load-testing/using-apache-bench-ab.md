---
author: ''
category: Load Testing
date: '2022-06-28'
summary: ''
title: Using Apache Bench
---

I have been using [locustio](https://locust.io/) as my go to load tester.
However, I haven't taken a look at the forefathers - the trusted reliable tech that has been used for many years to a powerful extent that goes ignored by plebs like me.

I am talking about Apache Bench or as the man page says: `ab - Apache HTTP server benchmarking tool`

With IT and web performance - it is always going to be guessing unless you verify and test

As always: Don't trust, verify.

> The nice thing is that `ab` is available by default on macbooks / OSX. If you are on ubuntu you can install it with `sudo apt install apache2-utils `

## Basic Usage of AB

Check the man page for detailed info: `man ab` or check it at [ab online](https://httpd.apache.org/docs/2.4/programs/ab.html)

To make 100 GET requests, 10 at a time to a url:

    ab -n 100 -c 10 https://fixes.co.za/

The response:

    This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking fixes.co.za (be patient).....done

    Server Software:        nginx
    Server Hostname:        fixes.co.za
    Server Port:            443
    SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
    TLS Server Name:        fixes.co.za

    Document Path:          /
    Document Length:        316111 bytes

    Concurrency Level:      10
    Time taken for tests:   6.484 seconds
    Complete requests:      100
    Failed requests:        0
    Total transferred:      31638000 bytes
    HTML transferred:       31611100 bytes
    Requests per second:    15.42 [#/sec] (mean)
    Time per request:       648.440 [ms] (mean)
    Time per request:       64.844 [ms] (mean, across all concurrent requests)
    Transfer rate:          4764.74 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:       99  233  58.9    224     421
    Processing:   166  386  61.3    382     535
    Waiting:       19   68  31.4     61     162
    Total:        392  619  75.6    627     799

    Percentage of the requests served within a certain time (ms)
    50%    627
    66%    642
    75%    654
    80%    662
    90%    694
    95%    767
    98%    789
    99%    799
    100%    799 (longest request)

We can analyse the results:

* Server software: `nginx` (sometimes this is cloudflare)
* `648.440ms` is the mean time per request
* Requests per second: `15.42 RPS`
    > Requests per second - This is the number of requests per second. This value is the result of dividing the number of requests by the total time taken
* Connect: average at `233ms` The amount of time it took to establish the connection (network latency)
* Processing time: average at `386ms` the time it took for the server to process the request
* Waiting time: average at `68ms` the time to get the first bits of the response

The important part of things you can actually control is in the `processing` part - in most cases. The networking and how fast a packet is received and sent. The HTTP protocol and underlying protocols can somewhat be controlled by enabling HTTP2 and HTTP3.

Make sure you are not testing the network instead of your website:

> There's a cheap, "optimal" solution available on every single computer. It offers the best available bandwidth and latency your web server, OS and CPU can provide (if properly configured). It's called `localhost`. 

The TCP stack also needs to be warmed up - due to TCP congestion control - which starts a connection be sending a small amount of data and then increases over time to prevent congestion. Check the [additive increase/multiplicative decrease (AIMD) alogoritm](https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease) if you are interested.

If I run this ab on the server or datacenter I am in I get the following results:

    Server Software:        nginx
    Server Hostname:        fixes.co.za
    Server Port:            443
    SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
    TLS Server Name:        fixes.co.za

    Document Path:          /
    Document Length:        316111 bytes

    Concurrency Level:      10
    Time taken for tests:   0.577 seconds
    Complete requests:      100
    Failed requests:        0
    Total transferred:      31638000 bytes
    HTML transferred:       31611100 bytes
    Requests per second:    173.25 [#/sec] (mean)
    Time per request:       57.719 [ms] (mean)
    Time per request:       5.772 [ms] (mean, across all concurrent requests)
    Transfer rate:          53529.05 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        6   11   2.6     10      19
    Processing:    11   46   7.3     47      57
    Waiting:        2    6   2.7      5      17
    Total:         21   57   8.4     58      70

    Percentage of the requests served within a certain time (ms)
    50%     58
    66%     60
    75%     62
    80%     64
    90%     66
    95%     68
    98%     70
    99%     70
    100%     70 (longest request)

> This is quite incredible - the processing time on average just to get a html file and display it is `46ms`. The other connection and waiting time is `17ms`.

If there was more processing done to generate the html instead of a static html file - by a python webserver gateway (web server gateway interface) or a php cgi (common gateway interface) - the time would be slower.

If you want a like for like benchmark - then using `ab` running on the actual server will let us compare the exact differences without networking interfering with the results.

## The Process

After you have the basic test conditions - you can see how your web resource responds to an increase in load.
Try and find the common scenario of how many visitors or concurrent visitors you will have. Then find the likely maximum.

Then increase the number of requests and concurrent users - and monitor the server to find where the bottleneck is. Is it CPU, RAM or I/O like network or filesystem storage.
Can caching be leveraged to reduce the load?

> Important to note is the context. Every application has a different context and that might mean that generic performance tests are not good enough for you to choose. It is better to test and profile yourself.

Also ask yourself what you want to test.
IF you want to test the end-to-end user experience from a certain geographical location - or do you only want to look at what each component did and time spent in that component. Like networking, dns, tls negotiation, web server, python (or other programming language), database etc.

## Other Load Testing Tools

* [Locustio](https://locust.io/) - Python based load testing tool
* [JMeter](https://jmeter.apache.org/) - Java Load Testing
* [h2load](https://nghttp2.org/documentation/h2load.1.html)
* gatling.io
* k6.io

## Sources

* [Using Apache Bench for simple load testing ](https://vyspiansky.github.io/2019/12/02/apache-bench-for-load-testing/)
* [ab definitions of connect, processing and waiting](https://stackoverflow.com/questions/2820306/definition-of-connect-processing-waiting-in-apache-bench)
* [Gwan Benchmarking](http://gwan.com/en_apachebench_httperf.html)
* [TCP Slow Start Problem](https://sirupsen.com/napkin/problem-15)
* [SQLite of Postgresql](https://www.twilio.com/blog/sqlite-postgresql-complicated)