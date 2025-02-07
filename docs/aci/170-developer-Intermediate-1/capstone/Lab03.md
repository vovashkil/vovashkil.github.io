# Capstone Project: Building a Customer Onboarding App - Lab 03

## Lab overview

As a cloud developer at AnyCompany Bank, you have been assigned the task of building the new onboarding application on AWS. The application is named Know Your Customer (KYC).

This is the third lab of a series of labs that build the KYC application for banking services. Your goal is to build the solution over 10 labs. In each lab, you build a few components of the overall solution.

In this lab, you add new permissions to the AWS Lambda function role, get started with the AWS Cloud9 environment to develop the application code, create a Lambda function and configure its settings, and configure an Amazon Simple Storage Service (Amazon S3) event notification to invoke the Lambda function.

This is a challenge-based lab. High-level guidance and references are provided to assist you in completing the lab tasks. Detailed solution instructions are provided in collapsible sections, which you can expand.

## Objectives

By the end of this lab, you should be able to do the following:

Configure the Lambda function AWS Identity and Access Management (IAM) role to add permissions for standard Lambda logging.
Start the AWS Cloud9 instance and become familiar with the environment.
Configure a new Lambda function and attach its permissions.
Configure an Amazon S3 event notification for the bucket to trigger the Lambda function.
Develop Python code using the AWS SDK for Python (Boto3) to interact with Amazon S3.
Develop Python code to verify the customer files.
Technical knowledge prerequisites
To successfully complete this lab, you should have a basic knowledge of:

Amazon S3
AWS Cloud9
AWS Lambda
AWS Management Console
IAM
Python
Icon key
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Hint: A hint to a question or challenge.
 Learn more: Where to find more information.
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
In this lab, you create and configure the Document Lambda function and Document Lambda function IAM role resources. These resources are highlighted in the following diagram.

Lab 3 architectural diagram.

Image description: The diagram depicts the KYC application architectural diagram. The diagram highlights the key resources that you must create or configure in this lab. These two resources are the Document Lambda function and the Document Lambda function IAM role.

Services used in this lab
AWS Cloud9
AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. AWS Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, PHP, Python, and more, so you don’t need to install files or configure your development machine to start new projects.

AWS IAM
AWS Identity and Access Management is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

AWS Lambda
AWS Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code on a high availability compute infrastructure and performs the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging. With Lambda, all you need to do is supply your code in one of the language runtimes that Lambda supports.

AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

## Task 1: Configure the Lambda function IAM role permissions

AWS Lambda automatically monitors Lambda functions on your behalf, pushing logs to Amazon CloudWatch. To help you troubleshoot failures in a function, after you set up permissions, Lambda logs all requests handled by your function and automatically stores logs generated by your code through Amazon CloudWatch Logs.

You can insert logging statements into your code to help you validate that your code is working as expected. Lambda automatically integrates with CloudWatch Logs and pushes all logs from your code to a CloudWatch log group associated with a Lambda function, which is named /aws/lambda/LAMBDA_FUNCTION_NAME.

You will start developing the Lambda function code and testing it in a later task in this lab. However, to monitor the output of your Lambda function, you first must give permissions to the function to write logs to CloudWatch Logs.

In this task, you add CloudWatch Logs permissions to the Lambda function IAM role. The Lambda function IAM role is named DocumentLambdaRole. It is provisioned for you as part of the lab build and already has all the permissions that you configured previously.

Create a new IAM managed policy and add the following permissions to it:

Standard Lambda function permissions to create a log group.
Standard Lambda function permissions to create a log stream and put the log events into the stream.
After you create the policy, attach it to the DocumentLambdaRole.
The policy must follow the principle of least privilege.
Do it yourself

 Hint: Here is a reference to assist you in solving the issue:

Access to CloudWatch Logs
 Caution: When you are on the IAM > Policies > Create policy > Specify permissions page in the AWS Management Console, use the JSON policy editor instead of the Visual policy editor. The Visual policy editor may have an issue creating a resource that has a forward slash “/” in its name.

Solution

Expand the following Detailed instructions section for the full solution.

### Detailed instructions

At the top of the AWS Management Console, in the search bar, search for and choose IAM.

First, create the new permissions policy and then attach it to the role.

In the left navigation pane, in the Access management section, choose Policies.

On the Policies page, choose Create policy.

On the Specify permissions page, choose JSON.

In the Policy editor pane, replace any existing policy with the following policy snippet, and then make the following changes:

Replace the INSERT_LAB_REGION placeholders values with the value of your LabRegion listed to the left of these instructions.
Replace the INSERT_ACCOUNT_ID placeholders values with the value of your AccountId listed to the left of these instructions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:INSERT_LAB_REGION:INSERT_ACCOUNT_ID:*"
        },

        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:INSERT_LAB_REGION:INSERT_ACCOUNT_ID:log-group:/aws/lambda/DocumentLambdaFunction:*"
            ]
        }
    ]
}
```

Choose Next.

On the Review and create page, for the Policy name, enter Lab3DocumentPolicy.

Choose Create policy.

Now, attach the policy to the role.

On the Policies page, find and select the Lab3DocumentPolicy.

 Note: You can type Lab3DocumentPolicy in the search box to find the policy.

From the Actions menu, choose Attach.

On the Attach as a permissions policy page, find and select the DocumentLambdaRole.

 Note: You can type DocumentLambdaRole in the search box to find the policy.

Choose Attach policy.

 Task complete: You successfully added CloudWatch Logs permissions to the Lambda function IAM role.

Task 2: Get started with the AWS Cloud9 environment
AWS Cloud9 is an integrated development environment.

The AWS Cloud9 IDE offers a rich code-editing experience with support for several programming languages and runtime debuggers, and a built-in terminal. It contains a collection of tools that you can use to code, build, run, test, and debug software, and it helps you release software in the cloud.

You can access the AWS Cloud9 IDE through a web browser. You can configure the IDE to your preferences. For instance, you can switch color themes, bind shortcut keys, enable programming language-specific syntax coloring and code formatting, and more.

In this task, you start using the AWS Cloud9 environment provisioned in the lab.

To start the AWS Cloud9 environment, locate the Cloud9Url value listed to the left of these instructions and open it in a new browser tab.

At the top of the AWS Cloud9 work area, close the Welcome tab.

By default, the AWS Cloud9 work area top section is used as a file editor while the lower section is used as a bash terminal. The pane on the left is the file explorer. You can customize the work area as you prefer.

Navigate through the AWS Cloud9 environment.

 Learn more: For more information on AWS Cloud9 navigation, refer to Working with the AWS Cloud9 Integrated Development Environment (IDE)

Complete the following tasks:

Verify the AWS Cloud environment Python3 runtime version.
Create a new text file using the AWS Cloud9 editor. Name the file my_s3_object.txt, add some text to the file, and save it in your working directory.
Create a new Python code using the AWS Cloud9 editor. The code should upload the my_s3_object.txt file to the documentbucket-${AccountId} S3 bucket, which is provisioned during the lab build.
Use an AWS Command Line Interface (AWS CLI) command to list the objects in the documentbucket-${AccountId} S3 bucket and verify that the object was uploaded successfully.
Do it yourself

 Hint: Here is a reference to assist you in solving the issue:

Python tutorial for AWS Cloud9
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
Verify the AWS Cloud9 environment Python3 runtime version

 Command: To find the Python3 runtime version, run the following command at the AWS Cloud9 bash terminal.

```
python -V
```

 Expected output: Your environment might be running a different minor Python version.


******************************
******* EXAMPLE OUTPUT *******
******************************

Python 3.12.3
Create a new text file

In the AWS Cloud9 menu, from the File menu, choose New File.

 Note: You can also choose the + icon on the file editor tab to create a new file.

In the new file, type any text like: This is an object to test Amazon S3 upload.

From the File menu, choose Save.

You can choose where to save the file. For this task, save the file on your home directory (default).

In the Filename field, enter my_s3_object.txt, and then choose Save. The file appears in the file explorer pane to the left.

Create a Python code to upload the file to the S3 bucket

Create a new file in the AWS Cloud9 environment. You can use steps similar to the ones you followed in the preceding step to create a text file.

Copy the following Python script, paste it into the new file, and then replace the INSERT_DOCUMENT_BUCKET with your DocumentBucketName value listed to the left of these instructions (keep the quotes).

```
# Import AWS boto3 module
import boto3

# Define file_name, object_name, bucket_name, and boto3 s3 client

file_name = 'my_s3_object.txt'
object_name = 'my_s3_object.txt'

# Replace <DOCUMENT_BUCKET> with your DocumentBucketName value listed to the left of these instructions (keep the quotes)

bucket_name = 'INSERT_DOCUMENT_BUCKET' 
s3_client = boto3.client('s3')

response = s3_client.upload_file(file_name, bucket_name, object_name)
```

Save the new file as s3_upload.py.

Test the code

 Command: From the bash terminal, run the following command to run the Python code.


python s3_upload.py
 Expected output:

None, unless there is an error.

Verify the object upload using the AWS CLI

You can verify that the object was uploaded successfully by using AWS CLI to list the objects in the bucket.

 Command: To list the objects in the bucket, in the bash terminal, run the following command. Replace the INSERT_DOCUMENT_BUCKET with your DocumentBucketName listed to the left of these instructions (keep the quotes).


aws s3 ls INSERT_DOCUMENT_BUCKET
 Expected output


******************************
******* EXAMPLE OUTPUT *******
******************************

2024-05-14 05:00:35         35 my_s3_object.txt
The file should be listed with details of the date created and size in bytes.

 Task complete: You successfully started using the AWS Cloud9 environment provisioned in the lab.

Task 3: Develop a Lambda function and configure its settings
Now, it is time to start developing the first Lambda function of the solution, which is referred to as the DocumentLambdaFunction. This function is invoked when a .zip file containing the customer information, license image, and selfie image is uploaded into the Document bucket.

In this task, you create the Lambda function; configure its permissions, invocation, and code; and verify it.

The Lambda function will perform multiple actions that you develop in its code throughout multiple labs. Here is a summary of what this Lambda function will perform:

Retrieve the .zip file from the S3 bucket, unzip the file, and write the individual unzipped files to another prefix in the S3 bucket.
Write the customer application data from the .csv file to the DynamoDB table.
Send a request to Amazon Rekognition to compare the faces on the driver’s license and selfie photos.
Send a request to Amazon Textract to extract the customer information from the driver’s license image.
Compare the extracted data (name, address, date of birth) with the application data provided by the customer.
Send the driver’s license number to a third-party validation API via Amazon Simple Queue Service (Amazon SQS).
Send notifications applications to the customer using the Amazon Simple Notification Service (Amazon SNS) topic based on the response of each validation.
The Lambda function needs permissions to perform the preceding actions. These permissions are provided by the DocumentLambdaRole that you created and configured in earlier labs.

Create a Lambda function with the following settings:

The function name is DocumentLambdaFunction.
Runtime should be Python 3.12.
The function should assume the DocumentLambdaRole when invoked.
The function should not run for more than 20 seconds.
The function should be invoked whenever an object is created by an Amazon S3 Put event in the zipped/ prefix in the Document bucket.
The Python code for the Lambda function should be a simple code that writes the Amazon S3 put event, which invoked the function, into CloudWatch Logs.
Do it yourself

 Hint: Here are some references to assist you in solving the issue:

Getting started with Lambda
Enabling and configuring event notifications using the Amazon S3 console
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
Configure the Lambda function

At the top of the AWS Management Console, in the search bar, search for and choose Lambda.

On the Functions page, choose Create function.

On the Create function page, configure the following:

For Function name, enter DocumentLambdaFunction.
For Runtime, select Python3.12.
Expand Change default execution role, select Use an existing role, and then select DocumentLambdaRole from the Existing role menu.
Choose Create function.
On the DocumentLambdaFunction page, choose the Configuration tab.
In the General configuration section, choose Edit.
In the Timeout field, enter 0 for min and 20 for sec.
Choose Save.
On the DocumentLambdaFunction page, choose the Code tab.
In the Code source section, in the code pane, replace the existing code with the following code snippet.


def lambda_handler(event, context):
    print(event)
Choose Deploy.
Configure Amazon S3 event notifications

At the top of the AWS Management Console, in the search bar, search for and choose S3.

On the Buckets page, choose the link for the documentbucket-${AccountId}.

On the bucket page, choose the Properties tab.

In the Event notifications section, choose Create event notification.

On the Create event notification page, configure the following:

For Event name, enter lambda_trigger.
For Prefix-optional, enter zipped/.
In the Event type section, select Put (s3:ObjectCreated:Put). This should be the only event type you select.
For Destination, select Lambda function.
For Specify Lambda function, select Choose from your Lambda functions.
From the Lambda function menu, select DocumentLambdaFunction.
Choose Save changes.
Test the Lambda function

To test the Lambda function:

Create a prefix in the Document bucket named zipped (case sensitive).

Download the sample .zip file 8d247914.zip.

Upload the .zip file into the zipped/ prefix and check CloudWatch Logs to verify that your function is invoked and printing the Amazon S3 event into CloudWatch Logs.

Expand the following Verification instructions section for the full solution.

Verification instructions
Upload the .zip file to the S3 bucket

On the document S3 bucket page, choose the Objects tab.

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

On the DocumentLambdaFunction, page, choose the Monitor tab.

Choose View CloudWatch logs.

On the /aws/lambda/DocumentLambdaFunction page, choose the link for the latest log stream.

Verify that the Lambda function was invoked and it printed the invocation event into the CloudWatch Logs.

 Task complete: You successfully created the Lambda function; configured its permissions, invocation, and code; and verified it.

Task 4: Develop Lambda function to interact with Amazon S3 events
Now that you created the DocumentLambdaFunction in the previous task, you can start developing its code to perform its first task.

The customer onboarding process starts by the customer using a mobile app to apply as a new customer to the bank. The customer, through the mobile app, enters personal details, uploads a driver’s license ID image, and takes a selfie. The mobile app writes the customer information into a .csv file, and then generates a unique identifier, denoted as app_uuid, for each customer. Then, the mobile app archives the customer details, driver’s license ID, and selfie into a .zip file and uploads it to the zipped/ prefix in the S3 bucket.

The uploaded .zip file has the following structure (for this example, “9c123456” is the app_uuid).


├── 9c123456.zip
│   ├── 9c123456_details.csv
│   ├── 9c123456_license.png
│   ├── 9c123456_selfie.png
In this task, you start developing the first task performed by the DocumentLambdaFunction to download the .zip file from the bucket and extract its contents to start processing and validating the customer details.

Modify the DocumentLambdaFunction to do the following:

Download the .zip file object from zipped/ prefix in the S3 bucket. Your code should know the .zip file name from the invocation event that you captured in the previous task.
Extract the .zip file into the /tmp directory in the Lambda function ephemeral storage.
Upload the three extracted files to the unzipped/ prefix in the same documentbucket-${AccountId} bucket. The individual unzipped files must be stored into a different prefix, as they will be required later in the validation so your Lambda function can reference them for future use.
Your code should also perform the following:

Extract the app_uuid value from the file name. You can save it into a variable named app_uuid.
Extract the unzipped selfie file object name in the unzipped/ prefix in the S3 bucket. The key should include the prefix, as well. You will use this file from the bucket for future sections of the code. You can save it into a variable named selfie_key.
Extract the unzipped driver’s license file object name in the unzipped/ prefix in the S3 bucket. The key should include the prefix, as well. You will use this file from the bucket for future sections of the code. You can save it into a variable named license_key.
Extract the local details file name in the Lambda function. You will use this file from the bucket for future sections of the code. You can save it into a variable named details_file.
Do it yourself

 Hint: Here are some hints to assist you in solving the issue:

Work with the assumption that the .zip file, individual files names, and types are always correct as they were validated by the mobile app.
Make sure that you upload the individual files to an S3 bucket prefix named unzipped/ (case sensitive).
Try following good practice when writing your code:
Add comments so your code is readable.
The DocumentLambdaFunction will perform multiple tasks that you code throughout this capstone project. It is recommended that you write these tasks as Python functions and pass the required I/O to or from the main program to each specific function. This also helps in case you need to reuse some code later.
You can use the CloudWatch Logs Live Tail feature to view the Lambda function logs. Refer to Use Live Tail to view logs in near real time.
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
Update the Lambda function code

At the top of the AWS Management Console, in the search bar, search for and choose Lambda.

On the Functions page, choose the link for the DocumentLambdaFunction.

On the DocumentLambdaFunction page, choose the Code tab.

In the Code source section, in the code pane, replace the existing code with the following code snippet.


"Lambda function to process license, data, and selfie .zip file"

import json
import os
import zipfile
import boto3

unzipped_dir = "/tmp/unzipped/"
unzipped_s3_prefix = "unzipped/"

s3 = boto3.client('s3')

def unzip_object(bucket, key):
    """Download zip file, extract, return bucket name, object names, app_uuid,
    delete zip file, and uploading objects to incoming"""
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

    # upload files to the unzipped location
    for file in files_list:
        s3.upload_file(unzipped_dir + file, bucket, unzipped_s3_prefix + file)

    # retrieve app_uuid, selfie_key, license_key, and details_file and save them as variables for later use
    app_uuid = os.path.basename(key).replace(".zip", "")
    selfie_key = f"{unzipped_s3_prefix}{app_uuid}_selfie.png"
    license_key = f"{unzipped_s3_prefix}{app_uuid}_license.png"
    details_file = f"{unzipped_dir}{app_uuid}_details.csv"

    # Add print to verify your solution by checking CloudWatch logs
    # You can remove these print statements once you verified your solution
    print(f"app_uuid = {app_uuid}")
    print(f"selfie_key = {selfie_key}")
    print(f"license_key = {license_key}")
    print(f"details_file = {details_file}")
Choose Deploy.

Test the function as described in the following section.

Test the Lambda function

Invoke your Lambda function by uploading the provided sample .zip file to the zipped/ prefix on the S3 bucket. You can retry uploading the file, as needed. Each upload will overwrite the existing object and create a new Lambda invocation event.

Verify that the Lambda function uploaded all three individual files to the unzipped/ prefix in the S3 bucket.

For debugging, you can use print statements in your code to verify that your code is working properly. You can view the CloudWatch Logs when the function is invoked to verify that your Lambda function code is extracting the app_uuid, selfie_key, license_key, and details_file into CloudWatch Logs.

Once you validate your function, you can remove the print statements from your code.

Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: You successfully developed the first task performed by the DocumentLambdaFunction to download the .zip file from the bucket and extract it to start processing and validating the customer details.

Conclusion
You successfully completed the following:

Configured the Lambda function IAM role to add permissions for standard Lambda logging.
Started the AWS Cloud9 instance and became familiar with the environment.
Configured a new Lambda function and attach its permissions.
Configured an Amazon S3 event notification for the bucket to trigger the Lambda function.
Developed Python code using the AWS SDK for Python (Boto3) to interact with Amazon S3.
Developed Python code to verify the customer files.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.