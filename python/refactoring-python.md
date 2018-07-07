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

