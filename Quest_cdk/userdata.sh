#!/bin/bash
sudo yum update -y
sudo yum -y install jq
sudo yum install -y python3
sudo dnf install -y pip
export bucket_name=$(aws s3api list-buckets --query 'Buckets[*].[Name]' --output text | grep lab-)
aws s3 cp s3://$bucket_name/vpcapp.zip .
unzip vpcapp.zip
export TOKEN=$(curl --request PUT "http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 3600")
export REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/region --header "X-aws-ec2-metadata-token: $TOKEN")
export DATABASE_HOST=$(aws rds describe-db-clusters --query 'DBClusters[*].[Endpoint]' --output text --region $REGION)
export DATABASE_USER=testuser
export DATABASE_PASSWORD=password1234!
export DATABASE_DB_NAME=Population
echo $DATABASE_DB_NAME $DATABASE_HOST $DATABASE_PASSWORD $DATABASE_USER $REGION
cd vpcapp
pip install -r requirements.txt
cd loaddatabase
python3 database_populate.py
cd ..
python3 application.py