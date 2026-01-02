<!-- Summary -->
This solution uses Step Function to aujtomate the data ingestion and data preprocessing for final consumption.

A  shipment planning application runs on an AWS Lambda function. The application drop a JSON file into the landing bucket in S3.
This invokes another Lambda function to start a Step Funxcction workflow.
Step Function starts an AWS Glue job to convert the JSON to Parquet file. The newly created Parquest file is stored in the staging bucket in S3.
After the AWS Glue job is completed, SF starts an AWS Glue Crawlr to discover the schema and the metadata in the parquet file. A new AWS Glue Data Catalog is created to store the meta data of the this raw data.
A different AWS Glue job drops a column, customer_name, the parquest file and stores the result in a new file in staging bucket in S3.
After the customer_name column is dropped, SF starts a second Glue crawler to extract the metadata and schema from the new data.
After the 2nd Crawler runs, SF calls Atheena to run SQL query on top of the already enriched data. The query gnrates a report that providess the amount of fuel to be purchased the next day. Th report is storeed in consumption bucket in S3, and it can be downloaded as a CSV file.
At the end of the SF/Workflow, SF calls SNS to send an email to the subscribers


<!-- Prerequisites -->
- Create an SNS topic named shipping_data_queries. Subscrib your a valid email to it
- Create a AWS Glue Data Catalog database "shipping-db"
- Create a glue role using AWSGlueServiceRole-Lab.json
- Create a lambda that is trigger by events from the landing bucket to start a Glue job using start_step_function.py with environmet variable "STATE_MACHINE_ARN ==> < WITH STATE MACHINE ARN>" place holder for now and change whe you create SF


- Create 3 S3 buckets namely:

  - landing-bucket-<unique-suffix>. Also create an S3 event notification with "All object create events" Event types,  with Destination type "lambda function" and destination    as "start_step_function" lambda function

  - staging-bucket-<unique-suffix>

  - consumption-bucket-<unique-suffix>

- Create a shipment application lambda, shipping_schedule_application, "using shipping_schedule_application.py" with ennvironment variable BUCKET_NAME ==> landing-bucket-<unique-suffix>. Also, add the fakerLayer in this folder to it

- Create 2 crawlers, namly:
  1. s3_crawler_raw: uses the "shipping-db" and data source as s3://staging-bucket-b3b1f610/transformed_data (stores result in transformed_data folder)
  2. s3_crawler_processed: uses the "shipping-db" and data source as s3://staging-bucket-b3b1f610/normalized (stores result in normalized folder)

- Create 2 Glue jobs using the respective files in this folder. Follow the screenshots to configure the jobs as require under the Job Details tab after Script.

  Name the jobs as follows:
  1. data-normalization-job (use drop_field.py script file)
  2. JSON2Parquet-job (use json_parquet.py script file)

- Create SF role using AWSStepFunctionRole-Lab.json

- Follow lab steps to creat an SF or Create an SF using data-workflow.json. Go thru and modify if some naming in lab is different from the name you usd when creating some resources

<!-- lab instructions -->
1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the General purpose buckets section, review to ensure that the following three bucket names are displayed: 

landing-bucket
staging-bucket
consumption-bucket  

2. Select (highlight) and copy the bucket name that starts with with landing-bucket-, and then paste it in the text editor of your choice on your device.
3. Copy the bucket name that starts with staging-bucket-, and also paste it in your text editor.
- You will use both bucket names in later steps.
4. Click the bucket name that starts with landing-bucket-.
5. Go to the next step.

1. On the landing-bucket page, click the Properties tab. 
2. Scroll down to Event notifications.
3. Go to the next step.

1. In the Event notifications section, review the Event types.
2. Under Destination type, review to ensure that the type is a Lambda function. 
- The Lambda function, named start_step_function, is invoked any time a new file is uploaded into the S3 bucket, landing-bucket.
3. Go to the next step.

1. In the top navigation bar search box, type: glue
2. Under the search box, click Features.
3. Click AWS Glue Studio.
4. Go to the next step.

1. In the Your jobs section, select (highlight) and copy both job names, data-normalization-job and JSON2Parquet-job, to your text editor. 
- You will use the job names in later steps.
2. Click the job name, JSON2Parquet-job.
3. Go to the next step.

1. On the Script tab, review the Python code.
- This script transforms the raw data in landing-bucket from JSON format to Parquet. It then stores the results in staging-bucket.
2. On line 21, paste the landing-bucket name that you copied in an earlier step. 
- Be sure to include the forward slash after the bucket name.
3. On line 50, paste the staging-bucket name that you copied earlier. 

- Be sure to include /transformed_data/ after the bucket name.
4. At the top of the page, click Save.
5. In the left navigation pane, click ETL Jobs.
6. Go to the next step.

1. In the Your jobs section, click data-normalization-job.
2. Go to the next step.

1. On the Script tab, review the Python script.
2. On line 37, paste the staging-bucket name that you copied earlier.
- Be sure to include /normalized after the bucket name.
3. At the top of the page, click Save.
4. Click Crawlers.
5. Go to the next step.

1. On the Crawlers page, review both crawlers, s3_crawler_processed and s3_crawler_raw.
- You will use the AWS Step Functions state machine to invoke these crawlers.
4. Go to the next step.

1. In the top navigation bar search box, type: state
2. In the search results, under Features, click State Machines.
3. Go to the next step.

1. In the State machines section, click Create state machine.
2. Go to the next step.

1. For State machine name, type: data-workflow
2. Click Continue.
3. Go to the next step.

1. Under Workflow for State machine query language choose JSONPath. 
2. In the Design workflow step, click the Actions tab, and then review the list of actions.
- The Actions tab includes a list of AWS APIs that you can drag and drop to the workflow graph canvas.
3. Click the Flow tab, and then review the list of flow states.
- The Flow tab includes a list of flow states that you can drag and drop to the canvas.
4. In the workflow graph canvas, review the current graph, which should have only a Start state and End state.
- This canvas is where you drag and drop states into your workflow graph.
5. Go to the next step.

1. In the left search box, type: glue
2. Click and hold AWS Glue StartJobRun.
3. Drag and drop the action to the canvas, below Start.
4. On the right Configuration tab, for State name, type:
Convert JSON to Parquet
5. Scroll down to API Parameters.
6. Go to the next step.

1. In the API Parameters terminal, for JobName, type: JSON2Parquet-job
- Be sure to enclose the job name in double quotation marks.
2. Choose the check box to select Wait for task to complete.
- The state machine will wait for the AWS Glue job, JSON2Parquet, to finish before moving to the next state.
3. Go to the next step.

1. In the left search box, type: crawl
2. Click and hold AWS Glue StartCrawler.
3. Drag and drop the crawler to the canvas, below Convert JSON to Parquet.
4. On the right Configuration tab, for State name, type: Create Raw Data Catalog
5. In the API Parameters terminal, for Name, type: s3_crawler_raw
- Be sure to enclose s3_crawler_raw in double quotation marks.
6. Go to the next step.

1. In the left search box, type: getcrawler
2. Click and hold AWS Glue GetCrawler.
- A getcrawlers search will find multiple API actions. Be sure to choose the correct one: GetCrawler (singular).
3. Drag and drop the crawler to the canvas, below Create Raw Data Catalog.
4. On the right Configuration tab, for State name, type: Get Status First Crawler
5. In the API Parameters terminal, for Name, type: s3_crawler_raw
- Be sure to enclose s3_crawler_raw in double quotation marks.
6. Go to the next step.

1. Click the Input/Output tab.
2. Scroll down to Output.
3. Go to the next step.

1. Choose the check box to select Add original input to output using ResultPath.
2. In the next filter box, on the dropdown menu, choose Combine original input with result.
3. In the next text box, type: $.response.get_crawler
4. Go to the next step.

1. Under the left search box, click the Flow tab.
- Clear the input from the search box if needed.
2. Click and hold Choice.    
3. Drag and drop the state to the canvas, below Get Status First Crawler.
4. On the right Configuration tab, for State name, type: Is First Crawler Running?
5. Under Choice Rules, for Rule #1, click the edit icon.
6. Go to the next step.

1. Click Add conditions.
2. Go to the next step.

1. In the pop-up box, on the top (statement type) dropdown menu, click Simple.
2. Choose OR.
3. Go to the next step.

1. In the first condition, for Variable, type: $.response.get_crawler.Crawler.State
2. For Operator, choose is equal to.
3. For Value, choose String constant.
4. In the next (empty) text box, type: RUNNING
5. Go to the next step.

1. In the second condition, for Variable, type: $.response.get_crawler.Crawler.State
2. For Operator, choose is equal to.
3. For Value, choose String constant.
4. In the next (empty) text box, type: STOPPING
5. Click Save conditions.
6. Go to the next step.

1. On the left Flow tab, click and hold Wait.
2. Drag and drop the state to the canvas, into the placeholder that has the path name $.response.get_crawler.Crawler.State.
3. On the right Configuration tab, for State name, type: Wait for First Crawler
4. Go to the next step.

1. Scroll down to Next state.
2. For Next state, choose Get Status First Crawler.
3. Go to the next step.

1. In the left search box, type: glue
2. Click and hold AWS Glue StartJobRun.
3. Drag and drop the state to the canvas, into the placeholder that has the path name Default.
4. On the right Configuration tab, for State name, type: Process Data
5. Go to the next step.

1. In the API Parameters terminal, for JobName, type: data-normalization-job
- Be sure to enclose the job name in double quotation marks.
2. Choose the check box to select Wait for task to complete.
3. Go to the next step.

1. In the left search box, type:

crawler

2. Click and hold AWS Glue StartCrawler.
3. Drag and drop the crawler to the canvas, below Process Data.
4. On the right Configuration tab, for State name, type:  Create Processed Data Catalog
5. In the API Parameters terminal, for Name, type: s3_crawler_processed
- Be sure to enclose the name in double quotation marks.
6. Go to the next step.

1. Click and hold AWS Glue GetCrawler.
2. Drag and drop the crawler to the canvas, below Create Processed Data Catalog.
3. On the right Configuration tab, for State name, type: Get Status Second Crawler
4. In the API Parameters terminal, for Name, type: s3_crawler_processed
- Be sure to enclose the name in double quotation marks.
5. Go to the next step.

1. Click the Input/Output tab.
2. Scroll down to Output.
3. Go to the next step.

1. Choose the check box to select Add original input to output using ResultPath.
2. In the next filter box, on the dropdown menu, choose Combine original input with result.
3. In the next text box, type: $.response.get_crawler
4. Go to the next step.

1. In the left search box, type: choice
2. Click and hold Choice. 
3. Drag and drop the state to the canvas, below Get Status Second Crawler.
4. On the right Configuration tab, for State name, type: Is Second Crawler running?
5. Under Choice Rules, for Rule #1, click the edit icon.
6. Click Add conditions (Not shown).
7. Go to the next step.

1. In the pop-up box, on the top (statement type) dropdown menu, choose OR.
2. In the first condition, for Variable, type: $.response.get_crawler.Crawler.State
3. For Operator, choose is equal to.
4. For Value, choose String constant.
5. In the next (empty) text box, type: RUNNING
6. Go to the next step.

1. In the second condition, for Variable, type: $.response.get_crawler.Crawler.State
2. For Operator, choose is equal to.
3. For Value, choose String constant.
4. In the next (empty) box, type: STOPPING
5. Click Save conditions.
6. Go to the next step.

1. Click and hold the Wait state.
2. Drag and drop the state to the canvas, into the placeholder that has the path name $.response.get_crawler.Crawler.State.
3. On the right Configuration tab, for State name, type: Wait for Second Crawler
4. Go to the next step.

1. For Next state, choose Get Status Second Crawler.
2. Go to the next step.

1. In the left search box, type: athena start
2. Click and hold Amazon Athena StartQueryExecution.
3. Drag and drop the state to the canvas, into the placeholder with the path name Default.
4. On the right Configuration tab, for State name, type: Query Processed Data
5. Scroll down to API Parameters.
6. Go to the next step.

1. In the API Parameters terminal, for QueryString, replace myQueryString with:

SELECT SUM(shipping_cost) AS \"Total_Cost_in_$\",SUM(shipping_distance) AS \"Total_Distance_in_miles\", SUM(quantity) AS \"Total_Fuel_Quantity_in_gal\"  FROM \"shipping-db\".\"transformed_data\";

- Be sure to enclose it in double quotation marks.
- You can copy the above query and paste it. If you receive an undefined message, try copying and pasting again.

2. Review to ensure that the JSON object is properly formatted.
3. Go to the next step.

1. At the top of the page, click Code.
2. Review the Amazon State Language definition code.
3. Next to the code, review the state machine workflow graph.
4. Go to the next step.

1. At the top of the page, click Config.
2. Scroll down to the Permissions section.
3. For Execution role, under Choose an existing role, choose the role that statys with the name AWSStepFunctionRole-Lab-.
4. Click Create.
5. Go to the next step.

# SF STEP ENDS

1. Review the success message.
2. Click Exit.
3. Go to the next step.

1. Under Details, click to copy the provided ARN, and then paste it in your text editor.
- You will use the Amazon Resource Name (ARN) for this state machine in later steps.
2. Go to the next step.

1. In the top navigation bar search box, type: lambda
2. In the search results, under Services, click Lambda.
3. Go to the next step.

1. In the Functions section, click start_step_function.
2. Go to the next step.

1. Click the Configuration tab.
2. Click Environment variables.
3. Click Edit.
4. Go to the next step.

1. For Value, paste the ARN for the Step Functions state machine that you copied in an earlier step.
2. Click Save.
3. Go to the next step.

1. Scroll up to the top of the page.
2. On the breadcrumb menu, click Functions.
3. Go to the next step.

1. Click shipping_schedule_application. 
2. Go to the next step.

1. Click the Test tab.
2. For Test event action, choose Create new event.
3. For Event name, type: testevent
4. For Template, choose hello-world.
5. Click Save.
6. Click Test.
- This test will generate shipping data and invoke a state machine automation workflow.
7. Go to the next step.

1. In the top navigation bar search box, type: step functions
2. In the search results, under Services, click Step Functions.
3. Go to the next step.

1. In the State machines section, click data-workflow.
2. Go to the next step.

1. To view the state machine automation workflow status, on the Executions tab, click the available execution name.
- Each state machine execution takes a few minutes to complete. 
2. Go to the next step.

1. In the Graph view section, review the state machine workflow graph. 
2. Click any step in the graph to get more details. 
3. To view the input and output JSON text of a step, click the Input/Output tab.
4. Go to the next step.

1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the General purpose buckets section, click the bucket name that starts with consumption-bucket-.
2. Go to the next step.

1. Click queries.
2. Go to the next step.

1. On the Objects tab, choose the check box to select the object name that ends with .csv.
2. Click Download, and then save the file to your local device.
3. Go to the next step.

1. To view the result of the Amazon Athena query, on your device, open the CSV file.
- Because this data is generated randomly, your CSV file might have different data than the screenshot example.
2. Go to the next step.

1. In the top navigation bar search box, type: sns
2. In the search results, under Services, click Simple Notification Service.
3. Go to the next step.

1. In the left navigation pane, click Topics.
1. In the Topics section, under Name, click shipping_data_queries.
2. Go to the next step.

1. Scroll down to the Subscriptions tab.
2. Click Create Subscription.
3. Go to the next step.

1. In the Details section, for Protocol, choose Email.
2. For Endpoint, type a valid email address.
- Amazon SNS will send a verification email with the title AWS Notification - Subscription Confirmation. Be sure that you can access the email that you provide and click Confirm subscription.
3. Click Create subscription.
4. Go to the next step.

Congratulations! You’ve completed the Practice section. Go to the DIY section to complete the solution.




