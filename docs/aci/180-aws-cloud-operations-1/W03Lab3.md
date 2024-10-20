# Monitoring and Alerting with AWS CloudTrail and Amazon CloudWatch

## Lab overview

In this lab, you configure logging and monitoring in an Amazon Web Services (AWS) account. You create an AWS CloudTrail trail, which is an audit log of API calls made in the account. You then create an Amazon Simple Notification Service (Amazon SNS) topic. By subscribing your email to the topic, you will be alerted when particular events occur. Next, you create an Amazon CloudWatch alarm to notice whenever multiple failed login attempts to the AWS Management Console occur.

Services used in this lab
AWS CloudTrail is a service that provides governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continually monitor, and retain account activity related to actions across your AWS infrastructure.

Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.

Amazon CloudWatch Logs enables you to centralize the logs from all of your systems, applications, and AWS services that you use, in a single, highly scalable service.

Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.

Objectives
By the end of this lab, you will be able to do the following:

Analyze CloudTrail events in CloudWatch.
Create a CloudTrail trail with CloudWatch logging enabled.
Create an Amazon SNS topic and an email subscription to it.
Create CloudWatch metric filters and CloudWatch alarms.
Query CloudTrail logs by using Amazon CloudWatch Logs Insights.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, macOS X, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Scenario
The lab starts with a preconfigured CloudTrail trail that writes to CloudWatch Logs. You go through the steps to create and configure one, but security restrictions don’t allow you to create a trail in the lab, so one has been created for you to use. The lab also includes a preconfigured AWS Identity and Access Management (IAM) user, which you use to test alerting for failed console login attempts.

Below is a diagram which shows the multiple failed log in attempts from the test user. These API events are written and sent to CloudTrail which then writes to CloudWatch Logs. It will then create a metrics filter which tirggers a CloudWatch alarm that will then send an SNS email notification to the user account:

Architecture at end of task 4.

Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
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

## Task 1: Creating a CloudTrail trail with CloudWatch Logs enabled

In this task, you analyze the type of event information that is available in the CloudTrail event history. You also create a CloudTrail trail with CloudWatch logging enabled.

Task 1.1: Analyzing the information available in the CloudTrail event history from CloudWatch
On the AWS Management Console, in the search box, search for and choose CloudWatch.
 Note: You might receive warning messages on your console. You can ignore these and they will not impact the lab.

In the left navigation pane, choose Log groups.

Choose CloudTrailLogGroup from the Log groups.

Choose one of the Log streams.

View any of the Log events that are logged from CloudTrail.

 Additional information: The event history exists by default in each Region. The history shows events from the last 90 days for the Region that you are viewing. This view is limited to management events with create, modify, and delete API calls and account activity. To maintain a record of account activity that extends past 90 days, including all management events with the option to include data events and read-only activity, you need to configure a CloudTrail trail. You do this in the next task.

Task 1.2: Creating a CloudTrail trail with CloudWatch Logs enabled.
On the AWS Management Console, in the search box, search for and choose CloudTrail.

In the left navigation pane, choose Trails, and then choose Create trail.

 Note: You might receive warning messages on your console. You can ignore these and they will not impact the lab.

On the Choose trail attributes page, configure the following settings:

Trail name: Enter MyLabCloudTrail.

Storage location: Select Create a new S3 bucket, and accept the default bucket name, which includes aws-cloudtrail-logs.

Log file SSE-KMS encryption: Clear the check box  (to disable this option).

CloudWatch Logs: Select  Enabled.

Select New for the log group, and accept the default log group name.

For IAM role, select Existing.

Role name: Choose LabCloudTrailRole.

Keep the other default trail attributes, and choose Next.

On the Choose log events page, configure the following settings:

Event type: Keep Management events selected.

API activity: Keep  Read and  Write selected.

Choose Next.

Scroll down to the bottom of the page.

 Note: This is where you would complete the process to create the trail. However, the user that you are logged in as does not have the necessary permissions to create a CloudTrail trail with CloudWatch Logs enabled. This is because of the security restrictions placed on AWS accounts that are used for labs.

Instead, choose Cancel.

Choose the LabCloudTrail trail to analyze it.

Notice that a trail named LabCloudTrail already exists. It is configured with the same settings that you chose in the previous step, except for minor differences such as the Amazon Simple Storage Service (Amazon S3) bucket name and log group name.

This CloudTrail trail, with CloudWatch logging enabled, is an essential component of the monitoring and alerting solutions that you build in the rest of this lab.

Task 2: Creating an SNS topic and subscribing to it
In this task, you create an SNS topic and subscribe your email address to the topic. The topic will be used in later tasks to deliver email alerts to you about important activity that occurs in the AWS account.

On the AWS Management Console, in the search box, search for and choose Simple Notification Service.

To open the navigation pane, choose the  menu icon in the upper-left corner.

In the navigation pane, choose Topics.

Choose Create topic.

On the Create topic page, configure the following settings:

Type: Select Standard.

Name: Enter MySNSTopic.

Expand the  Access policy - optional section.

In the Publishers  dropdown list, choose Everyone.

In the Subscribers  dropdown list, choose Everyone.

At the bottom of the page, choose Create topic.

To create an email subscription to the SNS topic, choose Create subscription.

On the Create subscription page, configure the following settings:

Topic ARN: Notice that the Amazon Resource Name (ARN) of the topic that you just created is already filled in.

Protocol: Choose Email.

Endpoint: Enter an email address where you can receive emails during this lab.

Scroll to the bottom of the page, and choose Create subscription.

Check your email for a message from AWS Notifications.

In the email body, choose the Confirm subscription link.

 Additional information: By confirming the subscription, you will get emailed alerts from Amazon SNS.

Task 3: Creating a CloudWatch alarm based on a metric filter
In this task, you use CloudWatch to notify you when a user fails to log in to the console a specific number of times.

Task 3.1: Creating a CloudWatch metric filter
On the AWS Management Console, in the search box, search for and choose CloudWatch.

In the left navigation pane, expand  Logs, and then choose Log groups.

Select the check box for  CloudTrailLogGroup.

 Note: Recall that when you created the CloudTrail trail, you configured it to create this log group.

Choose Actions  and choose Create metric filter.

Configure the following settings:

Filter pattern: Copy and paste the following code:


{ ($.eventName = ConsoleLogin) && ($.errorMessage = "Failed authentication") }
Choose Next.

Filter name: Enter ConsoleLoginErrors.

Metric namespace: Enter CloudTrailMetrics.

Metric name: Enter ConsoleLoginFailureCount.

Metric value: Enter 1.

At the bottom of the page, choose Next.

Choose Create metric filter.

 Expected output: A banner message like the following is displayed at the top of the page:  Metric filter “ConsoleLoginErrors” has been created. .

Task 3.2: Creating a CloudWatch alarm based on the metric filter
On the Metric filters tab, select the check box to the right of the ConsoleLoginErrors metric filter that you just created.

Choose Create alarm .

A new browser tab opens.

On the Specify metric and conditions page, in the Conditions section, configure the following alarm details:

Whenever ConsoleLoginFailureCount is…: Select Greater/Equal.

than…: Enter 3.

Observe the settings. This alarm will be invoked whenever the sum of the ConsoleLoginFailureCount metric that you defined is greater than or equal to 3 within any 5-minute period.

Choose Next.

On the Configure actions page, configure the following settings:

Send a notification to the following SNS topic: Select Select an existing SNS topic

Send a notification to…: Choose MySNSTopic.

Choose Next.

On the Add name and description page, configure the following settings:

Alarm name: Enter FailedLogins.

Choose Next.

Scroll to the bottom of the page, and choose Create alarm.

Task 3.3: Testing the CloudWatch alarm
On the AWS Management Console, in the search box, search for and choose IAM.

In the left navigation pane, choose Users.

Choose the link for the test user name.

Choose the Security credentials tab, and then copy the Console sign-in link.

Paste the copied link into a new browser tab to load the console sign-in page.

Enter credentials including an incorrect password, and attempt to sign in. Repeat this at least three times:

IAM user name: Enter test.

Password: Enter test.

Choose Sign in.

 Note: Each time that you attempt to log in, you will see a message indicating that your authentication information is incorrect. This is expected!

Re-establish your access to the AWS account.

Close all browser tabs where you have the AWS Management Console open.

On the lab instructions page, choose the Open Console  link above these instructions to log in again.

 Additional information: Your attempts to log in to the console as the test user cleared the previous authentication information from your browser’s cache. Therefore, you need to reauthenticate to gain access to the console.

Task 3.4: Graphing the metric that you created
Navigate to the CloudWatch console.

In the navigation pane, expand  Metrics, and then choose All metrics.

In the Metrics section, under Custom namespaces, choose CloudTrailMetrics.

 Note: If CloudTrailMetrics does not yet appear, wait until the SNS notification is received.

Choose Metrics with no dimensions.

Choose ConsoleLoginFailureCount and then choose Graph this metric only.

In the graph area at the top of the page, a small blue dot should appear. The dot indicates that a login failure was detected.

Task 3.5: Checking the alarm status and details in the CloudWatch console
Open the navigation pane, expand  Alarms, and then choose All alarms.
The State for the FailedLogins alarm should be In alarm.

 Note: If the alarm doesn’t show this state, wait a minute or two. To refresh the page, choose the  refresh icon.

 Hint: To find out if the alarm was invoked recently, choose the link for the FailedLogins alarm name, and then choose the History tab.

Check the inbox of the email address that you subscribed to the SNS topic.
You should have received a message about multiple failed login attempts, with content that is similar to the following image:

CloudWatch alarm email contents.

Task 4: Querying CloudTrail logs by using CloudWatch Logs Insights
In this task, you use CloudWatch Logs Insights to query CloudTrail logs.

With CloudWatch Logs Insights, you can interactively search and analyze your log data in Amazon CloudWatch Logs. You can perform queries to help you more efficiently and effectively respond to operational issues.

In the CloudWatch console, in the navigation pane, choose Logs Insights.

From the Select up to 50 log groups dropdown menu under the Logs Insights section heading, select  CloudTrailLogGroup.

Delete the existing content from the query field below the dropdown menu, and then copy and paste the following code into the query field:


filter eventSource="signin.amazonaws.com" and eventName="ConsoleLogin" and responseElements.ConsoleLogin="Failure"
| stats count(*) as Total_Count by sourceIPAddress as Source_IP, errorMessage as Reason, awsRegion as AWS_Region, userIdentity.arn as IAM_Arn
Choose Run query.
The output should look similar to the following graph:

CloudWatch Logs Insights example output.

Conclusion
 Congratulations! You now have successfully done the following:

Analyzed event details in the CloudTrail event history
Created a CloudTrail trail with CloudWatch logging enabled
Created an SNS topic and an email subscription to it
Created CloudWatch metric filters and CloudWatch alarms
Queried CloudTrail logs by using CloudWatch Logs Insights
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.