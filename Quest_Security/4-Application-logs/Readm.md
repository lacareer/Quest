The solution usees Amazon firehose to stream log files to an S3, AWS Glue to Crawl the log data to create a schema,
and Amazon Athena to query the data based on the AWS Glue schema

An EC2 called App-Server that has an a game application running. It could be any application.
make sure the instance has all the rght permissions

<!-- Lab instructions -->
1. In the top navigation bar search box, type: ec2
2. In the search results, under Services, click EC2.
3. Go to the next step.

1. On the EC2 Dashboard, in the Resources section, click Instances (running).
2. Go to the next step.

1. In the Instances section, choose the check box to select the App-Server instance.
2. Click Connect.
3. Go to the next step.

1. On the EC2 Instance Connect tab, under Public IPv4 address, click the copy icon to copy the provided address, and then paste it in the text editor of your choice on your device.
- You will use the address in a later step.
2. Click the Session Manager tab.
3. Go to the next step.

1. Click Connect.
- The Session Manager terminal opens in a new browser tab (or window).
2. Go to the next step.

1. To install the Amazon Kinesis agent, in the terminal window, at the command prompt, run (type the command and press Enter):
sudo yum install https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-agent-latest.amzn2.noarch.rpm -y
2. Go to the next step.

1. On your device, open the kinesis_agent_config.txt file that you downloaded at the beginning of the lab, and then, in the terminal, paste the contents of the file and press Enter.

- The configuration file contains the path of the access log that will contain log entries for each access attempt to the application website, as well as the name of the Firehose stream that was created by the lab.

2. To start the Kinesis agent, run: sudo service aws-kinesis-agent start
- The terminal will display an OK message.
3. To check that the agent is running, run: sudo service aws-kinesis-agent status
4. Review to ensure that the agent is in an active (running) state.
5. Type Q to return to the command prompt (Not shown).
6. Go to the next step.

1. To open the Kinesis agent access log, run: tail -f /var/log/httpd/access_log
2. Go to the next step.

1. In a new browser tab (or window) address bar, paste the public IP address of the App-Server EC2 instance that you copied in an earlier step (Not shown).
- If you receive an error message, be sure to use http:// not https://
2. Refresh the browser page a few times to add log entries in the access log on the instance.
- Feel free to try the game.
3. Go to the next step.

1. Navigate back to the terminal window in the previous browser tab, and then review the log entries that were created from the previous step.
- These entries are created every time the application's website is accessed.
2. Go to the next step.

1. On the Amazon EC2 console in the original browser tab, in the top navigation search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.

1. In the General purpose buckets section, click the bucket name that starts with log-bucket-.
- This bucket is set as the destination source in the Amazon Data Firehose stream.
2. Go to the next step.

1. On the Objects tab, click the refresh icon until a logs/ folder appears.
- This could take up to 5 minutes.
2. When it appears, click the logs/ folder.
3. Go to the next step.

1. Click each subfolder until you reach the lowest level in the hierarchy.
2. On the Objects tab, choose the check box to select one of the files.
3. Click Download.
- The file is downloaded to your device.
4. On your device, open the file in a text editor and review the log entries (not shown).
- These entries are the access requests logged on the App-Server in the /var/log/httpd/access_log file. The entries should match those that you reviewed in the EC2 Session Manager terminal.
5. Go to the next step.

1. In the top navigation bar search box, type: glue
2. In the search results, under Services, click AWS Glue.
3. Go to the next step.

1. In the left navigation pane, under Data Catalog, click Crawlers.
2. In the Crawlers section, click Create crawler.
3. Go to the next step.

1. In the Set crawler properties step, for Name, type: logcrawler
2. Click Next.
3. Go to the next step.

1. In the Choose data sources and classifiers step, for Data sources, click Add a data source.
2. Go to the next step.

1. In the pop-up box, for S3 path, click Browse S3.
2. Go to the next step.

1. In the Buckets section, choose the radio button to select the bucket name that starts with log-bucket-.
2. Click Choose.
3. Go to the next step.

1. For Subsequent crawler runs, review to ensure that Crawl all sub-folders is selected.
2. Click Add an S3 data source.
3. Go to the next step.

1. Click Next.
2. Go to the next step.

1. In the Configure security settings step, for Existing IAM role, on the dropdown menu, choose the role that starts with glue-service-role-.
2. Click Next.
3. Go to the next step.

1. In the Set output and scheduling step, for Target database, click Add database.
- This opens in a new browser tab (or window). After creating the database, you will return to the current browser tab.
2. Go to the next step.

1. For Name, type: logsdatabase
2. Click Create database.
3. Go to the next step.

1. In the Databases section, review to ensure that logsdatabase is displayed.
2. To continue building the crawler, return to the Add crawler page in the previous browser tab (not shown).
3. Go to the next step.

1. For Target database, click the refresh icon.
2. Choose logsdatabase.
3. Click Next.
4. Go to the next step.

1. In the Review and create step, scroll down to the bottom of the page.
2. Click Create crawler.
3. Go to the next step.

1. Click Run crawler.
2. Go to the next step.

1. Review to ensure that the crawler has finished running and that the Last run status is Completed.
2. In the left navigation pane, click Tables.
- A logs table was created in the logsdatabase database.
3. Go to the next step.

1. In the Tables section, click the name that starts with log_bucket_.
2. Go to the next step.

1. Scroll down to Schema.
2. Review the schema that was created from the App-Server access log data.
3. Go to the next step.

1. In the top navigation bar search box, type: athena
2. In the search results, under Services, click Athena.
3. Go to the next step.

1. On the Amazon Athena console home page, choose Query your data with Trino SQL.
2. Click Launch query editor.
- If the console defaults to the Query editor console, skip this step.
3. Go to the next step.

1. In the Query editor, click the Settings tab.
- Because this is the first query you have run in Amazon Athena, you need to set up a query result location in Amazon S3.
2. Go to the next step.

1. On the Settings tab, if you do not see the Manage settings section, click Manage.
2. Go to the next step.

1. In the Manage settings section, for Location of query result, click Browse S3.
2. Go to the next step.

1. In the pop-up box, choose the radio button to select the bucket name that starts with log-bucket-.
2. Click Choose.
3. Go to the next step.

1. At the end of the bucket name, type: /Athena-output/
- This creates a folder in the specified bucket where query results will be saved.
2. Click Save.
3. Go to the next step.

1. In the Query editor, click the Editor tab.
2. Go to the next step.

1. In the Data pane, for Database, review to ensure that logsdatabase is selected.
2. Under Tables, click the plus sign (+) next to log_bucket to expand the logs table.
3. To the right of Partitioned, click the vertical ellipses to expand the dropdown menu.
4. Under Run Query, click Preview Table.
5. Go to the next step.

1. On the Query results tab, review the log data.
- The data should look similar to the logs that were reviewed in the Session Manager terminal and the downloaded log file.
2. Go to the next step.

1. In the Query editor window, delete the existing SQL statement, and then type:

SELECT COUNT(clientip) FROM "logsdatabase"."xxxx";

2. Select (highlight) the "xxxx" in the SQL Query, including the quotes at the beginning and end.
3. Under Tables, double-click the name of the table that starts with log_bucket_.
- This should replace the xxxx with the name of the table.
4. Go to the next step.

1. To run the updated query, click Run (or Run again).
2. Review the results.
- This query counts the number of log entries in the access logs.
3. Go to the next step.
