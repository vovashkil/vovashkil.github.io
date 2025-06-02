# Monitoring and Troubleshooting Amazon EC2 Workloads with Detective Controls

## Lab Overview

In this lab, you have an opportunity to explore monitoring tools for your Amazon EC2 workloads, as well as apply troubleshooting steps to correct issues affecting your current workloads. You explore and use available monitoring tools for your workloads that allows you to understand when issues are occurring, and have the ability to take corrective actions. The corrective actions outline troubleshooting steps and that helps you narrow down and resolve the specific issue. The troubleshooting steps show how to apply the data received from the detective controls (monitoring tools) to identify root cause and bring the issue to a successful resolution.

## Objectives

By the end of this lab, you will be able to do the following:

Describe the methodology for troubleshooting Amazon EC2 issues.
Describe the monitoring tools available and their functionality.
Implement AWS monitoring tools for a given workload.
Troubleshoot scenarios/issues affecting EC2 workloads.
General prerequisites:

Access to a notebook computer with Wi-Fi Microsoft Windows, MacOS X, or Linux (Ubuntu, SuSE, or Red Hat).
A modern internet browser such as Chrome or Firefox.
Technical knowledge prerequisites
Experience with Cloud platforms.
Basic navigation of the AWS Management Console.
AWS Compute Services Overview and Amazon EC2 Basics.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Learn more: Where to find more information.
 Caution: Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal.
Duration
This lab requires 75 minutes to complete.

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
Lab Scenario
You have your application workload operating on Amazon EC2 instances. You are notified by a co-worker that your customers are complaining about the web site being inaccessible. You need to determine the issue and get the application up and running as soon as possible. This lab walks you through a couple of troubleshooting scenarios. In each scenario, you will use a high-level set of steps to narrow down the root cause and inform a correct solution based on the data gathered. You explore Amazon CloudWatch service to review metrics from various components, such as Amazon EC2 instances, an Application load balancer, EC2 target group, and EC2 Auto Scaling group. These tools and the troubleshooting steps outlined will lead you to understand how to break down and evaluate potential root causes for your workload issues.

Lab Environment
For this lab, you are provided with the following resources:

Three Amazon EC2 instances hosting your application website.
Application Load Balancers.
EC2 Target Groups.
EC2 Launch Templates.
An EC2 Auto Scaling Group.
Other supporting networking components such as a VPC, an Internet Gateway, Subnets, IAM Roles, Security Groups, and more.
Scenario 1: Application is unreachable
In this scenario, you are notified that your application is currently unreachable and customers are unable to reach your website. You are tasked to identify the problem and remediate the issue at hand. You use different troubleshooting steps and available monitoring tools to come up with a resolution. Lastly, you make monitoring improvements based on your lessons learnt during this scenario and apply those learnings to ensure you are better prepared in the future.

Task 1: Identify the problem
You received a page that your application is down and your customers are complaining about your website being unreachable for a while. In this task, your first step is to identify the problem and verify the accessibility of your application.

Since your application is using an external internet-facing Application load balancer, first step would be to verify if you are able to access your website using your load balancer URL.

 Copy edit: Copy the value of ApplicationURL to the left of these instructions and paste it into a new browser tab.
At this point, the application fails to load and the browser returns a 504 Gateway Time-out error:

 Expected Output:

504 Gateway Time-out

  Task complete: You successfully identified the problem and your application is indeed unreachable at this moment. In the following tasks, you will collect and analyze data related to your application and remediate the issue at hand.

Task 2: Collect and analyze data
In this task, you collect data by analyzing your application resources and find the root cause of this issue. You start by using Amazon CloudWatch and review several metrics which are available for your Application load balancer and target groups.

Some of the metrics to consider for load balancers are:

HTTP_Fixed_Response_Count: The number of fixed-response actions that were successful.
HTTPCode_ELB_3XX_Count: The number of HTTP 3XX redirection codes that originate from the load balancer. This count does not include response codes generated by targets.
HTTPCode_ELB_4XX_Count: The number of HTTP 4XX client error codes that originate from the load balancer. This count does not include response codes generated by targets.
HTTPCode_ELB_5XX_Count: The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the targets.
HTTPCode_ELB_504_Count: The number of HTTP 504 error codes that originate from the load balancer.
Similarly, the following metrics are useful for target groups:

HealthyHostCount: The number of targets that are considered healthy.
UnHealthyHostCount: The number of targets that are considered unhealthy.
 Learn more: For detailed information on Application Load Balancer metrics, see CloudWatch metrics for your Application Load Balancer.

Now review some of these metrics associated with your Application Load Balancer.

Switch back to the browser tab open to the AWS Management Console.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

From the left navigation menu, expand the Load Balancing section and choose Load Balancers.

On the Load balancers page, select the link to the load balancer named myAppLB-A.

On the myAppLB details page, scroll down and choose the Monitoring tab.

Here, you see a bunch of graphs displaying different metrics for your application load balancer. Notice the ELB 4XX and 5XX errors for all instances. Also, notice the HTTP 504 errors for the load balancer. These errors match with the errors that you saw earlier when trying to access your application.

To filter the results by time, select a time range using the Custom  option. To get a larger view of a single metric, select its graph.
 Caution: You might have to wait for about 5-7 minutes for CloudWatch to generate graphs for these metrics. Use the refresh  option as required.

 Learn more: Take a moment to review the HTTP errors generated by the load balancer. For more information, see The load balancer generates an HTTP error.

Next, review the Target Group metrics to get a better understanding of this issue.

From the left navigation menu under Load Balancing, choose Target Groups.

On the Target groups page, select the link to myTargetGroupA target group associated with myAppLB-A load balancer.

On myTargetGroupA details page, scroll down and choose the Targets tab.

Here you notice that currently there are 3 instances registered as targets. Reviewing the Health status column, you notice that all three instances are currently marked as unhealthy.

Choose the Monitoring tab to review the metrics associated with your target group.
Notice the graphs for Healthy Hosts and Unhealthy Hosts. Currently the Healthy Hosts count is 0 and Unhealthy Hosts count is 3. This confirms that the issue is with the underlying EC2 instances and not with your Application load balancer.

To filter the results by time, select a time range using the Custom  option. To get a larger view of a single metric, select its graph.
 Caution: You might have to wait for about 5-7 minutes for CloudWatch to generate graphs for these metrics. Use the refresh  option as required.

 Task complete: You successfully analyzed the data from your load balancer resources to narrow down the issue and identified that the issue is with the underlying EC2 instances and not with your Application load balancer.

Task 3: Remediate the issue and validate the solution
In this task, you investigate the EC2 instances in detail to figure out the root cause of this issue. Once identified, you will fix the issue and validate the solution.

From the left navigation menu, expand the Instances section and choose Instances.
On the Instances page, you see three EC2 instances (Lab-Instance-01, Lab-Instance-02 and Lab-Instance-03) which are serving your application.

Check the Instance state columns for these instances to see if any of these instances are stopped or terminated.
All appears normal and all three instances are currently in  Running state. Now it’s time to investigate these instances one by one and review them in detail.

Selec the box next to Lab-Instance-01 instance to review its details.

On the Instance Summary page, scroll down and choose the Status and alarms tab.

The status checks for your instances appear normal and both System status checks and Instance status checks passed without any issues.

Choose the Monitoring tab to review metrics related to this EC2 instance.
All graphs appears normal and you don’t see any anomalies with any of the metrics.

To filter the results by time, select a time range using the Custom  option. To get a larger view of a single metric, select its graph.
 Caution: You might have to wait for about 5-7 minutes for CloudWatch to generate graphs for its metrics. Use the refresh  option as required.

Now review the security configurations for this EC2 instance.

Choose the Security tab to review the security details associated with this instance.
Reviewing the inbound rules for security group, you notice that the HTTP rule is configured with the wrong port. The correct port for HTTP is 80, however the instance is currently configured to use port 88.

Repeat the above steps for remaining two instances.
You notice same issue for remaining two instances, and conclude that all three instances are using incorrect security group rules. This is why your website is unable to serve external traffic.

Upon further investigation, it was found that one of the DevOps Engineer in your team made an improper change to the security group configuration during last night’s maintenance window and accidentally changed the port from 80 to 88.

Now that you have identified the root cause, its time to fix the issue and validate your application.

Select the link to the security group attached to the instance.

On the security group details page, scroll down and choose the Inbound rules tab.

Choose Edit inbound rules.

Change the HTTP port from 88 to 80 and choose Save rules.

 Expected Output:

 Inbound security group rules successfully modified on security group message is displayed on top of the screen.

Now verify if your application is accessible or not.

From the left navigation menu, expand the Load Balancing section and choose Target Groups.

On the Target groups page, select the link to myTargetGroupA target group associated with myAppLB-A load balancer.

On target group details page, scroll down and choose the Targets tab.

Reviewing the Health status column, you notice that all three instances are now marked as  healthy.

 Caution: You might have to wait for about 3-5 minutes and use the refresh  option as required.

Choose the Monitoring tab to review the metrics associated with your target group.

To filter the results by time, select a time range using the Custom  option. To get a larger view of a single metric, select its graph.

Review the graphs for Healthy Hosts and Unhealthy Hosts. Notice that both these graphs are now reversed and the Healthy Hosts count moved to 3 while the Unhealthy Hosts count moved to 0. This is a positive sign and indicates that the instances are passing health checks now.

 Caution: You might have to wait for about 5-7 minutes for CloudWatch to generate graphs for these metrics after change in the security group rules. Use the refresh  option as required.

Now that your instances are healthy, its time to review the accessibility of your application.

 Copy edit: Copy the value of ApplicationURL to the left of these instructions and paste it into a new browser tab.
This time your applications loads correctly and you see the following message on your website:

 Expected Output:

Application Website Running

Refresh  the page a few times and you notice that the message changes to:
 Expected Output:

Application Website Running 2

 Expected Output:

Application Website Running 3

Notice that every time you refresh the page, you see a different Instance ID in the message. This behavior confirms that the Application Load Balancer is also working as expected, and it is using the default routing algorithm (round robin) to route requests to different instances within the target groups based on the content of the application traffic.

 Task complete: You successfully investigated the EC2 instances to identify the root cause of this issue. You also remediated the issue and successfully verified that your application is working fine now.

Task 4: Monitoring improvements
As seen in the first scenario, the application is currently hosted on standalone EC2 instances. In such cases, if we make any changes to the application code or modify any instance level properties, we need to make these changes individually on every instance. This is not a best practice in production and we might face issues where accidental changes are made to our application resources. To avoid these issues, we will be using an EC2 launch template and an Auto Scaling group, in addition to the existing Application load balancer for our application.

In this task, you terminate the existing EC2 instances and implement an EC2 launch template to host your application website.

Switch back to the browser tab open to the AWS Management Console.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

From the left navigation menu, expand the Instances section and choose Instances.

On the Instances page:

Select the Lab-Instance-01 instance option.
Choose Instance state .
Choose Terminate instance.
On the Terminate instance? pop-up window, choose Terminate.
 Expected Output:

 Successfully terminated i-xxxxxx message is displayed on top of the screen.

Repeat the above steps for remaining two instances: Lab-Instance-02 and Lab-Instance-03.
 Caution: Do not proceed with next steps until all the three EC2 instances are successfully terminated. You can confirm that by reviewing the Instance state column. Use the refresh  option as required.

In the following steps, you apply an EC2 launch template and verify your application.

 Note: For simplicity, the EC2 launch template was already pre-created during the initial lab setup. review it now.

From the left navigation menu, expand the Instances section and choose Launch Templates.

Select the link to the Prod-Launch-Template and review its configuration.

Your application was already pre-built in this launch template via the User data section.

Now use EC2 Auto Scaling to launch your instances that uses the above launch template.

From the left navigation menu, expand the Auto Scaling section and choose Auto Scaling Groups.

On the Auto Scaling groups page, select the link to myAutoscalingGroup to view its details.

In the Group details section, choose Edit.

On the Group size pop-up window, configure the following:

Desired capacity: Enter 3.
Min desired capacity: Enter 2.
Max desired capacity: Enter 3.
 Warning: Using any other values apart from the ones provided above will cause failure and you will not be able to proceed further.

Choose Update.
At this point, the autoscaling group will start launching EC2 instances for your application.

On the details page for myAutoscalingGroup, choose the Activity tab.

Scroll down to the Activity history section and review the events.

Here, you see that autoscaling group launched three EC2 instances using the launch template.

Wait for a few minutes for all the instances to launch successfully. Review the Status column and wait until it changes to Successful. Use the refresh  option as required.
Now verify if all three instances were launched successfully by the Auto Scaling group.

From the left navigation menu, expand the Instances section and choose Instances.

On the Instances page, use the  Find instance by atttribute or tag search box and choose Instance state = running to filter the instances by its state.

Here, you see three instances with the name InstanceFromLT2 that were launched by the Auto Scaling group.

Review the Status check column for these three instances. Wait for few minutes until it shows  3/3 checks passed. Use the refresh  option as required.
Now verify your application to confirm if your website is running or not.

 Copy edit: Copy the value of FinalApplicationURL to the left of these instructions and paste it into a new browser tab.
Your application website loads correctly and you see the following message on your website:

 Expected Output:

Application Website Running Via LT

Refresh  the page a few times and you notice that the message changes to:
 Expected Output:

Application Website Running Via LT 2

 Expected Output:

Application Website Running Via LT 3

Notice that every time you refresh the page, you see a different Instance ID in the message. This behavior confirms that the Application Load Balancer is also working as expected.

 Task complete: You successfully terminated the existing EC2 instances and implemented an EC2 launch template to host your application website. You also verified that your application is working as expected with the new approach of using an EC2 launch template setup.

Scenario 2: EC2 instance are under-performing
In the previous task, you implemented the improvements after fixing the first scenario and the application instance launches are now controlled by a launch template that creates EC2 instances in a correct, consistent, and repeatable way.

In this scenario, you are notified that your application is under-performing and you are seeing increased CPU utilization on your EC2 instances that were launched using the launch template. You are tasked to investigate this increase in CPU utilization and remediate the issue.

Task 5: Collect and analyze data to identify the problem
You received another page that your application is now under-performing and your website is loading very slow.

In this task, you investigate the EC2 instances and use AWS CloudWatch to monitoring its metrics. You also review your EC2 launch template to verify if there are any anomalies in its configuration that might have caused your application to under-perform.

Your first step is to verify if your website is loading or not.

 Copy edit: Copy the value of FinalApplicationURL to the left of these instructions and paste it into a new browser tab.
At this point, you confirm that your website is loading fine and functions for all instances.

Next, you examine the EC2 Auto Scaling group to investigate further.

Switch back to the browser tab open to the AWS Management Console.

From the left navigation menu, expand the Auto Scaling section and choose Auto Scaling Groups.

On the Auto Scaling groups page, select the link to myAutoscalingGroup to view its details.

On the details page for myAutoscalingGroup, choose the Monitoring tab.

In the CloudWatch monitoring details section, choose the EC2 tab and locate the CPU Utilization (Percent) widget.

At this point, you see a bunch of metrics related to your EC2 instances that were launched by the Auto Scaling group.

 Caution: Use the refresh  option as required, to view the updated graphs after the launch of new instances via Auto Scaling group. You might have to wait for around 5 to 7 minutes to get the latest data from the graphs.

Here you notice that there has been a spike in the CPU Utilization for your instances, and this is probably the reason why your website is under-performing.

Now review the CPU Utilization for individual instances in detail.

From the left navigation menu, expand the Instances section and choose Instances.

On the Instances page, use the  Find instance by atttribute or tag search box and choose Instance state = running to filter the instances by its state.

Here you see three EC2 instances which are serving your application. These instances are named InstanceFromLT2.

Select one of the EC2 instance named InstanceFromLT2 to review its details.

On the Instance Summary page, scroll down and choose the Monitoring tab.

Here you notice that there has been a spike in the CPU Utilization for this instance.

 Caution: You might have to wait for about 3-5 minutes and use the refresh  option as required.

Repeat the above steps and review the remaining two instances.
As expected, there has been a spike in the CPU Utilization for the remaining two instances as well.

The above behavior confirms that high CPU Utilization on these instances is the reason why your application is under-performing and your website performance is impacted.

Now investigate further by reviewing the EC2 launch template that is being used by Auto Scaling group to see if there was any accidental change in any of its configuration.

From the left navigation menu, expand the Auto Scaling section and choose Auto Scaling Groups.

On the Auto Scaling groups page, select the link to myAutoscalingGroup to view its details.

Navigate to the Launch template section and review the launch template details.

Notice that the launch template is called Dev-Launch-Template. This seems weird since your application is currently running in production.

Choose the link under the Launch template option where it shows the Dev-Launch-Template.
At this point, you are redirected to the Launch templates page.

Select the link for Dev-Launch-Template to review its details.

Navigate to the Launch template version details section and choose the Instance details tab.

Here you notice that this launch template is using t3.nano as the instance type which is incorrect. Originally, your application was designed to use t3.medium for your production website and it has been accidentally reset to a smaller instance footprint which is struggling to meet your application needs.

 Task complete: You successfully investigated and identified that your EC2 instances were using an incorrect instance type and hence there was a spike in their CPU Utilization which resulted in your application under-performing.

Task 6: Remediate the issue and validate the solution
In this task, you update your autoscaling group to use an EC2 launch template with the correct instance type for your application.

However before doing that, you need to ensure that Auto Scaling group terminates the old instances with incorrect instance type.

From the left navigation menu, expand the Auto Scaling section and choose Auto Scaling Groups.

On the Auto Scaling groups page, select the link to myAutoscalingGroup to view its details.

In the Group details section, choose Edit.

On the Group size pop-up window, configure the following:

Desired capacity: Enter 0.
Min desired capacity: Enter 0.
Max desired capacity: Enter 0.
Choose Update.
At this point, the autoscaling group will start terminating EC2 instances with incorrect instance type.

On the details page for myAutoscalingGroup, choose the Activity tab.

Scroll down to the Activity history section and review the events.

Here, you see that autoscaling group is now terminating the three EC2 instances. Wait for a few minutes for all the instances to terminate successfully. Review the Status column and wait until it changes from WaitingForELBConnectionDraining to Successful. Use the refresh  option as required.

You can also navigate to the EC2 Dashboard to confirm the termination status for these instances.

 Caution: You might have to wait for around 7-10 minutes for all three instances to terminate successfully.

Once all three instances are successfully terminated, modify the Auto Scaling group to use the correct instance type for your application.

 Note: For simplicity, a new launch template named Prod-Launch-Template with the correct instance type is already created as part of initial lab setup. You can review it to confirm the correct instance type.

On the details page for myAutoscalingGroup, choose the Details tab.

Navigate to the Launch template section and choose Edit.

On the Edit myAutoscalingGroup page, locate the Launch template dropdown menu and change the launch template to Prod-Launch-Template.

Scroll down and choose Update.

 Expected Output:

 Auto Scaling group updated successfully message is displayed on top of the screen.

Finally modify the autoscaling group to launch new set of EC2 instances with the newly selected Prod-Launch-Template.

Navigate to the Group details section and choose Edit.

On the Group size pop-up window, configure the following:

Desired capacity: Enter 3.
Min desired capacity: Enter 2.
Max desired capacity: Enter 3.
Choose Update.
At this point, the autoscaling group will start launching EC2 instances for your application.

On the details page for myAutoscalingGroup, choose the Activity tab.

Scroll down to the Activity history section and review the events.

 Caution: Wait for a few minutes for all the instances to launch successfully. Review the Status column and wait until it changes to Successful. Use the refresh  option as required.

Navigate to the EC2 dashboard and verify that all three instances were launched successfully.

From the left navigation menu, expand the Instances section and choose Instances.

On the Instances page, use the  Find instance by atttribute or tag search box and choose Instance state = running to filter the instances by its state.

These instances should have a name tag of InstanceFromLT1. Review the Status check column, and wait until it shows  3/3 checks passed. Use the refresh  option as required.

Now verify your application to confirm if your website is running or not.

 Copy edit: Copy the value of FinalApplicationURL to the left of these instructions and paste it into a new browser tab.
Your application website loads correctly and you see the following message on your website:

 Expected Output:

Application Website Running Via Correct LT

Refresh  the page a few times and you notice that the message changes to:
 Expected Output:

Application Website Running Via Correct LT 2

 Expected Output:

Application Website Running Via Correct LT 3

Notice that every time you refresh the page, you see a different Instance ID in the message. This behavior confirms that the Application Load Balancer is also working as expected.

Now confirm if the correct instance type resolved the high CPU Utilization issue.

Switch back to the browser tab open to the AWS Management Console.

From the left navigation menu, expand the Auto Scaling section and choose Auto Scaling Groups.

On the Auto Scaling groups page, select the link to myAutoscalingGroup to view its details.

On the details page for myAutoscalingGroup, choose the Monitoring tab.

In the CloudWatch monitoring details section, choose the EC2 tab and locate the CPU Utilization (Percent) widget.

Here you notice that the CPU Utilization for your instances has improved and the percent utilization has dropped to a lower value.

 Caution: You might have to wait for about 5-7 minutes for CloudWatch to generate updated graphs for the CPU Utilization metric. Use the refresh  option as required.

Now review the CPU Utilization for individual instances as well.

From the left navigation menu, expand the Instances section and choose Instances.
On the Instances page, you see three EC2 instances which are serving your application. These instances are named InstanceFromLT1.

Select the link to one of the EC2 instance named InstanceFromLT1 to review its details.

On the Instance Summary page, scroll down and choose the Monitoring tab.

Here you notice that the CPU Utilization for this instance has improved and the percent utilization has dropped to a lower value.

 Caution: You might have to wait for about 5-7 minutes for CloudWatch to generate updated graphs for the CPU Utilization metric. Use the refresh  option as required.

Repeat the above steps and review the remaining two instances.
Similar to first instance, the CPU Utilization for the remaining two instances has also improved and the percent utilization has dropped to a lower value.

The above behavior confirms that changing the instance type to a correct value has resolved the performance issue and your website is showing better performance now.

 Task complete: You successfully updated your autoscaling group to use a new launch template with the correct instance type for your application and that fixed the performance issue for your website.

Monitoring and Observability Summary
Monitoring is an important part of maintaining the reliability, availability, and performance of your Amazon Elastic Compute Cloud (Amazon EC2) instances and your AWS solutions. You should collect monitoring data from all of the parts in your AWS solutions so that you can more easily debug a multi-point failure if one occurs. Before you start monitoring Amazon EC2, however, you should create a monitoring plan that should include:

What are your goals for monitoring?
What resources will you monitor?
How often will you monitor these resources?
What monitoring tools will you use?
Who will perform the monitoring tasks?
Who should be notified when something goes wrong?
After you have defined your monitoring goals and have created your monitoring plan, the next step is to establish a baseline for normal Amazon EC2 performance in your environment. You should measure Amazon EC2 performance at various times and under different load conditions. As you monitor Amazon EC2, you should store a history of monitoring data that you collect. You can compare current Amazon EC2 performance to this historical data to help you to identify normal performance patterns and performance anomalies, and devise methods to address them. For example, you can monitor CPU utilization, disk I/O, and network utilization for your EC2 instances. When performance falls outside your established baseline, you might need to reconfigure or optimize the instance to reduce CPU utilization, improve disk I/O, or reduce network traffic.

 Consider: Some of the useful monitoring resources are provided in the Additional Resources section. Review them as required.

Conclusion
 Congratulations! You now have successfully:

Described the methodology for troubleshooting Amazon EC2 issues.
Described the monitoring tools available and their functionality.
Implemented AWS monitoring tools for a given workload.
Troubleshot scenarios issues affecting EC2 workloads.

Additional Resources
Troubleshoot EC2 instances
Troubleshoot EC2 Windows instances
Troubleshooting resources
Automated and manual monitoring
Monitor the status of your instances
Monitor your instances using CloudWatch
Automate Amazon EC2 using EventBridge
Monitor memory and disk metrics for Amazon EC2 Linux instances
Log Amazon EC2 and Amazon EBS API calls with AWS CloudTrail
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.
