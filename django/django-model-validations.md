# Django Model Validations

Something to keep in mind when validating on the model is that the `clean` method is not called automatically.

So you have to override the `save` method so that the validation is done. Otherwise only `IntegrityError`s are raised.

### Code

Add the following method to your model

        def save(self, *args, **kwargs):
            self.full_clean()
            return super().save(*args, **kwargs)

#### Source

[Django doesn't call model clean method](https://stackoverflow.com/questions/18803112/django-doesnt-call-model-clean-method)