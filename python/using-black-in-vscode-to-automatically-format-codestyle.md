# Using Black to Automatically format codestyle

[Black](https://black.readthedocs.io/en/stable/the_black_code_style.html) is an opinionated code formatter for python.
It isn't a linter as it does not suggest, it just makes your code fit the style.

To set it up on vscode, open your project settings and add:

    {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
    }

Now whenever you save, your code will be formatted.

## Source

* [Black formatting in vscode](https://devblogs.microsoft.com/python/python-in-visual-studio-code-may-2018-release/)
