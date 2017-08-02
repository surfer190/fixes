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