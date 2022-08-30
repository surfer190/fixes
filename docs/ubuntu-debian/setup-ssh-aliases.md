---
author: ''
category: Ubuntu-Debian
date: '2015-08-25'
summary: ''
title: Setup Ssh Aliases
---
# How to Set Up SSH Aliases - SSH Config

`vim ~/.ssh/config`

You can have as many entries as you like

#### Create a public key entry

```
Host somealias
	HostName example.com
	Port 22
	User someuser
	IdentityFile ~/.ssh/id_example
	IdentitiesOnly yes
```

### Create a password authentication entry

```
Host anotheralias
	HostName 192.168.33.10
	User anotheruser
	PubKeyAuthentication no
```

#### Use the alias

```
ssh somealias

ssh anotheralias
```

### Source

* [Servers for Hackers - SSH Tricks](https://serversforhackers.com/ssh-tricks)
