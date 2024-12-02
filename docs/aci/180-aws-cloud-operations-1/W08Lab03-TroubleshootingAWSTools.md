# Troubleshooting the AWS Tools for Windows PowerShell in Windows Environments

## Lab Overview

In this lab, you troubleshoot a misconfigured Windows application environment and correct issues that you encounter.

Objectives
By the end of this lab, you will be able to do the following:

Inspect the kiosk environment to make sure that it has been set up properly.
Review the log output to troubleshoot Windows PowerShell scripts.
Implement retry logic in a Windows Windows PowerShell script using a loop to make the code more resilient.
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
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal.
 Congratulations! You have successfully completed a task.
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
The operations team at AnyCompany Car Washes contacts you about issues at a particular car wash location. They cannot find any sales or customer data files in the Amazon Simple Storage Service (Amazon S3) bucket where the files should be located. They ask you to review the car wash setup to see if you can find and fix the problem.

For reference, the following is the original scenario from Lab 5.

AnyCompany Car Washes provides automated car washes in multiple locations. Customers sign up for a Basic, Enhanced, or Extreme subscription using a kiosk that dispenses a radio-frequency identification (RFID) tag sticker. Customers place the RFID tag in the front window of their vehicle. They gain automatic access to the car washes based on the RFID tag.

Architecture diagram for car wash kiosk.

Figure: The car wash kiosk server sends customer and sales data files to the AWS Cloud. The AWS Cloud contains an Amazon Simple Storage Service (Amazon S3) bucket and an AWS Identity and Access Management (IAM) user named LabStudent. The IAM user has permissions to create and update Amazon S3.

AnyCompany Car Washes needs to automate backups and sales reporting in their kiosk system, which is Windows-based. Customer data is stored to a file (car-wash-customers.csv) with the following fields: Customer Number, First Name, Last Name, Radio-frequency identification(RFID) Tag Number, Vehicle Identification Number (VIN), Car Wash Level, and Expiration Date.

Sales Data is stored in a file (car-wash-sales.csv) with the following fields: Transaction Number, Date, Location Number, RFID Tag Number, Customer Number, and Wash Type.

The sales and customer data needs to be uploaded to the cloud every 5 minutes. Data should be backed up locally every 5 minutes to a local backup directory. Backups should be zipped to save space.

To complete this assignment, you create multiple scripts and schedule them in the Task Scheduler. With the Task Scheduler, you can automatically perform routine tasks on a chosen computer. The Task Scheduler monitors the criteria you choose, called triggers, and performs the tasks when the criteria are met.

The following are a list of Windows PowerShell scripts used in this lab:

config.ps1: This file contains settings specific to the location, including the location number and Amazon Simple Storage Service (Amazon S3) bucket name. You can source this file from your other PowerShell scripts.

backup.ps1: This script makes copies of the car-wash-customers.csv and car-wash-sales.csv files and places them in a backup directory. The script then zips the files into a file named data_backup.csv

upload.ps1: This script uploads the car-wash-customers.csv and car-wash-sales.csv files to an S3 bucket in a path under the location ID called my_bucket/1234/car-wash-customers.csv and my_bucket/1234/car-wash-sales.csv. Here, 1234 is the location ID.

Services used in this lab
AWS Tools for Windows PowerShell:
The AWS Tools for PowerShell are a set of PowerShell modules that are built on the functionality exposed by the AWS SDK for .NET. With the AWS Tools for PowerShell, you can script operations on your Amazon Web Services (AWS) resources from the PowerShell command line.

The cmdlets provide an idiomatic PowerShell experience for specifying parameters and handling results even though they are implemented using the various AWS service HTTP query APIs. For example, the cmdlets for the AWS Tools for PowerShell support PowerShell pipelining, which means you can pipe PowerShell objects in and out of the cmdlets.

The AWS Tools for PowerShell are flexible in how you can use them to handle credentials, including support for the AWS Identity and Access Management (IAM) infrastructure. You can use the tools with IAM user credentials, temporary security tokens, and IAM roles.

Amazon S3:
Amazon S3 is an object storage service designed to offer industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-centered applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

Task 1: Troubleshoot the upload.ps1 script
In this task, you correct misconfigurations related to the upload.ps1 script. You review the upload.log file to find issues with the setup.

Task 1.1: Review upload.log and verify the security credentials
In this task, you connect to the kiosk server and begin investigating what may be causing the issues that have been reported.

In the Lab Information navigation pane, copy and paste the WindowsInstanceSessionUrl into a new browser tab to connect to the kiosk server.
 WARNING: If you receive i-xxxxxxxxx is not connected message. Please wait for about 5 minutes for the instance to come online and then try again.

 Command: To change directories to the application logs directory, run the following command:

cd C:\apps\car-wash-kiosk\logs\
 Command: To verify that there is existing log output from the automation scripts, run the following command:

dir
 Expected output:


    Directory: C:\apps\car-wash-kiosk\logs


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          1/2/2024  11:19 PM           5362 .machine.log
-a----          1/2/2024  11:19 PM          28222 backup.log
-a----          1/2/2024  11:19 PM          12822 upload.log
 WARNING: Each of the scripts are scheduled to run at 5 minute intervals. If the dir command does not list any directories, wait a few minutes and retry the command.

 Command: To view the contents of the upload.log file, run the following command:

cat upload.log
 Expected output: You may notice several entries in the log file that look similar to the excerpt below. The most recent entry appears at the end of the file.


...

started upload script 2024-01-02-23-24
Uploading sales and customer data for location 1001
S3_BUCKET_NAME = customer-and-sales-bucket
LOCATION_NUMBER = 1001
Write-S3Object : No credentials specified or obtained from persisted/shell defaults.
At C:\apps\car-wash-kiosk\bin\upload.ps1:13 char:1
+ Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (Amazon.PowerShe...eS3ObjectCmdlet:WriteS3ObjectCmdlet) [Write-S3Objec
   t], InvalidOperationException
    + FullyQualifiedErrorId : InvalidOperationException,Amazon.PowerShell.Cmdlets.S3.WriteS3ObjectCmdlet

Write-S3Object : No credentials specified or obtained from persisted/shell defaults.
At C:\apps\car-wash-kiosk\bin\upload.ps1:14 char:1
+ Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (Amazon.PowerShe...eS3ObjectCmdlet:WriteS3ObjectCmdlet) [Write-S3Objec
   t], InvalidOperationException
    + FullyQualifiedErrorId : InvalidOperationException,Amazon.PowerShell.Cmdlets.S3.WriteS3ObjectCmdlet

Upload complete
 Note: You see from the output that an error is occurring when trying to write the objects to Amazon S3. The error “No credentials specified or obtained from persisted/shell defaults” indicates that no security credentials exist for running the Write-S3Object command. Verify the identity and correct the error.

 Copy edit: Copy the following command, paste it into a text editor, and replace the LAB_ACCESS_KEY_ID and LAB_SECRET_KEY placeholder values with the LabAccessKeyId and LabSecretKey values listed to the left of these instructions:

Set-AWSCredential -AccessKey LAB_ACCESS_KEY_ID -SecretKey LAB_SECRET_KEY -StoreAs MyLabProfile
Copy and paste the edited command into the terminal and press Enter.
 WARNING: Replace the placeholders with the specified values or you will not have the appropriate access to complete the lab.

 Note: This command may take up to 3 minutes to complete.

 Expected output: There is no output.

 Command: To run upload.ps1 and verify that the upload is successful, run the following command:

..\bin\upload.ps1
 Expected output:



started upload script 2024-01-03-19-47
Uploading sales and customer data for location 1001
S3_BUCKET_NAME = customer-and-sales-bucket
LOCATION_NUMBER = 1001
Write-S3Object : The specified bucket does not exist
At C:\apps\car-wash-kiosk\bin\upload.ps1:13 char:1
+ Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-S3Object], AmazonS3Exception
    + FullyQualifiedErrorId : Amazon.S3.AmazonS3Exception,Amazon.PowerShell.Cmdlets.S3.WriteS3ObjectCmdlet

Write-S3Object : The specified bucket does not exist
At C:\apps\car-wash-kiosk\bin\upload.ps1:14 char:1
+ Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-S3Object], AmazonS3Exception
    + FullyQualifiedErrorId : Amazon.S3.AmazonS3Exception,Amazon.PowerShell.Cmdlets.S3.WriteS3ObjectCmdlet
 Note: You no longer receive the error about missing credentials, but the output in the upload.log file tells you that the S3 bucket that the process is attempting to upload objects to does not exist. In the next task, you determine the appropriate S3 bucket name and update the config.ps1 file.

Task 1.2: Verify the Amazon S3 bucket name in config.ps1
In this task, you determine the correct bucket name and update the config.ps1 file to correct the error.

Return to the browser tab that has the AWS Console open.

On the AWS Management Console, in the  Search box, search for and choose S3.

In the General purpose buckets tab, find the S3 bucket with customersalesbucket in the name.

 Copy edit: Copy the S3 bucket name, paste it into notepad or another text editor, and save it to use later.

Return to the browser tab with the connection to the terminal window.

To navigate to the bin directory of the application, run the following command:


cd ..\bin
 Command: To use nano text editor to open the config.ps1 file, run the following command:

nano config.ps1
 Expected output:


$S3_BUCKET_NAME="customer-and-sales-bucket"
$LOCATION_NUMBER="1001"
Replace the customer-and-sales-bucket placeholder value with the name of the S3 bucket that you saved to your text editor earlier in this task (keep the quotes).

To save the file, press Ctrl + O.

To confirm the file is saved, press Enter

To exit the nano editor, press Ctrl + X.

 Command: To test your changes to config.ps1, run the following command:


.\upload.ps1
 Expected output:


started upload script 2024-01-03-15-11
Uploading sales and customer data for location 1001
S3_BUCKET_NAME = labstack-a3ca558b-367e-4ade-b4-customersalesbucket-o1zjekafzenu
LOCATION_NUMBER = 1001
Upload complete
Notice that the output for upload.ps1 contains no errors!

 Congratulations! You have successfully corrected the errors with upload.ps1 by fixing the bucket name in config.ps1 file.

Task 2: Troubleshoot the backup.ps1 script
In this task, you correct misconfigurations related to the backup.ps1 script. You review the backup.log file to find issues with the setup.

 Command: To change directories to the application logs directory, run the following command:

cd ..\logs
To view the contents of the backup.log file in nano, run the following command:

cat backup.log
 Expected output: You may notice several entries in the log file that look similar to the excerpt below. The most recent entry appears at the end of the file.


started backup script 2024-01-03-15-21
BACKUP_DIRECTORY = C:\apps\car-wash-kiosk\backup
BACKUP_FILE_NAME = data-backup-2024-01-03-15-21.zip
Set-Location : Cannot find path 'C:\apps\car-wash-kiosk\backup' because it does not exist.
At C:\apps\car-wash-kiosk\bin\backup.ps1:14 char:1
+ Set-Location $BACKUP_DIRECTORY
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\apps\car-wash-kiosk\backup:String) [Set-Location], ItemNotFoundExcep
   tion
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

Compress-Archive : The path 'car-wash-customers.csv' either does not exist or is not a valid file system path.
At C:\apps\car-wash-kiosk\bin\backup.ps1:15 char:1
+ Compress-Archive -Path "car-wash-customers.csv", "car-wash-sales.csv" ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (car-wash-customers.csv:String) [Compress-Archive], InvalidOperationExc
   eption
    + FullyQualifiedErrorId : ArchiveCmdletPathNotFound,Compress-Archive

Remove-Item : Cannot find path 'C:\Windows\system32\car-wash-customers.csv' because it does not exist.
At C:\apps\car-wash-kiosk\bin\backup.ps1:16 char:1
+ Remove-Item "car-wash-customers.csv", "car-wash-sales.csv"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Windows\syst...h-customers.csv:String) [Remove-Item], ItemNotFoundEx
   ception
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.RemoveItemCommand

Remove-Item : Cannot find path 'C:\Windows\system32\car-wash-sales.csv' because it does not exist.
At C:\apps\car-wash-kiosk\bin\backup.ps1:16 char:1
+ Remove-Item "car-wash-customers.csv", "car-wash-sales.csv"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Windows\system32\car-wash-sales.csv:String) [Remove-Item], ItemNotFo
   undException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.RemoveItemCommand

Backup complete
 Note: The output indicates that the Set-Location command is returning an error indicating that the backup directory does not exist. The backup directory should be located at the path c:\apps\car-wash-kiosk\backup.

 Command: To view the subdirectories of the car-wash-kiosk directory, run the following commands:

cd ..
dir
 Expected output:


    Directory: C:\apps\car-wash-kiosk


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          1/3/2024   2:46 PM                .machine
d-----          1/3/2024   2:46 PM                bin
d-----          1/3/2024   2:51 PM                data
d-----          1/3/2024   2:51 PM                logs
-a----          1/3/2024   3:31 PM           3599 backup
 Note: In the output above, notice that the backup directory does not exist. Instead, there is a file named backup. Because the backup directory does not exist, the backup.ps1 script is copying the files to a file named backup instead of copying them into the directory. In the next steps, you remove the backup file and create the backup directory.

 Command: To remove the backup directory, run the following command:

Remove-Item backup
 Command: To create the backup directory, run the following command:

mkdir backup
 Expected output:


    Directory: C:\apps\car-wash-kiosk


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          1/3/2024   3:45 PM                backup
 Command: To run the backup.ps1 script, run the following command:

cd bin
.\backup.ps1
 Expected output:


started backup script 2024-01-03-15-47
BACKUP_DIRECTORY = C:\apps\car-wash-kiosk\backup
BACKUP_FILE_NAME = data-backup-2024-01-03-15-47.zip
Backup complete
Notice that the output for backup.ps1 has no errors.

 Congratulations! You have successfully corrected the errors with backup.ps1.

Task 3: Add retry logic to the upload.ps1 script
In this task, you modify the upload.ps1 script so that it tries to upload the files to the Amazon S3 bucket 3 times before exiting.

 Command: To navigate to the bin directory, run the following command:

cd ..\bin
To clear the contents of the existing upload.ps1 file, run the following command:

Clear-Content .\upload.ps1
 Command: To use the nano editor to open upload.ps1, run the following command:

nano upload.ps1
Copy and paste the following code into the upload.ps1 file in nano.

# Import configuration from config.ps1
. C:\apps\car-wash-kiosk\bin\config.ps1

Write-Host "started upload script $(Get-Date -Format 'yyyy-MM-dd-HH-mm')"

$DATA_DIRECTORY = "C:\apps\car-wash-kiosk\data"

Write-Host "Uploading sales and customer data for location $LOCATION_NUMBER"
Write-Host "S3_BUCKET_NAME = $S3_BUCKET_NAME"
Write-Host "LOCATION_NUMBER = $LOCATION_NUMBER"



# attempt to upload the sales data to S3 with a $location prefix a maximum of 3 times
foreach($i in 1..3)
{
    # Wrap the Write-S3Object calls in a try block to catch any failed attempts to upload to S3
    # If an error is encountered, the catch block writes out the error message and waits for 5 seconds
    # befor continuing the loop
    try {
        # Upload sales data to S3 with a $location prefix
        Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car-wash-customers.csv  -File $DATA_DIRECTORY\car-wash-customers.csv -ProfileName MyLabProfile
        Write-S3Object -BucketName $S3_BUCKET_NAME -Key $LOCATION_NUMBER/car-wash-sales.csv  -File $DATA_DIRECTORY\car-wash-sales.csv -ProfileName MyLabProfile
        Write-Host "Upload complete"
        break
    }
    catch {
        Write-Host $PSItem.Exception.Message -ForegroundColor Yellow
        Write-Host "Upload Failed.  Retrying in 5 seconds."
        Start-Sleep -Seconds 5
    }
}
To save the file, press Ctrl + O.

To confirm the file is saved, press Enter

To exit the nano, press Ctrl + X.

 Command: To test the upload.ps1 script, run the following command:


.\upload.ps1
 Expected output:


started upload script 2024-01-03-16-16
Uploading sales and customer data for location 1001
S3_BUCKET_NAME = labstack-a3ca558b-367e-4ade-b4-customersalesbucket-o1zjekafzenu
LOCATION_NUMBER = 1001
Upload complete
 Congratulations! You have modified upload.ps1 to be more resilient by adding retry logic.

Conclusion
Congratulations! You have successfully:

Inspected the kiosk environment to make sure that it is set up correctly.
Reviewed the log output to troubleshoot PowerShell scripts.
Implemented retry logic in a PowerShell script using a loop to make the code more resilient.
Additional resources
For more information, see each of the following resources:

Amazon S3 and Tools for Windows PowerShell
Windows PowerShell - Register-ScheduledTask
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.