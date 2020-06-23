# How to Add Someone elses pblic SSH key to a remote server

```
cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
```

or using `ssh-copy-id`:

    ssh-copy-id -f -i <someones.pub> user@hostname

## Source

* [How to Add Someone elses pblic SSH key to a remote server](http://www.howtogeek.com/168147/add-public-ssh-key-to-remote-server-in-a-single-command/)
