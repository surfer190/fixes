---
author: ''
category: Ubuntu-Debian
date: '2016-08-06'
summary: ''
title: How To Setup Key Based Ssh Authentication
---
# How to Setup key-based (SSH) authentication on your Server

1. Create the key pair on client

    `ssh-keygen -t rsa`

    *Convention over configuration keep the default location*

2. Install the public key on remote server

    `ssh-copy-id -i $HOME/.ssh/id_rsa.pub user@fixes.co.za`

    Not if you don't have the private key you need to use the `-f` option:

    `ssh-copy-id -f -i $HOME/.ssh/id_rsa.pub user@fixes.co.za`

    or

        scp $HOME/.ssh/id_rsa.pub user@fixes.co.za:~/.ssh/authorized_keys

    #### No `ssh-copy-id` installed?

        First create .ssh directory on server

        ssh user@fixes.co.za umask 077; test -d .ssh || mkdir .ssh

        cat local id.rsa.pub file and pipe over ssh to append the public key in remote server

        cat $HOME/.ssh/id_rsa.pub | ssh user@fixes.co.za cat >> .ssh/authorized_keys

3. Test

        ssh -T user@fixes.co.za

        or

        scp foo.txt user@fixes.co.za:/tmp

    Get rid of password:

    `eval $(ssh-agent)`

    add passphrase for private key maintained by ssh agent

    `ssh-add`

    Try login you shouldn't be prompted for password

    `ssh user@fixes.co.za`

## Now to Disable Password Authentication on your server

```
sudo vim /etc/ssh/sshd_config
```

#### Set:

```
PasswordAuthentication no
```

**Restart SSH**

```
sudo service ssh restart
```

#### Sources:

* [cyberciti](http://www.cyberciti.biz/faq/how-to-set-up-ssh-keys-on-linux-unix/)
* [digitaloceans](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)
