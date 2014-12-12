#How to Update Ruby on Rails on Linux

##Check Installed Ruby Gems Package Manager Version

`gem -v`

##Update [RubyGems](https://rubygems.org/gems/rubygems-update)

`gem update --system`

##List outdated gems

`gem outdated`

##Update stale gems

`gem update`

##Update Rails Project Basis

Rails updates on a project basis should specify the version in the `GemFile`:

```source 'https://rubygems.org'
gem 'rails', '4.1.9'```

`bundle update rails`

##Rails Update global

`gem install rails --no-ri --no-rdoc`

##Check rails version

`rails -v`

Source: [http://railsapps.github.io/](http://railsapps.github.io/updating-rails.html)
[stackoverflow](http://stackoverflow.com/questions/21364283/gemremotefetcherunknownhosterror-while-installing-rails-version-3-2-15)