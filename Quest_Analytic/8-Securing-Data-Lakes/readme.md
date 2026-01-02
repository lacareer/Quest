<!-- Lab Summary -->
- Use Amazon Athena to query nested JSON data stored in S3
- Create an AWS Glue job to flatten the data, and use Athena to query the flatten data
- Use Redshift Spectrum to query the external flatten tables in Amazon Redshift
- Create and use a materializd view to query data, noting the faster response time

<!-- Prerequisite -->
-  Create 3 IAM users: opsUser, opsDirector, and opsManager
-  Create an IAM group Operations-Athena-Users and assign the users to it and grant them aws managed policy AmazonAthenaFullAccess and add the inlinePolicy.json to the permissions
-  Create an s3 bucket named: operations-datalake-1234567890
-  Upload files to customerData.csv and employeeData.csv using the path below:
    - operations-datalake-28223b20/input/customer/customerData.csv
    - operations-datalake-28223b20/input/employee/employeeData.csv

<!-- Lab instructions -->
1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3. 
3. Go to the next step.

1. On the General purpose buckets tab, click the bucket name that starts with operations-datalake-.
2. Go to the next step.

1. On the Objects tab, click the input/ folder.
2. Go to the next step.

1. On the Objects tab, navigate between the customer and employee folders.
- Each folder contains one CSV file. These files are the source data for the data lake.
2. Go to the next step.

1. In the top navigation bar search box, type: glue
2. In the search results, under Services, click AWS Glue. 
3. Go to the next step.

1. In the left navigation pane, click to Crawlers.
- You may need to click Data Catalog to expand the submenu. 
2. Click Create crawler.
3. Go to the next step.

1. In the Set crawler properties step, for Name, type: OpsIngestionCrawler
2. Click Next.
3. Go to the next step.


1. In the Choose data sources and classifiers step, for "Is your data already mapped to Glue tables?", choose Not yet if not already chosen.
2. For Data sources, click Add a data source.
3. Go to the next step. 

1. In the pop-up box, for Data source, on the dropdown list, choose S3 if not already chosen.
2. For S3 path, click Browse S3.
3. In the Choose S3 path popup box, choose the radio button to select the operations-datalake bucket (not shown).
4. Review that you chose the correct S3 path.
5. Click Add an S3 data source.
6. Go to the next step. 

1. Click Next.
2. Go to the next step.

1. In the Configure security settings step, for Existing IAM role, choose OpsIngestionCrawlerRole.
2. Click Next.
3. Go to the next step. 


1. In the Set output and scheduling step, for Target database, click Add database.  
- This opens a new browser tab (or window). Keep this browser tab open. 
2. Go to the next step.


1. For Name, type: ops_data_ingestion
2. Click Create database. 
3. Go to the next step.

1. In the Databases section, review to confirm that the new database is displayed. 
2. Go to the next step. 

1. In the previous browser tab, for Target database, click the refresh button.
2. Use the dropdown, to choose the database that you just created. 
3. In the Crawler schedule section, for Frequency, review to confirm that On demand is chosen. 
4. Click Next. 
5. Go to the next step. 


1. In the Review and create step, review all the crawler settings. 
2. Scroll down to the bottom of the page, and then click Create crawler (not shown).
3. Go to the next step. 

1. In the success alert, review the message. 
2. Go to the next step. 


1. On the OpsIngestionCrawler page, click Run crawler.
2. On the Crawler runs tab, under status, review to confirm that the status changes to Completed.

- Wait until the status changes if needed.

3. Under Table changes, review the changes.
4. Navigate to the AWS Glue console home page. 
5. Go to the next step. 

1. In the left navigation pane, click Tables.
2. Go to the next step. 

1. In the Tables section, click the table that starts with operations_datalake_. 
- If the table is not displayed, click the refresh icon.
2. Go to the next step. 

1. On the Table details tab, review the details.
2. Scroll down to the Schema tab.
3. Go to the next step. 

1. On the Schema tab, review the eight columns added to the table.
- Ignore the partitions.
- The remaining lab steps enable restrictions on the following columns:
	- employee_id
	- social_security
	- checking_account
	- routing_number
2. Go to the next step.

1. In the top navigation bar search box, type:lake form
2. In the search results, under Services, click AWS Lake Formation. 
3. Go to the next step.

1. In the pop-up box, for Choose the initial administrative users and roles, keep the default choice of Add myself.
2. Click Get started.
3. Go to the next step.

1. In the left navigation pane, click Tables.
2. In the Tables section, review the chosen default catalog.
3. Under Name, click the table name that starts with operations_datalake_.
4. Go to the next step.

1. In the Table details section, review the details.
2. On the Schema tab, review the table schema.
3. Click Actions to expand the dropdown list.
4. Choose Grant.
5. Go to the next step.

- You can safely ignore the permission error alert in the next few steps.

1. In the Principals section, keep the default choice of IAM users and roles.
2. For IAM users and roles, click to expand the dropdown menu.
3. Choose opsUser.
4. Go to the next step.


1. In the LF-Tags or catalog resources section, choose Named Data Catalog resources.
2. For Catalogs, review to confirm that Default catalog is selected (I noticed, in opsUser case, not selecting is what worked. Appears to be the default).
3. For Databases, review to confirm that the ops_data_ingestion database is selected.
4. For Tables, review to confirm that the table that starts with operations_datalake_ is selected.
5. Go to the next step.

1. For Data filters, click Create new.
2. Go to the next step.

1. In the pop-up box, for Data filter name, type: ops_filter
2. Go to the next step.

1. For Column-level access, choose Exclude columns.
2. For Excluded columns, choose the check boxes to select checking_account, employee_id, routing_number, and social_security.
3. Go to the next step.

1. Choose Filter rows.
2. For Row filter expression, type: true
3. Click Create filter.
4. Go to the next step.

1. For Data filters, choose ops_filter.
2. In the Data filter permissions section, for Data filter permissions, choose Select.
3. For Grantable permissions, choose Select.
4. Scroll down to the bottom of the page, and then click Grant (not shown).
5. Go to the next step.

# Use these steps for DIY
1. In the success alert, review the message.
2. In the left navigation pane, click Data permissions.
3. In the Data permissions section, click Grant.
4. Go to the next step.

1. In the Principals section, keep the default choice of IAM users and roles.
2. For IAM users and roles, choose opsDirector.
3. Go to the next step.

1. In the LF-Tags or catalog resources section, choose Named data catalog resources.
2. For Catalogs, review to confirm that Default catalog is selected.
3. For Databases, review to confirm that the ops_data_ingestion database is selected.
4. For Tables, review to confirm that the table that starts with operations_datalake_ is selected.
5. Scroll down to Table permissions.
6. Go to the next step.

1. For Table permissions, choose Select.
2. For Data permissions, choose All data access.
3. Scroll down to the bottom of the page, and then click Grant (not shown).
4. Go to the next step.

1. In the left navigation menu, under Permissions, click Data permissions.
2. In the Data permissions section, choose the IAMAllowedPrincipals entry with the Database resource type.
3. Click Revoke.
4. Go to the next step.


1. In the pop-up box, click Revoke.
2. Go to the next step.


1. In the Data permissions section, choose the next IAMAllowedPrincipals entry.
2. Click Revoke.
3. Go to the next step.

1. In the pop-up box, click Revoke.
2. Go to the next step.

1. On the top navigation bar, click the user icon to expand the menu.
2. Click Sign out.
3. Go to the next step.

1. In a new browser tab (or window) address bar, paste the URL that you copied in an earlier step and press Enter.
2. For IAM user name, type:

opsUser

3. For Password, type: 

Lab1234! (OR WHATEVER THE PASSWORD IS)

- Note the capital L and the ! in the password.

4. Click Sign in.
5. Go to the next step.


1. On the top navigation bar, review the Region selector to confirm that it is set to United States (N. Virginia). 
2. In the top navigation bar search box, type: athena
3. In the search results, under Services, click Athena. 
4. Go to the next step.
- If the Athena welcome page appears, click Query editor in the left navigation pane or "Launch query editor" (not shown).


1. On the Editor tab, in the Data pane, under Tables, next to the operations_datalake table, click the vertical ellipsis (three dots) to expand the menu.
2. Choose Preview Table.
- The query might already be open in the editor. If it is, you can use this query instead.
3. In the query editor, change the limit to 100. 
4. Click Run. (Or, Run again.)
5. Go to the next step.

1. Scroll down to the Query results tab.
2. Review the query results.
- The columns that were restricted in the previous step should not be displayed.
3. On the top navigation bar, click the user icon to expand the menu.
4. Click Sign out.
5. Go to the next step.

1. In a new browser tab (or window) address bar, paste the URL that you copied in an earlier step and press Enter.
2. For IAM user name, type:

opsDirector

3. For Password, type: 

Lab1234! (OR WHATEVER THE PASSWORD IS)

- Note the capital L and the ! in the password.

4. Click Sign in.
5. Go to the next step.

1. On the top navigation bar, review the Region selector to confirm that it is set to N. Virginia (us-east-1). 
2. Navigate to the Amazon Athena console.
- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
3. Go to the next step.


- You can click Run if the previous query is still open in the query editor. If not, use the following instructions, which are the same as the previous query:

1. On the editor tab, in the Data pane, under Tables, next to the operations_datalake table, click the vertical ellipsis (three dots) to expand the menu.
2. Choose Preview Table.
3. In the query editor, change the limit to 100. 
4. Click Run. (Or, Run again.)
5. Go to the next step.


1. Scroll down to the Query results tab.
2. Review the query results.
- All columns should be displayed, even the columns that were restricted for the opsUser.
3. Log out of the console before moving to the DIY section (not shown).
4. Go to the next step.

Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->
Grant "opsMannager" access to all data

# Hints
1. In the success alert, review the message.
2. In the left navigation pane, click Data permissions.
3. In the Data permissions section, click Grant.
4. Go to the next step.

1. In the Principals section, keep the default choice of IAM users and roles.
2. For IAM users and roles, choose opsDirector.
3. Go to the next step.

1. In the LF-Tags or catalog resources section, choose Named data catalog resources.
2. For Catalogs, review to confirm that Default catalog is selected.
3. For Databases, review to confirm that the ops_data_ingestion database is selected.
4. For Tables, review to confirm that the table that starts with operations_datalake_ is selected.
5. Scroll down to Table permissions.
6. Go to the next step.

1. For Table permissions, choose Select.
2. For Data permissions, choose All data access.
3. Scroll down to the bottom of the page, and then click Grant (not shown).
4. Go to the next step.

# test
1. In a new browser tab (or window) address bar, paste the URL that you copied in an earlier step and press Enter.
2. For IAM user name, type:

opsDirector

3. For Password, type: 

Lab1234! (OR WHATEVER THE PASSWORD IS)

- Note the capital L and the ! in the password.

4. Click Sign in.
5. Go to the next step.

1. On the top navigation bar, review the Region selector to confirm that it is set to N. Virginia (us-east-1). 
2. Navigate to the Amazon Athena console.
- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
3. Go to the next step.


- You can click Run if the previous query is still open in the query editor. If not, use the following instructions, which are the same as the previous query:

1. On the editor tab, in the Data pane, under Tables, next to the operations_datalake table, click the vertical ellipsis (three dots) to expand the menu.
2. Choose Preview Table.
3. In the query editor, change the limit to 100. 
4. Click Run. (Or, Run again.)
5. Go to the next step.


1. Scroll down to the Query results tab.
2. Review the query results.
- All columns should be displayed, even the columns that were restricted for the opsUser.
3. Log out of the console before moving to the DIY section (not shown).
4. Go to the next step.