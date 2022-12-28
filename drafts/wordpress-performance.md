## Comparing PHP-FPM 7.4 vs PHP-FPM 8.1

> No cache

## 8.1

### PHP FPM Settings

pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3
pm.process_idle_timeout = 10

### WRK

    wrk -c 12 -d 1m -t 4 https://test.number1.co.za/
    
    Running 1m test @ https://test.number1.co.za/
    4 threads and 12 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   465.74ms   73.32ms 773.57ms   71.28%
        Req/Sec     7.63      4.17    20.00     77.78%
    1539 requests in 1.00m, 97.29MB read
    Requests/sec:     25.62
    Transfer/sec:      1.62MB
    
    wrk -c 12 -d 1m -t 4 https://test.number1.co.za/how-to-build-python-3-from-source-on-ubuntu-22-04/
    Running 1m test @ https://test.number1.co.za/how-to-build-python-3-from-source-on-ubuntu-22-04/
    4 threads and 12 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   415.89ms  109.98ms   1.25s    85.57%
        Req/Sec     8.71      4.53    20.00     77.80%
    1733 requests in 1.00m, 82.48MB read
    Requests/sec:     28.85
    Transfer/sec:      1.37MB

Load:

* 1 min home page: 4.30
* 1 min post: 4.15

### AB

    ab -n 1000 -c 10 https://test.number1.co.za/how-to-build-python-3-from-source-on-ubuntu-22-04/

    Server Software:        nginx/1.18.0
    Server Hostname:        test.number1.co.za
    Server Port:            443
    SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
    Server Temp Key:        X25519 253 bits
    TLS Server Name:        test.number1.co.za

    Document Path:          /how-to-build-python-3-from-source-on-ubuntu-22-04/
    Document Length:        49416 bytes

    Concurrency Level:      10
    Time taken for tests:   37.843 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      49795000 bytes
    HTML transferred:       49416000 bytes
    Requests per second:    26.43 [#/sec] (mean)
    Time per request:       378.429 [ms] (mean)
    Time per request:       37.843 [ms] (mean, across all concurrent requests)
    Transfer rate:          1284.99 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        5    8   3.3      7      40
    Processing:    84  369  65.2    362     618
    Waiting:       39  298  53.7    292     506
    Total:        116  377  65.3    370     627

    Percentage of the requests served within a certain time (ms)
    50%    370
    66%    395
    75%    413
    80%    425
    90%    461
    95%    493
    98%    537
    99%    573
    100%    627 (longest request)

    ab -n 1000 -c 10 https://test.number1.co.za/
    Server Software:        nginx/1.18.0
    Server Hostname:        test.number1.co.za
    Server Port:            443
    SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
    Server Temp Key:        X25519 253 bits
    TLS Server Name:        test.number1.co.za

    Document Path:          /
    Document Length:        65898 bytes

    Concurrency Level:      10
    Time taken for tests:   45.604 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      66115000 bytes
    HTML transferred:       65898000 bytes
    Requests per second:    21.93 [#/sec] (mean)
    Time per request:       456.042 [ms] (mean)
    Time per request:       45.604 [ms] (mean, across all concurrent requests)
    Transfer rate:          1415.78 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        6    9   4.9      7      54
    Processing:   107  445 116.1    422    1048
    Waiting:       42  338  89.4    320     845
    Total:        127  453 117.5    429    1065

    Percentage of the requests served within a certain time (ms)
    50%    429
    66%    466
    75%    497
    80%    518
    90%    556
    95%    625
    98%    880
    99%    969
    100%   1065 (longest request)

### Locust

## 7.4

### PHP FPM Settings

    pm = dynamic
    pm.max_children = 5
    pm.start_servers = 2
    pm.min_spare_servers = 1
    pm.max_spare_servers = 3
    pm.max_spawn_rate = 32
    pm.process_idle_timeout = 10
    pm.max_requests = 0

### WRK

    wrk -c 12 -d 1m -t 4 https://number1.co.za/
    Running 1m test @ https://number1.co.za/
    4 threads and 12 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   202.57ms   23.21ms 337.88ms   71.37%
        Req/Sec    14.98      5.28    30.00     97.29%
    3549 requests in 1.00m, 224.14MB read
    Requests/sec:     59.11
    Transfer/sec:      3.73MB


    wrk -c 12 -d 1m -t 4 https://number1.co.za/how-to-build-python-3-from-source-on-ubuntu-22-04/
    Running 1m test @ https://number1.co.za/how-to-build-python-3-from-source-on-ubuntu-22-04/
    4 threads and 12 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   175.17ms   20.49ms 243.06ms   68.58%
        Req/Sec    17.27      6.50    30.00     51.96%
    4106 requests in 1.00m, 194.73MB read
    Requests/sec:     68.35
    Transfer/sec:      3.24MB

Load:

* home page: 3.12
* page: 3.63

### AB

    ab -n 1000 -c 10 https://number1.co.za/how-to-build-python-3-from-source-on-ubuntu-22-04/
    
    Server Software:        nginx
    Server Hostname:        number1.co.za
    Server Port:            443
    SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
    Server Temp Key:        ECDH P-256 256 bits
    TLS Server Name:        number1.co.za

    Document Path:          /how-to-build-python-3-from-source-on-ubuntu-22-04/
    Document Length:        49251 bytes

    Concurrency Level:      10
    Time taken for tests:   15.756 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      49622000 bytes
    HTML transferred:       49251000 bytes
    Requests per second:    63.47 [#/sec] (mean)
    Time per request:       157.558 [ms] (mean)
    Time per request:       15.756 [ms] (mean, across all concurrent requests)
    Transfer rate:          3075.63 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        2    2   0.9      2      10
    Processing:    51  155  21.0    156     232
    Waiting:       20  125  17.6    126     191
    Total:         56  157  20.9    158     235

    Percentage of the requests served within a certain time (ms)
    50%    158
    66%    166
    75%    171
    80%    174
    90%    182
    95%    189
    98%    197
    99%    202
    100%    235 (longest request)

    ab -n 1000 -c 10 https://number1.co.za/

    Server Software:        nginx
    Server Hostname:        number1.co.za
    Server Port:            443
    SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
    Server Temp Key:        ECDH P-256 256 bits
    TLS Server Name:        number1.co.za

    Document Path:          /
    Document Length:        65897 bytes

    Concurrency Level:      10
    Time taken for tests:   17.708 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      66116000 bytes
    HTML transferred:       65897000 bytes
    Requests per second:    56.47 [#/sec] (mean)
    Time per request:       177.084 [ms] (mean)
    Time per request:       17.708 [ms] (mean, across all concurrent requests)
    Transfer rate:          3646.09 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        2    2   1.4      2      26
    Processing:    46  174  24.3    176     244
    Waiting:       19  134  19.0    135     190
    Total:         48  176  24.2    178     246

    Percentage of the requests served within a certain time (ms)
    50%    178
    66%    186
    75%    193
    80%    196
    90%    205
    95%    212
    98%    221
    99%    228
    100%    246 (longest request)

### Locust

## Commentary

8.1

Home (wrk): 7.63 RPS at 465.74 ms
Page (wrk): 8.71 RPS at 415.89 ms
Home (ab): 26.43 RPS at 378.43 ms
Page (ab): 21.93 RPS 456.04 ms

7.4

Home (wrk): 14.98 RPS at 202.57 ms
Page (wrk):17.27 RPS at 175.17 ms
Home (ab): 56.47 RPS at 177.08 ms
Page (ab): 63.47 RPS 157.56 ms

> 7.4 is double as fast - something must be different here...

Main difference was 7.4 using nginx/1.20.1 while 8.1 was on nginx/1.18.0.

Changed to nginx/1.22.1

### CPU Core differences

Old server:

    locust --headless --host http://number1.co.za -t 5m -u 10 -r 0.1

    Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
    GET      /                                                                                215     0(0.00%) |     38      33      60     37 |    0.72        0.00
    GET      /?s=green                                                                        200     0(0.00%) |     54      48      84     53 |    0.67        0.00
    GET      /canonical-hiring-process-is-it-worth-it/                                        218     0(0.00%) |     34      30      53     33 |    0.73        0.00
    GET      /helpful-utils/                                                                  216     0(0.00%) |     34      28     414     32 |    0.72        0.00
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
            Aggregated                                                                       849     0(0.00%) |     40      28     414     36 |    2.83        0.00

    Response time percentiles (approximated)
    Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
    GET      /                                                                                      37     38     39     41     45     48     49     52     60     60     60    215
    GET      /?s=green                                                                              53     55     55     57     62     66     72     83     85     85     85    200
    GET      /canonical-hiring-process-is-it-worth-it/                                              33     34     35     36     39     41     45     48     53     53     53    218
    GET      /helpful-utils/                                                                        32     33     34     34     37     41     47     52    410    410    410    216
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
            Aggregated                                                                             36     39     48     51     54     57     64     68    410    410    410    849

New server:

    locust --headless --host http://test.number1.co.za -t 5m -u 10 -r 0.1

    Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
    GET      /                                                                                187     0(0.00%) |    105      72     482     97 |    0.63        0.00
    GET      /?s=green                                                                        210     0(0.00%) |    149     101     875    130 |    0.70        0.00
    GET      /canonical-hiring-process-is-it-worth-it/                                        211     0(0.00%) |    103      61     685     91 |    0.71        0.00
    GET      /helpful-utils/                                                                  218     0(0.00%) |     96      59     497     87 |    0.73        0.00
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
            Aggregated                                                                       826     0(0.00%) |    113      59     875    100 |    2.76        0.00

    Response time percentiles (approximated)
    Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
    GET      /                                                                                      97    110    110    120    130    150    200    360    480    480    480    187
    GET      /?s=green                                                                             130    150    160    160    180    220    310    400    880    880    880    210
    GET      /canonical-hiring-process-is-it-worth-it/                                              91    100    110    120    140    170    240    270    690    690    690    211
    GET      /helpful-utils/                                                                        87     94     99    110    120    140    180    360    500    500    500    218
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
            Aggregated                                                                            100    120    130    130    150    180    240    360    880    880    880    826

> Average response time is 113 ms on the new server and 40ms on the old server.

Old:

    locust --headless --host http://test.number1.co.za -t 1m -u 1 -r 1

    Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
    GET      /                                                                                  2     0(0.00%) |    101      69     133     69 |    0.03        0.00
    GET      /?s=green                                                                          5     0(0.00%) |    115     112     118    118 |    0.09        0.00
    GET      /canonical-hiring-process-is-it-worth-it/                                          6     0(0.00%) |     95      77     128     92 |    0.10        0.00
    GET      /helpful-utils/                                                                    7     0(0.00%) |     77      62      91     83 |    0.12        0.00
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
            Aggregated                                                                        20     0(0.00%) |     94      62     133     91 |    0.34        0.00

    Response time percentiles (approximated)
    Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
    GET      /                                                                                     130    130    130    130    130    130    130    130    130    130    130      2
    GET      /?s=green                                                                             120    120    120    120    120    120    120    120    120    120    120      5
    GET      /canonical-hiring-process-is-it-worth-it/                                              94     94    100    100    130    130    130    130    130    130    130      6
    GET      /helpful-utils/                                                                        83     86     89     89     91     91     91     91     91     91     91      7
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
            Aggregated                                                                             92    110    120    120    130    130    130    130    130    130    130     20

New:

    locust --headless --host http://test.number1.co.za -t 1m -u 1 -r 1
    
        Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
    GET      /                                                                                  6     0(0.00%) |     82      78      86     82 |    0.10        0.00
    GET      /?s=green                                                                          2     0(0.00%) |    278     119     437    120 |    0.03        0.00
    GET      /canonical-hiring-process-is-it-worth-it/                                          8     0(0.00%) |     83      71     113     78 |    0.14        0.00
    GET      /helpful-utils/                                                                    2     0(0.00%) |     85      82      88     82 |    0.03        0.00
    --------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
            Aggregated                                                                        18     0(0.00%) |    105      71     437     82 |    0.31        0.00

    Response time percentiles (approximated)
    Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
    GET      /                                                                                      85     85     85     85     87     87     87     87     87     87     87      6
    GET      /?s=green                                                                             440    440    440    440    440    440    440    440    440    440    440      2
    GET      /canonical-hiring-process-is-it-worth-it/                                              80     91     91     91    110    110    110    110    110    110    110      8
    GET      /helpful-utils/                                                                        89     89     89     89     89     89     89     89     89     89     89      2
    --------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
            Aggregated                                                                             85     87     91     91    120    440    440    440    440    440    440     18

### Nginx Wordpress performance Improvements

[Nginx Wordpress Performance](https://www.nginx.com/blog/9-tips-for-improving-wordpress-performance-with-nginx/)

