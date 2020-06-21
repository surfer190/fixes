# Refactoring Python

## What is refactoring?

Repeatedly reorganising and rewriting code until it's obvious to a new reader.

## When to refactor?

Before adding complexity
It is hard to test
When you are repeating yourself
Brittleness, changing one part breaks others
Make something easier to read

Great programmers spend more time refactoring, after it is functional to make it obvious

## How to refactor?

1. Identify bad code
2. Improve it
3. Run tests
4. Fix and improve tests
5. Repeat

## In practise

* Rename, split and move
* Simplify
* Redraw boundaries - modules and classes relating to each other

## Prerequisites to Refactoring

* You need (thorough) tests 
* Quick tests (Max 1 or 2 mins)
* Need source control
* Willing to make mistakes

## Strategies

### Extract variable and extract function

There are hidden variables that make code seem more complicated than it is, you should extract these variables.

Bad Code:

{% raw %}
    MONTHS = ('January', 'February', 'March', 
            'April', 'May', 'June', 'July',
            'August', 'September', 'October',
            'November', 'December')


    def what_to_eat(month):
        if (month.lower().endswith('r') or month.lower().endswith('ary')):
            print('{}: oysters'.format(month))
        elif 8 > MONTHS.index(month) > 4:
            print('{}; tomatoes'.format(month))
        else:
            print('{} asparagus'.format(month))

    if __name__ == '__main__':
        what_to_eat('January')
        what_to_eat('July')
        what_to_eat('May')
{% endraw %}

After extract variable:

{% raw %}
    MONTHS = ('January', 'February', 'March', 
            'April', 'May', 'June', 'July',
            'August', 'September', 'October',
            'November', 'December')


    def what_to_eat(month):
        month_lower = month.lower()
        ends_in_r = month_lower.endswith('r')
        ends_in_ary = month_lower.endswith('ary')
        index = MONTHS.index(month)
        summer = 8 > index > 4
        
        if ends_in_r or ends_in_ary:
            print('{}: oysters'.format(month))
        elif summer:
            print('{}; tomatoes'.format(month))
        else:
            print('{} asparagus'.format(month))

    if __name__ == '__main__':
        what_to_eat('January')
        what_to_eat('July')
        what_to_eat('May')
{% endraw %}

Making it more clear at each level and with python there is no performance hit so always favour clarity.

We can take it a step further and extract a function.
So we need a (boolean) function determining when tomatoes are good and when oysters are good.

{% raw %}
    def what_to_eat(month):
        if oysters_good(month):
            print('{}: oysters'.format(month))
        elif tomatoes_good(month):
            print('{}: tomatoes'.format(month))
        else:
            print('{}: asparagus'.format(month))

    def oysters_good(month):
        month_lower = month.lower()
        return (
            month_lower.endswith('r') or
            month_lower.endswith('ary')
        )

    def tomatoes_good(month):
        index = MONTHS.index(month)
        return 8 > index > 4
{% endraw %}

This makes it much easier to read.

What if calling the method inline causes a performance problem?
You can then extract the function call into a variable.

{% raw %}
    def what_to_eat(month):
        time_for_oysters = oysters_good(month)
        time_for_tomatoes = tomatoes_good(month)
        
        if time_for_oysters:
            print('{}: oysters'.format(month))
        elif time_for_tomatoes:
            print('{}: tomatoes'.format(month))
        else:
            print('{}: asparagus'.format(month))
{% endraw %}

So now we have a cached value so we don't have to do computation multiple times and clarity.

Often conditions become more and more complex and dates and months may change based on certan criteria in which case it may be best to **extract variables into classes**

### Extract (boolean) variables into classes

    class TomatoesGood:
        def __init__(self, month):
            self.index = MONTH.index(month)
            self._result = 8 > index > 4
        
        def __bool__(self):
        return self._result

    def what_to_eat(month):
        time_for_oysters = OystersGood(month)
        time_for_tomatoes = TomatoesGood(month)
        ...

Remember python calls `__bool__()` when it is being evaluated in an `if`

#### Testing Easier

Testing is made much easier (maximises testability):

    test = OystersGood('November')
    self.assertTrue(test.r)
    self.assertTrue(test.ary)
    self.assertTrue(test)


## Extract Class and Move Fields

A complicated class with a bunch of fields and concerns bunched together then it may be time to refactor:

    class Pet:
        def __init__(self, name, age, *, has_scales=False, lays_eggs=False, drinks_milk=False):
            self.name = name
            self.age = age
            self.treats_eaten = 0
            self.has_scales = has_scales
            self.lays_eggs = lays_eggs
            self.drinks_milk = drinks_milk

this class has characteristics of a pet and characteristics of any animal. So let us talk abput boundaries:

### How to redraw boundaries

1. Add an improved interface
    * Maintain backwards compatibility
    * Issue warnings for old usage
2. Migrate old usage to new usage
    * Run tests to verify correctness
    * Fix and improve broken tests
3. Remove code for old interface

#### Warnings

Built into pythons

    import warnings
    warnings.warn('Helpful message')

* Defaults printing to `stderr`
* You can force warnings to become exceptions: `python -W error code.py` - a tool to find old ways of doing things

### Extracting Class

Extract an `Animal` class from `Pet`

    class Animal:
        def __init__(self, *, has_scales=False, lays_eggs=false, drinks_milk=False):
            self.has_scales = has_scales
            self.lays_eggs = lays_eggs
            self.drinks_milk = drinks_milk

Have Pet take an `Animal` instance and handle usage:

    class Pet:
        def __init__(self, name, age, animal=None, **kwargs):
            if kwargs and animal is not None:
                raise TypeError('Mixed Usage')
            if animal is None:
                warnings.warn('Should use Animal')
                animal = Animal(**kwargs)
            self.animal = animal
            self.name = name
            self.age = age
            self.treats_eaten = 0

But viewing properties on Pet that are `Animal` should still work, so we use `@property`

    class Pet:
        ...
        @property
        def has_scales(self):
            warning.warn('Use animal attribute')
            return self.animal.has_scales
        ...

* Use optional arguments when splitting a class
* Use `@property` to move fields between classes and inner classes
* Issue warnings for old usage

Always ask yourself when refactoring: **Is this obvious?**

You can use `@property.setter` to set the property of a inner object

    @has_scales.setter
    def has_scales(self, has_scales):
        warning.warn('Assign animal attribute')
        self.animal.has_scales = has_scales

## Example Refactoring

An example class that we can refactor

    import math
    import json


    class DataStats:

        def stats(self, data, iage, isalary):
            # iage and isalary are the starting age and salary used to
            # compute the average yearly increase of salary.

            # Compute average yearly increase
            average_age_increase = math.floor(
                sum([e['age'] for e in data])/len(data)) - iage
            average_salary_increase = math.floor(
                sum([int(e['salary'][1:]) for e in data])/len(data)) - isalary

            yearly_avg_increase = math.floor(
                average_salary_increase/average_age_increase)

            # Compute max salary
            salaries = [int(e['salary'][1:]) for e in data]
            threshold = '£' + str(max(salaries))

            max_salary = [e for e in data if e['salary'] == threshold]

            # Compute min salary
            salaries = [int(d['salary'][1:]) for d in data]
            min_salary = [e for e in data if e['salary'] ==
                        '£{}'.format(str(min(salaries)))]

            return json.dumps({
                'avg_age': math.floor(sum([e['age'] for e in data])/len(data)),
                'avg_salary': math.floor(sum(
                    [int(e['salary'][1:]) for e in data])/len(data)),
                'avg_yearly_increase': yearly_avg_increase,
                'max_salary': max_salary,
                'min_salary': min_salary
            })

So what are the issues with the code above

* The is no `__init()__` constructor so there are no class variables and might as well just be a function
* The `stats()` method is complicated and not obvious
* There is duplicate code

We want to maintain the code, as it works but there are no tests for it. So we need to do `TDR` Test driven refactoring. Once you have a test in place you can confidently modify the code and know if your refactoring has changed the results.

## Source

* [Brett Slatkin talk on Refactoring Python](https://www.youtube.com/watch?v=D_6ybDcU5gc)

