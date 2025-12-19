<!-- Prerequisite -->
- Create two instances to meet the  below requirement and with name each as:
  1. Test_Server (used to attach website/app server)
  2. BookClub_AppInstance (Simulates an  application or Host that displays only: "Welcome to the book club application page!")

- Proceed to lab instructions below


<!-- Lab instruction -->
1. In the left navigation pane, click Instances.
2. In the Instances section, choose the checkbox to select BookClub_Appinstance.
3. On the Details tab, under Public DNS, click the copy icon to copy the provided DNS for the EC2 instance, and then paste it in the text editor of your choice on your device. 
- You use this DNS in later steps.
4. Go to the next step.

1. In a new browser tab (or window) address bar, paste the Public DNS that you just copied and press Enter. 
2. Review the welcome message from the application server deployed in the EC2 instance.
- This message means that you can access the application server.
- If you receive an error, make sure that the URL begins with http:// and not https://.
3. Go to the next step.

1. Return to the Instances page on the Amazon EC2 console.
2. Choose the checkbox to select the Test_Server instance.
3. Click Connect.
4. Go to the next step.

1. On the Connect to instance page, click the Session Manager tab.
2. Click Connect.
- The Session Manager terminal opens in a new browser tab (or window).
3. Go to the next step.

1. In the new terminal, at the command prompt, replacing <Your Public DNS> with the DNS that you copied in an earlier step, run (type the command and press Enter): export BookClub_URL=<Your Public DNS>
- This command saves your EC2 public address as a variable to be used in the next few commands. 
2. In the terminal, run: curl -d 'user=<script><alert>Hello World!></alert></script>' $BookClub_URL
- You can also copy-paste this text. If you receive an undefined value when you paste this, try again.
- This command behaves as a cross-site scripting attack.
3. Review to see that you can access the application server.
- The application welcome message is displayed, so the site scripting attack is not blocked.
4. Go to the next step.

1. In the terminal, run: curl -H 'X-Book-Attack: Comics' $BookClub_URL
- This command simulates passing a request with a specific HTTP header (X-Book-Attack).
2. Review to see that you can still access the application server.
- The application welcome message is displayed, so the malicious request is not blocked.
3. Go to the next step.

1. Return to the AWS Management Console browser tab.
- Keep the current browser tab and Session Manager terminal open. You return to it later.
2. In the top navigation bar search box, type: waf
3. In the search results, under Services, click WAF & Shield.
4. Go to the next step.

1. On the AWS WAF console home page, click Create protection pack (web ACL).
2. Go to the next step.

1. To close the error alert, click the X.
- You can safely ignore the error alert, which might appear few more times during the web ACL creation.
2. For App category, on the dropdown list, choose Other.
3. For App focus, choose Web.
4. Go to the next step.

1. In the Select resources to protect section, click Skip for now.
2. Go to the next step.

1. For Choose protection pack (web ACL) resource types, choose AWS Amplify application, CloudFront distribution, and CloudFront distribution tenant.
2.For Choose initial protections, choose Build your own pack from all of the protections AWS WAF offers.
3. In the Add pane, choose AWS-managed rule group.
4. Click Next.
5. Go to the next step.

1. Under Free, review the SQL database rule.
- You must use this rule in the later DIY section of this solution.
2. Click to select Core rule set.
3. Go to the next step.

1. Review the Details section.
2. Under Inspection, keep the default choice of All requests.
3. To review all the default values (not shown), scroll down to the bottom of the section.
4. Click Add rule.
5. Go to the next step.

1. Review the created rule.
2. Click Add rule.
3. Go to the next step.

1. Choose Custom rule.
2. Click Next.
3. Go to the next step.

1. Choose Custom rule. 
2. Click Next.
3. Go to the next step.

1. For Action, choose Block.
2. For Rule name, type: MaliciousHeaderAttack
3. For If a request, keep the default choice of matches the statement.
4. Go to the next step.

1. For Inspect, choose Single header.
2. For Header field name, type: X-Book-Attack
- This rule inspects the header X-Book-Attack information.
3. For Match type, choose Size greater than or equal to.
4. For Size in bytes, type: 1
5. Click Add rule.
6. Go to the next step.

1. Review the new created rule.
2. Go to the next step.

1. In the Name and describe section, For Name, type: Book_WebACL
2. Click Create protection pack (web ACL).
3. Go to the next step.

1. In the success alert, review the message.
2. Choose Book_WebACL.
3. In the Book_webACL pane, choose Manage rules.
4. Go to the next step.

1. Review the two rules.
2. Go to the next step.

1. In the top navigation bar search box, type: cloudfront
2. In the search results, under Services, click CloudFront.
3. Go to the next step.

1. On the Distributions page, click Create distribution.
2. Go to the next step. 

1. In the Choose a plan step, review the available plans.
2. Go to the next step.

1. At the bottom of the page, choose Pay as you go.
2. Click Next (not shown).
3. Go to the next step.

1. In the Get started step, for Distribution name, type: ec2_instance_distribution
2. For Distribution type, choose Single website or app.
3. Scroll down to the bottom of the page, and then click Next (not shown).
4. Go to the next step.

1. In the Specify origin step, for Origin type, choose Other.
2. For Custom origin, paste the DNS address that you copied in an earlier step. 
3. Go to the next step.

1. For Origin settings, choose Customize origin settings.
2. For Enable Origin Shield, choose or keep No.
3. For Protocol, choose Match viewer.
4. Review the default values for the HTTP port and HTTPS port.
5. Scroll down to the bottom of the page, and then click Next (not shown).
6. Go to the next step.

1. In the Enable security step, for Web Application Firewall (WAF), choose Enable security protections.
2. Turn on Use existing WAF configuration.
3. For Choose a web ACL, choose BookClub_WebACL.
4. Click Next.
5. Go to the next step.

1. In the Review and create step, review the configurations.
2. Click Create distribution.
3. Go to the next step.

1. In the success alert, review the message.
2. Under Distribution domain name, click the copy icon to copy the provided name, and then paste it in your text editor.
- You use this domain name in a later step.
3. Under Last modified, review and wait for the value to change from Deploying to a date.
- The change might take up to 10 minutes.
4. Go to the next step.

1. On the top breadcrumb menu, review the CloudFront distribution ID.
- You must use this ID in the upcoming DIY section.
2. Under Last modified, review to confirm that a date is now displayed.
- The CloudFront distribution is now deployed.
3. Go to the next step.

1. Return to the Test_Server terminal in the other browser tab.
2. In the terminal window, replacing <Your CloudFront distribution domain name> with the distribution domain name that you copied in an earlier step, run:

export Protected_BookClub_URL=https://<Your CloudFront distribution domain name>
	
- If the terminal has timed out, use earlier lab steps to reconnect.
- The previous command saves the CloudFront distribution domain name as a variable to be used in the next few commands. 

3. To check if cross-site scripting attack is now blocked, run:

curl -d 'user=<script><alert>Hello World!></alert></script>' $Protected_BookClub_URL

4. Review the response to confirm that the cross-site scripting attack is blocked.	
- The response message "Request blocked" is displayed.
5. Go to the next step.



1. In the terminal, run:

curl -H 'X-Book-Attack: Comics' $Protected_BookClub_URL

- This command simulates an attack with a malicious header in the HTTP request.
2. Review the response to confirm that the attack is blocked.
- The response message "Request blocked." is displayed.
3. Go to the next step.


Congratulations! You've completed the Practice section. Go to the DIY section to complete the solution.

<!-- DIY -->

- Add a SQL Database managed rul rule in WAF to the "Book_WebACL" protection pack created in the lab exercise
- Log into th test instance and re-run the scripting injection and header test in the lab exercise
- run also: curl -d "user=' OR 'a'='a';" $Protected_BookClub_URL