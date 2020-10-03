# Fixes

Summaries, Fixes, Solutions and Notes

[fixes.co.za](http://fixes.co.za)

[![Build Status](http://37.139.28.74:8080/buildStatus/icon?job=fixes+mkdocs)](http://37.139.28.74:8080/job/fixes%20mkdocs/)

Common problems and solutions, fixes and tips that I have gathered while trying to solve problems.

Keeping a reference of common development problems and solutions I have come across to help others to be more efficient in problem solving.

### Where to view Fixes

The whole collection of fixes can be viewed with your web browser at:
[http://fixes.co.za](http://fixes.co.za)

The site is built with [mkdocs](https://www.mkdocs.org/) and is updated on a post-receive hook to this repo

### Create / Update the index page

    source env/bin/activate

    python update_index.py

Install a `pre-commit` hook:

    sudo vim ./fixes/.git/hooks/pre-commit

and write:

    #!/bin/sh
    source ./env/bin/activate && python update_index.py

