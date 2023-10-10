In the root of your project add a file called `pyproject.toml` with the content:

    [tool.black]
    line-length = 80

or for longer lines:

    [tool.black]
    line-length = 119

What is [pyproject.toml](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#what-on-earth-is-a-pyproject-toml-file)?

One could also add a config file to the home directory of your user:

[where black looks for config file?](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#where-black-looks-for-the-file)

In `~/.config/black` add:

    [tool.black]
    line-length = 119

## Source

* [Black change line length](https://datacomy.com/python/black/change_line_length/)