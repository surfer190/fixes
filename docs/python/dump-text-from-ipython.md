---
author: ''
category: Python
date: '2019-04-10'
summary: ''
title: Dump Text From Ipython
---
# How to Dump Text from iPython

So you have a very large variable that you want to put into a file from ipython

You can use `%store`

Then the variable and how to output:

* `>>`: append
* `>`: wipe and write

So either:

    %store <my_var> >><my_file>

or:

    %store <my_var> ><my_file>
    
### Example

    In [15]: %store soup >>vcloud.txt
    Writing 'soup' (BeautifulSoup) to file 'vcloud.txt'.

### Source

* [How to write the output of ipython command in python text file?](https://stackoverflow.com/questions/13199170/how-to-write-the-output-of-ipython-command-in-python-text-file)
