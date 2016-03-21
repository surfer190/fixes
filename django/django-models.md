# Django models

You can specify how django prints out the reference to the model instance

Using dunder str: `def __str__(self):`

Eg.

  def __str__(self):
    return self.title
