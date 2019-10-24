# The Path of Docker

I have been wondering how I should start moving my applications from traditional vm's to kubernetes - to attempt to save costs and compare.
I need to actually get data and experience to know whether moving certain workloads to containers is the right thing to do and whether deep diving into kubernetes is the way to go.

## Pragmatic Reality

I wanted to do this with a pragmatic approach.
Getting hello world up and running is okay but putting it into a real world scenario is important.

To not get into the **demo mode** trap

I have drafted a path towards containerisation:

1. Hello world - local machine
2. Hello world - kubernetes cluster
3. Static site - local machine
4. Static site - kubenernetes cluster
5. Deploying static site to kubernetes on deploy
6. Django site with containerised db - local machine
7. Django site with a managed db - kubernetes cluster

The reason we do the static site is because - html files static assets will be generated and that can be backed into an image and deployed.
There are no other dependencies other than a webserver to serve it.

## Setting up Jekyll

Check you current ruby version (or install it using rvm or brew)

    ruby -v
    ruby 2.1.10p492 (2016-04-01 revision 54464) [x86_64-darwin17.0]

Install recent ruby

    rvm install ruby-2.6.3
    # this takes about 4/5 minutes

> Remember we don't need ruby on our docker image - as ruby will only be used locally (or on ci) to generate the static files and then build that into an image.

    rvm use 2.6.3
    gem install bundler jekyll
    # takes about 3 minutes

    jekyll new <my_blog_name>

    cd <my_blog_name>
    bundle exec jekyll serve

Update `_config.yml` with your details

Build the site

    jekyll build

Add a `Dockerfile`

    FROM nginx:stable
    ADD ./_site /usr/share/nginx/html

Build the image

    docker build -t surfer190/fixes:0.1 .

Login to docker hub

    docker login
    docker push surfer190/fixes:0.1

Our `Dockerfile` assumes that `_site` exists.
We want the build to happen automatically - during the docker build - ie. include it in the push process.

Let us use [build phase hooks](https://docs.docker.com/docker-hub/builds/advanced/)

In `hooks/pre_build`:

    #!/bin/bash
    echo "=> Build the site using jekyll"
    mkdir -p _site
    docker run --volume=`pwd`:/srv/jekyll jekyll/jekyll jekyll build

What this does:

* Uses the `jekyll/jekyll` image for a jekyll environment - the [jekyll/jekyll](https://hub.docker.com/r/jekyll/jekyll/) image
* We map our current directory to `/srv/jekyll` where `jekyll/jekyll` expects the site
* We build the site with `jekyll build`






     
