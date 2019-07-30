# Orquesta

## Creating a Stackstorm Orquesta Workflow

1. Create your yaml specification in `../actions/workflows/..`

    /opt/stackstorm/packs/examples/actions/workflows/orquesta-basic.yaml

the content of will be:

    version: 1.0

    description: A basic workflow that runs an arbitrary linux command.

    input:
    - cmd
    - timeout

    tasks:
    task1:
        action: core.local cmd=<% ctx(cmd) %> timeout=<% ctx(timeout) %>
        next:
        - when: <% succeeded() %>
            publish:
            - stdout: <% result().stdout %>
            - stderr: <% result().stderr %>

    output:
    - stdout: <% ctx(stdout) %>

2. Specify the action metadata specifying the runner type:

    /opt/stackstorm/packs/examples/actions/orquesta-basic.yaml
    
with the content:

    ---
    name: orquesta-basic
    pack: examples
    description: Run a local linux command
    runner_type: orquesta
    entry_point: workflows/orquesta-basic.yaml
    enabled: true
    parameters:
      cmd:
        required: true
        type: string
      timeout:
        type: integer
        default: 60

3. Create the workflow / action in stackstorm

    st2 action create /opt/stackstorm/packs/examples/actions/orquesta-basic.yaml

The register the `examples.orquesta-basic` workflow

4. Execute the workflow asynchronously

    st2 run examples.orquesta-basic cmd=date -a

Both the workflow `examples.orquesta-basic` and the action `core.local` should be successful.

> Note: `st2 execution list` only shows top level executions (tasks are not displayed)

Get more detail about the tasks run in a workflow, eg:

    [cent@st2 actions]$ st2 execution get 5cdd39d652364c0144c846d8
    id: 5cdd39d652364c0144c846d8
    action.ref: examples.orquesta-basic
    parameters: 
    cmd: date
    status: succeeded (2s elapsed)
    start_timestamp: Thu, 16 May 2019 10:22:14 UTC
    end_timestamp: Thu, 16 May 2019 10:22:16 UTC
    result: 
    output:
        stdout: Thu May 16 10:22:16 UTC 2019
    +--------------------------+------------------------+-------+------------+-------------------------------+
    | id                       | status                 | task  | action     | start_timestamp               |
    +--------------------------+------------------------+-------+------------+-------------------------------+
    | 5cdd39d752364c04a73de24c | succeeded (1s elapsed) | task1 | core.local | Thu, 16 May 2019 10:22:15 UTC |
    +--------------------------+------------------------+-------+------------+-------------------------------+

## The Workflow Model

> A task can reference any registered StackStorm action directly.

| Attribute  | Required  | Description  |
|---|---|---|
| version  | Yes  | The version of the spec being used in this workflow DSL.  |
| description  | No  | The description of the workflow.  |
| input  | No  | A list of input arguments for this workflow.  |
| vars  | No  | A list of variables defined for the scope of this workflow.  |
| tasks  | Yes  | A dictionary of tasks that defines the intent of this workflow.  |
| output  | No  | A list of variables defined as output for the workflow.  |

### The Task Model

| Attribute  | Required  | Description  |
|---|---|---|
| delay  | No  | Number of seconds to delay the task execution.  |
| join  | No  | Sets up a barrier for a group of parallel branches  |
| with  | No  | When given a list, execute the action for each item.  |
| action  | No  | The fully qualified name of the action to be executed.  |
| input  | No  | A dictionary of input arguments for the action execution.  |
| next  | No  | Define what happens after this task is completed.  |

> Each task defines what StackStorm action to execute, the policies on action execution, and what happens after the task completes

All of the variables defined and published up to this point (aka context) are accessible to the task

**Geepuz...way to make is complicated:**

> If more than one tasks transition to the same task and `join` is specified in the latter (i.e. the task named `barrier_task` in the example below), then the task being transitioned into becomes a barrier for the inbound task transitions

To simplify:

**The barrier task will be blocked until all the parallel branches complete and reach it.**

Parrellel execution example:

    ---
    version: 1.0

    tasks:
    setup_task:
        # ...
        # Run tasks in parallel
        next:
        - do:
            - parallel_task_1
            - parallel_task_2
            - parallel_task_3

    parallel_task_1:
        # ...
        # Wait to run barrier_task after this
        next:
        - do:
            - barrier_task

    parallel_task_2:
        # ...
        # Eventually run barrier_task
        next:
        - do:
            - intermediate_task

    intermediate_task:
        # ...
        # Wait to run barrier_task after this
        next:
        - do:
            - barrier_task

    barrier_task:
        # ...
        # Run after parallel_task_1, parallel_task_2, and intermediate_task have all finished
        join: all

    parallel_task_3:
        # ...
        # Run immediately after setup_task, do NOT wait for barrier_task

which is visualised as:

    =---- time (not to scale) ---->

    setup_task--+
                |
                +------ parallel_task_1 --------------------------+
                |                                                 |
                +-- parallel_task_2 --+                           |
                |                     |                           |
                |                     +---- intermediate_task ----+
                |                                                 |
                |                                                 +-- barrier_task --+
                |                                                                    |
                +-- parallel_task_3 -------------------------------------------------+
                                                                                     |
                                                                                    +-- [finish]

> Conversely, if more than one tasks transition to the same task and join is not specified in the latter, then the target task will be invoked immediately following the completion of the previous task

#### With Items Model

> Use the with items section to process a list of items in a task

By default the tasks are executed concurrently.

| Attribute  |  Required  | Description  |
|---|---|---|
| items  | Yes  | The list of items to execute the action with.  |
| concurrency  | No  | The number of items being processed concurrently.  |

For example a task with a list of messages to echo:

    version: 1.0

    input:
    - messages

    tasks:
    task1:
        with: <% ctx(messages) %>
        action: core.echo message=<% item() %>

To name the item, the value returned by `item()` would be a dictionary like `{"message": "value"}`

    version: 1.0

    input:
    - messages

    tasks:
    task1:
        with: message in <% ctx(messages) %>
        action: core.echo message=<% item(message) %>

Working with multiple lists (that are pairs), requires them to be `zipped` first:

    version: 1.0
    
    input:
      - hosts
      - commands
    
    tasks:
      task1:
        with: host, command in <% zip(ctx(hosts), ctx(commands)) %>
        action: core.remote hosts=<% item(host) %> cmd=<% item(command) %>

#### Task transition model

The `next` section are task transitions executed after a task completes.
A task completes if it `succeeded`, `failed`, or `canceled`

If there is no `when` the default task completion is taken.

`publish` can be used to add new or update existing variables from the result into runtime workflow.

The tasks in `do` will be invoked in the order specified.

| Attribute  | Required  | Description  |
|---|---|---|
| when  | No  | The criteria defined as an expression required for transition.  |
| publish  | No  | A list of key value pairs to be published into the context.  |
| do  | No  | A next set of tasks to invoke when transition criteria is met.  |

It is important to know what the following mean and the differences between them:

* `<% result() %>`
* `<% ctx(msg) %>`
* `<% ctx().abcd %>`

#### Engine Commands

Engine commands have a special meaning to the workflow engine. When specified under `do` in the task transition they act accordingly. These words are reserved.

| Command  | Description  |
|---|---|
| noop  | No operation or do not execute anything else.  |
| fail  | Fails the workflow execution.  |

For the use of the `fail` case:

    version: 1.0

    description: >
        A workflow example that illustrates error handling. By default
        when any task fails, the notify_on_error task will be executed
        and the workflow will transition to the failed state.

    input:
      - cmd

    tasks:
      task1:
        action: core.local cmd=<% ctx(cmd) %>
        next:
          - when: <% succeeded() %>
            publish: stdout=<% result().stdout %>
          - when: <% failed() %>
            publish: stderr=<% result().stderr %>
            do: notify_on_error
      notify_on_error:
        action: core.echo message=<% ctx(stderr) %>
        next:
          # The fail specified here tells the workflow to go into
          # failed state on completion of the notify_on_error task.
          - do: fail

    output:
      - result: <% ctx(stdout) %>

> The trick is debugging these things - me

I wanted to debug what the value of the result of an action was

## Expressions

> Orquesta currently supports YAQL and Jinja expressions, although I find jinja is not supprted as much

**Note that mixing of both YAQL and Jinja expressions in a single statement is not supported**

* YAQL: `<% YAQL expression %>`
* Jinja: `{{ Jinja expression }}`

Accept expressions:
* workflow model: `input`, `output` and `vars`
* task model: `delay`, `with`, `action`, `input`
* with items: `items`, `concurrency`
* task transistion: `when` and `publish`

## Workflow Runtime Context

Variables can be assigned in `input`, `output` and `vars` in the workflow.
They can be assigned in `publish` in task transition.

> Once a variable is assigned into the context dictionary, it can be referenced by a custom function named `ctx`.

* `ctx(foobar)`: takes the variable name as the argument
* `ctx()`: returns the entire dictionary that can be referenced with `.` notation

ie. `<% ctx(a) %>` and `<% ctx().a %>` are the same

### Special keywords:

* `<% succeeded() %>`
* `<% result() %>`

### Dynamic Action execution

Apparently dynamic actions can happen in `orquesta`:

    version: 1.0

    input:
      - dynamic_action
      - data

    tasks:
      task1:
        action: "{{ ctx().dynamic_action }}"
        input:
          x: "{{ ctx().data }}"

### YAQL (Yet another Query Language)

Wrapped in `<%` and `%>`. Eg. `<% YAQL expression %>`

#### Dictionaries

Create a `dict`: `<% dict(a=>123, b=>true) %>`

Get keys: `<% ctx(dict1).keys() %>`

Get values: `<% ctx(dict1).values() %>`

Concatenate dicts: `<% dict(a=>123, b=>true) + dict(c=>xyz) %>`

#### Lists

Create a `list`: `<% list(1, 2, 3) %>`

Concatenate a list: `<% list(abc, def) + list(ijk, xyz) %>`

Access an item in the list: `<% ctx(list1)[0] %>`

#### Queries

Take this example:

    {
        "vms": [
            {
                "name": "vmweb1",
                "region": "us-east",
                "role": "web"
            },
            {
                "name": "vmdb1",
                "region": "us-east",
                "role": "db"
            },
            {
                "name": "vmweb2",
                "region": "us-west",
                "role": "web"
            },
            {
                "name": "vmdb2",
                "region": "us-west",
                "role": "db"
            }
        ]
    }

Return a list of VM names:

    <% ctx(vms).select($.name) %>

Return a list of names and roles:

    <% ctx(vms).select([$.name, $.role]) %>

Return a distinct list of regions:

    <% ctx(vms).select($.region).distinct() %>

Select VM's in a specific location:

    <% ctx(vms).where($.region = 'us-east').select($.name) %>

Select a web server in the us-east region:

    <% ctx(vms).where($.region = 'us-east' and $.role = 'web').select($.name) %>

##### Convert a list to a dictionary

    <% dict(vms=>dict(ctx(vms).select([$.name, $]))) %>

#### YAQL Standard Lib

The is also a [`yaql` standard library](https://yaql.readthedocs.io/en/latest/standard_library.html)

Stackstorm functions are available: `<% st2kv('system.shared_key_x') %>` and `<% st2kv('st2_key_id', decrypt=>true) %>`

## Workflow Operations

Pausing a workflow:

    st2 execution pause <execution-id>

Resume a workflow:

    st2 execution resume <execution-id>

Cancel a workflow:

    st2 execution cancel <execution-id>

Rerun a workflow:

    st2 execution re-run <execution-id>

## Sources

* [Stackstorm Docs on Orquesta](https://docs.stackstorm.com/orquesta/)
