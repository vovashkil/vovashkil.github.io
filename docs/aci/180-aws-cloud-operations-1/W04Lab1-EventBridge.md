# Using Amazon EventBridge

## Lab overview

In this lab, you create an Amazon EventBridge rule that calls an AWS Lambda function when an Amazon EC2 Auto Scaling group launches or terminates instance. This creates an Amazon CloudWatch log group with details about the event. You also create a Lambda function and attach a trigger to the function that uses an Amazon EventBridge scheduled rule based on a cron-based schedule.

Services used in this lab
EventBridge is a serverless service that uses events to connect application components together, making it more efficient for you to build scalable, event-driven applications.

Lambda is a compute service you can use to run code without provisioning or managing servers.

Amazon EC2 Auto Scaling helps ensure that you have the correct number of Amazon Elastic Compute Cloud (Amazon EC2) instances available to handle the load for your application.

Objectives
By the end of this lab, you will be able to do the following:

Create Lambda functions to log events and reboot EC2 instances.
Create an EventBridge scheduled rule to log Amazon EC2 Auto Scaling events.
Create an EventBridge Scheduler to reboot EC2 instances monthly.
Test an EventBridge rule by manually updating an EC2 Auto Scaling group.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, Mac OS X, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab requires 40 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 File contents: A code block that displays the contents of a script or file you need to run that has been precreated for you
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal
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
Task 1: Creating the LogAutoScalingEvent Lambda function
In this task, you create the Lambda function to be invoked by the EventBridge rule that you create later in this lab.

On the AWS Management Console, in the search box, search for and choose Lambda.

Choose Create function.

On the Create function page, configure the following the following settings:

Author from scratch: Leave this default option selected.
Function name: Enter LogAutoScalingEvent.
Runtime: Choose the latest supported version of Python, Python 3.xx
Choose  Change default execution role, and then choose Use an existing role.
Existing role: Choose LogAutoScalingGroupRole.
Select Create function.

 Expected output: A banner message like the following appears at the top of the page:  Successfully created the function LogAutoScalingEvent. You can now change its code and configuration. To invoke your function with a test event, choose “Test”.

In the Code source section, delete the code provided in the lambda_function.py file, and replace it with the following  File contents:

import boto3
import json

def lambda_handler(event, context):
    print('LogAutoScalingEvent')
    print('Received event:', json.dumps(event, indent=2))
    return 'Finished'
To deploy the Lambda code updates, choose Deploy.
 Expected output: A banner message like the following appears at the top of the page:  Successfully updated the function LogAutoScalingEvent.

Task 2: Creating the RebootEC2 Lambda function with an EventBridge scheduled rule
In this task, you create a Lambda function called RebootEC2. Then you attach a trigger to the function using an EventBridge scheduled rule that runs off a monthly cron job. When the EventBridge rule is invoked at the specified time, it reboots the EC2 instance associated with the Lambda function code. This is helpful for post patch updates.

In the top left of the page, choose Functions.

Choose Create function.

On the Create function page, configure the following settings:

Author from scratch: Leave this default option selected.
Function name: Enter RebootEC2.
Runtime: Select the latest supported version of Python, Python 3.xx.
Choose  Change default execution role, and then choose Use an existing role.
Existing role: Choose EventBridgeSchedulerRole.
Choose Create function.

 Expected output: A banner message like the following appears at the top of the page:  Successfully created the function RebootEC2. You can now change its code and configuration. To invoke your function with a test event, choose “Test”.

In the Code source section, delete the provided code in the lambda_function.py file, and replace it with the following  File contents:

import boto3
instances = ['REPLACEME']
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    ec2.reboot_instances(InstanceIds=instances)
    print('rebooted your instances: ' + str(instances))
 Copy edit: Copy the InstanceID value listed to the left of these instructions, and replace the REPLACEME placeholder in the previous code block with the copied instance ID.
 Note: Leave the quotation marks so they’re surrounding the instance ID. For example, ‘i-0e7d7bf8ae00cb436’.

To deploy the Lambda code updates, choose Deploy.
 Expected output: A banner message like the following appears at the top of the page:  Successfully updated the function RebootEC2. .

Choose the Configuration tab, and then choose Triggers.

Choose Add trigger, and then configure the following settings:

Choose the dropdown under Trigger configuration, and then choose EventBridge (CloudWatch Events).
Rule: Choose Create a new rule.
Rule name: Enter RebootEC2.
Rule description: Enter Reboots EC2 instances on monthly schedule.
Rule type: Choose Schedule expression.
In the Schedule expression text box, copy and paste the following cron expression: cron(0 23 ? * 2#3 *).
 Additional information: A cron expression creates a fine-grained recurring schedule that runs at a specific time of your choosing. This cron expression invokes at 23:00 every third Monday of every month.

Choose Add.
 Expected output:

 The trigger RebootEC2 was successfully added to function RebootEC2. The function is now receiving events from the trigger.

Choose the Test tab, and then for Event name, enter rebootec2test. Keep the other default options selected.

Choose Test.

 Expected output:

 Executing function: succeeded (logs )

To display the log output, choose  Details option below the Executing function: succeeded message.
 Note: You should observe the rebooted your instances message with the instance ID you added to the Lambda function code, signifying a successful test.

Task 3: Creating the LogAutoScaling EventBridge rule
In this task, you create an EventBridge rule that calls the LogAutoScalingEvent Lambda function when an EC2 Auto Scaling group starts or stops an instance. You send the logs to CloudWatch.

On the AWS Management Console, in the search box, search for and choose Amazon EventBridge.

Choose Create rule.

On the Define rule detail page, configure the following settings:

Name: Enter LogAutoScalingRule.
Description - optional: Enter Event rule logging changes for auto scaling group.
Event bus: Leave the default option selected.
Rule type: Make sure Rule with an event pattern is selected.
Choose Next.

On the Build event pattern page, configure the following settings:

Event source: Choose AWS events or EventBridge partner events.

In the Event pattern section, for AWS service, choose Auto Scaling.

For Event type, choose Instance Launch and Terminate. Leave the default options selected.

Choose Next.

On the Select target(s) page, configure the following settings:

For Select a target, choose Lambda function.
For Function, choose LogAutoScalingEvent.
Choose Next.

On the Configure tags - optional page, choose Next.

Review the information on the Review and create page, and then choose Create rule.

 Expected output: A banner message like the following appears at the top of the page:  Rule LogAutoScalingRule was created successfully.

Task 4: Testing the EventBridge rules
In this task, you manually update the EC2 Auto Scaling group so it launches an instance. After waiting a few minutes for the scale-out event to occur, you verify, through CloudWatch, that the Lambda function invokes.

On the AWS Management Console, in the search box, search for and choose EC2.

In the navigation pane, choose Auto Scaling Groups.

Select the check box  next to the Auto Scaling group with webASG in the name.

In the Group details section, choose Edit.

For Group size, configure the following settings:

Desired capacity: Enter 2.
Min desired capacity: Enter 2.
Max desired capacity: Enter 2.
Choose Update.

On the AWS Management Console, in the search box, search for and choose CloudWatch.

In the navigation pane, choose Logs, and then choose Log groups.

Choose the link for the /aws/lambda/LogAutoScalingEvent log group.

Choose the link for the most recent log stream.

Choose the "resources": [ log event, and then choose and observe the log stream immediately following it. It will look similar to the followng: "arn:aws:autoscaling:us-east-1:577323248295:autoScalingGroup:42f10574-cc4d-436d-bb3c-4ac14aebf419:autoScalingGroupName/LabStack.

 Additional information: This log stream displays the resources involved with this log stream. Here, it’s an Auto Scaling group and an EC2 instance.

Choose and obeserve the details of the log event that starts with "Description":.
 Additional information: This log stream indicates that an EC2 instance has been launched and provides the instance ID.

Choose and obeserve the details of the log event that starts with "Cause":.
 Additional information: This log stream indicates the cause of the event and what happened during the event.

In the left navigation pane, choose Log groups

Choose the link for the /aws/lambda/RebootEC2 log group.

Choose the link for the most recent log stream.

Locate the rebooted your ec2 instances message.

 Note: This message should match the message you received when you tested the Lambda function earlier in the lab.

Conclusion
 Congratulations You have successfully done the following:

Created Lambda functions to log events and reboot EC2 instances
Created an EventBridge rule to log Amazon EC2 Auto Scaling events
Created an EventBridge Scheduler to reboot EC2 instances monthly
Tested an EventBridge rule by manually updating an EC2 Auto Scaling group
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
For more information about how to use EventBridge Scheduler, see Schedule Types on EventBridge Scheduler.

For more information about how to use EventBridge rules, see Amazon EventBridge Rules.

For more information about cron-based schedules, see Cron-Based Schedules.