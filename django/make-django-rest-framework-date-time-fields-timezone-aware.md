## How to Make Django Rest Framework's DateTimeField Timezone Aware when outputting

The truth is that `django` and `drf` do really well with timezones. 
As shown in the (docs)[https://docs.djangoproject.com/en/1.11/topics/i18n/timezones], when `USE_TZ=True` django will store datetimes in `UTC`.
Then when they are retrieved to the template they will be output in the timezone set with the `TIME_ZONE` setting.

**But Django Rest Framework serialisers don't output date and times in the set timezone**

So to get around this we need to extend the default `DateTimeField` serializer.

    class DateTimeFieldWihTZ(serializers.DateTimeField):
        '''Class to make output of a DateTime Field timezone aware
        '''
        def to_representation(self, value):
            value = timezone.localtime(value)
            return super(DateTimeFieldWihTZ, self).to_representation(value)

    class QueueSerializer(serializers.ModelSerializer):
        class Meta:
            model = Queue
            fields = ('id', 'branch', 'date', 'length', 'wait_time',)

        date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')

So as shown above we `override` the `to_representation` method of the default `DateTimeField`.
Now the `json` output of the viewset will be in the expected timezone.

__Writing tests for these scenarios is very important__

Sources:

[Make DRF Timezone aware](https://stackoverflow.com/questions/17331578/django-rest-framework-timezone-aware-renderers-parser)s