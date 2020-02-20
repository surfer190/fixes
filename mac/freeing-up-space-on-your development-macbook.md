## Freeing Up Space on mac

### Brew

    brew cleanup

of

    brew update && brew upgrade && brew cleanup

### minikube

    minikube delete

### minishift

    minishift delete

### Vagrant

    vagrant box prune
    vagrant box list
    vagrant box remove <box-name>

### Node Modules

Remove all `node_modules` older than 4 months

    find . -name "node_modules" -type d -mtime +120 | xargs rm -rf

> I get permission denied for this crap

### Ruby

    gem cleanup

### Docker

Remove unused docker volumes

    docker volume prune

#### Sources

* [Freeing Up Macbook Space](https://www.freecodecamp.org/news/how-to-free-up-space-on-your-developer-mac-f542f66ddfb/)
