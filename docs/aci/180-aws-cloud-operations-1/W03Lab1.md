# Security Monitoring with Amazon CloudWatch Alarms

## Lab overview

Logging and monitoring are techniques implemented to achieve a common goal. They work together to help ensure that a system’s performance baselines and security guidelines are always met.

**Logging** refers to recording and storing data events as log files. Logs contain low-level details that can give you visibility into how your application or system performs under certain circumstances. From a security standpoint, logging helps security administrators identify red flags that are easily overlooked in their system.

**Monitoring** is the process of analyzing and collecting data to help ensure optimal performance. Monitoring helps detect unauthorized access and helps align your services’ usage with organizational security.

In this lab, you create an Amazon CloudWatch alarm that initiates when the Amazon Elastic Compute Cloud (Amazon EC2) instance exceeds a specific CPU utilization threshold. You create a subscription using Amazon Simple Notification Service (Amazon SNS) that sends an email to you if this alarm goes off. You log in to the Amazon EC2 instance and run a stress test command that causes the CPU utilization of the EC2 instance to reach 100 percent.

Services used in this lab
Amazon EC2 is a web service that provides secure, resizable compute capacity in the cloud.

Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.

Amazon SNS is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.

Objectives
By the end of this lab, you will be able to do the following:

Create an Amazon SNS notification.
Configure a CloudWatch alarm.
Stress test an EC2 instance.
Confirm that an Amazon SNS email was sent.
Create a CloudWatch dashboard.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, macOS X, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Scenario
In this lab, you have a preconfigured EC2 instance acting as a compromised web server. It has an attached AWS Identity and Access Management (IAM) role that you can use to connect through Session Manager, a capability of AWS Systems Manager.

You run a stress test command from within the malware instance. This test simulates a malicious actor gaining control of the EC2 instance and spiking the CPU utilization. CPU spiking has various possible causes, one of which is malware.

All backend components, such as Amazon EC2, IAM roles, and some Amazon Web Services (AWS) services, have been built in to the lab already.

Below is a diagram of the flow of the stress test from the EC2 instance to the Cloudwatch alarm, to the Amazon SNS email notification the the end user.

Architecture diagram showing architecture of the final state of the lab environment.

Duration
This lab requires approximately 45 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
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

## Task 1: Configuring Amazon SNS

In this task, you create an SNS topic and then create a subscription for the topic by using an email address. The topic will be able to send alerts to the email address that you associated with the Amazon SNS subscription.

On the AWS Management Console, in the search box, search for and choose Simple Notification Service.

On the left, choose the  button and choose Topics.

When the Topics page opens, choose Create topic.

On the Create topic page, in the Details section, configure the following options:

Type: Select Standard.
Name: Enter MyCwAlarm.
Choose Create topic.

On the MyCwAlarm details page, choose the Subscriptions tab, and then choose Create subscription.

On the Create subscription page, in the Details section, configure the following options:

Topic ARN: Leave the default option.
Protocol: From the dropdown list, choose Email.
Endpoint: Enter a valid email address that you can access.
Choose Create subscription.

In the Details section, the Status should be Pending confirmation. You should have received an AWS Notification - Subscription Confirmation email message at the email address that you provided in the previous step.

Open the email that you received with the Amazon SNS subscription notification, and choose Confirm subscription.

Go back to the console. In the left navigation pane, choose Subscriptions.

The Status should now be  Confirmed.

Task 2: Creating a CloudWatch alarm
In this task, you view some metrics and logs stored within CloudWatch. You then create a CloudWatch alarm to initiate and send an email to your SNS topic if the Web Server EC2 instance increases to more than 60 percent CPU utilization.

On the AWS Management Console, in the search box, search for and choose CloudWatch.

In the left navigation pane, choose the  Metrics dropdown list, and then choose All metrics.

 Note: CloudWatch usually takes 5–10 minutes after the creation of an EC2 instance to start fetching metric details.

On the Metrics page, choose EC2, and then choose Per-Instance Metrics.
From this page, you can view all the metrics being logged and the specific EC2 instance for the metrics.

Select the check box with CPUUtilization in the Metric name column for the Web Server EC2 instance.
 Note: The metrics may take some time to populate, you can select the refresh button periodically until you see the CPU Utilization. If you don’t see the CPU Utilization on the first page, you may need to select the second page of metrics.

When you select the check box, a graph of the CPU utilization metric displays at the top of the page. The graph is almost flat, near 0.

Expand the left navigation pane, choose the  Alarms dropdown list, and choose All alarms.
You will now create a metric alarm. A metric alarm watches a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. The alarm performs one or more actions based on the value of the metric or expression relative to a threshold over several time periods. The action then sends a notification to the SNS topic that you created earlier.

Choose Create alarm.

Choose Select metric.

Choose EC2, and then choose Per-Instance Metrics.

Select the check box with CPUUtilization as the Metric name for the Web Server instance name.

 Note: If you don’t see the CPU Utilization on the first page, you may need to select the second page of metrics.

Choose Select metric.

On the Specify metric and conditions page, configure the following options:

Metric

Metric name: Enter CPUUtilization
InstanceId: Leave the default option.
Statistic: Enter Average.
Period: From the dropdown list, choose 1 minute.
Conditions

Threshold type: Select Static.
Whenever CPUUtilization is…: Select Greater threshold.
than… Define the threshold value: Enter 60.
Choose Next.

On the Configure actions page, configure the following options:

Notification

Alarm state trigger: Select In alarm.
Send a notification to the following SNS topic: Select Select an existing SNS topic.
Send a notification to…: Choose the text box, and then choose MyCwAlarm.
Choose Next, and then configure the following options:

Name and description

Alarm name: Enter LabCPUUtilizationAlarm.
Alarm description - optional: Enter CloudWatch alarm for Web Server EC2 instance CPUUtilization.
Choose Next.

Review the Preview and create page, and then choose Create alarm.

Task 3: Testing the CloudWatch alarm
In this task, you log in to the Web Server EC2 instance and run a command that stresses the CPU load to 100 percent. This increase in CPU utilization activates the CloudWatch alarm, which causes Amazon SNS to send an email notification to the email address associated with the SNS topic.

Copy the EC2InstanceURL value to the left of these instructions, and paste it into a new browser tab.
This link connects you to the Web Server EC2 instance.

 Command: To increase the CPU load of the EC2 instance, run the following command:

sudo stress --cpu 10 -v --timeout 400s
The command should produce an output similar to the following:

 Expected output:


sh-4.2$ sudo stress --cpu 10 -v --timeout 400s
stress: info: [2504] dispatching hogs: 10 cpu, 0 io, 0 vm, 0 hdd
stress: dbug: [2504] using backoff sleep of 30000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 10 [2505] forked
stress: dbug: [2504] using backoff sleep of 27000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 9 [2506] forked
stress: dbug: [2504] using backoff sleep of 24000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 8 [2507] forked
stress: dbug: [2504] using backoff sleep of 21000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 7 [2508] forked
stress: dbug: [2504] using backoff sleep of 18000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 6 [2509] forked
stress: dbug: [2504] using backoff sleep of 15000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 5 [2510] forked
stress: dbug: [2504] using backoff sleep of 12000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 4 [2511] forked
stress: dbug: [2504] using backoff sleep of 9000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 3 [2512] forked
stress: dbug: [2504] using backoff sleep of 6000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 2 [2513] forked
stress: dbug: [2504] using backoff sleep of 3000us
stress: dbug: [2504] setting timeout to 400s
stress: dbug: [2504] --> hogcpu worker 1 [2514] forked
 Additional information: When you ran the sudo stress --cpu 10 -v --timeout 400s command within the AWS Command Line Interface (AWS CLI), the output shows that 10 CPUs were at 100 percent load over the period of 400 seconds. When 400 seconds passes, it will drop down to 0 percent.

 Note: This command runs for 400 seconds, loads the CPU to 100 percent, and then decreases the CPU to 0 percent after the allotted time.

Copy the EC2InstanceURL value to the left of these instructions, and paste it into a new browser tab to open a second terminal for the Web Server instance.

 Command: In the new terminal, run the following command:


top
 Expected output:


top - 20:57:39 up  1:18,  0 users,  load average: 6.45, 1.85, 0.64
Tasks: 107 total,  12 running,  57 sleeping,   0 stopped,   0 zombie
%Cpu(s): 87.5 us,  0.2 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si, 12.3 st
KiB Mem :   966816 total,   356800 free,   127208 used,   482808 buff/cache
KiB Swap:        0 total,        0 free,        0 used.   691416 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
31540 root      20   0    7580    100      0 R  17.3  0.0   0:10.19 stress
31541 root      20   0    7580    100      0 R  17.3  0.0   0:10.19 stress
31542 root      20   0    7580    100      0 R  17.3  0.0   0:10.19 stress
31543 root      20   0    7580    100      0 R  17.3  0.0   0:10.19 stress
31545 root      20   0    7580    100      0 R  17.3  0.0   0:10.25 stress
31536 root      20   0    7580    100      0 R  16.9  0.0   0:10.18 stress
31537 root      20   0    7580    100      0 R  16.9  0.0   0:10.18 stress
31538 root      20   0    7580    100      0 R  16.9  0.0   0:10.18 stress
31539 root      20   0    7580    100      0 R  16.9  0.0   0:10.18 stress
31544 root      20   0    7580    100      0 R  16.9  0.0   0:10.18 stress
    1 root      20   0  123512   5436   3924 S   0.0  0.6   0:01.40 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd
    4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:0H
    6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_wq
    7 root      20   0       0      0      0 S   0.0  0.0   0:00.05 ksoftirqd/0
    8 root      20   0       0      0      0 I   0.0  0.0   0:00.18 rcu_sched
    9 root      20   0       0      0      0 I   0.0  0.0   0:00.00 rcu_bh
   10 root      rt   0       0      0      0 S   0.0  0.0   0:00.00 migration/0
   11 root      rt   0       0      0      0 S   0.0  0.0   0:00.00 watchdog/0
   12 root      20   0       0      0      0 S   0.0  0.0   0:00.
This command shows the live CPU usage.

Navigate back to the console where you have the CloudWatch Alarms page open.

Choose LabCPUUtilizationAlarm.

Monitor the graph while choosing the  refresh button every 1 minute until the alarm state is In alarm.

 Note: It takes a few minutes for the alarm status to change to In alarm and for an email to send.

On the graph, you can see where CPUUtilization has increased above the 60 percent threshold.

Navigate to your email inbox for the email address that you used to configure the Amazon SNS subscription. You should see a new email notification from AWS Notifications.
Task 4: Creating a CloudWatch dashboard
In this task, you create a CloudWatch dashboard by using the same CPUUtilization metrics that you have used throughout this lab.

CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view. With CloudWatch dashboards, you can even monitor resources that are spread across different Regions. You can use CloudWatch dashboards to create customized views of the metrics and alarms for your AWS resources.

On the CloudWatch console, in the left navigation pane, choose Dashboards.

Choose Create dashboard.

For Dashboard name, enter LabEC2Dashboard and then choose Create dashboard.

Select Line.

Select Metrics and then select Next.

Choose EC2, and then choose Per-Instance Metrics.

Select the check box with CPUUtilization under the Metric name column for the Web Server EC2 instance.

 Note: If you don’t see the CPU Utilization on the first page, you may need to select the second page of metrics.

Choose Create widget.
Now you have created a quick-access shortcut to view the CPUUtilization metric for the Web Server instance.

 Congratulations! You have now created a CloudWatch alarm that activates when the Web Server instance exceeds a specific CPU utilization threshold. You created a subscription by using Amazon SNS that sent an email to you if this alarm goes off. You logged in to the EC2 instance and ran a stress test command that spiked the EC2 instance to 100 percent CPU utilization.

This test simulated what could happen if a malicious actor were to gain control of an EC2 instance and spike CPU utilization. CPU spiking has various possible causes, one of which is malware.

Conclusion
 Congratulations! You now have successfully done the following:

Created an Amazon SNS notification
Configured a CloudWatch alarm
Stress tested an EC2 instance
Confirmed that an Amazon SNS email was sent
Created a CloudWatch dashboard
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.