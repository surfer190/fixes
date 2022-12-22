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
    
## Decrease Journal Size

If you run this and see references to the `journal`

    /var/log/journal/8cbcddca1a876f4a6d2ebcc457e51618/system@25b4ea9a10124cd8b35f78511812b1a0-0000000000190463-0005e78573829d9f.journal
    /var/log/journal/8cbcddca1a876f4a6d2ebcc457e51618/system@25b4ea9a10124cd8b35f78511812b1a0-0000000000159198-0005e693197fe378.journal
    /var/log/journal/8cbcddca1a876f4a6d2ebcc457e51618/system@25b4ea9a10124cd8b35f78511812b1a0-000000000024db2f-0005eaccaa503be5.journal
    /var/log/journal/8cbcddca1a876f4a6d2ebcc457e51618/system@25b4ea9a10124cd8b35f78511812b1a0-00000000001749f2-0005e7050be16d57.journal
    ....

Systemd might be using a lot of space.

Check and decrease the size with:

    sudo journalctl --disk-usage
    sudo journalctl --vacuum-size=128M
    sudo journalctl --verify

## Decrease Git Repo Size

From time to timea git repo may gather a lot of garbage

If you have an entry like this in the above:

    /var/www/my_site/.git/objects/pack/pack-b6a7cb4684eaeab4006353c0381fb26decc72759.pack

You might want to go garbage collection:

    cd /var/www/my_site
    git gc

### Source

* [Finding All Large Files](https://unix.stackexchange.com/questions/140367/finding-all-large-files-in-the-root-filesystem)
* [Find largest files in a directory](https://www.cyberciti.biz/faq/how-do-i-find-the-largest-filesdirectories-on-a-linuxunixbsd-filesystem/)
* [How to reduce the amount of disk space used by the systemd journal](https://www.noulakaz.net/2017/10/06/how-to-reduce-the-amount-of-disk-space-used-by-the-systemd-journal/)