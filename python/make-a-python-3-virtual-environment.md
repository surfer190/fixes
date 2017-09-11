# How to create a Python 3 Virtual Environment

```
virtualenv -p python3 env
```

Or If you have python 3.6.1:

```
virtualenv -p python3.6 env
```

https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get


## Caveats

**Are you using `matplotlib` on MacOSX?**

Well then this style `venv` will not work so rather use:

    python3 -m venv my-venv

or

    python3.6 -m venv my-venv

Source: 

* [Stackoverflow using python 3 virtulenv](http://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv)
* [Install Python 3.6.1 on Ubunuty](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get)
* [Matplot on MaxOSX](https://matplotlib.org/faq/osx_framework.html)