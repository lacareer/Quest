<!-- Summary -->





<!-- Prequisites -->
- Deploy a VPC called: LabVpc
- Create 2 S3 buckets:
  - staging-bucket-1234567890
  - landing-bucket-1234567890
- Upload sample_data-2025-12-25-17-24.json to landing-bucket-1234567890
- Create a RedShft Cluster: toll-cluster ( I am not sure why you have to do this to open the RdShift Query editor with name/password as toll_db/admin)
- Create a secret in secret manager to store Redshift creds like below in 

  {
    "dbClusterIdentifier":"toll-cluster-186526355503-us-east-1",
    "password":"5H.+F2-d))rJl.$4coj_:4H%F{7)BV",
    "dbname":"toll_db",
    "engine":"redshift",
    "port":5439,
    "host":"toll-cluster-186526355503-us-east-1.crgb97iawjlr.us-east-1.redshift.amazonaws.com",
    "username":"admin"
  }

- Create a Glue crawler called "s3_crawler" that points to the landing-bucket-1234567890 and uses the AWSGlueServiceRole-Lab role
- Create a Glue Workflow(Orchestration) that runs the crawler s3_crawler. Steps:
      1. For Workflow name, type: Lab-Workflow
      2. Click to expand Properties.
      3. For Max concurrency, type: 2
      4. Scroll down to the bottom of the page, and then click Create workflow (not shown).
      - The new workflow should now be displayed on the Workflows page.
      5. Go to the next step.

      1. Click Lab-Workflow.
      2. Go to the next step.

      1. On the Graph tab, click Add trigger.
      2. Go to the next step.

      1. In the pop-up box, click the Add new tab.
      2. For Name, type: lab-workflows-start
      3. For Trigger type, choose On demand (can also be event based).
      4. Click Add.


<!-- Lab instructions -->
1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the Buckets section, review the lab-provided buckets stored in Amazon S3.
- The landing-bucket S3 bucket receives data from the toll plaza application.
- The staging-bucket S3 bucket receives data from the AWS Glue job.
2. Click the S3 bucket name that starts with landing-bucket-.
3. Go to the next step.

1. On the Objects tab, review the preloaded sample JSON file.

- The sample JSON file contains toll plaza transactions.
- Sample data:

{'transaction_id': 15884, 'transaction_date': '2022/09/02', 'toll_booth': '82nd_st', 'vehicle_make': 'Chevrolet', 'vehicle_category': 'Hatchback', 'transaction_amount': 6.82}

2. Click the Properties tab.
3. Go to the next step.

1. Scroll down to Event notifications.
2. Click Create event notification.
3. Go to the next step.

1. For Event name, type: s3Events
2. For Suffix, type: .json
3. For Object creation, choose Put.
4. Scroll down to the bottom of the page.
5. Go to the next step.

1. In the Destination section, review the default selections.
- The destination is an AWS Lambda function, and you choose from your Lambda functions.
2. For Lambda function, on the dropdown list, choose start_workflow_function.
3. Click Save changes.
4. Go to the next step.

1. In the top navigation bar search box, type: redshift
2. In the search results, under Services, click Amazon Redshift.
3. Go to the next step.

1. On the top navigation bar, review the Region selector to confirm that it is set to N. Virginia.
2. In the left navigation pane, click Clusters.
3. In the Clusters section, click the cluster name that starts with toll-cluster-.
4. Go to the next step.

1. On the toll-cluster- page, in the General information section, review the details.
- The section includes useful information, such as node type, endpoint, and JDBC URL.
2. Click Query data to expand the dropdown list.
3. Choose Query in the query editor.
4. Go to the next step.

1. On the Editor tab, click Connect to database.
2. Go to the next step.

1. In the pop-up box, for Connection, choose Create a new connection.

- If the pop-up box does not appear, click Change connection.

2. For Authentication, choose Temporary credentials.
3. For Cluster, choose the cluster name that starts with toll-cluster-.
4. For Database name, type:

toll_db

5. For Database user, type:

admin

6. Click Connect.
7. Go to the next step.

1. In the Resources pane, for Select database, choose toll_db.
2. For Select schema, choose public.
3. In the query editor terminal window, paste the SQL code from the lab file that you downloaded at the beginning of the lab.
4. Click Run.
5. Go to the next step.

1. In the Resources pane, review the table that you created.
2. Go to the next step.

1. Navigate to the AWS Secrets Manager console.

- Remember, on the top navigation bar, you can click Services (or use the Services search box) to navigate to a different service console.

2. In the left navigation pane, click Secrets.
3. In the Secrets section, click the secret name that starts with tollclusterSecret.
4. Go to the next step.

1. Scroll down to Secret value.
2. Click Retrieve secret value.
3. Go to the next step.

1. On the Key/value tab, review the Amazon Redshift details.
2. Go to the next step.

1. Navigate to the Amazon VPC console.
2. In the left navigation pane, under PrivateLink and Lattice, click Endpoints.
3. Click Create endpoint.
4. Go to the next step.

1. Under Type, choose AWS services.
2. Scroll down to Services. 
3. Go to the next step.

1. In the Search box, type s3 and press Enter.
2. Choose the com.amazonaws-us-east-1.s3 option with type Gateway.

- Be sure to select the Gateway type, not the Interface type.

2. Under VPC, choose LabVPC.
3. Go to the next step.

1. Scroll down to Route tables.
2. Choose the publicSubnet1 route table.
3. Under Policy, review to ensure Full access is chosen.
4. Scroll down to the bottom of the page and click Create endpoint (not shown).
5. Go to the next step.

1. Navigate to the AWS Glue console.
2. In the left navigation pane, click Data connections.
3. In the Connections section, click Create connection.
4. Go to the next step.

1. In the Choose data source step, for Data sources, type:

redshift

2. Choose Amazon Redshift.

- You can safely ignore any glue:DescribeConnectionType permission error alert if it appears in this or any further steps.

3. Click Next.
4. Go to the next step.

1. In the Configure connection step, for Database instances, choose the database name that starts with toll-cluster-.
2. For Database name, review to confirm that the name is toll_db.
3. For Credential type, choose AWS Secrets Manager.
4. For AWS Secret, choose the secret name that starts with tollclusterSecret.
5. For IAM service role, choose AWSGlueServiceRole-Lab.
6. Click Next.
7. Go to the next step.

1. In the Set properties step, for Name, type:

redshift_conn

2. Click Next.
3. Go to the next step.

1. In the Review and Create step, at the bottom of the page, click Create connection.
2. Go to the next step.

1. In the success alert, review the message.

- It might take up to 5 minutes for the connection to be ready.

2. Go to the next step.

1. In the left navigation pane, under Data Catalog, click Crawlers.
2. In the Crawlers section, review the available s3_crawler.

- This lab-provided s3_crawler adds a Data Catalog for JSON data in an S3 bucket.

3. Click Create crawler.
4. Go to the next step.


1. In the Set crawler properties step, for Name, type:

Redshift-Crawler

2. Click Next.
3. Go to the next step.

1. In the Choose data sources and classifiers step, for Data sources, click Add a data source.
2. Go to the next step.

1. In the pop-up box, for Data source, choose Redshift.
2. For Connection, choose redshift_conn.
3. For Include path, type:

toll_db/public/%

- You can substitute the percent (%) character for a schema or table. 
- For databases that support schemas, you can enter MyDatabase/MySchema/% to match all tables in MySchema within MyDatabase. 

4. Click Add a Redshift data source.
5. Go to the next step.

1. In the Data sources list, review the newly added JDBC connection. 
2. Click Next.
3. Go to the next step.

1. In the Configure security settings step, for Existing IAM role, choose AWSGlueServiceRole-Lab.
2. Click Next.
3. Go to the next step.

1. In the Set output and scheduling step, for Target database, choose toll-raw-db.
2. For Frequency, choose On demand.
3. Click Next.
4. Go to the next step.


1. In the Review and create step, review the settings.
2. Click Create crawler.
3. Go to the next step.

1. In the success alert, review the message.
2. Click Run crawler.

- In the Crawler properties section, under State, the crawler's state cycles through Starting, Running, Stopping, and Ready, which might take up to 5 minutes.

3. Click the refresh icon after starting the crawler, and then click it periodically until the state changes back to Ready.
4. Go to the next step.


1. On the Crawler runs tab, review to confirm that the Redshift-Crawler run was completed and that 1 table was created.
2. In the left navigation pane, click Tables.
3. Go to the next step.

1. In the Tables section, review the two available tables and classifications.
2. In the left navigation pane, click ETL jobs.
3. Go to the next step.

1. In the Create job section, choose Visual ETL.
2. Go to the next step.

1. On the Visual tab, under Add nodes, on the Sources tab, click Amazon S3.

- If you do not see the Add nodes window, click the plus sign (+).

2. Go to the next step.

1. On the right node panel, for S3 source type, choose Data Catalog table.
2. For Database, choose toll-raw-db.
3. For Table, choose the table name that starts with landing_bucket_.
4. On the left Visual job editor canvas, click the plus sign (+).
5. Go to the next step.


1. Under Add nodes, on the Transforms tab, click Change Schema.
2. On the right node panel, for the transaction_id source key, under Data type, choose bigint.
3. On the left Visual job editor canvas, to add another node, click the plus sign (+) (not shown).
4. Go to the next step.

1. Under Add nodes, on the Targets tab, click Amazon Redshift.

- You can safely ignore the permission error alert.

2. On the right node panel, for Node parents, choose Change Schema.
3. For Redshift access type, choose Glue Data Catalog tables.
4. For Database, choose toll-raw-db.
5. For Table, choose toll_db_public_toll_table.
6. Scroll down to Performance and security.
7. Go to the next step.


1. Click to expand Performance and security.
2. For S3 staging directory, click Browse S3.
3. In the pop-up box (not shown), choose the radio button to select the bucket name that starts with staging-bucket-.
4. On the top tab ribbon, click the Job details tab.
5. Go to the next step.

1. For Name, type:

s3_to_redshift_job

2. For IAM Role, choose AWSGlueServiceRole-Lab.
3. For Glue version, choose Glue 5.0.
4. Scroll down to Requested number of workers.
5. Go to the next step.

1. For Requested number of workers, type:

3

2. For Number of retries, type:

1

3. For Job timeout (minutes), type:

15

4. Click to expand Advanced properties.
5. Go to the next step.


1. Under Advanced properties, review the default settings.
2. Clear the check box to deselect Job metrics and Job observability metrics.
3. At the top of the page, click Save.
4. Go to the next step.

1. In the success alert, review the message.
2. Go to the next step.

1. In the left navigation pane, under Data Integration and ETL, click Workflows (orchestration).
2. In the Workflows section, review the available workflow.

- Lab-Workflow runs the s3_crawler to create a table.

3. Click Add workflow.
4. Go to the next step.

1. For Workflow name, type:

redshift_workflow

2. Click to expand Properties.
3. For Max concurrency, type:

2

4. Scroll down to the bottom of the page, and then click Create workflow (not shown).

- The new workflow should now be displayed on the Workflows page.

5. Go to the next step.

1. Click redshift_workflow.
2. Go to the next step.


1. On the Graph tab, click Add trigger.
2. Go to the next step.

1. In the pop-up box, click the Add new tab.
2. For Name, type:

redshift-workflows-start

3. For Trigger type, choose On demand.
4. Click Add.
5. Go to the next step.

1. On the workflow canvas, click Add node.
2. Go to the next step.


1. In the pop-up box, click the Crawlers tab.
2. Choose the check box to select s3_crawler.
3. Click Add.
4. Go to the next step.

1. On the workflow canvas, click the s3_crawler node.
2. Click Add trigger.
3. Go to the next step.

1. In the pop-up box, click the Add new tab.
2. For Name, type:

s3-crawler-event

3. For Trigger type, choose Event.
4. For Trigger logic, choose Start after ANY watched event.
5. Scroll down to the bottom of the pop-up box, and then click Add (Not shown).
6. Go to the next step.

1. On the workflow canvas, click Add node.
2. Go to the next step.

1. In the pop-up box, click the Jobs tab.
2. Choose the check box to select s3_to_redshift_job.
3. Click Add.
4. Go to the next step.

1. To review the workflow, click anywhere on the workflow canvas.
- This workflow is started by an S3 event notification, which starts s3_crawler. When completed, the AWS Glue crawler event runs s3_to_redshift_jobs.
2. Go to the next step.

1. In the top navigation bar search box, type: lambda
2. In the search results, under Services, click Lambda.
3. Go to the next step.

1. In the left navigation pane, click Functions.
2. In the Functions section, click Toll_Plaza_Application.
3. Go to the next step.

1. Scroll down to the Code tab.
2. Click Test to expand the dropdown list.
3. Choose Create new test event.
4. Go to the next step.

1. In the pop-up box, for Event name, type:

TestEvent

2. Click Save.
3. Go to the next step.

1. Click Test.
2. Choose TestEvent.
3. In the Execution results window, review the results.
4. Go to the next step.

1. Navigate to the redshift_workflow page on the AWS Glue console.
2. Click the History tab.
3. Review the workflow run information.

- The workflow run status might take a few minutes to change from Running to Completed.

4. Go to the next step.

1. Navigate to the Query editor page on the Amazon Redshift console.
2. On the Editor tab, click Connect to database.
3. Go to the next page.

1. In the Resources pane, next to toll-table, click the ellipsis icon (three dots) to expand the dropdown list.
2. Choose Preview data.
3. Go to the next step.

1. On the Table details tab, review the toll_table details.
2. Go to the next step.

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
Enable the "Job observability metrics" feature for s3_to_redshift_job in th AWS Glue job

# Hints
- Go to AWS Glue, under Data Ingestion and ETL click ETL jobs
- Click s3_to_redshift_job
- Click the Job details tab
- Click to expand Advanced properties
- Under Advanced properties, select the check box for Job observability metrics

Rerun the Toll_Plaza_Appliation lambda again to see the event driven ETL
