# Git: Find which commit removed a certain line of code

## Usage

```
git log -c -S'<line you noticed changed>' <filename>
```

Example:

```
git log -c -S'``django_jenkins.tasks.run_jshint``' README.rst
```

Source: [Stackoverflow: git find when a line was deleted](http://stackoverflow.com/questions/12591247/find-when-line-was-deleted)
