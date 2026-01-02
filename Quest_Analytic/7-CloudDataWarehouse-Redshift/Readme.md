<!-- Lab Summary -->
- Use Amazon Athena to query nested JSON data stored in S3
- Create an AWS Glue job to flatten the data, and use Athena to query the flatten data
- Use Redshift Spectrum to query the external flatten tables in Amazon Redshift
- Create and use a materializd view to query data, noting the faster response time

<!-- Prerequisite -->
- Create a Glue role with AWS managed policy AWSGlueServiceRole and aws_glue_role.json enter inline

- Create an S3 bucket named: raw-data-1234567890 and upload the players_gamesData.json files  to it

- Create an S3 bucket name: consumption-data-1234567890 and and 2 sub-direcctories under parquet/ folder:
    - games_data/
    - players_data/

              __games_data/
              |
i.e Parquet --|__players_data/
               
- Go to AWS Glu and create 2 databases: "games-data-db" and "games-flattened-data-db". 

- Under the games-data-db DB create a table  for points to the raw-data-1234567890 bucket. Use the schema below (which is the structure in players_gamesData.json):

[
  {
    "Name": "name",
    "Type": "string"
  },
  {
    "Name": "game_details",
    "Type": "array<struct<game_name:string,high_score:int,purchased_item:string,purchases:int>>"
  },
  {
    "Name": "city",
    "Type": "string"
  },
  {
    "Name": "country",
    "Type": "string"
  }
]


The table name should be same with bucket name once created.

- In AWS Glue, create a Crawler, "games-data-crawler", that points to the raw-bucket-1234567890 

- Create Amazon Redshift Clusters "games-db-cluster"

- Create a RedShift rol using redshiftspectrumrole.json


<!-- Lab instructions -->
#  
1. On the top navigation bar, review the Region selector to ensure that the Region is set to N. Virginia (us-east-1).
2. In the Services search box, type:  s3 
3. In the search results, under Services, click S3.
4. Go to the next step.

1. On the General purpose buckets tab, select (highlight) and copy the bucket name that starts with consumption-data-, and then paste it in the text editor of your choice on your device.
- You will use this bucket name in a later step.
- The bucket is used to store the transformed data later.
3. Click the bucket name that starts with raw-data-.
4. Go to the next step.

1. On the Objects tab, review to ensure that the raw-data- S3 bucket contains the players_gamesData.json file.
- This JSON file contains one million records on game players data. 
2. Go to the next step.

1. In the top navigation bar search box, type:  glue
2. In the search results, under Services, click AWS Glue.
3. Go to the next step.

1. In the left navigation pane, click Databases.
2. In the Databases section, review the AWS Glue database named games-data-db. 
- This database is for the raw data.
3. Review the AWS Glue database named games-flattened-data-db.
- This database is for the flattened data.
4. Go to the next step.

1. In the left navigation pane, click Tables.
2. In the Tables section, select (highlight) and copy the AWS Glue table name that starts with raw-data-, and then paste it in your text editor.
- You will use this table name in a later step.
3. Click the same table name.
4. Go to the next step.

1. Scroll down to the Schema tab.
2. Review the schema of the raw data table.
- This table includes player information, including name, game_details, city, and country.
- The game_details data type is an array.
3. To view data structure details, under Data type, click array.
4. Go to the next step.

1. In the pop-up box, review the data structure of the game_details array.
- The game_details array contains information about the games that a player has played. For each game, it contains the game name, player's high score, the in-game purchased item, and its cost.
2. Click Dismiss.
3. Go to the next step.

1. In the top navigation bar search box, type:  athena
2. In the search results, under Services, click Athena.
3. Go to the next step.

1. In the left navigation pane, click Query editor.
- You might need to click the menu icon (three lines) in the left side panel to expand the navigation pane.
2. Go to the next step.

1. On the Editor tab, in the Data pane, for Database, choose games-data-db.
2. Under Tables, next to the raw_data table name, click the plus sign (+) to expand the table details.
3. Review the schema of the raw data table.

- This raw data table is in JSON format with nested data structure.

4. Next to the raw-data table name, click the three vertical dots to expand the dropdown menu.
5. Choose Preview Table.
6. On the Query results tab, click the settings icon.
7. Go to the next step.

1. In the pop up box, if not already enabled, choose the check box to select Wrap lines.
2. Click Confirm.
3. Go to the next step.

1. On the Query results tab, review the results.

- The records displayed in the screenshot example might be different from yours because the query retrieves any ten items from the database.

2. Under game_details, review the nested data structure.
3. Go to the next step. 

1. Navigate to the AWS Glue console.

- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.

2. In the left navigation pane, click ETL jobs.
3. Click Script editor.
4. Go to the next step.

1. For Engine, choose Spark.
2. For Options, choose Start fresh.
3. Click Create script.
4. Go to the next step.

1. On the Script tab, in the terminal, delete the default code.
2. Go to the next step.

1. On your device, copy the code from the AWS_Glue_Job_Script.txt file that you downloaded at the beginning of the lab, and then paste the code in the Script terminal. 
2. On line 19, replace YOUR AWS GLUE RAW DATA TABLE NAME with the AWS Glue table name that you copied in an earlier step.

- The table name begins with raw_data_.
- Be sure to keep the double quotation marks around the table name.
- This line of code creates a DynamicFrame based on the database and table in the AWS Glue Data Catalog.

3. Go to the next step.

1. On line 25, review the use of the built-in transformation, relationalize, to flatten the nested data structures.
2. On line 25, replace YOUR CONSUMPTION DATA S3 BUCKET NAME with the S3 bucket name that you copied in an earlier step.

- Be sure to keep the double quotation marks around the bucket name.

3. Go to the next step.

1. On line 44 and 45, replace YOUR CONSUMPTION DATA S3 BUCKET NAME with the S3 bucket name that you copied in an earlier step.

- You replace the placeholder twice.
- Be sure to keep the double quotation marks around the bucket name.
- After running the job, the transformed data is stored in this consumption data S3 bucket in Parquet format.

2. Go to the next step.


1. Click the Job details tab.
2. In the Basic properties section, for Name, type:

games-flattened-data-job

3. For IAM Role, choose aws_glue_role.
4. For Glue version, choose Glue 3.0.
5. At the top of the page, click Save.
6. After the job is successfully saved, click Run.
7. Go to the next step.

1. Click the Runs tab.
2. Under Run status, review to ensure that the status changed to Running.

- The job might take a few minutes to be completed. When completed, the Run status will change to Succeeded.
- You may have to click the refresh button.

3. Go to the next step.


1. Review to ensure that the Run status changed to Succeeded.
2. Go to the next step.

1. Navigate to the AWS Glue console.
2. In the left navigation pane, click Crawlers.
3. In the Crawlers section, click Create crawler.

- This crawler is used to create metadata tables for the flattened data.

4. Go to the next step.

1. In the Set crawler properties step, for Name, type:

games-flattened-data-crawler

2. Click Next.
3. Go to the next step.

1. In the Choose data sources and classifiers step, for Data sources, click Add a data source.
2. Go to the next step.

1. In the pop-up box, for Data source, choose S3.
2. To choose the location of the data source, for S3 path, click Browse.
3. Go to the next step.

1. In the pop-up box, click the bucket name that starts with consumption-data-.

- This S3 bucket stores the flattened data created by the AWS Glue job.

2. Go to the next step. 

1. Choose the radio button to select the parquet key.
2. Click Choose.
3. Go to the next step.

1. For S3 path, if a "This is a required field" warning alert appears, click any empty space on the page to dismiss it.
2. Click Add an S3 data source.
3. Go to the next step.


1. Click Next.
2. Go to the next step.


1. In the Configure security settings step, for Existing IAM role, choose aws_glue_role.
2. Click Next.
3. Go to the next step.


1. In the Set output and scheduling step, for Target database, choose games-flattened-data-db.
2. Click Next.
3. Go to the next step.

1. In the Review and create step, review the configurations.
2. Click Create crawler.
3. Go to the next step.

1. In the success alert, review the message.
2. Click Run crawler.
3. Go to the next step.


1. In the Crawlers section, click the refresh icon from time to time to view the state update.
2. Under State, review to ensure that the crawler task state changes from Starting to Running, and then Stopping to Ready.

- The crawler task might take a few minutes to be completed.

3. Go to the next step.


1. In the left navigation pane, click Tables.
2. In the Tables section, review to ensure that two AWS Glue tables (games_data and players_data) were created.

- The two tables contain the metadata of the flattened data.
- If you do not see the two tables yet, click the refresh icon in the section.

3. Click the players_data table.
4. Go to the next step.

1. Scroll down to the Schema tab.
2. Review the schema of the players_data table. 

- The game_details array is flattened and transformed into an index that points to the games_data table.

3. Go to the next step.

1. In the left navigation pane, click Tables.
2. In the Tables section, click the games_data table.
3. Go to the next step.

1. Scroll down to the Schema tab.
2. Review the schema of the games_data table. 

- Two columns (id and index) were added.
- The id column in this table is mapped to the game_details column in the players_data. For example, the record with id=1 and game_details=1 refers to the same player.
- The index column refers to the index value of the original array.

3. Go to the next step.


1. Navigate to the Amazon Athena console. 
2. In the left navigation pane, click Query editor.
3. On the Editor tab, in the Data pane, for Database, choose games-flattened-data-db.
4. To view the table schema, under Tables, click the plus sign (+) next to the players_data table.
5. Review the schema of the table. 

- The raw data table was flattened with no nested data structures. 

6. Go to the next step.

1. If any previous queries are displayed in the query editor terminal, below the terminal, click Clear.

- Note that you can also click the plus sign (+) above the terminal to add a new query.

2. On your device, in the SQL_queries.txt file that you downloaded at the beginning of the lab, copy the query statement for Query 1, and then paste it in the query editor terminal.

- This query retrieves data from the players_data table and sorts it by game_details.

3. Click Run.
4. Go to the next step. 


1. On the Query results tab, review the results.

- The results display the data in the players_data table.
- The game_details column in the players_data table is mapped to the id column in the games_data table.

2. Go to the next step.

1. To view the table schema, in the Data pane, under Tables, click the plus sign (+) next to the games_data table.
2. Review the schema of the table. 

- The raw data table was flattened with no nested data structures. 

3. To clear the previous query, below the query editor terminal, click Clear.
4. On your device, in the SQL_queries.text file, copy the query statement for Query 2, and then paste it in the query editor terminal.

- This query retrieves data from the games_data table and sorts it by id and index.

5. Click Run.
6. Go to the next step.


1. On the Query results tab, review the results. 

- For example, in the players_data table, the game_details value for Jennifer Martinez is 1. This value maps to the id column in the games_data table. Therefore, the first two rows in the query results belong to the game details for Jennifer Martinez.

2. Go to the next step. 


1. In the top navigation bar search box, type:  

redshift 

2. In the search results, under Services, click Amazon Redshift.
3. Go to the next step.

1. In the left navigation pane, click Clusters.

- You might need to click the menu icon (three lines) in the left side panel to expand the navigation pane.

2. Scroll down to Clusters.
3. Choose the check box to select the cluster name that starts with games-db-cluster-.
4. Click Actions to expand the dropdown menu.
5. Choose Manage IAM roles.
6. Go to the next step.


1. Under Associated IAM roles, copy the ARN of the IAM role, and then paste it in your text editor.

- The ARN is below the IAM role name.

2. Click Cancel.
3. Go to the next step.

1. In the left navigation pane, click Query editor.
2. On the Editor tab, click Connect to database.
3. Go to the next step.

1. In the pop-up box, for Connection, choose Create a new connection.
2. For Authentication, choose Temporary credentials.
3. For Cluster, choose the cluster name that starts with games-db-cluster.
4. For Database name, type:

games_rs_db

5. For Database user, type:

awsuser

6. Click Connect.
7. Go to the next step.

1. For Status, review to ensure that the connection was successful.

- The status should be Connected.
- If a previous query is displayed in the query editor terminal, click Clear.

2. On your device, in the SQL_queries.txt file, copy the query statement for Query 3, and then paste it in the query editor terminal.

- The external schema references a database in the external data catalog and provides the IAM role ARN that authorizes your cluster to access Amazon S3 on your behalf. 

3. Replace ENTER YOUR IAM ROLE ARN ASSOCIATED WITH AMAZON REDSHIFT with the IAM role ARN that you copied in an earlier step.

- Be sure to keep the single quotation marks around the copied IAM role ARN.
- All external tables must be created in an external schema, which you create by using a CREATE EXTERNAL SCHEMA statement. 

4. Click Run.
5. Go to the next step.


1. After the query is completed, for Select schema, choose players_schema.
2. Review to ensure that two tables (games_data and players_data) are displayed.
3. Go to the next step.

1. To view the table schema, click the arrow next to players_data.
2. Review the schema of the players_data table.
3. Above the query editor terminal, click the plus sign (+) to add a new query.
4. On your device, in the SQL_queries.txt file, copy the query statement for Query 4, and then paste it in the query editor terminal.

- This query retrieves data from the players_data table and sorts it by game_details. 

5. Click Run.
6. On the Query results tab, scroll down to view the results.
7. Go to the next step.


1. Review the data in the players_data table.

- No nested data is in the flattened table.

2. Scroll up to the top of the page.
3. Go to the next step.


1. To view the table schema, click the arrow next to games_data.
2. Review the schema of the games_data table.
3. To clear the previous query, below the query editor terminal, click Clear.
4. On your device, in the SQL_queries.txt file, copy the query for Query 5, and then paste it in the the query editor terminal.

- This query retrieves data from the games_data table and sorts it by id and index.

5. Click Run.
6. On the Query results tab, scroll down to view the results.
7. Go to the next step.

1. Review the data in the games_data table.

- No nested data is in the flattened table.

2. Scroll up to the top of the page.
3. Go to the next step.


1. To clear the previous query, click Clear.
2. On your device, in the SQL_queries.txt file, copy the query statement for Query 6, and then paste it in the query editor terminal.

- This query finds the purchases by the player with ID 12345.

3. Click Run.
4. On the Query results tab, scroll down to view the results.
5. Go to the next step.


1. Review purchases by the player with ID 12345.

- Daniel Mccoy is the player with ID 12345.
- He bought the following in-game purchases:
	- drinks  for $4
	- clothes for $84

2. Review the ELAPSED TIME taken for the query.

- The query in this example took 7 seconds.

3. Scroll to the top of the page.
4. Go to the next step.

1. To clear the previous query, click Clear.
2. On your device, in the SQL_queries.txt file, copy the query statement for Query 7, and then paste it in the query editor terminal.

- This query creates a materialized view named mv_players_purchases.

3. Click Run.
4. Go to the next step.


1. To clear the previous query, click Clear.
2. On your device, in the SQL_queries.txt file, copy the query statement for Query 7, and then paste it in the query editor terminal.

- This query creates a materialized view named mv_players_purchases.

3. Click Run.
4. Go to the next step.

# following these steps too for the DIY sectin
1. For Select schema, choose public.
2. Review to ensure that the materialized view named my_players_purchases and the associated table were created.
3. To view its schema, click the arrow next to mv_players_purchases.
4. Review the schema in the materialized view.
5. Go to the next step.


1. To clear the previous query, click Clear.
2. On your device, in the SQL_queries.txt file, copy the query statement for Query 8, and then paste it in the query editor terminal.

- This query finds purchases by the player with ID 12345 from the materialized view instead.

3. Click Run.
4. Go to the next step.



1. Scroll down to the Query results tab.
2. Review the results.
3. Review the ELAPSED TIME.

- In this case, the query response time took only 2 seconds, compared to 7 seconds when the materialized view was not used. 

4. Go to the next step.



Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.


<!-- DIY -->
Create a materialized view for the totalpurchases by playeers (mv_players_purchases_amount). Query the created materialized veiw to find to find the total purchases by a player with ID 12345
# DIY: Hints
1. Use the following name for your materialized view:

mv_players_purchases_amount 

2. Create the materialized view based on the following query:

DROP MATERIALIZED VIEW IF EXISTS mv_players_purchases_amount;
CREATE MATERIALIZED VIEW mv_players_purchases_amount AS (
SELECT g.id as Id, p.name as Name, '$'||SUM(g.purchases) as Total_Purchases
FROM players_schema.players_data p, players_schema.games_data g
WHERE p.game_details = g.id 
GROUP BY g.id, p.name); 

3. Run:

SELECT * FROM  mv_players_purchases_amount
WHERE id='12345';


Should return:

id       name              total_purchases
12345	   Daniel Mccoy	     $88

