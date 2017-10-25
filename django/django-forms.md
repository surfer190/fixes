# Django Forms

* Help us quickly generate html to represent a form with special widgets
* let us validate data
* model forms create forms based on data and create/update

## Setting Up

Create a `forms.py` file

Forms are a class

Inherit from `forms.Form`

        class SuggestionForm(forms.Form):

Elements made in a similar way to models

        name = forms.CharField()
        email = forms.EmailField()
        suggestion = forms.CharField(widget=forms.Textarea)

## Validating a form

* Validate as a whole - validate two or more fields in relation to each other. Like either or both.
* validate individual fields - custom cleaning methods for complicated things
* validate using django's built in validators - take a value and return a specific error if value is wrong

## A honeypot field

Used to catch bots

        honeypot = forms.CharField(widget=forms.HiddenInput, required=False)

### The clean method

You can define a `clean_x` method in your form class which is repsonsible for cleaning and validating the data. 
Problem is it is not abstracted, it can't be used for many forms.

        def clean_honeypot(self):
                honeypot = self.cleaned_data['honeypot']        
                if len(honeypot):
                raise forms.ValidationError(
                        "honeypot should be left empty. Bad bot!"
                )
                return honeypot

### Utilising Validators

You can set the `validators` field to a form field

        honeypot = forms.CharField( required=False, 
                                widget=forms.HiddenInput,
                                label="Leave empty",
                                validators=[validators.MaxLengthValidator(0)]
                               )

## You can define a custom validator

Add a method to the file called `must_be_empty` that takes the field `value` as an argument

To use it just add it to the `validators` field

The validators must be unquoted - they are functions in the file, not strings

## Multi-value validation

Sometimes you need to validate 2 or more values as a combination.

Use the `clean` method without a field name:

        def clean(self):
                cleaned_data = super().clean()
                email = cleaned_data['email'] # or .get('email')
                verify = cleaned_data['verify_email']

                if email != verify:
                raise forms.ValidationError(
                        "You need to enter the same email in both fields"
                )

## Related Fields

Say you have a related field on the model:

        company = models.ForeignKey('projects.Company', on_delete=models.PROTECT)

when you fill out the `ModelForm` for that model the company field will have different states.

        >>>> form.data['company']
        1

Only the `cleaned_data` actually gives you back the related object

        >>>> form.cleaned_data['company']
        <Company: Default Company>

When assigning the foreign key with kwargs you can use the instance or the pk or primary key.

Just ensure that you use `company_id=3` when using integers and `company=my_company` when using the object instance.

## Abstract Inheritance

Model inheritance that does not create a new table
We call models without a db `abstract models

Django has 2 types of inheritance:
* Abstract - Won't actually have a database and you can't query. It is used as a starter for other models. Other models can extend from it.
* Multi-table - 2 tables even for models that inherit. No need to specify a foreign key as django will know that if parent model is not abstract

**Most Django develoeprs** will warn against using multi-table inheritance

### Abstract Models

In the models `Meta subclass` add:

        class Meta:
            abstract = True

## Specify how a model pluralises

    class Meta:
        verbose_name_plural = "Quizzes"

## Get Absolute Url

Tells django how to calculate the canonical url

## ModelForm

Automatically generated form based on a model

    from django import forms

* Extend from `forms.ModelForm`
* Requires 2 class `Meta` attibutes: `model` and `fields` or `exclude`
* Explicit is better than implicit so better to not use `exclude`

    class QuizForm(forms.ModelForm):
        class Meta:
            model = models.Quiz
            fields = [
                'title',
                'description',
                'order',
                'total_questions'
            ]

## Showing multiple forms

We utilise [formsets](https://docs.djangoproject.com/en/1.11/topics/forms/formsets/)

To use formsets with models with use [model formsets](https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#model-formsets)

        AnswerFormSet = forms.modelformset_factory(
                models.Answer, 
                form=AnswerForm,
        )

To control the associated answers you send in a `queryst`

        formSet = forms.AnswerFormSet(queryset=question.answer_set.all())


        forms.AnswerFormSet(request.POST, queryset=question.answer_set.all())

        if formset.is_valid():
                answers = formset.save(commit=False)

                for answer in answers:
                        answer.question = question
                        answer.save()
                return HttpResponseRedirect(question.quiz.get_absolute_url())

## Formsets

[Formsets](https://docs.djangoproject.com/en/1.11/topics/forms/formsets/) by default don't work with models

To create [model formsets](https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#model-formsets)

        AnswerFormSet = forms.modelformset_factory(
                models.Answer,
                form=AnswerForm
        )

Then on processing the form:

        formset = forms.AnswerFormSet(queryset=question.answer_set.all())

So sets answers associated with that specific question

        if request.method == 'POST':
            formset = forms.AnswerFormSet(request.POST, queryset=question.answer_set.all())

            if formset.is_valid():
                # Haven't set question for answers yet
                answers = formset.save(commit=False)
                for answer in answers:
                    answer.question = question
                    answer.save()

Printing out the formset in the view is simple:

It loops and prints through formsets for us

        {{ formset }}

Can set `extra` forms and `min_count` / `max_count` of forms by sending in the keyword args into the factory init

## Inline formsets

[Inline Formsets](https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#inline-formsets) appear in the model form for another model

An important form for checking whether a form is valid

    {{ formset.management_form }}

    AnswerInlineFormSet = forms.inlineformset_factory(
            models.Question,
            models.Answer,
            extra=0,
            fields=['order', 'text', 'correct'],
            formset=AnswerFormSet,
            min_num=1
    )

Getting a blank queryset

    answer_forms = forms.AnswerInlineFormSet(
            queryset=models.Answer.object.None()
    )

Handling:

    answer_forms = forms.AnswerInlineFormSet(
            request.POST,
            queryset=form.instance.answer_set.all()
    )

    answers = answer_forms.save(commit=False)
    for answer in answers:
        answer.question = question
        answer.save()

## Set assets that come with a form

Use `class Media`

        class productForm(forms.modelForm):
            class Media:
                # all this stuff is in static
                css = {'all': ('courses/css/order.css',)},
                js = (
                        'courses/js/vendor/jquery.fn.sortable.min.js',
                        'courses/js/order.js'
                )

Still need to add to layout css and js blocks with:

    {{ form.media.css }}
    {{ form.media.js }}

## Changing the widget type for a field on a model form

Use `class Meta`...`widgets` attribute

To use checkboxes instead of a MultiSelect, first import

        from django.forms.widgets import CheckboxSelectMultiple

Then set the widget for your field

        class MyForm(forms.ModelForm):
        class Meta:
                model = MyModel
                fields = ('tasks',)
                widgets = {
                'tasks': CheckboxSelectMultiple
                }

## Working with a many-to-many field with an intermediary model

 [Working with a many-to-many field with an intermediary model in the admin](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#working-with-many-to-many-intermediary-models) for this topic.

 This same method can be used for editing outside of admin, in a normal view:

 The `many-to-many` field and models

        class Project(models.Model):
                '''Project model
                '''
                name = models.CharField(max_length=255, unique=True)
                description = models.TextField()
                tasks = models.ManyToManyField(Task)
                users = models.ManyToManyField(
                        settings.AUTH_USER_MODEL,
                        through='ProjectMembership'
)


        class ProjectMembership(models.Model):
                '''Project Membership model
                '''
                user = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.PROTECT
                )
                project = models.ForeignKey(Project, on_delete=models.PROTECT)
                is_project_manager = models.BooleanField(default=False)
                full_time_equivalent = models.DecimalField(
                        max_digits=5,
                        decimal_places=2,
                        default=100,
                        validators=[
                        MinValueValidator(Decimal(0)),
                        MaxValueValidator(Decimal(100))
                        ]
                )

1. Create a form for the intermediary table in `forms.py`

    class ProjectMembershipForm(forms.ModelForm):
        class Meta:
            model = ProjectMembership
            fields = (
                'user',
                'project',
                'is_project_manager',
                'full_time_equivalent'
            )

2. Create a formset from the created form above in `forms.py`

    ProjectMembershipFormSet = inlineformset_factory(
        Project,
        ProjectMembership,
        form=ProjectMembershipForm
    )

3. Ensure that the template of the classview the `formset` is in the template

    <div class='col-sm-6 col-sm-offset-3'>
        <h2>Create Project</h2>
        <hr/>

        {% raw %}
        <form method='POST'>
            {% csrf_token %}
            {% bootstrap_form form %}
            <div id="#inline">
                {% bootstrap_formset projectmembership_formset layout='inline' %}
            </div>
            <input type="submit" class="btn btn-primary btn-lg" values="Save">
        </form>
        {% endraw %}
    </div>

4. Change the class-based view methods so that the formset is included and validated and data saved

    class ProjectCreateView(CreateView):
        model = Project
        form_class = ProjectForm

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.POST:
                context['projectmembership_formset'] = ProjectMembershipFormSet(
                    self.request.POST
                )
            else:
                context['projectmembership_formset'] = ProjectMembershipFormSet()
            return context

        def form_valid(self, form):
            '''Handle saving of the project membership formset
            '''
            context = self.get_context_data()
            project_memberships = context['projectmembership_formset']
            if project_memberships.is_valid():
                self.object = form.save()
                project_memberships.instance = self.object
                project_memberships.save()

            return super().form_valid(form)


 Sources:
 * [Django class based views with inline model formset](https://stackoverflow.com/questions/4497684/django-class-based-views-with-inline-model-form-or-formset)
 * [Old Gist - Do not use](https://gist.github.com/neara/6209563)

### More on FormSets

A formset always comes with a `ManagementForm` which contains metadata about the formset such as `form-TOTAL_FORMS`, `form-INITIAL_FORMS` and `form-MAX_NUM_FORMS`.

**If you are adding new forms via JavaScript, you should increment the count fields in this form as well.**

**if you are using JavaScript to allow deletion of existing objects, then you need to ensure the ones being removed are properly marked for deletion by including form-#-DELETE in the POST data**