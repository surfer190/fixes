#How to Update Ruby Versions on Linux

##Find Available versions

`rbenv install --list`

##Install version

`rbenv install 2.1.5`

##Update `ruby-build` as an rbenv plugin

`cd ~/.rbenv/plugins/ruby-build`

`git pull`

##Set the ruby version to use globally

`rbenv global 2.1.5`

##Check ruby version

`ruby -v`

##Note: You need to Reinstall bundler for each version of Ruby you use

Sources: [makandracards](http://makandracards.com/makandra/25477-rbenv-how-to-update-list-of-available-ruby-versions-on-linux)
[digitalocean](https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-with-rbenv-on-debian-7-wheezy)