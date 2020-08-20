---
author: ''
category: Ruby
date: '2015-01-18'
summary: ''
title: Installing With Without Rdoc Ri
---
##Rails with / Without rdoc and ri

#### Make --no-ri --no-doc default for gem install

Add: `gem: --no-document`

To: `~/.gemrc`

#### Remove ri and rdoc of installed gems

`rm -R gem_env_dir/doc`

Source: 
[Stackoverflow](http://stackoverflow.com/questions/1381725/how-to-make-no-ri-no-rdoc-the-default-for-gem-install)
[Stackoverflow](http://stackoverflow.com/questions/2941005/how-to-remove-installed-ri-and-rdoc)
