# # MAKE SURE LAMBDA ROLE HAS:
# - ec2:CreateTags
# - ec2:DescribeInstances
# - logs:CreateLogGroup
# - logs:CreateLogStream
# - logs:PutLogEvent

import boto3

def lambda_handler(event, context):
    """
    Lambda function to auto-remediate EC2 instances by enabling detailed monitoring
    when triggered by AWS Config.
    """

    ec2_client = boto3.client('ec2')

    # AWS Config passes the resourceId (instance ID) in the invoking event
    resource_id = event['IntsanceId']

    try:
        # Enable detailed monitoring on the instance
        ec2_client.monitor_instances(InstanceIds=[resource_id])

        print(f"Successfully enabled detailed monitoring on instance {resource_id}")

    except Exception as e:
        print(f"Error enabling detailed monitoring on instance {resource_id}: {str(e)}")
        raise e