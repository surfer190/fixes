---
author: ''
category: Security
date: '2019-08-04'
summary: ''
title: Sha256 Checksum Verification
---
# How to Verify a SHA256 Checksum on Mac OSX

Sometimes you need to verify the file you downloaded is the file you expected, not a file downloaded from a man in the middle on f your network.

Download the file

Can the checksum of the file you downloaded it with:

    shasum -a 256 bitcoin-0.18.0-osx64.tar.gz 

Check that against the release signature given on the website

eg.

    wget https://bitcoin.org/bin/bitcoin-core-0.18.0/SHA256SUMS.asc
    cat SHA256SUMS.asc

## Source

* [SHA256 Checksum Verification](https://www.dyclassroom.com/howto-mac/how-to-verify-checksum-on-a-mac-md5-sha1-sha256-etc)