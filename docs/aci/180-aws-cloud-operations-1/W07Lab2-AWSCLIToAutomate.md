# Using the AWS CLI in Bash to Automate Linux

## Lab overview

In this lab, you create and configure Bash shell scripts on a Linux environment to automate routine maintenance tasks.

Objectives
By the end of this lab, you will be able to do the following:

Navigate a Linux environment to inspect an existing application.
Create and modify folders and files for your maintenance solution.
Create Bash shell scripts to take backups and upload files to the Amazon Web Services (AWS) Cloud.
Schedule the maintenance scripts to run automatically by using the Linux crontab (cron) utility.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, Mac OS X, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab will require 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal
 Congratulations! You have successfully completed a task
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
Services used in this lab
AWS CLI:
The AWS Command Line Interface (AWS CLI) is an open-source tool that you can use to interact with AWS services by using commands in your command-line shell. With minimal configuration, you can start running commands from the command prompt in your terminal program that implement functionality equivalent to that provided by the browser-based AWS Management Console.

All AWS infrastructure as a service (IaaS) administration, management, and access functions in the console are available in the AWS API and AWS CLI.

You can explore a service’s capabilities with the AWS CLI and develop shell scripts to manage your resources. In addition to the low-level, API-equivalent commands, several AWS services provide customizations for the AWS CLI. Customizations can include higher-level commands that simplify using a service with a complex API. An example of this is the aws s3api low-level commands and the higher-level aws s3 commands.

Amazon S3:
Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and user-friendly management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

Scenario
AnyCompany Car Washes is a car wash company that has automated car washes in multiple locations. Customers sign up using a kiosk that dispenses an RFID tag sticker for the customer to place in the front window of their vehicle. After the customer has purchased a subscription (Basic, Enhanced, or Extreme), they are granted automatic access to the car wash based on the RFID tag.

Architecture diagram for car wash kiosk.

Figure: The car wash kiosk server sends customer and sales data files to the AWS Cloud containing an Amazon S3 bucket and a LabStudent user with permissions to create and update Amazon S3.

AnyCompany Car Washes needs to automate backups and sales reporting in their kiosk system, which is Linux based. Customer data is stored to a file (car-wash-customers.csv) with the following fields: Customer Number, First Name, Last Name, RFID Tag Number, VIN Number, Car Wash Level, and Expiration Date.

Sales data is stored in a file (car-wash-sales.csv) with the following fields: Transaction Number, Date, Location Number, RFID Tag Number, Customer Number, and Wash Type.

The sales and customer data must be uploaded to the cloud every 5 minutes. Data should be backed up locally every 5 minutes to a local backup directory. Backups should be zipped to save space.

To complete this assignment, you must create multiple scripts and schedule them in the crontab scheduler.

config.sh: This file contains settings specific to the location: location number and S3 bucket name. This file can be sourced from your other bash scripts.

backup.sh: This script makes copies of the car-wash-customers.csv and car-wash-sales.csv files and places them in a backup directory. The script then zips the files into a file named data_backup.csv.

upload.sh: This script uploads the car-wash-customers.csv and car-wash-sales.csv files to an S3 bucket in a path under the location id: my_bucket/1234/car-wash-customers.csv and my_bucket/1234/car-wash-sales.csv. In the previous sentence, 1234 is the location number.

Only the ec2-user Linux user should be allowed read/write/execute privileges on the scripts. All other users should only have read privileges on the created files.

Task 1: Inspecting the application setup and configuring the AWS credentials
In this task, you review the Linux environment where the car wash system is set up. You see where the files you are working with are located. You configure AWS credentials to be used with the AWS CLI. Finally, you create an Amazon S3 bucket where the sales and customer data files are uploaded.

Task 1.1: Inspecting the application setup
In this task, you review the Linux environment and locate the data and logs directories.

Copy the InstanceASessionUrl value that is listed to the left of these instructions, and paste it into a new browser tab.

 Command: To see the current user that you are assuming, run the following command in the command prompt:


whoami
 Expected output:


ssm-user
The output of the whoami command tells you that you are currently logged in to the system as ssm-user. For this application, we want to switch to the ec2-user.

 Command: To assume the ec2-user, run the following command:

sudo su ec2-user
 Command: To change directories to the ec2-user home directory, run the following command:

cd ~
 Command: To list the contents of the home directory, run the following command:

ll
 Expected output:


total 0
drwxr-xr-x. 5 ec2-user ec2-user 46 Nov 14 00:39 car-wash-kiosk
 Command: To view the contents of the car-wash-kiosk directory, run the following commands:

cd car-wash-kiosk
ll
 Expected output:


total 0
drwxr-xr-x. 2 ec2-user ec2-user 62 Nov 14 01:51 data
drwxr-xr-x. 2 ec2-user ec2-user 26 Nov 14 01:53 logs
 Note: A data directory and a logs directory have already been created. The data directory contains the customer and sales files. The logs directory will be used to store output from the application scripts.

Task 1.2: Configuring the AWS credentials
In this task, you configure the AWS credentials that allow you to create and send objects to the Amazon S3 bucket by using the AWS CLI.

 Command: To configure the AWS credentials, run the following command:

aws configure
Enter the following information in the aws configure prompt. Replace the LabAccessKeyId, LabSecretKey, and LabRegion placeholders with the values that are listed to the left of these instructions. When each value is entered, press Enter on the keyboard to move on to the next prompt:
AWS Access Key ID [None]: LabAccessKeyId
AWS Secret Access Key [None]: LabSecretKey
Default region name [None]: LabRegion
Default output format [None]: json
 WARNING: Replace the placeholders with the specified values or you will not have the appropriate access to complete the lab.

 Expected output: There is no output.

Task 1.3: Creating an S3 bucket
In this task, you use the AWS CLI to create an S3 bucket. After it is created, you verify that the bucket is in your account.

 Copy edit: Copy the following code into a text editor. Replace the DOC-EXAMPLE-BUCKET placeholder value with your first initial, last name, a hyphen, and your ZIP code. This will be the name of your bucket.

aws s3api create-bucket --bucket DOC-EXAMPLE-BUCKET --create-bucket-configuration LocationConstraint=us-west-2
 WARNING: Amazon S3 bucket names must be globally unique. For example, a user named Terry Whitlock with a ZIP code of 12345 would run the following code string:


aws s3api create-bucket --bucket twhitlock-12345 --create-bucket-configuration LocationConstraint=us-west-2
 Command: To create an S3 bucket, run the edited code in the command prompt.
 Expected example output:


{
    "Location": "http://twhitlock-12345.s3.amazonaws.com/"
}
 Command: To list the S3 buckets in your AWS account, run the following command:

aws s3api list-buckets
 Expected example output:


{
    "Buckets": [
        {
            "Name": "awslabs-resources-krxqqla59sui8d-us-east-1-582728007443",
            "CreationDate": "2023-03-01T06:46:56+00:00"
        },
        {
            "Name": "awslabs-resources-r5b3y6ojjszcap-us-east-1-582728007443",
            "CreationDate": "2023-10-02T23:13:56+00:00"
        },
        {
            "Name": "twhitlock-12345",
            "CreationDate": "2023-11-15T18:05:45+00:00"
        },
        {
            "Name": "labstack-a3ca558b-367e-4ade-b4d3-repotestingbucket-8tufgmk7migp",
            "CreationDate": "2023-11-15T17:59:14+00:00"
        }
    ],
    "Owner": {
        "DisplayName": "aws-labs-accounts+prodkiku-vv46EGCCWGt9PYgccC1iJk",
        "ID": "8cc98a27c9476409194c1ab657763007305dcd7df0216d57eaa5fbf6ac134cce"
    }
}
Task 1.4: Installing the necessary utilities to support the application
In this task, you install nano and zip.

 Command: To install nano and zip, run the following command:

sudo yum install -y nano zip
 Expected output:


Complete!
Congratulations! You have inspected the application setup and set up your credentials.

Task 2: Creating the appropriate directories
In this task, you create the bin and backup directories for your application, and set the appropriate permissions on the directories.

 Command: To create the application directories, run the following commands:

cd /home/ec2-user/car-wash-kiosk
mkdir bin
mkdir backup
 Command: To navigate to the bin directory, to create config.sh, and to modify the permissions to add execute permission to the file owner and remove write permission from the file’s group, run the following commands:

cd bin
touch config.sh
chmod g-w,u+x config.sh
 Command: To open config.sh using the nano editor, run the following command:

nano config.sh
 Copy edit: Copy the following code into a text editor. Replace YOUR_BUCKET_NAME with the name of the bucket that you created in Task 1.3.

S3_BUCKET_NAME=YOUR_BUCKET_NAME
LOCATION_NUMBER=1001
Copy and paste the edited code into the config.sh file in nano.

Save the file (Ctrl-O), confirm saving the file (Enter), and exit nano (Ctrl-X).

Task 3: Creating the backup.sh script
In this task, you create and test the backup.sh script.

 Command: To create the backup.sh script, run the following commands:

touch backup.sh
chmod g-w,u+x backup.sh
 Command: To open backup.sh using the nano editor, run the following command:

nano backup.sh
Copy and paste the following into the backup.sh file in nano:

#!/bin/bash

source /home/ec2-user/car-wash-kiosk/bin/config.sh

echo "S3 Bucket = $S3_BUCKET_NAME"
DATA_DIRECTORY="/home/ec2-user/car-wash-kiosk/data"
BACKUP_DIRECTORY="/home/ec2-user/car-wash-kiosk/backup"
BACKUP_FILE_NAME="data-backup-$(date +%Y-%m-%d-%H-%M).zip"

echo "BACKUP_DIRECTORY = $BACKUP_DIRECTORY"
echo "BACKUP_FILE_NAME = $BACKUP_FILE_NAME"

# copy car-wash-customers.csv and car-wash-sales.csv to the backup directory and zip them
cp $DATA_DIRECTORY/car-wash-customers.csv $DATA_DIRECTORY/car-wash-sales.csv $BACKUP_DIRECTORY
cd $BACKUP_DIRECTORY
zip -r $BACKUP_FILE_NAME car-wash-customers.csv car-wash-sales.csv
rm car-wash-customers.csv car-wash-sales.csv
cd ..

echo "Backup complete"
 Note: The backup.sh script copies the car-wash-customers.csv and car-wash-sales.csv files to the backup directory and then zips the files into a single archive named data-backup- with the current date appended. The script removes the file copies from the data directory.

Save the file (Ctrl-O), confirm saving the file (Enter), and exit nano (Ctrl-X).

 Command: To test the backup.sh script, run the following command:


./backup.sh
 Expected output:


S3 Bucket = car-wash-923d
BACKUP_DIRECTORY = /home/ec2-user/car-wash-kiosk/backup
BACKUP_FILE_NAME = data-backup-2023-11-14-20-31.zip
  adding: car-wash-customers.csv (deflated 40%)
  adding: car-wash-sales.csv (deflated 50%)
Backup complete
Task 4: Creating the upload.sh script
In this task, you create and test the upload.sh script.

 Command: To create the upload.sh script, run the following command:

touch upload.sh
chmod g-w,u+x upload.sh
 Command: To open upload.sh using nano, run the following command:

nano upload.sh
Copy and paste the following into the upload.sh script.

#!/bin/bash
source /home/ec2-user/car-wash-kiosk/bin/config.sh

DATA_DIRECTORY="/home/ec2-user/car-wash-kiosk/data"

echo "Uploading sales and customer data for location $LOCATION_NUMBER"
echo "S3_BUCKET_NAME = $S3_BUCKET_NAME"
echo "LOCATION_NUMBER = $LOCATION_NUMBER"


# upload sales data to s3 with a $location prefix
aws s3 cp $DATA_DIRECTORY/car-wash-customers.csv s3://$S3_BUCKET_NAME/$LOCATION_NUMBER/car-wash-customers.csv
aws s3 cp $DATA_DIRECTORY/car-wash-sales.csv s3://$S3_BUCKET_NAME/$LOCATION_NUMBER/car-wash-sales.csv

echo "Upload complete"
 Note: The upload.sh script uploads the car-wash-customers.csv and car-wash-sales.csv files to the S3 bucket that is configured in config.sh. The files are saved with a prefix of the location number that is in config.sh.

Save the file (Ctrl-O), confirm saving the file (Enter), and exit nano (Ctrl-X).

 Command: To test the backup.sh script, run the following command:


./upload.sh
 Expected output:


Uploading sales and customer data for location 1001
S3_BUCKET_NAME = car-wash-923d
LOCATION_NUMBER = 1001
upload: ../data/car-wash-customers.csv to s3://car-wash-923d/1001/car-wash-customers.csv
upload: ../data/car-wash-sales.csv to s3://car-wash-923d/1001/car-wash-sales.csv
Upload complete
 CAUTION: If your output is not similar to the expected output and contains error messages, return to the instructions for config.sh (Task 2), and confirm that your setting for S3_BUCKET_NAME is correct. Then reattempt running the ./upload.sh command.

Task 5: Scheduling the scripts to run by using cron
In this task, you schedule the backup.sh and upload.sh scripts to run every 5 minutes by using cron. You also configure the scripts to write output to files called backup.log and upload.log.

 Command: To navigate to the ec2-user home directory, run the following command:

cd ~
 Command: To write the ec2-user crontab file to a file named cronfile, run the following command:

crontab -l > cronfile
To open cronfile using nano, run the following command:

nano cronfile
 Note: Notice that the cronfile already has an entry. This entry must remain. The lines that you add in the next step are in addition to this line.

Copy and paste the following lines at the end of the file.

*/5 * * * * /home/ec2-user/car-wash-kiosk/bin/backup.sh >> /home/ec2-user/car-wash-kiosk/logs/backup.log
*/5 * * * * /home/ec2-user/car-wash-kiosk/bin/upload.sh >> /home/ec2-user/car-wash-kiosk/logs/upload.log
Save the file (Ctrl-O), confirm saving the file (Enter), and exit nano (Ctrl-X).

 Command: To update the ec2-user crontab, run the following command:


crontab cronfile
 Note: The backup.sh and upload.sh files are now scheduled to run every 5 minutes. For example, the files will run at 1:00, 1:05, 1:10, and so on.

 Note: You can verify that the jobs are running as scheduled by viewing the log files in the log directory. You might have to wait up to 5 minutes for the log files to appear.

To navigate to the log directory, run the following command:

cd /home/ec2-user/car-wash-kiosk/logs
 Note: You can list the contents of the directory to verify that the files have been created. You can use nano to view the contents of the log files to see the results of the scripts running.

 Copy edit: Copy the following code into a text editor. Replace DOC-EXAMPLE-BUCKET with the name of the bucket that you created in Task 1.3:

aws s3api list-objects-v2 --bucket DOC-EXAMPLE-BUCKET --prefix 1001
 Command: To verify that the files have been successfully uploaded to Amazon S3, run the edited command.
 Expected output:


{
    "Contents": [
        {
            "Key": "1001/car-wash-customers.csv",
            "LastModified": "2023-11-29T00:20:04+00:00",
            "ETag": "\"a58c8d16e468269599b2f4402d503643\"",
            "Size": 1578,
            "StorageClass": "STANDARD"
        },
        {
            "Key": "1001/car-wash-sales.csv",
            "LastModified": "2023-11-29T00:20:05+00:00",
            "ETag": "\"79fd22e2092fc2ba135dc34f00953c03\"",
            "Size": 1810,
            "StorageClass": "STANDARD"
        }
    ]
}
Congratulations! You have scheduled your scripts to run automatically by using the Linux crontab utility.

Conclusion
Congratulations! You have successfully done the following:

Reviewed an existing Linux environment and set up the environment to host your application.
Created and modified folders and files for your maintenance application.
Created backup.sh and upload.sh Bash shell scripts to take backups and upload files to the AWS Cloud.
Scheduled the maintenance scripts to run automatically by using the Linux crontab utility.
Additional resources
For more information, see create-bucket.
For more information, see Cron Expressions Reference.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.