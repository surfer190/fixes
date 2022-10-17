---
author: ''
category: AWS
date: '2022-10-01'
summary: ''
title: AWS Codebuild
---

## What is AWS Codebuild?

* fully managed build service
* compiles your source code
* runs unit tests
* produces artifacts that are ready to deploy
* No need to provision, manage and scale your own servers
* Pre-packlaged build environments for Apache Maven, Gradle

## How to run CodeBuild?

* AWS Management console (Web frontend)
* AWS cli
* AWS sdk (boto)
* AWS code pipeline (a seperate service)

## How Codebuild works?

1. A _build project_ is required:

    * where to get source code
    * environment to use
    * build commands to run
    * where to store build output
2. From the _build project_ a _build environment_ is created
3. CodeBuild downloads the source code into the build environment and then uses the yaml build specification (_buildspec_). [Build spec reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html).
4. If there is any build output, the build environment uploads its output to an S3 bucket. Other tasks like notifications from the spec are run.
5. Logs from the build are sent to cloud watch.

## Getting Started

### Buildspec

A buildspec is a collection of build commands and related settings, in YAML format, that CodeBuild uses to run a build.
Create a file `buildspec.yml` and save it in the root directory. 

    version: 0.2

    phases:
      install:
        runtime-versions:
        java: corretto11
      pre_build:
        commands:
        - echo Nothing to do in the pre_build phase...
      build:
        commands:
        - echo Build started on `date`
        - mvn install
      post_build:
        commands:
        - echo Build completed on `date`
    
    artifacts:
      files:
        - target/messageUtil-1.0.jar

> Instead of including a build spec file in your source code, you can declare build commands separately when you create a build project. Stored on the buildproject.

* `version` represents the version of the build spec standard being used.
* `phases` represents the build phases during which you can instruct CodeBuild to run commands: `install`, `pre_build`, `build`, and `post_build`
* `artifacts` represents the set of build output artifacts that CodeBuild uploads to the output bucket

### Build Environment

A build environment represents a combination of operating system, programming language runtime, and tools that CodeBuild uses to run a build.

![AWS CodeBuild project components](/img/aws/codebuild-project-components.png){: class="img-fluid" }

A build project is made up of:

* project configuration
* source
* environment
* buildspec
* batch configuration
* artifacts
* logs

### Summarised Build Information

The build statuses:

* SUBMITTED
* QUEUED
* PROVISIONING
* DOWNLOAD_SOURCE
* INSTALL
* PRE_BUILD
* BUILD
* POST_BUILD
* UPLOAD_ARTIFACTS
* FINALIZING
* COMPLETED

### Detailed Build Information

To protect sensitive information, the following are hidden in CodeBuild logs:

* AWS access key IDs.
* Strings specified using the Parameter Store.
* Strings specified using AWS Secrets Manager.

Click `Build logs`

### CodeBuild CLI

#### Creating a Build project

    aws codebuild create-project --generate-cli-skeleton

or

    aws codebuild create-project --cli-input-json file://create-project.json

> But why would you...

#### Running a Build Project

    aws codebuild start-build --project-name project-name

#### View summarised build info

    aws codebuild batch-get-builds --ids id

#### List Build Projects

    aws codebuild list-projects --sort-by sort-by --sort-order sort-order --next-token next-token

#### View a build's details

    aws codebuild batch-get-projects --names names

## Samples

There are a number of [samples of CodeBuilds on AWS](https://docs.aws.amazon.com/codebuild/latest/userguide/use-case-based-samples.html)

## Plan a build in AWS CodeBuild

Answer these questions

1. Where is the source code stored? Github, Bitbucket, S3, Codecommit, Gitlab
2. Which build commands do you need to run and in what order? tests, notifications...
3. Which runtimes and tools do you need to run the build? docker to create an image, if project is compiled need the compiler
4. Do you need AWS resources that aren't provided automatically by CodeBuild? What policies?
5. Do you want CodeBuild to work with your VPC?

### Buildspec Syntax

```
version: 0.2

run-as: Linux-user-name

env:
  shell: shell-tag
  variables:
    key: "value"
    key: "value"
  parameter-store:
    key: "value"
    key: "value"
  exported-variables:
    - variable
    - variable
  secrets-manager:
    key: secret-id:json-key:version-stage:version-id
  git-credential-helper: no | yes

proxy:
  upload-artifacts: no | yes
  logs: no | yes

batch:
  fast-fail: false | true
  # build-list:
  # build-matrix:
  # build-graph:
        
phases:
  install:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    runtime-versions:
      runtime: version
      runtime: version
    commands:
      - command
      - command
    finally:
      - command
      - command
  pre_build:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
  build:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
  post_build:
    run-as: Linux-user-name
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
reports:
  report-group-name-or-arn:
    files:
      - location
      - location
    base-directory: location
    discard-paths: no | yes
    file-format: report-format
artifacts:
  files:
    - location
    - location
  name: artifact-name
  discard-paths: no | yes
  base-directory: location
  exclude-paths: excluded paths
  enable-symlinks: no | yes
  s3-prefix: prefix
  secondary-artifacts:
    artifactIdentifier:
      files:
        - location
        - location
      name: secondary-artifact-name
      discard-paths: no | yes
      base-directory: location
    artifactIdentifier:
      files:
        - location
        - location
      discard-paths: no | yes
      base-directory: location
cache:
  paths:
    - path
    - path
```

* `version`: Recommended `0.2`
* `run-as`: Linux user to run build as (default is `root`)
* `env`: environment shells, variables, aws parameter stores and aws secret manager
* `proxy`: If using a proxy server
* `phases`: required commands for each phase
    * `install`: installing packages required for the build
    * `pre_build` - run before the build
    * `build` - commands during the build
    * `post_build` - commands to run after the build
    * `on-failure`: action to take if command fails: `ABORT` or `CONTINUE`
    * `finally`: run once other commands complete
* `reports`
    * `report-group-name-or-arn` - Specifies the report group that the reports are sent to
        * `files` - locations that contain the raw data of test results generated by the report
        * `file-format` - report file format.. Default is `JUNITXML`. Others: `CUCUMBERJSON`, `NUNITXML`, `TESTNGXML`. For coverage: `CLOVERXML`, `COBERTURAXML`, `SIMPLECOV`
* `artifacts` - build output
* `cache` - where codebuild can prepare files for uploading cache

### Testing

You can run a [codebuild build locally](https://docs.aws.amazon.com/codebuild/latest/userguide/use-codebuild-agent.html) with the codebuild agent

## Working with build projects

### Build Trigger

On the `Build triggers` tab

### Webhook build trigger from Github

This is set under `Build Details`

Event types: `PUSH`, `PULL_REQUEST_CREATED`, `PULL_REQUEST_UPDATED`, `PULL_REQUEST_REOPENED`, and `PULL_REQUEST_MERGED`

...Other stuff in the docs

## Test Reporting

### Example Pytest

```
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.7
    commands:
      - pip3 install pytest
  build:
    commands:
      - python -m pytest --junitxml=<test report directory>/<report filename>

reports:
  pytest_reports:
    files:
      - <report filename>
    base-directory: <test report directory>
    file-format: JUNITXML
```

## Coverage Report

Supported formats:

* JaCoCo XML
* SimpleCov JSON
* Clover XML
* Cobertura XML

Ensure you export your coverage report

    python -m coverage xml

The creates a [`coverage.xml`](https://coverage.readthedocs.io/en/6.5.0/cmd.html#cmd-xml) file in a format compatible with [cobertura](https://cobertura.github.io/cobertura/)

```
reports:
  coverage-report:
    files:
      - 'test-results/coverage.xml'
    file-format: 'COBERTURAXML'
```

### Other topics

* [Logging and Monitoring](https://docs.aws.amazon.com/codebuild/latest/userguide/logging-monitoring.html)
* [Security](https://docs.aws.amazon.com/codebuild/latest/userguide/security.html)
* [Advanced](https://docs.aws.amazon.com/codebuild/latest/userguide/advanced-topics.html)

## Source

* [AWS CodeBuild Userguide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
