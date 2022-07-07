---
author: ''
category: Git
date: '2022-07-05'
summary: ''
title: Git Submodules
---

## Git Submodules

Submodules are a fairly simple and effective method for developing on several related but still separate projects simultaneously.

Scenario: Using another project within an existing git repo.

> You want to keep them seperate but still use one from the other

The issue with including the library is that it’s difficult to customize the library in any way and often more difficult to deploy it, because you need to make sure every client has that library available

Any custom changes you have made are difficult to merge when upstream changes become available.

> Git Submodules allow you to keep a Git repository as a subdirectory of another Git repository.

It lets you clone another repo into your project and keep commits seperate.

### Getting Started

To add a submodule:

    git submodule add <repo-url>

> By default, submodules will add the subproject into a directory named the same as the repository, in this case “DbConnector”.

Current status `git status` - will have a `.gitmodules` file.

    $ git status                                                                                                                                                                                                                       master
    On branch master
    Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
        new file:   .gitmodules
        new file:   mongo-python-driver

The `.gitmodules` file maps a folder to the repo:

    [submodule "mongo-python-driver"]
	path = mongo-python-driver
	url = git@github.com:mongodb/mongo-python-driver.git

> this file should be version controlled

Checking the diff of the project folder you will see:

    $ git diff --cached mongo-python-driver                                                                                                                                                                                            master
    diff --git a/mongo-python-driver b/mongo-python-driver
    new file mode 160000
    index 0000000..6d916d6
    --- /dev/null
    +++ b/mongo-python-driver
    @@ -0,0 +1 @@
    +Subproject commit 6d916d68c2db341847b46fabf961f3ad4ba045e4

Git does not track the submodule contents - when you are not in the directory. It sees it as a certain commit.

    git diff --cached --submodule

When you commit:

    $ git commit
    [master 0f0d52e] Add pymongo module
    2 files changed, 4 insertions(+)
    create mode 100644 .gitmodules
    create mode 160000 mongo-python-driver

Notice the special `160000` mode - means you are recording a commit as a directory entry rather than a subdirectory.

### Cloning a Project with Submodules

By default when you clone a repo with subdirectories - you get the directories but without the submodules.

    git clone git@github.com:lxqt/lxqt.git

There will be nothing in the folders...

You must run:

* `git submodule init` - to initialise local configuration file
* `git submodule update` - to fetch data and checkout to commit set in the superproject

There is a simpler way, use `--recurse-submodules`:

    git clone --recurse-submodules git@github.com:lxqt/lxqt.git

You can get all submodules from an existing repo with:

    git submodule update --init --recursive

### Working on a Project with Submodules

#### Pulling in Upstream Changes from the Submodule Remote

Go to the submodules directory and run:

    git fetch
    git merge

You can then check the diff:

    git diff --submodule

> you can set the `--submodule` flag as the default with `git config --global diff.submodule log`

There is also a one-liner for the above fetch and merge:

    git submodule update --remote

> The above defaults to the `master` branch

You can configure your submodule to track the `releases-0.14.x` branch for example:

    git config -f .gitmodules submodule.libfm-qt.branch releases-0.14.x 

Then run:

    git submodule update --remote libfm-qt 

> Better to use `-f .gitmodule` so that it is added to the repo and not just for your local working tree

You can see changes in submodules by setting for `git status`:

    git config status.submodulesummary 1

You can see the differing commits with `git diff` 

Better to be explicit and set the submodules to update when running:

    git submodule update --remote <submodule_to_update>

#### Pulling Upstream Changes from the Project Remote

From the perspective of a collaborator

A `git pull` is not enough.

By default, the git pull command recursively fetches submodules changes, as we can see in the output of the first command above. However, it does not update the submodules. 

You need to finalise the update with:

    git submodule update:

To be safe you should run `git submodule update --init --recursive`

> In case there is a new submodule or nested submodules

To simplify the above, run:

    git pull --recurse-submodules

Caveat: the url of a repo changes in `.gitmodules`:

    git submodule sync --recursive

#### Working on a Submodule

It’s quite likely that if you’re using submodules, you’re doing so because you really want to work on the code in the submodule at the same time as you’re working on the code in the main project.

Otherwise you would probably instead be using a simpler dependency management system (such as Maven, Rubygems or Pip).

> Git would get the changes and update the files in the subdirectory but will leave the sub-repository in what’s called a “detached HEAD” state - meaning there is no local branch tracking changes. So even if you commit the changes, the enxt time you run `git submodule update` your changes will be lost.

1. Go to your submodule and checkout a branch

    cd my-sub-module
    # list remote branches
    git branch -r
    git checkout 42dev

2. Merge in changes from the remote

    git submodule update --remote --merge

3. A change happens on remote branch and you update stuff in your local:

    git submodule update --remote --rebase

    > If you forget to say `--rebase` or `--merge`, git will update the submodule to whatever is on the server and reset your project to a detached HEAD state. If this happens you can simply go back into the directory and check out your branch again and then merge or rebase `origin/42dev`

#### Publishing Submodule Changes

We have not yet pushed our local changes to the remote.

> If we commit in the main project and push it up without pushing the submodule changes up as well, other people who try to check out our changes are going to be in trouble since they will have no way to get the submodule changes that are depended on. Those changes will only exist on our local copy.

You can ask Git to check that all your submodules have been pushed properly before pushing the main project:

    git push --recurse-submodules=check

> This push will fail if submodule changes haven't been pushed

From the message it will mention to either `cd` to each submodule directory and push - or use `git push --recure-submodules=ondemand`

#### Merging Submodule Changes

If you change a submodule reference at the same time as someone else, you may run into some problems.

That is, if the submodule histories have diverged and are committed to diverging branches in a superproject, it may take a bit of work for you to fix.

If one of the commits is a direct ancestor of the other (a fast-forward merge), then Git will simply choose the latter for the merge, so that works fine.

You will get a message like:

> warning: Failed to merge submodule my-sub-mod (merge following commits not found)

To solve the problem, you need to figure out what state the submodule should be in.

1. Use `git diff` to see the different commit SHA1's

    $ git diff
    diff --cc DbConnector
    index eb41d76,c771610..0000000
    --- a/DbConnector
    +++ b/DbConnector

2. Create a new branch and merge in the changes from the other commit

    cd DbConnector
    git rev-parse HEAD
    # eb41d764bccf88be77aced643c13a7fa86714135
    git branch try-merge c771610 # create branch from other commit
    git merge try-merge # merge branch into current branch

3. Resolve the conflict:

    1. First we resolve the conflict.
    2. Then we go back to the main project directory.
    3. We can check the SHA-1s again.
    4. Resolve the conflicted submodule entry.
    5. Commit our merge.

#### Submodule Tips

Foreach submodule stash work:

    git submodule foreach 'git stash'

Switch to new branch in all submodules:

    git submodule foreach 'git checkout -b featureA'

A diff for your main project and all sub projects:

    git diff; git submodule foreach 'git diff'

#### Set up aliases if you work on Submodules Alot

    git config alias.sdiff '!'"git diff && git submodule foreach 'git diff'"
    git config alias.spush 'push --recurse-submodules=on-demand'
    git config alias.supdate 'submodule update --remote --merge'

#### Issues with Submodules

Switching branches on older git versions (Older than 2.13) - after creating a new submodule - won't remove it.

Newer git fixes this by using:

    git checkout --recurse-submodules <branch name>

### Config changes

> A reminder that `git fetch` updates your remote-tracking branches never changing your local branches, git pull brings a local branch up to date with the remote version

In my `~/.gitconfig` I have:

    [status]
        submodulesummary = 1

    [submodule]
        recurse = 1

    [diff]
        submodule = log

    [push]
        recurseSubmodules = check

    [alias]
            sdiff = !git diff && git submodule foreach 'git diff'
            spush = push --recurse-submodules=on-demand
            supdate = submodule update --remote --merge

Read about the options in the [git config docs](https://git-scm.com/docs/git-config)

> It’s important to note that submodules these days keep all their Git data in the top project’s .git directory, so unlike much older versions of Git, destroying a submodule directory won’t lose any commits or branches that you had.

### Source

* [Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
* [git diffference between pull and fetch](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)
