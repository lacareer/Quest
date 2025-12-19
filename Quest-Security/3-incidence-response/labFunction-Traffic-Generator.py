"""
This lambda function generates login logs
"""
import os, json
import boto3
import logging
import requests

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Importing EC2 boto3 client and resources.
# For additional info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def lambda_handler(event, context):
    #logger.info(event)
    pub_ip = get_pub_ip_from_tags("App-Server")
    
    url = f"http://{pub_ip}:8443/"
    print(url)
    for num in range(40):
        response = requests.post(url,data="username=admin&password=test123")
        print(response)

def get_pub_ip_from_tags(Tags):

    logger.info(Tags)
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    Tags,
                ]
            },
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running',
                ]
            }
        ],
        MaxResults=5
    )
    logger.info(response['Reservations'])
    logger.info(len(response['Reservations'][0]['Instances']))


    if len(response['Reservations'][0]['Instances']) > 1 :
        logger.info(len(response['Reservations'][0]['Instances']))
        logger.info(f"Too many EC2 instances match tags, try again {len(response)}")
    else:
        #logger.info(len(response['Reservations'][0]['Instances']))
        logger.info(response['Reservations'][0]['Instances'])

    #aws:cloudformation:stack-name	IncidentResponse-LabStack
    #Name	App-Server
    logger.info(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
    
    return response['Reservations'][0]['Instances'][0]['PublicIpAddress']
