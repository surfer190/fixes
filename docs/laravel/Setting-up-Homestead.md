---
author: ''
category: Laravel
date: '2015-09-25'
summary: ''
title: Setting Up Homestead
---
# Setting up homestead

`homestead` is a virtual machine. A virtual environment suited for `laravel`.

It has everything installed on it that needs to be installed for a `laravel` application and is a reusable, idempotent environment.

It uses `vagrant`

## Lets go

1. Install Vagrant

2. Install laravel

3. Require Homestead from `composer`

```
composed global require "laravel/homestead=~2.0"
```

4. Add the vagrant box

```
vagrant box add laravel/homestead
```
5. Initialise

```
homestead init
```

This does all the tricky stuff like stting up shared folders, SSH keys and the like.

This process creates a file called `~/.homestead/homestead.yml` which defines your setup.

6. Set your local dev folder in `homestead.yml`

7. Run homestead

```
homestead up
```

**You can now visit your site at localhost:8000**

8. Setup your local host file

```
sudo vim /etc/hosts
```

Change to the following:

```
192.168.10.10 homestead.App
```

7. If you change settings or add multiple sites I think you will need to destory and restart the whole thing:

```
homestead destroy
homestead up
```

### SSH into the Box

You might want to SSH into the box which can be achieved with:

```
ssh vagrant@localhost -p 2222
```

The details can be retrived just like avagrant box with:

```
homestead ssh-config
vagrant ssh-config
```
