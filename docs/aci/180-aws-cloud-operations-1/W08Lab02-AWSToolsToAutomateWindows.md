# Using the AWS Tools for Windows PowerShell to Automate Windows

## Lab Overview

In this lab, you create and configure Windows Windows Windows PowerShell scripts on a Windows environment to automate routine maintenance tasks.

Objectives
By the end of this lab, you will be able to do the following:

Navigate a Windows environment to inspect an existing application.
Create and modify folders and files for your maintenance solution.
Create Windows PowerShell scripts to take backups and upload files to the AWS Cloud.
Schedule the maintenance scripts to run automatically using Task Scheduler in Windows.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, Mac OS X, or Linux (Ubuntu, SuSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab will require 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Additional information: Where to find more information.
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal.
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
AnyCompany Car Washes is a car wash company that has automated car washes in multiple locations. Customers sign up using a kiosk which dispenses an RFID Tag Sticker for the customer to place in the front window of their vehicle. After the customer has purchased a subscription (Basic, Enhanced, or Extreme), they are granted automatic access to the car wash based on the RFID Tag.

The following diagram shows the basic architecture of the car wash kiosk system:

Architecture diagram for car wash kiosk.

Figure: The car wash kiosk server sends customer and sales data files to the AWS Cloud. The AWS Cloud contains an Amazon Simple Storage Service (Amazon S3) bucket and an AWS Identity and Access Management (IAM) user named LabStudent. The IAM user has permissions to create and update Amazon S3.

AnyCompany Car Washes needs to automate backups and sales reporting in their kiosk system, which is Windows-based. Customer data is stored to a file (car-wash-customers.csv) with the following fields: Customer Number, First Name, Last Name, Radio-frequency identification(RFID) Tag Number, Vehicle Identification Number (VIN), Car Wash Level, and Expiration Date.

Sales data is stored in a file (car-wash-sales.csv) with the following fields: Transaction Number, Date, Location Number, RFID Tag Number, Customer Number, and Wash Type.

The sales and customer data needs to be uploaded to the cloud every 5 minutes. Data should be backed up locally every 5 minutes to a local backup directory. Backups should be zipped to save space.

To complete this assignment, you create multiple scripts and schedule them in the Task Scheduler. With the Task Scheduler, you can automatically perform routine tasks on a chosen computer. The Task Scheduler monitors the criteria you choose, called triggers, and performs the tasks when the criteria are met.

The following are a list of Windows PowerShell scripts used in this lab:

config.ps1: This file contains settings specific to the location, including the location number and Amazon Simple Storage Service (Amazon S3) bucket name. You can source this file from your other PowerShell scripts.

backup.ps1: This script makes copies of the car-wash-customers.csv and car-wash-sales.csv files and places them in a backup directory. The script then zips the files into a file named data_backup.csv

upload.ps1: This script uploads the car-wash-customers.csv and car-wash-sales.csv files to an S3 bucket in a path under the location ID called my_bucket/1234/car-wash-customers.csv and my_bucket/1234/car-wash-sales.csv. Here, 1234 is the location ID.

Services used in this lab
AWS Tools for Windows PowerShell:
The AWS Tools for PowerShell are a set of PowerShell modules that are built on the functionality exposed by the AWS SDK for .NET. With AWS Tools for PowerShell, you can script operations on your Amazon Web Services (AWS) resources from the PowerShell command line.

The cmdlets provide an idiomatic PowerShell experience for specifying parameters and handling results even though they are implemented using the various AWS service HTTP query APIs. For example, the cmdlets for the AWS Tools for PowerShell support PowerShell pipelining, which means you can pipe PowerShell objects in and out of the cmdlets.

The AWS Tools for PowerShell are flexible in how you can use them to handle credentials, including support for the AWS Identity and Access Management (IAM) infrastructure. You can use the tools with IAM user credentials, temporary security tokens, and IAM roles.

Amazon S3:
Amazon S3 is an object storage service designed to offer industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-centered applications, and mobile apps. With cost-effective storage classes and user-friendly management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

Task 1: Inspecting the application setup and configuring the AWS credentials
In this task, you review the Windows environment where the car wash system is set up. You examine where the files you are working with are located. You configure AWS credentials to be used with the AWS Tools for Windows PowerShell. Finally, you create an Amazon S3 bucket where the sales and customer data files are uploaded.

Task 1.1: Inspect the application setup
In this task, you review the Windows environment and locate the data and logs directories.

In the Lab Information navigation pane, copy and paste the WindowsInstanceSessionUrl into a new browser tab.
 WARNING: If you receive i-xxxxxxxxx is not connected message, Please wait for about 5 minutes for the instance to come online and then try again.

 Command: To see the current user that you are assuming, run the following command:

whoami
 Expected output:


ec2amaz-aa2pgd1\ssm-user
The output of the whoami command indicates that you are currently logged into the system as ssm-user.

 Command: To change directories to the application directory, run the following command:

cd C:\apps\
 Command: To list the contents of the apps directory, run the following command:

ls
 Expected output:


    Directory: C:\apps


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        12/20/2023   9:32 PM                car-wash-kiosk
 Command: To view the contents of the car-wash-kiosk directory, run the following commands:

cd car-wash-kiosk
ls
 Expected output:


    Directory: C:\apps\car-wash-kiosk


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        12/20/2023   9:32 PM                .machine
d-----        12/20/2023   9:32 PM                data
d-----        12/20/2023   9:32 PM                logs
 Note: A data directory and a logs directory have already been created. The data directory contains the customer and sales files. The logs directory will be used to store output from the application scripts.

Task 1.2: Configure the AWS credentials
In this task, you configure the AWS credentials used to create and send objects to the S3 bucket by using the AWS Tools for Windows PowerShell.

 Copy edit: Copy the following command, paste it into a text editor, and replace the LAB_ACCESS_KEY_ID and LAB_SECRET_KEY placeholder values with the LabAccessKeyId and LabSecretKey values listed to the left of these instructions:

Set-AWSCredential -AccessKey LAB_ACCESS_KEY_ID -SecretKey LAB_SECRET_KEY -StoreAs MyLabProfile
Copy and paste the edited command into the terminal and press Enter.
 WARNING: Replace the placeholders with the specified values or you will not have the appropriate access to complete the lab.

 WARNING: This command will take some time to complete, please wait for about 2 to 3 minutes.

 Expected output: There is no output, you have to wait for the prompt to show up again.

 Command: Use Set-AWSCredential command to specify a default profile for a particular session.

Set-AWSCredential -ProfileName MyLabProfile
 Note: This profile overrides the default profile for the duration of the session.

Task 1.3: Create an S3 bucket
In this task, you create an S3 bucket using the AWS Tools for Windows PowerShell. Once created, you verify that the bucket is in your account.

 Copy edit: Copy the following code into a text editor. Replace the DOC_EXAMPLE_BUCKET placeholder value with your first initial, last name, a hyphen, and a random 5 digit number. This will be the name of your bucket.

New-S3Bucket -BucketName DOC_EXAMPLE_BUCKET -Region us-west-2
 WARNING: Amazon S3 bucket names must be globally unique. Replace the capital letters with your first initial, last name, and a random 5 digit number. For example a user named Terry Whitlock with a random number of 12345 would enter the following code.:


New-S3Bucket -BucketName twhitlock-12345 -Region us-west-2
 Expected example output:


CreationDate           BucketName
------------           ----------
12/20/2023 10:08:16 PM twhitlock-12345
 Command: To list the S3 buckets in your AWS account, run:

Get-S3Bucket
 Expected output:


CreationDate           BucketName
------------           ----------
2/28/2023 3:16:08 AM   awslabs-resources-krxqqla59sui8d-us-east-1-000688971897
12/20/2023 10:08:17 PM twhitlock-12345
 Task complete: You have successfully inspected the application setup and set up your credentials.

Task 2: Create the appropriate directories
In this task, you create the bin and backup directories for your application. Bin directory will have all your Windows PowerShell scripts, whereas the backup directory is used to keep backup zip files.

 Command: To create the application directories, run the following commands:

mkdir backup
mkdir bin
 Command: To navigate to the bin directory, to create and open config.ps1 by using the nano text editor, run the following command:

cd bin
nano config.ps1
 Note: An alternate option to edit a file in Windows environment is Windows notepad, which would only be available via remote desktop session. To edit a file in a Session Manager, a capability of AWS Systems Manager, nano text editor has been installed on your Windows instance.

 Copy edit: Copy the following code into the config.ps1 file in nano. Be sure to replace YOUR_BUCKET_NAME with the name of the bucket that you created in Task 1.3.

$S3_BUCKET_NAME="YOUR_BUCKET_NAME"
$LOCATION_NUMBER="1001"
To save the file, press Ctrl + S.

To exit the nano editor, press Ctrl + X.

 Task complete: You have successfully created the backup directory and the config.ps1 file.

Task 3: Create the backup.ps1 script
In this task, you create and test the backup.ps1 script.

 Command: To create and open backup.ps1 by using the nano editor, run the following command:

nano backup.ps1
Copy and paste the following into the backup.ps1 file in nano.

Write-Host "started backup script $(Get-Date -Format 'yyyy-MM-dd-HH-mm')"

# Set data and backup directories
$DATA_DIRECTORY = "C:\apps\car-wash-kiosk\data"
$BACKUP_DIRECTORY = "C:\apps\car-wash-kiosk\backup"
$BACKUP_FILE_NAME = "data-backup-$(Get-Date -Format 'yyyy-MM-dd-HH-mm').zip"

Write-Host "BACKUP_DIRECTORY = $BACKUP_DIRECTORY"
Write-Host "BACKUP_FILE_NAME = $BACKUP_FILE_NAME"

# Copy customer_data.csv and sales_data.csv to the backup directory and zip them
Copy-Item "$DATA_DIRECTORY\car-wash-customers.csv", "$DATA_DIRECTORY\car-wash-sales.csv" -Destination $BACKUP_DIRECTORY
Set-Location $BACKUP_DIRECTORY
Compress-Archive -Path "car-wash-customers.csv", "car-wash-sales.csv" -DestinationPath $BACKUP_FILE_NAME
Remove-Item "car-wash-customers.csv", "car-wash-sales.csv"

Write-Host "Backup complete"
 Note: The backup.ps1 script copies the car-wash-customers.csv and car-wash-sales.csv files to the backup directory and then zips the files into a single archive named data-backup- with the current date appended. The script removes the file copies from the data directory.

To save the file, press Ctrl + S.

To exit nano editor, press Ctrl + X.

 Command: To test the backup.ps1 script, run the following command:


.\backup.ps1
 Expected output:


started backup script 2024-01-02-19-11
BACKUP_DIRECTORY = C:\apps\car-wash-kiosk\backup
BACKUP_FILE_NAME = data-backup-2024-01-02-19-11.zip
Backup complete
 Task complete: You have successfully created backup.ps1 script.

Task 4: Create the upload.ps1 script
In this task, you create and test the upload.ps1 script.

 Command: To create and open upload.ps1 by using the nano editor, run the following command:

cd C:\apps\car-wash-kiosk\bin
nano upload.ps1
Copy and paste the following into the upload.ps1 script.

# Import configuration from config.ps1
. C:\apps\car-wash-kiosk\bin\config.ps1

Write-Host "started upload script $(Get-Date -Format 'yyyy-MM-dd-HH-mm')"

$DATA_DIRECTORY = "C:\apps\car-wash-kiosk\data"

Write-Host "Uploading sales and customer data for location $LOCATION_NUMBER"
Write-Host "S3_BUCKET_NAME = $S3_BUCKET_NAME"
Write-Host "LOCATION_NUMBER = $LOCATION_NUMBER"

# Upload sales data to S3 with a $location prefix
Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car-wash-customers.csv  -File $DATA_DIRECTORY\car-wash-customers.csv -ProfileName MyLabProfile
Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car-wash-sales.csv  -File $DATA_DIRECTORY\car-wash-sales.csv -ProfileName MyLabProfile

Write-Host "Upload complete"
 Note: The upload.ps1 script uploads the car-wash-customers.csv and car-wash-sales.csv files to the S3 bucket that is configured in config.ps1. The files are saved with a prefix of the location number that is in config.ps1.

To save the file, press Ctrl + S.

To exit nano editor, press Ctrl + X.

 Command: To test the upload.ps1 script, run the following command:


.\upload.ps1
 Expected output:


started upload script 2023-12-26-22-01
Uploading sales and customer data for location 1001
S3_BUCKET_NAME = twhitlock-12345
LOCATION_NUMBER = 1001
Upload complete
 CAUTION: If your output is not similar to the expected output and contains error messages, return to the instructions for config.ps1 (Task 2), and confirm that your setting for S3_BUCKET_NAME is correct. Then reattempt running the ./upload.sh command.

 Task complete: You have successfully created upload.ps1 script.

Task 5: Schedule the scripts to run by using TaskScheduler
In this task, you schedule the backup.ps1 and upload.ps1 scripts to run every five minutes by using the Task Scheduler in Windows. You also configure the scripts to write output to files called backup.log and upload.log.

To register a task using Task Scheduler, there are 3 important Windows PowerShell commands (cmdlets) which are required: New-ScheduledTaskAction, New-ScheduledTaskTrigger, and New-ScheduledTaskPrincipal.

The New-ScheduledTaskAction cmdlet creates an object that contains the definition of a scheduled task action. A scheduled task action represents a command that a task initiates when Task Scheduler runs the task. You can use a task action definition to register a new scheduled task or update an existing task registration.

The New-ScheduledTaskTrigger cmdlet creates and returns a new scheduled task trigger object. You can use a time-based trigger or an event-based trigger to start a task. Time-based triggers include starting a task at a specific time or starting a task multiple times on a daily or weekly schedule. Event-based triggers include starting a task when the system starts up or when a user logs on to the computer. Each task can contain one or more triggers, which means there are many ways that you can start a task. If a task has multiple triggers, Task Scheduler starts the task when any of the triggers occur.

The New-ScheduledTaskPrincipal cmdlet creates an object that contains a scheduled task principal. Use a scheduled task principal to run a task under the security context of a specified account. When you use a scheduled task principal, Task Scheduler can run the task regardless of whether that account is logged on.

In this task, you configure them one by one.

 Command: To configure the action which the task will initiate, run the following commands:

$action = New-ScheduledTaskAction -Execute 'powershell' -Argument 'C:\apps\car-wash-kiosk\bin\backup.ps1 *>> C:\apps\car-wash-kiosk\logs\backup.log'

$action2 = New-ScheduledTaskAction  -Execute 'powershell' -Argument 'C:\apps\car-wash-kiosk\bin\upload.ps1 *>> C:\apps\car-wash-kiosk\logs\upload.log'
 Note: The $action initiates the backup.ps1 script whereas $action2 initiates the upload.ps1 script.

 Command: To configure the trigger which initiates the task every 5 minutes, run the following command:

$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
 Command: To configure the task principal, run the following command:

$principal = New-ScheduledTaskPrincipal -UserID "NT AUTHORITY\SYSTEM" -LogonType ServiceAccount
 Note: This creates a task as the SYSTEM user that runs automatically in the background and doesn’t depend on a user being logged in.

 Command: To register a scheduled task, run the following command:

Register-ScheduledTask -Action @($action,$action2) -Trigger $trigger -TaskName "Backup-Upload-Task" -Description "Run Backup and Upload script every 5 minutes" -Principal $principal
 Additional information: The Register-ScheduledTask cmdlet registers a scheduled task definition on a local computer. It uses the different parameters we created in earlier steps as arguments.

 Expected output:


TaskPath                                       TaskName                          State
--------                                       --------                          -----
\                                              Backup-Upload-Task                Ready
 Note: The backup.ps1 and upload.ps1 files are now scheduled to run every five minutes. For example, the files will run at 1:00, 1:05, 1:10, etc.

 Note: You can verify that the tasks are running as scheduled by viewing the log files in the log directory. You may have to wait up to 5 minutes for the log files to appear.

 Command: To check the LastRunTime and NextRunTime of the task, run the following command:

Get-ScheduledTaskInfo -TaskName Backup-Upload-Task
 Expected output:


LastRunTime        : 11/30/1999 12:00:00 AM
LastTaskResult     : 267011
NextRunTime        : 1/2/2024 7:19:19 PM
NumberOfMissedRuns : 0
TaskName           : Backup-Upload-Task
TaskPath           :
PSComputerName     :
 Command: To navigate to the log directory, run the following command:

cd C:\apps\car-wash-kiosk\logs
 Note: You can list the contents of the directory to verify that the files have been created. You can use nano to view the contents of the log files to see the results of the scripts running.

 Copy edit: Copy the following code, paste it into a text editor, and replace the DOC_EXAMPLE_BUCKET placeholder value with the name of the bucket you created in Task 1.3:

Get-S3Object -BucketName DOC_EXAMPLE_BUCKET -Prefix 1001
Copy and paste the edited command into the terminal and press Enter.
 Expected output:


ChecksumAlgorithm : {}
ETag              : "83a6e976a80b4a483da790adb6cb3366"
BucketName        : twhitlock-12345
Key               : 1001/car-wash-customers.csv
LastModified      : 12/21/2023 1:11:58 AM
Owner             : Amazon.S3.Model.Owner
RestoreStatus     :
Size              : 513
StorageClass      : STANDARD

ChecksumAlgorithm : {}
ETag              : "e903a1bf579f905d333972fe1284a116"
BucketName        : twhitlock-12345
Key               : 1001/car-wash-sales.csv
LastModified      : 12/21/2023 1:11:58 AM
Owner             : Amazon.S3.Model.Owner
RestoreStatus     :
Size              : 274
StorageClass      : STANDARD
 Task complete: You have successfully scheduled your scripts to run automatically using TaskScheduler.

Conclusion
Congratulations! You have successfully:

Navigated a Windows environment to inspect an existing application.
Created and modified folders and files for your maintenance solution.
Created PowerShell scripts to take backups and upload files to the AWS Cloud.
Scheduled the maintenance scripts to run automatically by using Task Scheduler in Windows.
Additional resources
For more information, see create-bucket.
For more information, see Task Scheduler reference
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.