## Fetch and Track all remote Branches

```
for remote in `git branch -r`; do git branch --track $remote; done
git fetch --all
git pull --all
```

[Source](http://stackoverflow.com/questions/10312521/how-to-fetch-all-git-branches)
