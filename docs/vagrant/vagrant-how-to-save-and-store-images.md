---
author: ''
category: Vagrant
date: '2015-09-25'
summary: ''
title: Vagrant How To Save And Store Images
---
# How to Compress and Save Images with vagrant

```
vagrant package
```

Which will create a file `<image_name>.box`

You can put the box in the same directory as your `VagrantFile` and say

## Adding the box again

```
vagrant box add package.box --name "<box_name>"
```

#### Note: The name must match the existing box

eg. `laravel/homestead`

```
vagrant box add package.box --name "laravel/homestead"
```

#### See a list of installed boxes

```
vagrant box list
```

### Sources

* [Vagrant Package Docs](https://docs.vagrantup.com/v2/cli/package.html)
* [Box File Format](https://docs.vagrantup.com/v2/boxes/format.html)
