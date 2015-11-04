# Common Ansible Errors and Solutions

### ERROR! template error while templating string: expected token 'end of print statement', got 'key'

```
fatal: [localhost]: FAILED! => {"failed": true, "msg": "ERROR! template error while templating string: expected token 'end of print statement', got 'key'"}
```

This is usually an issue with a variable containing a space

`ssh_pub_key={{ public key }}`

Should be:

`ssh_pub_key={{ public_key }}`

Source: [Stackoverflow](http://stackoverflow.com/questions/31295662/ansible-copy-fails-template-error)
