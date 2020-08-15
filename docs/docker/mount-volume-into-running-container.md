---
author: ''
category: Docker
date: '2019-11-18'
summary: ''
title: Mount Volume Into Running Container
---
## How to Mount a volume into a Running Docker Container

So you have a running container, that you have done significant stuff in and want to ensure that what you have done in the container - persists.
In this case, I don't know where the container is storing the configuration I have done.

You **commit** the container.

So get the running container's id:

    docker container list

Then commit it:

    docker commit <running-container-id> <commit-name>

Now create the folder for your mount and mount it:

    docker run -d -p 5000:8080 --mount type=bind,source=<my-source>,target=<my-target> <commit-name>


## Sources

* [How can I add a volume to an existing Docker container?](https://stackoverflow.com/questions/28302178/how-can-i-add-a-volume-to-an-existing-docker-container)
* 