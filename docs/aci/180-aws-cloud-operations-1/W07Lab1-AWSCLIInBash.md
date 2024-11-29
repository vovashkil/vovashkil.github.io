# Using the AWS Command Line Interface (AWS CLI) in Bash to Interact with AWS

## Lab Overview

In this lab, you run commands in the Linux environment running on an Amazon Elastic Compute Cloud (Amazon EC2) instance. You create and navigate through directories and files and use the AWS Command Line Interface (AWS CLI) to create Amazon Web Services (AWS) services.

Objectives
By the end of this lab, you will be able to do the following:

Review basic Linux commands.
Create and edit a comma-separated values (.csv) file with the nano text editor.
Create an Amazon Simple Storage Service (Amazon S3) bucket and upload an object using the AWS CLI.
Invoke an AWS Lambda function using the AWS CLI.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, Mac OS X, or Linux (Ubuntu, SuSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab will require 60 minutes to complete.

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
AnyCompany tasks you with creating a main directory named AnyCompany with two subdirectories in the AnyCompany directory. The first subdirectory is for sales-data, and it holds a sales-data-2023.csv file inside it. The second subdirectory is for management, and it has a schedule.csv file inside it. The following diagram depicts the directory structure AnyCompany requested.


/home/ec2-user
└── AnyCompany
    ├── management
    │   └── schedule.csv
    └── sales-data
        └── sales-data-2023.csv
After you complete the file structure, AnyCompany wants you to add data to the sales-data-2023.csv file. AnyCompany also wants you to upload the file to an Amazon S3 bucket that you create for them. AnyCompany asks for a Lambda function that returns data.

Services used in this lab
AWS CLI
The AWS CLI is a tool that you can use to interact with AWS services by using commands in your command-line shell. With minimal configuration, you can start running commands from the command prompt in your terminal program that implement functionality equivalent to that provided by the browser-based AWS Management Console.

All AWS infrastructure as a service (IaaS) administration, management, and access functions in the console are available in the AWS API and AWS CLI.

You can explore a service’s capabilities with the AWS CLI and develop shell scripts to manage your resources. In addition to the low-level, API-equivalent commands, several AWS services provide customizations for the AWS CLI. Customizations can include higher-level commands that use services to make complex APIs straightforward. Examples include the aws s3api low-level commands and the higher-level aws s3 commands.

Amazon S3
Amazon S3 is an object storage service designed to offer industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-centered applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

Lambda
Lambda is a compute service that runs your code in response to events. It automatically manages the compute resources, making it convenient to build applications that respond quickly to new information. Lambda starts running your code within milliseconds of an event, such as an image upload, in-app activity, website selection, or output from a connected device. You can also use Lambda to create new backend services where compute resources are automatically invoked based on custom requests.

Task 1: Reviewing basic Linux commands and configuring AWS credentials
In this task, you review basic Linux commands to navigate the Linux terminal and configure AWS credentials.

Task 1.1: Switching users
In this task, you change to the ec2-user from the ssm-user.

Copy the InstanceASessionURL value that is listed to the left of these instructions, and paste it into a new browser tab.

 Command: To display the current user you are assuming, run this command:


whoami
 Expected output:


ssm-user
 Command: To switch to the ec2-user, run this command:

sudo su ec2-user
Run the command that makes it possible for you to display the current user you are assuming.
 Note: You can use the whoami command here.

 Command: You have now assumed the user ec2-user. To display the path of the directory you are in, run this command:

pwd
 Expected output:


/usr/bin
 Command: To change directories to the ec2-user home directory, run this command:

cd ~
 Command: To confirm that you are in the /ec2-user directory, run this command:

pwd
 Expected output:


/home/ec2-user
Task 1.2: Creating the AWS credentials
In this task, you create the AWS credentials you need later in this lab to call AWS services using the AWS CLI.

 Command: To configure the AWS credentials, run this command:

aws configure
 WARNING: Replace the placeholder values with the specified values.

For the aws configure prompt, replace the following LabAccessKeyId, LabSecretKey, and LabRegion placeholder values with the values listed to the left of these instructions. After you enter a value, press Enter to move to the next prompt.

For Default output format [None], enter json.

AWS Access Key ID [None]: LabAccessKeyId
AWS Secret Access Key [None]: LabSecretKey
Default region name [None]: LabRegion
Default output format [None]: json
 Expected output: There is no expected output.

Task 1.3: Creating directories
In this task, you create the following directory AnyCompany and subdirectories called sales-data, and management:


/home/ec2-user
└── AnyCompany
    ├── management
    └── sales-data
 Command: To display the current directory that you are in, run this command:

pwd
 Command: In the /home/ec2-user directory, create the following directories: AnyCompany, sales-data, and management. To create these directories, run this command:

mkdir -p AnyCompany/sales-data
mkdir -p AnyCompany/management
 Expected output: There is no expected output.

 Command: To change to the AnyCompany directory, run this command:

cd AnyCompany
 Command: To list the subdirectories in the AnyCompany directory, run this command:

ls
 Expected output: You observe both the sales-data and management subdirectories.

 Congratulations! You successfully created subdirectories for AnyCompany.

Task 2: Creating and editing the .csv files with the nano text editor
In this task, you create the sales-data-2023.csv file and add data to it using the nano text editor. You create the following:


/home/ec2-user
└── AnyCompany
    ├── management
    │   └── schedule.csv
    └── sales-data
        └── sales-data-2023.csv
Task 2.1: Creating the sales-data-2023.csv file
In this task, you create the file named sales-data-2023.csv.

 Command: To change to the sales-data subdirectory, run this command:

cd sales-data
 Command: To install the nano text editor, run this command:

sudo yum install nano -y
In the sales-data subdirectory, create a file using the nano text editor. To create a file using nano, run this command:

nano sales-data-2023.csv
The command nano opens the nano text editor that is used to create or edit files.

Copy the following data, and paste it into the nano text editor:

Month,Sales
August 2023,1000.00
September 2023,2000.00
October 2023,1000.00
November 2023,3000.00
To save your changes to the file, press Ctrl + O.

To confirm the file name, press Enter.

Now that the file is saved, press Ctrl + X to exit the nano text editor.

 Command: To list the contents of the sales-data directory, run this command:


ls
 Expected output: You observe the sales-data-2023.csv.

 Command: To list the contents of the sales-data-2023.csv file, run this command:

cat sales-data-2023.csv
 Expected output: You observe the contents of the sales-data-2023.csv file.

Task 2.2: Creating the schedule.csv file
In this task, you create an empty schedule.csv file in the management subdirectory.

 Command: To confirm the current subdirectory, run this command:

pwd
You are in the /home/ec2-user/AnyCompany/sales-data subdirectory.

 Command: To change to the management subdirectory, run this command:

cd ../management
Confirm the current subdirectory that you are in and list the contents.
 Note: To do this, you can use the commands pwd to check your path and ls to list your directory.

 Command: To create the empty schedule.csv file, run this command:

touch schedule.csv
Task 2.3: Creating a text file
In this task, you create a custom .csv file in the AnyCompany directory.

 Command: To change to the AnyCompany directory, run this command:

cd ..
 Command: To write contents to a new file, run this command:

echo "This command writes what is in quotation marks into the helloworld file." > helloworld.txt
 Command: To list the contents of the helloworld.txt file, run this command:

cat helloworld.txt
 Expected output:


This command writes what is in quotation marks into the helloworld file.
Task 2.4: Moving the text file
In this task, you move the helloworld.txt file to the management subdirectory.

 Command: To move the helloworld.txt file to the management subdirectory, run this command:

mv helloworld.txt management
 Command: To list the contents of the management subdirectory, run this command:

ls management
 Expected output:


helloworld.txt schedule.csv
 Congratulations! You successfully created and moved files.

Task 3: Deleting a subdirectory
AnyCompany requests that you remove the management subdirectory and its contents from AnyCompany directory during this phase of the project. In this task, you remove the schedule.csv file and delete the management subdirectory.

Task 3.1: Deleting the management subdirectory
In this task, you delete the management subdirectory and its contents.

In the AnyCompany directory, delete the management subdirectory. To delete the subdirectory, run this command:

rmdir management
 Expected output:


rmdir: failed to remove 'management': Directory not empty
Change directories to the management subdirectory.
 Note: You can use the command cd and the name of the directory to change directories. You must first delete the contents inside the directory to delete the directory.

To remove the schedule.csv from the management subdirectory, run this command:

rm schedule.csv
To remove the helloworld.txt file from the management subdirectory, run this command.

rm helloworld.txt
 Command: To list the contents of the management subdirectory, run this command:

ls
 Expected output: You observe there is nothing in the management directory now that you removed the two files.

Change to the AnyCompany directory.
 Note: You can use the command cd and the name of the directory to change the directory. You can use the pwd command to confirm the path of the directory. For example, cd AnyCompany.

In the AnyCompany directory, delete the management subdirectory. To delete the management subdirectory, run this command:

rmdir management
 Expected output: There is no expected output.

 Command: To list the contents of the AnyCompany directory, run this command:

ls
 Expected output: You observe only the sales-data subdirectory.

 Congratulations! You successfully removed contents from a directory and removed a directory.

Task 4: Creating an S3 bucket and uploading an object
In this task, you create an S3 bucket using the AWS CLI and run an AWS CLI command to verify that the bucket is in your account. Then, you upload the sales-data.csv file to the bucket.

Task 4.1: Creating an S3 bucket
In this task, you create an S3 bucket using the AWS CLI. Then, you verify that the bucket is in your account.

 Command: To create an S3 bucket, run this command:
 WARNING: Replace DOC-EXAMPLE-BUCKET with your first initial, last name, and zip code. S3 buckets need to be globally unique.


aws s3api create-bucket --bucket DOC-EXAMPLE-BUCKET --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
For example, a user named Terry Whitlock with a zip code of 00000, would use the following:


aws s3api create-bucket --bucket twhitlock-00000 --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
 Expected example output:


{
    "Location": "http://twhitlock-00000.s3.amazonaws.com/"
}
 Command: To list the S3 buckets in your AWS account, run this command:

aws s3api list-buckets
 Expected output: The following is an example output, and your results might differ:

```
[ec2-user@ip-10-0-1-227 AnyCompany]$ aws s3api list-buckets
{
    "Buckets": [
        {
            "Name": "awslabs-resources-krxqqla59sui8d-us-east-1-166836080631",
            "CreationDate": "2023-03-01T13:11:01+00:00"
        },
        {
            "Name": "awslabs-resources-r5b3y6ojjszcap-us-east-1-166836080631",
            "CreationDate": "2023-09-26T20:46:44+00:00"
        },
        {
            "Name": "twhitlock-00000",
            "CreationDate": "2023-11-06T15:43:06+00:00"
        }
    ],
    "Owner": {
        "DisplayName": "aws-labs-accounts+prodkiku-waseCiMPiooD73B5swT1g5",
        "ID": "20d0c2ddd34a415006e8f02a6ced3207a81e42965fcdbb5fdc16704838026b5a"
    }
}
```

Task 4.2: Uploading a file to your S3 bucket
In this task, you upload the sales-data-2023.csv file to your S3 bucket by running the aws s3api put-object command. After uploading the file, you list the objects in the S3 bucket by running the aws s3api list-objects-v2 command.

 Command: To upload the sales-data-2023.csv file to your S3 bucket, run this command:
 WARNING: Replace DOC-EXAMPLE-BUCKET with your bucket name. For example, the bucket used in the following example is twhitlock-00000.


aws s3api put-object --bucket DOC-EXAMPLE-BUCKET --key AnyCompany/sales-data/sales-data-2023.csv --body sales-data/sales-data-2023.csv
 WARNING: Replace DOC-EXAMPLE-BUCKET with your bucket name. For example, the bucket used in the following example is twhitlock-00000.


aws s3api put-object --bucket twhitlock-00000 --key AnyCompany/sales-data/sales-data-2023.csv --body sales-data/sales-data-2023.csv
 Expected output:


{
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
    "ServerSideEncryption": "AES256"
}
 Command: To list the objects in the S3 bucket, run this command:
 WARNING: Replace DOC-EXAMPLE-BUCKET with your bucket name.


aws s3api list-objects-v2 --bucket DOC-EXAMPLE-BUCKET --output table
 WARNING: Replace DOC-EXAMPLE-BUCKET with your bucket name.

 Expected output:


sh-5.2$ aws s3api list-objects-v2 --bucket twhitlock-00000 --output table
--------------------------------------------------------------------------------------------------------------------------------------------
|                                                               ListObjectsV2                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------+
||                                                                Contents                                                                ||
|+-------------------------------------+---------------------------------------------+----------------------------+-------+---------------+|
||                ETag                 |                     Key                     |       LastModified         | Size  | StorageClass  ||
|+-------------------------------------+---------------------------------------------+----------------------------+-------+---------------+|
||  "d41d8cd98f00b204e9800998ecf8427e" |  AnyCompany/sales-data/sales-data-2023.csv  |  2023-11-06T16:35:04+00:00 |  0    |  STANDARD     ||
|+-------------------------------------+---------------------------------------------+----------------------------+-------+---------------+|
 Congratulations! You successfully created an S3 bucket and uploaded a file using the AWS CLI.

Task 5: Invoking a Lambda function using the AWS CLI
In this task, you create a JSON file to use as a parameter for a Lambda function invocation. You invoke the Lambda function using the AWS CLI and view the results.

Task 5.1: Creating the params.json file
In this task, you create a file in nano text editor called params.json. This file contains the parameters used by the Lambda function.

 Command: To create the params.json file using the nano text editor, run this command:

nano params.json
Copy and paste the following code into the params.json file, replacing DOC-EXAMPLE-BUCKET with your bucket values:
 WARNING: Replace DOC-EXAMPLE-BUCKET with your bucket name or it will give you an error in the following tasks.


{
    "s3bucketname": "DOC-EXAMPLE-BUCKET",
    "objectKey": "AnyCompany/sales-data/sales-data-2023.csv"
}
To save your changes to the file, press Ctrl + O.

To confirm the file name and save it, press Enter.

Now that the file is saved, press Ctrl + X to exit the nano text editor.

Task 5.2: Invoking the Lambda function
In this task, you invoke a Lambda function using the AWS CLI.

 Command: To invoke the lambda function, run this command:

aws lambda invoke --function-name SalesLambda --cli-binary-format raw-in-base64-out --payload file://params.json response.json
 Expected output:


{
    "StatusCode": 200
    "ExecutedVersion": "$LATEST",
}
 Command: To display the output of the response.json file, run this command:

cat response.json
 Expected output:


{"statusCode": 200, "body": "August 2023: 1000.00\nSeptember 2023: 2000.00\nOctober 2023: 1000.00\nNovember 2023: 3000.00\n"}
 Congratulations! You successfully invoked a Lambda function.

Conclusion
Congratulations! You have successfully done the following:

Reviewed basic Linux commands
Created and edited a .csv file with the nano text editor
Created an S3 bucket and uploaded an object using the AWS CLI
Invoked a Lambda function using the AWS CLI
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
For more information, see each of the following resources:

AWS CLI Command Reference: create-bucket
AWS CLI Command Reference: invoke
Invoke in the AWS Lambda Developer Guide