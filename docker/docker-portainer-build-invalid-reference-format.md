## Docker error on portainer Build invalid reference format

I got this error when trying to deploy a stack. I set the `docker-compose.yml` file to use and link to the git repo I get this error:

    Build invalid reference format

So my first thought was that the `docker-compose version` was too high `3.7`, but that wasn't the problem.

The problem was that this docker compose was structured for development - ie. it relied on the code being local and building the image.

When you deploy to production there is nothing to build only an image to pull and set commands or env variabled.

So I change the `docker-compose.yml` from:

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file:
      - ./env.dev
    depends_on:
      - db

and added a `production.yml`:

    web:
      command: /bin/bash run.sh
      image: registry.example.com:5000/dyndns_api_web:0.1
      ports:
        - "8000:8000"
      env_file:
        - ./env.dev
      depends_on:
        - db

So it is now pulling the image from the repo and running the command to set it up

### Source

* [Docker compose in Production](https://docs.docker.com/compose/production/)
