# Maintaining Traceability Through AWS CloudTrail

## Lab overview

In this lab, you learn about the maintain traceability design principle. You also learn how to use cloud-centered controls like AWS CloudTrail, security groups, and AWS Systems Manager to secure the cloud architecture. You will modify the architecture provided in the lab to support granular logging of API calls made to the environment. And you secure network traffic by narrowing the scope of traffic allowed by security groups and network access control lists (network ACLs).

Services used in this lab
AWS CloudTrail is a service that provides governance, compliance, operational auditing, and risk auditing of your Amazon Web Services (AWS) account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure.

AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.

Objectives
By the end of this lab, you will be able to do the following:

Apply granular logging.
Improve granular control of communication.
Improve granular network-based controls.
Evaluate detailed logging capabilities.
Prerequisites
This lab requires the following:

Use of a personal computer or laptop with Wi-Fi. The lab is not accessible using an iPad or tablet device, but you can use these devices to access the student guide.
Access to the administrator account on your local computer.
Access to an internet browser, such as Chrome or Firefox.
Scenario
Disjointed security tooling was identified at the on-premises environment. There is a lack of insight into what is going on in the environment. There is difficulty managing change control and permissions, which led to risks becoming problems. Set up monitoring with AWS Config and AWS CloudTrail. This helps you have more complete insight into who is doing what in the environment and what changes are being made, and provides notification when problems arise.

For the given architecture, you want to apply detailed, holistic logging and network-based security monitoring. You want to save these logs to a new Amazon Simple Storage Service (Amazon S3) bucket for future evaluation.

Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
Start lab
To launch the lab, at the top of the page, choose Start lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Task 1: Establishing granular logging
Task 1.1: Setting up AWS CloudTrail
In this task, you use CloudTrail to create a trail to log all read/write events. This will record every API call made to the lab’s AWS environment.

On the AWS Management Console, in the search box, search for and choose CloudTrail.
 Note: You might receive a warning message on your console with text like the following:

“AccessDeniedException User: arn:aws:sts::XXXXXXXXXXXX:assumed-role/AWSLabsUser-rGHZHM9PZVJvdrZ5anYqkb/8be0dfc8-4d90-4470-8cc9-f4f0a1bb8ff2 is not authorized to perform: cloudtrail:LookupEvents with an explicit deny in an identity-based policy”
In the left navigation pane, choose Dashboard.
 Note: There are two Dashboard options, be sure to choose the top level one and not the one under the Lake section.

The browser displays the AWS CloudTrail Dashboard page.

Choose Create trail.
The browser displays the Choose trail attributes page.

 Note: You might receive a warning message on your console with text like the following:

“AccessDeniedException User: arn:aws:sts::XXXXXXXXXXXXX:assumed-role/AWSLabsUser-uyQYpXMX4BgHft6ZVqGNmJ/a3ca558b-367e-4ade-b4d3-210024a75bca is not authorized to perform: cloudtrail:GetEventSelectors on resource: arn:aws:cloudtrail:us-east-1:XXXXXXXXXXXXX:trail/AWSLabs-CloudtrailSubaccountAudit with an explicit deny in a service control policy”
Close the error message warning. You can safely ignore this warning and continue with the next step.

On the Choose trail attributes page, in the General details section, configure the following settings:
For Trail name, enter All-API-Commands-across-all-Regions.

For Storage location, select  Create new S3 bucket.

For Trail log bucket and folder, enter cloudsecurity-demo-bucket-ZIP-CODE.

 Additional information: For this lab, you save AWS CloudTrail logs to a new Amazon S3 bucket for future evaluation, referred to on the console as the trail log bucket. Amazon S3 buckets must have unique names, and the names must be DNS compliant. For this lab, to make a unique bucket name, replace the ZIP-CODE placeholder text in the bucket name that you just copied, with your 5-digit ZIP code. Bucket names can only contain lowercase letters, numbers, “-”, and “.”). A valid bucket name would be like this: cloudsecurity-demo-bucket-12345.

For Log file SSE-KMS encryption, clear the check box for  Enabled.

Keep all other parameters at their default settings.

Choose Next.
The browser displays the Choose log events page.

In the Events section, configure the following settings:
For Event type, select the  Management events check box.

Keep all other parameters at their default settings.

Choose Next.
The browser displays the Review and create page. Review your selections for accuracy.

Choose Create trail.
 Note: You might receive an error message like this: “You don’t have adequate permissions in Amazon S3 to perform this operation. Learn more.” If so, check that the trail log bucket that you are creating follows the cloudsecurity-demo-bucket-ZIP-CODE naming convention.

The browser displays the Trails page.

 Note: You might receive a warning message on your console with text like the following:

“AccessDeniedException User: arn:aws:sts::XXXXXXXXXXXXX:assumed-role/AWSLabsUser-uyQYpXMX4BgHft6ZVqGNmJ/a3ca558b-367e-4ade-b4d3-210024a75bca is not authorized to perform: cloudtrail:GetEventSelectors on resource: arn:aws:cloudtrail:us-east-1:XXXXXXXXXXXXX:trail/AWSLabs-CloudtrailSubaccountAudit with an explicit deny in a service control policy”
Close the error message warning. You can safely ignore this warning and continue with the next step.

A list of available trails, including the new one, is displayed. You review the API calls recorded in the CloudTrail log later in the lab.

You have created a new trail for your AWS environment.

Task 1.2: Setting up AWS Config
In this task, you set up the AWS Config service to be used as a change management tool for resources in the environment.

On the AWS Management Console, in the search box, search for and choose Config.

Choose Get started.

 Note: If the option is not available, you can access the configuration by choosing Settings in the navigation menu at the left of the page.

The browser displays the Settings page.

In the Recording method section, configure the following settings:
For Recording strategy, confirm that  All resource types with customizable overrides is selected.

In the Override settings section, choose the Remove button next to All globally recorded IAM resource types.

You store AWS Config data for this lab in a central Amazon S3 bucket.

Next, you create a second new S3 bucket. Use the default name provided to ensure that it is unique.

 Note: It is possible to use the previously created S3 bucket for this. But permissions on the bucket would have to be updated to allow communication with the AWS Config service, which is beyond the scope of this lab.

In the Delivery method section, configure the following settings:
For Amazon S3 bucket, confirm that  Create a bucket is selected.

Keep all other parameters at their default settings.

Choose Next.
The browser displays the Rules page.

No configuration is needed on this page.

Choose Next.
The browser displays the Review page. Review the configuration for accuracy.

Choose Confirm.
The AWS Config Dashboard is displayed.

 Note: If prompted, you can close the Welcome to AWS Config pop-up window.

 Congratulations! In this task, you have set up the AWS CloudTrail and AWS Config services to provide more centralized logging and monitoring of actions occurring in your AWS environment.

Task 2: Improving granular control of communication
In this task, you review and improve upon granular control of network communication between workloads in the cloud.

On the AWS Management Console, in the search box, search for and choose EC2.

In the left navigation pane, under Network & Security, choose Security Groups.

The browser displays the Security Groups page.

Security groups currently in the VPC are listed.

By using the security groups feature of the Amazon Elastic Compute Cloud (Amazon EC2) service, you can define stateful communication rules between services.

Select the security group with the security group name wa-database-sg.
You want to define the scope of the security group. Allow only for the connections that the database instances are intended to communicate with, and no more.

In this lab, you configure the input rules of the security group named wa-database-sg. So only instances using the same security group (self) and the security group named wa-asg-sg (the application instances) are allowed to open connections to instances that are using the security group named wa-database-sg (the database instances).

On the bottom half of the page, choose the Inbound rules tab.
Choose Edit inbound rules.
The browser displays the Edit inbound rules page.

Choose Delete to remove any existing rule.
Choose Add rule.
Configure a rule as follows:
For Type, choose MYSQL/Aurora.

For Source, choose Custom.

In the search box next to the Source dropdown, choose the security group named wa-asg-sg.

Choose Add rule.
Configure a rule as follows:
For Type, choose MYSQL/Aurora.

For Source, choose Custom.

In the search box next to the Source dropdown, choose the security group named wa-ec2-database-sg.

Choose Save rules.
 Expected output: A banner message like the following is displayed at the top of the page:  Inbound security group rules successfully modified on security group (sg-0182867f2c1d7c460 | wa-database-sg) .

On the Inbound rules tab, in the Source column, confirm that the only allowed sources are the security groups named wa-ec2-database-sg and wa-asg-sg. This column can be expanded if necessary.

Choose the Outbound rules tab.

The existing rule is too broad and would allow outbound communication originating from the database on any port.

Choose Edit outbound rules.
The browser displays the Edit outbound rules page.

Choose Delete to remove the existing rule.

Choose Add rule.

Configure the rule as follows:

For Type, choose All traffic.

For Destination, choose Custom.

In the search box next to the Destination dropdown, choose the security group named wa-asg-sg.

Choose Save rules.
 Expected output: A banner message like the following is displayed at the top of the page:  Outbound security group rules successfully modified on security group (sg-0182867f2c1d7c460 | wa-database-sg) .

On the Outbound rules tab, in the Destination column, confirm that the outbound rule now shows the wa-asg-sg security group that you selected. This column can be expanded if necessary.
The configuration that you made means that traffic originating from instances using the wa-database-sg (the database instances) are only allowed to communicate to instances using the security group named wa-asg-sg (the application instances).

 Congratulations! In this task, you narrowed the scope of allowed inbound and outbound connections in the security group named wa-database-sg, so that only the intended connections are allowed.

Task 3: Improving granular network-based controls
In this task, you improve network-based controls by using network ACLs to prevent side-to-side movement in a granular way. You want to explicitly block the Application Load Balancer in your environment from talking directly to the database servers on specific ports.

Security groups are used to define the allowed inbound and outbound traffic for the associated resources in an explicit manner. Security groups work with the connections in stateful manner.

If there is need to define stateless access to your environment, use network ACLs.

On the AWS Management Console, in the search box, search for and choose VPC.

In the left navigation pane, under Security, choose Network ACLs.

The browser displays the Network ACLs page.

Choose Create network ACL.
The browser displays the Create network ACL page.

In the Network ACL settings section, configure the following settings:
For Name, enter LoadBalancerIsolation.

For VPC, choose wa-lab-vpc.

Keep all other parameters at their default settings.

Choose Create network ACL.
The browser displays the Network ACLs page.

 Expected output: A banner message like the following is displayed at the top of the page:  You successfully created acl-05bef764a1dd175c7 / LoadBalancerIsolation. .

Select  LoadBalancerIsolation in the list.

Choose the Details tab.

Copy the Network ACL ID value. Save the value in a text editor for future use.

Choose the Outbound rules tab.

Choose Edit outbound rules.

The browser displays the Edit outbound rules page.

Add three outbound rules as follows:
For each rule, choose Add new rule.

Use the following information to configure each rule:

For Rule number, enter 50.
For Type, choose All traffic.
For Destination, enter 10.100.4.0/24.
For Allow/Deny, choose Deny.

For Rule number, enter 60.
For Type, choose All traffic.
For Destination, enter 10.100.5.0/24.
For Allow/Deny, choose Deny.

For Rule number, enter 100.
For Type, choose All traffic.
For Destination, enter 0.0.0.0/0.
For Allow/Deny, choose Allow.

When you have added all three rules, choose Save changes.
When applied to a subnet, these network ACL rules block network communication that originates within the subnet that is targeting the subnets that host the databases. The network ACLs still allow for outbound access to other IP addresses. Note that network ACLs are evaluated in the order of their rule number, from lowest to highest.

The browser displays the Network ACLs page.

 Expected output: A banner message like the following is displayed at the top of the page:  You have successfully updated outbound rules for acl-05bef764a1dd175c7 / LoadBalancerIsolation.

 CAUTION: When you create a subnet, each subnet has a default network ACL that has rules to allow all communication in both directions. However, when you create a new network ACL rule, a Deny All rule is applied in both directions.

After saving the new outbound network ACL rules, you need to allow access to that subnet from the internet.

Recreating the All Traffic Allow rule for Inbound Rules is necessary.

Choose the Inbound rules tab.

Choose Edit inbound rules.

The browser displays the Edit inbound rules page.

Choose Add new rule.

Configure the rule as follows:

For Rule number, enter 100.
For Type, choose All traffic.
For Source, enter 0.0.0.0/0.
For Allow/Deny, choose Allow.
Choose Save changes.
The browser displays the Network ACLs page.

 Expected output: A banner message like the following is displayed at the top of the page:  You have successfully updated inbound rules for acl-05bef764a1dd175c7 / LoadBalancerIsolation.

Choose the Subnet associations tab.

Choose Edit subnet associations.

Select the check box next to the  wa-public-subnet-1 subnet.

Select the check box next to the  wa-public-subnet-2 subnet.

Choose Save changes.

The browser displays the Network ACLs page.

 Expected output: A banner message like the following is displayed at the top of the page:  You have successfully updated subnet associations for acl-0a44182f71dd800e6 / LoadBalancerIsolation.

Now confirm that the application is working after these changes.

Copy the ApplicationUrl value that is listed to the left of these instructions, and paste it into a new browser tab to access the application.
The browser displays the application web page.

Using network ACLs, you have effectively ensured that the Application Load Balancer, which is exposed to the internet, cannot communicate with or compromise the database servers directly.

 Congratulations! In this task, you created and configured network ACLs that deny communication directly between the Application Load Balancer and the database instances.

Task 4: Evaluating detailed logging capabilities
You made several configuration changes to the network. These kinds of changes might be difficult to track on premises. However, with AWS CloudTrail, which was set up in prior tasks, all the different actions that took place throughout the lab have been recorded.

Task 4.1: Examining the CloudTrail logs
In this task, you examine some of the CloudTrail logs.

On the AWS Management Console, in the search box, search for and choose CloudTrail.
 Note: You might receive a warning message on your console with text like the following:

“AccessDeniedException User: arn:aws:sts::XXXXXXXXXXXX:assumed-role/AWSLabsUser-rGHZHM9PZVJvdrZ5anYqkb/8be0dfc8-4d90-4470-8cc9-f4f0a1bb8ff2 is not authorized to perform: cloudtrail:LookupEvents with an explicit deny in an identity-based policy”
The browser displays the AWS CloudTrail Dashboard page.

The dashboard shows recent events, but you want to review the specific API calls that you made throughout this lab.

In the left navigation pane, choose Trails.
The browser displays the Trails page.

Choose the link for the trail named All-API-Commands-across-all-Regions. This is the name of the trail that you created earlier.
The browser displays the All-API-Commands-across-all-Regions details page.

In the General details section, locate the Trail log location.
This link indicates the Amazon S3 bucket where the logs for this trail are stored.

Choose the link for the S3 bucket, which has a name beginning with cloudsecurity-demo-bucket-ZIP-CODE, which you customized previously.
The Amazon S3 console opens and shows the trail log bucket, at the top level of the directory for the log files.

Choose the CloudTrail/ link.
There is a folder for each Region where a log was recorded. The hierarchy of the Amazon S3 bucket navigation at this level is bucket-name/AWSLogs/account-id/CloudTrail/region-name.

Choose the folder for the AWS Region that matches the region to the left of the instructions to review log files. For example, choose us-west-2/.

Navigate the bucket folder structure to the year, month, and day where you want to review AWS CloudTrail logs of activity in that Region.

The hierarchy of the Amazon S3 bucket navigation at the individual log level is bucket-name/AWSLogs/account-id/CloudTrail/region-name/year/month/day.

For each day, there are several log files. The names of the files begin with your AWS account ID, and end with the extension .gz. For example, if your account ID is 123456789012, the files are named like this: 123456789012_CloudTrail_us-east-2_20190610T1255abcdeEXAMPLE.json.gz.

To review these files, you can download them, uncompress them, and then review them using a plain-text editor or a JSON file viewer. Some browsers also support opening .gz and JSON files directly.

To open and view a file, do the following:

Select the check box  next to the most recent file in the list.

Choose the Download option, and save the file locally.

The downloaded log file can be uncompressed and viewed with a text editor.

AWS CloudTrail logs events for every AWS service that experienced activity in that AWS Region at the time that event occurred. In other words, events for different AWS services are mixed, based solely on time.

 Additional information: To learn more about what a specific service logs with CloudTrail and the content and structure of CloudTrail log files, refer to the links in the Additional resources section at the end of this lab.

Console sign-in and AWS Identity and Access Management (IAM) events are global service events, but are logged in a specific AWS Region. Those files are not accessible in this lab. The following snippet represents an IAM sign-in event that you would find in those logs.

 Example:


{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AKIAIOSFODNN7EXAMPLE",
    "arn": "arn:aws:iam::123456789012:user/Mary_Major",
    "accountId": "123456789012",
    "userName": "Mary_Major"
  },
  "eventTime": "2019-06-10T17:14:09Z",
  "eventSource": "signin.amazonaws.com",
  "eventName": "ConsoleLogin",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "203.0.113.67",
  "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
  "requestParameters": null,
  "responseElements": {
    "ConsoleLogin": "Success"
  },
  "additionalEventData": {
    "LoginTo": "https://console.aws.amazon.com/console/home?state=hashArgs%23&isauthcode=true",
    "MobileVersion": "No",
    "MFAUsed": "No"
  },
  "eventID": "2681fc29-EXAMPLE",
  "eventType": "AwsConsoleSignIn",
  "recipientAccountId": "123456789012"
}
This log file tells you more than just the identity of the IAM user who logged in (Mary Major), the date and time that they logged in, and that the login was successful. You can also learn the IP address that the user logged in from, the operating system and browser software of the computer, and that multi-factor authentication was not used.

Now that you have a trail, you have access to an ongoing record of events and activities in your AWS account. This ongoing record helps you meet accounting and auditing needs for your AWS account. However, there is a lot more that you can do with AWS CloudTrail.

In this task, you navigated to AWS CloudTrail and retrieved one of the trail logs made from API calls during the lab.

Task 4.2: Examining logs of the changes made with AWS Config
In this task, you verify that AWS Config is recording configuration changes made to the AWS environment.

On the AWS Management Console, in the search box, search for and choose Config.

In the left navigation pane, choose Resources.

 Note: There are two Resources options to choose, be sure to NOT choose the option under Aggregators.

The browser displays the Resource Inventory page.

In the Resources section, for Resource type, choose AWS EC2 NetworkAcl.
A list of currently managed ACLs is displayed.

Choose the link in the Resource identifier column that matches the network ACL ID that you copied earlier in this lab when you created the network access list.
The browser displays the Details pages for the ACL.

Choose Resource Timeline.
The browser displays the Timeline page.

In the resource timeline, you can find the events that occurred when changes were made to the network ACL in the lab.

Expand newest  Configuration change event.
The Relationship Change value shows, in JSON format, which subnets were associated with the network ACL in the configuration event.

Examine details of the event and confirm that the subnets were associated with the ACL.
 Congratulations! In this task, you examined a configuration change to one of the ACLs to verify that AWS Config is recording configuration changes made to the AWS environment.

Conclusion
 Congratulations! You now have successfully done the following:

Applied granular logging
Improved granular control of communication
Improved granular network-based controls
Evaluated detailed logging capabilities
Additional resources
For more information about the security pillar design principles, see Design Principles.
To learn more about what a specific service logs with CloudTrail, including examples of log file entries, review the documentation for the list of supported services for CloudTrail on the CloudTrail Supported Services and Integrations page and read the CloudTrail integration topic for that service.
To learn more about the content and structure of CloudTrail log files, see CloudTrail Log Event Reference.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.