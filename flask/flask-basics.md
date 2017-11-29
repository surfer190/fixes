# Flask Basics

The `app` receives all the requests. The requests are sent to the correct function or `view`.
The function/view is found through the `route`.

## Installing Flask

        pip install flask

## Simple App

        from flask import Flask

Now we need an app instance and we want it named the same as the current namespace

        app = Flask(__name__)

This means use whatever our current namespace is.
Run the app and set `debug=True` so it auto refreshes

        app.run(debug=True)

You can run the site now with

        python simple_app.py

But you will get a `404` as there is no route

Routes should be defined before `app.run()`

### Creating a Route

A route is a function and a routing decorator directive

        @app.route('/')
        def index():
            return "Hello from treehouse"

#### URL Parameters

If you want to add parameters to the route you need the `request` object

        from flask import request

It is a global object, so it is always available but python neckbeards hate it.
The function is given a default and the `name` is acquired with `request.args.get('name', name)`

        @app.route('/')
        def index(name="surfer190"):
            name = request.args.get('name', name)
            return f'Hello from { name }'

### Neat Routes

Views can have more than 1 route

        @app.route('/<name>')

This acquired the name parameter and the `request.args.get()` is no longer required

You can even specify the data type in the route.
If a different data type is given the route will `404`:

        @app.route('/add/<int:num1>/<int:num2>')
        def add(num1, num2):
            return '{} + {} = {}'.format(num1, num2, num1 + num2)

You need to return a stirng, you cannot return a string.

If you want to accept both `int` and `float` use multiple routes:

        @app.route('/add/<float:num1>/<float:num2>')
        @app.route('/add/<int:num1>/<int:num2>')
        @app.route('/add/<int:num1>/<float:num2>')
        @app.route('/add/<float:num1>/<int:num2>')
        def add(num1, num2):
            return '{} + {} = {}'.format(num1, num2, num1 + num2)

## Templates

You can render html with a multiline string:

        def add(num1, num2):
            return '''
            <!doctype html>
            <html>
            <head><title>Adding!</title></head>
            <body>
            <h1>{} + {} = {}</h1>
            </body>
            </html>
            '''.format(num1, num2, num1 + num2)

But the better way is use `templates`

1. Create a `templates` folder

2. Add the template file `base.html`:

        <!doctype html>
        <html>
            <head>
                <title>Adding!</title>
            </head>
            <body>
                <h1>Num1 + Num2 = Sum-thing</h1>
            </body>
        </html>

3. Import `render_template` from `flask`

        from flask import render_template

4. In your `view function`

        return render_template('base.html')

Flask uses [jinja2](http://jinja.pocoo.org/docs/2.10/) to template and in jinja2 you print variables with `{{ }}`.Ensure that the view is passed the variable in `render_template`.

        def add(num1, num2):
            return render_template('add.html', num1=num1, num2=num2)

We can also use `**` to unpack a `context` dictionary

        def add(num1, num2):
            context = {'num1': num1, 'num2': num2}
            return render_template('add.html', **context)

## Template Inheritance

Removes duplicate html and makes use of `blocks` that can be swapped out

Create a `layout.html` file in `templates`, copy generic code and add blocks for changable context:

        {% block content %}
        {% endblock %}

To use it in other template files you need to `extend`:

        {% extends 'layout.html' %}

To add the content from the parent block use the `super()` function in the block

## Static Files

Static files like images, js and css are stored in the `static` directory

You can then reference the file with `/static/*`

        <link rel="stylesheet" href="/static/styles.css">

## Forms

There are many libraries available for making forms.

You can set a route only applicable to certain methods

        @app.route('/save', methods=['POST'])

Then set the url of the form:

        <form action="{{ url_for('save') }}" method="POST">

### Redirect

To redirect import `url_for` and `redirect` from `flask`

        return redirect(url_for('index'))

### Form Data

When posting to a url the `request` has a `form` attribute 

### Cookies

Cookies are good for when you don't have a database and don't want to use javascript local storage.

In `flask` cookies are set on the response, which you don't have access to until after the `return`.
So you have to fake the response with `make_response`

        response = make_response(redirect(url_for('index')))
            return response

To set the cookie as a json object of the form data use:

        response.set_cookie('character', json.dumps(dict(request.form.items())))

> Remember `json.dumps()` stands for `dump string`

#### Retrieval

        request.cookies.get('character')

## Flash Messages

        from flask import flash

Use the user's session, for that you need a `secret_key`

        app.secret_key = 'KJHSADOABSLKDNknkjsfhoi768HDIu76'

Setting flash message inthe view

        flash("Saved changes!")

Can set a category:

        flash("Yay! you registered", "success")

Displaying messags in the template

        <div class="wrap no-bottom messages">
            {% with messages = get_flashed_messages() %}
                {% if messages %}
                <ul class="flashes">
                    {% for message in messages %}
                    <li>{{ message }}</li>
                    {% endfor %}
                </ul>
                {% endif %}
            {% endwith %}
        </div>

> Remember flashes only happen once (persist till next time page is viewed)

## Database

Connecting to and disconnecting from the db responsibility.

We can run certain things before and after a request.
With decorators `@app.before_request`

> Remember the function for `@app.after_request` takes in a response object

### The Global object

`g` is a global object that gets passed around.
We can use to set up things we want available everywhere.

        from flask import g

Then you can set the database:

    @app.before_request
    def before_request():
        '''Connect to the database before each request'''
        g.db = models.DATABASE
        g.db.connect()

and close the database after:

    @app.after_request
    def after_request(response):
        '''Close the database connection after each request'''
        g.db.close()
        return response

### Run the app

    if __name__ == '__main__':
        app.run(debug=DEBUG)

## Login

To get the login sorted you need the `LoginManager`

        from flask_login import LoginManager

You also need to enable sessions so you need the `secret_key`

        app.secret_key = 'djkh7dhYYGSHhhsbjdyd'

You need to create the login mnager and initilaise the app and give it the view t redirect anonymous users to:

        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = 'login'

Add the `user_loader` method:

        @login_manager.user_loader
        def load_user(userid):
            try:
                return models.User.get(models.User.id == userid)
            except models.DoesNotExist:
                return None

## Forms

Forms are all about validation and a bit about display

The defactor package is `flask_wtf` build on `wtforms`

    pip install flask-wtf

Example form with validation

        from flask_wtf import Form
        from wtforms import StringField, PasswordField
        from wtforms.validators import (
            DataRequired, Email, Regexp, ValidationError
            Length, EqualTo)   

        from models import User

        def name_exists(form, field):
            if User.select().where(User.username == field.data).exists():
                raise ValidationError('Username already exists')

        def email_exists(form, field):
            if User.select().where(User.email == field.data).exists():
                raise ValidationError('Email already exists')

        class RegisterForm(Form):
            username = StringField(
                'Username',
                validators=[
                    DataRequired(),
                    Regexp(
                        r'^[a-zA-Z0-9_]+$',
                        messsage=("Username should be one word; letters, "
                                "numbers or underscores only")
                    ),
                    name_exists
                ]
            )
            email = StringField(
                'Email',
                validators=[
                    DataRequired(),
                    Email(),
                    email_exists
                ]
            )
            password = PasswordField(
                'Password',
                validators=[
                    DataRequired(),
                    Length(min=2),
                    EqualTo('password2', message='Passwords must match'),
                ]
            )
            password2 = PasswordField(
                'Confirm Password',
                validators=[
                    DataRequired()
                ]
            )

### Handling forms in the view

        @app.route('/register', methods=('GET', 'POST',))
        def register():
            form = forms.RegisterForm()
            if form.validate_on_submit():
                flash("Yay! you registered", "success")
                models.User.create_user(
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data
                )
                return redirect(url_for('index'))
            return render_template('register.html', form=form)

### Showing the view

        <form method="POST" action="" class="form">
            {{ form.hidden_tag() }}
            {% for field in form %}
                <div class="field">
                    {% if field.errors %}
                        {% for error in field.errors %}
                            <div class="notification error">{{ error }}</div>
                        {% endfor %}
                    {% endif %}
                    {{ field(placeholder=field.label.text) }}
                </div>
        </form>

### Macros

Macros are pieces of reusabel tremplate code

Create the macro in `templates/macros.html`:

        {% macro render_field(field) %}
        <div class="field">
            {% if field.errors %}
                {% for error in field.errors %}
                    <div class="notification error">{{ error }}</div>
                {% endfor %}
            {% endif %}
            {{ field(placeholder=field.label.text) }}
        </div>
        {% endmacro %}

Then use the macro with:

{% from 'macros.html' import render_field %}

<form method="POST" action="" class="form">
    {{ form.hidden_tag() }}
    {% for field in form %}
        {{ render_field(field) }}
    {% endfor %}
</form>

## Template Layout

Setting variables for flash messages:

        {% with messages = get_flashed_messages(with_categories=True) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="notification {{ category }}">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

Checking logged in:

        <!-- Log in/Log out -->
        {% if current_user.is_authenticated() %}
        <a href="{{ url_for('logout') }}" class="icon-power" title="Log out"></a>
        {% else %}
        <a href="{{ url_for('login') }}" class="icon-power" title="Log in"></a>
        <a href="{{ url_for('register') }}" class="icon-profile" title="Register"></a>
        {% endif %}

## Returning a 404

To return a 404 we need `abort`

        from flask import abort

Usage:

        abort(404)

### Setting a custom404 page

        @app.errorhandler(404)
        def not_found(error):
            return render_template('404.html'), 404

