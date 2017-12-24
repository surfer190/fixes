# Pipenv

Now the official recommendation for managing python dependencies is [pipenv](https://docs.pipenv.org/)

## Advantages

* You no longer need to use pip and virtualenv separately. They work together.
* Managing a requirements.txt file can be problematic, so Pipenv uses the upcoming Pipfile and Pipfile.lock instead, which is superior for basic use cases.
* Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.

## Installing

#### Install on your system:

        pip install pipenv

#### Install a package

        pipenv install requests

1. Creates a pipfile
2. Installs `requests`
3. Creates a lockfile

#### Installing just for development

Use the `---dev` parameter

        pipenv install --dev nose2

Then to install with dev packages run:

        pipenv install --dev


## Open shell

        pipenv shell

then `exit` shell instead of deactivate

## Use requirements.txt

If you still want to use this relic you can:

        pipenv lock -r

## Use with django

To run commands from the environment prefix the command with:

        pipenv run xxx

Eg.

        pipenv run ./manage.py runserver

Personally I don't like this but perhaps the advantages outway the longer command

## Using Pipenv with Visual Studio

Often times we want intellisense from the python virtualenv.

With `pipenv` and `vscode` we first need to find where the virtual environment is with:

        pipenv --venv

Then open `cmd + shift + p` and `Select Interpreter` and paste the path

## Source

* [More Information on pipenv](https://docs.pipenv.org/)
* [vscode with pipenv](https://olav.it/2017/03/04/pipenv-visual-studio-code/)