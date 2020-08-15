---
author: ''
category: Git
date: '2017-02-23'
summary: ''
title: Git Commands
---
# Git Hub Shell Commands 

### Reverting branch to a previous commit to delete all (ie. wiping everything after a commit)
    git reset --hard <SHA>
    git push origin master -f

### Reverting a single erroneous commit and keeping all others before and after
Basically undoes everything in that commit and commits as a new commit.   
Example, you have commits A,B,C,D. You **only** want to get rid of C but can't revert the entire branch to D and lose commits AB.
```
git revert <SHA>
git push origin master
```

### Delete untracked files

    git clean -f -d

> or

    git checkout --

###Search for commit message
```
git log --grep=<pattern>
```

###Reset head to a specific branch

> Helpful when you performing a merge and want to reset branch to repo

```
git fetch origin
git reset --hard origin/staging
```

###Reset master branch to the full contents on another branch

> Use the ours merging strategy

```
git checkout master
git pull origin master
git checkout staging
git pull origin staging
git merge -s ours master
git checkout master
git merge staging
```

### Tag an old commit

```
git tag -a <version tag> <commit hash> -m "<message>"
git tag -a v1.2 9fceb02 -m "Message here"
```
