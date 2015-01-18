#Common Issues on Initial Setup

1. `bundle install`
2. Set the database username and password
3. `bundle exec rake db:create db:migrate`

#Secret Key Base for Environment

`<%= ENV["SECRET_KEY_BASE"] %>`

You need to set the variable in the unix environment 

In `~/.bashrc`

`SECRET_KEY_BASE="TH3S3Cr3tK3Y"; export SECRET_KEY_BASE;`

#Database password in Production is also an environment issue

#For The Asset Pipeline in Production

In `config/environments/production.rb`:
```
config.assets.compile = true
config.assets.precompile =  ['*.js', '*.css', '*.css.erb']
```


