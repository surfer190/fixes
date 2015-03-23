#Common Vagrant Commands

Boot Server

```
vagrant up
```

Shut down the VM:

```
vagrant halt
```

Completely delete the machine

```
vagrant destroy
```

Re-create from original box downloaded

```
vagrant up
```

SSH into server
*must call command from where the Vagrantfile is located*

```
vagrant ssh
```

Or to connect from elsewhere

```
vagrant ssh-config
```

Run the Provisioner again
```
vagrant provision
```

