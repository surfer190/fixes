# Django ORM

## Recap

Using the `Course` model

### All records in database

    Course.objects.all()

### No records but an empty queryset

    Course.objects.none()

### Get a single course

    Course.get()

or

    get_object_or_404()

### Creating records

New Instance

    Course.create()

Also returns the instance

Save existing

    Course.save()

## Queryset

Queryset - collection of records returned from the database

* Anything that can return from a SQL query can be in a queryset
* They are lazy, they won't do the work until it is needed - they are in memory and don't hit the dtabase until they are consumed

### User Model

Useful but not required features are in `django.dontrib`

So `from django.contrib.auth.models import User`

## Mass Update

`update()` can be called on a queryset but not a single record

        models.Course.objects.update(published=True)

But that is the same as using `all()` so we can use `filter()` or `exclude()` the same way

        models.Course.objects.all().update(published=True)

Much better than using a `loop`

A `delete()` can also be run on a `querySet`

## Filter

        courses = models.objects.Course.filter(
                teacher__username=teacher
            )

What does the `__` do?

It jumps from one relationship to another

Funny things like greater or equal to filter is:

        reviews = models.Review.objects.filter(rating__gte = 3)

Instead of the intuitive

        reviews = models.Review.objects.filter(rating >= 3)

More Info on [field lookups](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups)

## Blunk Create

You have to pass `bulk_create` an itereable that contains model instances that are not saved, eg.

    Courses.objects.bulk_create([
        Course(title=..., ...),
        Course(..)
    ])

## Only select the values you neeed

Use `values()`

courses = Courses.objects.filter(published=True).values('id', 'title')[:5]

## Select jsut a single field from a bunch of record

datetimes = Courses.objects.datetimes('created-at', 'year')

## Order By

        .order_by('-created_at')

`created_at` is the field to order by, normally we do it in `Ascending` order

Then `-` makes it decending order

## F Objects

Allow you to refer to value in database not in instance which could be outdated

Use on sensitive data that has to be correct and real time, avoid race conditions

        from django.db.models import F

Example

        quiz.times_taken = F('times_taken') + 1
        quiz.save()

So `quiz.times_taken` becomes a `CombinedExpression`

        quiz.refresh_from_db()

Can do a db update on live data with:

        Course.objects.all().update(rating = F('rating') * 2)

## Q objects

### Multiple conditions on Filter are ANDS

When you add a filter:

        .filter(
            title__iconatins = 'red',
            description_icontains = 'green'
        )

It adds an `AND` not an `OR`

You can also add multiple `.filter().filter()` but then that will act as a chain

        from django.db.models import Q

Q object filter 

        filter(
            Q(title__icontains=title)|Q(description__icontains=term)
        )

Q objects are sub-queries

`|` makes it an `OR` or `UNION`

Remember `Q()` are non-keyword arguments `**args` where as normal filters are keyword arguments `**kwargs`

Kwargs must always go after args

Searching is better to use a dedicated search engine like elasticsearch

## Annotations

Let django run operations on each item in a queryset and append the result of that as a new attribute

        from django.db.models import Count, Sum

        courses = models.course.objects.filter(
            published=True
        ).annotate(
            total_steps=Count('text',distinct(True)) + Count('quiz', distinct(True))
        )

## Aggregates

        total = courses.aggregate(total=Sum(total_steps))

Aggregates are done on qurysets

## Prefetching and Seleting related

`prefetch_related` is for getting lots of other items, used if you want the reverse relationship - `parent` to `sub`

Sometimes you can check the SQL debug toolbar to see any duplciate queries and extended time

        try:
            models.Course.objects.prefetch_related(
                'quiz_set', 'text_set', 'quiz_set__question_set'
            ).get(pk=pk)
        catch models.Course.DoesNotExist:
            raise Http404

`selected_related` is for smaller amounts of items (one)
The foreign key field, going from `sub` to `parent`

        step = models.Quiz.objects.select_related('course').get(
            course_id=course_pk, pk=step.pk, course__published=True
        )

**These can make some huge performance improvements on SQL side**

## Testing ORM

You can use the `assertNumQueries` assertion to ensure that a certain number are queries are called