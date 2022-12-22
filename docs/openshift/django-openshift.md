---
author: ''
category: Openshift
date: '2020-06-14'
summary: ''
title: Django Openshift
---
## Deploying Django to Openshift

There are a few key things to understand about docker images on openshift:

* Don’t run as root (you can build as root)
* Don’t listen port < 1024
* Openshift starts the image with a random UID but **always with root GID**. So if the container need to write a directory. Set the directory group as root with rwx permission to make openshift happy!

1. Initialise project

    django-admin startproject keycloak-portal
    
2. Go into the folder and intialise a `venv`

    python3.8 -m venv env
    source env/bin/activate
    pip install django

3. Add requirements 

    pip freeze > requirements.txt

4. Create a dockerfile based on an [example dockerfile](https://github.com/openshift-katacoda/blog-django-py/blob/master/Dockerfile) probably best to avoid a [dockerfile like this](https://github.com/CentOS/CentOS-Dockerfiles/blob/master/Django/centos7/Dockerfile)

    # pull official python alpine image
    FROM python:3.8-alpine

    LABEL maintainer="My Name <my@email.co.za>"

    ENV PYTHONUNBUFFERED 1
    ENV PYTHONDONTWRITEBYTECODE 1

    USER root

    # Update pip
    RUN pip install --upgrade pip

    # Create the working directory
    RUN mkdir -p /code
    WORKDIR /code

    # Installing requirements.txt from project
    COPY ./requirements.txt /code/
    RUN pip install --no-cache-dir -r /code/requirements.txt

    # removing temporary packages from docker and removing cache 
    RUN rm -rf ~/.cache/pip

    # Copy Project
    COPY . /code/

    # Allow the root user access to the code
    RUN rm -rf /code/.git* && \
        chown -R 1001 /code && \
        chgrp -R 0 /code && \
        chmod -R g+w /code

    USER 1001

    EXPOSE 8000

    # CMD will run when this dockerfile is running
    CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; python manage.py runserver 0.0.0.0:8000"]

5. Build the image

    docker build -t keycloak_portal:0.1 .

6. Run the image

    docker run -it -p 8000:8000 keycloak_portal:0.1

7. Push the image to a private or public repo

8. Create the project and deploy the app on openshift


## Sources

https://blog.openshift.com/migrating-django-applications-openshift-3/
https://ruddra.com/posts/openshift-python-gunicorn-nginx-jenkins-pipelines-part-one/
https://medium.com/@uddishverma22/leveraging-docker-images-to-deploy-your-django-backend-on-openshift-5e268d679173
* [Elasticsearch Openshift Compatability](https://medium.com/faun/official-elasticsearch-images-and-openshift-compatibility-a7ea03b31924)