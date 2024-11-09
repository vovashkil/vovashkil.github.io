# Using AWS Systems Manager Automation to Resize EC2 Instances

## Lab Overview

In this lab, you resize multiple Amazon Elastic Compute Cloud (Amazon EC2) instances by using the predefined Automation document called AWS-ResizeInstance.

Objectives
By the end of this lab, you will be able to do the following:

Configure an Automation workflow.
Identify the different actions involved in an Automation workflow.
Duration
This lab requires 30 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
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
Lab environment
2 Amazon EC2 instances have been provisioned. Systems Manager Agent is a prerequisite for this lab and hence the instances have the agent installed.

Lab Scenario
Imagine that you are an administrator of a business that had 10,000 instances across 3 regions. The finance team worked with Enterprise Support to perform a Cost Optimization analysis and identified 2,500 instances running larger instance types than are necessary for the workload. You are now tasked with resizing them. Automation can now take what would be a painful task and turn it into a planned maintenance that one person can execute in a timely manner.

Services used in this lab
AWS Systems Manager Overview
AWS Systems Manager is a powerful unified interface from AWS that provides you with the ability to centrally manage your AWS resources.

Automation, a capability of AWS Systems Manager, simplifies common maintenance, deployment, and remediation tasks for AWS services like Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS), Amazon Redshift, Amazon Simple Storage Service (Amazon S3), and many more.

Automation helps you to build automated solutions to deploy, configure, and manage AWS resources at scale. With Automation, you have granular control over the concurrency of your automations. This means you can specify how many resources to target concurrently, and how many errors can occur before an automation is stopped.

Task 1: Observe EC2 instance size
In this task, you observe EC2 instance size.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

In the navigation pane on left, select Instances.

On this page, there are two EC2 instances which are name tagged as Test-Instance and one instance which is name tagged as Prod-Instance. Observe that the Instance type value is set to t3.small for all 3 instances.

Task 2: Configure Automation workflow
In this task, you change the instance size of the instances in Test environment from t3.small to t3.micro using Automation workflow.

At the top of the AWS Management Console, in the search bar, search for and choose Systems Manager.

In the navigation pane on left, select Automation under Change Management.

Choose Execute automation

Now, you are on the Choose runbook page. In the search box, type and enter AWS-ResizeInstance

Choose the radio button next to AWS-ResizeInstance.

Scroll down and choose Next

In the Execution Mode runbook section, Choose Rate control.

 Additional information:

Rate control allow you to control the deployment of an automation across your fleet by specifying a concurrency value and an error threshold.

Concurrency is used to specify how many resources are allowed to run an automation simultaneously. Concurrency helps to limit the impact or downtime on your resources when processing an automation. You can specify either an absolute number of resources, for example 20, or a percentage of the target set, for example 10%.

Error threshold is used to specify how many automations are allowed to fail before AWS Systems Manager stops sending the automation to other resources. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%.

In the Targets section, choose Parameter value as InstanceId.

Choose Targets value as Tags.

Enter Tag key as Name

Enter Tag value as Test-Instance

Choose Add

 Note: In complex production environments with thousands of instances, this is the recommended approach where you select targets by Specifying a tag. In this approach, you give the same tag name for each resource, and Systems Manager systematically applies the configuration for every resource identified by that tag.

In the Input parameters, enter InstanceType value as t3.micro

 Note: This is the desired instance type value you want your instances to be set too.

Keep the rest of the values as default, choose Execute

 Expected output This message is displayed at the top of the screen Execution has been initiated

The Overall status value is set to In progress.

Wait about 5 to 10 minutes, until the Overall status value is changed to Success

Once the status is changed to success, observe that the Executed steps section have 2 Step IDs, one for each of the instance.

Choose the first Step ID. This takes you to the Execution detail page.

Choose Step execution ID, to observe more detailed steps about the steps executed in this particular automation.

In the Executed steps section, you can see 5 different actions performed in this automation. Note the following details about some of the Actions:

Actions:

aws:assertAwsResourceProperty: This action allows you to assert a specific resource state or event state for a specific Automation step. In this case, this action verifies if the instance type is not set to t3.micro already. Since, the instance is not set to t3.micro, it marks this action as failed and moves forward with the next steps.

aws:changeInstanceState: This action changes or asserts the state of the instance. In this case, it changes the instance to Stop state by initiating a StopInstance API call.

aws:executeAwsApi: This action calls and runs AWS API operations. In this case, it calls and runs the ModifyInstanceAttribute API operation, which resizes the instance to the desired value (t3.micro in this lab).

aws:sleep: This action delays an automation for a specified amount of time.

aws:changeInstanceState: This action changes or asserts the state of the instance. In this case, it changes the instance to running state by starting the instance using a StartInstance API call.

Navigate to EC2 instance page, to view the changes.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

In the navigation pane on left, select Instances.

On this page, observe that the Instance type value is now changed to t3.micro for the instances tagged with name Test-Instance, whereas the instance tagged Prod-Instance is still set to t3.small.

 Task complete: You have successfully resized EC2 instances using Systems Manager Automation service.

Conclusion
You successfully done the following:

Configured an Automation workflow.
Identified the different actions involved in an Automation workflow.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional Resources
For more information about AWS Systems Manager Automation, see AWS Systems Manager Automation.
For more information about Automation actions, see Automation actions.