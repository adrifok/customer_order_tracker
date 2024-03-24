# customer_order_tracker 
Lambda-Amazon SQS queuing service-API Gateway
A company wants to create a system that can track customer orders and send notifications when orders have been shipped. They want to use AWS services to build the system: SQS, Lambda, and Python for the project.

Foundational Tasks:
-Create a Standard SQS Queue using Python: This involves using the Boto3 library (AWS SDK for Python) to programmatically create an SQS queue.
-Create a Lambda function in the console with a Python 3.7 or higher runtime: In the AWS Lambda console, create a new function and configure it to use Python 3.7 or a higher version.
-Modify the Lambda to send a message to the SQS queue: Update the Lambda function code to send a message to the SQS queue. You can use the current time or a random number as the message content. Make sure to use the Boto3 library to interact with SQS.
-Create an API Gateway HTTP API type trigger: Set up an HTTP API trigger for the Lambda function in the API Gateway console. This allows you to invoke the Lambda function through an API endpoint.
-Test the trigger to verify the message was sent: Use a tool like curl or a web browser to send a request to the API endpoint and verify that the Lambda function sends a message to the SQS queue.

