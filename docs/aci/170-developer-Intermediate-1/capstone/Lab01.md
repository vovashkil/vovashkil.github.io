# Capstone Project: Building a Customer Onboarding App - Lab 01

## Lab overview

Customer onboarding is one of the most important stages of a customer’s journey with a bank. During this stage, the bank and customers exchange significant information. This exchange involves obtaining documentation needed to meet regulatory requirements and provide relevant products and services to customers.

AnyCompany Bank has decided to develop and deploy a customer onboarding serverless application on AWS. With the proposed customer onboarding solutions on AWS, the bank can use artificial intelligence (AI), machine learning (ML), and digital tools to streamline the onboarding process. With these solutions, the bank can transform the ways that customers are onboarded and reduce friction during this essential process.

As a cloud developer at AnyCompany Bank, you have been assigned the task of building the new onboarding application on AWS. The application is named Know Your Customer (KYC).

This is the first lab of a series of labs that build the KYC application for banking services. Your goal is to build the solution over 10 labs. In each lab, you build a few components of the overall solution.

In this lab, you create an Amazon Simple Storage Service (Amazon S3) bucket to store the customers’ documents, configure the bucket policy, and create an AWS Identity and Access Management (IAM) role with specific permissions to access the S3 bucket.

This is a challenge-based lab. High-level guidance and references are provided to assist you in completing the lab tasks. Detailed solution instructions are provided in collapsible sections, which you can expand.

Objectives
By the end of this lab, you should be able to do the following:

Create an S3 bucket to store the customers’ documents.
Configure a bucket policy to deny Amazon S3 actions over HTTP (TLS is not used).
Configure an IAM role for an AWS Lambda function and set the role permissions.
Technical knowledge prerequisites
To successfully complete this lab, you should have a basic knowledge of:

Amazon S3
AWS Management Console
IAM
Icon key
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
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
In this lab, you create and configure the Document S3 bucket and Document Lambda function IAM role resources. These resources are highlighted in the following diagram.

Lab 1 architectural diagram.

Image description: The diagram depicts the KYC application architectural diagram. The diagram highlights the key resources that you need to create and configure in this lab. These two resources are the Document S3 bucket and the Document Lambda function IAM role.

Services used in this lab
Amazon S3
Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. It stores and protect any amount of data for a range of use cases, such as data lakes, websites, built-for-the-cloud applications, backups, archives, machine learning, and analytics.

IAM
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Create an S3 bucket to store the customers’ documents
In this task, you create an S3 bucket to store the customers’ application documents.

Use the AWS Management Console to create an S3 bucket in the lab region with the following settings:

The bucket name must be documentbucket-${AWS::AccountId}. For example, if your account ID is 111122223333, your bucket name would be documentbucket-111122223333.
Bucket encryption must be set to SSE-S3.
The bucket must not be public.
Do it yourself

 Hint: Here are some references to assist you in solving the issue:

Specifying server-side encryption with Amazon S3 managed keys (SSE-S3)
Blocking public access to your Amazon S3 storage
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions

At the top of the AWS Management Console, in the search bar, search for and choose S3.

On the Buckets page, choose Create bucket.

On the Create bucket page, configure the following:

For Bucket name, enter documentbucket-111122223333 after replacing 111122223333 with the value of your AccountId value that is listed to the left of these instructions.
For Block Public Access settings for this bucket, ensure that Block all public access is selected.
For Default encryption, select Server-side encryption with Amazon S3 managed keys (SSE-S3).
Accept the default values for all other settings.
Choose Create bucket.

 Task complete: You successfully created an S3 bucket to store the customers’ application documents.

Task 2: Configure a bucket policy to enforce encrypted connections
In this task, you configure a bucket policy to ensure that all connections to the bucket are encrypted using TLS.

Configure a policy on the document bucket that you created in the previous task to deny all Amazon S3 actions from any principal over HTTP (TLS is not used).
Do it yourself

 Hint: Here are some references to assist you in solving the issue:

AWS global condition context keys
What S3 bucket policy can I use to comply with the AWS Config rule s3-bucket-ssl-requests-only?
Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions

On the Buckets page, choose the link of the bucket you created in the previous task.

On the bucket page, choose the Permissions tab.

In the Bucket policy section, choose Edit.

In the Policy pane, add the following policy snippet, and then replace both INSERT_BUCKET_NAME placeholders values with the value of your document bucket name.

{
    "Version": "2012-10-17",
    "Statement": [
    {
        "Sid": "Allow SSL Requests Only",
        "Action": "s3:*",
        "Effect": "Deny",
        "Resource": [
        "arn:aws:s3:::INSERT_BUCKET_NAME",
        "arn:aws:s3:::INSERT_BUCKET_NAME/*"
        ],
        "Principal": "*",
        "Condition": {
            "Bool": {
            "aws:SecureTransport": "false"
            }
        }
    }
    ]
}
Choose Save changes.

 Task complete: You successfully configured a bucket policy to ensure that all connections to the bucket are encrypted using TLS.

Task 3: Create an IAM role and configure role permissions
Later in the project, you will configure an AWS Lambda function to process the customer’s documents. The Lambda function needs an IAM execution role with the required permissions.

In this task, you create the IAM role for the Lambda function and add Amazon S3 permissions to the role so the Lambda function can read, write, and delete objects from the document bucket that you created.

Create an IAM role with the following settings:

The role name must be DocumentLambdaRole (case sensitive).
The role can only be assumed by a Lambda function.
You must attach the Role-Boundary managed policy as a permission boundary when creating the role. Failing to do so will prevent you from creating the role. The permission boundary is used as a security feature in the lab platform and is not directly related to this lab.
The role must have the following permissions on the documentbucket-${AWS::AccountId} bucket that you created:
Read objects from the bucket.
Write objects into the bucket.
Delete objects from the bucket.
The role must follow the principle of least privilege. You must allow only the required service to assume the role and attach only the required permissions.
 Note: The role you create in this task will not be used in this lab. It will be attached to a Lambda function in a later lab in this capstone project.

Do it yourself

 Hint: Here are some references to assist you in solving the issue:

Using IAM roles
Creating a role to delegate permissions to an AWS service
Lambda execution role
Creating IAM policies
 Note: If you need to edit your policy after creating it, you must delete the old policy and then re-create a new one.

Solution

Expand the following Detailed instructions section for the full solution.

Detailed instructions
At the top of the AWS Management Console, in the search bar, search for and choose IAM.

First, create the permissions policy and then create the role*.

In the left navigation pane, in the Access management section, choose Policies.

On the Policies page, choose Create policy.

On the Specify permissions page, choose JSON.

In the Policy editor pane, add the following policy snippet, and then replace the INSERT_BUCKET_NAME placeholder value with the value of your document bucket name.


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::INSERT_BUCKET_NAME/*"
        }
    ]
}
choose Next.

On the Review and create page, in the Policy name box, enter DocumentLambdaPermissions.

Choose Create policy.

Now, create the role.

In the left navigation pane, in the Access management section, choose Roles.

Choose Create role.

On the Select trusted entity page, in the Trusted entity type section, select AWS service.

In the Use case section, on the Service or use case menu, select Lambda.

Choose Next.

On the Add permissions page, in the Permissions policies section, find and select the DocumentLambdaPermissions policy.

 Note: You can type DocumentLambdaPermissions in the search box to find the policy.

Expand the Set permissions boundary - optional section and select Use a permissions boundary to control the maximum role permissions.

Select the Role-Boundary policy.

 Note: You can type Role-Boundary in the search box to find the policy.

Choose Next.

On the Name, review, and create page, for the Role name, enter DocumentLambdaRole.

Choose Create role.

 Task complete: You successfully created the IAM role for the Lambda function and added Amazon S3 permissions to the role so the Lambda function can read, write, and delete objects from the document bucket that you created.

Conclusion
You successfully completed the following:

Created an S3 bucket to store the customers’ documents.
Configured a bucket policy to deny any Amazon S3 actions over HTTP (TLS is not used).
Configured an IAM role for an AWS Lambda function and set the role permissions.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.