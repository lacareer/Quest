<!-- Learn -->
This lab uses Amazon Kinesis Data Stream to stream real time data and Amazon Managed Apache Flink to process the ingested data
Note that both srvices are now combined t be what is called Amazon Kinesis Data Stream for Apache Flink
Wind speed sensors data is sent directly to Amazon Kinesis Data Stream, a service that collects and process large streams of data record in real time
An Amazon Apache Flink application processes and analyses the data from Kinesis Data Stream. An Apache Flink application is a Java or Scala application
that is created with the Apache Flink framework.
The Flink application uses the Random Cut Forest algorithm to perform anomaly detection and assign an anomaly score to a record.
A record is an anomaly if t is distanct from other records.
A lambda is set as the external destination for the Kinesis Data Analytic application, parses the records(contains farm location, wind speed, and anomaly score) and stores it in DDB
A second lambda scans the DDB table and filters for anomaly scores grater than or equal to 2. For each discovered anomaly, the function publishes a notification message to an SNS topic which the maintenance team can subscribe to

<!-- Prerequisites -->
- Create an S3 Bucket named "kinesis-flink-application-1234567890" and upload each file in /java-code to it

- Find a way to deploy the Java app with a UI, or us the AWS CLI to send data to your data stream, that takes a Kinesis Data Stream name and generate data(contains farm location, wind speed, and anomaly score) to a running EC2 with SG port 80  0.0.0.0/0 that is the UI APP for the lab 

- Create DDB called "WindDataTable" and "DIYTable" with partition key as "timestamp"

- Create a role, lab-lambda-function-role-1234567890, for lambdas with this aws manageed roles:
  - AWSLambdaKinesisExecutionRole
  - AmazonDynamoDBFullAccess
  - AmazonSNSFullAccess
  - AWSLambdaBasicExecutionRole

- Deploy DIYFunction and analytics.py  as a lambda function with environment variable "OUTPUT_TABLE_NAME => WindDataTable"

- Deploy  anomalyMessageDeliveryFunction.py  as a lambda function with environment variable "OUTPUT_TABLE_NAME => WindDataTable" and "SNS_TOPIC_ARN => arn:aws:sns:us-east-1:55322590371234567890:AnomalyNotification"

- Create an SNS topic named "AnomalyNotification" add the sns.json as it's policy

- Learn how to set-up a Kinesis Data application with Java: https://github.com/awslabs/amazon-kinesis-agent or https://aws.amazon.com/kinesis/getting-started/ or any oth AWS docs

- Anomaly detection code is found here: https://github.com/aws-samples/amazon-kinesis-data-analytics-examples/tree/master/AnomalyDetection/RandomCutForest


<!-- Lab instructions -->
1. On the top navigation bar, review the Region selector to ensure that the Region is set to N. Virginia (us-east-1).
2. In the Services search box, type: s3
3. In the search results, under Services, click S3. 
4. Go to the next step.

1. In the Buckets section, click the bucket name that starts with kinesis-flink-application-.
2. Go to the next step. 

1. On the Objects tab, select (highlight) and copy AnomalyDetection.jar, and then paste it in the text editor of your choice on your device.
- You will use this application name in later step.
2. Go to the next step.

1. Navigate to Amazon EC2 Dashboard.
- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
2. On the EC2 Dashboard, in the Resources section, click Instances (running).
3. Go to the next step.

1. In the Instances section, choose the check box to select Wind Turbine Simulator.
2. On the Details tab, under Public IPv4 address, click the copy icon to copy the provided address.
3. Go to the next step.

1. In a new browser tab (or window) address bar, paste the public IP address that you just copied.
2. At the end of the IP address, type: /kinesis  and press Enter.
- This opens the wind turbine data simulator web application.
- Keep this new browser tab open. You will return to it in later steps.
3. Return to the Amazon EC2 console in the previous browser tab (not shown).
4. Go to the next step.

1. Navigate to the Amazon Kinesis console.
2. On the console home page, under Get started, review to ensure that Kinesis Data Streams is selected.
3. Click Create data stream.
- This data stream will be used to ingest incoming wind speed data.
4. Go to the next step.

1. For Data stream name, type: WindDataStream
2. For Capacity mode, choose Provisioned.
3. Scroll down to the bottom of the page, and then click Create data stream (not shown).
4. Go to the next step.

1. In the success alert, review the message.
2. Go to the next step.

1. Return to the Wind Turbine Data Simulator in the other browser tab, and then, for Amazon Kinesis data stream name, type: WindDataStream
2. Click Submit.
- This tells the simulator where (which Kinesis data stream) to send the wind data.
3. Go to the next step.

1. Click Start.
2. Go to the next step.

1. In the Test data terminal, review to ensure that data is being generated.
2. Go to the next step.

1. Return the WindDataStream page on the Amazon Kinesis console in the other browser tab, and then click the Data viewer tab.
2. For Shard, on the dropdown menu, choose the only available shard, shardId-0000000000000.
3. For Starting position, choose Latest.
4. Click Get records.
- If no data displays, you may need to click Retry getting records a few times.
5. Review the data.
6. Go to the next step.

1. In the left navigation pane, click Data streams.
2. In the Data streams section, click Create data stream.
- This data stream will be used to ingest the results of anomaly detection generated by the Managed Service for Apache Flink.
3. Go to the next step.

1. For Data stream name, type: AnomalyDetectionStream
2. For Capacity mode, choose Provisioned.
3. Scroll down to the bottom of the page, and then click Create data stream (not shown).
4. Go to the next step.

1. Review that the AnomalyDetectionStream was created successfully.
2. In the left navigation pane, click Managed Apache Flink.
- A new browser window or tab will open.
3. Go to the next step.

1. If not already selected, choose Streaming applications.
2. Click Create streaming application.
3. Go to the next step.

1. If not already selected, choose Create from scratch.
2. Scroll down to Apache Flink configuration.
3. Go to the next step.

1. In the Apache Flink configuration section, review the Apache Flink description and version.
- Your default Apache Flink version might differ from the screenshot example.
2. Scroll down to Application configuration. 
3. Go to the next step.

1. For Application name, type: AnomalyDetection
2. For Access to application resources, choose the radio button to select Choose from IAM roles that Managed Service for Apache Flink can assume.
3. For Service role, choose lab-apache-flink-role.
4. Scroll down to Template for application settings.
5. Go to the next step.

1. For Templates, choose Development.
2. Click Create streaming application.
3. Go to the next step.

1. In the success alert, review the message.
2. In the Application details section, review the details. 
- Note that the application status is Ready.                
3. At the top of the page, click Configure.
4. Go to the next step.

1. For Apache Flink runtime, choose Keep current Apache Flink runtime.
2. In the Application code location section, for Amazon S3 bucket, click Browse.
3. Go to the next step.

1. In the pop-up box, choose the radio button to select the bucket name that starts with kinesis-flink-application-.
2. Click Choose.
3. Go to the next step.

1. For Path to S3 object, paste the application name that you copied in an earlier step.
- The application was designed specifically for this solution use case.
- The sample files are available at https://github.com/aws-samples/amazon-kinesis-data-analytics-examples/tree/master/AnomalyDetection/RandomCutForest.
2. For Access to application resources, choose the radio button to select Choose from IAM roles that Managed Service for Apache Flink can assume.
3. For Service role, choose lab-apache-flink-role
4. Scroll down to Runtime properties.
5. Go to the next step.

- Next, add runtime properties to specify Kinesis data streams for the input and output streams.

1. Click Add new item.
2. For Group ID, type: lab
3. For Key, type: inputStreamName
4. For Value, type: WindDataStream
- You created the Kinesis data stream, WindDataStream, in earlier steps.
5. Go to the next step.

1. To add another new item, repeat the previous process and use the following values:

Group ID: lab
Key: outputStreamName
Value: AnomalyDetectionStream

2. To add another new item, repeat the previous process and use the following values:

Group ID: lab
Key: region
Value: us-east-1

3. Click Save changes.
4. Go to the next step.

1. In the success alert, review the message.
2. To start the application, below the alert, click Run.
3. Go to the next step.

1. For Snapshots, choose Run with latest snapshot.
2. Click Run.
3. Go to the next step.

1. Under Status, review to ensure that the application status changes from Starting to Running.
- The Apache Flink application retrieves streaming wind speed records from the Kinesis data stream, WindDataStream.
- The application uses the RCF algorithm to calculate an anomaly score for each record. The higher the score, the bigger the difference in wind speed between one record and the rest. 
2. Go to the next step.

1. Return to the Wind Turbine Data Simulator in the other browser tab, and then, under Wind speed data set, click Start.
2. Go to the next step. 

1. Review to ensure that the simulator is producing wind data.
2. Go to the next step.

1. Return to the Amazon Kinesis console in the previous browser tab.
2. In the left navigation pane, click Data streams.
3. In the Data streams section, click AnomalyDetectionStream.
4. Go to the next step.

1. To view the anomaly detection result, click the Data viewer tab.
2. For Shard, choose the only available shard, shardId-0000000000000.
3. For Starting position, choose Latest.
4. Click Get records.
5. To view incoming data, in the Records section, click Next records.
6. Review the data.
- If you don't see any records, wait for a few seconds and click Next records again.
7. Go to the next step.

1. Return to the Wind Turbine Data Simulator in the other browser tab, and then, under Wind speed anomaly data set, click Start.
2. Go to the next step. 

1. Review to ensure that the simulator is producing wind data.
2. Go to the next step.

1. In the other browser tab, navigate to the AWS Lambda console.
2. In the Functions section, click AnalyticsDestinationFunction.
- This Lambda function pulls records from the Kinesis data stream, AnomalyDetectionStream, and stores the records in the Amazon DynamoDB table, WindDataTable.
3. Go to the next step.

1. In the Function overview section, click Add trigger.
2. Go to the next step.

1. In the Trigger configuration section, on the Select a source dropdown menu, choose Kinesis.
2. Go to the next step.

1. For Kinesis stream, choose AnomalyDetectionStream.
2. Review to ensure that Activate trigger is selected.
3. For Starting position, choose Trim horizon.
4. Scroll down to the bottom of the page, and then click Add (not shown).
5. Go to the next step.

1. To review the code for AnalyticsDestinationFunction, on the Code tab, scroll down to the analytics.py window.
2. Review the code.
- This code accepts the wind data from the analytics application destination stream in JSON format and parses the data to store it in Amazon DynamoDB. 
3. Go to the next step.

1. Navigate to the Amazon DynamoDB console.
2. In the left navigation pane, under Tables, click Explore items.
3. In the Tables section, choose WindDataTable.
4. In the Items returned section, click the expand icon.
5. Go to the next step.

1. In the Items returned section, click the refresh button until you see the table populate with items.
- It may take a minute or two for items to show up.
2. In the information alert, click Retrieve next page, and then continue to click it until all table items are listed.
3. Go to the next step.

1. In the Items returned section, to display the first page of results, on the page selector, click 1 if not already selected.
2. Click the anomaly_score column header until the results are sorted in descending order.
- In descending order, the highest anomaly scores are at the top.
3. Review to ensure that the three anomalies are listed at the top of the results.
4. Go to the next step.

1. Navigate to the Amazon SNS console.
2. In the left navigation pane, click Topics.
3. In the Topics section, click AnomalyNotification.
4. Go to the next step.

1. Scroll down to the Subscriptions tab.
2. Click Create subscription.
3. Go to the next step.

1. For Protocol, choose Email.
2. For Endpoint, type a valid email address that you can access.
3. Click Create subscription.
- You will receive an email to confirm the subscription. Check your email inbox, and choose Confirm subscription in the email from AWS Notifications before continuing with the next step. The email might take a couple of minutes to arrive.
4. Go to the next step.

1. Navigate to the AWS Lambda console.
2. In the Functions section, click AnomalyMessageDeliveryFunction.
3. Go to the next step.

1. To review the code for AnomalyMessageDeliveryFunction, on the Code tab, scroll down to the anomaly.py window.
2. Review the code.
- This code runs a scan on the WindDataTable DynamoDB table and filters the results by anomaly score. If the item's anomaly score is greater than or equal to 2, the code adds the location and wind speed for that item to an SNS message and publishes it to the AnomalyNotification SNS topic.
3. To create a test event, on the Code source navigation bar, click Test.
4. Go to the next step.

1. In the pop-up box, for Event name, type a name that you like, such as AnomalyNotification.
2. Scroll down to the bottom of the page, and then click Save (not shown).
3. Go to the next step.

1. In the success alert, review the message.
2. To invoke the function, click Test again.
3. Go to the next step.

1. In the Execution results window, review the results.
- The function filtered through the WindDataTable DynamoDB table items and grabbed the three anomalies based on the function's filter logic.
2. Go to the next step.

1. Review to ensure that you received three emails to the email address that you provided for the AnomalyNotification SNS topic subscription.
- You should receive one notification email for each wind speed anomaly that was detected.
2. Go to the next step.

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY --> 
- Create a new Manage Service for Apache Flink application to calculate the wind speed maximum for one of the wind farms

# Hints
- Create a new Managed Service for Apache Flink application , called CalculateMaxSpeed. The MaxWindSpeed.jar file will be used, and is located in the S3 bucket that begins with Kinesis-flink-application.

- Create a new Kinesis Data Stream, called, MaxWindSpeed, to ingest the output from Apache Flink application

- Add the Kinesis Data Stream, MaxWindSpeed, as a trigger to the DIYFunction lambda function

From the wind turbine application simulator,  start the DIY Data Set. Check to verify that th DIY DDB is populated with maximum wind speed data for the city wind farm
