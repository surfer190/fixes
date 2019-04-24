# Django Class Based Views

Remember that things with similar functionality and only slight differences can be reused by the use of classes in python, well we can do the same with django views.

* class `View`
* class`genericViews` - built on `view`


        from django.views.generic import view

Have the class extend `View`

        class HelloWorldView(View):
            def get(self, request):
                return HttpResponse("Hello World!")

Create a `get` method that takes `self` because it is an instance and `request` just like function based views

The `url` is a bit different as it must point to a callable (function) not a class

So we use `class.as_view()` which handles instanitating class

        url(r'^hello/$', views.HelloWorldView.as_view(), name='hello')

`as_view()` is a class method so it does not need an instance of a class to run, it creates the instance. Like setting up request and then runs `dispatch` method which runs the HTTP methods `get`

## TemplateView

There is also a `TemplateView` class

from django.views.generic import View, TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

### Override context data

        class NameView(TemplateView):
            template_name = 'name.html'
            
            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['name'] = 'hello'
                return context

### DetailView and ListView

Using defaults saves time

        from django.views.generic import ListView, DetailView

        class TeamListView(ListView):
            model = models.Team
            context_object_name = 'teams'

        class TeamDetailView(DetailView):
            model = models.Team

**Sticking with the defaults - speeds you up**

## CreateView, UpdateView, DeleteView

        from django.views.generic import (
            ListView, DetailView,
            CreateView, UpdateView, DeleteView
        )

Need to define `model` and `fields` for `CreateView`
Also add a `get_absolute_url` method to the model


#### Reverse Lazy

        from django.core.urlresolvers import reverse_lazy

So reverse lazy is ealuated when view is instantiated not when file is created
If view does not exist it does not matter

### Override queryset

You can set `queryset` variable in a class based view, but `queryset` is mutable so you must write `.all()` at end to get a fresh one

Best way is to override `get_query_set` method

So you can for example only delete a team if you are a superuser

        def get_queryset(self):
            if not self.request.user.is_superuser:
                return self.model.objects.filter(coach=self.request.user)
            return self.model.objects.all()

You can also change the intial data:

            def get_initial(self):
                intial = super().get_initial()
                initial['coach'] = self.request.user.pk
                return initial

[An Excellent resource to use to know the method is CCBV](https://ccbv.co.uk/)

## Combining class-based views

Example extending from both: `DetailView`, `UpdateView`

        class TeamDetailView(DetailView, UpdateView):
            model = models.Team
            fields = ('name', 'practice_location', 'coach')
            template_name = "teams/team_detail.html"

You should explicitly set `template_name` when combining, so django knows what is the template to use. Otherwise I think it takes the first.

Problem that sometimes happen is that the `super()` methods work left to right.
So the left class being extended is run first then right class.

`CreateView` looks for a object and `ListView` only has multiple objects.

Sometimes you can just reverse the order

## Mixins

Sometimes you need to override or manipulate a class

But to do it in many locations use a little repeatable class: `Mixins`

[check ccbv.co.za for docs on class based views and mixins](https://ccbv.co.uk/)

To enforce authentication use the [loginRequiredMixin](https://ccbv.co.uk/projects/Django/1.11/django.contrib.auth.mixins/LoginRequiredMixin/)

        from django.contrib.auth. import LoginRequiredMixin

Then inherit from in a class based view on the left:

        class TeamCreateView(LoginRequiredMixin, CreateView):
            ...

Then it will automatically redirect to the `accounts/login` page

[Read the Mixins in Class based views docs](https://docs.djangoproject.com/en/1.11/topics/class-based-views/mixins/)

[Django Braces](http://django-braces.readthedocs.io/en/latest/index.html)

### Creating a Custom Mixin

Create a file called `mixins.py`

Create the mixin class:

        class PageTitleMixin:
            page_title = ""

            def get_pagetitle(self):
                return self.page_title

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["page_title"] = self.get_pagetitle
                return context

Import it:

        from . import mixins

Extend from the mixin:

        class TeamCreateView(mixins.PageTitleMixin, CreateView):
            page_title = "Create a new team"

            def get_pagetitle(self):
                obj = self.get_object()
                return "Update {}".format(obj.name)

Now you can set the `page_title` in the class based view

