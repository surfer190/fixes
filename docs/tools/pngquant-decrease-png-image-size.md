---
author: ''
category: tools
date: '2022-11-23'
summary: ''
title: Pngquant compress images in place
---

##  Pngquant compress images in place

Convert images in place:

    pngquant --strip --verbose --force --ext .png --speed 2 *

Run pngquant recursively on subfolders:

Create a bash script `shrink_png.sh`:

    for file in `find /var/www/my_site/images/. -name '*.png'`; do
        pngquant --strip --verbose --speed 1 --force --ext '.png' $file
    done

## Sources

* [Systutorials: Pngquant](https://www.systutorials.com/docs/linux/man/1-pngquant/)
* [Coderwall: Run pngquant on subfolder](https://coderwall.com/p/zqi0jg/run-pngquant-on-subfolder)
