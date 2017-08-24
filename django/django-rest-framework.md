# Django Rest Framework

Abbreviated to `DRF`

* Framework that sits on top of django for writing RESTful web API's
* Fast and smarter than plain django Rest API creation
* Token based auth built in
* Proper status codes cooked in
* Throttling, pagination and browsable API

## Installation

        pip install djangorestframework

Add into `INSTALLED_APPS` in `settings.py`

        INSTALLED_APPS = [
            '...',
            'rest_frameowork',
            '...',
        ]

Some basic settings to start with are:

        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework.authentication.SessionAuthentication',
            ),
            'DEFAULT_PERMISSION_CLASSES': (
                'rest_framework.permissions.IsAuthenticatedOrReadOnly',
            )
        }

Then you need a URL so you can authentication in `urls.py` add:

        urlpatterns = [
            ...,
            url(r'^api-auth/', include('rest_framework.urls', 
                                    namespace="rest_framework")),
        ]

Follow the [Django Rest Framework Quickstart](http://www.django-rest-framework.org/) if you get stuck

## Serialisation

Built in model serialisation to serialise data into `json` or `xml` or whatever

They can also turn json back into model instances

Similar to django `ModelForm`

### Code

Create a file `serializers.py`

        from rest_framework import serializers

        from . import models

        class ReviewSerializer(serializers.ModelSerializer):
            class Meta:
                model = models.Review
                # write only means it can be added but is not sent out
                extra_kwargs = {
                    'email': {'write_only': True},
                }
                fields = (
                    'id',
                    'course',
                    'name',
                    'email',
                    'review',
                    'rating',
                    'created_at'
                )

        class CourseSerializer(serializers.ModelSerializer):
            class meta:
                model = models.Course
                fields = (
                    'id',
                    'title',
                    'url'
                )

Remember to be explicit about which fields in the model are serialised / visible

## Using serialisers and JSON

Try this in the shell: `./manage.py shell`

        >>> from rest_framework.renderers import JSONRenderer
        >>> from courses.models import Course
        >>> from courses.serializers import CourseSerializer
        >>> ourse = Course.objects.latest('id')
        >>> course = Course.objects.latest('id')
        >>> serializer = CourseSerializer(course)
        >>> serializer
        CourseSerializer(<Course: Python Collections>):
            id = IntegerField(label='ID', read_only=True)
            title = CharField(max_length=255)
            url = URLField(max_length=200, validators=[<UniqueValidator(queryset=Course.objects.all())>])
        >>> serializer.data
        {'id': 2, 'title': 'Python Collections', 'url': 'https://teamtreehouse.com/library/python-collections'}
        >>> type(serializer.data)
        <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
        >>> JSONRenderer().render(serializer.data)
        b'{"id":2,"title":"Python Collections","url":"https://teamtreehouse.com/library/python-collections"}'

`JSONRenderer().render(serialiser)` returns a byte-string `b'...'` string which is used for sending strings over the internet. It is not a normal python string.

## Handling HTTP Requests

DRF provides `APIView`

The `request` sent to the `APIView` will be DRF request objects and not djangos
The DRF request object extends djangos and adds request parsing and authentication

In `views.py` you can remove `from django.shortcuts import render` as there won't be views that **render** templates

We need these imports

        from rest_framework.views import APIView
        from rest_framework.response import Response

Then handle the view

        class ListCourse(APIView):
            def get(self, request, format=None):
                courses = models.Course.objects.all()
                serializer = serializers.CourseSerializer(courses, many=True)
                return Response(serializer.data)

Make sure to send the `many=True` keyword argument to the serializer constructor otherwise it will try to serialise the single option from multiple queryset

Add the url and bob' your uncle:

        urlpatterns = [
            url('^$', views.ListCourse.as_view(), name='course_list'),
        ]

## Creating records

        def post(self, request, form=None):
            serializer = serializers.CourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Only when we save is it persisted to disk, previously was in memory
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)