# Django Authentication

* **Authentication** is connecting crednetials to an incoming request. A person is who they say they are.
* **Authorization** is ensuring a user has permission to do what they want to do

## Decorators

Django provides [the `login_required` decorator](https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-login-required-decorator) but they are iffy with class-based views.

So for class based views, `django` provides mixins (small classes)

        from django.contrib.auth.mixins import LoginRequiredMixin

Thenadd as inherited from:

        class CreatePost(LoginRequiredMixin, generic.CreateView):
                ...


## Creating a Login View

Might be worth it to make an `accounts` app:

        ./manage.py startapp accounts

Then add to `INSTALLED_APPS`:

        `accounts`

For the actual view in `views.py`:

        class LoginView(generic.FormView):
            form_class = AuthenticationForm
            success_url = reverse_lazy("posts:all")
            template_name = "accounts/login.html"

            def get_form(self, form_class=None):
                if form_class is None:
                    form_class = self.get_form_class()
                return form_class(self.request, **self.get_form_kwargs())

            def form_valid(self, form):
                login(self.request, form.get_user())
                return super().form_valid(form)

In `urls.py`:

        urlpatterns = [
            url(r'^login/$', views.LoginView.as_view(), name="login"),
        ]

Add the template is `accounts/templates/accounts/login.html`:

        {% raw %}
        {% extends 'layout.html' %}

        {% load bootstrap3 %}

        {% block title_tag %}Login | {{ block.super }}{% endblock %}

        {% block body_content %}
        <div class="container">
            <h1>Login</h1>
            <form method="POST">
                {% csrf_token %}
                {% bootstrap_form form %}
                <input type="submit" lue="Login" class="btn btn-default">
            </form>
        </div>
        {% endblock %}
        {% endraw %}

## The Easier Way

Alas, there is an even easier way that uses the existing django auth

In `urlpatterns` for prject use:

        url(r'^accounts/', include("django.contrib.auth.urls"))

At `accounts/login` you will get the `TemplateDoesNotExist at /accounts/login/ - registration/login.html` error

So create that file in the project level templates with our exisitng template code

Now when you login it will go to `accounts/profile` if you don't have a template for this add a setting:

        LOGIN_REDIRECT_URL = "posts:all"

This can be a `url` or a `url name`

## Logout

Import logout:

        from django.contrib.auth import login, logout

Now we just want it to redirect after logout

Code:

        class LogoutView(generic.RedirectView):
            url = reverse_lazy('home')

            def get(self, request, *args, **kwargs):
                logout(request)
                return super().get(request, *args, **kwargs)

url:

    url(r'^logout/$', view.LogoutView.as_view(), name="logout"),

## Signing Up

Signing up is usually very site specific so there is no generic 

**signup view**:

        from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

        class SignupView(generic.CreateView):
            form_class = UserCreationForm
            success_url = reverse_lazy("login")
            template_name = "accounts/signup.html"

**template**:

        {% raw %}
        {% extends 'layout.html' %}

        {% load bootstrap3 %}

        {% block title_tag %}Signup | {{ block.super }}{% endblock %}

        {% block body_content %}
        <div class="container">
            <h1>Signup</h1>
            <form method="POST">
                {% csrf_token %}
                {% bootstrap_form form %}
                <input type="submit" lue="Signup" class="btn btn-default">
            </form>
        </div>
        {% endblock %}
        {% endraw %}


**url**:

        url(r'^signup/$', views.SignupView.as_view(), name="signup")

Make changes to default user create form in `forms.py`:

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

        class UserCreateForm(UserCreationForm):
            class Mate:
                fields = ['username', 'email', 'password1', 'password2']
                model = User

            def __init__(self, *args, **kwargs):
                super().__init__(self, *args, **kwargs)
                self.fields['username'].label = "Display Name" 
                self.fields['email'].label = "Email Address"

### Mailed Activation

There is a good library that works on the wprkflow of your app

Specifically sending activation email etc.

Check it out at [django-registration](https://django-registration.readthedocs.io/en/2.1.2/)

## Autologin after registration

        class SignUp(generic.CreateView):
            form_class = forms.UserCreateForm
            template_name = 'accounts/signup.html'
            success_url = reverse_lazy('products:list')

            def form_valid(self, form):
                res = super().form_valid(form)
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                if user is not None:
                    if user.is_active:
                        login(self.request, user)
                return res

## Password Reset

Django has built-in except the tmeplates look like django admin

So to change that template you can override it at `<root_templates>/registration/password_reset_form.html`

Then to change the email template change: `<root_templates>/registration/password_reset_done.html`

Then the password reset page: `<root_templates>/registration/password_reset_confirm.html`

Update password reset complete: `<root_templates>/registration/password_reset_complete.html`

To catch the email during development use: the [Django debug bar mail panel](https://github.com/scuml/django-mail-panel)

## Customising Users

* Create a custom model that has a 1-to-1 relationship with Django's `User` model - extra non-critical data
* Extend the abstract `User` model in an absract form
* Replace the User model and extend `AbstractBaseUser`

### Replacing the existing user model


        from django.contrib.auth.models import (
            AbstractBaseUser, 
            BaseUserManager, 
            PermissionsMixin
        )
        from django.db import models
        from django.utils import timezone


        class UserManager(BaseUserManager):
            def create_user(self, email, username, display_name=None, password=None):
                if not email:
                    raise ValueError("Users must have an email address")
                if not display_name:
                    display_name = username

                user = self.model(
                    email=self.normalize_email(email),
                    username=username,
                    display_name=display_name
                )
                user.set_password(password)
                user.save()
                return user

            def create_super_user(self, email, username, display_name, password):
                '''Create a custom super user
                mainly run through the commandline
                '''
                user = self.create_user(email, username, display_name, password)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                return user



Also create the actual `User` class with:

        class User(AbstractBaseUser, PermissionsMixin):
            email = models.EmailField(unique=True)
            username = models.Charfield(max_length=40, unique=True)
            display_name = models.CharField(max_length=140)
            bio = models.CharField(max_length=140, blank=True, default="")
            avatar = models.ImageField(blank=True, null=True)
            date_joined = models.DateTimeField(default=timezone.now)
            is_active = models.BooleanField(default=True)
            is_staff = models.BooleanField(default=False)

            # So calling User.object.all()
            objects = UserManager()

            # Unique identifier to search user
            USERNAME_FIELD = 'email'

            REQUIRED_FIELDS = ['display_name', 'username']

            def __str__(self):
                return "@{}".format(self.username)

            def get_short_name(self):
                return self.display_name

            def get_long_name(self):
                return "{} @({})".format(display_name, username)

You need to tell django in `settings.py` what User mdoel to use:

        # Tells django what model to use for the user model
        AUTH_USER_MODEL = "accounts.user"

Then in related models user use this instead of normal `User` from `django.contrb.auth.models`:

        from django.conf import settings

        settings.AUTH_USER_MODEL

In other places where you need the actual model:

        from django.contrib.auth import get_user_model

        get_user_model()


## Permissions

For every new Non-Abstract model you create with django, it creates a content_type instance.
Stores model and model_name. So you can link to model without knowing where it is defined.

Add, Change, delete permissions

Permissions are about models, not the instances. So user does not have permission for objects just belonging to them.

Groups can also be used to clumping together permissions

### Adding a permission

In a model add to `class Meta:`

        permissions = (
            ('ban_member', 'Can ban members'),
        )

**When you add a permission you need to migrate, as adds to permissions table**

Check if a user has a permission:

    if self.request.user.has_perm("products.can_give_discount")

So it uses `model plural name` + `permission_name`

### Creating groups

from django.contrib.auth.models import (
    Permission,
    Group
)

new_group, group = Group.objects.get_or_create(name="Editors")

### Creating permissions

content_type = ContentType.objects.get_for_model(models.Product)
permission = Permission.objects.get_or_create(
    codename='can_give_discount',
    name='Can Give Discount',
    content_type=content_type
)

group.permissions.add(permission)

user.groups.add(group)