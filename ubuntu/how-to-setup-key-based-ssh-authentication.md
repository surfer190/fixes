#How to Setup key-based (SSH) authentication on your Server

1. Create the key pair on client

`ssh-keygen -t rsa`

*Convention over configuration keep the default location*

2. Install the public key on remote server

`ssh-copy-id -i $HOME/.ssh/id_rsa.pub user@doolan.pw`

or

`scp $HOME/.ssh/id_rsa.pub user@doolan.pw:~/.ssh/authorized_keys`

*No `ssh-copy-id` installed?*

```
## First create .ssh directory on server ##
ssh user@doolan.pw umask 077; test -d .ssh || mkdir .ssh
 
## cat local id.rsa.pub file and pipe over ssh to append the public key in remote server ##
cat $HOME/.ssh/id_rsa.pub | ssh user@doolan.pw cat >> .ssh/authorized_keys
```

3. Test
```
ssh -T user@doolan.pw

or

scp foo.txt user@doolan.pw:/tmp
```

Get rid of password:

```
eval $(ssh-agent)
```

add passphrase for private key maintaind by ssh agent
```
ssh-add
```

Try login you shouldn't be prompted for password
```
ssh user@doolan.pw
```
(source)[http://www.cyberciti.biz/faq/how-to-set-up-ssh-keys-on-linux-unix/]