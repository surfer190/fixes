# Sync from the upstream in your fork

Forking is a unique function of `github (and some others)` not `git`

It is basically creating your own version of another person's repo.

You should sync with the upstream repo frequently to ensure you have the latest version (and that someone else hasn't already fixed or added the feature/bug you are attempting to fix)

## How to Sync your Git Repo with the Upstream

1. Add a new remote (the original), for example:

    git remote add upstream git@github.com:hvac/hvac.git

2. Update your repo

    git pull upstream master --allow-unrelated-histories
    git push origin master



