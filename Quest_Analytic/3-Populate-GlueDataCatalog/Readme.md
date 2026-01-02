<!-- Learn -->

AWS Glue is a serverless data integration service for discovering, cataloging, preparing, and moving data for analytics and machine learning.

Key points:

- Purpose: ETL/ELT and metadata management for data lakes and analytics.
- Serverless: You don’t manage infrastructure; Glue scales automatically.
- Glue Data Catalog: Central metadata store for tables, schemas, and partitions (used by Athena, Redshift Spectrum, EMR).
- Crawlers & Classifiers: Automatically discover schema and populate the Data Catalog from S3, JDBC sources, etc.
- Jobs: Managed Spark-based ETL jobs (PySpark/Scala) or Python shell jobs to transform/move data.
- Glue Studio: Visual/low-code UI to author, run, and monitor ETL pipelines.
- Triggers & Workflows: Schedule or event-trigger pipelines and orchestrate multi-step flows.
- Integrations: S3, DynamoDB, RDS, Redshift, Athena, Kinesis, JDBC sources, and IAM for access control.
- Pricing: Pay for Data Processing Units (DPUs) used by jobs and crawlers; serverless billing model.
- Common uses: build/maintain data lakes, prepare data for analytics/ML, populate catalogs for query engines.
- Limitations/notes:
  Jobs run on Spark (suitable for batch/large-scale transformations); for lightweight scripting consider Lambda or Glue Python shell.
  Glue versions differ (features, Spark version) — pick version that matches your dependencies.
  Secure with IAM roles, VPC endpoints, and encryption for sensitive data.

<!-- Lab prerequisite-->
- Create 2 s3 bucket named: raw-data-1234567890 and athena-result-1234567890
- Create a lambda function using labFunction-Inventory-Management.py with an env of input_bucket = raw-data-1234567890 and python 3.12 layers using the /layers zips in this folder for below:
      faker_layeer
      numpy_layer
      pandas_layer
- create a Glue role using sample info in aws_glue_role.json file

<!-- Lab -->

1. On the top navigation bar, review the Region selector to ensure that the Region is set to United State (N. Virginia).
2. In the Services search box, type: s3 
3. In the search results, under Services, click S3.
4. Go to the next step.

1. In the left navigation pane, click Buckets.
2. In the Buckets section, select (highlight) and copy the bucket name that starts with raw-data-, and then paste it in the text editor of your choice on your device.
- You will use this bucket name in a later step.
3. Click the bucket name that starts with raw-data-.
4. Go to the next step.

1. On the Objects tab, review to ensure that the raw-data- S3 bucket contains the inventory.csv file.
- This file includes an inventory table with product information.
2. Go to the next step.

1. In the top navigation bar search box, type: glue
2. In the search results, under Services, click AWS Glue.
3. Go to the next step.

1. In the left navigation pane, click Databases.
2. Click Add database.
3. Go to the next step.

1. For Name, type: inventory-db
2. Click Create database.
3. Go to the next step.

1. In the Databases section, review to ensure that the inventory database was created.
2. In the left navigation pane, click Tables.
3. Go to the next step.

1. In the Tables section, click Add tables using crawler (this creates a table under the above DB).
2. Go to the next step.

1. In the Set crawler properties step, for Name, type: inventory-crawler
2. Click Next.
3. Go to the next step.

1. In the Choose data sources and classifiers step, for Data sources, click Add a data source.
2. Go to the next step.

1. In the pop-up box, for Data source, on the dropdown menu, choose S3.
2. To choose the location of the data source, for S3 path, click Browse S3.
3. Go to the next step.

1. Choose the radio button to select the bucket name that starts with raw-data-.
2. Click Choose.
3. Go to the next step. 

1. Under S3 path, if a "This is a required field." warning alert appears, click any empty space on the page to dismiss it.
2. Click Add an S3 data source.
3. Go to the next step.

1. Click Next.
2. Go to the next step.

1. In the Configure security settings step, for Existing IAM role, choose aws_glue_role.
2. Click Next.
3. Go to the next step.

1. In the Set output and scheduling step, for Target database, choose inventory-db.
2. Click Next.
3. Go to the next step.

1. In the Review and create step, review the settings.
2. Click Create crawler.
3. Go to the next step.

1. In the success alert, review the message.
- If you see a blue information alert about the new AWS Glue console experience, you might need to close it in order to see this green success alert.
2. To start running the crawler, click Run crawler.
4. Go to the next step.

1. In the Crawlers runs tab, click the refresh icon from time to time to view the state update.
2. Under Status, review to ensure that the crawler task state changes from Starting to Running, and then from Stopping to Ready.
- The crawler task might take a few minutes to be completed.
3. Go to the next step.

1. Review to ensure that the crawler run status changed to Completed.
2. Review the Table changes information.
3. Go to the next step.

1. In the left navigation pane, click Tables.
- Click the refresh button if the table is not listed.
2. Click the table that starts with raw_data_.
3. Go to the next step.

1. Scroll down to the Schema tab.
2. Review the schema of the table.
- AWS Glue has cataloged your S3 data in the AWS Glue Data Catalog table. 
- The table includes the metadata information, including the schema.
3. Go to the next page.

1. In the top navigation bar search box, type: athena
2. In the search results, under Services, click Athena.
3. Go to the next step.

1. If you land on the Amazon Athena console home page, review that Query your data with Trino SQL is selected.
2. Click Launch query editor.
3. Go to the next step.

1. Review the information regarding setting up a query result location.
2. Click the Query Settings tab.
3. Go to the next step.

1. For Location of query result, click Browse S3.
2. Go to the next step.

1. In the pop-up box, choose the radio button to select the S3 bucket name that starts with athena-results-.
2. Click Choose.
3. Go to the next step.

1. Click Save.
2. Go to the next step.

1. In the success alert, review the message.
2. To return to the query editor, click the Editor tab.
3. Go to the next step.

1. In the Data pane, for Database, choose inventory-db.
2. Under Tables, review to ensure that the raw_data_ table created in an earlier step is displayed.
3. Next to the table name, click the plus sign (+) to expand the table details.
4. Go to the next step.

1. Review the schema of the table.
- The table includes product_id, product_stock, and product_barcode information.
2. Next to the table name, click the vertical three dots to expand the dropdown menu.
3. Choose Preview Table.
4. Go to the next step.

1. In the query editor terminal, review the SQL query command.
- This query lists the first ten items in the inventory database.
2. Scroll down to the Query results tab.
3. Review the query results.
- The results show the data in the table.
4. Go to the next step.

1. In the top navigation bar search box, type: lambda
2. In the search results, under Services, click Lambda.
3. Go to the next step.

1. In the Functions section, click the Lambda function name that starts with labFunction-.
2. Go to the next step.

1. On the labFunction- page, click the Configuration tab.
2. Scroll down to view the tab.
3. Go to the next step.

1. Click Environment variables.
2. Click Edit.
3. Go to the next step.

1. Under Value, paste the raw-data- S3 bucket name that you copied in an earlier step.
2. Click Save.
3. Go to the next step.

1. In the success alert, review the message.
2. Click the Code tab.
3. To create a test event, click Test.
4. Choose Create new test event (not shown).
4. Go to the next step.

1. For Event name, type a name that you like, such as testEvent. 
2. For Event sharing settings, keep the default of Private.
3. For Template, choose hello-world.
4. Click Save.
5. Click Invoke
6. Go to the next step.

1. In the Execution results window, for Status, review to ensure that the test event was successfully completed. 
2. Under Function Logs, review the new data and columns in the inventory table.
- Two new columns were added: Product_city and Product_country.
- If some columns are hidden due to long product country names, you can click Test again to generate new data.
3. Go to the next step.

1. Navigate to the AWS Glue console.
- Remember, in the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
2. In the left navigation pane, click Crawlers.
3. In the Crawlers section, choose the check box to select the crawler name, inventory-crawler.
4. Click Run.
5. Go to the next step.

1. In the success alert, review the message.
2. Under State, review to ensure that the crawler task state changes from Starting to Running, and then from Stopping to Ready.
- The crawler task might take a few minutes to be completed.
3. Go to the next step.

1. Under State, review to ensure that the crawler task state changed to Ready.
2. Go to the next step.

1. In the left navigation pane, click Tables.
2. In the Tables section, click the raw_data_ table name that corresponds to the inventory_db database (under Database).
3. Go to the next step.

1. On the raw_data_ table page, review the current version.
- This should be Version 1.
2. On the Table details tab, review the table details.
3. Scroll down to the Schema tab.
4. Go to the next step.

1. Review the schema of the current table version, Version 1.
- Two columns (product_city and product_country) were added to the table.
2. Scroll up to the top of the page.
3. Go to the next step.

1. Click Version 1 (Current version) to expand the dropdown menu.
2. Review the two table versions, Version 0 and Version 1.
- You can keep track of the schema changes in your AWS Glue table.
3. Choose Version 0.
4. Scroll down to the bottom of the page.
5. Go to the next step.

1. On the Schema tab, review the schema of the previous table version, Version 0.
2. Scroll up to the top of the page.
3. Go to the next step.

1. Click Actions to expand the dropdown menu.
2. Review the Edit schema option. 
- You must use Edit schema in the upcoming DIY section of this solution.
3. Go to the next step.

1. Navigate to the Query editor page on the Amazon Athena console page.
2. On the Editor tab, in the Data pane, for the raw_data_ table, click the plus sign (+) to view the updated table schema.
3. Review to ensure that the table was updated with the two new columns.
4. Go to the next step.

1. Next to the raw_data_ table, click the vertical three dots to expand the dropdown menu.
2. Choose Preview Table.
3. Go to the next step.

1. On the Query results tab, review the updated table data with the two new columns.
- Because data is randomly generated each time, your query results might look different from what is displayed in the screenshot example.
2. Go to the next step.

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
- Modify "product id" data type from "bigint" to "string"
- Validate the updated data type in the Data Catalog and in Athena

# HINT
- Go to AWS Glue
- Under Data Catalog
- Click on Tables under Databases
- Click on the raw_data_1234567890 table name
- Click Actions on top right corner
- Pick Edit Schema
- Check the column with "product_id"
- Click Edit
- Under Data type, click "string"
- Click Save

