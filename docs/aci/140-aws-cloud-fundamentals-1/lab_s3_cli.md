Using Amazon S3 with the CLI, Hosting Static Websites, and Updating Tags with Batch Operations
© 2023 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

Note: Do not include any personal, identifying, or confidential information into the lab environment. Information entered may be visible to others.

Corrections, feedback, or other questions? Contact us at AWS Training and Certification.

Lab overview
In this lab, you use the aws s3 and aws s3api command line interface (CLI) commands to perform various tasks. You create buckets, move objects, configure a static website, and configure an Amazon Simple Storage Service (Amazon S3) Batch Operations job.

Objectives
By the end of this lab, you will be able to do the following:

Use the AWS CLI to interact with Amazon S3.
Configure an Amazon S3 bucket to host a static website.
Use Amazon S3 Batch Operations to update S3 object tags.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, macOS, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made)
 File contents: A code block that displays the contents of a script or file you need to run that has been precreated for you
 Knowledge check: An opportunity to check your knowledge and test what you have learned
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand
 Security: An opportunity to incorporate security best practices
 Refresh: A time when you might need to refresh a web browser page or list to show new information
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal
 Hint: A hint to a question or challenge
 Answer: An answer to a question or challenge
 Group effort: A time when you must work together with another student to complete a task
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
AWS Command Line Interface

The AWS Command Line Interface (AWS CLI) is an open-source tool that you can use to interact with Amazon Web Services (AWS) services by using commands in your command-line shell. With minimal configuration, you can start running commands from the command prompt in your terminal program that implement functionality equivalent to that provided by the browser-based AWS Management Console.

All AWS infrastructure as a service (IaaS) administration, management, and access functions in the console are available in the AWS API and AWS CLI. New AWS IaaS features and services provide full console functionality through the API and CLI at launch or within 180 days of launch.

The AWS CLI provides direct access to the public APIs of AWS services. You can explore a service’s capabilities with the AWS CLI, and develop shell scripts to manage your resources. In addition to the low-level, API-equivalent commands, several AWS services provide customizations for the AWS CLI. Customizations can include higher-level commands that simplify using a service with a complex API. An example of this is the aws s3api low-level commands and the higher-level aws s3 commands.

Task 1: Exploring the high-level aws s3 commands
In this task, you use the AWS CLI to perform various tasks with the aws s3 commands.

Task 1.1: Using the aws s3 commands to create an S3 bucket
Copy the InstanceASessionUrl value from the list to the left of these instructions, and paste it into a new web browser tab.
A new web browser tab opens with a console connection to the instance. The prompt looks similar to this:



sh-5.2$
 To determine which version of the AWS CLI is running, run this command:

aws --version
 Expected output:



aws-cli/2.9.19 Python/3.9.16 Linux/6.1.38-59.109.amzn2023.x86_64 source/x86_64.amzn.2023 prompt/off
 The output from the command tells which versions of the AWS CLI, Python, and Linux are being used.

With the aws s3 ls command, you can list S3 objects and common prefixes under a prefix or all S3 buckets.

 To list all the S3 buckets to which the account has access, run this command:


aws s3 ls
 Expected output: The expected output should be similar to this:



2023-02-28 03:08:58 awslabs-resources-krxqqla59sui8d-us-east-1-862268750686
With the aws s3 mb command, you can create an S3 bucket.

 To create a new S3 bucket, run the following command:

aws s3 mb s3://lab-bucket
 Expected output:



make_bucket failed: s3://test-bucket An error occurred (BucketAlreadyExists) when calling the CreateBucket operation: The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.
 CAUTION: The previous command failed because the requested name has already been used in Amazon S3. To create a bucket with a unique bucket name, append a random, six-digit number to the end of the name (for example, lab-bucket-123456).

 Copy edit: Copy the following code into a text editor and replace the XXXXXX placeholder value with the six digits that you’ve chosen.

aws s3 mb s3://lab-bucket-XXXXXX
 Copy the updated command from the text editor and run it in the CLI.
 Expected output:


make_bucket: lab-bucket-XXXXXX
 Note: This newly created bucket will be referred to in the following tasks as the lab-bucket. You must follow the same technique to replace lab-bucket-XXXXXX in the remaining code instructions with the name of the bucket that you created.

 List the contents of the lab-bucket:

aws s3 ls s3://lab-bucket-XXXXXX
 Expected output: There is no expected output because your newly created bucket should be empty.

Congratulations! You successfully used the aws s3 command to create an S3 bucket.

Task 1.2: Using aws s3 sync to upload objects to your bucket
In this task, you copy some files to the lab-bucket and use aws s3 commands to further manipulate them.

The aws s3 sync command synchronizes directories and Amazon S3 prefixes. It recursively copies new and updated files from the source directory to the destination, and only creates folders in the destination if they contain one or more files.

 To copy files from a source bucket to the lab-bucket that you created in Task 1, use the aws s3 sync command:

aws s3 sync s3://us-west-2-tcprod/courses/SPL-PW-100-CLF161/v1.0.0.prod-c7b23d73/scripts/data/ s3://lab-bucket-XXXXXX
 Expected output:



copy: s3://us-west-2-tcprod/courses/SPL-PW-100-CLF161/v1.0.0.dev-1f3bafa0/scripts/data/2023_12_transactions.csv to s3://lab-bucket-XXXXXX/2023_12_transactions.csv
copy: s3://us-west-2-tcprod/courses/SPL-PW-100-CLF161/v1.0.0.dev-1f3bafa0/scripts/data/2024_01_transactions.csv to s3://lab-bucket-XXXXXX/2024_01_transactions.csv
copy: s3://us-west-2-tcprod/courses/SPL-PW-100-CLF161/v1.0.0.dev-1f3bafa0/scripts/data/current_transactions.csv to s3://lab-bucket-XXXXXX/current_transactions.csv
copy: s3://us-west-2-tcprod/courses/SPL-PW-100-CLF161/v1.0.0.dev-1f3bafa0/scripts/data/2024_02_transactions.csv to s3://lab-bucket-XXXXXX/2024_02_transactions.csv
 List the contents of your bucket:

aws s3 ls s3://lab-bucket-XXXXXX
 Expected output:


2023-08-15 19:42:22      21995 2023_12_transactions.csv
2023-08-15 19:42:22      22002 2024_01_transactions.csv
2023-08-15 19:42:22      22204 2024_02_transactions.csv
2023-08-15 19:42:22       8609 current_transactions.csv
The aws s3 mv command moves a local file or S3 object to another location locally or in Amazon S3.

 To move a file to an archive folder in your lab-bucket, use the mv command:


aws s3 mv s3://lab-bucket-XXXXXX/2023_12_transactions.csv s3://lab-bucket-XXXXXX/archive/2023_12_transactions.csv
 Expected output:



move: s3://lab-bucket-XXXXXX/2023_12_transactions.csv to s3://lab-bucket-XXXXXX/archive/2023_12_transactions.csv
The aws s3 cp command copies a local file or S3 object to another location locally or in Amazon S3.

 To create a copy of the current_transactions.csv object named 2024_02_transactions.csv, use the cp command:

aws s3 cp s3://lab-bucket-XXXXXX/current_transactions.csv s3://lab-bucket-XXXXXX/2024_02_transactions.csv
 Expected output:


copy: s3://lab-bucket-XXXXXX/current_transactions.csv to s3://lab-bucket-XXXXXX/2024_02_transactions.csv
The aws s3 rm command deletes an S3 object.

 To delete the current_transactions.csv file from your lab-bucket, use the rm command:

aws s3 rm s3://lab-bucket-XXXXXX/current_transactions.csv
 Expected output:


delete: s3://lab-bucket/current_transactions.csv
Congratulations! You successfully used aws s3 sync to upload files to your S3 bucket and used the cp, mv, and rm commands to move files.

Task 1.3: Generating a presigned URL to grant temporary access to an S3 object
In this task, you create a presigned URL to grant temporary access to an S3 object.

The aws s3 presign command generates a presigned URL for an Amazon S3 object. This allows anyone who receives the presigned URL to retrieve the S3 object with an HTTP GET request, such as by pasting the URL into a browser window.

Open the following URL in a new browser tab. Remember to replace lab-bucket-XXXXXX with your unique bucket name from Task 1.1: https://lab-bucket-XXXXXX.s3.us-west-2.amazonaws.com/2024_01_transactions.csv
 Expected output:


<Error>
    <Code>AccessDenied</Code>
    <Message>Access Denied</Message>
    <RequestId>BXGQKSGN500714GT</RequestId>
    <HostId>+opSbjVdsiG3MiNquyyu+5tCOAqtHOZO8mpU9DpvzNqFzzFiL7bSLTlG+d9DbnExtYt+j8Fm6F8=</HostId>
</Error>
 CAUTION: You received this error because the current bucket permissions do not allow access to the file. Grant temporary access to this URL by using a presigned URL.

Return to the AWS Systems Manager - Session Manager tab in your browser.

 To create a presigned URL that expires after 15 minutes (900 seconds), run the following command:



aws s3 presign s3://lab-bucket-XXXXXX/2024_01_transactions.csv --expires-in 900
 Expected output:



https://lab-bucket-XXXXXX.s3.us-west-2.amazonaws.com/site/index.html?Amz=VGhpcyBpcyBhIHJlYWxseSBsb25nIHVybC4gIExvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0Li4uICBOb3cgSSB3aWxsIGp1c3QgdXNlIHBhcnQgb2YgdGhlIGxhYiBpbnN0cnVjdGlvbnMuICBUaGUgX2F3cyBzMyBwcmVzaWduXyBjb21tYW5kIGdlbmVyYXRlcyBhIHByZS1zaWduZWQgVVJMIGZvciBhbiBBbWF6b24gUzMgb2JqZWN0LiBUaGlzIGFsbG93cyBhbnlvbmUgd2hvIHJlY2VpdmVzIHRoZSBwcmUtc2lnbmVkIFVSTCB0byByZXRyaWV2ZSB0aGUgUzMgb2JqZWN0IHdpdGggYW4gSFRUUCBHRVQgcmVxdWVzdCwgc3VjaCBhcyBieSBwYXN0aW5nIHRoZSBVUkwgaW50byBhIGJyb3dzZXIgd2luZG93LiAgQmUgY2FyZWZ1bCBub3QgdG8gcHV0IGNyZWRlbnRpYWxzIGluIHlvdXIgc291cmNlIGNvZGUgYW5kIGNoZWNrIHRoZW0gaW50byBnaXQu
Copy the entire output from the previous command, and paste the link into a new browser tab. The file is downloaded in your browser.
Congratulations! You have successfully used the AWS CLI to create a bucket, manipulate S3 objects, and create a presigned URL to grant temporary access to an S3 object.

Task 2: Hosting a static website using Amazon S3
In this task, you use the aws s3api command to create a bucket and configure it for use as a website. This task focuses on using the low-level aws s3api command instead of using the high-level aws s3 command. The s3api commands often require different and more parameters.

Task 2.1: Creating and populating an S3 bucket for your site
In this task, you create a bucket to host your site and populate it with the site html files.

The aws s3api create-bucket command is used to create a bucket. This command is similar to the aws s3 mb command.

Return to the AWS Systems Manager - Session Manager tab in your browser.

 Use the aws s3api command to create a bucket. Following the same Copy edit procedure used in Task 1, append a random, six-digit number to the bucket name to ensure that the bucket name is unique. For the remainder of this lab, this bucket will be referred to as the site-bucket. Follow the same technique to replace site-bucket-XXXXXX in the remaining code instructions with the name of the bucket that you created. Run the updated command.



aws s3api create-bucket --bucket site-bucket-XXXXXX --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
 Expected output:


{
    "Location": "http://site-bucket-XXXXXX.s3.amazonaws.com/"
}
 Note: Notice the additional parameters that are required to create a bucket by using aws s3api create-bucket instead of using aws s3 mb. With this command, you can specify the Region in which the bucket is created.

 Note: Notice that the output of the command by default is in the JSON format. Use the --output parameter to specify a different format.

A simple website has been created for you. The files are located in a source bucket. Copy the files to your site-bucket by using the low-level aws s3api commands.

The aws s3api list-objects-v2 command returns a list of objects in the specified S3 bucket. This command is similar to the aws s3 ls command.

 To see the files used in the website, run the following command. The output is requested in a table format.


aws s3api list-objects-v2 --bucket us-west-2-tcprod --prefix courses/SPL-PW-100-CLF161/v1.0.0.prod-c7b23d73/scripts/site --output table
 Expected output:



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                                               ListObjectsV2                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
||                                                                                Contents                                                                                ||
|+--------------------------------------+---------------------------------------------------------------------------+----------------------------+-------+----------------+|
||                 ETag                 |                                    Key                                    |       LastModified         | Size  | StorageClass   ||
|+--------------------------------------+---------------------------------------------------------------------------+----------------------------+-------+----------------+|
||  "d020102cb0a5731a31ae0d4744eff3de-1"|  courses/SPL-PW-100-CLF161/v1.0.0.dev-23c48b5e/scripts/site/error.html    |  2023-08-03T15:58:58+00:00 |  360  |  STANDARD      ||
||  "a7afbccf1a42798dc8f00b2a6d24fd99-1"|  courses/SPL-PW-100-CLF161/v1.0.0.dev-23c48b5e/scripts/site/index.html    |  2023-08-03T15:58:58+00:00 |  287  |  STANDARD      ||
||  "fbff22c9cf08d8d1cc580c5790ee79ea-1"|  courses/SPL-PW-100-CLF161/v1.0.0.dev-23c48b5e/scripts/site/policy.json   |  2023-08-03T15:58:58+00:00 |  337  |  STANDARD      ||
||  "fecdd090b68600eeef7d1bbe5d3bf6ae-1"|  courses/SPL-PW-100-CLF161/v1.0.0.dev-23c48b5e/scripts/site/website.json  |  2023-08-03T15:58:58+00:00 |  121  |  STANDARD      ||
|+--------------------------------------+---------------------------------------------------------------------------+----------------------------+-------+----------------+|
 To copy the index.html file from the source bucket to your bucket, run the following command:

aws s3api copy-object --copy-source us-west-2-tcprod/courses/SPL-PW-100-CLF161/v1.0.0.prod-c7b23d73/scripts/site/index.html --key index.html --bucket site-bucket-XXXXXX
 Expected output:


{
    "ServerSideEncryption": "AES256",
    "CopyObjectResult": {
        "ETag": "\"43395bef03e2fa8c35639e24db141e03\"",
        "LastModified": "2023-08-01T22:34:52+00:00"
    }
}
 To copy the error.html file from the source bucket to your bucket, run the following command:

aws s3api copy-object --copy-source us-west-2-tcprod/courses/SPL-PW-100-CLF161/v1.0.0.prod-c7b23d73/scripts/site/error.html --key error.html --bucket site-bucket-XXXXXX
 Expected output:


{
    "ServerSideEncryption": "AES256",
    "CopyObjectResult": {
        "ETag": "\"43395bef03e2fa8c35639e24db141e03\"",
        "LastModified": "2023-08-01T22:34:52+00:00"
    }
}
 To verify the contents of your site bucket, run the list-objects-v2 command:


aws s3api list-objects-v2 --bucket site-bucket-XXXXXX --output table
 Expected output:



-------------------------------------------------------------------------------------------------------------
|                                               ListObjectsV2                                               |
+-----------------------------------------------------------------------------------------------------------+
||                                                Contents                                                 ||
|+-------------------------------------+-------------+-----------------------------+-------+---------------+|
||                ETag                 |     Key     |        LastModified         | Size  | StorageClass  ||
|+-------------------------------------+-------------+-----------------------------+-------+---------------+|
||  "453505ee472c48912951efe8164d90e9" |  error.html |  2023-08-03T16:24:53+00:00  |  360  |  STANDARD     ||
||  "43395bef03e2fa8c35639e24db141e03" |  index.html |  2023-08-03T16:24:22+00:00  |  287  |  STANDARD     ||
|+-------------------------------------+-------------+-----------------------------+-------+---------------+|
Congratulations! You have successfully created and populated an S3 bucket for your website.

Task 2.2: Turning off Block Public Access and associating a security policy with your bucket
By default, S3 Block Public Access settings are enabled to prevent inadvertent exposure of the objects in your bucket. For users to access your website, you have to turn off Block Public Access.

In this task, you turn off Block Public Access and add a bucket policy that grants public access to your bucket.

 To allow configuration of a bucket policy to grant public access to your bucket, turn off Block Public Access by running this command:


aws s3api delete-public-access-block --bucket site-bucket-XXXXXX
 Expected output: No output is expected from this command if it runs successfully.

 CAUTION: Use caution when modifying the Block Public Access settings of an S3 bucket. Make sure that you understand the consequences for your specific situation.

 To move to the ssm-user home directory, run this command:

cd ~
 To retrieve the policy.json file from the source bucket, run the following command:

aws s3api get-object --bucket us-west-2-tcprod --key courses/SPL-PW-100-CLF161/v1.0.0.prod-c7b23d73/scripts/site/policy.json policy.json
 Expected output:


{
    "AcceptRanges": "bytes",
    "LastModified": "2023-08-03T15:58:58+00:00",
    "ContentLength": 337,
    "ETag": "\"fbff22c9cf08d8d1cc580c5790ee79ea-1\"",
    "ContentType": "application/json",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}
 View the contents of the policy.json file by running the following command:


cat policy.json
 Expected output:


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket-placeholder>/*"
            ]
        }
    ]
}
 To replace the <bucket-placeholder> text in the policy.json file with your unique site-bucket name, run the following command. Remember to replace site-bucket-XXXXXX in the command with your unique bucket name.


sed -i 's/<bucket-placeholder>/site-bucket-XXXXXX/g' policy.json
 Expected output: No output is expected from this command if it runs successfully.

 To view the contents of the policy.json file to verify that the replacement happened correctly, run the following command:

cat policy.json
 Expected output:


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::site-bucket-XXXXXX/*"
            ]
        }
    ]
}
 To add a bucket policy to grant public read access to your bucket, use the aws s3api pub-bucket-policy command:

aws s3api put-bucket-policy --bucket site-bucket-XXXXXX --policy file://policy.json
 Expected output: No output is expected from this command if it runs successfully.

Congratulations! You successfully turned off Block Public Access and added a bucket policy to grant public access to your bucket.

Task 2.3: Configuring your S3 bucket for web access
In this task, you configure your S3 bucket for public access. You specify default index and error documents for your site.

 To retrieve the website.json file from the source bucket, run the following command:

aws s3api get-object --bucket us-west-2-tcprod --key courses/SPL-PW-100-CLF161/v1.0.0.prod-c7b23d73/scripts/site/website.json website.json
 Expected output:


{
    "AcceptRanges": "bytes",
    "LastModified": "2023-08-03T15:58:58+00:00",
    "ContentLength": 337,
    "ETag": "\"fbff22c9cf08d8d1cc580c5790ee79ea-1\"",
    "ContentType": "application/json",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}
 View the contents of the policy.json file by running the following command:


cat website.json
 Expected output:


{
    "IndexDocument": {
        "Suffix": "index.html"
    },
    "ErrorDocument": {
        "Key": "error.html"
    }
}
 To configure your bucket as a website, run the following command:


aws s3api put-bucket-website --bucket site-bucket-XXXXXX --website-configuration file://website.json
 Expected output: No output is expected from this command if it runs successfully.

This is the format for the web site: http://site-bucket-XXXXXX.s3-website-us-west-2.amazonaws.com.

Test the site by pasting that URL into a new browser tab.
 Expected output: The browser should open and display index.html. The page will display the words S3 Hosted Site.

Congratulations! You created a static site hosted on Amazon S3, and you used the low-level aws s3api commands.

Task 3: Using Amazon S3 Batch Operations to update S3 object tags
In this task, you use S3 Batch Operations to update the tags on the files in your website.

Task 3.1: Preparing an S3 object inventory file
In this task, you prepare an inventory file listing each of the S3 objects for which you want to update the tags.

 To retrieve the inventory.csv file from the source bucket, run the following command:

aws s3api get-object --bucket us-west-2-tcprod --key courses/SPL-PW-100-CLF161/v1.0.0.prod-c7b23d73/scripts/inventory/inventory.csv inventory.csv
 Expected output:


{
    "AcceptRanges": "bytes",
    "LastModified": "2023-08-03T15:58:58+00:00",
    "ContentLength": 49,
    "ETag": "\"587cfe7fa3a8853f2b61f28f4ed4933b-1\"",
    "ContentType": "text/csv",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}
 To view the contents of the file, run the following command:


cat inventory.csv
 Expected output:


<bucket-name>,index.html
<bucket-name>,error.html
The inventory file format requires a bucket name and a key name separated by a comma on each line.

 To update the file replacing the <bucket-name> placeholder with your site-bucket name, run the following command:

sed -i 's/<bucket-name>/site-bucket-XXXXXX/g' inventory.csv
 Expected output: There is no expected output if the command runs successfully.

 To verify the updates to the file, run the following command:


cat inventory.csv
 Expected output:


site-bucket-XXXXXX,index.html
site-bucket-XXXXXX,error.html
 Upload the inventory.csv to your site bucket by running the following command:

aws s3api put-object --bucket site-bucket-XXXXXX --key inventory.csv --body ./inventory.csv
 Expected output:


{
    "ETag": "\"afbc4d34c0978e12615bc9b1ffbf34a2\"",
    "ServerSideEncryption": "AES256"
}
 To verify that inventory.csv is in your site-bucket, use the list-objects-v2 command:


aws s3api list-objects-v2 --bucket site-bucket-XXXXXX --output table
 Expected output:


----------------------------------------------------------------------------------------------------------------
|                                                 ListObjectsV2                                                |
+--------------------------------------------------------------------------------------------------------------+
||                                                  Contents                                                  ||
|+-------------------------------------+----------------+-----------------------------+-------+---------------+|
||                ETag                 |      Key       |        LastModified         | Size  | StorageClass  ||
|+-------------------------------------+----------------+-----------------------------+-------+---------------+|
||  "453505ee472c48912951efe8164d90e9" |  error.html    |  2023-08-03T16:24:53+00:00  |  360  |  STANDARD     ||
||  "43395bef03e2fa8c35639e24db141e03" |  index.html    |  2023-08-03T16:24:22+00:00  |  287  |  STANDARD     ||
||  "afbc4d34c0978e12615bc9b1ffbf34a2" |  inventory.csv |  2023-08-03T17:20:48+00:00  |  59   |  STANDARD     ||
|+-------------------------------------+----------------+-----------------------------+-------+---------------+|
Congratulations! You successfully prepared an inventory file to use in an S3 Batch Operations job.

Task 3.2: Creating and running an S3 Batch Operations job
On the AWS Management Console, in the  Search box, search for and choose S3.

In the navigation pane on the left side of the page, choose Batch Operations.

Choose the Create job button.

On the Choose Region and manifest page, make the following selections:

AWS Region: Choose us-west-2.

Manifest format: Select CSV.

Manifest object: Enter s3://site-bucket-XXXXXX/inventory.csv.

Remember to replace the site-bucket with the unique bucket name that you created.

Leave all other selections at their defaults.

Choose Next.

On the Choose operation page, make the following selections:

In the Operation section, select Replace all object tags.

In the Replace all object tags section, add the following tags:

Key	Value - optional
Site Name	Lab Site
Publish Date	Current date in YYYY-MM-DD format (i.e. 2024-01-01)
Choose Next.

In the Completion report section, make the following selections:

Path to completion report destination: Enter s3://site-bucket-XXXXXX/report.

IAM Role: Choose LabBatchOperationRole.

Choose Next.

Choose Create job.

 Expected output: You see a message stating that you successfully created a job.

 Refresh: You might have to refresh the console to see the update.

You are on the Batch Operations page.

The job status will be Awaiting your confirmation to run.

Select the job.

Choose the Run job button.

Choose Run job.

 Expected output: Successfully received confirmation to run job ID asdfasdf.

In a few minutes, the job status will change to completed.

In the left navigation pane, choose Buckets.

Choose the name of your site-bucket.

Choose index.html.

Scroll down to tags and verify that the Site Name and Publish Date tags are present.

Congratulations! You successfully created an S3 Batch Operations job to update tags on objects in an S3 bucket.

Conclusion
 Congratulations! You have successfully done the following:

Used the AWS CLI to interact with Amazon S3
Configured an S3 bucket to host a static website
Used Amazon S3 Batch Operations to update S3 object tags
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
What is the AWS Command Line Interface
Adding and Removing Object Tags with Amazon S3 Batch Operations
AWS CLI Command Reference – s3api
AWS CLI Command Reference – s3
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.