# Docker accessing the host network

One thing I have struggled with is having a docker container access the host network.

The documentation about [host networking](https://docs.docker.com/network/host/) and [host networking tutorial](https://docs.docker.com/network/network-tutorial-host/) gives good insight in how to achieve this.

    docker run -d --network host --name my_nginx nginx

I tried the above on my host that already had nginx running, looking at the log it failed with:

    [cent@cent]$ docker logs 132738f47938
    2019/05/29 07:02:23 [emerg] 1#1: bind() to 0.0.0.0:80 failed (98: Address already in use)
    nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
    2019/05/29 07:02:23 [emerg] 1#1: still could not bind()
    nginx: [emerg] still could not bind()

All I wanted to do was to figure out how to access the local machine, but getting a container to stay running is also a struggle.

