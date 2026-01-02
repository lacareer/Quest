<!-- Summary -->

Deploy an Amazon OpenSearch Search domain to index bank transactions. Create an AWS Glue job to process transactions generated from upstream on-premises application into OpenSearch domain

- Deploy and configurean OpenSearch domain
- Create an ETL job by using AWS Glue Studio
- Configure an ETL script to ingest Amazon S3 data in OpenSearch services
- Use OpenSearch dashboard to call the search api to query data from the OpenSearch service domain

<!-- prerequisites -->
- Create an S3 bucket named: ingestion-bucket-1234567890 and upload the two files below using the exact path below:
  - ingestion-bucket-1234567890/elasticsearch-hadoop-7.8.0.jar
  - ingestion-bucket-1234567890/input/transactions.csv.gz
- Create an IAM role using AWSGlueServiceRole-lab.json called AWSGlueServiceRole-lab

<!-- lab -->

1. In the top navigation bar search box, type: opensearch
2. In the search results, under Services, click Amazon OpenSearch Service.
3. Go to the next step.

1. On the top navigation bar, review the Region selector to ensure that the Region is set to N. Virginia (us-east-1).
2. In the left navigation pane, review to ensure the Managed clusters dashboard is selected. 
3. Click Create domain.
4. Go to the next step.


1. For Domain name, type: bank-transactions 
2. For Domain creation method, choose Standard create.
3. Scroll down to Templates.
4. Go to the next step.

1. For Templates, choose Dev/test.
2. For Deployment Option(s), choose Domain without standby.
3. For Availability Zone(s), choose 1-AZ.
4. Scroll down to Engine options.
5. Go to the next step.

1. For Version, on the dropdown menu, choose Elasticsearch 7.10.
- This lab uses version 7.10 of Elasticsearch because the open source connector that you use later in the lab supports only that version.
2. In the Data nodes section, for Instance family, choose General purpose.
3. For Instance type, choose m5.large.search.
4. For Number of nodes, type: 1
5. Scroll down to Network.
6. Go to the next step.

1. For Network, choose Public access.
2. Choose the check box to select Enable fine-grained access control.
3. Go to the next step.

1. For Master user, choose Create master user.
- Do not customize the following credentials, which are expected in this practice section and for validation in the later DIY section of this solution.
2. For Master username, type: lab-user   
3. For Master password, type: LabUserP433!		
4. For Confirm master password, type it again.
5. Scroll down to Access policy.
6. Go to the next step.


1. For Domain access policy, choose Only use fine-grained access control.
2. Scroll down to the bottom of the page, and then click Create (not shown).
- New domains typically take 15–30 minutes to initialize. While this domain is initializing, you can run the next steps in the lab. You will return later to check completion of the cluster provisioning.
3. Go to the next step. 

1. Navigate to the Amazon S3 console.
- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
2. On the General purpose buckets tab, click the bucket name that begins with ingestion-bucket-.
3. Go to the next step.

1. On the Objects tab, choose the check box to select the elasticsearch-hadoop-7.8.0.jar object.
2. Click Copy S3 URI, and then paste it in the text editor of your choice on your device.
- You will use the object's S3 URI in later steps, during the configuration of your AWS Glue job. To ingest data into OpenSearch Service, your AWS Glue job will configure this elasticsearch-hadoop JAR file as a dependency. Should look like so: s3://ingestion-bucket-1234567890/elasticsearch-hadoop-7.8.0.jar
3. Click the input/ folder.
4. Go to the next step. 

1. On the Objects tab, review to see the transactions.csv.gz object. 
- This gzipped file contains 1,000,000 sample bank transactions that you will use as the ingestion data.
2. At the top of the page, click Copy S3 URI, and then paste it in your text editor.
- You will use the folder's S3 URI, s3://ingestion-bucket-ACCOUNT-XXX/input, in later steps.
3. Go to the next step. 

1. Navigate to the AWS Glue Studio console.
2. In the left navigation pane, click ETL jobs.
3. Go to the next step.

1. In the Create job section, click Script editor.
2. Go to the next step.

1. In the pop-up box, for Engine, choose Spark.
2. For Options, choose Upload script.
3. Click Choose file, and then locate the glue_to_opensearch_job.py file that you downloaded in an earlier step. 
4. Click Create script.
5. Go to the next step. 

1. For Job Name, type: bank-transactions-ingestion-job
2. On the Script tab, review line 9.
- AWS Glue jobs can receive parameters as arguments.
- For its run, this script received es_user, es_pass, es_endpoint, and input_bucket as inputs.
3. Scroll down to line 18.
4. Go to the next step.

1. Review lines 18–38.
2. Scroll down to line 40. 
3. Go to the next step. 

1. Review the list of mappings on lines 48–60.
2. Scroll down to line 75.
3. Go to the next step. 

1. Review line 75, and then read the previous comments for this section.
- These comments are relevant for the later DIY section.
2. Review lines 77–88.
- These lines define the authentication information and the endpoint for OpenSearch Service.
- This practice lab uses the open source elasticsearch-hadoop connector.
3. Go to the next step. 

1. Click the Job details tab.
2. For IAM Role, choose AWSGlueServiceRole-lab.
3. For Glue version, choose Glue 2.0.
4. Scroll down to Job bookmarks.
5. Go to the next step.

1. For Job bookmark, choose Disable.
- By disabling Job bookmark in this practice lab, you facilitate the run in the later DIY section.
2. For Number of retries, type: 0 
3. Click to expand Advanced properties (not shown).
4. Go to the next step. 

1. Scroll down to Libraries.
2. For Dependent JARs path, paste the S3 URI that you copied in an earlier step.
- This URI is for the elasticsearch-hadoop.jar driver located in the ingestion bucket.
3. At the top of the page, click Save.
4. Go to the next step. 

- In this step, you open the Amazon OpenSearch Service console in a new browser tab while keeping the AWS Glue Studio console open in your current browser tab. You are opening two browser tabs because you will return to the AWS Glue Studio console in later steps.

1. In the top navigation bar search box, type: opensearch 
2. On your keyboard, hold down Ctrl (Windows) or Cmd (Mac), and then, in the search results, under Services, click Amazon OpenSearch Service.
- The new console should open in a new browser tab. To open the console in a new browser window, you can hold down Shift.
3. Go to the next step.

1. Click the menu icon (three lines) in the left side panel to expand the navigation pane (not shown), and then click Domains.
2. In the Domains section, under Domain processing status, review to ensure that the status is Active.  
- If the status is still Creating, wait for it to change to Active.
3. Click the bank-transactions domain.
4. Go to the next step. 

1. Under Domain endpoint (IPv4), click the copy icon to copy the provided endpoint URL.
2. Go to the next step.

1. Return to the AWS Glue Studio console in the other browser tab.
2. On the Job details tab, scroll down to Job parameters.
3. Click Add new parameter.
4. For Key, type:

 --es_endpoint

- If copying the above, be sure there is no white space before or after.

5. For Value, paste the OpenSearch Service domain endpoint URL that you just copied.
6. Go to the next step. 

1. Click to add two more parameters. 
2. For the first, for Key and Value, type: --es_user and lab-user
3. For the second, for Key and Value, type: --es_pass and LabUserP433!
4. Review to ensure that the credentials are correct.
- Your entries should look similar to what is displayed in the screenshot example.
5. Go to the next step. 

1. Click Add new parameter. 
2. For Key, type: --input_bucket
3. For Value, paste the S3 URI for the ingestion-bucket- input folder that you copied in an earlier step. 
- If needed, you can open a new browser tab and copy the URI again from your Amazon S3 console. Check that the end of the URI has no white spaces, and that it includes the "input" folder.
4. At the top of the page, click Save.
5. Click Run.
- If the job immediately fails, review the job parameter argument variables to ensure that the parameters are correct.
6. Go to the next step. 

1. Click the Runs tab.
2. Under Run status, review to see that the job successfully started and is running. 
3. Go to the next step.

1. Click the Job runs refresh icon. 
2. Under Run status, review to ensure that the status changed to Succeeded.
- The job might take 5–10 minutes to finish.
- If the job fails, review the job parameter argument variables in an earlier step to ensure that the parameters use underscores " _ " and not hyphens " - ". 
- Be sure that the user and password for authentication are also correct. 
3. Go to the next step.

<!-- I don't have the app so try using AWS cli to do the listed queries -->
1. Navigate to the Instances page on the Amazon EC2 console.
2. Choose the check box to select SearchInstance.
- This lab provisioned a sample client application on Amazon EC2 to help search the OpenSearch Service index. 
3. On the Details tab, under Public IPv4 address, click the copy icon to copy the provided public IP address for the instance.
4. Open a new browser tab, and then, in the address bar, paste the address that you just copied (not shown).
5. Go to the next step. 

1. On the Search Bank Statement page, click Search.
-  The "debit" keyword is an example query term. Try searching other terms, such as "cash" and "credit". 
2. Go to the next step. 

1. Review the search results.
- For demonstration purposes, the screenshot example limits the search results to 10. You should see similar results in your browser.
2. Go to the next step. 

1. Navigate to the Amazon OpenSearch Service console.
2. In the left navigation pane, click Domains.
3. In the Domains section, click the bank-transactions domain. 
4. Go to the next step.

1. In the General information section, under Kibana URL, click the provided URL.
2. Go to the next step. 

1. For user, type:

lab-user

2. For password, type:

LabUserP433!

3. Click Log In.
4. Go to the next step. 

- If you receive a pop-up, click Explore on my own.

1. In the Select your tenant pop-up box, choose Private.
2. Click Confirm. 
3. Go to the next step.

1. Under Manage your data, click Interact with the Elasticsearch API.
2. Go to the next step. 

1. In the query editor, review the provided query example. 
2. Above the example, click the play icon.
3. Scroll down if necessary to find a result indexed by the ingestion job. 

- This query searches all indexes in your cluster.

4. Review a document from the main-index, defined in the ETL job, and its corresponding fields.  
5. Go to the next step. 


1. After the first forward slash (/) in your GET, type:

main-index/

2. Click the play icon.
3. Review the results.
4. Go to the next step. 

1. In the query editor, copy-paste the following format query:

{
"query" : {
 "query_string" :  { 
  "query"  : "debit",
   "fields"   :  ["type"]
  }
 }
}

- If you receive an undefined value when you paste this, try again.

2. Click the play icon.
3. Review the results.
4. Go to the next step. 

1. On line 5, for the query term, type: 

credit

2. Click the play icon.
3. Review results.
4. Go to the next step. 

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
- On your TL job, change the target "balance" column to "account_balance" and the target "amount" column to "transaction_amount"
- Remove the column, k_symbol, to keep it from being indexed
- Change the index name to new-index and then re-run gthe job

# Hints
- Go to Glue job
- Click on the bank-transactions-ingestion-job job
- Click on Script editor
- On the Script tab, scroll to line 54 and make the required change: "amount" ==> "transaction_amount"
- On the Script tab, scroll to line 55 and make the required change: "balance" ==> "account_balance"
- On the Script tab, scroll to line 75 and make the required change: es_index = "new-index/transactions" ==> es_index = "main-index/transactions"

