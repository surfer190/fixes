---
author: ''
category: Python
date: '2019-07-10'
summary: ''
title: Mock A Single Instance Method
---
# Mock a Single Instance Method

Patch the object with the method name. In this case `VeeamClient` is my class and `get_successfulP_jobs` is the instance method I am mocking.

    @patch.object(VeeamClient, 'get_successful_jobs')
    @responses.activate
    def test_calls_successful(self, mock_get_successful_jobs):
        '''
        Ensure persistently failed jobs calls the successful jobs method
        '''
        ...
        
        mock_get_successful_jobs.assert_called_with(job_name, creationtime)

## Source

* [Mock a single instance method](https://stackoverflow.com/questions/8469680/using-mock-patch-to-mock-an-instance-method)
