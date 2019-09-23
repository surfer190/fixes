# Continuous Integration with Gitlab

* Continuous Integration - Pushing small chunks of code and on every push, run a pipeline of scripts to build, test, and validate the code changes before merging them into the main branch
* Continuous Delivery/Deployment - Deploying your application to production at every push

> Allow you to catch bugs and errors early in the development cycle

## Overview

GitLab CI/CD is configured by a file called `.gitlab-ci.yml` placed at the repository’s root.

The scripts in that file are executed by the gitlab runner - an open source project used to  run your jobs and send the results back to GitLab.

In this file you can specify(basically everything):
* what you want to run
* define include and cache dependencies
* choose commands you want to run in sequence and those you want to run in parallel
* define where you want to deploy your app
* specify whether you will want to run the scripts automatically or trigger any of them manually

> imagine that all the scripts you add to the configuration file are the same as the commands you run on a terminal in your computer

It is a good idea to check some of the [gitlab CI templates](https://gitlab.com/gitlab-org/gitlab-foss/tree/master/lib/gitlab/ci/templates) for ideas on your specific project.

The scripts are grouped into *jobs*, and together they compose a *pipeline*

You can view the result of your CI under `CI -> Jobs`

## Gitlab CI Workflow

1. Create Branch / Push new changes
2. Automated build and test (Continuous Integration)
3. Deploy Review App
4. Review and Approve
5. Merge
6. Deploy (Continuous Deployment)

You can go a bit deeper at each stage:

Continuous Integration could include code quality, performance testing, Junit tests, Container scanning and dependency scanning.
Packing can be done to the container registry.

## Practical Example

For a jekyll site to be built locally you would do `jekyll build`. Before that you would need jekyll on your computer. For that you would have had to `gem install jekyll`.
So for `gitlab` you tell it to do the same thing

The script would look like this:

    script:
      - gem install jekyll
      - jekyll build

Each script is organised by a job:

    job:
      script:
        - gem install jekyll
        - jekyll build

In the context of gitlab pages the job has a specific name called `pages`

    pages:
      script:
        - gem install jekyll
        - jekyll build

GitLab Pages will only consider files in a directory called public, so we need to tell jekyll to output to that folder:

    pages:
      script:
        - gem install jekyll
        - jekyll build -d public

#### Artifacts

We need to tell gitlab that the job generates artifacts in the public directory

    pages:
      script:
        - gem install jekyll
        - jekyll build -d public
      artifacts:
        paths:
        - public

From jenkins 3.4 onwards, the default template requires bundler.

    pages:
      script:
        - bundle install
        - bundle exec jekyll build -d public
      artifacts:
        paths:
        - public

But where did we specify that we are using ruby?

> the first thing GitLab Runner will look for in your `.gitlab-ci.yml` is a `Docker image` specifying what do you need in your container to run that script

So we should add `image: ruby:2.3` to the top of the file

#### Branching

Tell gitlab to only run the job called `pages` on the `master` branch

You do that with `only`:

    pages:
      script:
        - bundle install
        - bundle exec jekyll build -d public
      artifacts:
        paths:
        - public
      only:
      - master

#### Stages

> There are three default stages on GitLab CI: build, test, and deploy

To specify which stage your job is running, simply add another line to your CI: `stage`:

    pages:
      stage: deploy
      script:
        - bundle install
        - bundle exec jekyll build -d public
      artifacts:
        paths:
        - public
      only:
      - master

Stages are good because it lets you build and test before deploying.

You could tell gitlab to run the tests on every branch other than master:

Eg.

    image: ruby:2.3

    pages:
      stage: deploy
      script:
      - bundle install
      - bundle exec jekyll build -d public
      artifacts:
        paths:
        - public
      only:
      - master

    test:
      stage: test
      script:
      - bundle install
      - bundle exec jekyll build -d test
      artifacts:
        paths:
        - test
      except:
      - master

The test job is running on the stage `test`, Jekyll will build the site in a directory called `test`, and this job will affect all the branches except master.

> The best benefit of applying stages to different jobs is that every job in the same stage builds in parallel

#### Before Script

To avoid running the same script multiple times across your jobs, use `before_script`.
For example we run `bundle install` for both jobs.

    before_script:
      - bundle install

#### Caching Dependencies

To cache the installation files for your projects dependencies, for building faster, you can use the parameter `cache`

we’ll cache Jekyll dependencies in a `vendor` directory when we run `bundle install`

    cache:
      paths:
      - vendor/

    before_script:
      - bundle install --path vendor

The final `.gitlab-ci.yaml`:

    image: ruby:2.3

    cache:
      paths:
      - vendor/

    before_script:
      - bundle install --path vendor

    pages:
      stage: deploy
      script:
      - bundle exec jekyll build -d public
      artifacts:
        paths:
        - public
      only:
      - master

    test:
      stage: test
      script:
      - bundle exec jekyll build -d test
      artifacts:
        paths:
        - test
      except:
      - master

### Running with Docker

Docker, when used with GitLab CI, runs each job in a separate and isolated container using the predefined image that is set up in `.gitlab-ci.yml`.

> This makes it easier to have a simple and reproducible build environment that can also run on your workstation

#### Register a gitlab runner

To use the gitlab runner with docker you need to register a new runner to use the `docker` executor.

Eg.

    sudo gitlab-runner register \
    --url "https://gitlab.example.com/" \
    --registration-token "PROJECT_REGISTRATION_TOKEN" \
    --description "docker-ruby-2.1" \
    --executor "docker" \
    --docker-image ruby:2.1 \
    --docker-services postgres:latest \
    --docker-services mysql:latest

The registered runner will use the `ruby:2.1` image and will run 2 services 








## Sources

* [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/README.html)