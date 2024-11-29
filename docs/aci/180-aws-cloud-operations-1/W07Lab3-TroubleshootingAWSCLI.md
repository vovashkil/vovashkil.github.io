# Troubleshooting the AWS CLI and Bash in Linux Environments

## Lab overview

In this lab, you troubleshoot a misconfigured Linux application environment and correct any issues you encounter.

Objectives
By the end of this lab, you will be able to do the following:

Inspect a kiosk environment to make sure that it is set up properly.
Review the log output from bash scripts to troubleshoot errors.
Implement retry logic in a bash shell script using a loop.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, Mac OS X, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made)
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal.
 Congratulations! A conclusion or summary point in the lab
Start lab
To launch the lab, at the top of the page, choose Start lab.
 You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console.
You are automatically signed in to the AWS Management Console in a new web browser tab.

 Do not change the Region unless instructed.

Common sign-in errors
Error: You must first sign out


If you see the message, You must first log out before logging into a different AWS account:

Choose the click here link.
Close your Amazon Web Services Sign In web browser tab and return to your initial lab page.
Choose Open Console again.
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Scenario
AnyCompany Car Washes provides automated car washes in multiple locations. The company has a kiosk where customers purchase a subscription (Basic, Enhanced, or Extreme) to use the car washes. The kiosk then dispenses a radio frequency identification (RFID) tag for customers to place in the front window of their vehicle. After customers purchase a subscription, they receive automatic access to the car washes by using the RFID tag.

Architecture diagram for the car wash kiosk.

Figure: The car wash kiosk server sends customer and sales data files to the AWS Cloud containing an Amazon Simple Storage Service (Amazon S3) bucket. The account includes a role with permissions to create and update Amazon S3.

AnyCompany Car Washes needs to automate backups and sales reporting in their kiosk system, which is Linux-based. The system stores customer data to a file called car-wash-customers.csv. The file includes the following fields: Customer Number, First Name, Last Name, RFID Tag Number, Vehicle Identification Number (VIN), Car Wash Level, and Expiration Date.

The system stores sales data in a file called car-wash-sales.csv. The file includes the following fields: Transaction Number, Date, Location Number, RFID Tag Number, Customer Number, and Wash Type.

AnyCompany Car Washes wants the sales and customer data uploaded to the cloud every 5 minutes. The company also wants the data backed up locally every 5 minutes to a local backup directory. It wants the backups zipped to save space.

To complete this assignment, you must create multiple scripts and schedule them in the cron table (crontab) schedule. The scripts are as follows:

config.sh: This file contains settings specific to the location, including the location number and S3 bucket name. You can source this file from your other bash scripts.

backup.sh: This script makes copies of the car-wash-customers.csv and car-wash-sales.csv files and places them in a backup directory. The script then zips the files into a file named data_backup.csv.

upload.sh: This script uploads the car-wash-customers.csv and car-wash-sales.csv files to an S3 bucket in a path under the location ID called my_bucket/1234/car-wash-customers.csv and my_bucket/1234/car-wash-sales.csv. The numbers 1234 represent the location number.

Only the Linux ec2-user should have read, write, and execute permissions on the scripts. All other users should have only read permissions on the created files.

Services used in this lab
AWS CLI
The AWS Command Line Interface (AWS CLI) is a tool that you can use to interact with Amazon Web Services (AWS) services by using commands in your command-line shell. With minimal configuration, you can start running commands from the command prompt in your terminal program that implement functionality equivalent to that provided by the browser-based AWS Management Console.

All AWS infrastructure as a service (IaaS) administration, management, and access functions in the console are available in the AWS API and AWS CLI.

You can explore a service’s capabilities with the AWS CLI and develop shell scripts to manage your resources. In addition to the low-level, API-equivalent commands, several AWS services provide customizations for the AWS CLI. Customizations can include higher-level commands that make using a service with a complex API less complicated. An example of this is the aws s3api low-level commands and the higher-level aws s3 commands.

Amazon S3
Amazon S3 is an object storage service designed to offer industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-centered applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

Task 1: Troubleshoot the upload.sh script
In this task, you correct misconfigurations related to the upload.sh script. You review the upload.log file to find issues with the setup.

Task 1.1: Verify the Amazon S3 bucket name in config.sh
In this task, you connect to the kiosk server and begin to investigate the cause of any reported issues.

Copy the InstanceASessionUrl value that is listed to the left of these instructions, and paste it into a new browser tab to connect to the kiosk server.

 Command: To assume the ec2-user, run this command:


sudo su ec2-user
 Command: To change directories to the application logs directory, run this command:

cd ~/car-wash-kiosk/logs
 Command: To view the contents of the upload.log file using nano text editor, run this command:

cat upload.log
 Expected output: You might notice that several entries in the log file look similar to the following excerpt. The most recent entry appears at the end of the file.


Uploading sales and customer data for location 1001
S3_BUCKET_NAME=customer-and-sales-bucket
LOCATION_NUMBER=1001
upload failed: car-wash-kiosk/data/car-wash-customers.csv to s3://customer-and-sales-bucket/1001/car-wash-customers.csv An error occurred (NoSuchBucket) when calling the PutObject operation: The specified bucket does not exist
upload failed: car-wash-kiosk/data/car-wash-sales.csv to s3://customer-and-sales-bucket/1001/car-wash-sales.csv An error occurred (NoSuchBucket) when calling the PutObject operation: The specified bucket does not exist
Upload complete
 Note: The output in the upload.log file indicates that the S3 bucket where the process is attempting to upload objects does not exist. In the next few steps, you determine the correct S3 bucket name.

Return to the browser tab that has the AWS Management Console.

On the AWS Management Console, in the  search box, search for and choose S3.

Under General purpose buckets, find the S3 bucket with customersalesbucket in the name.

 Copy edit: Copy the S3 bucket name, paste it into notepad or another text editor, and save it to use later.

Return to the browser tab with the terminal window.

 Command: To navigate to the bin directory of the application, run this command:


cd ../bin
 Command: To use nano text editor to open the config.sh file, run this command:

nano config.sh
 Expected output:


S3_BUCKET_NAME=customer-and-sales-bucket
LOCATION_NUMBER=1001
 Note: In the output above, customer-and-sales-bucket is not the correct value for S3_BUCKET_NAME.

Update the customer-and-sales-bucket value with the name of the S3 bucket that you saved earlier in this task.

To save the file, press Ctrl + O, and then press Enter to confirm saving the file.

To exit nano text editor, press Ctrl + X.

 Command: To test the changes to config.sh, run this command:


./upload.sh
 Expected output:


S3_BUCKET_NAME=labstack-a3ca558b-367e-4ade-b-customersalesbucket-m22xfcrmlhcc
LOCATION_NUMBER=1001
upload failed: ../data/car-wash-customers.csv to s3://labstack-a3ca558b-367e-4ade-b-customersalesbucket-m22xfcrmlhcc/1001/car-wash-customers.csv An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
upload failed: ../data/car-wash-sales.csv to s3://labstack-a3ca558b-367e-4ade-b-customersalesbucket-m22xfcrmlhcc/1001/car-wash-sales.csv An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
Upload complete
 Note: Notice that the bucket name is correct, but an error occurs when trying to write the objects to Amazon S3. AccessDenied indicates that the identity behind the process does not have access to the S3 bucket. In the next task, you verify the identity and correct the error.

Task 1.2: Configure permissions to load objects into the S3 bucket
In this task, you correct the AccessDenied issue with upload.sh. In the AWS environment where the S3 bucket holds the sales and customer data, there is a role configured with permissions to create and update S3 objects. The kiosk server must use this role when interacting with AWS.

 Command: To configure the AWS credentials, run this command:

aws configure
For the aws configure prompt, replace the following LabAccessKeyId, LabSecretKey, and LabRegion placeholder values with the values listed to the left of these instructions. After you enter a value, press Enter to move to the next prompt.
AWS Access Key ID [None]: LabAccessKeyId
AWS Secret Access Key [None]: LabSecretKey
Default region name [None]: LabRegion
Default output format [None]: json
 WARNING: Replace the placeholder values with the specified values or you will not have the appropriate access to complete the lab.

 Expected output: There is no output.

 Command: To run upload.sh and verify that the upload is successful, run this command:

./upload.sh
 Expected output:



Uploading sales and customer data for location 1001
S3_BUCKET_NAME=labstack-a3ca558b-367e-4ade-b-customersalesbucket-m22xfcrmlhccLOCATION_NUMBER=1001
upload: ../data/car-wash-customers.csv to s3://labstack-a3ca558b-367e-4ade-b-customersalesbucket-m22xfcrmlhcc/1001/car-wash-customers.csvupload: 
        ../data/car-wash-sales.csv to s3://labstack-a3ca558b-367e-4ade-b-customersalesbucket-m22xfcrmlhcc/1001/car-wash-sales.csv
Upload complete
Notice that the output for upload.sh contains no errors.

 Congratulations! You successfully corrected the errors with upload.sh.

Task 2: Troubleshoot the backup.sh script
In this task, you correct misconfigurations related to the backup.sh script. You review the backup.log file to find issues with the setup.

Task 2.1: Correct the backup directory permissions
 Command: To change directories to the application logs directory, run this command:

cd ../logs
 Command: To view the contents of the backup.log file in nano text editor, run this command:

nano backup.log
 Expected output: You might notice that several entries in the log file look similar to the following excerpt. The most recent entry appears at the end of the file.


S3 Bucket = labstack-a3ca558b-367e-4ade-b4-customersalesbucket-rh4fm25svrfi
BACKUP_DIRECTORY = /home/ec2-user/car-wash-kiosk/backup
BACKUP_FILE_NAME = data-backup-2023-12-07-16-39.zip
cp: cannot create regular file '/home/ec2-user/car-wash-kiosk/backup/car-wash-customers.csv': Permission denied
cp: cannot create regular file '/home/ec2-user/car-wash-kiosk/backup/car-wash-sales.csv': Permission denied
        zip warning: name not matched: car-wash-customers.csv
        zip warning: name not matched: car-wash-sales.csv

zip error: Nothing to do! (try: zip -r data-backup-2023-12-07-16-39.zip . -i car-wash-customers.csv car-wash-sales.csv)
rm: cannot remove 'car-wash-customers.csv': No such file or directory
rm: cannot remove 'car-wash-sales.csv': No such file or directory
Backup complete
 Note: The output indicates that the cp command returns a Permission denied error when trying to create files in the backup directory.

To exit nano text editor, press Ctrl + X.

 Command: To view the permissions of the backup directory, run this command:


cd ..
ll
 Expected output:


d---------. 2 ec2-user ec2-user  6 Dec  7 16:35 backup
drwxr-xr-x. 2 ec2-user ec2-user 57 Dec  7 16:15 bin
drwxr-xr-x. 2 ec2-user ec2-user 62 Dec  7 16:20 data
drwxr-xr-x. 2 ec2-user ec2-user 62 Dec  7 16:38 logs
 Note: In the previous output, notice that for the backup directory, neither the owner, group, or others have read or write permissions in the directory. This is a misconfiguration. In the next steps, you modify the permissions for the backup directory.

 Command: To update the permissions for the backup directory, run this command:

chmod u+rwx,g+r,o+r backup
 Note: The previous command modifies the backup directory by adding read, write, and execute permissions to the owner, read and execute permissions to the group, and read permissions to others.

 Command: To verify that the permissions have been updated, run this command:

ll
 Expected output:


drwxr--r--. 2 ec2-user ec2-user  6 Dec  7 16:35 backup
drwxr-xr-x. 2 ec2-user ec2-user 57 Dec  7 16:15 bin
drwxr-xr-x. 2 ec2-user ec2-user 62 Dec  7 16:20 data
drwxr-xr-x. 2 ec2-user ec2-user 62 Dec  7 16:38 logs
 Command: To run the backup.sh script, run this command:

cd bin
./backup.sh
 Expected output:


S3 Bucket = labstack-a3ca558b-367e-4ade-b4-customersalesbucket-rh4fm25svrfi
BACKUP_DIRECTORY = /home/ec2-user/car-wash-kiosk/backup
BACKUP_FILE_NAME = data-backup-2023-12-07-17-02.zip
  adding: car-wash-customers.csv (deflated 44%)
  adding: car-wash-sales.csv (deflated 60%)
Backup complete
Notice that the output for backup.sh has no errors.

 Congratulations! You successfully corrected the errors with backup.sh.

Task 3: Add retry logic to the upload script
In this task, you modify the upload.sh script so that it tries to upload the files to the Amazon S3 bucket 3 times before exiting.

 Command: To delete all of the existing contents from the upload.sh script, run the following command:

truncate --size 0 upload.sh
 Note: The truncate command is used to shrink or extend the size of a file to the specified size. In this case, you specify the --size parameter to set the file size to 0 bytes. This deletes all of the contents of the file.

 Command: To open upload.sh using the nano text editor, run this command:

nano upload.sh
Copy the following information, and paste it into the backup.sh file in nano text editor:

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
To save the file, press Ctrl + O, and then press Enter to confirm saving the file.

To exit nano, press Ctrl + X.

 Command: To test the upload.sh script, run this command:


./upload.sh
 Expected output:


Uploading sales and customer data for location 1001
S3_BUCKET_NAME=labstack-a3ca558b-367e-4ade-b4-customersalesbucket-rh4fm25svrfi
LOCATION_NUMBER=1001
upload: ../data/car-wash-customers.csv to s3://labstack-a3ca558b-367e-4ade-b4-customersalesbucket-rh4fm25svrfi/1001/car-wash-customers.csv
upload: ../data/car-wash-sales.csv to s3://labstack-a3ca558b-367e-4ade-b4-customersalesbucket-rh4fm25svrfi/1001/car-wash-sales.csv
Upload complete
 Congratulations! You modified upload.sh to be more resilient by adding retry logic.

Conclusion
Congratulations! You have successfully done the following:

Inspected a kiosk environment to make sure that it is set up properly.
Reviewed the log output from bash scripts to troubleshoot errors.
Implemented retry logic in a bash shell script using a loop.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
For more information, see each of the following resources:

AWS CLI Command Reference: create-bucket
Cron Expressions Reference in the Amazon EventBridge User Guide