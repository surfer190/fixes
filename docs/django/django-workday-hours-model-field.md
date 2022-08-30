---
author: ''
category: Django
date: '2017-10-11'
summary: ''
title: Django Workday Hours Model Field
---
# Django How to create a Django Workday hours Field

To create a field storing workday hours it is sometimes good to use `seconds`to capture and use choices like below.

    WORKDAY_CHOICES = (
        (0, '0'),
        (1800, '0.5'),
        (3600, '1'),
        (5400, '1.5'),
        (7200, '2'),
        (9000, '2.5'),
        (10800, '3'),
        (12600, '3.5'),
        (14400, '4'),
        (16200, '4.5'),
        (18000, '5'),
        (19800, '5.5'),
        (21600, '6'),
        (23400, '6.5'),
        (25200, '7'),
        (27000, '7.5'),
        (28800, '8'),
        (30600, '8.5'),
        (32400, '9'),
        (34200, '9.5'),
        (36000, '10')
    )

    workday_hours = models.PositiveIntegerField(
        choices=WORKDAY_CHOICES,
        default=28800
    )

But there is a way to do this with a list comprehension

    choices = [(3600 * num, num) for num in range(0, 10, 1)]

Unfortunately `range()` does not work with a decimal step