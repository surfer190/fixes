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
