<!-- Before starting create the following resources -->
- lambda role using with the required s3 and rds permissions
- lambda layer using 

<!-- Lab instructions -->
1. In the top navigation bar search box, type: lambda
2. In the search results, under Services, click Lambda.
3. Go to the next step.

1. In the Functions section, click Create function.
2. Go to the next step.

1. For Function name, type: labFunction
2. For Runtime, on the dropdown menu, choose Python 3.13.
3. Scroll down to Permissions.
4. Go to the next step.

1. Under Permissions, click to expand Change default execution role.
2. For Execution role, choose Use an existing role.
3. For Existing role, choose lambda_security_role.
4. Click to expand Additional Configurations.
5. Scroll down to Enable VPC.
6. Go to the next step.

1. To connect the Lambda function to your VPC, choose the check box to select Enable VPC.
2. For VPC, choose the VPC with Name: LabVPC.
3. Go to the next step.

1. For Subnets, in the search box, type: lambda
2. Choose the check boxes to select the two subnet names that contain lambda_subnet.
- You are selecting lambda_subnetSubnet1 and lambda_subnetSubnet2.
3. Go to the next step.

1. For Security groups, choose the check box to select the default VPC security group.
2. Click Create function.
- The function might take 5–10 minutes to be created.
3. Go to the next step.

1. In the success alert, review the message.
- You might need to wait for the success alert to appear.
2. To add a layer to your Lambda function, in the Function overview section, click Layers.
3. Go to the next step.

1. In the Layers section, click Add a layer.
2. Go to the next step.

1. For Layer source, choose Custom layers.
2. For Custom layers, choose the layer name that starts with labfunctionlayer.
3. For Version, choose a version.
- Only one version should be available in the list. The available version number might not be 1, depending on the number of times you created the Lambda function with this custom layer. Any version number will work.
4. Click Add.
5. Go to the next step.

1. In the Function overview section, next to Layers, review the number (1). 
- One layer is added.
2. On the Code tab, click Upload from to expand the dropdown menu.
3. Choose .zip file.
4. Go to the next step.

1. In the pop-up box, click Upload.
2. Choose the lambda_security_code.zip file that you downloaded at the beginning of the lab.
3. Click Save.
4. Go to the next step.

1. In the success alert, review the message.
2. Scroll down to the Code source section.
3. Go to the next step.


1. In the lambda_function.py code, review lines 30 and 31.
- The Lambda function retrieves the database credentials from AWS Secrets Manager. 
- The value of the secret_name is read from the environment variable with the key, secret_arn.
2. Go to the next step.

1. In the top navigation bar search box, type:
secrets
2. In the search results, under Services, click Secrets Manager.
3. Go to the next step.

1. In the Secrets section, click the secret name that starts with DatabaseSecret.
2. Go to the next step.

1. In the Secret details section, under Secret ARN, click the copy icon to copy the provided ARN, and then paste it in the text editor of your choice on your device. 
- You will use this ARN in later steps (arn:aws:secretsmanager:us-east-1:553225903739:secret:DatabaseSecret3B817195-djQcWg8y8yDd-ffiJSW).
2. In the Secret value section, click Retrieve secret value.
3. Go to the next step.

1. In the Secret value section, review the key-value pairs of secrets stored in Secrets Manager.
- Secrets Manager stores the database credentials, such as the database login username and password, database name, and database engine.
2. Scroll down to Sample code.
3. Go to the next step.

1. In the Sample code section, review the provided code samples.
- The code samples are written in different programming languages to retrieve the secret in your application.
2. Go to the next step.

1. Navigate to the labFunction page on the AWS Lambda console.
- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.
2.  Click the Configuration tab.
3. Go to the next step.

1. On the Configuration tab, click General configuration.
2. Click Edit.
3. Go to the next step.

1. For Timeout, in the first (min) text box, type: 3
- This will increase the timeout value.
2. Click Save.
3. Go to the next step.

1. In the success alert, review the message.
2. Click the Configuration tab.
3. Click Environment variables.
4. Click Edit.
5. Go to the next step.

1. Click Add environment variable.
2. Go to the next step.

1. For Key, type: secret_arn
2. For Value, paste the Secrets Manager ARN that you copied in an earlier step.
3. Click Save.
4. Go to the next step.

1. In the success alert, review the message.
2. Click the Code tab.
3. In the left explorer pane, under Deploy, click Test.
4. On the Select test event dropdown menu, choose Create new test event.
5. Go to the next step.

1. For Event name, type a name that you like, such as testEvent. 
2. Click Save.
3. Go to the next step.

1. After the test event is successfully saved, click Invoke.
2. On the Output tab, review Status: Succeeded.
3. Under Function Logs, review the logs. - Database credentials were successfully retrieved  from AWS Secrets Manager.
4. To close the Output window, click the X.
5. To close the Create new test event tab, click the X.
6. Go to the next step.

1. In the lambda_function code, review lines 53–69. 
- This code block tests the Amazon Relational Database Service (Amazon RDS) connection with your Lambda function, using the retrieved database username and password. 
- The Amazon RDS database "talentpool" includes first_name, last_name, occupation, company, date of birth, and country of people. 
2. Review lines 73–78.
- This code block defines a custom query, which finds all the records with Toxicologist as occupation in the database. 
3. Go to the next step.

1. To uncomment the code block of lines 53–69, select (highlight) lines 53–69.
2. On the Code source navigation bar, click the three horizontal lines to expand the dropdown menu.
3. Choose Edit.
4. To uncomment the code block, choose Toggle Line Comment.
- Be sure to keep the indentations in the Python code blocks.
5. To save the updated function, click Deploy.
6. Go to the next step.

1. In the success alert, review the message.
2. To test the Amazon RDS connection, under Test Events, click testEvent and then click the Run arrow.
- The test might take 1–2 minutes because it has to load the data.
3. Go to the next step.

1. On the Output tab, review Status: Succeeded.
2. Under Function Logs, review the logs. 
- The Lambda function has successfully created and populated the talentpool table in the Amazon RDS database.
3. Go to the next step

1. Navigate to the Amazon VPC console.
- You can type "vpc" in the top navigation bar search box.
2. In the left navigation pane, click Endpoints.
3. In the Endpoints section, click Create endpoint.
4. Go to the next step.

1. In the Endpoint settings section, for Name tag (s3-gatway-ep), type a name that you like.
2. To search for Amazon S3 services, in the Services section search box, type: s3
 Choose Service Name = com.amazonaws.us-east-1.s3.
4. Go to the next step.

1. Choose the service name that has a Type of Gateway.
2. For VPC, choose the VPC name that includes (LabVPC).
3. Scroll down to Route tables.
4. Go to the next step.

1. In the Route tables section, choose the two check boxes to select the subnet names that include lambda_subnet:
- You are selecting Lab/LabVPC/lambda_subnetSubnet1 and Lab/LabVPC/lambda_subnetSubnet2.
2. Scroll down to the bottom of the page, and then click Create endpoint (not shown).
3. Go to the next step.

1. In the success alert, review the message.
2. Go to the next step.

1. Navigate to the Amazon S3 console.
2. In the General purpose buckets section, click the bucket name that ends with -practice. 
- You will use this S3 bucket for this practice lab.
- You will use another S3 bucket, with a name ending with -diy, in the upcoming DIY section of this solution.
3. Go to the next step.

1. Above the Objects tab, select (highlight) and copy the S3 bucket name (lambda-security-practice-51674fb0 ), and then paste it in your text editor.
- You will use this bucket name in a later step. 
2. On the Objects tab, review to ensure that the S3 bucket is currently empty.
3. Go to the next step.

1. Navigate to the labFunction page on the AWS Lambda console.
2. To view the lambda_function.py code, scroll down to the Code source section.
3. Go to the next step. 

1. In the lambda_function code, review the code block of lines 93–104. 

- The code tests the Lambda connection with Amazon S3. 
- If successful, File Uploaded Successfully is printed in the log.

2. On line 98, to replace Enter_your_bucket_name, paste the -practice S3 bucket name that you copied in an earlier step.
3. Uncomment lines 93–104.
- You practiced uncommenting lines in an earlier step.
- Be sure to keep the indentations in the Python code blocks.
4. To save the updated function, click Deploy.
5. Go to the next step.

1. In the success alert, review the message.
2. To test the Amazon S3 connection, hover over testEvent and click the Run arrow.
3. Go to the next step.

1. On the Execution results tab, review Status: Succeeded. 
2. Under Function Logs, review the logs.
- The query results of the Amazon RDS were successfully uploaded to the S3 bucket.
3. Go to the next step.

1. Navigate to the Amazon S3 console.
2. In the General purpose buckets section, click the bucket name that ends with -practice.
3. Go to the next step.

1. To download the Amazon RDS queried results to your device, click Download.
2. Go to the next step.

1. On your device, open the downloaded results.json file with a text editor or JSON viewer, and then review the Amazon RDS queried results.
- The results include the people in the database with Toxicologist as their occupation.
2. Go to the next step. 

<!-- DIY -->
- Change the custom query for the RDS TO Retrieve results for people whoose occupation is Data Scientist
- Cahnge the bucket name to the one that end with '-diy'