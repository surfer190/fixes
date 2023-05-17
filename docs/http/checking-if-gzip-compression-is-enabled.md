---
author: ''
category: HTTP
date: '2023-05-02'
summary: ''
title: Check if Gzip is Enabled
---

## Checking if Gzip Compression is Enabled

You need to tell the server than you can accept gzipped content.
That is done with request headers:

### Do not accept Gzip

    $ curl https://fixes.co.za --silent --write-out "%{size_download}\n" --output /dev/null
    312114

### Accept Gzip

    $ curl https://fixes.co.za --silent -H "Accept-Encoding: gzip,deflate" --write-out "%{size_download}\n" --output /dev/null
    53955

## Source

* [How can I tell if my server is serving GZipped content?](https://stackoverflow.com/questions/9140178/how-can-i-tell-if-my-server-is-serving-gzipped-content)
