---
author: ''
category: Django
date: '2019-06-21'
summary: ''
title: Django Rotating Log
---
# Add a Rotating Log to your Django Project

Use the [RotatingFileHandler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler) a log handler that comes with Python

In your django settings file:

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASE_DIR, 'debug.log'),
                'maxBytes': 1024 * 1024 * 15, # 15MB
                'backupCount': 10,
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file', ],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }

### Source:

* [Stackoverflow Location of Rotating Logs](https://stackoverflow.com/questions/19256919/location-of-django-logs-and-errors/19257221)
* [LogHandler Can't set max bytes](https://stackoverflow.com/questions/50677053/django-logging-cant-set-maxbytes)
