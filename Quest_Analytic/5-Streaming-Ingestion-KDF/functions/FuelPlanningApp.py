import os
import time
import boto3


"""
Make sure you Lambda has the following environment variables set:
glue_database => conversion
glue_table => conversion_table
output_bucket => s3://athena-output-bucket-186526355503-bf4453e0/
queue_url => https://sqs.us-east-1.amazonaws.com/186526355503/Fuel_Planning_Queue
"""
# Athena constant
DATABASE = os.environ['glue_database']
TABLE = os.environ['glue_table']

# S3 constant
S3_OUTPUT = os.environ['output_bucket']

# SQS constant
QUEUE_URL = os.environ['queue_url']


"""
This application uses the Amazon Athena API to query the data in the S3 bucket. 
The specified query looks for all gas stations with at least one fuel tank with a level under 200. 
On invocation, the application runs the query and returns a list of gas stations with low fuel.
"""
def lambda_handler(event, context):

    # Created query
    query = """SELECT * 
               FROM %s.%s 
               WHERE fuel_tank1_level < '200'
               OR fuel_tank2_level < '200'
               OR fuel_tank3_level < '200'
               OR fuel_tank4_level < '200'
               OR fuel_tank5_level < '200';""" % (DATABASE, TABLE)

    # Athena client
    client = boto3.client('athena')

    
    # Execution
    queryStart = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT,
        }
    )

    queryId = queryStart['QueryExecutionId']
    time.sleep(3)
    
    stationids = []
    queryResults = client.get_query_results(QueryExecutionId = queryId)

    rowheaders = queryResults['ResultSet']['Rows'][0]['Data'] #The first item in ['ResultSet']['Rows'] contains a list of the column names
    rowindex = 0
    for r in queryResults['ResultSet']['Rows']:
        row_dict = {}
        if rowindex > 0: #Skip column names
            columnindex = 0
            for columnvalue in r['Data']:
                row_dict[rowheaders[columnindex]['VarCharValue']] = columnvalue['VarCharValue']
                columnindex += 1
            stationids.append("Gas station " + row_dict['station_id'] + " is low on fuel. Alerting fuel trucks.")
            stationID = row_dict['station_id']
                
            send_sqs_message(stationID)
                
        rowindex += 1

    return stationids
    
def send_sqs_message(stationID):
    
    # SQS client
    client = boto3.client('sqs')
    
    sendMessage = client.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=stationID
    )
    
    print(sendMessage['MessageId'])
