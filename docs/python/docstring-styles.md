---
author: ''
category: Python
date: '2022-07-25'
summary: ''
title: Docstring types
---

### DocBlockr

    def __init__(self, driver, username, password, host, port, db_name, app_name=None):
        """_summary_

        Arguments:
            driver {_type_} -- _description_
            username {_type_} -- _description_
            password {_type_} -- _description_
            host {_type_} -- _description_
            port {_type_} -- _description_
            db_name {_type_} -- _description_

        Keyword Arguments:
            app_name {_type_} -- _description_ (default: {None})
        """

### Sphinx

    def __init__(self, driver, username, password, host, port, db_name, app_name=None):
        """_summary_

        :param driver: _description_
        :type driver: _type_
        :param username: _description_
        :type username: _type_
        :param password: _description_
        :type password: _type_
        :param host: _description_
        :type host: _type_
        :param port: _description_
        :type port: _type_
        :param db_name: _description_
        :type db_name: _type_
        :param app_name: _description_, defaults to None
        :type app_name: _type_, optional
        """

### Google

    def __init__(self, driver, username, password, host, port, db_name, app_name=None):
        """_summary_

        Args:
            driver (_type_): _description_
            username (_type_): _description_
            password (_type_): _description_
            host (_type_): _description_
            port (_type_): _description_
            db_name (_type_): _description_
            app_name (_type_, optional): _description_. Defaults to None.
        """

### Numpy

    def __init__(self, driver, username, password, host, port, db_name, app_name=None):
        """_summary_

        Parameters
        ----------
        driver : _type_
            _description_
        username : _type_
            _description_
        password : _type_
            _description_
        host : _type_
            _description_
        port : _type_
            _description_
        db_name : _type_
            _description_
        app_name : _type_, optional
            _description_, by default None
        """

### PEP 257

    def __init__(self, driver, username, password, host, port, db_name, app_name=None):
        """_summary_

        Arguments:
            driver -- _description_
            username -- _description_
            password -- _description_
            host -- _description_
            port -- _description_
            db_name -- _description_

        Keyword Arguments:
            app_name -- _description_ (default: {None})
        """

## Source

* [Autodocstring vscode extensions](https://github.com/NilsJPWerner/autoDocstring/)
