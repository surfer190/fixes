## Adding Tasks to a Celery Queue on an Infinite Loop

Sometimes you need to continuously do a certain task on an interval.

Oftentimes people use cron, but it isn't the correct tool in my opinion.

    

You can also use a python `while True:` loop with `sleep()`s.

    

You could use [timeloop](https://github.com/sankalpjonn/timeloop)

If you are using `celery` you can use `celery.beat` for [periodic tasks](https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html)



### Sources

* [An elegant way to run periodic tasks in python](https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679)
* [Celery 4 best practices](https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/)
