Old server with https:

    staging@web:/etc/nginx/conf.d$ wrk -c 4 -d 30s -t 4 https://fixes.co.za/nginx/nginx-cookbook/
    Running 30s test @ https://fixes.co.za/nginx/nginx-cookbook/
    4 threads and 4 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    10.63ms    3.49ms  34.18ms   60.98%
        Req/Sec    94.20     36.65   220.00     88.33%
    11296 requests in 30.05s, 2.41GB read
    Requests/sec:    375.87
    Transfer/sec:     82.03MB

New server no https:

    ubuntu@web:/etc/nginx/conf.d$ wrk -c 4 -d 30s -t 4 http://fixes.co.za/nginx/nginx-cookbook/
    Running 30s test @ http://fixes.co.za/nginx/nginx-cookbook/
    4 threads and 4 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     1.42ms    1.66ms  26.26ms   94.01%
        Req/Sec     0.87k   323.84     2.68k    74.75%
    104027 requests in 30.03s, 22.21GB read
    Requests/sec:   3464.35
    Transfer/sec:    757.41MB

New server with https (gzip disabled and tcp+no_delay disabled):

    ubuntu@web:/etc/nginx/conf.d$ wrk -c 4 -d 30s -t 4 https://fixes.co.za/nginx/nginx-cookbook/
    Running 30s test @ https://fixes.co.za/nginx/nginx-cookbook/
    4 threads and 4 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     4.75ms    2.58ms  29.22ms   76.27%
        Req/Sec   218.92     81.98   690.00     76.58%
    26196 requests in 30.04s, 5.59GB read
    Requests/sec:    871.92
    Transfer/sec:    190.64MB

After enabling gzip and tcp_no_delay:

    wrk -c 4 -d 30s -t 4 https://fixes.co.za/nginx/nginx-cookbook/
    Running 30s test @ https://fixes.co.za/nginx/nginx-cookbook/
    4 threads and 4 connections
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     4.22ms    2.07ms  21.49ms   74.49%
        Req/Sec   242.40     88.15   710.00     74.83%
    29016 requests in 30.07s, 6.20GB read
    Requests/sec:    965.09
    Transfer/sec:    211.00MB

> interesting

Nginx shows horrendous results...however `top` revealed that the cpu was not at 100%.

So is `io` the bottleneck?

Let us monitor io by installing `sysstat` and `iotop`.

    iostat -x 1

or:

    iotop

Nginx did not have `gzip` enabled.

When it was enabled it ran very well.

### Sources

* [Stackoverflow: How can I monitor disk io?](https://unix.stackexchange.com/questions/55212/how-can-i-monitor-disk-io)
