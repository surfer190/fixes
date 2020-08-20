---
author: ''
category: Docker
date: '2019-11-18'
summary: ''
title: Edit A File In Docker Container With No Editor
---
## How to Edit a File in a docker container with no Text Editor

THe lightwight nature of docker images, means that often they do not have the standard utilities we expect on every standard linux machine.

Simply editing a file is an ordeal if you don't have `vim`, `vi` or `nano` available.

One of the best things to do may be to copy the file from the container to your host machine:

    docker cp <container>:/path/to/file.ext .
    
Edit the file.

Then send it back to the container.

    docker cp file.ext <container>:/path/to/file.ext

### Sources

* [How do I edit a file after I shell to a Docker container?](https://stackoverflow.com/questions/30853247/how-do-i-edit-a-file-after-i-shell-to-a-docker-container)