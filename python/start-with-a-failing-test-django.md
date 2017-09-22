# Start with a Failing Test Django

1. In you app go to `tests.py`

2. Create a class that extends `TestCase` and a function that starts with `test` that fails

        class EntryModelTest(TestCase):

            def test_string_representation(self):
                self.fail("TODO Complete this test")


Source: (Django Test Driven Development)[http://test-driven-django-development.readthedocs.io/en/latest/02-models.html]