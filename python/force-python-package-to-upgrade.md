## Force Pip to install a new version of a package

Usually this is the case when pip uses cache

so use:

    pip install --no-cache-dir --upgrade <package>

Source: [Force Installing pip package](https://stackoverflow.com/questions/14617136/why-is-pip-installing-an-old-version-of-my-package)