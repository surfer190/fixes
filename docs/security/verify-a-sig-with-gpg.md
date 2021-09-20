---
author: ''
category: Security
date: '2021-09-15'
summary: ''
title: How to Verify a .sig with PGP on Mac 10.13
---

## How to Verify a .sig with PGP on Mac 10.13

To verify a sig you need to use PGP - Pretty Good Privacy

1. Install [GPG suite for MacOS 10.13](45c5aad48e4cace9d7be8496a33958e435e3272c2d2dd9876bf5610713b6555f) and verify with `sha256sum`
2. Install it
3. Get the key id of the file

    cat imager_1.4.dmg.sig | gpg --list-packets
    
    # off=0 ctb=89 tag=2 hlen=3 plen=307
    :signature packet: algo 1, keyid 8738CD6B956F460C
        version 4, created 1595074651, md5len 0, sigclass 0x00
        digest algo 10, begin of digest cd c1
        hashed subpkt 33 len 21 (issuer fpr v4 54C3DD610D9D1B4AF82A37758738CD6B956F460C)
        hashed subpkt 2 len 4 (sig created 2020-07-18)
        subpkt 16 len 8 (issuer key ID 8738CD6B956F460C)
        data: [2043 bits]

4. Lookup the public key with the key id and import

    gpg --keyserver pgp.mit.edu --recv 8738CD6B956F460C
    
    gpg: key 8738CD6B956F460C: public key "Raspberry Pi Downloads Signing Key" imported
    gpg: Total number processed: 1
    gpg:               imported: 1

5. Verify the signature

    gpg --verify imager_1.4.dmg.sig imager_1.4.dmg
    
    gpg: Signature made Sat Jul 18 14:17:31 2020 SAST
    gpg:                using RSA key 54C3DD610D9D1B4AF82A37758738CD6B956F460C
    gpg: Good signature from "Raspberry Pi Downloads Signing Key" [unknown]
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 54C3 DD61 0D9D 1B4A F82A  3775 8738 CD6B 956F 460C

> I'm not sure this really verifies anything

## Source

* [How to Verify a GPG Signature](https://www.devdungeon.com/content/how-verify-gpg-signature)
* [Signature Key for Raspbian images?](https://www.raspberrypi.org/forums/viewtopic.php?t=187739)
