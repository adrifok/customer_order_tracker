import boto3

# Initialize a session with the adrif profile
session = boto3.Session(profile_name='adrif')

# Attempt to get credentials from the session
credentials = session.get_credentials()

# Check if credentials were obtained successfully
if credentials is None:
    print("Failed to retrieve AWS credentials.")
else:
    # Print out the AWS credentials
    print("AWS Access Key ID:", credentials.access_key)
    print("AWS Secret Access Key:", credentials.secret_key)
    print("AWS Session Token:", credentials.token)

    # Initialize the SQS client using the session
    sqs = session.client('sqs')

    # Define the queue name
    queue_name = 'customer_order_tracker'

    try:
        # Create the SQS queue
        response = sqs.create_queue(QueueName=queue_name)
        print("SQS queue created with URL:", response['QueueUrl'])
    except Exception as e:
        print("An error occurred:", str(e))

