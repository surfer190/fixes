---
author: ''
category: Datascience
date: '2020-06-14'
summary: ''
title: Python - avoid venv clashes with 
---

You should set [`--system-site-packages`](https://virtualenv.pypa.io/en/latest/cli_interface.html?highlight=system-site#system-site-packages
)

    pip install -r requirements.txt --system-site-packages False



