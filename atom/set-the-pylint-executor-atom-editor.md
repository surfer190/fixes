# How to set the pylint executable in the atom editor

If you have installed `linter-pylint` and you are getting the following error:

```
Failed to spawn command pylint. Make sure pylint is installed and on your PATH
```

The chances are that the package does not know where pylint is.

## Fixing the Path for Pylint

The first thing to do is make sure the package is installed globally (Not in a `virtualenv`)

```
pip install pylint
```

Then find out the path of pylint:

```
which pylint
> /usr/local/bin/pylint
```

Now to set the executable:

### Method 1

Click `Edit` or `Atom` then `Open Config...`

Append the following settings:

```
"linter-pylint":
  executable: "/usr/local/bin/pylint"
```

Replace `/usr/local/bin/pylint` with the results of `which pylint`

### Method 2

Click `Edit` or `Atom` then `Click Preferences`

Select `Packages->linter-pylint->Settings`

Under `Executable` set it as the path the `pylint`

eg. `/usr/local/bin/pylint`


##Source

[Github linter-pylint executable issue](https://github.com/AtomLinter/linter-pylint/issues/30)
