---
author: ''
category: Ruby
date: '2015-05-10'
summary: ''
title: Create A Rails Api Quickly
---
# How to Create a Rails API quickly

1. `gem install rails-api`

2. `rails-api new myapi`

3. `rails g scaffold <NAME> fields...`

    eg. `rails g scaffold user email:string cell:string`

4. `rake db:migrate`

5. Test it out: `rails s`

    go to `http://localhost:3000/users`

    **Notice: Plural**

6. Add extra modules to Controllers. `rails-api` extends `APIController` so check in `BaseController` for extra modules you may want to include.

7. Slims down rack middleware stack. Current differences:

    ```
    use ActionDispatch::Cookies
    use ActionDispatch::Session::CookieStore
    use ActionDispatch::Flash
    use WebConsole::Middleware
    use Rack::MethodOverride
    use Rack::Sendfile
    ```

    So add the relevant lines above if you want session or cookies. Some modules depend on other modules so may need `Helpers` module as well.

    eg. in `Controller`:

    ```
    include ActionController::Cookies
    include ActionController::Helpers
    ```

**Optional:**

    * Create a page to create or manage users
    * `rails-api` doesn't allow showing views and hence this must be done in another app or in `/public.html`

    ```
    <!DOCTYPE html>
    <html>
      <head>
        <style type="text/css" media="screen">
          html, body{
            background-color: #4B7399;
            font-family: Verdana, Helvetica, Arial;
            font-size: 14px;
          }

          a { color: #0000FF; }

          #container {
            width: 75%;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px 40px;
            border: solid 1px black;
            margin-top: 20px;
          }
        </style>
        <script src="http://code.jquery.com/jquery-latest.min.js"
            type="text/javascript"></script>
        <script>
            $(function(){
              function addUser(user){
                $('#users').append('<li>' + user.email + ', ' +
                                            user.cell + ', ' + '</li>');
              }

              $('#new_user').submit(function(e){
                console.log('click');
                $.post('/users', $(this).serialize(), addUser);
                this.reset();
                e.preventDefault();
              });

              $.getJSON('/users', function(users){
                $.each(users, function(){ addUser(this)});
              });
          });
        </script>
      </head>
    <body>
      <div id="container">
        <h1>Add User</h1>
        <form id="new_user">
          <label for="email">Email</label>
          <input id="email" type="text" name="user[email]" id="user_email">
          <br/>
          <label for="cell">Cell</label>
          <input id="cell" type="text" name="user[cell]" id="user_cell">
          <br/>
          <input type="submit" name="Add">
        </form>
        <ul id="users"></ul>
      </div>
    </body>
    </html>```

**source: [Railscast rails-api gem](http://railscasts.com/episodes/348-the-rails-api-gem)**
