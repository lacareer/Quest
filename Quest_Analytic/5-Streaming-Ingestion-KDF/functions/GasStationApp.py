import os
import json
import random
import boto3
import time

firehose_client = boto3.client('firehose')

timestamp = time.time()

"""
This application creates simulated data from fuel tank level sensors for multiple gas stations. 
On invocation, the data is streamed to the Kinesis Data Firehose delivery stream in JSON format.
"""

def lambda_handler(event, context):
    # Update the delivery stream name in the environment variables once you complete creating your KDF
    # delivery_stream = 'your-delivery-stream-name' according to your lab setup may be SI-Firehose 
    DELIVERY_STREAM = os.environ['delivery_stream']
    
    station_list = []
    
    for _ in range(10):
        
        id = _ + 1
        # guarantee a low fuel tank for one station
        if _ == 0:
            json_data = {
            'station_id': str(id),
            'fuel_tank1_level': str(random.randint(100,999)),
            'fuel_tank2_level': str(random.randint(100,999)),
            'fuel_tank3_level': str(random.randint(100,999)),
            'fuel_tank4_level': str(random.randint(100,999)),
            'fuel_tank5_level': str(random.randint(100,199)),
            'event_timestamp': int(timestamp)
            }
        else:
            json_data = {
            'station_id': str(id),
            'fuel_tank1_level': str(random.randint(100,999)),
            'fuel_tank2_level': str(random.randint(100,999)),
            'fuel_tank3_level': str(random.randint(100,999)),
            'fuel_tank4_level': str(random.randint(100,999)),
            'fuel_tank5_level': str(random.randint(100,999)),
            'event_timestamp': int(timestamp)
            }
        
        response = firehose_client.put_record(
            DeliveryStreamName=DELIVERY_STREAM,
            Record={
                    'Data': json.dumps(json_data)
            }
        )
        
        station_list.append(json_data)
        
    return station_list
