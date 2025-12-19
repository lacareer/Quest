Please provision an EC2 with an SG with port 8443 open to the public and an instance profile attached using with the labFunction-roles-for both-functions.json config.
The incidence response removes the SG nad the instance profile attached to it

<!-- Lab instructions -->

1. In the top navigation bar search box, type: sns
2. In the search results, under Services, click Simple Notification Service.
3. Go to the next step.

1. On the Amazon SNS console home page, for Topic name, type:UnauthorizedExceptionNotification
2. Click Next step.
3. Go to the next step.

1. For Type, keep or choose the default topic type of Standard.
2. For Display name, type: Notify when an unauthorized error is detected (HTTP 401)
3. Go to the next step.

1. At the bottom of the page, review the other options that can be configured.
2. Click Create topic.
3. Go to the next step.

1. In the success alert, review the message.
2. On the Subscriptions tab, review to see that this topic currently has no subscriptions.
- You subscribe an AWS Lambda function to this topic in a later step. 
3. Go to the next step.

1. In the top navigation bar search box, type: instances
2. In the search results, under Features, click Instances.
3. Go to the next step.

1. In the Instances section, choose the checkbox to select the App-Server instance.
2. Below that section, on the Security tab, under IAM Role, review the provided role for the instance. 
3. Under Security groups, review the provided group.
- This Amazon EC2 instance is currently configured as needed, and it has the proper instance profile and security group attached to accept connections.
4. In the Instances section, for the App-Server instance, under Instance ID, select (highlight) and copy the provided ID, and then paste it in the text editor of your choice on your device.
- You will use this ID in later steps.
5. Go to the next step.

1. In the top navigation bar search box, type:ssm
2. In the search results, under Services, click Systems Manager.
3. Go to the next step.

1. In the left navigation pane, click Fleet Manager.
- You can safely ignore the missing permissions alert from Systems Manager.
2. Go to the next step.

1. In the Managed Nodes section, choose the checkbox to select the available App-Server managed node.
2. Click Node actions to expand the dropdown list.
3. Choose Tools.
4. Choose Execute run command.
- This action opens a new browser tab (or window).
5. Go to the next step.

1. In the Command document section, choose the radio button to select AWS-ConfigureAWSPackage.
2. Go to the next step.

1. Scroll down to Command parameters.
2. For Action, keep the default choice of Install.
3. For Installation Type, keep the default choice of Uninstall and reinstall.
4. For Name, type:AmazonCloudWatchAgent
5. Go to the next step.

1. In the Target selection section, for Target selection, keep or choose the radio button to select Choose instances manually.
2. For Instances, keep or choose the checkbox to select the App-Server instance.
3. Go to the next step.

1. Click to expand the Rate control section.
2. Review the Concurrency and Error threshold settings.
3. In the Output options section, clear the checkbox to deselect Enable an S3 bucket.
- Command output can be logged to an S3 bucket or a CloudWatch log group.
4. Go to the next step.

1. At the bottom of the page, click Run.
2. Go to the next step.

1. In the success alert, review the message.
2. In the Command status section, review to see that the command was successfully completed.

- If the status is still Processing, click the refresh icon above the section.
- While the Run Command is processing, you are provided data such as # of targets, # completed, and # of errors.

3. In the Targets and outputs section, choose the radio button to select the available instance ID.
4. Click View output.
5. Go to the next step.

1. In the Step 1 section, review the command output.
- Step 1 was skipped because it's required only when the target instance is on a Windows platform.
2. Go to the next step.

1. In the Step 2 section, click to expand Output.
2. Go to the next step.

1. Review the Step 2 command output.
- This output shows that the AmazonCloudWatchAgent was successfully installed.
2. In the left navigation pane, click Session Manager.
3. Go to the next step.

1. On the Sessions tab, click Start session.
2. Go to the next step.

1. In the Specify target step, under Target instances, choose the App-Server instance.
2. Click Start session.

- The session opens in a new browser tab (or window).

3. Go to the next step.

1. To go to the ssm-user home directory, in the terminal window, at the command prompt, run (type the command and press Enter):

cd ~

2. To list the contents of the directory, run:

ls -ltr

- The files staged are for running a Flask application. The application will log access attempts to the record.log file.

3. To check the current status of the CloudWatch agent, run:

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status

- You can also copy-paste this text. If you receive an undefined value when you paste this, try again.

4. Review the returned output.

- The status currently shows that the CloudWatch agent is stopped and has not yet been configured.

5. Go to the next step.

1. To start the CloudWatch agent configuration wizard, run: 

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard

2. Review the Welcome message.
3. Go to the next step.
- The configuration wizard walks you through a series of questions. To answer each question, type the number for the correct option, and then press Enter.
1. For each of the first 6 questions, after you read the question, choose (in order):
linux (1)
EC2 (1)
root (2)
no (2)
no (2)
no (2)
2. Go to the next step.

1. For "Do you have any existing CloudWatch Log Agent?", choose no (2).
2. For "Do you want to monitor any log files?", choose yes (1).
3. For Log file path, type: /home/ssm-user/record.log
4. For Log group name, to keep the default, press Enter 'record.log'.
5. For Log group class, choose STANDARD (1).
6. For Log stream name, to keep the default, press Enter.
7. For Log Group Retention in days, choose option 5 (7 day retention).
8. Go to the next step.

1. For "Do you want to specify any additional log files to monitor?", choose no (2).
2. For "Do you want the CloudWatch agent to also retrieve X-ray traces?", choose no (2).
3. Review the contents of the saved config file and its location.
4. Go to the next step.

1. For "Do you want to store the config file in the SSM parameter store?", choose yes (1).
2. For "What parameter store name do you want to use to store your config?", to keep the default, press Enter.
3. For "Which region do you want to store the config in parameter store?", to keep the default, press Enter.
4. For "Which AWS credentials should be used to send json config to parameter store?", choose option 1.
5. Review to make sure that the configuration was successfully written to the parameter store.
6. Go to the next step.

1. To start the CloudWatch agent, run:
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -s -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
2. Review the output.
3. Go to the next step.

1. Return to the AWS Management Console in the other browser tab. 
2. In the top navigation bar search box, type: cloudwatch
3. In the search results, under Services, click CloudWatch.
4. Go to the next step.

1. In the left navigation pane, click to expand Logs.
2. Click Log groups.
3. In the Log groups section, click the log group named record.log.
4. Go to the next step.

1. On the Log streams tab, click the available log stream (EC2 instance ID).
2. Go to the next step.

1. In the Log events search box, type: 401
and press Enter.
- You can safely ignore any alerts.
2. Click Create metric filter.
3. Go to the next step.


1. In the pop-up box, for Filter name, type: Unauthorized-401
2. For Metric namespace, type: LabApplications
3. For Metric name, paste the EC2 instance ID that you copied in an earlier step.
4. For Metric value, type: 1
5. Go to the next step.

1. For Unit, choose Count.
2. Click Create.
3. Go to the next step.

1. In the success alert, review the message.
2. Go to the next step.

1. In the top navigation bar search box, type: lambda
2. In the search results, under Services, click Lambda.
3. Go to the next step.

1. In the left navigation pane, click Functions.
2. In the Functions section, click the labFunction-Traffic-Generator function.

- This Lambda function mimics a malicious actor, trying to brute-force guess a password, thereby generating HTTP 401 errors.
- You can safely ignore any other Lambda functions you see that are not displayed in the screenshot example.

3. Go to the next step.

1. To create a new test event, click the Test tab.
2. Go to the next step.

1. For Event name, type: Generate401Traffic
- You can review and keep the default settings.

2. Click Save.
3. Go to the next step.

1. In the success alert, review the message.
2. Click Test.
3. Go to the next step.

1. Click to expand Details.
2. Under Log output, review the results.
- The function repeatedly tried to log in to the application by using the wrong username and password.
3. Go to the next step.


1. Navigate to the Amazon CloudWatch console.
2. In the left navigation pane, click All alarms.
3. In the Alarms section, click Create alarm.
4. Go to the next step.

1. In the Specify metric and conditions step, click Select metric.
2. Go to the next step.

1. In the pop-up box, on the Browse tab, click LabApplications.
2. Go to the next step.

1. Click Metrics with no dimensions.
2. Go to the next step.

1. Choose the checkbox to select the available metric name (EC2 instance ID).
2. Click Select metric.
3. Go to the next step.

1. For Metric name, review the name (EC2 instance ID).
2. For Statistic, choose Sum.
3. For Period, choose 30 seconds.
4. Go to the next step.

1. In the Conditions section, for Threshold type, choose Static.
2. For Define the alarm condition, choose Greater.
3. For Define the threshold value, type: 20

4. Click to expand Additional configuration.
5. For Missing data treatment, choose Treat missing data as good.
6. Click Next.
7. Go to the next step.

1. In the Configure actions step, for Alarm state trigger, choose In alarm.
2. For Send a notification to the following SNS topic, choose Select an existing SNS topic.
3. For Send a notification to..., choose UnauthorizedExceptionNotification - You created this SNS topic in an earlier step.
4. Go to the next step.

1. At the bottom of the page, click Next.
2. Go to the next step.

1. In the Add name and description step, for Alarm name, type: Unauthorized401ErrorBreach
2. For Alarm description, on the Edit tab, type:
Triggers when the number of HTTP 401 errors is greater than 20 during a 30 second period.
3. Click Next.
4. Go to the next step.

1. In the Preview and create step, review the alarm configurations for accuracy.
2. Go to the next step.

1. At the bottom of the page, click Create alarm.
2. Go to the next step.

1. In the success alert, review the message.
2. Under State, review to see that the initial state of the alarm is Insufficient data.
3. Go to the next step.

1. After a couple of minutes, under Alarms, click the refresh icon.
2. Under State, review to confirm that the alarm state has changed to OK.
3. Go to the next step.

1. Navigate to the AWS Lambda console.
2. In the left navigation pane, click Functions.
3. In the Functions section, click the labFunction-isolator function.
- When this Lambda function is invoked, it will isolate the AWS resource (the App-Server EC2 instance). 
4. Go to the next step.

1. In the Function overview section, click + Add trigger.
2. Go to the next step.

1. For Trigger configuration, choose SNS.
2. Go to the next step.

1. For SNS topic, choose UnauthorizedExceptionNotification.
2. Click Add.
3. Go to the next step.

1. In the success alert, review the message.
2. On the breadcrumb menu, click Functions.
- This is the horizontal top menu with right-pointing arrows separating page layers.
3. Go to the next step.

1. In the Functions section, click the labFunction-Traffic-Generator function.
2. Go to the next step.

1. On the Test tab, click Test.
- This invokes the CloudWatch alarm that you created earlier, which sends a notification to the SNS topic, which invokes the labFunction-isolator Lambda function.
2. Go to the next step.

1. Navigate to the Amazon EC2 console.
2. On the Dashboard, in the Resources section, click Instances (running).
3. Go to the next step.

1. In the Instances section, choose the checkbox to select the App-Server instance.
2. Below that section, click the Security tab.
3. Under IAM Role, review to see that the original role attached to the instance was removed.
4. Under Security groups, review to see that the EC2 instance is now assigned an Isolated_SG security group.
- The Isolated_SG security group does not have ingress or egress rules attached, stopping the malicious intruder from being able to connect.
5. Go to the next step.

Congratulations! You've completed the Practice section. Continue with the DIY section to complete the solution.


<!-- DIY -->

- Subscribe  your email to the Topic in the lab
