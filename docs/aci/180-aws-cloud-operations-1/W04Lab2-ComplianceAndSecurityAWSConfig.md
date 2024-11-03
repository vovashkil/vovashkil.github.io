# Compliance and security automation with AWS Config

## Lab overview

In this lab, you learn how to set up AWS Config, view your resource inventory, create compliance rules, and remediate resources that are noncompliant. You discover how AWS Config can help you accomplish the following security governance goals:

Define security rules and compliance requirements.
Monitor infrastructure against the rules and requirements.
Detect violations.
Rapidly act on violations with automation.
Services used in this lab
AWS Config helps you streamline compliance auditing, security analysis, change management, and operational troubleshooting of your AWS resources. AWS Config continually monitors and records your AWS resource configurations and automatically evaluates the recorded configurations against your desired configuration. With AWS Config you can do the following:

Review changes in configurations.
Dive into detailed resource configuration histories.
Review relationships between AWS resources.
Determine overall compliance with your defined configurations and internal guidelines.
Objectives
By the end of this lab, you will be able to do the following:

Apply managed rules through AWS Config to selected resources.
Automate remediation based on AWS Config rules.
Use the AWS Config dashboard to monitor resource compliance.
Prerequisites
To successfully complete this lab, you should be familiar with basic navigation of the AWS Management Console and understand the purpose and features of AWS Config.

Scenario
As a cloud security administrator at AnyCompany, you need to be able to secure a growing inventory of AWS resources. You are responsible for Amazon Elastic Compute Cloud (Amazon EC2) instances that are used in application testing. You are also responsible for Amazon Simple Storage Service (Amazon S3) buckets that the company keeps important intellectual property in. You must ensure that resources stay in compliance with the company’s security policies. So, you need a solution that can rapidly conduct an inventory, check and monitor compliance, and remediate issues for the resources used by your company. Although you have manually remediated security and compliance issues in the past, you want a more automated solution going forward.

The following diagram shows the basic architecture of the lab environment:

The lab architecture diagram depicts the AWS resources that are deployed for use in the lab.

The following list details the major resources in the diagram:

Two Amazon EC2 instances in a public subnet
Three Amazon S3 buckets
Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 Expected output: A sample output that you can use to verify the output of a command or edited file
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: You must first sign out
Log out error

If you see the message, You must first log out before logging into a different AWS account:

Choose the click here link.
Close your Amazon Web Services Sign In web browser tab and return to your initial lab page.
Choose Open Console again.
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Task 1: Setting up AWS Config to manage your resources
On the AWS Management Console, in the search box, search for and choose Config.

On the AWS Config home page, choose 1-click setup.

 Note: The 1-click setup option configures AWS Config based on AWS best practices and sets the following options:

All AWS resource types are recorded.
The AWS Identity and Access Management (IAM) role used to grant permissions to monitor your resources is set to AWSServiceRoleForConfig. This is a service-linked role that provides read access to the resources across other AWS services that you might use.
An S3 bucket is created with an automatically generated name to store configuration history and configuration snapshot files.
 Additional information: For more information about first-time setup of AWS Config, see Setting Up AWS Config with the Console in the Additional resources section.

On the review page, choose Confirm.
After the setup completes, you are redirected to the AWS Config dashboard.

If the Welcome to AWS Config pop-up appears, close it to display the dashboard.

On the Dashboard page, locate the Compliance status section.

Notice that there are no Rules or Resources currently listed because no rules are in place to evaluate compliance against.

 Additional information: For more information about reviewing resources in AWS Config, see Looking Up Resources That Are Discovered by AWS Config in the Additional resources section.

Task 2: Identifying resources in the inventory to manage
In the left navigation pane, choose Resources.
 CAUTION: There are two Resources options in the navigation pane. Be sure to choose the one that is not in the Aggregators section.

 Additional information: The Aggregators section is used for multi-account or multi-Region scenarios. To learn more about data aggregation in AWS Config, see Multi-Account Multi-Region Data Aggregation in the Additional resources section.

On the Resource Inventory page, notice that there are multiple pages of resources that AWS Config is recording. The resources list varies from virtual private clouds (VPCs), subnets, and route tables to EC2 instances, S3 buckets, and many others.

For Resource type, choose AWS EC2 Instance.
With the filter applied, notice that configuration data is being recorded for two EC2 instances.

Clear the AWS EC2 Instance resource type filter.

For Resource type, search for and choose AWS S3 Bucket.

With the filter applied, notice that there are several S3 buckets listed. Identify the buckets in the list that have the specific compliance requirements you check for later in the lab.

 Note: The bucket names will match the VersionedBucket and VersionedLoggedBucket values listed to the left of these instructions as follows:

One S3 bucket with a Resource identifier that starts with versioned-bucket- followed by a random number
One S3 bucket with a Resource identifier that starts with versioned-logged-bucket- followed by a random number
There are additional buckets in your inventory that are outside the scope of this lab. For example, the config-bucket was created when you set up AWS Config and is used for recording updates and actions taken by the service.

Task 3: Creating a rule to check for EC2 instances with public access
Remember from the scenario that you have a growing number of EC2 instances that you are responsible to secure. AnyCompany uses the EC2 instances to test a groundbreaking new application that has yet to be released. Your highest priority is the security of the source code and other proprietary information. Each instance must be isolated in the cloud and cannot have a public IP address mapped to it.

In this task, you create an AWS Config rule to check all EC2 instances in your account and verify that they are compliant with the company’s security requirements.

In the left navigation pane, choose Rules.
 CAUTION: There are two Rules options in the navigation pane. Be sure to choose the one that is not in the Aggregators section.

On the Rules page, choose Add rule.

On the Specify rule type page, do the following:

In the Select rule type section, select Add AWS managed rule.
In the AWS Managed Rules section, search for and select ec2-instance-no-public-ip.
 Additional information: The ec2-instance-no-public-ip rule checks whether EC2 instances have a public IP association. The rule is NON_COMPLIANT if the publicIp field is present in the EC2 instance configuration item. The rule applies only to IPv4. For more information about AWS managed rules, see AWS Config Managed Rules and ec2-instance-no-public-ip rule in the Additional resources section.

At the bottom of the page, choose Next.

On the Configure rule page, do the following:

In the Details section, for Name, enter isolated-compute-rule.
Keep the remaining default values.
 Additional information: In the Resources section, notice that AWS EC2 Instance is the selected resource type. Also, notice the optional Resource identifier field. With AWS Config rules, you can optionally specify a single resource identifier or allow the rule to apply to all resources matching the Resource category and Resource type selections. In this example, AWS EC2 Instance was applied automatically based on the type of rules that were chosen. AWS managed rules or custom rules might be applicable to multiple resource types in some situations. For more information about rule triggers, refer to Evaluation Mode and Trigger Types for AWS Config Rules in the Additional resources section.

 Note: The default configuration for this rule is set to perform a new evaluation when any resource of the specified type—an EC2 instance in this example—is created, changed, or deleted.

At the bottom of the page, choose Next.

On the Review and create page, review the rule configurations, and then choose Save.

 Expected output: A green banner should appear at the top of the page with a message that indicates the rule has been added to your account.

Task 4: Creating rules to enforce Amazon S3 security policies
AnyCompany uses S3 buckets to store various pieces of information about their new application. Each bucket has specific security requirements based on the content stored in them as follows:

No buckets should be publicly accessible.
Feedback from application developers and testers is considered medium security data and requires versioning. The bucket that stores medium security data has a name that starts with versioned-bucket.
Application source code is classified as high security data, which requires that it be both versioned and logged. The bucket that stores high security data has a name that starts with versioned-logged-bucket.
In this task, you create AWS Config rules to check the specified S3 buckets and verify that they are compliant with the company’s security requirements.

Task 4.1: Creating a rule to check for public read access on all S3 buckets
First, create a rule to check if any buckets have public access enabled.

If you are not already on the Rules page, in the left navigation pane, choose Rules.

On the Rules page, choose Add rule.

On the Specify rule type page, do the following:

In the Select rule type section, select Add AWS managed rule.
In the AWS Managed Rules section, search for and select s3-bucket-public-read-prohibited.
 Additional information: The s3-bucket-public-read-prohibited rule checks whether your S3 buckets do not allow public read access. The rule checks the Block Public Access settings, the bucket policy, and the bucket access control list (ACL). For more information, see s3-bucket-public-read-prohibited rule in the Additional resources section.

At the bottom of the page, choose Next.

On the Configure rule page, do the following:

In the Details section, for Name, enter s3-block-public-access.
Keep the remaining default values.
In the Resources section, notice that AWS S3 Bucket is the selected resource type.
 Note: The default configuration for this rule is set to perform a new evaluation when any resource of the specified type—an S3 bucket in this example—is created, changed, or deleted. The checks are run every 24 hours.

At the bottom of the page, choose Next.

On the Review and create page, review the rule configurations, and then choose Save.

 Expected output: A green banner should appear at the top of the page with a message that indicates the rule has been added to your account.

Task 4.2: Creating a rule to check for bucket versioning on all S3 buckets
Next, create a rule to check if buckets have versioning enabled. Versioning in Amazon S3 is a means of keeping multiple variants of an object in the same bucket. You can use the S3 Versioning feature to preserve, retrieve, and restore every version of every object stored in your buckets.

On the Rules page, choose Add rule.

On the Specify rule type page:

In the Select rule type section, select Add AWS managed rule.
In the AWS Managed Rules section, search for and select s3-bucket-versioning-enabled.
 Additional information: The s3-bucket-versioning-enabled rule checks whether versioning is enabled for your S3 buckets. For more information, refer to s3-bucket-versioning-enabled rule in the Additional resources section.

At the bottom of the page, choose Next.

On the Configure rule page:

In the Details section, for Name, enter s3-bucket-versioning-on.
Keep the remaining default values.
In the Resources section, notice AWS S3 Bucket is the selected resource type.
 Note: The default configuration for this rule is set to perform a new evaluation when any resource of the specified type—a S3 bucket in this example—is created, changed, or deleted.

At the bottom of the page, choose Next.

On the Review and create page, review the rule configurations, and then choose Save.

 Expected output: A green banner should appear at the top of the page with a message that indicates the rule has been added to your account.

Task 4.3: Creating a rule to check for logging on an S3 bucket
Next, create a rule to check the specified S3 bucket and determine whether access logging is turned on. Logging provides detailed records for all requests made to a bucket after logging is enabled. Access logs are useful for many applications, such as security and access audits and troubleshooting.

On the Rules page, choose Add rule.

On the Specify rule type page, do the following:

In the Select rule type section, select Add AWS managed rule.
In the AWS Managed Rules section, search for and select s3-bucket-logging-enabled.
 Additional information: The s3-bucket-logging-enabled rule checks whether logging is enabled for your S3 buckets. For more information, refer to s3-bucket-logging-enabled rule in the Additional resources section.

At the bottom of the page, choose Next.

On the Configure rule page, do the following:

In the Details section, for Name, enter s3-bucket-logging-on.
In the Evaluation mode section, for Resource identifier - optional, copy and paste the value of VersionedLoggedBucket listed to the left of these instructions.
 Note: The previous rule you created specified that all buckets must be versioned. You are limiting this rule to apply to only the bucket that requires logging as well.
Keep the remaining default values.
In the Resources section, notice AWS S3 Bucket is the selected resource type.
 Note: The default configuration for this rule is set to perform a new evaluation when any resource of the specified type—an S3 bucket in this example—is created, changed, or deleted.

At the bottom of the page, choose Next.

On the Review and create page, review the rule configurations, and then choose Save.

 Expected output: A green banner should appear at the top of the page with a message that indicates the rule has been added to your account.

Task 5: Identifying noncompliant resources
In the left navigation pane, choose Dashboard.
On the Dashboard page, in the Compliance status section, notice there are now compliant and noncompliant rules and resources listed.

You should observe three noncompliant rules, one compliant rule, at least four noncompliant resources, and one compliant resource.

 Note: If you don’t observe any rules or resources listed, wait 2 minutes for the rules to finish processing and refresh the page.

In the Compliance status section, under Rules, choose the link for Noncompliant rule(s).
The Rules page opens. Notice that the Rules section is set to Noncompliant to filter for only those rules that have noncompliant resources. There should be three rules: isolated-compute-rule, s3-bucket-versioning-on, and s3-bucket-logging-on.

Notice that the s3-block-public-access rule is not listed because all the buckets in the account are already configured to be in compliance with this rule.

In the left navigation pane, choose Dashboard.

In the Compliance status section, under Resources, choose the link for Noncompliant resource(s).

The Resource Inventory page opens. In the Resources section, notice that Compliance is set to Noncompliant to filter for only those resources that are noncompliant with the rules you configured.

In the Resources section, for Resource identifier, choose the link for the versioned-logged-bucket resource.

At the bottom of the page, in the Rules section, observe the rules that have been applied to this resource.

You should notice the three rules you created to check for S3 bucket compliance are listed along with their current Compliance status. In this example, bucket versioning and logging are not enabled, causing those rules to be noncompliant. If any rule applied to a resource is noncompliant, then the resource is also listed as noncompliant.

The other resources contain similar information.

 Additional information: For more information about reviewing rule and resource compliance, refer to Viewing Configuration Compliance in the Additional resources section.

Task 6: Remediating noncompliant resources
Now that you identified resources that are not compliant with AnyCompany’s security policies, you must perform remediation to bring them into compliance.

In this task, you configure automatic remediation for the rules you created previously.

To configure automatic remediation, you associate the isolated-compute-rule rule with the Automation Document AWS-TerminateEC2Instance. The AWS-TerminateEC2Instance document accepts two parameters: InstanceId and AutomationAssumeRole. The remediation is configured to retrieve the InstanceID from the noncompliant resource, and AutomationAssumeRole is configured with a role that has been created for you.

Task 6.1: Turning on automatic remediation for the EC2 instance rule
In the left navigation pane, choose Dashboard.

In the Compliance status section, under Rules, choose the link for Noncompliant rule(s).

On the Rules page, select isolated-compute-rule.

For Actions , choose Manage remediation.

On the Edit: Remediation action page, do the following:

In the Select remediation method section, select Automatic remediation.
In the Remediation action details section, search for and select AWS-TerminateEC2Instance.
 CAUTION: Be sure not to choose the AWS-TerminateEC2InstanceWithApproval option.
In the Resource ID Parameter section, choose InstanceId.
In the Parameters section, for AutomationAssumeRole, copy and paste the AutomationServiceRole value listed to the left of these instructions.
 Note: The AutomationServiceRole IAM role contains minimal permissions to allow the AWS Config service to remediate the compliance issues discovered in this lab.

At the bottom of the page, choose Save changes.
 Expected output: A green banner should appear at the top of the page with a message that indicates the isolated-compute-rule rule has been updated.

Task 6.2: Turning on automatic remediation for the S3 bucket versioning rule
In the left navigation pane, choose Rules.
On the Rules page, notice there are now two compliant rules and two noncompliant rules.

 Note: If there are no compliant rules listed, wait 1–2 minutes and refresh the page. Remediation steps can take a few minutes to complete.

Select s3-bucket-versioning-on.

For Actions , choose Manage remediation.

On the Edit: Remediation action page, do the following:

 Note: If any of the fields are pre-populated, such as Remediation action details, refresh the page to clear them. In some situations, settings from the previous remediation actions page can carry over to the next one.

In the Select remediation method section, select Automatic remediation.
In the Remediation action details section, search for and select AWS-ConfigureS3BucketVersioning.
In the Resource ID Parameter section, choose BucketName.
 Note: In the Parameters section, there are three items listed: BucketName, VersioningState, and AutomationAssumeRole. Because you selected BucketName in the Resource ID parameter section, that resource is automatically set to RESOURCE_ID and cannot be changed.

In the Parameters section, for AutomationAssumeRole, copy and paste the AutomationServiceRole value listed to the left of these instructions.
 Note: The AutomationAssumeRole field might be populated already from when you configured remediation for the EC2 instance rule.
Keep the remaining default values.
At the bottom of the page, choose Save changes.
 Expected output: A green banner should appear at the top of the page with a message that indicates the s3-bucket-versioning-on rule has been updated.

Task 6.3: Turning on automatic remediation for the S3 bucket logging rule
In the left navigation pane, choose Rules.

Select s3-bucket-logging-on.

For Actions , choose Manage remediation.

On the Edit: Remediation action page, do the following:

 Note: If any of the fields are pre-populated, such as Remediation action details, refresh the page to clear them. In some situations, settings from the previous remediation actions page can carry over to the next one.

In the Select remediation method section, select Automatic remediation.
In the Remediation action details section, search for and select AWS-ConfigureS3BucketLogging.
In the Resource ID Parameter section, choose BucketName.
In the Parameter section:
For TargetBucket, copy and paste the LogFilesBucket value listed to the left of these instructions.
For AutomationAssumeRole, copy and paste the AutomationServiceRole value listed to the left of these instructions.
 Note: The AutomationAssumeRole field might be populated already from when you configured remediation for the EC2 instance rule. You can leave the rest of the parameter fields empty because they are optional.
At the bottom of the page, choose Save changes.
 Expected output: A green banner should appear at the top of the page with a message that indicates the s3-bucket-logging-on rule has been updated.

In the left navigation pane, choose Dashboard.

In the Compliance status section, you should observe that all resources are now marked as compliant.

 Note: You might need to wait 2–3 minutes and refresh the page before remediation of all resources completes successfully.

Task 6.4: Reviewing the resource timeline
AWS Config maintains a timeline of compliance status and configuration changes for each tracked resource.

In the Compliance status section, under Resources, choose the link for Compliant resource(s).

On the Resource Inventory page, in the Resources section, choose the versioned-logged-bucket link to view its details.

In the top right of the page, choose Resource Timeline.

On the Timeline page, review the event timeline. You should find the time of day when the resource changed compliance states and when configuration changes were applied.

Task 7: Verifying resource remediation
Now that you successfully remediated all the AWS Config rules, verify that the changes you configured during remediation were applied.

First, verify that EC2 instances with public IP addresses mapped to them have been terminated.

At the top of the page, in the unified search bar, search for and choose EC2.

In the left navigation pane, choose Instances.

On the Instances page, notice that there are two instances—one named Private IP that is Running and one named Public IP, which has been Terminated. The terminated instance had a public IP address, so it was terminated when you configured automatic remediation of the EC2 instance rule.

Select Private IP.

In the details pane at the bottom of the window, in the Details tab, locate the Public IPv4 address field and verify that a public address is not assigned.

Next, verify that the S3 buckets now have the correct security measures in place.

At the top of the page, in the unified search bar, search for and choose S3.

Choose the link for the versioned-bucket.

On the bucket details page, choose the Properties tab.

In the Bucket Versioning section, verify that Bucket Versioning is Enabled.

Return to the S3 Buckets page by selecting the Buckets button, and then choose the link for the versioned-logged-bucket.

On the bucket details page, choose the Properties tab.

In the Bucket Versioning section, verify that Bucket Versioning is Enabled.

In the Server access logging section, verify that Server access logging is Enabled.

Following is another way to verify the remediation throughout AWS Systems Manager:

1. At the top of the page, in the unified search bar, search for and choose Systems Manager.

In the left navigation pane, choose Automation.

Here, you can observe the Execution ID for the automated executions that have been run with a Success status.

Conclusion
 Congratulations! You now have successfully done the following:

Applied managed rules through AWS Config to selected resources
Automated remediation based on AWS Config rules
Used the AWS Config dashboard to monitor resource compliance
Additional resources
Setting Up AWS Config with the Console
Looking Up Resources That Are Discovered by AWS Config
Multi-Account Multi-Region Data Aggregation
AWS Config Managed Rules
ec2-instance-no-public-ip rule
Evaluation Mode and Trigger Types for AWS Config Rules
s3-bucket-public-read-prohibited rule
s3-bucket-versioning-enabled rule
s3-bucket-logging-enabled rule
Viewing Configuration Compliance
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.