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
    docker image prune (clean up unused images)
    docker image prunt -a (clean up used images of existing containers)
    
    docker container prune
    docker network prune

Prune everything

    docker system prune

#### Sources

* [Freeing Up Macbook Space](https://www.freecodecamp.org/news/how-to-free-up-space-on-your-developer-mac-f542f66ddfb/)
* [Pruning Docker](https://docs.docker.com/config/pruning/)