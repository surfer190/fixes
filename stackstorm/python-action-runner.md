# Python Action Runner Overview

The official stackstorm docs don't really go into detail into using the [python-action-runners](https://docs.stackstorm.com/reference/runners.html#python-runner-python-script)

The first port of call is to read that documentation but when you need a little more, check below.

## Need to Know

The python action runner uses `python 2`, that is what it is. So your python code should be compatible.

You need to create a class that extends `st2common.runners.base_action.Action`

So create your class with:

    from st2common.runners.base_action import Action


    class MyTestActionAction(Action):
        def run(self):

Check the examples at [stackstorm action examples](https://github.com/StackStorm/st2/blob/master/contrib/examples/actions/pythonactions/forloop_parse_github_repos.py), which has an example to print out the python version.

When you install a pack, a virtualenv is automatically created. If you are developing a pack that is already installed, you might need to initialise the virtualenv with:

    st2 run packs.setup_virtualenv packs=my-pack-name

Virtualenvs are stored at `/opt/stackstorm/virtualenvs` on a per pack basis

If you are using any external python packages, these need to be specified in `requirements.txt` in the base directory of the pack, as show in the [docs](https://docs.stackstorm.com/reference/packs.html?highlight=requirements%20txt)

If the library is not in your packs virtualenv, an attempt will be made to load it from [stackstorms default libraries](https://github.com/StackStorm/st2/blob/master/requirements.txt)

`Action` extends `st2client.models.core.Resource`, which `import six` and `from __future__ import absolute_import`.
So I think you can do `print(x)` the python 3 way...but not 100% on this.

If you want parameters you set them in the action definition:

    ---
    name: "delete-domain"
    runner_type: "python-script"
    description: "Action to delete a domain"
    enabled: true
    entry_point: "python2_actions/delete_domain.py"
    parameters:
    domain:
        type: "string"
        description: "domain name to delete"
        required: true

Then ensure your `run()` method takes additional paramters:

    def run(self, domain):
        ...

### Developing Pack New Requirements not Picked Up

The recommended way is to use git to version control your pack, in `/opt/stackstorm/packs/my-pack-name`.

So commit everything (make sure you have commited your `requirements.txt` and `pack.yaml`)

    git add .
    git commit

Then install your pack after making changes.

    st2 pack install file://$PWD


