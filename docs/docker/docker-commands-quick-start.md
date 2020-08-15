---
author: ''
category: Docker
date: '2020-06-14'
summary: ''
title: Docker Commands Quick Start
---
# Docker Quickstart

Build a dockerfile:

    docker build -t <name> .

List the available images:

    docker images

Run an image:

    docker run <image_name>:<tag>

If you want to run it in the background use `-d`

    docker run elastalert:latest -d

If you want to publish a containers ports to the host use `-p`:

    docker run <image>:<version> -d -p <port on host>:<port on container> -p <port on host>:<port on container> --net="host"

Eg.

    docker run elastalert:latest -d -p 3030:3030 -p 3333:3333 --net="host"
    
If you want to bind a volume use `-v`:

    docker run elastalert:latest -d -p 3030:3030 -v $HOME/myContainer/configDir:/myImage/configDir

Use `--name ` to assign a name to the container

More info on the [docker run reference](https://docs.docker.com/engine/reference/run/)

View all running and non-running containers:

    docker ps -a

Remove an image:

    docker rm <name>

Get the reason why a docker container exited:

    docker logs <container-id>

Inspect the container:

    docker inspect <container-id>

Ensure a container is removed when it exits or stops, use `--rm`:

    docker run --rm -d --network host --name my_nginx nginx

# Key Concepts

You got Images and Containers, and you need to know what state you are at:

* Does the docker **image** exist?
* Does the docker **container** exist?
* Is the docker container **running**?

If we are talking containers your command will look like:

    docker container <command>

These are container commands:

* `create` — Create a container from an image. 
* `start` — Start an existing container. 
* `run` — Create a new container and start it. 
* `ls` — List running containers. 
* `inspect` — See lots of info about a container.
* `logs` — Print logs. 
* `stop` — Gracefully stop running container. 
* `kill` —Stop main process in container abruptly. 
* `rm`— Delete a stopped container.

If we are dealing with images:

    docker image <command>

These are image commands:

* `build` — Build an image.
* `push` — Push an image to a remote registry.
* `ls` — List images. 
* `history` — See intermediate image info.
* `inspect` — See lots of info about an image, including the layers. 
* `rm` — Delete an image.

Misc commands:

* `docker version` — List info about your Docker Client and Server versions.
* `docker login` — Log in to a Docker registry.
* `docker system prune` — Delete all unused containers, unused networks, and dangling images.

## Container

Create a container from an image

    docker container create my_repo/my_image:my_tag

You can use `-a` for attach (for `STDIN`, `STDOUT` or `STDERR`)

    docker container create -a STDIN my_image

Start an existing container

    docker container start my_container

> A container can be refered to by its id or name

Run combines both create and start:

    docker container run my_image

Some options:

* `-i` or `--interactive` - Keep STDIN open even if unattached
* `-t` or `--tty` - Allocates a pseudo terminal that connects your terminal with the container’s STDIN and STDOUT
* `-p` or `--port` - The port is the interface with the outside world. `1000:8000` maps the docker port `8000` to port `1000` on your machine / host. Eg. go to `localhost:1000` on your host
* `--rm` - automatically remove container when it stops running
* `-d` or `--detach` - Run the container in the background as a daemon

List all containers and sizes:

    docker container ls -a -s

Inspect a container:

    docker container inspect my_container

Print a containers log:

    docker container logs my_container

Stop a running container:

    docker container stop my_container

Stop a running container immediately (abruptly):

    docker container kill my_container

Kill all running containers:

    docker container kill $(docker ps -q)

Delete one or more containers:

    docker container rm my_container

## Image

Build a docker image from a dockerfile located at a specific path:

    docker image build -t my_repo/my_image:my_tag .

Pushing an image to a registry

    docker image push my_repo/my_image:my_tag

List images and sizes

    docker image ls

View the history of an image:

    docker image history my_image

Show details and layers of your image:

    docker image inspect my_image

Remove an image

    docker image rm my_image

## Admin

Get docker system info

    docker system info

Delete unused containers, unused networks and dangling images

    docker system prune

Show docker disk usage

    docker system df


