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

## Generic views

This makes the above much easier, quicker and better

        from rest_framework import generics

        class ListCreateCourse(generics.ListCreateAPIView):
            queryset = models.Course.objects.all()
            # Serializer is not instantaited as it is going to be instantiated every time
            serializer_class = serializers.CourseSerializer

You can also use a `detail view`:

        class RetrieveUpdateDestoyCourse(generics.RetrieveUpdateDestroyAPIView):
            queryset = models.Course.objects.all()
            serializer_class = serializers.CourseSerializer

Remember to add the url:

        url('^(?P<pk>\d+)/$', 
            views.RetrieveUpdateDestoyCourse.as_view(), 
            name='course_detail'),

### Creating sub views

So if you want to see the `reviews` from a specific `course` then you would add the urls;

        url('^(?P<course_pk>\d+)/reviews/$', views.ListCreateReview.as_view(), 
        name='review_list'),
        url('^(?P<course_pk>\d+)/reviews/(?P<pk>\d+)/$', 
            views.RetrieveUpdateDestoyReview.as_view(), 
            name='review_detail'),

Then the code

        class ListCreateReview(generics.ListCreateAPIView):
            queryset = models.Review.objects.all()
            serializer_class = serializers.ReviewSerializer

            def get_queryset(self):
                return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

            def perform_create(self, serializer):
                '''
                method run when created
                Prevents a user from giving a differnt pk
                '''
                course = get_object_or_404(
                    models.Course, pk=self.kwargs.get('course_pk')
                )
                serializer.save(course=course)

        class RetrieveUpdateDestoyReview(generics.RetrieveUpdateDestroyAPIView):
            queryset = models.Review.objects.all()
            serializer_class = serializers.ReviewSerializer

            def get_object(self):
                return get_object_or_404(
                    self.get_queryset(), 
                    course_id=self.kwargs.gets('course_pk'),
                    pk=elf.kwargs.gets('pk')
                )

### Routers and Viewsets

Work hand in hand with viewsets so you don't have to write url for each route

So you don't have to create multiple views for each resource you can do this all in one class

Simpler to add viewset urls in the site wide `urls` not in an app's `urls`

### Viewsets

Keep in mind that rest frameworks viewsets only generate crud views for a single model

        from rest_framework import viewsets

        class CourseViewSet(viewsets.ModelViewSet):
            queryset = models.Course.objects.all()
            serializer_class = serializers.CourseSerializer

        class ReviewViewSet(viewsets.ModelViewSet):
            queryset = models.Review.objects.all()
            serializer_class = serializers.ReviewSerializer

If you want to add the similar functionality

            from rest_framework.decorators import detail_route
            from rest_framework.response import Response

Then put the below in the viewset, using the `decorator`

            @detail_route(methods=['get'])
            def reviews(self, request, pk=None):
                course = self.get_object()
                serializer = serializers.ReviewSerializer(
                    course.reviews.all(), many=True
                )
                return Response(serializer.data)

### Registering viewset

        from rest_framework import routers
        from courses import views

        router = routers.SimpleRouter()
        router.register(r'courses', views.CourseViewSet)
        router.register(r'reviews', views.ReviewViewSet)

Tells the resource keyword and url, then register in `urlpatterns`:

        url(r'^api/v2/', include(router.urls, namespace='apiv2')),

### Mixins

Small classes that are mixed in to create larger classes

Sometimes you don't want a resource to have a list method for example fso you do:

        class ReviewViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
            queryset = models.Review.objects.all()
            serializer_class = serializers.ReviewSerializer

### Function based views instead of class based views

You can check [function based views docs](http://www.django-rest-framework.org/api-guide/views/#function-based-views)

## Relationships to a resource

* Include related records with the parent
* List foreign keys to reviews
* include urls to review instead

### Nested Relationships

You can add a serializer to the parent serializer then add that to the list of fields

        class CourseSerializer(serializers.ModelSerializer):

            reviews = ReviewSerializer(many=True, read_only=True)

            class Meta:
                model = models.Course
                fields = (
                    'id',
                    'title',
                    'url',
                    'reviews'
                )

But if there are many reviews for each course, then performance could degrade quickly.
So works best with a **limited amount of data** like **one-to-one**

### Hyperlinked related

The proper REST way [HATEOS](https://en.wikipedia.org/wiki/HATEOAS) Hypermedia.
Could also drasticly increase response time.

        class CourseSerializer(serializers.ModelSerializer):

            reviews = serializers.HyperlinkedRelatedField(
                many=True,
                read_only=True,
                view_name='apiv2:review-detail'
            )

            class Meta:
                model = models.Course
                fields = (
                    'id',
                    'title',
                    'url',
                    'reviews'
                )

### Primarykey Related

This just gets the primary key, so much faster

        class CourseSerializer(serializers.ModelSerializer):

            reviews = serializers.PrimaryKeyRelatedField(
                many=True,
                read_only=True
            )

            class Meta:
                model = models.Course
                fields = (
                    'id',
                    'title',
                    'url',
                    'reviews'
                )

Good if users know the uri

## Pagination

Will also limit results and reduce strain on API, can set a global default, can also set directly on viewsets or generic views

Add to `settings.py` in `REST_FRAMEWORK`

            'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
            'PAGE_SIZE': 5
    
Will work everywhere but not on `Ad-hoc`/ decorated views

Can set ad-hoc with:

        @detail_route(methods=['get'])
        def reviews(self, request, pk=None):
            self.pagination_class.page_size = 1
            reviews = models.Review.objects.filter(course_id=pk)

            page = self.paginate_queryset(reviews)

            if page is not None:
                serializer = serializers.ReviewSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = serializer.ReviewSerializer(reviews, many=True)
            course = self.get_object()
            serializer = serializers.ReviewSerializer(
                course.reviews.all(), many=True
            )
            return Response(serializer.data)