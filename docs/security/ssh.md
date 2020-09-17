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

## 3. Inside SSH




## Source

* SSH, the Secure Shell, 2nd Edition. - Daniel J. Barrett;Richard E. Silverman;Robert G. Byrnes. 

