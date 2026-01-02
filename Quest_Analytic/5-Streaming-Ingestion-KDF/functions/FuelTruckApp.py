import os
import boto3
""""
Make sure you Lambda has the following environment variables set:
queue_url => https://sqs.us-east-1.amazonaws.com/186526355503/Fuel_Planning_Queue
"""


"""
This application polls the Fuel_Planning_Queue in Amazon Simple Queue Service (Amazon SQS) for messages that contain the IDs of gas stations with low fuel. 
The application processes those messages and alerts the fuel trucks to be dispatched to the gas stations needing fuel
"""
def lambda_handler(event, context):
    
    QUEUE_URL = os.environ['queue_url']
    
    # sqs client
    client = boto3.client('sqs')
    
    receiveMessage = client.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=5
    )
    
    for m in receiveMessage.get('Messages', []):

        print("Fuel truck has been dispatched to gas station " + m['Body'] + ".")
        
        receipt_handle = m['ReceiptHandle']
        client.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )
    
    processed_messages = len(receiveMessage.get('Messages', []))
    
    if processed_messages == 0:
        message = 'No messages found in queue. Messages processed: ' + str(processed_messages)
    else:
        message = 'Messages processed: ' + str(processed_messages)
        
    return message
