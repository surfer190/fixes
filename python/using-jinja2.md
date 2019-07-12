# Using Jinja 2 with FileSystem Templates

Install jinja

    pip install jinja2

In your file import required stuff

    from jinja2 import Environment, FileSystemLoader

Create a folder called `templates` and add a file called `config.j2`

{% raw %}
    {% for customer in customers %}
        set groups {{ customer['group'] }} interfaces {{ customer['interface'] }} unit {{ customer['unit'] }} {{ line }}
    {% endfor %}
{% endraw %}

Create the environment

    env = Environment(
        loader=FileSystemLoader('templates'),
        trim_blocks=True,
        lstrip_blocks=True
    )

Get the template

    template = env.get_template('config.j2')

Render the template with a context dict

    print(template.render(customers=[
        {
            'group': 'lx-1',
            'interface': 'ae16',
            'unit': '556'
        },
        {
            'group': 'lx-2',
            'interface': 'ae16',
            'unit': '557'
        },
    ]))

### Removing / Managing Indentation

We are concerned about 2 variables `trim_blocks` and `lstrip_blocks`:

* trim_blocks: If this is set to True the first newline after a block is removed (block, not variable tag!). Defaults to False.
* lstrip_blocks: If this is set to True leading spaces and tabs are stripped from the start of a line to a block. Defaults to False.

    env = Environment(
        loader=FileSystemLoader('templates'),
        trim_blocks=True,
        lstrip_blocks=True
    )

## Source

* [Jinja 2: Working with jinja 2 templates](https://devinpractice.com/2017/06/12/python-working-with-jinja2-templates/)
* [Jinja 2 templates docs](http://jinja.pocoo.org/docs/2.10/templates/)
* [Managing Jinja 2 Indentation](https://ansiblemaster.wordpress.com/2016/07/29/jinja2-lstrip_blocks-to-manage-indentation/)
* [Jinja 2: Network Automation Example](https://blogs.cisco.com/developer/network-configuration-template)
* [Stackoverflow: Remove unnecessary whitespace from jinja template output](https://stackoverflow.com/questions/35775207/remove-unnecessary-whitespace-from-jinja-rendered-template)