# Introduction to Amazon EC2 Auto Scaling

## Lab overview

In this lab, you create a launch template that defines your Amazon Elastic Compute Cloud (Amazon EC2) instances and an Amazon EC2 Auto Scaling group with a single instance in it.

You then terminate the instance and verify that the instance was removed from service and replaced. To maintain a constant number of instances, Amazon EC2 Auto Scaling automatically detects and responds to Amazon EC2 health and reachability checks.

### Objectives

By the end of this lab you will be able to do the following:

Create a launch template.
Create an Auto Scaling group.
Test the Amazon EC2 Auto Scaling infrastructure.
View the results of the Auto Scaling group launch.
Technical knowledge prerequisites
This hands-on lab assumes that you are familiar with launching Amazon EC2 instances and have already created and used key pairs and security groups.

Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 Refresh: A time when you might need to refresh a web browser page or list to show new information
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
Services used in this lab
Amazon EC2 Auto Scaling
Amazon EC2 Auto Scaling helps you ensure that you have the correct number of EC2 instances available to handle your application’s workload. You create collections of EC2 instances, called Auto Scaling groups.

You can specify the minimum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below this size.
You can specify the maximum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes above this size.
If you specify scaling policies, Amazon EC2 Auto Scaling will launch new instances or terminate existing instances when the demand on your application increases or decreases.

 Note: Amazon EC2 Auto Scaling only launches new instances or terminates existing instances. It does not stop or start instances.

Task 1: Creating a launch template
With a launch template, you can save an instance configuration that can be reused, shared, and launched at a later time. For example, a launch template can contain the Amazon Machine Image (AMI) ID, instance type, and network settings that you typically use to launch instances. When you launch an instance using the Amazon EC2 console, an AWS SDK, or the command line interface, you can specify the launch template to use.

In this task, you create a launch template that will be used later for creating an Auto Scaling group.

On the AWS Management Console, in the search box, search for and choose EC2.

In the left navigation pane, in the Instances section, choose Launch Templates.

Choose Create launch template.

In the Launch template name and description section, provide the following details:

For Launch template name, enter Lab-template.
For Template version description, enter version 1.
In the Launch template contents section, specify the details of the launch template, as follows:

In Application and OS Images (Amazon Machine Image), choose Amazon Linux.

In Instance type, choose t3.micro from the dropdown menu.

In Network settings, for Security groups, choose MySecurityGroup.

Leave all other values at their default settings.

Choose Create launch template.

 Expected output: A success message is displayed at the top of the page.

At the bottom of the page, choose View launch templates.

 Note: You are routed to the Launch Templates page, where you can find the details about the template created.

 Congratulations! You have successfully created a launch template with instance configuration that can be launched at a later time.

Task 2: Creating an Auto Scaling group
An Auto Scaling group contains a collection of EC2 instances that share similar characteristics and are treated as a logical grouping for the purposes of instance scaling and management. You can use the Auto Scaling group to scale the number of instances automatically based on criteria that you specify. Or you can maintain a fixed number of instances even if an instance becomes unhealthy. This automatic scaling and maintaining the number of instances in an Auto Scaling group is the core functionality of the Amazon EC2 Auto Scaling service.

In this task, you configure an Auto Scaling group with one instance.

In the left navigation pane, in the Auto Scaling section, choose Auto Scaling Groups.

 Note: If the menu is collapsed, choose the menu  icon.

Choose Create Auto Scaling group.

On the Choose launch template or configuration page, configure the following settings:

For Auto Scaling group name, enter Lab-Group.
For Launch template, choose Lab-template from the dropdown menu.
Choose Next.

On the Choose instance launch options page, configure the network as follows:

For VPC, choose Lab VPC from the dropdown menu.
For Availability Zones and subnets, select both subnets from the dropdown menu.
Choose Next.

On the Configure advanced options - optional page, configure the following settings:

For Health check grace period, enter 60.

 Note: By default, the health check grace period is set to 300. Because this is a lab environment, you have set it to 60 to avoid having to wait very long to see Amazon EC2 Auto Scaling perform the first health check.

For Monitoring, select Enable group metrics collection within CloudWatch.

Choose Next.

On the Configure group size and scaling - optional page, configure group size as follows:

For Min desired capacity, enter 1.
For Max desired capacity, enter 2.
Choose Next.

On the Add notifications - optional page, choose Next.

On the Add tags - optional page, choose Next.

At the bottom of the Review page, choose Create Auto Scaling group.

 Note: You are routed to the Auto Scaling groups page, where you can find the details about the Auto Scaling group created.

 Congratulations! You have successfully created an Auto Scaling group.

Task 3: Verifying your Auto Scaling group
In this task, you learn to access information from the Auto Scaling groups page and verify that the Auto Scaling group has launched the EC2 instance.

Select the check box beside Lab-Group.

 Note: A new pane opens up at the bottom of the page with various tabs providing information about the Auto Scaling group.

Choose the Activity tab.

 Note: Under Activity history, the Status column shows the current status of your instance. When the instance is launching, the status column shows PreInService. The status changes to Successful when the instance is launched. You can choose the refresh  button to see the current status of your instance.

Choose the Instance management tab.

 Note: Under Instances, the Lifecycle column contains the state of your instances. You can see that your Auto Scaling group has launched your EC2 instance and it is in the InService lifecycle state. The Health status column shows the result of the EC2 instance health check on your instance.

Choose the Monitoring tab.

 Note: The Auto Scaling group metrics collected for Amazon CloudWatch monitoring are displayed.

 CAUTION: It can take up to 5 minutes for the metrics to appear.

 Congratulations! You have successfully learned to access and verify details about the Auto Scaling group created.

Task 4: Testing Amazon EC2 Auto Scaling
In this task, you test Amazon EC2 Auto Scaling by taking a running instance out of service. The minimum size for the Auto Scaling group is one instance. Therefore, upon taking the running instance out of service, Amazon EC2 Auto Scaling must launch a new instance to replace it.

In the left navigation pane, choose Instances.

Select  your instance.

From the Instance state  menu, choose Terminate instance.

In the Terminate instance? dialog box, choose Terminate.

 Expected output: A successfully terminated message is displayed at the top of the page, and the Instance state changes to shutting-down and eventually to Terminated.

 CAUTION: Ensure that the Instance state is Terminated. Choose refresh  to update the state.

In the left navigation pane, choose Auto Scaling Groups.

Select the check box beside Lab-Group.

 Note: A new pane opens up at the bottom of the page with various tabs providing information about the Auto Scaling group.

Choose the Activity tab.

 Note: All scaling activities are logged here. Notice the entry for the launch and termination of the first instance and then an entry for the launch of the new instance. This new instance was launched by the Auto Scaling group in response to the instance that was taken out of service.

 CAUTION: It can take a couple of minutes for the Auto Scaling group activities to appear.

Choose the Instance management tab.

 Note: You can see a new instance (with different Instance ID) launch with the instance configuration defined in the launch template.

In the left navigation pane, choose Instances.

 Note: Notice that the first instance is in Terminated state and the second instance launched by Amazon EC2 Auto Scaling is in Running state. You might have to choose refresh  to see the new instance.

 Congratulations! You have successfully tested the Amazon EC2 Auto Scaling functionality.

Conclusion
You have successfully done the following:

Created a launch template
Created an Auto Scaling group
Tested the Amazon EC2 Auto Scaling infrastructure
Viewed the results of the Auto Scaling group launch
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
Amazon EC2 Auto Scaling
Auto Scaling Groups
