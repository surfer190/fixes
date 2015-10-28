# Host Key Verification Failed when Testing SSH

So Everything is good and well. You have added the jenkins user's `public ssh key` to the server and you are A-for-Away.

Lets test is quick:

```
ssh -T user@hostname
```

And we get...

```
host key verification failed.
```

You can get a better understanding of this sometimes ellusive statement with:

```
ssh user@hostname -v
```

You will probably get something about no permission to `/dev/tty`

THe only way to fix this I have found is to specifiy the shell to use when switching to the `jenkins` user:

`sudo su -s /bin/bash jenkins`

Now it should work...

Source: [Hitmaroc Jenkins Host key Verification Failed](http://www.hitmaroc.net/36176-9147-jenkins-host-key-verification-failed.html)
