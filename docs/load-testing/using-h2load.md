---
author: ''
category: Load Testing
date: '2022-06-28'
summary: ''
title: Using h2load
---

## Nghttp2

[NgHttp2](https://nghttp2.org/) is the implementation of HTTP/2 in C.

The [nghttp2 documentation](https://nghttp2.org/documentation/) is very good and the utilities include a [`h2load`](https://nghttp2.org/documentation/h2load.1.html) binary available on the cli.

### Usage

Usage is very similar to that of [Apache Bench ab](./using-apache-bench-ab.md)

    $ h2load -n 10 -c 1 https://fixes.co.za/
    starting benchmark...
    spawning thread #0: 1 total client(s). 10 total requests
    TLS Protocol: TLSv1.2
    Cipher: ECDHE-RSA-AES256-GCM-SHA384
    Server Temp Key: ECDH P-256 256 bits
    Application protocol: h2
    progress: 10% done
    progress: 20% done
    progress: 30% done
    progress: 40% done
    progress: 50% done
    progress: 60% done
    progress: 70% done
    progress: 80% done
    progress: 90% done
    progress: 100% done

    finished in 46.26s, 0.22 req/s, 66.84KB/s
    requests: 10 total, 10 started, 10 done, 10 succeeded, 0 failed, 0 errored, 0 timeout
    status codes: 10 2xx, 0 3xx, 0 4xx, 0 5xx
    traffic: 3.02MB (3166069) total, 1.28KB (1310) headers (space savings 37.32%), 3.01MB (3161110) data
                        min         max         mean         sd        +/- sd
    time for request:      3.37s       6.82s       4.61s       1.30s    80.00%
    time for connect:   207.57ms    207.57ms    207.57ms         0us   100.00%
    time to 1st byte:   447.55ms    447.55ms    447.55ms         0us   100.00%
    req/s           :       0.22        0.22        0.22        0.00   100.00%

It uses HTTP/2 by default but you can force HTTP/1.1 with `--h1`
