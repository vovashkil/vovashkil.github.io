# Capstone Project: Building a Customer Onboarding App - Lab 02

DynamoDB: arn:aws:dynamodb:us-east-1:867246243847:table/CustomerMetadataTable
SNS Topic: arn:aws:sns:us-east-1:867246243847:ApplicationNotifications

## Lab overview

As a cloud developer at AnyCompany Bank, you have been assigned the task of building the new onboarding application on Amazon Web Services (AWS). The application is named Know Your Customer (KYC).

This is the second lab of a series of labs that build the KYC application for banking services. Your goal is to build the solution over 10 labs. In each lab, you build a few components of the overall solution.

In this lab, you create an Amazon DynamoDB table to store customer data, create an Amazon Simple Notification Service (Amazon SNS) topic to send application notifications, and add DynamoDB and Amazon SNS permissions to the AWS Lambda function AWS Identity and Access Management (IAM) role.

This is a challenge-based lab. High-level guidance and references are provided to assist you in completing the lab tasks. Detailed solution instructions are provided in collapsible sections, which you can expand.

Objectives
By the end of this lab, you should be able to do the following:

Create and configure a DynamoDB table to store customers’ metadata.
Create an SNS topic for the application notifications and subscribe to the topic.
Configure the IAM role to allow permissions for the DynamoDB table and SNS topic.
Technical knowledge prerequisites
To successfully complete this lab, you should have a basic knowledge of:

Amazon DynamoDB
Amazon SNS
AWS Management Console
IAM
Icon key
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Hint: A hint to a question or challenge
 Note: A tip or important guidance
 Task complete: A conclusion or summary point in the lab
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
In this lab, you create and configure the resources that are highlighted in the following diagram.

Lab 2 architectural diagram.

Image description: The diagram depicts the KYC application architectural diagram. The diagram highlights the key resources that you must create and configure in this lab. These resources are the Customer DynamoDB table, the Document Lambda function IAM role, and the SNS topic.

Services used in this lab
Amazon S3
Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. It stores and protect any amount of data for a range of use cases, such as data lakes, websites, built-for-the-cloud applications, backups, archives, machine learning (ML), and analytics.

Amazon SNS
Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers). Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical access point and communication channel. Clients can subscribe to the Amazon SNS topic and receive published messages using a supported endpoint type, such as Amazon Data Firehose, Amazon SQS, AWS Lambda, HTTP, email, mobile push notifications, and mobile text messages (SMS).

DynamoDB
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database so that you don’t have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. DynamoDB also offers encryption at rest, which eliminates the operational burden and complexity involved in protecting sensitive data.

IAM
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Create and configure a DynamoDB table to store customers’ metadata
The next step in building the KYC application is to create a database storage to store the customers’ information that was uploaded by the application. In this scenario, a DynamoDB table will be used for this purpose.

In this task, you create a DynamoDB table and configure its capacity provisioning.

Use the AWS Management Console to create a DynamoDB table in the lab region to store the customer’s metadata. The DynamoDB table should have the following settings:

The table must be named as CustomerMetadataTable.
The table partition key is named APP_UUID and has a type of string.
No sort key is required for the table.
The table should use standard class.
The table capacity is provisioned with two RCUs and two WCUs.
The table capacity must scale automatically when it reaches 70% of its provisioned capacity. The capacity should not be less than 2 RCU/WCU or more than 20 RCU/WCU at any given time.
After the table is created, capture and save the table Amazon Resource Name (ARN) of the table, as you will use it in a later task in the lab.

Do it yourself

 Hints: Here are some references to assist you in solving the issue:

Getting started with DynamoDB.
Managing throughput capacity automatically with DynamoDB auto scaling.
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
At the top of the AWS Management Console, in the search bar, search for and choose DynamoDB.

Choose Create table.

On the Create table page, for the Table details section, configure the following options:

For Table name, enter CustomerMetadataTable.
For Partition key, enter APP_UUID and then select String.
In the Table settings section, select Customize settings.

In the Table class section, for Choose table class, select DynamoDB Standard.

In the Read/write capacity settings section, for Capacity mode, select Provisioned.

In the Write capacity section, configure the following:

For Auto scaling, select On.
For Minimum capacity units, enter 2.
For Maximum capacity units, enter 20.
For Target utilization (%), enter 70.
In the Read capacity section, configure the following:

For Auto scaling, select On.
For Minimum capacity units, enter 2.
For Maximum capacity units, enter 20.
For Target utilization (%), enter 70.
Accept the default values for all other settings.

Choose Create table.

After the table is created, on the Tables page, choose the link for the CustomerMetadataTable.

On the CustomerMetadataTable page, under the General information section, expand the Additional info section.

Locate and copy the table ARN and save it in your preferred note editor.

 Task complete: You successfully created a DynamoDB table and configured its capacity provisioning.

Task 2: Create an SNS topic for the application notifications and configure its subscription
Throughout the phase of submitting and verifying the customers’ documents, the solution must send notifications back to the customers.

In this task, you create an SNS topic and subscribe to it. This allows the code that you build in later labs to use the SNS topic to send notifications about the status of customers’ applications.

Use the AWS Management Console to:

Create a standard SNS topic named ApplicationNotifications in the lab region.
The topic must be encrypted using the (Default) alias/aws/sns key.
Subscribe to the topic using an email address.
Ensure that you confirm the subscription in the SNS topic.
After the topic is created, capture and save the table ARN of the topic, as you will use it in a later task in the lab.

 Note:

The topic you create will be used to send notifications in future labs.
With Amazon SNS, you normally send push notification messages directly to apps on mobile devices using the mobile push notification feature, rather than email notifications. However, for the purpose of this lab, you send the notification by subscribing to the topic using email.
Do it yourself

 Hints: Here are some references to assist you in solving the issue:

Creating an Amazon SNS topic.
Subscribing to an Amazon SNS topic.
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
At the top of the AWS Management Console, in the search bar, search for and choose Simple Notification Service.

On the Amazon Simple Notification Service page, choose Next step.

On the Create topic page, configure the following:

For Type, select Standard.
For Name, enter ApplicationNotifications.
Expand the Encryption - optional section and enable Encryption.
Accept the default values for all other settings.
Choose Create topic.

On the ApplicationNotifications page, in the Details section, locate and copy the topic ARN of the topic and save it in your preferred note editor.

In the Subscriptions section, choose Create subscription.

On the Create subscription page, configure the following:

For Protocol, select Email.
For Endpoint, enter a valid email address that you can access.
Choose Create subscription.

Check the email address inbox that you entered. You should receive an email titled AWS Notifications, indicating that you subscribed to the SNS topic. Choose the Confirm Subscription link in the email to confirm.

Return to the AWS Management Console Amazon SNS page and refresh the subscription page.

Ensure that the subscription status is changed to Confirmed.

 Task complete: You successfully created an SNS topic to send notifications about the status of customers’ applications and subscribed to it.

Task 3: Configure the IAM role to allow permissions for the DynamoDB table SNS topic
In the previous lab, you created the DocumentLambdaRole that your Lambda function assumes in a later lab. The DocumentLambdaRole is provisioned for you as part of the lab build and already has the Amazon S3 permissions that you configured previously.

In this task, you add DynamoDB and Amazon SNS permissions to the DocumentLambdaRole.

Create a new managed policy and add the following permissions to it:

Write and update items to the newly created DynamoDB table.
Publish to the newly created SNS topic.
After you create the policy, attach it to the DocumentLambdaRole.
The policy must follow the principle of least privilege.
Do it yourself

 Hint: Here are some references to assist you in solving the issue:

Creating IAM policies (console).
Amazon DynamoDB: Allows access to a specific table.
Using identity-based policies with Amazon SNS.
 Note: If you need to edit your policy after creating it, you must delete the old policy and re-create a new one.

Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
At the top of the AWS Management Console, in the search bar, search for and choose IAM.

First, create the new permissions policy and then attach it to the role.

In the left navigation pane, in the Access management section, choose Policies.

On the Policies page, choose Create policy.

On the Specify permissions page, choose JSON.

In the Policy editor pane, replace any existing policy with the following policy snippet, and then make the following changes:

Replace the INSERT_YOUR_TABLE_ARN placeholder value with the value of your DynamoDB table ARN and keep the quotes.
Replace the INSERT_YOUR_TOPIC_ARN placeholder value with the value of your SNS topic ARN and keep the quotes.

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBPermissions",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:UpdateItem"
            ],
            "Resource": "INSERT_YOUR_TABLE_ARN"
        },
        {
            "Sid": "SNSPermissions",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "INSERT_YOUR_TOPIC_ARN"
        }
    ]
}
choose Next.

In the Review and create pane, for the Policy name, enter Lab2DocumentPolicy.

Choose Create policy.

Now, attach the policy to the role.

On the Policies page, find and select the Lab2DocumentPolicy.

 Note: You can type Lab2DocumentPolicy in the search box to find the policy.

From the Actions menu, choose Attach.

On the Attach as a permissions policy page, find and select the DocumentLambdaRole.

 Note: You can type DocumentLambdaRole in the search box to find the policy.

Choose Attach policy.

 Task complete: You successfully configured the IAM role to allow permissions for the DynamoDB table SNS topic.

Conclusion
You successfully completed the following:

Created and configured a DynamoDB table to store customers’ metadata.
Created an SNS topic for the application notifications and subscribed to the topic.
Configured the IAM role to allow permissions for the DynamoDB table and SNS topic.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.