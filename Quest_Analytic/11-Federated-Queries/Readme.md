<!-- Summary -->
This solution requires the ability to prform SQL queries on data that is stored in DDB noSQL database
# Methos 1.
AWS Glu reads th data from from DDB and creates an AWS Glue Data Catalog. This Data Catalog takes the form of an AWS Glue Database and table
After the data catalog is in place, AWS Glue can run an extract, transform, and load, ETL, job that uses  the data in DDB to create a data lake
in an S3 bucket using the parquest format. Amazon Athena can the use the data catalog and data lake to perform SQL queries on the data. Note that you will
need to run the ETL job again because the data in DDB changes

# Method 2
To avoid the requird data lake refresh as th source data changes, federated queries can use SQL on th  data source without the need for a data catalog or data lakes
Federated quries use a connectore function, running the AWS Lambda, to provide access to the data source. With the connectore in place, Athena can perform SQL queries directly.



<!-- Prerequisites -->
- Create lambda function "athena_connector_function" using athena_connector_function.py (Note that  could not download the function or layer). Learn about Lambda as an Athena    Connector and sample code

- Create 2 S3 buckets:
  - athena-bucket-1234567890
  - data-lake-bucket-1234567890

-Create a Glue DB called "glue_ticket_db"

- Create a DDB named, DynamoDBTicketTable with Partition key TicketNumber (String). Populate the DB with faker using the structure below:

{
 "TicketNumber": "47932",
 "City": "CQ",
 "EmailAddress": "Donald.Rocha@example.com",
 "Name": "Daniel Neal",
 "Neighborhood": "Machine Learning Island",
 "PhoneNumber": "(929)358-4601x197",
 "Prefix": "Dr.",
 "RequestType": "grind rail request"
}

<!-- lab -->
# Method 1
1. In the top navigation bar search box, type: glue	
2. In the search results, under Services, click AWS Glue.
3. Go to the next step.

1. In the left navigation pane, under Data Catalog, click Crawlers.
2. Go to the next step. 

1. In the Crawlers section, click Create crawler.
2. Go to the next step.

1. In the Set crawler properties step, for Name, type: ticket-data-crawler
2. Click Next.
3. Go to the next step.

1. In the Choose data sources and classifiers step, for "Is your data already mapped to Glue tables?", keep the default setting of Not yet.
2. For Data sources, click Add a data source.
3. Go to the next step.

1. In the pop-up box, for Data source, on the dropdown list, choose DynamoDB.
- An arrow in the text box indicates a dropdown list.
2. Go to the next step.

1. For Table name, type: DynamoDBTicketTable
2. Click Add a DynamoDB data source.
3. Go to the next step.

1. Click Next.
2. Go to the next step.

1. In the Configure security settings step, for Existing IAM role, choose AWSGlueServiceRole-lab.
2. Click Next.
3. Go to the next step.

1. In the Set output and scheduling step, for Target database, choose glue_ticket_db.
2. Click Next.
3. Go to the next step.

1. In the Review and create step, at the bottom of the page, click Create crawler.
2. Go to the next step.

1. In the Crawler properties section, under State, review to confirm that the state changed to Ready.
2. Above the section, click Run crawler.
- The state of your crawler will change to Running, and a green success alert will appear at the top of the page. After a few minutes, the state will change to Stopping.
-  You might need to click the refresh icon.
3. Go to the next step.

1. After several minutes, review to confirm that the state has returned to Ready.
- You might need to click the refresh icon.
2. On the Crawler runs tab, under Status, review to confirm that the status is Completed.
3. In the left navigation pane, click Tables.
4. Go to the next step.

1. In the Tables section, review to confirm that the table that you created earlier was added (by the crawler) to the AWS Glue database.  
- If the table name is not displayed, click the section's refresh icon.
2. In the left navigation pane, click ETL jobs.
3. Go to the next step.

1. In the Create job section, click Visual ETL.
2. Go to the next step.

1. On the Visual tab, on the Sources tab, click AWS Glue Data Catalog.
2. On the Visual job editor canvas, review the new component.
3. Click the Transforms tab.
4. Go to the next step.

1. Click Change Schema.
2. On the canvas, review the new component.
3. Click the Targets tab.
4. Go to the next step.

1. Click Amazon S3.
2. On the canvas, review the new component.
3. Click the node, AWS Glue Data Catalog.
4. Go to the next step.

1. In the right node panel, on the Data source properties - Data Catalog tab, for Database, choose glue_ticket_db.
2. For Table, choose dynamodbtickettable.
3. Go to the next step.

1. On the Visual job editor canvas, click the Amazon S3 node.
- You might need to scroll down in the canvas to see the Amazon S3 node.
2. In the right node panel, on the Data target properties - S3 tab, for Format, choose Parquet.
3. For S3 Target Location, click Browse S3.
4. Go to the next step.

1. In the pop-up box, choose the radio button to select the bucket that starts with data-lake-bucket-.
2. Click Choose.
3. Go to the next step.

1. Scroll down to Data Catalog update options.
2. To update the schema, choose the second option.
3. For Database, choose glue_ticket_db.
4. For Table name, type: glue-etl-ticket-table
5. On the job editor tab ribbon, click the Job details tab.
6. Go to the next step.

1. For Name, type: ticket-etl-job
2. For IAM Role, choose AWSGlueServiceRole-lab.
3. For Glue version, choose Glue 3.0.
4. At the top of the page, click Save.
5. Go to the next step.

1. In the success alert, review the message.
2. Click the Script tab.
3. Go to the next step.

1. To update this script, click Edit script.
2. Go to the next step.

1. In the pop-up box, review the warning message.
2. Click Confirm.
3. Go to the next step.

1. Scroll down to line 30.
2. For the "enableDataQualityResultsPublishing" variable, to replace the True value, type False.
- Line 30 should now look similar to the screenshot example.
3. At the top of the page, click Save.
4. Go to the next step.

1. In the success alert, review the message.
2. Click Run.
3. To review the job status, click the Runs tab.
4. Go to the next step.

1. In the success alert, review the message.
2. On the Runs tab, under Run status, review to confirm that the job is Running, and then wait for the status to change to Succeeded.
- You might need to click the refresh icon.
3. Go to the next step.

1. In the top navigation bar search box, type: s3	
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the Buckets section, select (highlight) and copy the name of the bucket that starts with data-lake-bucket, and then paste it to the text editor of your choice on your device. 
- You use the bucket name in a later step.
2. Go to the next step.

1. In the top navigation bar search box, type: athena	
2. In the search results, under Services, click Athena.
3. Go to the next step.

1. On the Amazon Athena console home page, under Get started, choose Query your data with Trino SQL.
2. Click Launch query editor.
- You might have navigated directly to the Query editor page in the previous step.
3. Go to the next step.
- One or more query tabs, from other labs, might already be open. You can safely close these tabs.

1. On the Editor tab, in the left Data window, review to confirm that the following are selected:
For Data source: AwsDataCatalog
For Database: glue_ticket_db
2. Under Tables and views, review to confirm that glue-etl-ticket-table is listed (You won't see the dynamodbtickettable table bcs Athena deals with S3).
3. Click the Settings tab.
4. Go to the next step.

1. In the Query result and encryption settings section, click Manage.
2. Go to the next step.

1. For Location of query result, click Browse S3.
2. Go to the next step.

1. In the pop-up box, choose the radio button to select the bucket name that starts with athena-bucket-.
2. Click Choose.
3. Go to the next step.

1. Click Save.
2. Go to the next step.

1. Click the Editor tab.
2. In the top query terminal window, paste the Query 1 contents from the lab file that you downloaded at the beginning of the lab.
3. For external_location, to replace <DATE_LAKE_BUCKET_NAME>, paste the bucket name that you copied in an earlier step.
4. Click Run.
5. On the bottom Query results tab, review to confirm that the query was successful.
6. Go to the next step.

1. In the top query terminal window, click the plus sign (+) to create a new query.
2. In the new query terminal, paste the Query 2 contents from the downloaded lab file.
3. Click Run.
4. Go to the next step.

1. On the Query results tab, review the results of your query.  
2. In the left side panel, click the menu icon (three lines) to expand the navigation pane.
3. Go to the next step.

# Method 2
# (Since I could not download the function as mentioned in the Prerequisite section, you will have to come with a function that can achieve this and then complete the lab)
1. In the left navigation pane, click Data sources and catalogs.
2. Go to the next step.

1. In the Data sources section, click Create data source.
2. Go to the next step.

1. In the Choose a data source step, in the Data sources search box, type:

custom

2. Choose Custom or shared connector.
3. Click Next.
4. Go to the next step.

1. In the Enter data source details step, for Data source name, type: athena-federated-dynamodb
2. Scroll down to the bottom of the page.
3. Go to the next step.

1. For Lambda function, choose athena_connector_function. 
2. Click Next.
3. Go to the next step.

1. In the Review and create step, at the bottom of the page, click Create data source.
2. Go to the next step.

1. Review the athena-federated-dynamodb data source and its default database.
- You can ignore the connection not found error alert.
2. In the left navigation pane, click Query editor.
3. Go to the next step.

1. On the Editor tab, in the Data pane, for Data source, choose athena-federated-dynamodb.
2. Go to the next step.

1. For Database, choose default. 
2. In the top query terminal window, paste the Query 3. contents from the downloaded lab file.

- For a simple query, the FROM line does not require the fully qualified name (FQN) that we use here. However, you must use the FQN in the upcoming DIY section. The FQN follows the format of "Data_source"."database_name"."table_name". For example,  "athena-federated-dynamodb"."default"."dynamodbtickettable".

3. Click Run.
4. Go to the next step.

1. On the Query results tab, review to confirm that you received the same results as before.
2. Go to the next step.

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
- Create a copy of the DDB ticket table by using th "crate table as" (CTAS) command

- Include an external_location in a folder called "newtable" in the data-lake-bucket in S3 

# Hints
- Use the FQN for the FROM table and new Table bcs this is a federated query
- Which is "AwsDataCatalog.glue_ticket_db.newDIYTableV2" for the new and frm where to create it as "athena-federated-dynamodb"."default"."dynamodbtickettable"
- Include an external_location in a folder called "newtable" in the data-lake-bucket in S3
- Use the SQL command below

CREATE TABLE AwsDataCatalog.glue_ticket_db.newDIYTable
WITH (
        external_location = 's3://data-lake-bucket-cb998c00/newtable'
     )
AS SELECT * 
FROM "athena-federated-dynamodb"."default"."dynamodbtickettable" ;

