---
author: ''
category: Security
date: '2020-06-23'
summary: ''
title: Openssl Cookbook
---
# OpenSSL Cookbook Notes and Summaries

One of the most important open source projects. It is widely used and a large portion of internet infrastrcuture relies on it.

Project contents:

* Key cryptographic algorithms
* Complete TLS and PKI Stack
* Command line toolkit

If you are in IT security, web development and system administration it is an unavoidable tool.

> OpenSSL, which is not very well documented; what you can find on the Internet is often wrong and outdated

## 1. OpenSSL

Consists of:

* Cryptographic library
* TLS Toolkit

Licensing of OpenSSL is a mess and `GnutLS` is favoured.

### Getting Started

#### OpenSSL Versions

On macOS:

    $ openssl version
    LibreSSL 2.2.7

On ubuntu:

    $ openssl version
    OpenSSL 1.1.1f  31 Mar 2020

On debian:

    $ openssl version
    OpenSSL 1.1.1g  21 Apr 2020

You can get more information with:

    openssl version -a

    OpenSSL 1.1.1g  21 Apr 2020
    built on: Tue Apr 21 14:33:04 2020 UTC
    platform: debian-amd64
    options:  bn(64,64) rc4(16x,int) des(int) blowfish(ptr) 
    compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -Wa,--noexecstack -g -O2 -fdebug-prefix-map=/build/openssl-RvYbbo/openssl-1.1.1g=. -specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector-strong -Wformat -Werror=format-security -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_CPUID_OBJ -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DKECCAK1600_ASM -DRC4_ASM -DMD5_ASM -DAESNI_ASM -DVPAES_ASM -DGHASH_ASM -DECP_NISTZ256_ASM -DX25519_ASM -DPOLY1305_ASM -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=2
    OPENSSLDIR: "/usr/lib/ssl"
    ENGINESDIR: "/usr/lib/x86_64-linux-gnu/engines-1.1"
    Seeding source: os-specific

The `OPENSSLDIR` tells you where OpenSSL will look for configuration.

`/usr/lib/ssl` is usually an alias for `/etc/ssl`

    lrwxrwxrwx  1 root root   14 Apr 24  2019 certs -> /etc/ssl/certs
    drwxr-xr-x  2 root root 4096 May  8 19:21 misc
    lrwxrwxrwx  1 root root   20 Apr 21 16:33 openssl.cnf -> /etc/ssl/openssl.cnf
    lrwxrwxrwx  1 root root   16 Apr 24  2019 private -> /etc/ssl/private

The `misc` folder is for scripts allowing for the implementation of a private CA (_certificate authority_)

#### Building from Source

Sometimes to get a recent version you need to install from source

Releases can be pulled from: https://github.com/openssl/openssl/releases

    cd /opt
    wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz
    wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz.sha256
    
    sha256sum openssl-1.1.1g.tar.gz
    # output should equal contents of openssl-1.1.1g.tar.gz.sha256

You can install it in a different location:

    sudo tar xf openssl-1.1.1g.tar.gz
    cd openssl-1.1.1g
    
    sudo ./config --prefix=/opt/openssl --openssldir=/opt/openssl enable-ec_nistp_64_gcc_128

    make depend
    make
    sudo make install

The contents of `/opt/openssl`:

    drwxr-xr-x 9 root root  4096 Jun 11 09:06 .
    drwxr-xr-x 5 root root  4096 Jun 11 09:06 ..
    drwxr-xr-x 2 root root  4096 Jun 11 09:06 bin
    drwxr-xr-x 2 root root  4096 Jun 11 09:06 certs
    -rw-r--r-- 1 root root   412 Jun 11 09:06 ct_log_list.cnf
    -rw-r--r-- 1 root root   412 Jun 11 09:06 ct_log_list.cnf.dist
    drwxr-xr-x 3 root root  4096 Jun 11 09:06 include
    drwxr-xr-x 4 root root  4096 Jun 11 09:06 lib
    drwxr-xr-x 2 root root  4096 Jun 11 09:06 misc
    -rw-r--r-- 1 root root 10909 Jun 11 09:06 openssl.cnf
    -rw-r--r-- 1 root root 10909 Jun 11 09:06 openssl.cnf.dist
    drwxr-xr-x 2 root root  4096 Jun 11 09:06 private
    drwxr-xr-x 4 root root  4096 Jun 11 09:07 share

The `/private` folder is empty - as you do not have any private keys.

The `/certs` folder is also empty - OpenSSL does not include any root certificates - mainting trust stores is outside the scope of the project.

Luckily your operating system usually comes with a trust store. I think they are in `cd /etc/ssl/certs/`.
You can also build your own trust store.

### OpenSSL Available Commands

It is the swiss army knife of cryptography. 

Typing `openssl help` you get some info

    Standard commands
    asn1parse         ca                ciphers           cms               
    crl               crl2pkcs7         dgst              dh                
    dhparam           dsa               dsaparam          ec                
    ecparam           enc               engine            errstr            
    gendh             gendsa            genpkey           genrsa            
    nseq              ocsp              passwd            pkcs12            
    pkcs7             pkcs8             pkey              pkeyparam         
    pkeyutl           prime             rand              req               
    rsa               rsautl            s_client          s_server          
    s_time            sess_id           smime             speed             
    spkac             srp               ts                verify            
    version           x509    

To get info on the above just write: `man openssl <command>`

Also output is the message digest commands:

    Message Digest commands (see the `dgst' command for more details)
    md4               md5               rmd160            sha               
    sha1  

and cipher commands:

    Cipher commands (see the `enc' command for more details)
    aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb       
    aes-256-cbc       aes-256-ecb       base64            bf                
    bf-cbc            bf-cfb            bf-ecb            bf-ofb            
    camellia-128-cbc  camellia-128-ecb  camellia-192-cbc  camellia-192-ecb  
    camellia-256-cbc  camellia-256-ecb  cast              cast-cbc          
    cast5-cbc         cast5-cfb         cast5-ecb         cast5-ofb         
    des               des-cbc           des-cfb           des-ecb           
    des-ede           des-ede-cbc       des-ede-cfb       des-ede-ofb       
    des-ede3          des-ede3-cbc      des-ede3-cfb      des-ede3-ofb      
    des-ofb           des3              desx              rc2               
    rc2-40-cbc        rc2-64-cbc        rc2-cbc           rc2-cfb           
    rc2-ecb           rc2-ofb           rc4               rc4-40            
    seed              seed-cbc          seed-cfb          seed-ecb          
    seed-ofb 

### Building a Trust Store

OpenSSL does not come with a _trust store_, trusted root certificates.

You can rely on the outdated trust store of your operating system or something like mozilla.
Check this link [https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/)

[mozzila certs](https://hg.mozilla.org/releases/mozilla-beta/file/tip/security/nss/lib/ckfw/builtins/certdata.txt), unfortunately it is in a kak proprietary format.

You can get it in a PEM (Privacy Enhanced Mail) format at: [https://curl.haxx.se/docs/caextract.html](https://curl.haxx.se/docs/caextract.html)

### Key and Certificate Management

Most users have a webserver they want to use to support SSL

Steps:

1. Generate a strong private key
2. Create a certificate signing request (CSR)
3. Install the CA provided certificate in your webserver

#### Key Generation

Ask yourself?

* Key algorithm - RSA, DSA and ECDSA
* Key size - 256bit for ECDSA and 2048 and above for RSA
* Passphrase - optional - convenience vs security

To generate a key:

    openssl genrsa -aes128 -out fd.key 2048

The private keys are stored in a PEM format:

    -----BEGIN RSA PRIVATE KEY-----
    Proc-Type: 4,ENCRYPTED
    DEK-Info: AES-256-CBC,EA701D65440153BF0C560E351D781E77

    eCvKLIkv9PcFsfBrGCoqGiqUp96Mgdgw1IVKPt05iJlfJN2DBhrZGpzQyUZe8kY3
    sPiWxAxrWpdWAEx7LtexLktKEqClVSLLFSWYp5ThkbRFQPiV5YPxCRs2NcvPq8Ng
    6k+rZUEBDnHX4PLFojnNB9TlTkTHVx6NPQcYoPLuTr+yqZvTRFMvHBHccyMbQEVE
    ...
    -----END RSA PRIVATE KEY-----

View the key's structure:

    openssl rsa -text -in fd.key

To get the public key seperately:

    openssl rsa -in fd.key -pubout -out fd-public.key

Contents of the public key:

    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyxw6YklR4eWw5qS/9Dj+
    DRCr9s+ePL9qyiOiEb/2e9wxV0K+OjBkHucw//wzjCE0fJCN2Dduvicgnko9bvon
    mnVGC0uOOMnmAa0vTwPQl7p7l3RnZtuIhQXQ1j1vTqaH6Z028J78QQu6dUCD928x
    U4LFH5P/JzxqKnmJb3wI6RnhWzxL0ri3Sp2HzR3E+q/meW+mQAdzi8MqZXQCvDaT
    DiQwNjmeF8qAfjJqCpKQcfZnkBw3MAucQgiVXpOq2vSeBSCmqrtswaxI+7hgYz+V
    00NN8gc+WR+gMNYgj/myaaCCOJBZouOC9ka6ZdivviJhdwlQ62cPu19hZig1l1k3
    6QIDAQAB
    -----END PUBLIC KEY-----

> Important to use the correct command, if you didn't specify `-pubout` the output would be the private key

Generate a ECDSA key:

    openssl ecparam -genkey -name secp256r1 | openssl ec -out ec.key -aes128

You can also use the `genpkey` command:

    openssl genpkey

#### Creating Certificate Signing Requests

Once you have a private key, you can create a CSR.

A formal request asking a CA to sign a certificate, contains a public key from the entity requesting the certificate and some information about the entity.

    openssl req -new -key fd.key -out fd.csr

It will ask some info about the company

    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [AU]:ZA
    State or Province Name (full name) [Some-State]:Gauteng
    Locality Name (eg, city) []:Johannesburg
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Fixes.co.za
    Organizational Unit Name (eg, section) []:
    Common Name (e.g. server FQDN or YOUR name) []:fixes.co.za
    Email Address []:example@fixes.co.za

> _challenge password_ is used for certificate revocation

After a CSR is generated, use it to sign your own certificate or send it to a public CA asking them to sign your certificate.

Double check that the CSR is correct:

    openssl req -text -in fd.csr -noout

    Certificate Request:
    Data:
        Version: 0 (0x0)
        Subject: C=ZA, ST=Gauteng, L=Johannesburg, O=Fixes.co.za, CN=fixes.co.za/emailAddress=example@fixes.co.za
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
    ...

Create a new CSR from an existing certificate (Renew)

    openssl x509 -x509toreq -in fd.crt -out fd.csr -signkey fd.key

You can create a config file for the csr.

#### Signing your own Certificates

If you are installing a TLS server for your own use, you don't need a go to a CA for a publicly trusted certificate.
It is much easier to sign your own - by generating a self signed certificate.

If you are on firefox on your first visit you can add a certificate exception, after which the site will be secure as if it were protected by a publicy trusted certificate.

> There is an illusion that self signed certificates are not secure and that only publicly trusted certs are. It is a myth. A self-signed certificate is as secure as one signed by a root CA...the only difference is it is not trusted by default via certificate chain and a root CA.

Create a cert from a CSR:

    openssl x509 -req -days 365 -in fd.csr -signkey fd.key -out fd.crt

You don't have to create a CSR in a seperate step, this command does it with the key alone:

    openssl req -new -x509 -days 365 -key fd.key -out fd.crt

#### Creating Certs Valid for Multiple Hostnames

By default certs have 1 common name and are valid for one hostname.

**More info in the book**

#### Examining Certificates

use the `x509` command to get info

    openssl x509 -text -in fd.crt -noout

    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number: 17080102344465494832 (0xed08b696892eb330)
        Signature Algorithm: sha256WithRSAEncryption
            Issuer: C=ZA, ST=Gauteng, L=Joburg, O=Fixes.co.za, CN=fixes.co.za/emailAddress=example@fixes.co.za
            Validity
                Not Before: Jun 11 10:58:51 2020 GMT
                Not After : Jun 11 10:58:51 2021 GMT
            Subject: C=ZA, ST=Gauteng, L=Joburg, O=Fixes.co.za, CN=fixes.co.za/emailAddress=example@fixes.co.za
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    Public-Key: (2048 bit)
                    Modulus:
                        ...
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                X509v3 Subject Key Identifier: 
                    F8:9B:A5:BF:5C:D0:D0:EB:86:8A:90:AD:70:6D:20:12:E2:E8:6E:27
                X509v3 Authority Key Identifier: 
                    keyid:F8:9B:A5:BF:5C:D0:D0:EB:86:8A:90:AD:70:6D:20:12:E2:E8:6E:27

                X509v3 Basic Constraints: 
                    CA:TRUE
        Signature Algorithm: sha256WithRSAEncryption
            ...

Now lets get the certificate from `outlook.office.com`

    openssl s_client -connect outlook.office.com:443 > outlook.crt
    # remove the other stuff and leave the certificate

    openssl x509 -text -in outlook.crt -noout
    
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                06:54:f8:4b:63:25:59:5a:20:bc:68:a6:a5:85:1c:bb
        Signature Algorithm: sha256WithRSAEncryption
            Issuer: C=US, O=DigiCert Inc, CN=DigiCert Cloud Services CA-1
            Validity
                Not Before: Feb 25 00:00:00 2020 GMT
                Not After : Feb 25 12:00:00 2022 GMT
            Subject: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=outlook.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    Public-Key: (2048 bit)
                    Modulus:
                        ...
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                X509v3 Authority Key Identifier: 
                    keyid:DD:51:D0:A2:31:73:A9:73:AE:8F:B4:01:7E:5D:8C:57:CB:9F:F0:F7

                X509v3 Subject Key Identifier: 
                    9E:D8:AF:8C:CC:35:67:F3:68:E9:6B:92:05:CC:FD:34:F4:07:95:63
                X509v3 Subject Alternative Name: 
                    DNS:*.clo.footprintdns.com, DNS:*.hotmail.com, DNS:*.internal.outlook.com, DNS:*.live.com, DNS:*.nrb.footprintdns.com, DNS:*.office.com, DNS:*.office365.com, DNS:*.outlook.com, DNS:*.outlook.office365.com, DNS:attachment.outlook.live.net, DNS:attachment.outlook.office.net, DNS:attachment.outlook.officeppe.net, DNS:attachments.office.net, DNS:attachments-sdf.office.net, DNS:ccs.login.microsoftonline.com, DNS:ccs-sdf.login.microsoftonline.com, DNS:hotmail.com, DNS:mail.services.live.com, DNS:office365.com, DNS:outlook.com, DNS:outlook.office.com, DNS:substrate.office.com, DNS:substrate-sdf.office.com
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment
                X509v3 Extended Key Usage: 
                    TLS Web Server Authentication, TLS Web Client Authentication
                X509v3 CRL Distribution Points: 

                    Full Name:
                    URI:http://crl3.digicert.com/DigiCertCloudServicesCA-1-g1.crl

                    Full Name:
                    URI:http://crl4.digicert.com/DigiCertCloudServicesCA-1-g1.crl

                X509v3 Certificate Policies: 
                    Policy: 2.16.840.1.114412.1.1
                    CPS: https://www.digicert.com/CPS
                    Policy: 2.23.140.1.2.2

                Authority Information Access: 
                    OCSP - URI:http://ocspx.digicert.com
                    CA Issuers - URI:http://cacerts.digicert.com/DigiCertCloudServicesCA-1.crt

                X509v3 Basic Constraints: critical
                    CA:FALSE
                CT Precertificate SCTs: 
                    Signed Certificate Timestamp:
                        Version   : v1(0)
                        Log ID    : ...
                        Timestamp : Feb 25 21:17:59.486 2020 GMT
                        Extensions: none
                        Signature : ecdsa-with-SHA256
                                    ...
                    Signed Certificate Timestamp:
                        Version   : v1(0)
                        Log ID    : ...
                        Timestamp : Feb 25 21:17:59.458 2020 GMT
                        Extensions: none
                        Signature : ecdsa-with-SHA256
                                    ...
                    Signed Certificate Timestamp:
                        Version   : v1(0)
                        Log ID    : ...
                        Timestamp : Feb 25 21:17:59.503 2020 GMT
                        Extensions: none
                        Signature : ecdsa-with-SHA256
                                    ...
        Signature Algorithm: sha256WithRSAEncryption
            ...

`Basic Constraints` mark a certificate as belonging to a CA - giving them the ability to sign other certificates.
Non-CA certificates have this omitted or set as false.

    X509v3 Basic Constraints: critical
    CA:FALSE

`Key Usage` and `Extended Key Usage` restrict what a certificate can be used for.

    X509v3 Key Usage: critical
        Digital Signature, Key Encipherment
    X509v3 Extended Key Usage: 
        TLS Web Server Authentication, TLS Web Client Authentication

> A web server will not allow for code signing

`CRL Distribution Points` lists where the certificates `Certificate Revocation List` info can be found.
Important when certificates need to be revoked.

    X509v3 CRL Distribution Points: 

        Full Name:
        URI:http://crl3.digicert.com/DigiCertCloudServicesCA-1-g1.crl

        Full Name:
        URI:http://crl4.digicert.com/DigiCertCloudServicesCA-1-g1.crl

> Each CRL is signed by the CA that issued it. If they were distributed over TLS browsers might face chicken or egg problem.

`Certificate Policies` indicate the policy under which the cert was issued

    X509v3 Certificate Policies: 
        Policy: 2.16.840.1.114412.1.1
        CPS: https://www.digicert.com/CPS
        Policy: 2.23.140.1.2.2

`Authority Information Access` gives the `Online Certificate Status Protocol (OCSP)` to check for certificate revocation in real time. May also contain a link to the next issuers certificate is found.

> These days, server certificates are rarely signed directly by trusted root certificates, which means that users must include one or more intermediate certificates in their configuration

> Mistakes are easy to make and will invalidate the certificates. Some clients (e.g., Internet Explorer) will use the information provided in this extension to fix an incomplete certificate chain, but many clients won’t.

    Authority Information Access: 
        OCSP - URI:http://ocspx.digicert.com
        CA Issuers - URI:http://cacerts.digicert.com/DigiCertCloudServicesCA-1.crt

`Subject Alternative Name` identifies all the hostnames for which the certificate is valid, if this does not exist it falls back to the `CN` - `Common Name`

#### Key and Certificate Conversion

Private keys can be stored in a variety of formats:

* Binary (DER) Certificate: `x.509` in its raw form
* Ascii (PEM) Certificate: `base64`  encoded DER with `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`. Usually with one certificate per file.
* Binary (DER) Key: Private key in raw form
* Ascii (PEM) key: `base64` DER key
* `PKCS#7` certificates: complex format designed for transport of signed or encrypted data. Has `.p7b` or `.p7c` extensions and can inclue the entire certificate chain.
* `PKCS#12` (PFX) key and certificate: complex format can store and protect key along wit entire certificate chain. `.p12` or `.pfx` extensions. Common on microsoft.

#### PEM and DER conversions

Convert from pem to der

    openssl x509 -inform PEM -in fd.pem -outform DER -out fd.der

Convert from der to pem

    openssl x509 -inform DER -in fd.der -outform PEM -out fd.pem

**More in the book on other conversions**

### Configuration

* Choosing a cipher suite
* performance measurement of crypto operations

#### Choosing a Cipher Suite

A common task on TLS web servers.

In apache, cipher strength may look like this:

    SSLHonorCipherOrder On
    SSLCipherSuite "HIGH:!aNULL:@STRENGTH"

Get a list of supported ciphers:

    openssl ciphers -v 'ALL:COMPLIMENTOFALL'

    ECDHE-ECDSA-CHACHA20-POLY1305 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=ChaCha20-Poly1305 Mac=AEAD
    ECDHE-RSA-CHACHA20-POLY1305 TLSv1.2 Kx=ECDH     Au=RSA  Enc=ChaCha20-Poly1305 Mac=AEAD
    DHE-RSA-CHACHA20-POLY1305 TLSv1.2 Kx=DH       Au=RSA  Enc=ChaCha20-Poly1305 Mac=AEAD
    ECDHE-RSA-AES256-GCM-SHA384 TLSv1.2 Kx=ECDH     Au=RSA  Enc=AESGCM(256) Mac=AEAD
    ECDHE-ECDSA-AES256-GCM-SHA384 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=AESGCM(256) Mac=AEAD
    ECDHE-RSA-AES256-SHA384 TLSv1.2 Kx=ECDH     Au=RSA  Enc=AES(256)  Mac=SHA384
    ECDHE-ECDSA-AES256-SHA384 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=AES(256)  Mac=SHA384
    ...

Output contains: `suite name`, `required minimum protocol version`, `key-exchange algorithm`, `Authentication Algorithm`, `Cipher Algorithm and Strength` and `MAC algorithm`

The order you place the algorithms in is important.

You can select algorithms using different criteriaL

    openssl ciphers -v HIGH

Sorting by `@STRENGTH`:

    openssl ciphers -v HIGH@STRENGTH
    
**More info on the various keywords in the book**

### Putting it all together

* Use only strong ciphers 128-bits and up
* Use only suites that provide strong authnetication
* Do not use suites relying on weak primitives (MD5)
* Prefer ECDSA over RSA

Recommended:

    ECDHE-ECDSA-AES128-GCM-SHA256
    ECDHE-ECDSA-AES256-GCM-SHA384
    ECDHE-ECDSA-AES128-SHA
    ECDHE-ECDSA-AES256-SHA
    ECDHE-ECDSA-AES128-SHA256
    ECDHE-ECDSA-AES256-SHA384
    ECDHE-RSA-AES128-GCM-SHA256
    ECDHE-RSA-AES256-GCM-SHA384
    ECDHE-RSA-AES128-SHA
    ECDHE-RSA-AES256-SHA
    ECDHE-RSA-AES128-SHA256
    ECDHE-RSA-AES256-SHA384
    DHE-RSA-AES128-GCM-SHA256
    DHE-RSA-AES256-GCM-SHA384
    DHE-RSA-AES128-SHA
    DHE-RSA-AES256-SHA
    DHE-RSA-AES128-SHA256
    DHE-RSA-AES256-SHA256
    EDH-RSA-DES-CBC3-SHA

## Performance

OpenSSL has built in benchmarking

Test algorithms:

    openssl speed rc4 aes rsa ecdh sha

                        sign    verify    sign/s    verify/s
        rsa  512 bits 0.000696s 0.000040s   1437.6   25296.0
        rsa 1024 bits 0.004225s 0.000200s    236.7   4996.5
        rsa 2048 bits 0.028837s 0.000822s     34.7   1215.9
        rsa 4096 bits 0.196471s 0.003028s      5.1    330.2
                                    op      op/s
        160 bit ecdh (secp160r1)   0.0012s    844.2
        192 bit ecdh (nistp192)   0.0011s    923.3
        224 bit ecdh (nistp224)   0.0016s    633.7
        256 bit ecdh (nistp256)   0.0020s    507.0
        384 bit ecdh (nistp384)   0.0051s    196.9
        521 bit ecdh (nistp521)   0.0114s     87.8
        163 bit ecdh (nistk163)   0.0010s   1008.0
        233 bit ecdh (nistk233)   0.0014s    725.0
        283 bit ecdh (nistk283)   0.0031s    327.0
        409 bit ecdh (nistk409)   0.0065s    153.2
        571 bit ecdh (nistk571)   0.0143s     70.0
        163 bit ecdh (nistb163)   0.0011s    932.3
        233 bit ecdh (nistb233)   0.0015s    683.8
        283 bit ecdh (nistb283)   0.0034s    297.4
        409 bit ecdh (nistb409)   0.0072s    138.5
        571 bit ecdh (nistb571)   0.0162s     61.6

It is good because you can upgrade to newer `openssl` versions and then see a speed enchancement

> By default, the `speed` command uses only a single process - to use mutliple cores use the `-multi` switch

    openssl speed -multi 4 rsa

                         sign    verify    sign/s verify/s
        rsa  512 bits 0.000260s 0.000018s   3844.5  54424.3
        rsa 1024 bits 0.001450s 0.000072s    689.5  13889.0
        rsa 2048 bits 0.009740s 0.000274s    102.7   3652.1
        rsa 4096 bits 0.066480s 0.000996s     15.0   1004.1

The performance is 4 times better than before.

The results show that `102.7` 2048-bit signatures - meaning 100 brand new TLS connections per second.

So when you get to servers with high load, TLS connnections performance may become a bottleneck.

Sometimes the speed command is wrong as it does not use the fastest implementation making use of native instructions on the CPU: `AES-NI`

### Creating a Private Certificate Authority

* All you need for your own CA is included in `openssl`
* Interface is purely command-line, so not user friendly
* Much better to use a private CA in a development environment than to use self-signed certificates everywhere
* Client certificates can also increase the security
* Biggest challenge with a private CA is keeping the infrastructure secure
* The `root` key must be kept offline because all security depends on it
* CRL's and OCSP responder certificate's must be refreshed on a regular basis

#### Features and Limitations

* One root CA that is similar in structure to which other subordinate CA's can be created
* The `root CA` should remain offline
* Subordinate CA will be technically constrained - it is allowed to issue certificates only for allowed hostnames

After setup the `root certificate` will have to be securely distributed to intended clients.
Once the root is in place you can issue client and server certificates.

Creating a root CA:

1. Root CA Configuration
2. Directory structure and intialisation of key files
3. generating the root key and certificate

> All certificates will be CA's according to the `basicConstraints`
`nameConstriants` limits the allowed hostnames - keeping it safe so they can't issue arbirary hostnames.

##### Root CA Configuration

    man config

* You can choose to make the root certificate valid for 10 years

    man ca
    
**Info in the book about setting up the config**

##### Root CA Directory Structure

    mkdir root-ca
    cd root-ca
    mkdir certs db private
    chmod 700 private
    touch db/index
    openssl rand -hex 16  > db/serial
    echo 1001 > db/crlnumber

* `certs/` - Certificate storage
* `db/` - certificate db (index) and files that hold the next certificate and CRL
* `private/` - stores private keys - one for the CA and one for the OCSP responder. Important that no other user has access to it.

##### Root CA generation

Example `root_ca.conf`:

    # Simple Root CA

    # The [default] section contains global constants that can be referred to from
    # the entire configuration file. It may also hold settings pertaining to more
    # than one openssl command.

    [ default ]
    ca                      = root-ca               # CA name
    dir                     = .                     # Top dir

    # The next part of the configuration file is used by the openssl req command.
    # It defines the CA's key pair, its DN, and the desired extensions for the CA
    # certificate.

    [ req ]
    default_bits            = 2048                  # RSA key size
    encrypt_key             = yes                   # Protect private key
    default_md              = sha1                  # MD to use
    utf8                    = yes                   # Input is UTF-8
    string_mask             = utf8only              # Emit UTF-8 strings
    prompt                  = no                    # Don't prompt for DN
    distinguished_name      = ca_dn                 # DN section
    req_extensions          = ca_reqext             # Desired extensions

    [ ca_dn ]
    0.domainComponent       = "org"
    1.domainComponent       = "simple"
    organizationName        = "Simple Inc"
    organizationalUnitName  = "Simple Root CA"
    commonName              = "Simple Root CA"

    [ ca_reqext ]
    keyUsage                = critical,keyCertSign,cRLSign
    basicConstraints        = critical,CA:true
    subjectKeyIdentifier    = hash

    # The remainder of the configuration file is used by the openssl ca command.
    # The CA section defines the locations of CA assets, as well as the policies
    # applying to the CA.

    [ ca ]
    default_ca              = root_ca               # The default CA section

    [ root_ca ]
    certificate             = $dir/ca/$ca.crt       # The CA cert
    private_key             = $dir/ca/$ca/private/$ca.key # CA private key
    new_certs_dir           = $dir/ca/$ca           # Certificate archive
    serial                  = $dir/ca/$ca/db/$ca.crt.srl # Serial number file
    crlnumber               = $dir/ca/$ca/db/$ca.crl.srl # CRL number file
    database                = $dir/ca/$ca/db/$ca.db # Index file
    unique_subject          = no                    # Require unique subject
    default_days            = 3652                  # How long to certify for
    default_md              = sha1                  # MD to use
    policy                  = match_pol             # Default naming policy
    email_in_dn             = no                    # Add email to cert DN
    preserve                = no                    # Keep passed DN ordering
    name_opt                = ca_default            # Subject DN display options
    cert_opt                = ca_default            # Certificate display options
    copy_extensions         = none                  # Copy extensions from CSR
    x509_extensions         = signing_ca_ext        # Default cert extensions
    default_crl_days        = 365                   # How long before next CRL
    crl_extensions          = crl_ext               # CRL extensions

    # Naming policies control which parts of a DN end up in the certificate and
    # under what circumstances certification should be denied.

    [ match_pol ]
    domainComponent         = match                 # Must match 'simple.org'
    organizationName        = match                 # Must match 'Simple Inc'
    organizationalUnitName  = optional              # Included if present
    commonName              = supplied              # Must be present

    [ any_pol ]
    domainComponent         = optional
    countryName             = optional
    stateOrProvinceName     = optional
    localityName            = optional
    organizationName        = optional
    organizationalUnitName  = optional
    commonName              = optional
    emailAddress            = optional

    # Certificate extensions define what types of certificates the CA is able to
    # create.

    [ root_ca_ext ]
    keyUsage                = critical,keyCertSign,cRLSign
    basicConstraints        = critical,CA:true
    subjectKeyIdentifier    = hash
    authorityKeyIdentifier  = keyid:always

    [ signing_ca_ext ]
    keyUsage                = critical,keyCertSign,cRLSign
    basicConstraints        = critical,CA:true,pathlen:0
    subjectKeyIdentifier    = hash
    authorityKeyIdentifier  = keyid:always

    # CRL extensions exist solely to point to the CA certificate that has issued
    # the CRL.

    [ crl_ext ]
    authorityKeyIdentifier  = keyid:always

Generate key and CSR

    openssl req -new -config root-ca.conf -out root-ca.csr -keyout private/root-ca.key

Create a self-signed certificate

    openssl ca -selfsign -config root-ca.conf -in root-ca.csr -out root-ca.crt -extensions ca_ext

The index file `db/index` is plaintext and contains certificate information one per line.

    V    240706115345Z        1001    unknown    /C=GB/O=Example/CN=Root CA

* Status flag: `V - valid, R - revoked, E - expired`
* expiration date: `YYMMDDHHMMSSZ`
* Revocation date
* Serial number: Hex
* File location, `unknown` if not known
* Distinguished Name

#### Root CA Operations

**More info in the book**

## Testing with OpenSSL

> Due to the large number of protocol features and implementation quirks, it’s sometimes difficult to determine the exact configuration and features of secure servers

### Connnecting to SSL Services

Supply a hostname and a port

    openssl s_client -connect fixes.co.za:443

You will get output then get to send HTTP requests, type:

    HTTP / HTTP/1.0

We know the TLS layer is working.

#### Parts of the Cert

Server Certificate info

    CONNECTED(00000005)
    depth=1 C = US, O = Let's Encrypt, CN = Let's Encrypt Authority X3
    verify error:num=20:unable to get local issuer certificate
    verify return:0

If you have certificate validation required and there is a self-signed certificate in the chain:

    self signed certificate in certificate chain

You would want to point `s_client` to the trusted certificate CA, eg:

    openssl s_client -connect www.feistyduck.com:443 -CAfile /etc/ssl/certs/ca-certificates.crt

Next the certificates are presented in the order in which they are delivered:

    Certificate chain
    0 s:/CN=fixes.co.za
    i:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    1 s:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    i:/O=Digital Signature Trust Co./CN=DST Root CA X3

First line is the subject, second line is the issuer.

Next part is the cserver certificate:

    Server certificate
    -----BEGIN CERTIFICATE-----
    MIIGDjCCBPagAwIBAgISAz7feX99SqugF...
    -----END CERTIFICATE-----
    subject=/CN=fixes.co.za
    issuer=/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3

whenever you see a long string on numbers it means that OpenSSL does not know the object identifier (OID)

Information about the TLS protocol

    ---
    No client certificate CA names sent
    ---
    SSL handshake has read 3417 bytes and written 444 bytes
    ---
    New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
    Server public key is 2048 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    No ALPN negotiated
    SSL-Session:
        Protocol  : TLSv1.2
        Cipher    : ECDHE-RSA-AES256-GCM-SHA384
        Session-ID: 8B6F4472535450C0BEF7DEC8831C769188D946585868F49EE748D71283D5865A
        Session-ID-ctx: 
        Master-Key: AC39C620EAA804CD3554AA7949CB076211A4E851F651E1FA264C0F96973F74A012E59165C16DAD58B71749536B1F3A2F
        TLS session ticket lifetime hint: 300 (seconds)
        TLS session ticket:
        0000 - c3 06 75 ff 57 44 fb d1-96 7a 3a 84 71 13 d4 e5   ..u.WD...z:.q...
        ...

        Start Time: 1592554496
        Timeout   : 300 (sec)
        Verify return code: 0 (ok)

The most important thing here is tht TLS version and cipher suite used:

    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384

You also have a session ID and ticket for resuming and maintaining state client side

### Testing Protocol Upgrades

When used with HTTP, TLS wraps the entire plaintext communication to form HTTPS

Other protocols start as plaintext and are then upgraded.

Supported protocols: `smtp`, `pop3`, `imap`, `ftp` and `xmpp`

To test that kind of protocol you would use the `-starttls` switch:

    openssl s_client -connect mx1.privateemail.com:25 -starttls smtp

#### Extracting Remote Certificates

> When you connect to a remote secure server using `s_client`, it will dump the server’s PEM encoded certificate to standard output

You can write the certificate to a file:

    echo | openssl s_client -connect fixes.co.za:443 2>&1 | sed --quiet '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > fixes.co.za.crt

#### Explicitly testing a protocol

Openssl will always choose the best that both client and server can support

    openssl s_client -connect www.example.com:443 -tls1_2
    
    openssl s_client -connect www.example.com:443 -tls1_3

#### Test is a server supports a specific cipher suite

    openssl s_client -connect www.feistyduck.com:443 -cipher RC4-SHA

    ---
    no peer certificate available
    ---
    No client certificate CA names sent
    ---
    SSL handshake has read 7 bytes and written 100 bytes
    ---
    New, (NONE), Cipher is (NONE)
    Secure Renegotiation IS NOT supported
    Compression: NONE
    Expansion: NONE
    No ALPN negotiated

#### SNI

SNI is a TLS extension that enables use of more than one certificate on the same IP endpoint.

> Makes virtual scure hosting possible

    openssl s_client -connect www.feistyduck.com:443 -servername www.feistyduck.com

**Testing Cerfiticate reuse, OCSP Revocation in the book**

#### Testing OCSP Stapling

OCSP stapling is an optional feature allowing a server certificate to be accompanied by an OCSP response that proves its validity.

OCSP stapling is requested using the `-status` switch

    echo | openssl s_client -connect www.feistyduck.com:443 -status

**Checking CRL Certficate Revocation List, Testing Renegotiation**

#### Testing for the BEAST vulnerability

    echo | openssl s_client -connect www.feistyduck.com:443 -cipher 'ALL:!RC4' -no_ssl2 -no_tls1_1 -no_tls1_2

**Testing for Heartbleed in the book**

## TLS Deployment Best Practices

> Obtaining a comprehensive understanding of the SSL/TLS and PKI landscape requires a lot of time and dedication. In my experience, most people don’t need to know everything, but it’s tricky to find the small bits that they do need to know

**Best practices are in the book**


## Source

* [OpenSSL Cookbook (free Ebook) - Ivan Ristić](https://www.feistyduck.com/books/openssl-cookbook/)
* [Bulletproof TLS](https://www.feistyduck.com/books/bulletproof-ssl-and-tls/)
* [Example root_ca.conf](https://pki-tutorial.readthedocs.io/en/latest/index.html)