# Gitlab Runners

For a seemingly simple concept, gitlab runners are made to seem very complex espescially when aided by the constant redirection in the gitlab docs.

Let's try and simplify the concept.

## Disambiguation

Terms:

\* gitlab instance - this is where you host your projects and version control history
* gitlab groups - like github organisations, groups can own projects, userc can be members of groups.

Gitlab runner:

\* A worker machine that executes your project's GitLab CI jobs
* Different runners have different capabilities
* Tag runners and give jobs tags to match them up

A runner can be:

\* `specific` - to a chosen project
* `group` - available to all projects in a group
* `shared` - available to every project

A gitlab runner can also be seen as a service responsible for executing jobs and reporting their progress.
It can execute the job on the same machine or a different machine. The machine might be launched on the fly in response to job submission.

## Gitlab Runner Info

When installed a gitlab runner generally runs as a long-running background service.

YOu can check the status with:

    sudo gitlab-runner status

## Registration

There is a registration process for runners.

> They continually poll a GitLab instance for jobs that match their tags, execute them, and communicate the progress and results back

> Runners must be added incrementally with gitlab-runner register, which takes a registration token and exchanges it with the GitLab instance for a runner token that is stored in the configuration file

The registration token:

\* tells your GitLab Runner which GitLab instance to ask for jobs
* tells your GitLab instance that it is allowed to assign your jobs to your GitLab Runner

> Where to find the token you need depends on the type of Runner you want to register: shared, specific (project), or group

## Executors

Each Runner is configured with its own executor that defines how it executes jobs

* `shell executor` - executes jobs on the same machine as the Runner
* `ssh executor` - execute jobs on an existing remote machine
* `docker+machine executor` - uses docker machine to launch cloud instances and execute jobs on those instances

With a fleet of runners it is important to assign tags for: size speed, OS and dependencies


### Sources

* [Understanding GitLab Runner](https://jfreeman.dev/blog/2019/03/22/understanding-gitlab-runner/)
* [How to set up GitLab Runner on DigitalOcean ](https://about.gitlab.com/blog/2016/04/19/how-to-set-up-gitlab-runner-on-digitalocean/)
