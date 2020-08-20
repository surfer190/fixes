---
author: ''
category: Stackstorm
date: '2019-09-23'
summary: ''
title: St2client Execute Action
---
# How to execute an action with st2client

    from st2client.client import Client
    from st2client.models.action import Execution

    st2_client = Client(
        base_url='https://my-url/',
        auth_url='https://my-url/',
        api_url='https://my-url/api',
        api_key='XYZ'
    )

    execution = Execution()
    execution.action = 'my_pack.my_action'
    execution.parameters = {'domain': 'josetest1.co.za'}

    execution_obj = st2_client.executions.create(execution)

