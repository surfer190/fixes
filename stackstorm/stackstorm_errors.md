# Common Stackstorm Errors

## Workflows

**'''NoneType'' object has no attribute ''iteritems'''**

When running a workflow I get:

```
[test@st2 workflows]$ st2 run example.my_check
.
id: 5ce24f5152364c6d5cb1d957
action.ref: example.my_check
parameters: None
status: failed
start_timestamp: Mon, 20 May 2019 06:55:13 UTC
end_timestamp: Mon, 20 May 2019 06:55:13 UTC
result: 
  errors:
  - message: '''NoneType'' object has no attribute ''iteritems'''
  output: null
```

This is an issue with indentation of `yaml`. Ensure that you are showing whitespace in your editor and that you are looking at example workflows like `example.orquesta-basic`.

**TemplateAssertionError: no filter named ''decrypt_kv'''**

When running a workflow I get: `'JinjaEvaluationException: Unable to evaluate expression ''{{ st2kv.my_pass | decrypt_kv }}''. TemplateAssertionError: no filter named ''decrypt_kv'''`



**I get context errors where variables do not exist when running my workflow**

    result: 
      errors:
      - message: 'YaqlEvaluationException: Unable to resolve key ''stdout'' in expression ''<% result().stdout %>'' from context.'
        route: 0
        task_id: task1
        task_transition_id: noop__t0
        type: error
      - message: 'YaqlEvaluationException: Unable to resolve key ''stderr'' in expression ''<% result().stderr %>'' from context.'
        route: 0
        task_id: task1
        task_transition_id: noop__t0
        type: error
      - message: 'YaqlEvaluationException: Unable to evaluate expression ''<% ctx(stdout) %>''. VariableUndefinedError: The variable "stdout" is undefined.'
        type: error
      output: null

This was created with the following workflow:

    ---
    version: 1.0

    description: A basic workflow that runs the vdc check with hardcoded parameters from chatops.

    tasks:
      task1:
        action: core.remote
        input:
            cmd: "xxxx"
        next:
          - when: <% succeeded() %>
            publish:
              - stdout: <% result().stdout %>
              - stderr: <% result().stderr %>

    output:
      - stdout: <% ctx(stdout) %>

I changed the `when` condition and just used `stdout` as the output, not the best but it worked:

    ---
    version: 1.0

    description: A basic workflow that runs the vdc check with hardcoded parameters from chatops.

    tasks:
      task1:
        action: core.remote
        input:
            cmd: "xxyy"
        next:
          - publish:
              - stdout: <% result() %>

    output:
      - stdout: <% ctx(stdout) %>

The result of the workflow:

    result: 
      output:
        stdout:
          host:
            failed: false
            return_code: 0
            stderr: "xxx"
            stdout: 'yyy'
            succeeded: true

