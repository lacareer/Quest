<!-- Learn -->
This solution uses AWS Glue to extract, transform, and load data from RDS to S3. It then uses Athena to run on-demand queries.

# Batch Extraction from RDS to S3 using AWS Glue and Athena
This solution demonstrates how to use AWS Glue to perform batch extraction of data from an Amazon RDS database and store it in Amazon S3. Once the data is in S3, Amazon Athena can be used to run SQL queries on the extracted data.
AWS Glue crawler is usd to extract raw data from RDS. The schema is inferred and imported into AWS Glue Data Catalog


Users run  queries, as needed, on the data byu using the Athena query e ditor which retrieves the schema info from Data Catalog

<!-- Lab prerequisites -->
- Create a Database Security Group for your Aurora RDS. 
  1. Inbound rule:
    Type: MYSQL/Aurora
    Protocol: TCP
    Port Range: 3306
    Source: 0.0.0.0/0
  2.outbound rule
    Type: All traffic
    Protocol: All
    Port Range: All
    Source:0.0.0.0/0 
- Create an Aurora RDS named: sales-database-cluster (This RDS contains 2 tables: sales_customers and sales_transactions). Prepopulat this tables with info using below

  sale_customer table schema info: 
      address
      last_name
      dod
      customer_id
      first_name
      email

  sales_transaction table schema info (note the join by customer ID):

      transaction_id
      transaction_date
      product_price
      customer_id
      product_name  

- Create 2 s3 buckets: raw-bucket-1234567890 and processed-bucket-1234567890
- Create a similar role for Glue name GlueRole-1234567890 and using GlueRole-1234567890.json file in tis folder
- Create your RDS secret in secret manager like below:
{"dbClusterIdentifier":"sales-database-cluster","password":"LejX.mUHvS,apH8kqzF_lBp51MtCcH","dbname":"sales","engine":"mysql","port":3306,"host":"sales-database-cluster.cluster-c5sblmgwoury.us-east-1.rds.amazonaws.com","username":"clusteradmin"}

<!-- Lab instructions -->

1. On the top navigation bar, review the Region selector to ensure that the Region is set to N. Virginia (us-east-1).
2. In the Services search box, type: secrets
3. In the search results, under Services, click Secrets Manager.
- The Amazon Relational Database Service (Amazon RDS) credentials that you need for this lab are saved in Secrets Manager.
4. Go to the next step.

1. Under Secret name, click the name that starts with  batchdatasalesClusterSecret.
2. Go to the next step.

1. Scroll down to Secret value.
2. Click Retrieve secret value.
3. Go to the next step.

1. On the Key/value tab, for password, click the copy icon to copy the password to a local text editor.
- You will use this password in later steps. Note the other details of your Amazon RDS cluster. (You do not need these details for this lab, but it is useful to know where they can be found.)
2. Go to the next step.

1. In the top navigation bar search box, type: rds
2. In the search results, under Services, click Aurora and RDS.
3. Go to the next step.

1. In the left navigation pane, click Databases.
2. In the Databases section, under DB identifier, click the identifier for the Writer instance role.
3. On the Connectivity & security tab, scroll down to Subnets.
4. Go to the next step.

1. Under VPC, highlight and copy just the VPC ID to the text editor of your choice on your device.
2. Under Subnets, highlight and copy the two provided subnet IDs to your text editor.
- You will use the VPC ID and subnet IDs in later steps.
3. Under VPC security groups, click the provided security group.
4. Go to the next step.

1. With RDS Security Group selected, click the Inbound rules tab.
2. Click Edit inbound rules.
3. Go to the next step.

1. In the Inbound rules section, click Add rule.
2. Go to the next step.

1. To configure the new rule, for Type, on the dropdown menu, choose All TCP.
2. For Source, choose Custom.
3. In the Custom search box, choose the name that starts with Database Security Group.
4. Click Save rules.
5. Go to the next step.

1. In the top navigation bar search box, type: glue
2. In the search results, under Services, click AWS  Glue.
3. Go to the next step.

1. In the left navigation pane, click Databases.
2. In the Databases section, click Add database.
3. Go to the next step.

1. For Name, type: batch-db
2. Click Create database.
3. In the left navigation pane, click Connections.
- You are redirected to the AWS Glue Studio Connectors page.
4. Go to the next step.

1. Scroll down to Connections.
2. Click Create connection.
3. Go to the next step.

1. In the Choose data source step, for Data sources, choose Amazon Aurora.
2. Scroll down to the bottom of the page, and then click Next (not shown).
3. Go to the next step.

1. In the Configure connection step, for Database instances, choose sales-database-instance-writer.
2. For Credential type, choose Username and password.
3. For password, paste the password that you copied in an earlier step.
4. Click to expand Network options.
5. Go to the next step.

1. For VPC, choose the LabVPC ID.
- You copied this VPC ID to your text editor in an earlier step.
2. For Subnet, choose one of the two database subnet IDs.
- You copied these subnet IDs to your text editor in an earlier step.
3. For Security groups, choose Database Security Group.
4. Click Next.
5. Go to the next step.

1. In the Set properties step, for Name, type: batch-conn
2. Click Next.
3. Go to the next step.

1. In the Review and create step, scroll down as you review the configuration details.
2. Click Create connection.
3. Go to the next step.

1. Navigate to the AWS Glue console.
- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
2. In the left navigation pane, click Tables.
3. In the Tables section, click Add tables using a crawler.
4. Go to the next step.

1. In the Set crawler properties step, for Name, type: batch-db-table
2. Click Next.
3. Go to the next step.

1. In the Choose data sources and classifiers step, for Data sources, click Add a data source.
2. Go to the next step.

1. In the pop-up box, for Data source, choose JDBC.
2. For Connection, choose batch-conn.
3. For Include path, type: sales/%
- Here, you are selecting all the tables in the sales database.
4. Click Add a JDBC data source.
5. Go to the next step.

1. Click Next.
2. Go to the next step.

1. In the Configure security settings step, for Existing IAM role, choose the role name that starts with GlueRole-.
- The crawler assumes this role, and it must have permissions similar to the AWS managed policy AWSGlueServiceRole.
2. Click Next.
3. Go to the next step.

1. In the Set output and scheduling step, for Target database, choose batch-db.
2. For Frequency, choose On demand.
3. Click Next.
4. Go to the next step.

1. In the Review and create step, review the crawler configuration.
2. Scroll down to the bottom of the page.
3. Click Create crawler.
4. Go to the next step.

1. In the success alert, review the message.
2. Click Run crawler.
3. Go to the next step.

1. On the Crawler runs tab, under Status, review the crawler status.
- The state changes from Starting > Running > Stopping > Ready.
- The Tables added/changed entry changes to 2.
- Wait until the state changes to Stopped or Ready.
- The job might take 2–6 minutes to be completed.
2. In the left navigation pane, click Tables.
3. Go to the next step.

# *FOLLOW THE STEPS HERE TO THE END TO COMPLETE DIY SECTIONS FOR sales_transactions
1. In the Tables section, review the detected tables.
2. In the left navigation pane, under Data Integration and ETL, click ETL jobs.
3. Go to the next step.

1. In the Create job section, click Visual ETL.
2. Go to the next step.

1. On the Visual tab, on the Sources tab, click AWS Glue Data Catalog.
- If the Visual job editor canvas is empty, click Add node.
2. Go to the next step.

1. On the Visual job editor canvas, click the Data Catalog node.
2. In the right node panel, on the Data source properties - Data Catalog tab, for name, type: Customer Table
3. For Database, choose batch-db.
4. For Table, choose sales_customers.
5. To add a new node, on the job editor canvas, click the plus sign (+).
6. Go to the next step.

1. On the Transforms tab, click Change Schema.
2. Go to the next step.

1. Click the Change Schema node.
2. In the right node panel, on the Transform tab, review the mapping.
3. Under Drop, choose the check box to select dob.
4. On the job editor canvas, click the plus sign (+).
5. Go to the next step.

1. In the Add nodes search box, type: s3
2. Choose Amazon S3 – Target.
- This is the data target as opposed to the source.
3. Go to the next step.

1. Click the Amazon S3 node.
2. In the right node panel, on the Data target properties - S3 tab, for Format, choose Parquet.
- Parquet is a performance-oriented, column-based data format. AWS Glue supports use of the Parquet format. 
3. For Compression Type, choose Snappy.
- Snappy focuses on high compression and decompression speed rather than the maximum compression of data.
4. For S3 Target Location, click Browse S3.
5. Go to the next step.

1. In the pop-up box, choose the radio button to select the bucket name that starts with raw-bucket-.
2. Click Choose.
3. Go to the next step.

1. Scroll down to Data Catalog update options.
2. To keep the existing schema, choose the third option (Create a table in the Data Catalog and on subsequent runs, keep existing schema and add new partitions).
3. For Database, choose batch-db.
4. For Table name, type: customers
5. Go to the next step.

1. Click the Script tab.
2. Click Edit script.
- Note that you can download the script. You can also edit the script in the editor.
3. Go to the next step.

1. In the pop-up box, review the warning message.
2. Click Confirm.
3. Go to the next step.

1. Scroll down to line 30.
2. For the "enableDataQualityResultsPublishing" variable, to replace the True value, type False.
- Line 30 should now look similar to the screenshot example.
3. Go to the next step.

1. Click the Job details tab.
2. For Name, type: Customers_Job
3. For IAM Role, choose the role that starts with GlueRole-.
4. For Glue version, choose Glue 4.0.
5. Scroll down to Requested number of workers.
6. Go to the next step.

1. For Requested number of workers, type:3
2. For Generate job insights, clear the check box.
3. Scroll down to Number of retries.
4. Go to the next step.


1. For Number of retries, type: 1
2. For Job timeout (minutes), type: 5
3. Click to expand Advanced properties.
4. Scroll down to Connections.
5. Go to the next step.

1. Under Connections, in the dropdown menu, choose batch-conn.
2. Click Save.
- You can safely ignore the S3 Block Public Access permission error alert.
3. Go to the next step.

1. In the success alert, review the message.
2. At the top of the page, click Run.
3. Go to the next step.

1. Click the Runs tab.
2. Review the recent job runs.
- The job might take 2–5 minutes to be completed. Wait until the Run status changes to Succeeded.
3. Go to the next step.

1. In the top navigation bar search box, type: athena
2. In the search results, under Services, click Athena.
3. Go to the next step.

# Don't do this next 5 steps for DIY bcaus it is alredy setup when you did this lab step
1. In the left navigation pane, click Query editor.
2. On the Query editor page, click the Settings tab.
3. Go to the next step.

1. Click Manage.
2. Go to the next step.

1. For Location of query result, click Browse S3.
2. Go to the next step.

1. In the pop-up box, choose the radio button to select the bucket name that starts with processed-bucket.
2. Click Choose.
3. Go to the next step.

1. Click Save.
2. Go to the next step.

# continue DIY
1. Click the Editor tab.
2. Review the Data source and Database values.
- Ensure that AwsDataCatalog appears under Data source and batch-db appears under Database.
3. Review the Tables section.
- You should see the customers table.
4. Go to the next step.

1. On the Editor tab, in the query editor window, type:

SELECT * FROM "batch-db"."customers" limit 10;   

# DIY Command

SELECT * FROM "batch-db"."transactions" limit 10;

2. Click Run.
3. Go to the next step.

1. Scroll down to Results.
2. Review the results.
- You should see data from the customers table.
- The table should not contain a dob column.
3. Go to the next step.

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
