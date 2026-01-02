
<!-- Lab instructions -->
1. Go to the console and deploy all the lambda function code making sure to add env ("input_bucket" and "output_bucket") were applicable
   Ensure the function have the right permissions


1. In the top navigation bar search box, type: s3
2. In the search results, under Services, click S3.
3. Go to the next step.
4. Create "input_bucket" and "output_bucket" with name as "raw-zone-bucket-chukky" and "consumption-zone-bucket-chukky" respectively 
5. Enable EventBridge on each bucket
6. Create an EventBridge rule for the input_bucket that targets all lambda but labFunction-Data-Generator.py
7. Run the labFunction-Data-Generator.py function to generate data to the input bucket







