---
author: ''
category: Linux
date: '2019-08-27'
summary: ''
title: Find Large Files
---
# Find Large Files

Look at the top folders and files in current directory

    du -hsx * | sort -rh | head -10

> Go to `/var`, `/opt` and `~` to try the above

When your VM has run out of space 

    find / -xdev -type f -size +100M

### Source

* [Finding All Large Files](https://unix.stackexchange.com/questions/140367/finding-all-large-files-in-the-root-filesystem)
* [Find largest files in a directory](https://www.cyberciti.biz/faq/how-do-i-find-the-largest-filesdirectories-on-a-linuxunixbsd-filesystem/)
