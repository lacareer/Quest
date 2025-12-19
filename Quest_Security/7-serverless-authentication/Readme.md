<!-- Lab instructions -->

1. In the app-code folder, open (double-click) the scripts.sh file.
- This file contains all the required commands to deploy the backend resources and the frontend resources for your serverless application.
2. Go to the next step.

1. In the Explorer window, click to expand the backend folder, and then open (double-click) the samconfig.toml file.
- This file contains all the configurations needed for AWS SAM to deploy the backend components.
2. Go to the next step.

1. In the scripts.sh file window, select (highlight) lines 3–9, and then open the context (right-click) menu on the highlighted content.
2. Choose Copy.
3. Go to the next step.

1. In the bottom terminal window, at the command prompt, paste the content that you just copied and press Enter.
- This script retrieves the S3 bucket name, the AWS Region, and the AWS Lambda role Amazon Resource Name (ARN) that were created during the lab startup process. These variables are used in a backend configuration file to deploy the backend API components.
2. After the last line populates, press Enter.
3. Go to the next step.

1. In the terminal, run (type the command and press Enter): sam deploy
- The "sam deploy" command deploys the backend components by using AWS SAM.
- You can also copy-paste this text. If you receive an undefined value when you paste this, try again. The code should look similar to what is displayed in the screenshot example.
2. Go to the next step.

1. In the terminal, review all the resources deployed during the "sam deploy" process.
2. Go to the next step.

1. In the terminal, review the stack in a CREATE_COMPLETE state after the creation is completed.
2. Go to the next step.

1. In the previous browser tab, in the top navigation bar search box, type: cloudformation
2. In the search results, under Services, click CloudFormation.
- Make sure to keep Code Editor in the other browser tab open throughout this lab.
3. Go to the next tab.

1. In the Stacks section, click the sam-bookmark-app stack.
2. Go to the next step.

1. In the right Stack details pane, click the Resources tab.
2. Review to confirm that an API Gateway endpoint, a DynamoDB table, and a few Lambda functions have been created for the application.
3. Go to the next step.

1. In the top navigation bar search box, type: dynamo
2. In the search results, under Services, click DynamoDB.
3. Go to the next tab.

1. In the left navigation pane, click Explore items.
2. Review the table named bookmarksTable.
- This table was created to store items created through the application.
3. In the Items returned section, review the item count.
- The item count is 0 because no items have been created from the application.
4. Go to the next step. 

1. In the top navigation bar search box, type: cognito
2. In the search results, under Services, click Cognito.
3. Go to the next tab.

1. In the left navigation pane, click User pools.
- You might need to click the menu icon (three lines) in the left side panel to expand the navigation pane. 
2. Go to the next step.

1. On the User pools page, click Create user pool.
2. Go to the next step.

1. On the Set up your application page, scroll down to Define your application.
2. For Application type, choose Single-page application (SPA). 
3. For Name your application, type: AppClientForBookmarkUserPool
4. Go to the next step.

1. In the Configure options section, for Options for sign-in identifiers, choose Username.
2. For Required attributes for sign-up, choose email.
3. Go to the next step.

1. At the bottom of the page, click Create user directory.
2. Go to the next step.

1.  In the success alert, review the message.
- You can safely ignore the managed login error alert.
2. For development platform, review the default selection.
3. Go to the next step.

1. In the left navigation pane, click User pools.
2. On the User pools page, click the user pool name that starts with pool -.
3. Go to the next step.

1. In the User pool overview section, review the user pool details.
2. Above the section, click Rename.
3. Go to the next step.

1. In the pop-up box, to replace the current user pool name, type: bookmark-app-userpool
- The user pool name is updated so that it can be accessed with this name by using a CLI command in a later step of the lab.
2. Click Save changes.
3. Go to the next step.

1. In the success alert, review the message.
2. Under User pool name, review the updated name.
3. Go to the next step.

1. In the left navigation pane, under Authentication, click Authentication methods.
2. In the Password policy section, click Edit.
3. Go to the next step.

1. For Password policy mode, choose Custom.
2. For Password requirements, clear the two check boxes to deselect:

Contains at least 1 number
Contains at least 1 special character 

3. Click Save changes.
4. Go to the next step.

1.  In the success alert, review the message.
2. Go to the next step.

1. In the left navigation pane, under Authentication, click Extensions.
2. Review the Lambda triggers section.
- Note that Amazon Cognito can invoke Lambda functions to further customize your authentication process.
- You must use the information in this section in the later DIY section of this solution.
3. Go to the next step.

1. Return to the Code Editor browser tab, and then, in the bottom terminal window, run the following two commands one at a time:
cd ~/app-code/frontend
npm install
- These commands change the directory to the frontend folder, and then install the npm packages required for the frontend UI deployment.
- The frontend UI is built using the Vue Javascript framework.
2. Review to confirm that all the npm packages were successfully installed (not shown).
- You can safely ignore any warning or notice messages.
3. Go to the next step.

1. In the Explorer window, click to expand the frontend folder.
2. In the frontend folder, click to expand the src folder.
3. In the src folder, open (double-click) the aws-exports.js file.
- The aws-exports.js file is a configuration file for the frontend UI. The file defines the AWS Region, the Amazon Cognito user pool ID, the app client ID for user account creation, and the API Gateway endpoint URL to connect to the backend.
4. Go to the next step.

1. In the top scripts.sh window, select (highlight) and copy the contents from lines 13–23.
2. To update the aws-exports.js file, in the bottom terminal window, paste the code that you just copied and press Enter.
- This script substitutes the placeholders in the aws-exports.js file with the API Gateway endpoint URL, Amazon Cognito user pool ID, app client ID, and the AWS Region.
3. After the final line populates, press Enter.
4. Go to the next step.

1. In the top window, click the aws-export.js tab.
2. In the file code, review to confirm that the placeholders are updated with the actual values.
3. Go to the next step.

1. In the bottom terminal window, run: npm run build
2. Go to the next step.

1. After the build is completed, review the Build complete message.
2. Go to the next step.

1. In the terminal, run the following two commands one at a time:
cd dist
ls
2. Go to the next step.

1. To zip all the contents of the frontend folder, run: zip -r bookmarkapp.zip *
2. Go to the next step.

1. In the top scripts.sh window, copy the last two lines (27–28) of code.
- These two lines retrieve the S3 bucket name from the environment and copy the bookmarkapp.zip file to the S3 bucket.
2. In the bottom terminal, paste and the code that you just copied and press Enter.
3. After the bottom line populates, press Enter.
4. Go to the next step.

1. In the previous browser tab, in the top navigation bar search box, type: amplify
2. In the search results, under Services, click AWS Amplify.
3. Go to the next step.

1. On the AWS Amplify console home page, click Deploy an app.
2. Go to the next step.

1. In the Choose create method step, choose Deploy without Git.
2. Click Next.
3. Go to the next step.

1. For App name, type: bookmarkapp
2. For Branch name, type: dev
3. For Method, choose Amazon S3.
4. For S3 bucket, choose the bucket name that starts with resource-bucket-.
5. For Zip file, choose bookmarkapp.zip.
6. Click Save and deploy.
7. Go to the next step.

1. Review to confirm that deployment of the frontend app successfully completed.
2. Under Domain, click the provided link to launch the app.
- The app opens in a new browser tab (or window).
3. Go to the next step.

1. On the BookmarkApp page, click Create account.
2. Go to the next step.

1. For Username, type: testuseraccount
2. For Password, type: Test1234
3. For Email Address, type a valid email address.
- The Amazon Cognito service sends a confirmation code to your email address for verification purposes.
4. For Phone Number, type: 1111111111
- This is not used for verification purposes, so you can enter any numbers.
5. Click CREATE ACCOUNT.
6. Go to the next step.

1. For Confirmation Code, type the code that you receive in your email.
- You code is different from what is displayed in the example screenshot.
2. Click CONFIRM.
3. Go to the next step.

1. Click the add (+) icon.
2. Go to the next step.

1. To add a new bookmark, for Name, type: AWS Skill Builder
2. For Description, type: AWS Training
3. For Bookmark URL, type: skillbuilder.aws
4. Click ADD BOOKMARK.
5. Go to the next step.

1. Review the details of the bookmark that you just added.
2. Go to the next step.

1. In the previous browser tab, navigate to the Explore items page on the Amazon DynamoDB console.
2. Choose bookmarksTable.
3. In the Items returned section, review to see the item that was added through the Bookmark App.
4. Go to the next step.

Congratulations! You've complete the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->

- Add a lambda function to th Comgnito user pool to remove the valdation code process

# Hint

- Go to the Cognito User Pool
- Click on it
- Click Extensions under Authentication in the LHS pane
- Click Add Lambda Trigger
- Select Sign-up and Pre sign-up trigger
- Select a  function f rom the dropdwon
- Click Add Lambda trigger
