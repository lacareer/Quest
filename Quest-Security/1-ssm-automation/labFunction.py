# # MAKE SURE LAMBDA ROLE HAS:
# - ec2:CreateTags
# - ec2:DescribeInstances
# - logs:CreateLogGroup
# - logs:CreateLogStream
# - logs:PutLogEvent
import boto3

def lambda_handler(event, context):
    """
    Lambda function to auto-remediate EC2 instances by tagging them with Environment=Prod
    when triggered by AWS Config.
    """
    ### test properly as this code was from copilot
    print(event)
    ec2_client = boto3.client('ec2')

    # AWS Config passes the resourceId (instance ID) in the invoking event
    resource_id = event['IntsanceId']

    try:
        # Apply the tag
        ec2_client.create_tags(
            Resources=[resource_id],
            Tags=[{'Key': 'Environment', 'Value': 'Prod'}]
        )
        print(f"Successfully tagged instance {resource_id} with Environment=Prod")

    except Exception as e:
        print(f"Error tagging instance {resource_id}: {str(e)}")
        raise e