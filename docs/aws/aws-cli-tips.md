---
author: ''
category: AWS
date: '2022-07-25'
summary: ''
title: Aws Cli Tips
---

### View your Identity

    $ aws sts get-caller-identity
    {
        "UserId": "AROAXXXXXXX:i-065fb72xxxxxxx",
        "Account": "4xxxxxxx",
        "Arn": "arn:aws:sts::4xxxxxxx:assumed-role/all-services.fixes.dev-ec2-role/i-065fb72xxxxxx"
    }

### Generate a Kubeconfig

    aws eks update-kubeconfig --name my-qa-env --alias qa --profile my-aws-cli-profile

This will create your `~/.kube/config` file
