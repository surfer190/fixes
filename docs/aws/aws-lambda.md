---
author: ''
category: AWS
date: '2022-08-01'
summary: ''
title: AWS Lambda
---

## What is AWS Lambda?

* Compute service - run code without the server
* Server admin, operating system maintenance, capacity provisioninig, auto-scaling, monitoring and logging is done for you.
* All you do is supply your code in a lanaguage supported
* Code is organised into lambda functions
* Pay only while the code is running

Triggering lambda function:

* using the Lambda API
* in response to events from other AWS services
    - data processing triggers from AWS s3 (simple storage service) or dynamodb
    - streaming data from kinesis

### When should I use Lambda?

When you don't want or need to fine tune and manage the runtime environment and resources.

### Lambda Features

* Concurrency and scaling controls
* Functions defined as container images - use container image tooling to build, test and deploy lambda functions
* Code signing - proof that approved developers write the code
* Lambda extensions - integrate with monitoring, observability, security and governance
* function blueprints - sample code
* database access
* filesystem access

### Lambda Pricing

* There is no additional charge for creating Lambda functions.
* There are charges for running a function and for data transfer between Lambda and other AWS services.
* Some optional Lambda features (such as provisioned concurrency) also incur charges.

## Tools

### AWS Cli

You can access lmabda info from the cli:

    aws lambda list-functions 

### AWS SAM

AWS Serverless Application Model is an extension of the CloudFormation template language - lets you define serverless applications at a higher level.

The **AWS SAM CLI** is a seperate commandline tool to manage and test AWS SAM applications.

### Code authoring tools

* Node.js
* Java - AWS toolkit for eclipse and intellij
* C# - AWS toolkit for visual studio
* Python - Lambda console and Pycharm with AWS Toolkit for JetBrains
* Ruby
* Go
* Powershell

## Getting Started

* You can author functions in the Lambda console, or with an IDE toolkit, command line tools, or the AWS SDKs
* The Lambda console provides a code editor for non-compiled languages that lets you modify and test code quickly

Deploying code:

* A `.zip` file archive that contains your function code and its dependencies
* A container image that is compatible with the Open Container Initiative (OCI) specification.

1. Go to Lambda home
2. Create a function
3. Give it a name and select the runtime (programming language)
4. An execution role will be created automatically

Go the the `Test` tab and run the function

![Successful run image](/img/lambda/success-example.png){: class="img-fluid" }

There is a summary reported in the log output:

    START RequestId: 4ee13858-8904-45af-9465-e911f6fd054b Version: $LATEST
    END RequestId: 4ee13858-8904-45af-9465-e911f6fd054b
    REPORT RequestId: 4ee13858-8904-45af-9465-e911f6fd054b	Duration: 1.27 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 36 MB	Init Duration: 107.95 ms	

Not the best logs...

Go the the `Monitor` tab and click `Metrics` you can then see the graph of metrics sent to cloudwatch.

To clean up:

1. Delete the Function. Functions page: Actions -> Delete
2. Delete the log group. Log groups page: `/aws/lambda/my-function` Actions -> Delete
3. Delete the execution role. IAM console: `my-function-role-31exxmpl` Delete role

## AWS Lambda foundations

* Function - resource to run your code, it processes events you send it
* Trigger - resource that starts a lambda function. They can be aws services, manually triggered (api) or with an event source mapping.
* Event - json formatted document containing data to process converted to a `dict` if you are using python
* Event Source Mapping - Amazon Simple Queue Service (Amazon SQS) queue, an Amazon Kinesis stream, or an Amazon DynamoDB stream, and sends the items to your function in batches
* Execution environment - isolated runtime for your function
* Instruction-set architecture (cpu architecture) - type of processor running your functions `arm64` or `x86_64`
* Deployment package - `.zip` or container
* Runtime - language-specific environment that runs in an execution environment
* Layer - a zip file that can contain: libraries, a custom runtime, data, or configuration files. Way to package libraries and other dependencies for sharing.
* Extension - augment with mointoring, observability, security and governance
* Concurrency - number of requests your function is serving at a time
* Qualifier - an alias or pointer to a specific version to split traffic between 2 versions
* Destination - an AWS resource where Lambda can send events from an asynchronous invocation

### Instruction set architectures

Advantages of ARM64:

* Better price
* Better performance

### VPC (Virtual Private Cloud) Private Network

* A Lambda function always runs inside a VPC owned by the Lambda service
* By default, Lambda runs your functions in a secure VPC. Lambda owns this VPC, which isn't connected to your account's default VPC.
* Your lambda VPC can access otehr VPCs with a VPC-to-VPC NAT (V2N) - one way.
* Multiple Lambda functions can share a network interface, if the functions share the same subnet and security group.
    - To connect to another AWS service, you can use VPC endpoints
    - a NAT gateway to route outbound traffic to another AWS service
* To give your function access to the internet, route outbound traffic to a NAT gateway in a public subnet. The NAT gateway has a public IP address and can connect to the internet through the VPC's internet gateway.
* A ENI (Elastic Network Interface) is used

### Lambda scaling

* If multi events arrive before the prior one has finished processing - another instance of the lambda function is added.
* The default regional concurrency quota starts at 1,000 instances
* Note that the burst concurrency quota is not per-function; it applies to all your functions in the Region - initial burst of traffic
* When requests come in faster than your function can scale, or when your function is at maximum concurrency, additional requests fail with a throttling error (429 status code).

> [Layers look to allow sharing of dependencies across lambas](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)

### Lambda with AWS CLI

Create the execution role:

    aws iam create-role --role-name lambda-ex \
    --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

You can also specify a json file:

    {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
            }
        ]
    }

    aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json

To add policies to the role:

    aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

* The `AWSLambdaBasicExecutionRole` policy has the permissions that the function needs to write logs to CloudWatch Logs.

### Commands for Lambda Functions

List functions:

    aws lambda list-functions --max-items 10

Get a lambda function:

    aws lambda get-function --function-name my-function

Delete a function:

    aws lambda delete-function --function-name my-function

## Lambda Permissions

* Every Lambda function has an IAM role called an execution role.
* In this role, you can attach a policy that defines the permissions that your function needs to access other AWS services and resources.
* At a minimum, your function needs access to Amazon CloudWatch Logs for log streaming.
* **If your function calls other service APIs with the AWS SDK, you must include the necessary permissions in the execution role's policy.**
* To give other accounts and AWS services permission to use your Lambda resources, use a resource-based policy.

> When a user tries to access a Lambda resource, Lambda considers both the user's identity-based policies and the resource's resource-based policy. When an AWS service such as Amazon Simple Storage Service (Amazon S3) calls your Lambda function, Lambda considers only the resource-based policy.

### Lambda execution role

1. Select Function
2. Choose `Configuration` tab
3. Under resource summary - review the resources the function can access

> To debug an error you can configure a function to have the same permissions as another function

### Creating a Lambda Execution Role

1. Open the Roles page
2. in the IAM console.
3. Choose Create role.
4. Under Common use cases, choose Lambda.
5. Choose Next: Permissions.
6. Under Attach permissions policies, choose the AWS managed policies `AWSLambdaBasicExecutionRole` and `AWSXRayDaemonWriteAccess`.
7. Choose Next: Tags.
8. Choose Next: Review.
9. For Role name, enter lambda-role.
10. Choose Create role.

When it goes into production remember to apply [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

> Use IAM Access Analyzer to help identify the required permissions for the IAM execution role policy.

### AWS Managed Policies

* `AWSLambdaBasicExecutionRole` - upload to cloudwatch
* `AWSLambdaDynamoDBExecutionRole` - read DynamoDB records
* `AWSLambdaKinesisExecutionRole` - read events on kinesis
* `AWSLambdaMSKExecutionRole` - read and access to records on Apache Kafka (MSK)
* `AWSLambdaSQSQueueExecutionRole` - Read from SQS
* `AWSLambdaVPCAccessExecutionRole` - manage ENIs within an Amazon VPC
* `AWSXRayDaemonWriteAccess` - upload trace data to X-Ray.
* `CloudWatchLambdaInsightsExecutionRolePolicy` - write runtime metrics to CloudWatch Lambda Insights
* `AmazonS3ObjectLambdaExecutionRolePolicy` - interact with s3

Services lambda reads from:

* Amazon DynamoDB
* Amazon Kinesis
* Amazon MQ
* Amazon Managed Streaming for Apache Kafka (Amazon MSK)
* Self-managed Apache Kafka
* Amazon Simple Queue Service (Amazon SQS)

### Identity-based IAM policies for Lambda

* You can use identity-based policies in AWS Identity and Access Management (IAM) to grant users in your account access to Lambda

Levels:

* `AWSLambda_FullAccess` - Grants full access to Lambda actions and other AWS services
* `AWSLambda_ReadOnlyAccess` - Grants read-only access to Lambda resources.
* `AWSLambdaRole` - Grants permissions to invoke Lambda functions

## Working with Python

> The minimum runtime is python3.7 and the max at time of writing is python3.9. Important to note that AWS Lambda does deprecate old runtimes so you then have to rewrite your code sometimes.

There is a sample application to get you up and running with dev and deployment as well as practices regarding logging and tracking:

[Python Sample Lambdas Application](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-python)

* Your Lambda function comes with a CloudWatch Logs log group.
* The function runtime sends details about each invocation to CloudWatch Logs.
* It relays any logs that your function outputs during invocation.
* If your function returns an error, Lambda formats the error and returns it to the invoker.

### Handler

The Lambda function handler is the method in your function code that processes events.

    def handler_name(event, context): 
        ...
        return some_value

On lambda you set the hander as the path to the function: eg. `mymodule.myfunction`

Two arguments are passed:

* Event object - json formatted data (usually arrives as a dict, but can be str, int, float or None type)
* Context object - methods and properties around invocation and the environment

    print(type(event))
    <class 'dict'>

> When you invoke a function, you determine the structure and contents of the event. When an AWS service invokes your function, the service defines the event structure.

#### Returning a value

Returning a value is optional.

* If a `RequestResponse` invocation type is used the response is returned
* If the response can't be serialised by `json.dumps` a runtime error is raised
* If the function returns none - the truntime returns `null`

## Deploy Python Lambda functions with .zip file archives

Zip must contain:

* function code and dependencies
* if it is larger than 50MB it is recommended to upload to S3
* If your package contains native libraries you can use AWS SAM CLI `sam build --use-container` to build them for a container at runtime
* The package must be built for the [instruction set of the function / cpu architecture arm64 or x86_64](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html)
* Lambda uses POSIX file permissions

> A python package may contain initialization code in the` __init__.py` file. Prior to Python 3.9, Lambda did not run the `__init__.py` code for packages in the function handler’s directory or parent directories.

### Runtime Dependencies

A [deployment package](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) is required to update a lambda
A dependency can be any package, module or other assembly dependency that is not included with the Lambda runtime environment for your function's code.

The `boto3` and standard library are included with all runtimes after python3.8

### Deployment without dependencies

Copy function into a folder: `my-math-function`, then run:

    zip my-deployment-package.zip lambda_function.py

### Deployment package with dependencies

Create the folder:

    mkdir my-sourcecode-function
    cd my-sourcecode-function

Create the module function: `lambda_function.py`:

    import requests
    def lambda_handler(event, context):   
        response = requests.get("https://www.example.com/")
        print(response.text)
        return response.text

Install the `requests` dependency to a new `packages` directory:

    pip install --target ./package requests

Create a deployment package with the installed library at the root:

    cd package
    zip -r ../my-deployment-package.zip .

> This generates a `my-deployment-package.zip` file in your project directory. 

Add the lambda function file to the root of the zip:

    cd ..
    zip -g my-deployment-package.zip lambda_function.py

### Using a virtual environment

    ~/my-function$ source myvenv/bin/activate
    (myvenv) ~/my-function$ pip install requests
    (myvenv) ~/my-function$ deactivate
    cd myvenv/lib/python3.8/site-packages
    zip -r ../../../../my-deployment-package.zip .

You can always `pip show <packagename>` to find where a package lives:

    $ pip show requests
    Name: requests
    Version: 2.28.1
    Summary: Python HTTP for Humans.
    Home-page: https://requests.readthedocs.io
    Author: Kenneth Reitz
    Author-email: me@kennethreitz.org
    License: Apache 2.0
    Location: ~/.virtualenvs/api-testing/lib/python3.7/site-packages
    Requires: certifi, charset-normalizer, idna, urllib3
    Required-by: requests-aws4auth

Add the function to the root of the library:

    zip -g my-deployment-package.zip lambda_function.py

### Deploying

You can use the frontend to upload your deployment package or you can use the cli:

    aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://my-deployment-package.zip

## Deploy Python Lambda functions with container images

Use:

* AWS base images for Lambda
* Using a private or community base image you need the [runtime interface client](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html#runtimes-api-client)
* Open-source runtime interface emulator (RIE) - Lambda provides a runtime interface emulator for you to test your function locally

The workflow for a function defined as a container image includes these steps:

1. Build your container image
2. Upload to ECR - Elastic Container Registry
3. Create the lambda function or update function code

### AWS Base Images

The [Python AWS Base Images](https://gallery.ecr.aws/lambda/python)

### Creating an Image from the Base

1. Creae a directory and add the function 'my_function.py`:

    import sys
    def handler(event, context):
        return 'Hello from AWS Lambda using Python' + sys.version + '!'

2. Add a `requirements.txt`

3. Create a `DockerFile`:

FROM public.ecr.aws/lambda/python:3.8

    # Copy function code
    COPY app.py ${LAMBDA_TASK_ROOT}

    # Install the function's dependencies using file requirements.txt
    # from your project folder.

    COPY requirements.txt  .
    RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

    # Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
    CMD [ "app.handler" ]

4. Build

    docker build -t hello-world . 

5. Run

    docker run -p 9000:8080 hello-world 

6. Test, once happy upload:

    # Auth with ECR
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com    
    # Create repo
    aws ecr create-repository --repository-name hello-world --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
    # tag and push
    docker tag  hello-world:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest
    docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

### Python runtime interface clients

When not using a lambda base image you must install the runtime interface clients

    pip install awslambdaric

## AWS Lambda context object in Python

    print(type(context))
    <class 'awslambdaric.lambda_context.LambdaContext'>

When Lambda runs your function, it passes a context object to the handler.

Available properties of `context`:

* `function_name` – The name of the Lambda function.
* `function_version` – The version of the function.
* `invoked_function_arn` – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
* `memory_limit_in_mb` – The amount of memory that's allocated for the function.
* `aws_request_id` – The identifier of the invocation request.
* `log_group_name` – The log group for the function.
* `log_stream_name` – The log stream for the function instance.
* `identity` – (mobile apps) Information about the Amazon Cognito identity that authorized the request.
    - `cognito_identity_id` – The authenticated Amazon Cognito identity.
    - `cognito_identity_pool_id` – The Amazon Cognito identity pool that authorized the invocation.
* `client_context` – (mobile apps) Client context that's provided to Lambda by the client application.
    - `client.installation_id`
    - `client.app_title`
    - `client.app_version_name`
    - `client.app_version_code`
    - `client.app_package_name`
    - `custom` – A dict of custom values set by the mobile client application.
    - `env` – A dict of environment information provided by the AWS SDK.

## Logging

To output logs from your function code, you can use the [`print` method](https://docs.python.org/3/library/functions.html#print) or **any logging library that writes to `stdout` or `stderr`**.

Eg:

    def lambda_handler(event, context):
        print(event)
        print(context)

Output:

    START RequestId: a5719ed3-2754-4880-b810-0223dfb9497f Version: $LATEST
    {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    LambdaContext([aws_request_id=a5719ed3-2754-4880-b810-0223dfb9497f,log_group_name=/aws/lambda/stephen-test-function,log_stream_name=2022/08/03/[$LATEST]e16c2353ced84a249c9909dd774997be,function_name=stephen-test-function,memory_limit_in_mb=128,function_version=$LATEST,invoked_function_arn=arn:aws:lambda:eu-west-1:449369602245:function:stephen-test-function,client_context=None,identity=CognitoIdentity([cognito_identity_id=None,cognito_identity_pool_id=None])])
    END RequestId: a5719ed3-2754-4880-b810-0223dfb9497f
    REPORT RequestId: a5719ed3-2754-4880-b810-0223dfb9497f	Duration: 1.27 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 36 MB	Init


The Report log:

* `RequestId` – The unique request ID for the invocation.
* `Duration` – The amount of time that your function's handler method spent processing the event.
* `Billed Duration` – The amount of time billed for the invocation.
* `Memory Size` – The amount of memory allocated to the function.
* `Max Memory Used` – The amount of memory used by the function.
* `Init Duration` – For the first request served, the amount of time it took the runtime to load the function and run code outside of the handler method.
* `XRAY TraceId` – For traced requests, the AWS X-Ray trace ID.
* `SegmentId` – For traced requests, the X-Ray segment ID.
* `Sampled` – For traced requests, the sampling result.

### Using the CloudWatch console

1. Open Log Groups on CloudWatch console
2. Choose the log group for your function: `/aws/lambda/your-function-name`
3. Choose a log stream

> To find logs for a specific invocation, we recommend instrumenting your function with AWS X-Ray. X-Ray records details about the request and the log stream in the trace.

### Using the AWS

    aws lambda invoke --function-name my-function out --log-type Tail
    {
        "StatusCode": 200,
        "LogResult": "U1RBUlQgUmVxdWVzdElkOiA4N2QwNDRiOC1mMTU0LTExZTgtOGNkYS0yOTc0YzVlNGZiMjEgVmVyc2lvb...",
        "ExecutedVersion": "$LATEST"
    }

Decode the logs:

    aws lambda invoke --function-name my-function out --log-type Tail --query 'LogResult' --output text |  base64 -d

### Deleting Logs

* Log groups aren't deleted automatically when you delete a function.
* To avoid storing logs indefinitely, delete the log group, or configure a retention period after which logs are deleted automatically.

### Logging Library

Make sure to set the loglevel - by default only warning and above will log:

    import json
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    def lambda_handler(event, context):
        message = f'{context.function_name} {context.function_version} {context.client_context}'
        
        logger.debug(event)
        logger.debug(context)
        logger.debug(message)
        
        key1_name = event.get('key1')
        return {
            'statusCode': 200,
            'body': f'Hello {key1_name}, from Lambda!',
            'context': message
        }

The format:

    START RequestId: eef2f4b3-5150-4c89-a3fc-62802d3cb297 Version: $LATEST
    [DEBUG]	2022-08-03T10:21:36.705Z	eef2f4b3-5150-4c89-a3fc-62802d3cb297	{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    [DEBUG]	2022-08-03T10:21:36.706Z	eef2f4b3-5150-4c89-a3fc-62802d3cb297	LambdaContext([aws_request_id=eef2f4b3-5150-4c89-a3fc-62802d3cb297,log_group_name=/aws/lambda/stephen-test-function,log_stream_name=2022/08/03/[$LATEST]4fd4ab7fefa54c869f54ad55ec6fbb1c,function_name=stephen-test-function,memory_limit_in_mb=128,function_version=$LATEST,invoked_function_arn=arn:aws:lambda:eu-west-1:449369602245:function:stephen-test-function,client_context=None,identity=CognitoIdentity([cognito_identity_id=None,cognito_identity_pool_id=None])])
    [DEBUG]	2022-08-03T10:21:36.706Z	eef2f4b3-5150-4c89-a3fc-62802d3cb297	stephen-test-function $LATEST None

Raise an execption - which will include a stacktrace:

    logger.exception('whoops what now?')
    
    ...

    [ERROR]	2022-08-03T10:24:46.155Z	ba9581f5-470c-4f9c-892f-f807eb6cc6c5	whoops what now?
    NoneType: None[ERROR] ValueError: Whoops some problem
    Traceback (most recent call last):
      File "/var/task/lambda_function.py", line 16, in lambda_handler
        raise ValueError('Whoops some problem')END RequestId: ba9581f5-470c-4f9c-892f-f807eb6cc6c5

If an error is raised:

    raise ValueError('Whoops some problem')

    ...

    [DEBUG]	2022-08-03T10:26:21.984Z	bbcf1882-2631-4008-9c55-7d61caad0a73	stephen-test-function $LATEST None
    [ERROR] ValueError: Whoops some problem
    Traceback (most recent call last):
      File "/var/task/lambda_function.py", line 14, in lambda_handler
        raise ValueError('Whoops some problem')END RequestId: bbcf1882-2631-4008-9c55-7d61caad0a73
    REPORT RequestId: bbcf1882-2631-4008-9c55-7d61caad0a73	Duration: 7.97 ms	Billed Duration: 8 ms	Memory Size: 128 MB	Max Memory Used: 36 MB	Init Duration: 134.31 ms

## Errors

When your code raises an error, Lambda generates a JSON representation of the error.

Invoke and run your lambda:

    aws lambda invoke   \
    --function-name my-function   \
        --cli-binary-format raw-in-base64-out  \
            --payload '{"key1": "value1", "key2": "value2", "key3": "value3"}' output.txt

### Examples

Runtime exception (Import error):

    {
    "errorMessage": "Unable to import module 'lambda_function': Cannot import name '_imaging' from 'PIL' (/var/task/PIL/__init__.py)",
    "errorType": "Runtime.ImportModuleError"
    }

> This happens if you have uploaded a deployment package that contains a C or C++ library: Pillow, Numpy or Pandas

In that case the recommendation is to use the`sam build` command with the `--use-container` option to create your deployment package - that creates a Docker container with a Lambda-like environment that is compatible with Lambda

JSON Serialization error:

    {
    "errorMessage": "Unable to marshal response: Object of type AttributeError is not JSON serializable",
    "errorType": "Runtime.MarshalError"
    }

This can be caused by base64 encoding:

    import base64
    encrypted_data = base64.b64encode(payload_enc).decode("utf-8")

or not specifying your zip file as a binary file:

    aws lambda create-function --function-name my-function --zip-file fileb://my-deployment-package.zip --handler lambda_function.lambda_handler --runtime python3.8 --role arn:aws:iam::your-account-id:role/lambda-ex

## Tracing

AWS clearly want you to use AWS X-Ray - as it is mentioned throughout the docs.

Using [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/?otel-blogs.sort-by=item.additionalFields.createdDate&otel-blogs.sort-order=desc) or the [X-RAY SDK for Python](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html)

> ADOT (Open Telemetry) is the preferred method for instrumenting your Lambda functions.

More on [Python tracing in the docs](https://docs.aws.amazon.com/lambda/latest/dg/python-tracing.html)

## Adding a trigger

When you add a trigger the IAM role of the lambda executor must have access to the tragger otherwise you get an error when creating the trigger:

    An error occurred when creating the trigger: Cannot access stream arn:aws:dynamodb:eu-west-1:449369602245:table/xxx-qa/stream/2021-03-23T15:21:51.322. Please ensure the role can perform the GetRecords, GetShardIterator, DescribeStream, and ListStreams Actions on your stream in IAM.

In that case you should get the executor role and then in `IAM` create an inline policy for dynamo DB to add:

    Allow: dynamodb:DescribeStream
    Allow: dynamodb:GetRecords
    Allow: dynamodb:GetShardIterator
    Allow: dynamodb:ListStreams
    Allow: dynamodb:ListShards

## Monitoring

Check the [Monitoring Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html)

## Security

Check the [Security Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html)

## Troubleshooting

Check the [Troubleshooting Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html)

## Profiling Lambdas with CodeGuru

Check the [Profiling Lambdas with CodeGuru Docs](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-lambda.html)

## Source

* [AWS Lmabda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)