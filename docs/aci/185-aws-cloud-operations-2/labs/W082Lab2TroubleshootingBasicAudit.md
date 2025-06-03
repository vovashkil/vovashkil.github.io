# Performing a Basic Audit of Your AWS Environment

## Auxiliary data

```text
PVC ID vpc-03e77e4129bf71093
```

## Lab overview

In this lab, you perform basic audits of core AWS resources. You use the AWS Management Console to understand how to audit the use of multiple AWS services, such as Amazon Elastic Compute Cloud, Amazon Virtual Private Cloud (Amazon VPC), Amazon IAM Identity Center, Amazon Security Groups, Amazon CloudTrail, and Amazon CloudWatch. This lab teaches you how to extend your existing auditing objectives related to organizational Governance, Asset Configuration, Logical Access Controls, Operating Systems, Databases, and Applications security configurations within AWS.

## Objectives

By the end of this lab, you will be able to do the following:

Review user permissions in AWS IAM.
Capture audit evidence using AWS IAM Policy Simulator.
Review Inbound and Outbound networking rules for Amazon EC2 Security Groups.
Review Amazon VPC configurations, subnets, and Network ACLs.
Review Amazon CloudWatch performance metrics.
Review raw Amazon CloudTrail logs within Amazon S3.
Technical knowledge prerequisites
To successfully complete this lab, you should be familiar with basic AWS services.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Learn more: Where to find more information.
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Task complete: A conclusion or summary point in the lab.
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
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Audit user permissions in IAM
AWS Identity and Access Management (IAM) enables you to securely control access to AWS services and resources for your users. Using IAM, you can create and manage AWS users and groups and use permissions to allow and deny their access to AWS resources.

In this task, you launch IAM secure AWS Access Control in order to review permissions, group assignments and roles associated with the auditing instance:

Review your permissions
At the top of the AWS Management Console, in the search bar, search for and choose IAM.

In the navigation pane at the left of the page, under Access management, choose Users.

On the Users page, choose the link for user-1 to view its details.

Review the Summary section for information about your user.

Select the Security credentials tab to review it.

Here, you can see how many access keys a user has, when an access key was created, whether a Multi-Factor Authentication (MFA) device is assigned, and more.

Access Keys: Keys can be active or inactive and only administrators have the ability to inactivate or delete keys. If a user with limited permissions tried to deactivate or delete an access key, they would receive a message similar to the following:
We encountered the following errors while processing your request: User:arn:aws:iam::111122223333:user/user-1_01 is not authorized to perform: iam:UpdateAccessKey on resource: user user-1_01
Signing Certificates: Can be signed certificates, X.509 Certificate and/or third party tools (e.g. OpenSSL).
Console password: Users with access to the AWS Management Console require a password. Passwords can be generated and/or changed by administrators within the IAM dashboard. Passwords can be auto-generated or custom-generated based on organization preferences.
Assigned MFA (Multi-Factor Authentication) Device: Multi-Factor Authentication is a simple best practice that adds an extra layer of protection on top of your username and password.
Virtual: Use your existing smartphone, tablet, or computer running any application that supports the open TOTP standard.
Hardware Keyfob: Tamper-evident hardware keyfob device provided by Gemalto, a 3rd-party provider.
Hardware Display Card: Tamper-evident hardware display card device provided by Gemalto, a 3rd-party provider.
Choose the Groups tab.
 Consider: Which groups is user-1 associated with?

Notice that user-1 is a member of the user1group group. Groups are a collection of IAM users. Administrators use groups to specify permissions for a collection of users to manage those permissions more efficiently.

### Run the IAM Policy Simulator

You can use the IAM Policy Simulator to test the effects of AWS IAM policies to test your existing IAM policies to verify that they have the intended effect and capture the Policy Simulator output to use as supporting evidence in user access reviews.

Choose the Permissions tab.

In the Permissions policies section, notice there is one policy attached to the user. The Attached via column shows that the ReadOnlyAccess policy is attached to user-1 via the user1group IAM group.

To run the IAM Policy Simulator, open the following link in a new web browser tab: [IAM Policy Simulator](https://policysim.aws.amazon.com/).

On the IAM Policy Simulator page, in the Users, Groups, and Roles pane, choose user-1.

In the Policy Simulator pane, on the Select service drop-down menu, choose IAM Identity Center (successor to AWS Single Sign-On) directory.

On the Select actions drop-down menu, select the following options:

DeleteGroup
Choose Run Simulation.
The Action Settings and Results section displays the effective permissions for user-1, similar to this:

Service	Action	Resource Type	Simulation Resource	Permission
IAM Identity Center (successor to AWS Single Sign-On) directory	DeleteGroup	not required	*	denied Denied by AWS Organizations.
 Consider: Why do you think the action was denied?

Recall that the policy attached to user-1 is a read-only policy. Any actions that could allow changes to a service or resource are denied.

Close the IAM Policy Simulator web browser tab.
 Learn more: Refer to Testing IAM policies with the IAM policy simulator in the Additional resources section for more information.

Collecting audit evidence
From an audit evidence standpoint, you can capture the IAM settings and the IAM Policy Simulator output to be used as support evidence in user access reviews.

 Congratulations! You have successfully audited the permissions assigned to an IAM user.

Task 2: Review the security configuration of Amazon EC2 instances
What is Amazon EC2?
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale computing easier for developers. Amazon EC2 presents a true virtual computing environment, allowing you to use web service interfaces to launch instances with a variety of operating systems, load them with your custom application environment, manage your network’s access permissions, and run your image using as many or few systems as you desire.

In this task, you review security groups and view the running EC2 instances:

What is a security group?
A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level. For each security group, you add rules that control the inbound traffic to instances and a separate set of rules that control the outbound traffic.

The following are basic characteristics of security groups:

You can specify allow rules, but not deny rules.
You can specify separate rules for inbound and outbound traffic.
By default, no inbound traffic is allowed until you add inbound rules to the security group.
By default, all outbound traffic is allowed until you add outbound rules to the group. Then, you specify the outbound traffic that is allowed.
Responses to allowed inbound traffic are allowed to flow outbound regardless of outbound rules and vice versa, as security groups are therefore stateful.
Instances associated with a security group can’t talk to each other unless you add rules allowing it.
Exception: The default security group has these rules by default.
After you launch an instance, you can change which security groups the instance is associated with.
Review running Amazon EC2 instances
At the top of the AWS Management Console, in the search bar, search for and choose EC2.

In the navigation pane at the left of the page, under Instances, choose Instances.

In this lab environment, there are three running instances: Web Server, Bastion Host, and SQL Server.

Review the web server security group
In the navigation pane at the left of the page, under Network & Security, choose Security Groups.

Select WebServerSG.

In the details pane at the bottom of the page, choose the Inbound rules tab.

Review the Inbound rules.

 Consider: Are the inbound rules what you would expect for a web server?

The WebServerSG security group contains rules that allow inbound traffic on ports 80 (HTTP), 443 (HTTPS), and 3389 (RDP). Notice that traffic on ports 80 and 443 is allowed from any source (0.0.0.0/0). However, traffic on port 3389 is only allowed from the BastionSG security group. Even if an EC2 instance in the same subnet as the Web Server attempts to connect to the Web Server instance via RDP, it is only allowed if the BastionSG security group is associated with it. In this example, the Basion Host instance can connect to the Web Server instance via RDP, but the SQL Server instance can’t.

 Note: You can specify a number of different sources in security group rules, such as anywhere, a custom IP address or CIDR, My IP (the IP address of your current workstation), or specific security groups. The rules you choose to implement are a critial step towards running instances and services within Amazon EC2.

Review the bastion host security group
Clear WebServerSG.

Select BastionSG.

A bastion host is a special purpose server on a network specifically designed and configured to withstand attacks. The computer generally hosts a single application (such as a proxy server) and all other services are removed or limited to reduce threats to the computer. It is hardened in this manner primarily due to its location and purpose, which is typically on the outside of the firewall and usually involves access from untrusted networks or computers.

To review the inbound and outbound rules, choose the Inbound rules and Outbound rules tabs respectively.
 Consider: Are the Inbound and Outbound rules what you would expect for the bastion host?

Notice that the Bastion host instance is specifically set up to be accessed from any IP address with the intent to support a protected SQL database instance, which supports an externally facing Web Server.

Review the SQL server security group
Clear BastionSG.

Select SQLSG.

To review the inbound rules, choose the Inbound rules tab.

 Consider: Are the inbound rules what you would expect for the SQL Server?

Notice that the inbound rules are configured with a custom source—a security group ID from this account.

To review the outbound rules, choose the Outbound rules tab.
 Consider: Are the Outbound Rules what you would expect for the SQL Server?

Collecting audit evidence
From an audit evidence standpoint, these findings can support your resource access isolation and data protection from internal or external threats. All access to the SQL Server instance is restricted via a jump box (Bastion Host); therefore, no internal user has direct access to it. Externally, the SQL Server only communicates with the web service via the WebServerSG and SQLSG security groups.

 Congratulations! You have successfully reviewed the security group configuration for each EC2 instance in the environment.

Task 3: Review Amazon VPC security configurations
What is Amazon VPC?
Amazon Virtual Private Cloud (Amazon VPC) permits you to launch AWS resources into a virtual network that you have defined. This virtual network closely resembles a traditional network that you would operate in your own data center, with the benefits of using the scalable infrastructure of AWS. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.

In this task, you will review the VPC settings:

Amazon VPC provides two features that you can use to increase security for your VPC:

Security Groups: Act as a firewall for associated Amazon EC2 instances, controlling both inbound and outbound traffic at the instance level.
Network Access Control Lists (ACLs): Act as a firewall for associated subnets, controlling both inbound and outbound traffic at the subnet level.
When you launch an instance in a VPC, you can associate one or more security groups that you have created. Each instance in your VPC could belong to a different set of security groups. If you do not specify a security group when you launch an instance, the instance automatically belongs to the default security group for the VPC.

Locate Amazon EC2 instance VPC configurations
In the navigation pane at the left of the page, under Instances, choose Instances.

Select Web Server.

The Details pane appears below the list of instances that shows information about the instance you selected.

In the Instance summary section, locate the VPC ID value and copy it to your favorite text editor.
 Note: The VPC ID should look similar to: vpc-0586914dd2bce2335.

Every VPC is associated with a VPC ID. In the next section, you identify the VPC that is associated with this VPC ID.

Review existing VPCs, subnets, and NACLs
In this section, you review your existing VPCs, subnets, and Network ACL capabilities within a Virtual Private Cloud.

At the top of the AWS Management Console, in the search bar, search for and choose VPC.

In the navigation pane at the left of the page, under Virtual private cloud, choose Your VPCs.

Select Lab VPC.

The Details pane appears below the list of VPCs that shows the configuration elements for the selected VPC.

Notice that the VPC ID value is the same VPC ID value that you copied to your text editor.

In the Details section, choose the Main network ACL link.

On the Network ACLs page, select the Network ACL which has a Default parameter value of Yes.

 Note: There should only be one choice.

To review the inbound and outbound rules, in the Details pane at the bottom of the page, choose the Inbound rules and Outbound rules tabs respectively.
 Note: As audit evidence, you can see how the VPC is using ACLs to communicate with an external network via explicit protocols.

 Congratulations! You have successfully reviewed the details of the lab VPC.

Task 4: Audit CloudWatch metrics and alarms
In this task, you review built-in CloudWatch metrics, alarms, and service health associated with running instances, storage volumes, and data services within the auditing instance.

What is Amazon CloudWatch?
Amazon CloudWatch is a monitoring and management service built for developers, system operators, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, understand and respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, providing you with a unified view of AWS resources, applications and services that run on AWS, and on-premises servers. You can use CloudWatch to set high resolution alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to optimize your applications, and ensure they are running smoothly.

In this task, you will review the CloudWatch metrics and alarms:

Audit CloudWatch metrics and alarms
At the top of the AWS Management Console, in the search bar, search for and choose CloudWatch.

In the navigation pane at the left of the page, in the Metrics section, choose All metrics.

On the Browse tab, choose EC2.

Choose Per-Instance Metrics.

In the Search box, search for CPUUtilization.

The search results should display the three EC2 instance that you reviewed previously.

Select SQL Server.

Choose the Graphed metrics tab.

 Note: You can change the Statistic and the Period settings to customize the view to your liking.

Review CloudWatch data for EBS volumes
In addition to viewing Amazon CloudWatch metrics and alarms via the CloudWatch dashboard, you can also view the data in other locations. In this section, you review Amazon CloudWatch data for your Amazon EBS volumes.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

In the navigation pane at the left of the page, under Elastic Block Store, choose Volumes.

Select the Volume that is attached to the Web Server instance.

 Note: To review the volume names and their attached instances, you might need to scroll to the right until you see the Attached resources column header.

In the details pane at the bottom of the page, choose the Monitoring tab.

Review the CloudWatch metrics and any configured CloudWatch alarms.

 Note: Amazon CloudWatch metrics can directly support several auditing elements and provide real-time audit evidence based on pre-defined criterion and custom criterion related to organization processes.

 You have successfully reviewed where to locate CloudWatch metrics and alarms related to an EC2 instance.

Task 5: Audit CloudTrail logs
In this task, you use AWS CloudTrail to review configuration details and S3 storage locations.

What is AWS CloudTrail?
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting.

In this task, you will view the CloudTrail logs:

Find CloudTrail logs
At the top of the AWS Management Console, in the search bar, search for and choose CloudTrail.
 Note: You might receive a warning message on your console with text like the following:

“AccessDeniedException User: arn:aws:sts::XXXXXXXXXXXX:assumed-role/AWSLabsUser-rGHZHM9PZVJvdrZ5anYqkb/8be0dfc8-4d90-4470-8cc9-f4f0a1bb8ff2 is not authorized to perform: cloudtrail:LookupEvents with an explicit deny in an identity-based policy”
In the navigation pane at the left of the page, choose Trails.

Choose the LabCloudTrail link to view its details.

Review the CloudTrail configuration details.

 Note: The LabCloudTrail trail was created using AWS CloudFormation when you started the lab. It’s configured to store logs in the Amazon S3 bucket with a name that starts with CLO281Logs, as defined by the Trail log location property.

At the top of the AWS Management Console, in the search bar, search for and choose S3.

Choose the link for the bucket name that starts with clo281logs.

Choose the AWSLogs/ link.

Continue selecting the links for the various folders until you get to a folder that represents the region your lab was launched in.

 Note: The Region value is listed to the left of these instructions.

Continue selecting the links for the various folders, which represent today’s date, until you see a log file.
The log file name contains the AWS account number, AWS region, a numeric representation of the day’s date and time, and a unique identifier, similar to this: 111122223333_CloudTrail_us-east-1_20230314T1535Z_MArnLpySt8ZdwFnQ.json.gz

Choose the link for one of the log files, with a file name that ends in json.gz.

Choose Open.

Depending on your web browser settings, a new window or a new tab opens that displays the contents of the log file. It is in JSON format.

An alternate approach to viewing your Amazon CloudTrail logs is to download them locally and use a text editor along with the JSON Viewer plug-in.

3rd Party Solutions: AWS partners with third-party specialists in logging and analysis to provide solutions that leverage Amazon CloudTrail output, such as Splunk or Alert Logic.

 Congratulations! You have successfully reviewed the CloudTrail logs for an EC2 instance.

Conclusion
 Congratulations! You have successfully done the following:

Reviewed user permissions in AWS IAM.
Captured audit evidence using AWS IAM Policy Simulator.
Reviewed Inbound and Outbound networking rules for Amazon EC2 Security Groups.
Reviewed Amazon VPC configurations, subnets, and Network ACLs.
Reviewed Amazon CloudWatch performance metrics.
Reviewed raw Amazon CloudTrail logs within Amazon S3.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
Testing IAM policies with the IAM policy simulator
AWS Cloud Security
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.
