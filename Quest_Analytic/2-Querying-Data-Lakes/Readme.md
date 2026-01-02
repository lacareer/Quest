<!-- Lab prerequisites -->
1. Create two buckets named:
  - transaction-ingest-1234567890
  - staging-records-2bb19530

2. Deploy the lambda, Transaction_Generator, using transaction_Generator.py file or content
  - Give  lambda the requird permissions if role errors arises.

<!-- Lab instructions  -->
1. On the top navigation bar, review the Region selector to confirm that the Region is set to N. Virginia (us-east-1).
2. In the top navigation bar search box, type: lambda
3. In the search results, under Services, click Lambda.
4. Go to the next step.

1. In the Functions section, click the Transaction_Generator function.
2. Go to the next step.

1. Scroll down to the Code source section.
2. Click Create new test event.
3. Go to the next step.

1. In the pop-up box, for Event name, type: myTestEvent
2. Click Save.
3. Click Invoke.
4. Go to the next step.

1. In the Execution Results window, under Function Logs, review to ensure that no errors occurred.
- By testing the function, you are running the code to generate test data. This data will be used in the "default" database.
2. Go to the next step.

1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the General purpose buckets section, select (highlight) and copy the bucket name that starts with transaction-ingest-, and then paste it in the text editor of your choice on your device.
- You will use this bucket name in a later step.
2. Go to the next step.

1. In the top navigation bar search box, type: athena
2. In the search results, under Services, click Athena.
3. Go to the next step.

1. If not already selected, choose Query your data with Trino SQL.
2. Click Launch query editor.
3. Go to the next step.

1. Review the message to set up a query result location.
2. Click Edit settings.
- Alternatively, you can click on the Settings tab and then click Manage to update your query result location in S3.
3. Go to the next step.

1. For Location of query result, click Browse S3.
2. Go to the next step.

1. In the pop-up window, choose the radio button to select the staging-records bucket.
2. Click Choose.
3. Go to the next step.

1. Review that the staging-records bucket is displayed.
2. Choose the checkbox to enable Encrypt query results.
3. For Encryption type, choose SSE_S3.
4. Click Save.
5. Go to the next step.

- One or more of the queries used in this lab might be prepopulated in the Athena query editor. You can use these pre-existing queries, but pay close attention to the lab instructions to change certain text as needed.

1. On your device, open the qdl_lab_queries.txt file that you downloaded in an earlier step, and then copy the SQL query in section 1 of the file (not shown).
- Leave out the lines beginning with ###.
2. To return to the Query editor, on the console, click the Editor tab.
3. In the Query editor, paste the query that you just copied.
4. Go to the next step.

1. On line 17, to replace the <YOUR_INGEST_BUCKET_NAME> placeholder text, paste the transaction-ingest bucket name that you copied in an earlier step.
- If you use a prepopulated query in the Athena query editor, you must change the LOCATION to your specific S3 bucket. Otherwise, the query will generate errors.
2. Go to the next step.

1. On the same line, at the end of what you just pasted, type: /
2. Review to ensure that the bucket name was pasted properly and the entire S3 URL is wrapped in single quotation marks.
- Your S3 URL should look similar to what is displayed in the screenshot example.
3. Click Run.
4. Go to the next step.

1. On the Query results tab, review to ensure that the query completed successfully.
- In the left Data pane, under Tables, a new table, cc_transactions, should be displayed.
- Note the three vertical dots menu next to this new table. You must use this menu in the upcoming DIY section of this solution.
2. Go to the next step.

1. On your device, in the qdl_lab_queries.txt file, copy the query from section 2 of the file (not shown).
- Leave out the lines beginning with ###.
2. On the console, on the Editor tab, click the plus sign (+) to create a new Query tab.
- Your Query tab numbers might not match those in the screenshot example.
3. On the new Query tab, paste the query that you just copied.
4. Click Run.
5. Go to the next step.

1. On the Query results tab, review to ensure that the query completed successfully.
- In the left Data pane, under Tables, a new table, sus_transactions, should be displayed.
2. Go to the next step.

1. On your device, in the qdl_lab_queries.txt file, copy the query from section 3 of the file (not shown).
- Leave out the lines beginning with ###.
2. Click the plus sign (+) to create a new Query tab.
3. On the new Query tab, paste the query that you just copied.
4. Next to the new Query tab, click the three vertical dots to expand the dropdown menu.
5. Choose Save as.
6. Go to the next step.

1. In the pop-up box, for Query name, type: Invalid_Security_Codes
2. Click Save query.
3. Go to the next step.

1. Click Run.
2. Go to the next step.

1. On the Query results tab, review to ensure that the query completed successfully.
 - Because of the randomness of the results created by the Lambda function, your results might look different than the screenshot example.
2. Go to the next step.

1. On your device, in the qdl_lab_queries.txt file, copy the query from section 4 of the file (not shown).
- Leave out the lines beginning with ###.
2. Click the plus sign (+) to create a new Query tab.
3. On the new Query tab, paste the query that you just copied.
4. Next to the new Query tab, click the three vertical dots to expand the dropdown menu.
5. Choose Save as.
6. Go to the next step.

1. In the pop-up box, for Query name, type: Diners_Club_Suspected
2. Click Save query.
3. Go to the next step.

1. Click Run.
2. Go to the next step.

1. On the Query results tab, review to ensure that the query completed successfully.
 - Because of the randomness of the results created by the Lambda function, your results might look different than the screenshot example.
2. Go to the next step.

1. To close the three latest Query tabs, click the X on each.
- This closes the sus_transactions creation query, the Invalid_Security_Codes query, and the Diners_Club_Suspected query.
2. Go to the next step.

1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the General purpose buckets section, click the bucket name that starts with staging-records-.
2. Go to the next step.

1. On the Objects tab, review the objects in the S3 bucket.
- Prefixes for the queries that you created should be displayed. All results for these queries are stored here.
2. Go to the next step.

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
Drop the sus_ransactions table

# Hints:
- Locate the table name in the left pane of Athena query editor
- Click on the vertical ellipses to the right of the table
- Choose Delete table 
- Enter name to confirm
- Click delete