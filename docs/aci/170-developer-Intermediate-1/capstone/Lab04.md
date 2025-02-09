# Capstone Project: Building a Customer Onboarding App - Lab 04

## Lab overview

As a cloud developer at AnyCompany Bank, you have been assigned the task of building the new onboarding application on AWS. The application is named Know Your Customer (KYC).

This is the fourth lab of a series of labs that build the KYC application for banking services. Your goal is to build the solution over 10 labs. In each lab, you build a few components of the overall solution.

In this lab, you will learn how to deploy resources using AWS Serverless Application Model (AWS SAM) from the AWS SAM command line interface (CLI). These are the same resources you deployed in previous labs using the AWS Management Console. You will also learn how to parse the customer details from a comma-separated values (.csv) file and write it to an Amazon DynamoDB table.

This is a challenge-based lab. High-level guidance and references are provided to assist you in completing the lab tasks. Detailed solution instructions are provided in collapsible sections, which you can expand.

Objectives
By the end of this lab, you should be able to do the following:

Deploy resources using AWS SAM.
Configure a new AWS Lambda function, attach its permissions, and update its code using AWS SAM.
Configure an Amazon Simple Storage Service (Amazon S3) event notification for the bucket to invoke the Lambda function using AWS SAM.
Develop Python code to parse the customer details CSV file.
Develop Python code using the AWS SDK for Python (Boto3) to interact with a DynamoDB table.
Technical knowledge prerequisites
To successfully complete this lab, you should have a basic knowledge of:

Amazon DynamoDB
Amazon S3
AWS Cloud9
AWS Lambda
AWS Management Console
Python
Icon key
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Hint: A hint to a question or challenge.
 Note: A tip or important guidance.
 Task complete: A conclusion or summary point in the lab.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Lab environment
In this lab, you will create and configure the Document Lambda function and its code to parse the customer details from a .csv file and write it to a DynamoDB table. The Lambda function is highlighted in the following diagram.

Lab 4 architectural diagram.

Image description: The diagram depicts the KYC application architectural diagram. The Document Lambda function that you will build in this lab is highlighted.

Services used in this lab
AWS Cloud9
AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. AWS Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, PHP, Python, and more, so you don’t need to install files or configure your development machine to start new projects.

AWS Lambda
AWS Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code on a high availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging. With Lambda, all you need to do is supply your code in one of the language runtimes that Lambda supports.

AWS SAM
AWS SAM consists of two parts, AWS SAM templates and the AWS SAM CLI. AWS SAM templates provide a shorthand syntax, optimized for defining infrastructure as code (IaC) for serverless applications. An extension of AWS CloudFormation, you deploy AWS SAM templates directly to CloudFormation, benefiting from its extensive IaC support on AWS. The AWS SAM CLI is a developer tool that puts AWS SAM features at your fingertips. Use it to quickly create, develop, and deploy serverless applications.

AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Deploy resources using AWS SAM
In previous labs, you created resources using the AWS Management Console. Using the console is useful and simple when learning new concepts. However, as a developer, you might want to use other tools to create these resources using code. AWS provides many tools that can help you build your infrastructure as a code.

AWS Serverless Application Model is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines per resource, you can define the application you want and model it using YAML. During deployment, AWS SAM transforms and expands the AWS SAM syntax into AWS CloudFormation syntax, enabling you to build serverless applications faster.

To deploy AWS resources using AWS SAM, you build these resources as a code in a template file. Then, use the AWS SAM CLI to build and deploy the template file. This will create a CloudFormation stack that builds the resources in your AWS account.

In this task, you are provided with a template.yaml file that already has the full code to deploy most of the resources that you built in previous labs using the console. Your task is to use the AWS SAM CLI to build and deploy an AWS SAM application that will build the lab resources.

The template file contains the following resources:

S3 bucket and its policy
DynamoDB table and its scaling configuration
Amazon Simple Notification Service (Amazon SNS) topic
You will use AWS SAM to add the Lambda function DocumentLambdaFunction and its code in the next task.

Do it yourself

Open the AWS Cloud9 environment and complete the following steps:

Verify that AWS SAM is running on AWS Cloud9 environment and check its version.
Explore the AWS SAM files that are provisioned in the lab build. You should see the template.yaml file under the ~/environment directory.
Open the template.yaml file and view its contents without changing it.
From the AWS Cloud9 bash terminal, use the command sam build to build the application.
From the AWS Cloud9 bash terminal, use the command sam deploy --stack-name kyc-app --guided to deploy the application. Accept the default option for all prompts when running the command.
 Note: Here is a summary of the options used in the sam deploy command:

stack-name kyc-app represents the CloudFormation stack that will be built by AWS SAM to deploy the resources. Do not use a different name for the stack.
guided allows the AWS SAM CLI to use prompts to guide you through the deployment.
This will start deploying a CloudFormation stack that builds the resources defined in the template. It also creates a samconfig.toml file that has the deployment parameters.

Once the stack is successfully deployed, use the AWS Management Console or AWS CLI to verify that the resources are correctly deployed.

 Note: Here is a description of the files in the AWS Cloud9 home directory:

8d247914.zip: Sample compressed file, which you can upload to Amazon S3 to invoke the Lambda function
DocumentLambdaFunction folder:
app.py: Lambda Python code for the DocumentLambdaFunction
previous_lab_solutions folder:
previous_document_lambda_code.py: Python code from the previous lab
README.md: Information file for AWS Cloud9
sample_lambda_resource.yaml: Sample Lambda function resource snippet to use when adding the Lambda function
template.yaml: AWS SAM template that you use to build lab resources
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
To start the AWS Cloud9 environment, locate the Cloud9Url value listed to the left of these instructions and open it in a new browser tab.

At the top of the AWS Cloud9 work area, close the Welcome tab.

Verify the AWS SAM version and explore the template file

 Command: To verify that the AWS SAM is running on AWS Cloud9 and check its version, run the following command at the bash terminal.


sam --version
 Expected output: Your environment might be running a different minor AWS SAM version.


******************************
******* EXAMPLE OUTPUT *******
******************************

SAM CLI, version 1.116.0
In the AWS Cloud9 file explorer, expand the ~/environment directory, and then open the template.yaml file and explore its contents.

Do not make any changes to the template.yaml file at this point.

Build and deploy the application using the AWS SAM CLI

 Command: To build the application, run the following command in the AWS Cloud9 bash terminal.


sam build
 Expected output: Output has been truncated.


******************************
******* EXAMPLE OUTPUT *******
******************************

Build Succeeded
 Command: To deploy the application, run the following command in the AWS Cloud9 bash terminal.


sam deploy --guided --stack-name kyc-app
Accept all default answers for all the prompts.
 Expected output: Output has been truncated and might be slightly different.


******************************
******* EXAMPLE OUTPUT *******
******************************

Deploying with following values
        ===============================
        Stack name                   : kyc-app
        Region                       : us-west-2
        Confirm changeset            : False
        Disable rollback             : False
        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-cxecxpvtaoax
        Capabilities                 : ["CAPABILITY_IAM"]
        Parameter overrides          : {}
        Signing Profiles             : {}

Successfully created/updated stack - kyc-app in us-west-2
Verify that the Amazon S3, DynamoDB, and Amazon SNS resources are built using the AWS Management Console or AWS CLI.
 Task complete: You successfully deployed resources using AWS SAM.

Task 2: Deploy a Lambda function using AWS SAM
In the previous task, you built resources using AWS SAM. However, the template file was already provisioned for you.

In this task, you will deploy a Lambda function using AWS SAM.

To deploy a Lambda function with a Python runtime using AWS SAM, you update the following two files:

AWS SAM template file (template.yaml).
Lambda code file (app.py). This file resides in the DocumentLambdaFunction directory.
For this task, the app.py file is configured with a simple Python code that will print the invocation event to CloudWatch Logs.

However, you will update the template.yaml file to add a Lambda function to your resources.

Since this might be the first time you write a resource using an AWS SAM template, a senior member of your team provided you with a sample template for creating a Lambda function using AWS SAM. The sample is in the sample_lambda_resource.yaml file in your AWS Cloud9 home directory.

Do it yourself

In the AWS Cloud9 environment, open the sample_lambda_resource.yaml file in the ~/environment directory.

Update the values for the parameters labelled REPLACE_WITH_ as below:

The function name must be DocumentLambdaFunction.
Runtime should be Python 3.12.
The function code should point to the path where the app.py is stored. This should be a relative path from where your template.yaml is stored.
The function should assume the DocumentLambdaRole when invoked. The DocumentLambdaRoleArn value is listed to the left of these instructions.
The function should not run for more than 20 seconds.
Copy the contents of the sample_lambda_resource.yaml file and paste it at the end of the template.yaml file.

Save the template.yaml file.

Make sure that you do not change anything in the template.yaml file except adding the Lambda function resource.

Deploy the changes using the sam build and sam deploy CLI commands. You do not need to use any options for the sam deploy command.

Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
Update the “template.yaml” file

In the AWS Cloud9 file explorer, expand the ~/environment directory, and then open the sample_lambda_resource.yaml file.

In the AWS Cloud9 editor, update the values for the following parameters:

For FunctionName, enter DocumentLambdaFunction.
For Timeout, enter 20.
For CodeUri, enter DocumentLambdaFunction/ (This is the relative path to the app.py file).
For Runtime, enter python3.12.
For Role, copy and paste the DocumentLambdaRoleArn value listed to the left of these instructions.
Copy all the contents of the file and paste it at the end of the template.yaml file. Make sure that your indentation is correct. The DocumentLambdaFunction resource must be aligned with the other resources in the template. Correct any misalignment due to the copy and paste operation.

Save the template.yaml file.

Build and deploy the application using AWS SAM CLI

 Command: To build the application, run the following command in the AWS Cloud9 bash terminal.


sam build && sam deploy
 Expected output: Output has been truncated and might be slightly different.


******************************
******* EXAMPLE OUTPUT *******
******************************

Build Succeeded

Successfully created/updated stack - kyc-app in us-west-2
Once the stack is successfully deployed, use the AWS Management Console or AWS CLI to verify that the function is correctly deployed.

 Task complete: You successfully deployed a Lambda function using AWS SAM.

Task 3: Configure an Amazon S3 event notification for a bucket to invoke the Lambda function using AWS SAM
After you deployed the Lambda function using AWS SAM, you configure the Amazon S3 event notification to invoke the Lambda function. This is similar to the task you did in the previous lab using the AWS Management Console. However, this time you complete the task using AWS SAM.

Do it yourself

Modify the template.yaml file to add an Amazon S3 event notification to trigger the DocumentLambdaFunction whenever an object is created by an Amazon S3 Put event in the zipped/ prefix in the document bucket.

 Hint: Here are some hints to assist you in completing the task:

A senior member of your team provided this reference to assist you in completing the task.
The Event key that you add is a property of the Lambda function resource in the AWS SAM template.
Ensure that you maintain the correct indentation when adding the Event key under the Lambda resource in the template file.
Once you update and save the template.yaml file, use the AWS SAM CLI to build and deploy commands.

Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
In the AWS Cloud9 file explorer, expand the ~/environment directory, and then open the template.yaml file.

Add the following snippet at the end of the file. The Events key must be aligned as one of the Lambda function Properties.


Events:
  S3Event:
    Type: S3
    Properties:
      Bucket: !Ref DocumentBucket # This is the bucket resource name in the template
      Events: s3:ObjectCreated:Put
      Filter:
        S3Key:
          Rules:
          - Name: prefix
            Value: zipped/
 Note: The Event key must be aligned exactly under the Role key in the Lambda function resource. Make sure that your indentation is correct. Correct any misalignment due to the copy and paste operation.

Save the template.yaml file.

 Command: To re-deploy the application, run the following command from the AWS Cloud9 bash terminal.


sam build && sam deploy
 Expected output: Output has been truncated and might be slightly different.


******************************
******* EXAMPLE OUTPUT *******
******************************

Build Succeeded

Successfully created/updated stack - kyc-app in us-west-2
Test the Lambda function

To test the Lambda function:

Create a prefix in the document bucket named zipped (case-sensitive).

Download the sample .zip file 8d247914.zip.

Upload the zipped file into the zipped/ prefix and check CloudWatch Logs to verify that your function is invoked and printing the Amazon S3 event into CloudWatch Logs.

Expand the following Verification instructions section for the full solution.

Verification instructions
Upload the zipped file to the S3 bucket

On the Amazon S3 document bucket page, choose the Objects tab.

Choose Create folder.

For Folder name, enter zipped.

Choose Create folder.

On the Objects page, choose the zipped/ link.

On the zipped/ page, choose Upload.

On the Upload page, choose Add files and add the 8d247914.zip file that you downloaded.

Choose Upload.

Verify CloudWatch Logs

At the top of the AWS Management Console, in the search bar, search for and choose Lambda.

On the Functions page, choose DocumentLambdaFunction link.

On the DocumentLambdaFunction page, choose the Monitor tab.

Choose View CloudWatch logs.

On the /aws/lambda/DocumentLambdaFunction page, choose the link for the latest log stream.

Verify that the Lambda function was invoked and printed the invocation event into the CloudWatch Logs.

 Task complete: You successfully configured the Amazon S3 event notification to invoke the Lambda function using AWS SAM.

Task 4: Develop Python code to parse the customer details .csv file
Now that you have created the DocumentLambdaFunction and configured the Amazon S3 event notification in the previous tasks, you will update the code of the Lambda function using AWS SAM.

The code will be similar to the code you developed in the last task of the previous lab so you do not need to rewrite the code from scratch. Instead, you can get the code from one of these options:

If you wrote your own code in the previous lab, you can use a copy of your code that you saved and downloaded at the end of Lab 03 - Task 4.
Use a sample solution provided in the previous_lab_solutions/previous_document_lambda_code.py file, which you can find in the home directory of your AWS Cloud9 environment.
 Note: Throughout the remaining labs in this project, you will regularly update the code of many Lambda functions. It is strongly recommended that you familiarize yourself with AWS SAM and use it as the preferred method to update the Lambda functions’ code.

Do it yourself

Modify the code in the app.py file located under the DocumentLambdaFunction directory using a working version of your code from the last lab or the sample solution provided.

Here is a reminder of what the code should perform:

Download the compressed file object from the zipped/ prefix in the S3 bucket. Your code should know the compressed file name from the invocation event that you captured in the previous task.

Extract the compressed file into the /tmp directory in the Lambda function ephemeral storage.

Upload the three extracted files to the unzipped/ prefix in the same documentbucket-${AccountId} bucket. The unzipped files must be stored into a different prefix as they will be required later in the validation so your Lambda function can reference them for future use.

Your code should also perform the following:

Extract the app_uuid from the file name. You can save it into a variable named app_uuid.
Extract the unzipped selfie file object name in the unzipped/ prefix in the S3 bucket. The key should include the prefix. You will need to use this file from the bucket for future sections of the code. You can save it into a variable named selfie_key.
Extract the unzipped license file object name in the unzipped/ prefix in the S3 bucket. The key should include the prefix. You will need to use this file from the bucket for future sections of the code. You can save it into a variable named license_key.
Extract the local details file name in the Lambda function. You will need to use this file from the bucket for future sections of the code. You can save it into a variable named details_file.
Once you update the app.py file, save it, and then build and deploy it using the AWS SAM CLI.

 Hint:

Work with the assumption that the compressed file and individual files names and types are always correct, as they were validated by the mobile app.
Make sure that you upload the individual files to an S3 bucket prefix named unzipped.
Adhere to good practice when writing your code:
Add comments so your code is easily readable and understandable.
The DocumentLambdaFunction will perform multiple tasks that you code throughout this capstone project. Write these tasks as Python functions and pass the required I/O to and from the main program to each specific function. This also helps when you need to reuse code later.
You can also use the AWS Cloud9 terminal to monitor the Lambda function logs using the following command.

aws logs tail /aws/lambda/DocumentLambdaFunction
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
Update the Lambda function code

In the AWS Cloud9 file explorer, expand the ~/environment directory, and then open the app.py file under the DocumentLambdaFunction directory.

Replace the existing code with the following code snippet.


"Lambda function to process license, zip and selfie zip files"

import json
import os
import zipfile
import boto3

unzipped_dir = "/tmp/unzipped/"
unzipped_s3_prefix = "unzipped/"

s3 = boto3.client('s3')

def unzip_object(bucket, key):
    """Download .zip file, extract, return bucket name, object names, app_uuid,
    delete .zip file, and uploading objects to incoming"""
    zip_name = os.path.basename(key)
    zip_fullpath = f'/tmp/{zip_name}'
    s3.download_file(bucket, key, zip_fullpath)
    with zipfile.ZipFile(zip_fullpath, 'r') as zip_ref:
        zip_ref.extractall(unzipped_dir)
    os.remove(zip_fullpath)

    zipped_files = os.listdir(unzipped_dir)
    return zipped_files

def lambda_handler(event, context):
    "Main lambda handler"
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    # Unzip the object from the event
    files_list = unzip_object(bucket, key)

    # Upload files to the unzipped location
    for file in files_list:
        s3.upload_file(unzipped_dir + file, bucket, unzipped_s3_prefix + file)

    # Retrieve app_uuid, selfie_key, license_key, and details_file and save them as variables for later use
    app_uuid = os.path.basename(key).replace(".zip", "")
    selfie_key = f"{unzipped_s3_prefix}{app_uuid}_selfie.png"
    license_key = f"{unzipped_s3_prefix}{app_uuid}_license.png"
    details_file = f"{unzipped_dir}{app_uuid}_details.csv"

    # Add print to verify your solution by checking CloudWatch Logs
    # You can remove these print statements once you verified your solution
    print(f"app_uuid = {app_uuid}")
    print(f"selfie_key = {selfie_key}")
    print(f"license_key = {license_key}")
    print(f"details_file = {details_file}")
Save the app.py file.

 Command: To redeploy the application, run the following command from the AWS Cloud9 bash terminal.


sam build && sam deploy
 Expected output: Output has been truncated and might be slightly different.


******************************
******* EXAMPLE OUTPUT *******
******************************

Build Succeeded

Successfully created/updated stack - kyc-app in us-west-2
Test the function as described in the following section.

Test the Lambda function

Invoke your Lambda function by uploading the provided sample compressed file to the zipped/ prefix on the S3 bucket. You can retry uploading the file, as needed. Each upload will overwrite the existing object and create a new Lambda invocation event.

Verify that the Lambda function uploaded all three individual files to the unzipped/ prefix in the S3 bucket.

For debugging, you can use print statements in your code to verify that your code is working properly. You can view the CloudWatch Logs when the function is invoked to verify that your Lambda function code is extracting the app_uuid, selfie_key, license_key, and details_file into CloudWatch Logs.

 Task complete: You successfully updated the code of the Lambda function using AWS SAM to parse the customer details .csv file.

Task 5: Develop Python code using the AWS SDK for Python to interact with a DynamoDB table
After your code unzipped the three files (details.csv, selfie.png, and license.png), you use these files to verify your customer details. The first step is to write the customer details to the DynamoDB table.

In this task, you will modify the DocumentLambdaFunction code to read and parse the details.csv file and then writes its parsed contents to the DynamoDB table, which you created earlier CustomerMetadataTable.

You have options to update the Lambda function code using the method you prefer. However, it is strongly recommended that you complete this task and all future tasks where code update is required using AWS SAM CLI.

Do it yourself

Modify the DocumentLambdaFunction to do the following:

Read and parse the details.csv file.
Write its parsed contents to the DynamoDB table, which you created earlier CustomerMetadataTable.
Recall that the details.csv file is still saved in the Lambda function /tmp directory. So you do not need to download it from the S3 bucket.
When writing the parsed .csv contents to the DynamoDB table, you must use the app_uuid value (which you extracted in the previous task) as the DynamoDB table HASH key.
You do not need to change your previous code. You only need to add extra code to it.
 Hint: Here are some changes you need to consider to add to your code for this task:

Add the Dynamodb table Boto3 resource, as you need to use it in this task.
Add the DynamoDB table as an environment variable named TABLE using the AWS SAM template file template.yaml. For more information, refer to the Environment section in the AWS SAM documentation.
At the end of your previous code, call a new function (you can name it parse_csv_ddb) and pass to it the app_uuid and the .csv file name. The app_uuid will be used as the HASH key for the DynamoDB table.
Define in your code the parse_csv_ddb function. The function should be a simple function that will open the .csv file, read its contents using the DictReader method, and then writes the contents to the DynamoDB table.
For more information on reading and writing .csv files in Python, refer to CSV File Reading and Writing.
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
Update the Lambda function code

In the AWS Cloud9 file explorer, expand the ~/environment directory, and then open the app.py file under the DocumentLambdaFunction directory.

Replace the existing code with the following code snippet. (This snippet has the full code of previous and current tasks.)


"Lambda function to process license, zip and selfie zip files"
# Environment variables:
# TABLE = CustomerMetaDataTable

import json
import os
import csv
import zipfile
import boto3

unzipped_dir = "/tmp/unzipped/"
unzipped_s3_prefix = "unzipped/"
env_table = os.environ['TABLE']

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
ddb_table = dynamodb.Table(env_table)

def unzip_object(bucket, key):
    """Download .zip file, extract, return bucket name, object names, app_uuid,
    delete .zip file, and uploading objects to incoming"""
    zip_name = os.path.basename(key)
    zip_fullpath = f'/tmp/{zip_name}'
    s3.download_file(bucket, key, zip_fullpath)
    with zipfile.ZipFile(zip_fullpath, 'r') as zip_ref:
        zip_ref.extractall(unzipped_dir)
    os.remove(zip_fullpath)

    zipped_files = os.listdir(unzipped_dir)
    return zipped_files

def parse_csv_ddb(app_uuid, details_file):
    "Load CSV and save to dynamo"
    with open(details_file, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        details_dict = next(reader)

    ddb_table.put_item(Item={**details_dict, "APP_UUID": app_uuid})

    return details_dict

def lambda_handler(event, context):
    "Main lambda handler"
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    # Unzip the object from the event
    files_list = unzip_object(bucket, key)

    # Upload files to the unzipped location
    for file in files_list:
        s3.upload_file(unzipped_dir + file, bucket, unzipped_s3_prefix + file)

    # Retrieve app_uuid from .zip file
    app_uuid = os.path.basename(key).replace(".zip", "")
    selfie_key = f"{unzipped_s3_prefix}{app_uuid}_selfie.png"
    license_key = f"{unzipped_s3_prefix}{app_uuid}_license.png"
    details_file = f"{unzipped_dir}{app_uuid}_details.csv"

    # Save CSV to dynamo
    
    details_dict = parse_csv_ddb(app_uuid, details_file)
Save the app.py file.

Update the template.yaml code to add the environment variable for the table

In the AWS Cloud9 file explorer, expand the ~/environment directory, and then open the template.yaml file.

Add the following snippet under the Properties of the DocumentLambdaFunction resource. Environment key must be aligned as one of the Lambda function Properties. Note that you are using CloudFormation !Ref to refer to the table. This means that when you deploy the same template in a different account, the function will always get the correct table name as an environment variable.


Environment:
  Variables:
    TABLE:  !Ref CustomerDDBTable
 Note: Make sure that your indentation is correct. Correct any misalignment due to the copy and paste operation.

Save the template.yaml file.

 Command: To redeploy the application, run the following command from the AWS Cloud9 bash terminal.


sam build && sam deploy
 Expected output: Output has been truncated and might be slightly different.


******************************
******* EXAMPLE OUTPUT *******
******************************

Build Succeeded

Successfully created/updated stack - kyc-app in us-west-2
Test the function as described in the following section.

Test the Lambda function

Invoke your Lambda function by uploading the provided sample compressed file to the zipped/ prefix on the S3 bucket. You can retry uploading the file, as needed. Each upload will overwrite the existing object and create a new Lambda invocation event.

Verify that the Lambda function wrote the key-value pairs of the .csv file into the DynamoDB table using the app-uuid hash key.

Expand the following DynamoDB table verification section for detailed instructions.

DynamoDB table verification
At the top of the AWS Management Console, in the search bar, search for and choose DynamoDB.

On the Amazon DynamoDB page, in the navigation pane at the left of the page, choose Tables.

On the Tables page, choose the link for the CustomerMetadataTable table.

On the CustomerMetadataTable page, choose Explore table items.

Locate the item in the Items returned section and verify that its hash key has the correct app-uuid value.

Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: You successfully modified the DocumentLambdaFunction code to read and parse the details.csv file and then writes its parsed contents to the DynamoDB table.

Conclusion
You successfully completed the following:

Deployed resources using AWS SAM.
Configured a new Lambda function, attached its permissions, and updated its code using AWS SAM.
Configured an Amazon S3 event notification for a bucket to invoke the Lambda function using AWS SAM.
Developed Python code to parse the customer details .csv file.
Developed code using the AWS SDK for Python to interact with a DynamoDB table.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.