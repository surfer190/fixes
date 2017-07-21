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