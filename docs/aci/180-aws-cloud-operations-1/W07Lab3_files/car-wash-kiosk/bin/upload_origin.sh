#!/bin/bash
source /home/ec2-user/car-wash-kiosk/bin/config.sh

DATA_DIRECTORY="/home/ec2-user/car-wash-kiosk/data"

echo "Uploading sales and customer data for location $LOCATION_NUMBER"
echo "S3_BUCKET_NAME=$S3_BUCKET_NAME"
echo "LOCATION_NUMBER=$LOCATION_NUMBER"

# upload sales data to s3 with a $location prefix
aws s3 cp $DATA_DIRECTORY/car-wash-customers.csv s3://$S3_BUCKET_NAME/$LOCATION_NUMBER/car-wash-customers.csv
aws s3 cp $DATA_DIRECTORY/car-wash-sales.csv s3://$S3_BUCKET_NAME/$LOCATION_NUMBER/car-wash-sales.csv

echo "Upload complete"
