#!/bin/bash
source /home/ec2-user/car-wash-kiosk/bin/config.sh

DATA_DIRECTORY="/home/ec2-user/car-wash-kiosk/data"

echo "Uploading sales and customer data for location $LOCATION_NUMBER"
echo "S3_BUCKET_NAME=$S3_BUCKET_NAME"
echo "LOCATION_NUMBER=$LOCATION_NUMBER"

for i in {1..3}
do
    # upload sales data to s3 with a $location prefix
    # the && at the end of the next line is a short-circuit operator, it will only execute the next line if the previous line succeeded
    # Both lines must succeed for the upload to succeed
    aws s3 cp $DATA_DIRECTORY/car-wash-customers.csv s3://$S3_BUCKET_NAME/$LOCATION_NUMBER/car-wash-customers.csv &&
    aws s3 cp $DATA_DIRECTORY/car-wash-sales.csv s3://$S3_BUCKET_NAME/$LOCATION_NUMBER/car-wash-sales.csv
    if [ $? -eq 0 ]; then
        echo "Upload complete"
        break
    else
        echo "Upload failed, retrying in 5 seconds"
        sleep 5
    fi
done

