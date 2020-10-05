---
author: ''
category: Security
date: '2020-09-20'
summary: ''
title: SSH - The Secure Shell Book (Notes)
---
# SSH - The Secure Shell Book (Notes)

## 1. Introduction to SSH

Multiple Computers and Accounts - making connection between them is useful:

* copy files
* log in remotely

`telnet`, `ftp` and `rsh` lack security

A third party can intercept the data - usernames and passwords are transmitted in plain text

SSH - secure shell - fixes this issue:

* data is always encrypted in transit
* client-server architecture

SSH software comes prepackaged with all good OS's.

> It is not a true shell - not a command interpreter, does not keep command history or wildcard expansion

It creates a channel between 2 systems with end-to-end encryption between

### SSH Protocol

It is a protocol, not a product. It specifies how data should be transferred over a network and the methods of authentication used.

Authentication - determining that an identity belongs to the entity claiming it
Encryption - scrambling data so it cannot be viewed or understood
Integrity - Guarenteeing that data arrives unaltered from source to destination

Protocols (dashes): `SSH-1`, `SSH-2`
Products (mixed case): `OpenSSH`, `PuTTY`
Client programs (lower case): `ssh`, `scp`, `putty`

### Secure Remote Logins

Remotely log into another machine with:

    ssh -l smith host.example.com

An encrypted conenction is used so your username and password is encrypted before leaving your machine

### Secure File Transfer

`ftp` allows packets to be intercepted and plain data viewed

You could encrypt the file before sending but that is quite tedious.
With `scp` the encryption happens automatically

Send local `myfile` to another computer account:

    scp myfile metoo@secondaccount.com:

### Secure Remote Command Execution

...

## Keys and Agents

Having multiple accounts and having to remember multiple passwords is difficult.
Also the more you use a password the more risk of it accidently being revealed.

SSH has various authentication methods - the most secure is based on keys.
A key is a small blob of bits identifying an SSH user
A key if often kept encrypted and only decryped when a passphase is used (not great for automation)

Using keys and authnetication agents - you can ssh into machines without requiring passwords

It works by:

1. Adding your public key from your ssh key pair into the `autorized_keys` file in the remote accoutns `~/.ssh` folder
2. Use an ssh agent program that has your secret key in memory

Access control can be used to permit other users to do certain things on the machine...

Any port can be used to ssh - provided the server is listening on the other side

### PGP vs SSH

Pretty Good Privacy or GnuPG (GNU Privacy Guard) is typically file based encryption - encrypting files one at a time. SSH encrypts an ongoing session between 2 computers.

### Kerberos

Secure authentication system or environments where networks may be monitored and computers arn't under central control.

Authenticates using `tickets` with a limited lifespan while user passwords stay secure on a central machine

SSH is lightweight, easily deployed and usually already running.

Kerberos needs significant setup and infrastructure to be established - a centralised host, admin and time synchronisation.
Kerberos also adds a centralized user account database, access control lists, and a hierarchical model of trust.

SSH can secure most TCP based programs using port forwarding.
With Kerberos the source code of client applications needs to be modified or libraries added.

### IPSEC and VPN

IPSec is the internet standard for network security - on a lower level of the network layers.
Can connect single machines or entire networks to each other through the internet (VPN)

IPSec does not deal with user authentication

### TLS

TLS - Transport Layer Security - is a protocol is an authentication and encryption technique developed by netscape to secure HTTP packets between clients and servers.

Nothing about it is specific to HTTP though.

A participant proves its identity with a _digital certificate_
The certificate indicates that a trusted third party has verified the binding between the identity and a given cryptographic key.

The trusted third parties are called root CA's and are packaged by default and sometimes updates on operating systems.

Once that check is done - transmission between client and server is encrypted using public key cryptography.

### STunnel

SSL tool that adds protection to TCP based services without having to change the source code
Email clients can connect to IMAP, POP and SMTP servers using SSL.

## 2. Basic Client Usage

More about this in the book...

### Known Hosts

The first time an SSH client connects to a server it may report that it has never seen the machine before:

    ubuntu@ubuntu:~$ ssh root@192.168.0.107
    The authenticity of host '192.168.0.107 (192.168.0.107)' can't be established.
    ECDSA key fingerprint is SHA256:2nJMAZX13WjEAMqO7Fo+56Q7+tJRdC/pMy2OUZN5Qiw.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?

If you say yes:

    Warning: Permanently added '192.168.0.107' (ECDSA) to the list of known hosts.

This is a security feature.

Suppose an advesary knows you are using ssh - so he subverts your naming service - so that the intended remote host points to an ip he controls.
He then installs an altered SSH server that records your password.

This is a _man-in-the-middle_ attack

Each SSH server has a secret, unique ID, called a host key, to identify itself to clients

Each time you connect the client checks the hosts identity using the public key.

Of course the first time you connect could be compromised but it is acceptable until `X.509-based public-key infrastructure` or secure DNS exists

If the host key is different the client raises a warning telling you it might be a man-in-the-middle attack

### Escape character

when in the middle of an ssh session you can escape it (pause it) and work locally.
The escape character is usually `~`

Type that then type `C-z` / `Ctrl-z`

Unsuspend it by typing `fg`

Source of the above info is [techrepublic - How to escape SSH sessions without ending them](https://www.techrepublic.com/blog/it-security/how-to-escape-ssh-sessions-without-ending-them/)

...More in the book on SSH key pairs

### Agent forwarding

Agents are a way for SSH clients to remember your identity.

You can give access to the remote ssh client to your local ssh agent.
So you can masquerade on the remote server as if you were the local machine.

Agent forwarding does not send your private key to the remote host - it just relays authentication requests back to the first host for processing.

### Passwordless SSH

Options for password-less ssh:

* public key authentication with an agent
* host based authentication
* kerberos authentication

### SFTP

* Secure File Transfer Protocol
* Mulitple operations in a single session - `scp` can only do a single thing in a session
* Can be scripted

### SLogin

`slogin` is an alternative name for `ssh` - better to just use `ssh` for consistency.

## 3. Inside SSH

Review of Major features of SSH:

* Privacy of data - strong encryption
* Intergrity of communications - unaltered
* Authentication - proof of identity
* Authorization - access control to accounts
* Forwarding or tunnelling - to encrypt other TCP/IP Sessions

### Privacy

* End-to-end encryption based on random keys securely negotiated for the session and destroyed once complete.

### Integrity

A `replay attack` is used when an attacker captures the bits and sees your plaintext commands.
The attacker can then replay those bits in an attack on the same session to run the same command you did.

SSH Integrity checking uses keyed hashing algorithms - probably `SHA1`

### Authentication

* 2 auths: server authentication and user authentication
* server authenticaiton - is host key `known_hosts`
* user authentication - traditionally done with passwords. The password is encrypted as it passes over the network.
* Other better authentication methods: per-user public key signatures, Kerberos, RSA's SecureID tokens, Pluggable authentication modules (PAM)

### Authorization

* Can be controlled server-wide (`/etc/ssh/sshd_config`)
* Per account: `~/.ssh/uthorized_keys` or `~/.shosts`

### Forwarding

* Encapsulating another TCP based service like Telnet or IMAP within a SSH Session.

Types of forwarding:

* TCP port forwarding - Secures any TCP based service
* X Forwarding - Secure th X11 Protocol
* Agent forwarding - Permits SSH clients to use SSH private keys on remote machines

### Cryptography Primer

#### Symmetric vs Assymetric Encryption

* `symmetric` or `secret key` ciphers - use the same key to encrypt and decrypt: `blowfish`, `AES`. There is a key distribution problem - how do you transport it securely.
* `assymetric` or `public key` ciphers - data encrypted wit 1 key can only be decrypted with the other private member of the pair. It is not feasible to derive a private key from a public one. When someone wants to send you a message they encrypt it with the public key.

> Public-key methods are also the basis for digital signatures: extra information attached to a digital document to provide evidence that a particular person has seen and agreed to it. Any asymmetric cipher (RSA, ElGamal, Elliptic Curve, etc.) may be used for digital signatures, though the reverse isn't true. For instance, the DSA algorithm is a signature-only public-key scheme and is not intended to be used for encryption

Public key algorithms are enourmously slower than secret key algorithms.
It is not feasible to enrypt large amounts of data with public key encryption.

The way large files are encrypted over networks would be:

1. Generate a key for AES encryption
2. Encrypt the plaintext with the key
3. Secure the AES private key by encrypting it with Bob's public key
4. Send the encrypted file and key to bob

#### Hashing

A hash function is simply a mapping from a larger set of data values to a smaller set

> For instance, a hash function H might take an input bit string of any length up to 50,000 bits, and uniformly produce a 128-bit output

THe idea is the hash is sent along with the mesage. The receiver calcualtes the hash from the message and compares it with the sent hash. If they differ - the integrity of the message is failed and has been changed in transit.

Uses:

* networking: datagrams transmitted over a network frequently include a message hash that detects transmission errors due to hardware failure or software bugs. 
* implementing digital signatures: signing a large amount of data is expensive - as it is a public key operation.

Digital signatures steps:

1. Hash the document - producing a small hash value
2. sign the hash and send that along with the document
3. verifier independently computes the hash and decrypts the signature and compares them

Hashes need to make in infeasible to find 2 same hashes for different messages. They must be `collision-resistant`.

#### SSH Architecture

> An SSH connection has several session keys: each direction (server to client, and client to server) has keys for encryption and others for integrity checking. In our discussions we treat all the session keys as a unit and speak of "the session key" for convenience; they are all derived from a single master secret, anyway

### Inside SSH-2

Four major pieces:

* `SSH-TRANS` - SSH transport layer protocol
* `SSH-AUTH` - SSH Authentication layer protocol
* `SSH-CONN` - SSH Connection Protocol
* `SSH-SFTP` - SSH File transfer protocol

`SSH-TRANS` is the building block:

* Intial connection
* Record protocol
* Server authnetication
* Basic encryption
* Integrity services

Single secure full-duplex byte stream

Then `SSH-AUTH` is used over `SSH-TRANS`. Then `SSH-CONN`.
`SSH-CONN` and `SSH-AUTH` are at the same layer - insude `SSH-TRANS`.

Protocol only mentions about _on the wire_ communication. Other conventions we think are part of the protocol like `authorized_keys` and `known_hosts` are not. THey are _implementation dependent_.

#### SSH-TRANS

##### Connection

    ssh -vv 192.168.0.107

    OpenSSH_7.6p1, LibreSSL 2.6.2
    debug1: Reading configuration data /Users/stephen/.ssh/config
    debug1: Reading configuration data /etc/ssh/ssh_config
    debug1: /etc/ssh/ssh_config line 48: Applying options for *
    debug1: /etc/ssh/ssh_config line 52: Applying options for *
    debug2: ssh_connect_direct: needpriv 0
    debug1: Connecting to 192.168.0.107 port 22.
    debug1: Connection established.

##### Protocol version Selection

After the server accepts connection, the server announces its protocol version:

    debug1: Remote protocol version 2.0, remote software version OpenSSH_8.2p1 Ubuntu-4ubuntu0.1

> The server in this case is ubuntu running OpenSSH 8.2

You can also see this if you connect to the server socket

    telnet 192.168.0.107 22
    
    SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1

Some people like to change it on security grounds - but it is more hassle than it is worth as clients may stop working

The version is parsed:

    debug1: match: OpenSSH_8.2p1 Ubuntu-4ubuntu0.1 pat OpenSSH* compat 0x04000000
    
Local client version is selected:

    debug1: Local version string SSH-2.0-OpenSSH_7.6

Now the switch is made to non-textual record oriented protocol...called the `ssh binary packet protocol`

##### Parameter negotiation

Both sides must agree on session parameters.

    debug1: SSH2_MSG_KEXINIT sent
    debug1: SSH2_MSG_KEXINIT received

Key exchange algorithms are presented:

    debug2: KEX algorithms: curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha256,diffie-hellman-group14-sha1,ext-info-c

Host key types client can accept:

    debug2: host key algorithms: ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-ed25519-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,ssh-ed25519,rsa-sha2-512,rsa-sha2-256,ssh-rsa

Also bulk data encryption ciphers:

    debug2: ciphers ctos: chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com
    debug2: ciphers stoc: chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com

> The `none` encryption cipher is allowed - presumably for debugging - it is dangerous however. If a hacker gains access to the ssh config `~/.ssh/config` and sets:

    Host *
      Ciphers none

Then all ssh sessions become transparent.

The client and server must support `none`.

Then client gives integrity algorithms it supports:

    debug2: MACs ctos: umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1
    debug2: MACs stoc: umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1

Finally the data compression techniques it supports:

    debug2: compression ctos: none,zlib@openssh.com,zlib
    debug2: compression stoc: none,zlib@openssh.com,zlib

Then the same thing happens from the server side.

The server's host key is also returned:

    debug1: Server host key: ecdsa-sha2-nistp256 SHA256:2nJMAZX13WjEAMqO7Fo+56Q7+tJRdC/pMy2OUZN5Qiw

This is checked in the `known_hosts` file

> The problem of verifying the owner of a public key is hardly a new one; that's what Public Key Infrastructure (PKI) systems are for, such as the X.509 standard for public-key certificates. SSH-2 supports PKI, defining a number of key types which include attached certificates:

* `ssh-rsa` - plain rsa key
* `ssh-dss` - plain dss key
* `x509v3-sign-rsa` - X.509 certificate (RSA key)
* `x509v3-sign-dss` - X.509 certificate (DSS key)
* `spki-sign-rsa` - SPKI certificate (RSA key)
* `spki-sign-dss` - SPKI certificate (DSS key)
* `pgp-sign-rsa` - OpenPGP certificate (RSA key)
* `pgp-sign-dss` - OpenPGP certificate (DSS key)

Many SSH products don't support PKI.

> with PKI support, the client could verify the host key by its accompanying certificate. New hosts could be added and existing keys changed, without having to push out new known-hosts files to all clients every time—often a practical impossibility anyway, when you consider laptops, many different SSH clients with different ways of storing host keys, etc. Instead, clients only need a single key; that of the authority issuing your host key certificates.

....Book starts getting a bit hectic

## PKI

The reason I started reading this book was getting the fundementals of how to enable secure and scalable SSH through central auth using your own certificate authority. Known as Public Key Infrastructure.

So I search the book for that term and will paste the content:

* Tectia clients can use external key providers that distribute keys, somewhat like authentication agents. These are typically part of a more general solution for PKI (Public Key Infrastructure)


## 11. Case Studies

### Scalable Authnetication for SSH

One of the strength of SSH is easy setup.
Setup the client and server - and you have secure login with a password.
Generate a SSH key pair and even better security.

A lightweight approach.

However, the simplicity becomes a liability when the number of hosts and users grow.
Managing server and user authnetication becomes difficult.

Everytime a servers host or name changes you must update a global `known_hosts` file.

Problem is that the format of this file is different per client.

> The difficulty in managing SSH server keys leads to a lax approach to server verification

IT just recommends to click `yes` or ignore the warning. Some even go so far as to update their config to disable host checking:

    # /etc/ssh/ssh_config
    GlobalKnownHostsFile   /dev/null
    UserKnownHostsFile     /dev/null
    StrictHostKeyChecking  no

> Skipping host checking skips a vital partof SSH security - resistance to server host spoofing and man-in-the-middle attacks

This also applies to user auth, authorizing a new user means adding their public key to the `authorized_keys` on every server in your fleet.
Revoking also means removing the keys.

> The protocol says nothing about how a server key should be verified or a user key authorized for access, and SSH software is free to use more sophisticated methods

### X.509 public-key infrastructure (PKI) with Tectia

#### What is PKI?

Public key infrastructure - a system for dealing with trust issues raised by deploying assymetric (public key) cryptography

* Binding public keys to indentities: users, hosts and routers
* Indicating or controlling the use of keys (encryption, signing, email and Web TLS)
* Replacing keys
* Renewing or revoking keys
* Securely communciating the above

It is a hierachical system where Certificate Authorities (CA's) vouch for identity of principals and the ownership of cryptographic keys.

CA's can be vouched for by CA's higher in the chain - seperating responsiibilities.

X.509 is a directory authentication framework.
It specifies a format for digital signatures - data structures that embody the key-principal binding.

The most important components of a certificate:

* Issuer name
* Subject name
* Public key
* Validity dates
* Signature

The _signature_ is ciphertext of the entire datastrucutre - made by the issuer using its private key.

The meaning of the signature:

> Issuers vouches that the subject owns the private counterpart to this public key - but only from this date tot this date

The issuer and subject names are expressed as _Distinguished names_ 

    /C=US/ST=New York/O=Mad Writer Enterprises/CN=Richard E. Silverman 
    /emailAddress=res@oreilly.com

The abbreviations are `/C` country, `/ST` state, `/O` organisastion and `/CN` common name.

### Using Certificates with Tectia Host Keys

When a client connects to a server it needs to verify that the server's host key actually belongs to the host it intended to contact.
The usual way is to compare that to a local list of already known keys.

Instead of managing a set of host keys with `PKI` - each client needs only 1 public key - that of a `CA` shared by all hosts in the system.
Each time you deploy a new tectia host - you generate a new hostkey as usual - but you also obtain a certificate biding its host's name to its public key.
That certificate is signed by the CA, and every client has the CA's public key.

> During the key-exchange phase of the SSH protocol, the client receives the certificate along with the server's hostkey

The hostkey is an `x509v3-sign-rsa` or `x509v3-sign-dss` - instead of `ssh-rsa` or `ssh-dsa`

Instead of looking up the hostkey in a list, the tectia client:

1. Compares subject name in cert to the server hostname and ensures they match
2. Verifies the server signature - proving it holds the private key
3. Verifies the issuer signature on the certificate using the CA's public key

If all 3 tests pass the client considers the key valid and server authentication succeeds.
The clients still need to get the CA key in a trusted way (does not eliminate key distribution issues).
But it is much easier to distribute a single CA key infrequently that constantly update a shared `known_hosts`.

### A Simple Configuration

1. Start with a new instance of Tectia Server installed on a Linux host
2. generate a hostkey with a certificate

> The generation of a certificate is determined by the PKI system in use: a homebrew CA using OpenSSL generated certs to an outsourced managed security vendor with multiple hierachies, cross-certification among organisations, seperate registration authorities and private-key escrow

If the PKI in question uses `certificate management protocols` then you can use `ssh-cmp-client` to communicate with the PKI system: generating keys, request, receive or update certificates.

#### Getting a Certificate

To generate a key pair and certificate request for the company `Fixes` that has the hostname `foo.fixes.co.za`:

    openssl req -nodes -newkey rsa:1024 -out request.pem -outform pem \
    -keyout private.pem -days 1095 \
    -subj '/C=ZA/ST=Gauteng/L=Johannesburg/O=Fixes.co.za/CN=security.fixes.co.za'

This generates a 1024 bit RSA key pair

* `private.pem` - the unecrypted private key
* `request.pem` - An x.509 certificate request. Contains the public key and asks to bind the hsotname `security.fixes.co.za` to that key for 3 years. 

> PEM stands for `Privacy Enchanced Mail` format - it is the de facto format for storing certs and sending cryptographic keys

A PEM encoded certifcate starts with `-----BEGIN CERTIFICATE-----` and ends with `-----END CERTIFICATE-----`

A PEM encoded certifcate signing requests starts with `-----BEGIN CERTIFICATE REQUEST-----` and ends with `-----END CERTIFICATE REQUEST-----`

Then send the `request.pem` to  your CA , to authenticates that certificate you created, when the CA is satisfied it will return a file `certificate.blob`

Now `private.pem` and `certificate.blob` contain the host private key and our desired certificate.

You can delete `request.pem`.

Then convert the files to the format for `tectia host keys`:

    openssl pkcs12 -export out fixes.pl2 -in certificate.blob -inform pem -inkey private.pem

Then generate the certificate and private key pair for ssh:

    ssh-keygen -k fixes.p12 -p 

This produces:

* fixes.p12-1_ssh2.crt - Certificate in DER format
* fixes.p12_ssh2 - Unencrypted private key in SECSH format used by Tectia”

Now we need to get Tectia SSH server to use them

#### Host key verification - configuring the server

Install the new key and certificate in the tectia configuration directory:

    install -o root -m 444 fixes.p12-1_ssh2.crt /etc/ssh2/fixes.crt
    install -o root -m 444 fixes.p12_ssh2 /etc/ssh2/fixes

And add this to `sshd2_config`:

    HostCertificateFile fixes.crt
    HostKeyFile fixes

To continue allowing regular public key pairs, uncomment:

    PublicHostKyeFile hostkey.pub
    HostKeyFile hostkey

> Suggestion is to leave all other host key verification files

Restart tectia:

    service sshd restart

Try to connect with ssh:

    ssh security.fixes.co.za

now we just need to ensure the client verifies the certificate.

#### Hostkey verification - configuring the client

The CA's public key is required - this should be readily available. It is of no use if everyone does not have it.

Convert it to `DEM` from `PEM`:

    openssl x509 -inform pem -outform der -in <certificate file> -out cacert.der

Now install the CA cert:

    install -o root -m 444 cacert.der /etc/ssh2

Edit `/etc/ssh2/ssh2_config`:

    HostCANoCRLs /etc/ssh2/cacert.der

Then try:

    ssh -v security.fixes.co.za

#### User Authentication - configuring the client

We need to authenticate users with the certificate as well.
Now we need a new keypair and certificate for a DN matching a user.

We follow the same procedure as earlier but with a different subject name:

    openssl req -nodes -newkey rsa:1024 -out request.pem -outform pem \
    -keyout private.pem -days 1095 \
    -subj '/C=ZA/ST=Gauteng/L=Johannesburg/O=Fixes.co.za/CN=Stephen Fixes subjectAltName=emailstephen@fixes.co.za'

> It is crucial to include `subjectAltName` - tectia requires this attribute as an email

Once you have your private key and certificate place them in: `~/.ssh2`

* `~/.ssh2/pvj.crt` - certificate
* `~/.ssh2/pvj` - private key

Then configure ssh to use this key: `~/.ssh2/identification`

    CertKey pvj

It won't work yet as we haven't configured the server but to test:

    ssh -l pvj fixes -o AllowedAuthentications=publickey

Now we need to configure the server on how to authorize users based on certificates

#### User authentication - configuring the server

The old way there was an _implicit correspondence between an account and a public key authorized to log into it_

The key was in a special file in the home directory `authorized_keys`

With PKI, there is only 1 certificate - so we need to let tectia verify that a particular certificate grants access to the requested account.

In `/etc/ssh2/sshd2_config`:

    PKI cacert.der
    PKIDisableCrls yes
    MapFile cert.users

This tells tectia server it must trust user certificates signed by our CA and use the rules in `/etc/ssh2/cert.users` to authorize access to accounts.

The rule language is described in the manpage for `ssh_certd_config` section `MAPPING_FILES`

Example:

    # allow a certificate issued to Prostetnic V. Jeltz in our company, access to account pvj
    #
    pvj subject C=US,ST=New York,L=Manhattan,O=Vogon Construction, Inc.,CN=Prostetnic V. Jeltz

    # allow any certificate issued to Prostetnic V. Jeltz, whether by our organization or not
    #
    pvj subject CN=Prostetnic V. Jeltz

    # allow certificate serial number 17 issued by our CA
    #
    pvj SerialAndIssuer 17 C=US,ST=New York,L=Manhattan,O=Vogon Construction, Inc.

    # allow any certificate issued by us to access account "shared"
    #
    shared Issuer C=US,ST=New York,L=Manhattan,O=Vogon Construction, Inc.
    # allow certificate with email address pvj@vcon.com
    #
    pvj email pvj@vcon.com

    # pattern rule: allow certificate with email address <foo>@vcon.com to access account <foo>
    #
    %subst% EmailRegex ([a-z]+)@vcon\.com”

Tectia has a seperate daemon for certificate validation:

    service ssh-certd restart

If all goes well:

    sshd2: Certificate authentication for user pvj accepted.

## Using Vault as a Certicate Authority and Secret Manager for SSH

I used the following resources as guides:

* https://www.vaultproject.io/docs/secrets/ssh/signed-ssh-certificates
* https://abridge2devnull.com/posts/2018/05/leveraging-hashicorp-vaults-ssh-secrets-engine/
* https://learn.hashicorp.com/tutorials/vault/ssh-otp
* https://gist.github.com/kawsark/587f40541881cea58fbaaf07bb82b1be


## Source

* SSH, the Secure Shell, 2nd Edition. - Daniel J. Barrett;Richard E. Silverman;Robert G. Byrnes. 

