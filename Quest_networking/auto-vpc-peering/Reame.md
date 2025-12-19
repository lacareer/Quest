<!-- MAKE SURE ALL 4 FILES ARE IN AN S3 BUCKET -->
<!-- SEE AUTOMATE INTER-REGION PEERING SCREENSHOT -->

- The four .zip files (put them in the s3 bucket) contain AWS Lambda functions for the automation of inter-Region peering. 

- The .json file is an AWS CloudFormation template file to create the Lambda functions.

- deploy cfn using the url of the .json with s3 option

- The get-transit-gateway-peering-status, peer-transit-gateway, modify-transit-gateway-requester-routes and diy-modify-transit-gateway-all-routes were all built by the CloudFormation template that you just ran. They are used to automate peering between Regions.

- create sf using the transit-gateway-automation-step-function-us-east-1.yaml

- create sf using the transit-gateway-automation-step-function-us-west-2

Both sf need no input to run but run the us-east-1 first and then us-west-2

