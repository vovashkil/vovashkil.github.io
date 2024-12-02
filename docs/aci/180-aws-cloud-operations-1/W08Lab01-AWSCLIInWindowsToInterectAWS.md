# Using the AWS CLI in Windows to Interact With AWS

## Lab overview

In this lab, you run commands in the Windows environment running on an Amazon Elastic Compute Cloud (Amazon EC2) instance. You create and navigate through directories and files and use the AWS Command Line Interface (AWS CLI) to create Amazon Web Services (AWS) services.

Objectives
By the end of this lab, you will be able to do the following:

Review basic Windows commands.
Create and edit a comma-separated values (.csv) file with Windows PowerShell commands.
Create an Amazon Simple Storage Service (Amazon S3) bucket and upload an object using the AWS CLI.
Invoke an AWS Lambda function by using the AWS CLI.
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
AnyCompany tasks you with creating a main directory named AnyCompany with two subdirectories in the AnyCompany directory. The first subdirectory is called sales-data, and it has a sales-data-2023.csv file inside it. The second subdirectory is called management, and it has a schedule.csv file in it. The following diagram is the directory structure AnyCompany requested.


C:\
└── AnyCompany
    ├── management
    │   └── schedule.csv
    └── sales-data
        └── sales-data-2023.csv
After you complete this file structure, AnyCompany requests that you add data to the sales-data-2023.csv file and upload the file to an S3 bucket that you create. AnyCompany also asks for a Lambda function that returns data.

Services used in this lab
AWS Command Line Interface
The AWS CLI is a tool that you can use to interact with AWS services by using commands in your command-line shell. With minimal configuration, you can start running commands from the command prompt in your terminal program that implement functionality equivalent to that provided by the browser-based AWS Management Console.

All AWS infrastructure as a service (IaaS) administration, management, and access functions in the console are available in the AWS API and AWS CLI.

You can explore a service’s capabilities with the AWS CLI and develop shell scripts to manage your resources. In addition to the low-level, API-equivalent commands, several AWS services provide customizations for the AWS CLI. Customizations can include higher-level commands that use services to make complex APIs straightforward. Examples include the aws s3api low-level commands and the higher-level aws s3 commands.

Amazon S3
Amazon S3 is an object storage service designed to offer industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-centered applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

Lambda
Lambda is a compute service that runs your code in response to events. It automatically manages the compute resources, making it convenient to build applications that respond quickly to new information. Lambda starts running your code within milliseconds of an event, such as an image upload, in-app activity, website selection, or output from a connected device. You can also use Lambda to create new backend services where compute resources are automatically invoked based on custom requests.

Task 1: Install the AWS CLI and configure AWS credentials
In this task, you install the AWS CLI and configure AWS credentials on Windows Powershell.

Task 1.1: Install the AWS CLI
In this task, you install the AWS CLI version 2 on the Windows instance by using Windows Powershell.

In the Lab Information navigation pane, copy the WindowsInstanceSessionUrl value, and paste it into a new web browser tab.

 Command: To display the current user that you are assuming, run this command:


whoami
 Expected output: You should notice a similar output to the following:


ec2amaz-hsoq2oc\ssm-user
 Command: To install the AWS CLI on Windows, run this command:

msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi /qn
 Expected output: There is no expected output.

 Command: To set the path for the AWS CLI, run this command:

$env:PATH += ";C:\Program Files\Amazon\AWSCLIV2\" 
 Expected output: There is no expected output.

 WARNING: AWS CLI version 2 takes up to 2 minutes to install in the background.

Task 1.2: Create the AWS credentials
In this task, you create the AWS credentials that you use later in this lab to call AWS services using the AWS CLI.

 Command: To configure the AWS credentials, run this command:

aws configure
 WARNING: Replace the placeholder values with the specified values.

For the aws configure prompt, replace the following LabAccessKeyId, LabSecretKey, and LabRegion placeholder values with the values listed in the Lab Information navigation pane. After you enter a value, press Enter to move to the next prompt:
AWS Access Key ID [None]: LabAccessKeyId
AWS Secret Access Key [None]: LabSecretKey
Default region name [None]: LabRegion
Default output format [None]: json
 Note: If you receive an error, run the command $env:PATH += ";C:\Program Files\Amazon\AWSCLIV2\" again, and then run the command aws configure.

 Expected output: There is no output.

Task 1.3: Create directories
In this task, you create a directory called AnyCompany and two subdirectories called sales-data and management. You create the following:


C:\
└── AnyCompany
    ├── management
    └── sales-data
 Note: Notice the current directory you are in by looking at the prompt. In Windows PowerShell, it displays the path for you.

 Command: You are in the C:\Windows\system32 directory. To change to the C:\ directory, run this command:

cd ..\..
 Expected output:


PS C:\>
To create the AnyCompany directory, run this command:

New-Item -Path "c:\" -Name "AnyCompany" -ItemType "directory"
 Expected output:


Directory: C:\


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         12/8/2023   4:28 PM                AnyCompany
To create the sales-data subdirectory by using Windows PowerShell aliases, run this command:

md AnyCompany\sales-data
 Expected output:


Directory: C:\AnyCompany


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         12/8/2023   4:40 PM                sales-data
 Note: In Windows PowerShell, the md command is an alias to the New-Item cmdlet.

To create the management subdirectory, run this command:

md AnyCompany\management
 Expected output:


Directory: C:\AnyCompany


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         12/8/2023   4:44 PM                management
 Command: To list the subdirectories of C:\AnyCompany, run this command:

ls AnyCompany
 Expected output:


Directory: C:\AnyCompany


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         12/8/2023   4:44 PM                management
d-----         12/8/2023   4:40 PM                sales-data
 Congratulations! You successfully created a directory and two subdirectories for AnyCompany.

Task 2: Create and edit the .csv files with PowerShell commands
In this task, you create the sales-data-2023.csv file and add data to it using Windows PowerShell commands. You create the following:


C:\
└── AnyCompany
    ├── management
    │   └── schedule.csv
    └── sales-data
        └── sales-data-2023.csv
Task 2.1: Create the sales-data-2023.csv file
In this task you create the file named sales-data-2023.csv.

 Command: To change to the sales-data subdirectory, run this command:

cd AnyCompany\sales-data
 Command: To create a file and its contents using Windows PowerShell, run this command:

New-Item -Path . -Name "sales-data-2023.csv" -ItemType "file" -Value "Month,Sales
August 2023,1000.00
September 2023,2000.00
October 2023,1000.00
November 2023,3000.00"
 Expected output:


Directory: C:\AnyCompany\sales-data


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         12/8/2023   4:51 PM             97 sales-data-2023.csv
 Command: To display the contents of the sales-data-2023.csv file, run this command:

Get-Content -Path .\sales-data-2023.csv
 Expected output:


Month,Sales
August 2023,1000.00
September 2023,2000.00
October 2023,1000.00
November 2023,3000.00
Task 2.2: Create the schedule.csv file
In this task, you create an empty schedule.csv file in the management subdirectory.

You are in the C:\AnyCompany\sales-data subdirectory.

 Command: To change to the management subdirectory, run this command:

cd ..\management
 Command: To create the empty schedule.csv file, run this command:

New-Item -Path . -Name "schedule.csv" -ItemType "file" -Value ""
 Expected output:


Directory: C:\AnyCompany\management


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         12/8/2023   5:23 PM              0 schedule.csv
Task 2.3: Create a text file
In this task, you create a custom .csv file in the AnyCompany directory.

 Command: To change to the AnyCompany directory, run this command:

cd ..
 Command: To write the contents to a new file, run this command:

New-Item -Path . -Name "helloworld.txt" -ItemType "file" -Value "This is a file that needs to be moved and eventually deleted."
 Command: To display the contents of the helloworld.txt file, run this command:

Get-Content -Path .\helloworld.txt
 Expected output:


This is a file that needs to be moved and eventually deleted.
Task 2.4: Move the text file
In this task, you move the helloworld.txt file to the management subdirectory.

 Command: To move the helloworld.txt to the management directory, run this command:

move helloworld.txt management\
 Command: To list the contents of the management subdirectory, run this command:

ls management
 Expected output:


Directory: C:\AnyCompany\management


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         12/8/2023   5:25 PM             61 helloworld.txt
-a----         12/8/2023   5:23 PM              0 schedule.csv
 Congratulations! You successfully created and moved files.

Task 3: Delete a directory
AnyCompany requests that you remove the management subdirectory and its contents from AnyCompany during this phase of the project. In this task, you remove the schedule.csv file and delete the management subdirectory.

Task 3.1: Delete the management subdirectory
In this task, you delete the subdirectory and its contents.

To delete the management subdirectory, run this command:

Remove-Item management
 Expected output:


Confirm
The item at C:\AnyCompany\management has children and the Recurse parameter was not specified. If you continue, all children will be removed with the item. Are you sure you want to continue?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): A
At the prompt, enter A for Yes to All. This deletes all the files in the subdirectory and the subdirectory itself.
 Note: Using the Remove-Item command and entering A deletes all the content in the subdirectory and the subdirectory itself.

 Command: To list the contents of the AnyCompany directory, run this command:

ls
 Expected output:


Directory: C:\AnyCompany


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         12/8/2023   4:51 PM                sales-data
 Congratulations! You successfully removed contents from a subdirectory and removed a subdirectory.

Task 4: Create an S3 bucket and upload an object
In this task, you create an S3 bucket by using the AWS CLI and run an AWS CLI command to verify that the bucket is in your account. Then, you upload the sales-data.csv file to the bucket.

Task 4.1: Create an S3 bucket
In this task, you create an S3 bucket by using the AWS CLI. Then, you verify that the bucket is in your account.

 Command: To set your S3 environment variable one time, run this command.
 WARNING: Replace DOC-EXAMPLE-BUCKET with your first initial, last name, and zip code. S3 buckets need to be globally unique.


$Env:MYBUCKET = 'DOC-EXAMPLE-BUCKET'
This sets your bucket name to the $Env:MYBUCKET variable. Use this variable every time the S3 bucket is called.

 Expected output: The following is an example output for a user named Terry Whitlock with a zip code of 00000. Your results might differ.


$Env:MYBUCKET = 'twhitlock-00000'
 Command: To create an S3 bucket, run this command:

aws s3api create-bucket --bucket $Env:MYBUCKET --create-bucket-configuration LocationConstraint=us-west-2
 Expected output: This is an example output, and your results might differ.


{
    "Location": "http://twhitlock-00000.s3.amazonaws.com/"
}
 Command: To list the S3 buckets in your AWS account, run this command:

aws s3api list-buckets
 Expected output: This is an example output, and your results might differ.


C:\AnyCompany> aws s3api list-buckets
{
    "Buckets": [
        {
            "Name": "awslabs-resources-krxqqla59sui8d-us-east-1-985905141927",
            "CreationDate": "2023-03-01T10:00:04+00:00"
        },
        {
            "Name": "awslabs-resources-r5b3y6ojjszcap-us-east-1-985905141927",
            "CreationDate": "2023-10-03T22:46:07+00:00"
        },
        {
            "Name": "twhitlock-00000",
            "CreationDate": "2023-12-11T16:58:28+00:00"
        }
    ],
    "Owner": {
        "DisplayName": "aws-labs-accounts+prodkiku-aEsRSNYqdzWPyJWDw1qn71",
        "ID": "06ad71c97264d5c86f3ee6466bcd961acee383d66bf8a28de08e768e7ea47250"
    }
}
Task 4.2: Upload a file to your S3 bucket
In this task, you upload the sales-data-2023.csv file to your S3 bucket by running the aws s3api put-object command. After uploading the file, you list the objects in the S3 bucket by running the aws s3api list-objects-v2 command.

 Command: To upload the sales-data-2023.csv file to your S3 bucket, run this command:

aws s3api put-object --bucket $Env:MYBUCKET --key AnyCompany/sales-data/sales-data-2023.csv --body sales-data/sales-data-2023.csv
 Expected output: This is an example output, and your results might differ.


{
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
    "ServerSideEncryption": "AES256"
}
 Command: To list the objects in the S3 bucket, run this command:

aws s3api list-objects-v2 --bucket $Env:MYBUCKET --output table
 Expected output:


PS C:\AnyCompany> aws s3api list-objects-v2 --bucket twhitlock-00000 --output table
-----------------------------------------------------------------
|                         ListObjectsV2                         |
+-------------------------------------------+-------------------+
|  RequestCharged                           |  None             |
+-------------------------------------------+-------------------+
||                          Contents                           ||
|+---------------+---------------------------------------------+|
||  ETag         |  "1cb70c7629fa1251b4b53f236663cfd4"         ||
||  Key          |  AnyCompany/sales-data/sales-data-2023.csv  ||
||  LastModified |  2023-12-11T16:59:03+00:00                  ||
||  Size         |  97                                         ||
||  StorageClass |  STANDARD                                   ||
|+---------------+---------------------------------------------+|
 Congratulations! You successfully created an S3 bucket and uploaded a file using the AWS CLI.

Task 5: Invoke a Lambda function using the AWS CLI
In this task, you create a json file to use as a parameter for a Lambda function invocation. You invoke the Lambda function by using the AWS CLI and view the results.

Task 5.1: Create the params.json file
In this task, you create a file called params.json. This file contains the parameters used by the Lambda function.

 Command: To create the params.json file, run this command:

New-Item -Path . -Name "params.json" -ItemType "file" -Value "{
    ""s3bucketname"": ""$Env:MYBUCKET"",
    ""objectKey"": ""AnyCompany/sales-data/sales-data-2023.csv""
}"
Task 5.2: Invoke the Lambda function
In this task, you invoke a Lambda function by using the AWS CLI.

 Command: To invoke the Lambda function, run this command:

aws lambda invoke --function-name SalesLambda --cli-binary-format raw-in-base64-out --payload file://params.json response.json
In the background, the Lambda function runs the following code:


import boto3
import csv

s3 = boto3.client('s3') 

def lambda_handler(event, context): 
    # Retrieve bucket name and object key from the event 
    bucket_name = event['s3bucketname'] 
    object_key = event['AnyCompany/sales-data/sales-data-2023.csv'] 

    try: 
        # Get the object from S3 
        response = s3.get_object(Bucket=bucket_name, Key=object_key) 

        # Read the content of the object 
        content = response['Body'].read().decode('utf-8') 

        # Process CSV, calculate sales total
        rows = content.split("\n")
        reader = csv.DictReader(rows, delimiter=',')
        total = sum([ float(r['Sales']) for r in reader ])


        # Return the content of the object 
        return { 
            'statusCode': 200, 
            'body': {
                "RowCount": len(rows),
                "SalesTotal": total
            } 
        } 
    except Exception as e: 

        # If an error occurs, return an error message 
        return { 
            'statusCode': 500, 
            'body': str(e) 
        }
The code, written in Python, counts the data and returns a sum value. The Lambda function processes this information and returns the value when you invoke the function in the next step.

 Expected output:


{
    "StatusCode": 200
    "ExecutedVersion": "$LATEST",
}
 Command: To display the output of the response.json file, run this command:

Get-Content -Path .\response.json
 Expected output:


PS C:\AnyCompany> Get-Content -Path .\response.json
{"statusCode": 200, "body": {"RowCount": 5, "SalesTotal": 7000.0}}
 Congratulations! You successfully invoked a Lambda function.

Conclusion
Congratulations! You have successfully done the following:

Reviewed basic Windows commands
Created and edited a .csv file with Windows PowerShell commands.
Created an S3 bucket and uploaded an object by using the AWS CLI.
Invoked a Lambda function by using the AWS CLI.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
For more information, see each of the following resources:

AWS CLI Command Line Reference: create-bucket
AWS CLI Command Line Reference: invoke
Invoke in the AWS Lambda Developer Guide