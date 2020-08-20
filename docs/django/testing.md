---
author: ''
category: Django
date: '2017-07-19'
summary: ''
title: Testing
---
# Django Testing

When you create an app the `tests.py` file is already created

It has the `import`:

        from django.test import TestCase

So we extend from that to write our test:


        class CourseModelTest(TestCast):
            def test_course_creation(self):
                course = Course.objects.create(
                    title="Python Regular Expressions",
                    description="Learn to write regular expression in python"
                )
                now = timezone.now()
                self.assertLess(course.created_at, now)
## Run the test

        ./manage.py test

## Set Up

Create your models at beignning of every test

        class CourseModelTest(TestCase):
            def setUp(self):
                model = Course.objects.create(....)


## Testing views

Using the name to get the route to view

        from django.core.urlresolvers import reverse

When testing views you get a `self.client` which is like a browser

        response = self.client.get(reverse('courses:list'))
        self.assertEqual(response.status_code, 200)

The client has a context on django views

        self.assertIn(self.course, response.context['courses'])
        self.assertIn(self.course2, response.context['courses'])

## Testing URL with primary keys

        response = self.client.get(reverse('courses:step', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.step.pk
        }))

    
    Use `kwargs`