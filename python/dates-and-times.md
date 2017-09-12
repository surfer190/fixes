# Dates and times in Python

we will be using `datetime` a lot of the time

        import datetime

It has 4 modules we usually use:

* `date`
* `time`
* `datetime` - lets us work with time and date at the same time
* `timedelta`
* `timezone`

## Now

        >>> datetime.datetime.now()
        datetime.datetime(2017, 9, 12, 9, 19, 45, 673933)

## Replace

Replace attributes of the `datetime` object

        >>> treehouse_start = treehouse_start.replace(hour=9, minute=0, second=0, microsecond=0)

## Manually initialise a date

        h_start = datetime.datetime(2014, 10, 15, 9)

## Getting datetime difference

When you subtract 2 datetimes you get a timedelta

        >>> datetime.datetime.now() - treehouse_start
        datetime.timedelta(0, 1383, 884597)

* 0 - days
* 1383 - seconds
* 884597 - microseconds

You can check properties of a `tiemdelta`:

    td = datetime.datetime.now() - treehouse_start
    td.days
    td.microseconds
    td.seconds

## Timedeltas

Represent a gap of time

        datetime.timedelta(days=3)

You can also create negative 5 days

        datetime.timedelta(days=-5)

Then add that to a date:

        now = datetime.datetime.now()
        now - datetime.timedelta(days-5)

Just use the date or time

        now.date()
        now.time()

YOu can multiple timedeltas

        hour = datetime.timedelta(hour=1)
        workday = hour * 9

### Other methods

`datetime.datetime.today()` is different because you cannot control the timezone.

Combine a date and a time

        today = datetime.datetime.combine(datetime.date.today(), datetime.time())

Which creates a date at midnight

#### Find Day of the week

        today.weekday()

Python weeks start on `monday == 0`

#### Find Posix Tiemstamp

        today.timestamp()

#### Total seconds

Get the total number of seconds in a `timedelta`

        time.total_seconds()

## Converting times and dates

### Strftime

strftime - Convert a date, time or datetime into a string formatted how we want

        now.strftime('%B %d')

[Full cheatsheet of strftime python docs](https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior)

### Strptime

Think of it as **string parsed into time**

It lets us make a datetime out of a string of a certain format

    >>> birthday = datetime.datetime.strptime('2015-12-21', '%Y-%m-%d')
    >>> birthday
    datetime.datetime(2015, 12, 21, 0, 0)

## Timezones

A datetime object that knows its timezone is `aware`, those that don't are `naive`

#### Creating a Timezone object

        pacific = datetime.timezone(datetime.timedelta(hours=-8))
        eastern = datetime.timezone(datetime.timedelta(hours=-5))

The offset is from `UTC`

Create an aware datetime

        aware = datetime.datetime(2014, 4, 21, 9, tzinfo=pacific)

You can then change the timezone

        aware.astimezone(eastern)

You can also replace timezones

        import datetime

        naive = datetime.datetime(2015, 10, 21, 4, 29)

        timezone = datetime.timezone(datetime.timedelta(hours=-8))

        hill_valley = naive.replace(tzinfo=timezone)

Then move datetime to a new timezone:

        paris_tz = datetime.timezone(datetime.timedelta(hours=1))
        paris = hill_valley.astimezone(paris_tz)

### Pytz

        pip install pytz

Setting a timezone

        pacific = pytz.timezone('US/Pacific')
        utc = pytz.utc

Creating a `datetime` and makes aware:

        start = pacific.localize(datetime.datetime(2014, 4, 41, 9))
        start_eatern = start.astimezone(eastern)

`localize` is for naive timezones, we can't localize again

### Storing

Store as `UTC` as it is easier to convert with daylight savings time `DST`

### List all timezones

    pytz.all_timezones

### Country timezones

    >>> pytz.country_timezones('za')
    ['Africa/Johannesburg']