<!-- Learn -->
This solutmion uses Amazon Kinesis Firehose to receive and ingest fuel level data directly into a data lake. 
Amazon Athena is then used to consume the data and identify the need to send fuel tankers to a gas station
Fuel levels is sent from each gas station from the gas station app, running on AWS Lambda, which immediately streams
the data to Kinesis Data Firehose delivery stream.
KDF sends sends the data to S3 consumption zone  bu,cket  where it is consumed by Amazon Athena every 60 seconds
Athena sends a list of stations that are low on fuel to the fuel planning app, on Lambda, which set delivery tickets into
and moves those tickets into SQS to be picked up by a dispatch
The fuel truck app, on lambda, queries the SQS for a delivery tickt, and the fuel truck app accepts it.
A fuel truck then sends th fuel to the gas station



<!-- Lab prerequisites -->
- Create the 3 lambdas using the code in /function and suitable roles for each after studying the code
- Create 2 buckets : consumption-bucket-1234567890 and athena-output-bucket-1234567890
- Create an SQS called Fuel_Planning_Queue
- Using AWS Glue, create a DB called 'conversion' nd a table under it called 'conversion_table' with locations of s3://consumption-bucket-1234567890/station-data/using below for table schema:

[
  {
    "Name": "station_id",
    "Type": "string"
  },
  {
    "Name": "fuel_tank1_level",
    "Type": "string"
  },
  {
    "Name": "fuel_tank2_level",
    "Type": "string"
  },
  {
    "Name": "fuel_tank3_level",
    "Type": "string"
  },
  {
    "Name": "fuel_tank4_level",
    "Type": "string"
  },
  {
    "Name": "fuel_tank5_level",
    "Type": "string"
  },
  {
    "Name": "event_timestamp",
    "Type": "int"
  }
]


<!-- Lab instructions -->
1. In the top navigation bar search box, type: kinesis
2. In the search results, under Services, click Kinesis.
3. Go to the next step.

1. On the Amazon Kinesis console home page, under Get started, choose Amazon Data Firehose.
2. Click Create delivery stream.
3. Go to the next step.

1. For Source, on the dropdown menu, choose Direct PUT.
2. For Destination, choose Amazon S3.
3. For Firehose stream name, type a name that you like, such as SI-Firehose, and then copy the name in the text editor of your choice on your device.
- You will use this name in later steps.
4. Scroll down to Convert record format.
5. Go to the next step.

1. For Convert record format, choose the check box to select Enable record format conversion.
2. For Output format, review to ensure that Apache Parquet is selected.
3. Scroll down to Schema for source records.
4. Go to the next step.

1. For AWS Glue region, choose US East (N. Virginia).
2. For AWS Glue database, choose conversion.
3. For AWS Glue table, click Browse.
4. Choose conversion_table.
5. Scroll down to Destination settings.
6. Go to the next step.

1. For S3 bucket, click Browse.
2. Choose the S3 bucket that starts with consumption-bucket-.
3. For Dynamic partitioning, choose Enabled.
4. Go to the next step.

1. For Multi record deaggregation, keep the default setting of Not enabled.
2. For Inline parsing for JSON, choose Enabled.
3. Go to the next step.

# Contains DIY step
1. Under Dynamic partitioning keys, for Key name, type:

station_id

2. For JQ expression, type: .station_id

3. Click Add dynamic partitioning key.
4. For Key name, type: year
5. For JQ expression, type: .event_timestamp| strftime("%Y")
6. Repeat this process for each key (month, day, and hour with corresponding values as '.event_timestamp| strftime("%m")', '.event_timestamp| strftime("%m")', and '.event_timestamp| strftime("%m")' respectively) and JQ expression in the screenshot example. Note that event_timestamp is derived from the table schema of conversion_table
7. Go to the next step.

1. For S3 bucket prefix, type:

station-data/station_id=

2. To populate the remainder of the S3 bucket prefix, click Apply dynamic partitioning keys.
3. Review to ensure that the S3 bucket prefix matches the screenshot example.
4. For S3 bucket error output prefix, type: error
5. For Retry duration, type: 60
6. Go to the next step.

1. Click to expand Buffer hints, compression and encryption.
2. For Buffer interval, type: 60
3. Scroll down to Advanced settings.
4. Go to the next step.

1. Click to expand Advanced settings.
2. For Permissions, choose the radio button to select Choose existing IAM role.
3. For Existing IAM roles, choose the role name that contains KinesisFirehoseRole.
4. Scroll down to the bottom of the page, and then click Create Firehose stream (not shown).
5. Go to the next step.

1. In the success alert, review the message.
- It may take a couple of minutes for the delivery stream to be created.
2. Go to the next step.

1. In the top navigation bar search box, type: lambda
2. In the search results, under Services, click Lambda.
3. Go to the next step.

1. In the Functions section, click the GasStationApp function.
2. Go to the next step.

1. On the GasStationApp page, on the Code tab, review the GasStationApp function code.

- This application creates simulated data from fuel tank level sensors for multiple gas stations. On invocation, the data is streamed to the Kinesis Data Firehose delivery stream in JSON format.

2. Click the Configuration tab.
3. Go to the next step.

1. On the Configuration tab, click Environment variables.
2. Click Edit.
3. Go to the next step.

1. In the Environment variables section, for the delivery_stream key, under Value, paste the Kinsesis Data Firehose delivery stream name that you copied in an earlier step.
2. Click Save.
3. Go to the next step.

1. In the success alert, review the message.
2. Scroll down and click the Test tab.
3. Go to the next step.

1. In the Test event section, under Event name, type a name for the test event, such as test.
2. Click Save.
3. Go to the next step.

1. In the success alert, review the message.
2. To run the test event, click Test.
3. Go to the next step.

1. In the Executing function window, click to expand the Details section.
- Fuel tank level sensor data for each gas station should be displayed.
2. Go to the next step.

1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the Buckets section, click the S3 bucket name that starts with consumption-bucket-.
2. Go to the next step.

1. On the Objects tab, click the refresh icon until the station-data/ folder is displayed.
- The folder might take up to five minutes to be displayed.
2. Go to the next step.

1. Navigate through the station-data/ subfolders for one of the gas stations until you reach the file level.
- This directory structure is based on the S3 bucket prefixes that were set up using the dynamic partitioning keys in the Kinesis Data Firehose delivery stream.
2. On the Objects tab, review to ensure that the file has been converted to Parquet format.
3. Navigate to the AWS Lambda console.
- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
4. Go to the next step.

1. In the Functions section, click the FuelPlanningApp function.
2. Go to the next step.

1. On the Code tab, review the FuelPlanningApp function code.
- This application uses the Amazon Athena API to query the data in the S3 bucket. The specified query looks for all gas stations with at least one fuel tank with a level under 200. On invocation, the application runs the query and returns a list of gas stations with low fuel.
2. To configure a test event, under TEST EVENTS, click Create new test event.
3. Go to the next step.

1. In the Create new test event pane, click Invoke.
2. In the Execution results window, in the OUTPUT tab, review to ensure that the test event was successfully completed.
- The gas stations that report at least one fuel tank with a level under 200 should be displayed.
3. Go to the next step.

1. In the top navigation bar search box, type: sqs
2. In the search results, under Services, click Simple Queue Service.
3. Go to the next step.

1. In the Queues section, under Messages available, review to ensure that Fuel_Planning_Queue messages are available.
2. Go to the next step.

1. Navigate to the AWS Lambda console.
2. In the Functions section, click the FuelTruckApp function.
3. Go to the next step.

1. On the Code tab, review the FuelTruckApp function code.
- This application polls the Fuel_Planning_Queue in Amazon Simple Queue Service (Amazon SQS) for messages that contain the IDs of gas stations with low fuel. The application processes those messages and alerts the fuel trucks to be dispatched to the gas stations needing fuel.
2. To configure a test event, under TEST EVENTS, click Create new test event.
3. Go to the next step.

1. In the Create new test event pane, click Invoke.
2. In the Execution results window, in the OUTPUT tab, review to ensure that the test event was successfully completed.
- The number of queue messages that were processed, along with a confirmation that a fuel truck is being dispatched to one or more gas stations low on fuel, should be displayed.
3. Go to the next step.

1. On the Code tab, click Invoke until there are no more Amazon SQS messages.
- You might need to click several times to process all the messages from the queue.
2. In the Execution results window, review the results.
3. Go to the next step.

1. Under Response, review to ensure that no more messages are in the queue.
2. Go to the next step.

1. Navigate to the Amazon SQS console.
2. In the Queues section, under Messages available, review to ensure that no messages are available in the Amazon SQS queue.
3. If number of messages available is not 0, click the refresh icon until it is 0.
4. Go to the next step.


Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
-Update the KDF delivery to stream to include minute as partition key

# hint
- Go to your KDF stream
- Go configuration tab
- Scroll to destination settings
- Click Edit
- Go to Dynamic partition keys
- Click on Add dynamic partitioning key
- For Key name, type: minute
- For JQ expression, type: .event_timestamp| strftime("%M")




