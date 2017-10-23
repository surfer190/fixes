# Django Model Validations

Something to keep in mind when validating on the model is that the `clean` method is not called automatically.

So you have to override the `save` method so that the validation is done. Otherwise only `IntegrityError`s are raised.

### Code

Add the following method to your model

        def save(self, *args, **kwargs):
            self.full_clean()
            return super().save(*args, **kwargs)

### Model Validations do not run on model level

These validations will fire when creating objects with a `ModelForm` but they will not if you are just creating the object directly.

    full_time_equivalent = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            default=100,
            validators=[
                MinValueValidator(Decimal(0)),
                MaxValueValidator(Decimal(100))
            ]
        )

So it is again as above you need to run the `self.full_clean()` method on `save()`

#### Source

* [Django doesn't call model clean method](https://stackoverflow.com/questions/18803112/django-doesnt-call-model-clean-method)
* [Django Validating Positive decimals](https://stackoverflow.com/questions/12384460/allow-only-positive-decimal-numbers)