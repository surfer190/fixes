## Expecting a test to fail in Python or Django

How do you expect a test to fail when using Python or Django

You need to make use of `assertRaises`

We need to ensure we use the context keyword `with`

To expect a `KeyError`:

        def test_init_without_entry(self):
            with self.assertRaises(KeyError):
                CommentForm()

To expect a `TypeError`:

        def test_split(self):
            s = 'hello world'
            # check that s.split fails when the separator is not a string
            with self.assertRaises(TypeError):
                s.split(2)

Source: [assertRaises](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)