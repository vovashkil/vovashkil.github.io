#!/bin/bash

source /home/ec2-user/car-wash-kiosk/bin/config.sh

echo "S3 Bucket = $S3_BUCKET_NAME"
DATA_DIRECTORY="/home/ec2-user/car-wash-kiosk/data"
BACKUP_DIRECTORY="/home/ec2-user/car-wash-kiosk/backup"
BACKUP_FILE_NAME="data-backup-$(date +%Y-%m-%d-%H-%M).zip"

echo "BACKUP_DIRECTORY = $BACKUP_DIRECTORY"
echo "BACKUP_FILE_NAME = $BACKUP_FILE_NAME"

# copy customer_data.csv and sales_data.csv to the backup directory and zip them
cp $DATA_DIRECTORY/car-wash-customers.csv $DATA_DIRECTORY/car-wash-sales.csv $BACKUP_DIRECTORY
cd $BACKUP_DIRECTORY
zip -r $BACKUP_FILE_NAME car-wash-customers.csv car-wash-sales.csv
rm car-wash-customers.csv car-wash-sales.csv
cd ..

echo "Backup complete"
