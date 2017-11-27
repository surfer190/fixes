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

Displaying messags in the tempalte

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

