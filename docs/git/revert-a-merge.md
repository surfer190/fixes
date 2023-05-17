---
author: ''
category: git
date: '2023-05-15'
summary: ''
title: Revert a Merge
---

If you are in the middle of a merge - the merge has not been commited and there are merge conflicts that are being resolved.
The merge can be aborted with:

    git merge --abort

> Have not tried this

If you merge a branch into another, eg:

    git checkout integration
    git merge my-feature-branch

Then you check how it looks in git using `git log`:


    commit 02b1e83ee7c695d8227ba40a68c1c9ef8b7290ce (HEAD -> integration)
    Merge: 8d36df0 c0b893a
    Author: surfer190
    Date:   Mon May 15 11:12:29 2023 +0200

        Merge branch 'my-feature-branch' into integration

As you can see this commit has 2 parents:

    Merge: 8d36df0 c0b893a

if the form:

    Merge: parent1 parent2

If you scroll down in `git log` the 2 parent commits may be highlighted a different colour

In reverting a merge one cannot just do:

    git revert 02b1e83ee

The form:

    git revert <merge-commit>

An error wil arise:

    $ git revert 02b1e83e
    error: commit 02b1e83ee7c695d8227ba40a68c1c9ef8b7290ce is a merge but no -m option was given.
    fatal: revert failed

Soyou need to think about which parent the merge should revert to. In this case it is parent 1:

    git revert 02b1e83e -m 1

> This will revert the merge and write it to git history.

This is the case when the change has already been pushed to the remote.

If the merge has not been pushed to the remote yet, one can just reset the branch back to where it was with:

    git reset --hard origin/<branch-name>

or

    git reset --hard commit_sha

### History

There is some interesting history and explaination of this from Linus Torvalds: [git documentation: how to revert a faulty merge](https://github.com/git/git/blob/master/Documentation/howto/revert-a-faulty-merge.txt)

## Sources

* [How do I revert a merge commit that has already been pushed to remote?](https://stackoverflow.com/questions/7099833/how-do-i-revert-a-merge-commit-that-has-already-been-pushed-to-remote)
* [Undo a git merge that has not been pushed yet](https://stackoverflow.com/questions/2389361/undo-a-git-merge-that-hasnt-been-pushed-yet/6217372#6217372)