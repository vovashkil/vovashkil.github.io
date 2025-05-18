# Week 6: Logging and Scaling: Monitoring and Amazon CloudWatch

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## Logging and Monitoring in AWS

### Pre-assessment

#### Which AWS service can you use to monitor API calls made by a user, role, or AWS service?

* AWS CloudTrail

Wrong answers:

* Amazon CloudWatch
* AWS X-Ray
* Amazon Simple Notification Service (Amazon SNS)

##### Explanation

AWS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs.

The other options are incorrect for the following reasons:

* You can use CloudWatch to collect metrics and store logs. You can use CloudWatch to monitor a near real-time stream of system events. CloudWatch doesn't monitor API calls.
* You can use X-Ray to analyze and debug distributed applications in both development and production environments. X-Ray alone doesn't monitor API calls.
* Amazon SNS is a managed service that provides message delivery from publishers to subscribers. It doesn't monitor API calls.

#### What is an advantage of enabling detailed monitoring for Amazon EC2?

* Metrics are published in 1-minute intervals.

Wrong answers:

* Metrics are published in 5-minute intervals.
* It is provided at no additional charge.
* Memory usage metrics are provided by default.

##### Explanation

Amazon EC2 detailed monitoring provides more frequent metrics, published at 1-minute intervals, instead of the 5-minute intervals used in Amazon EC2 basic monitoring. It also incurs charges. To use it for an AWS service, you must choose to activate it.

The other options are incorrect for the following reasons:

* Basic monitoring publishes metrics in 5-minute intervals.
* Detailed monitoring incur charges.
* You need to create a custom metric to monitor memory usage.  

#### Which AWS service can you use to display custom metrics about AWS services and custom applications that you use?

* Amazon CloudWatch

Wrong answers:

* AWS CloudTrail
* AWS X-Ray
* Amazon Simple Notification Service (Amazon SNS)

##### Explanation

Amazon CloudWatch monitors your AWS resources and the applications that you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables that you can measure for your resources and applications.

The CloudWatch home page automatically displays metrics about every AWS service that you use. You can additionally create custom dashboards to display metrics about your custom applications and display custom collections of metrics that you choose.

The other options are incorrect for the following reasons:

* CloudTrail is used to monitor API calls.
* You can use X-Ray to analyze and debug distributed applications in both development and production environments. X-Ray doesn't display custom metrics.
* Amazon SNS is a managed service that provides message delivery from publishers to subscribers. It doesn't display custom metrics.

## Logging Overview

### Log files

Log files are software-generated files that contain information about the operations, activities, and usage patterns of an application, server, or IT system.

* Log files contain a historical record of processes, events, and messages.
* Timestamps show when each logged action happened, providing a detailed timeline of system activity.
* Log files help identify issues by providing a record of all system events leading up to any incidents.
* By reviewing log files, you can reconstruct system activity and understand what went wrong if problems occur.

### Why logging is important

Comprehensive logging and the ability to analyze logs are critical in the cloud to ensure optimal performance, security, compliance, and cost management. Logs provide visibility into cloud operations that isn't possible otherwise.

Companies can aggregate logs from their services, applications, servers, and other resources into a central cloud logging system. This makes logging and monitoring easier to manage. Cloud logging services provide tools to search, analyze, and visualize logs. You can use these services to identify trends and anomalies, extract metrics, and obtain other insights.

#### Troubleshooting issues

You can use logs to debug issues with your cloud infrastructure, applications, and resources. When something goes wrong, logs provide insight into what happened. 

#### Security and compliance

Logs record user activity and administrator actions. This is important for detecting potential security breaches and demonstrating compliance with regulations.

#### Performance monitoring

Logs contain data, like resource utilization, that can be used to monitor performance and availability of cloud services. You can examine log timestamps to identify slow or inefficient operations.

#### Billing audits

Usage logs can be used to verify the accuracy of cloud bills and optimize costs. You can use logs to analyze resource consumption and spending over time.

#### Incident response

Detailed activity logs can help investigate incidents like outages or hacks. They provide an audit trail to understand what went wrong and how.

#### Auto scaling

Usage data from logs permits services like auto scaling to activate based on changes in demand. Logs help correlate usage patterns with ideal resource levels.

#### Analytics

Log analysis can provide insights into usage patterns, operational trends, and other metrics that help optimize the cloud environment.

### Types of logs

1. **Event logs**

    An event log is a high-level log that records system activity data to provide an audit trail for troubleshooting issues. Event logs are essential to understand the behavior of complex systems, particularly in the case of applications with little user interaction. For example, in networks, event logs record network traffic, access, and usage.

2. **System logs**

    A system log records operating system events, such as system changes, startup messages, errors, warnings, and unexpected shutdowns.

3. **Access logs**

    An access log records the list of all requests for individual files that people or applications request from a system. It includes information about user authentication, who requested a particular system file, when they asked for it, and other associated information.

4. **Server logs**

    A server log is a log file that a server automatically creates and maintains. It contains a list of activities that the server performs, such as the number of page requests, client IP addresses, types of requests, and so on.

5. **Change logs**

    A change log is a file that contains a chronological record of changes made to the software. For example, it might log changes between different versions of an application or log configuration changes to a system. Change logs are created by people working on a software project.

6. **Other types of logs**

    Depending on the use case, there are other types of log files, such as the following:

    * Availability logs that track system performance and availability
    * Resources logs that deliver information on connectivity issues
    * Threat logs that contain information regarding suspicious network profiles

### Amazon CloudWatch Logs

The Amazon CloudWatch Logs service helps you to collect and store logs from your resources, applications, and services in near real time. CloudWatch Logs supports logs from many AWS services and on-premises sources. Custom applications on Amazon EC2 instances or on-premises can also send their logs to CloudWatch Logs by using the CloudWatch Logs agent.

The following are three main categories of logs:

* **Logs published by AWS services** – Many AWS services publish logs to CloudWatch, including Amazon API Gateway, AWS Lambda, AWS CloudTrail, and many others.
* **Vended logs** – These are published by AWS services on your behalf, and are available at volume discount pricing.
* **Custom logs** – These are logs from your own application and on-premises resources, and from other clouds.

#### Vended logs and logs published by AWS services

The main difference between vended logs and logs published by AWS services to CloudWatch Logs is how they are priced.

The following are some key points to keep in mind when comparing vended logs and standard logs published by AWS services:

* Vended logs are logs that certain AWS services can publish directly to Amazon Simple Storage Service (Amazon S3) or Amazon Data Firehose, in addition to CloudWatch Logs. These logs have a per-GB volume pricing model.
* Standard logs published by AWS services to CloudWatch Logs have limits on the number of log events ingested per month, as well as data retention periods.
* To publish standard logs to CloudWatch Logs, no additional configuration is needed. For vended logs, you need to enable the specific AWS service to publish logs to other services like Amazon S3.

Each log type has its own advantages and disadvantages, and the best choice for your organization will depend on your specific needs and use cases. For example, vended logs and logs published by AWS services are widely used and provide a lot of useful information. But they might not capture all the data you need for your specific use cases. However, you can use custom logs to capture precisely the data that you need, but they require more development effort to create and maintain.

#### Custom logs

AWS services can publish some logs to CloudWatch by default. However, there might be instances where you need to collect data from additional logs that aren't provided by default. In these cases, you can push custom logs to CloudWatch by using the unified CloudWatch agent or the API. With custom logs, you can define and collect your own log data from your resources and applications running in AWS, on-premises, or in other clouds.

Custom logs are log files that are generated by your own applications and services that are running on Amazon EC2 instances or elsewhere. These could be application logs, server logs, database logs, or other types of logs. You can use CloudWatch Logs to monitor, store, and access your custom log files, just like you do for standard log files from AWS services.

Here are some key things that you can do with custom logs in CloudWatch Logs:

* Centralize all your log data from various sources like applications, servers, and services in a single service for convenient management.
* Query and analyze log data using CloudWatch Logs Insights. This makes it possible for you to search logs, detect patterns, and debug issues.
* Configure alarms and notifications on metrics generated from your logs, so that you are alerted of issues or changes.
* Archive and retain logs for as long as you want.
* Securely monitor and troubleshoot logs from production systems without directly accessing servers.
* Associate AWS Identity and Access Management (IAM) roles and policies to control access to logs from various sources.

**Note**: To manage costs, logs should be stored and retained according to need by using features like log expiration policies. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

### CloudWatch Logs concepts

#### Log events

A log event is a record of some activity recorded by the application or resource being monitored. The log event record that CloudWatch Logs understands contains two properties: the timestamp of when the event occurred and the raw event message. Event messages must be UTF-8 encoded.

The following example shows the raw event message from Apache in a structured logging format. You can store log events in JSON format to make it easier to use log analytics and to extract metrics from your logs.

```json
{
    "time": "2022-11-01T16:00:00.000Z",
    "remoteIP": "10.0.155.113",
    "host": "10.0.53.21",
    "request": "/index.php",
    "query": "",
    "method": "GET",
    "status": "200",
    "userAgent": "ELB-HealthChecker/2.0",
    "referrer": "-"
}
```

#### Log streams

A log stream is a sequence of log events that share the same source. More specifically, a log stream is generally intended to represent the sequence of events coming from the application instance or resource being monitored.

In this example, the log stream is associated with an Apache access log on a specific host.

![Log streams screenshot](./images/W06Img010LoggingLogStreams.png)

#### Log groups

Log groups define groups of log streams that share the same retention, monitoring, and access control settings. Each log stream must belong to one log group.

The previous log stream example shows a list of log events from an Apache log stream on a specific host. But this image shows log streams contained within a log group. In this example, the log group contains multiple log streams from Apache on every host that runs a single application.

![Log groups screenshot](./images/W06Img012LoggingLogGroups.png)

#### Metric filters

You can use metric filters to extract metric observations from ingested events and transform them to data points in a CloudWatch metric. Metric filters are assigned to log groups, and all filters assigned to a log group are applied to their log streams.

This example shows a search for status codes beginning with a 2, resulting in a list of successful page loads. The name of the field in the filter pattern can be defined because the logs are structured using JSON.

![Metric filters screenshot](./images/W06Img014LoggingMetricFilters.png)

Metric filters are often useful to extract metrics from logs where there might be useful technical or business metrics that have only been exposed in logs. For example, if you had a payment gateway and your logs recorded whether or not the transaction was successful, you could use a metric filter to expose this as a metric and alert you if there is an anomalous amount of failures.

### Monitoring with CloudWatch

Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights that you can use to monitor your applications, respond to system-wide performance changes, and optimize resource utilization. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events. You get a unified view of operational health and can get visibility of your AWS resources, applications, and services running both on AWS and on premises.

For example, you can use CloudWatch to do the following:

* Integrate log files from over 70 AWS services.
* Automatically publish metrics, including custom metrics, for deep log analysis.
* Set alarms and automate actions based on predefined thresholds.
* Explore, analyze, and visualize logs to troubleshoot operational problems.
* Create dashboards to view metrics and alarms across multiple resources.

#### CloudWatch metric concepts

##### Metrics

Metrics are data about the performance of your systems that are presented as time-ordered sets of data points. Think of a metric as a variable to monitor.

By default, many services provide metrics for resources, such as Amazon EC2 instances, Amazon Elastic Block Store (Amazon EBS) volumes, and Amazon Relational Database Service (Amazon RDS) DB instances. You can also enable detailed monitoring for some resources, such as your EC2 instances, or publish your own custom application metrics. CloudWatch can load all the metrics in your account for searching, graphing, and alarms.

The console displays a custom namespace named CWAgent that includes 83 metrics. Namespaces are shown for many AWS resources.

##### Namespaces

A namespace is a container for CloudWatch metrics. Metrics in different namespaces are isolated from each other, so that metrics from different applications are not mistakenly aggregated into the same statistics.

The default namespace for metrics collected by the CloudWatch agent is CWAgent.

##### Dimensions

A dimension is part of the identity of a metric. It consists of a name and a value. You can assign up to 30 dimensions to a metric. Think of dimensions as categories for the unique characteristics that describe a metric.

Dimensions help you design a structure for your statistics plan. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name-value pair to one of your metrics, you are creating a new variation of that metric.

##### Percentiles

A percentile indicates the relative standing of a value in a dataset. Percentiles are often used to isolate anomalies. Using percentiles can uncover a bad user experience that an average metric would not.

For example, monitoring the average user page-load time can hide anomalies, and monitoring the maximum can skew the results. Monitoring the 99.7 percentile might reveal that 99.7 percent of page loads take less than 24 seconds. This means that some percentage of users are experiencing unusually long load times.

#### CloudWatch monitoring example

In the following diagram, AWS resources publish default and custom metrics to CloudWatch. In response to the data, a CloudWatch alarm sends an Amazon Simple Notification Service (Amazon SNS) email notification and initiates Amazon EC2 Auto Scaling. Metrics and data visualization are sent to the AWS Management Console and a third-party service.

![CloudWatch monitoring example](./images/W06Img016LoggingCloudWatch.png)

1. **Metrics**

    Many services offer standard metrics available to stream to CloudWatch. For example, CPU utilization is a standard Amazon EC2 metric.

    However, memory utilization is not visible from the hypervisor, so it is not visible as a standard metric. In this case, you can create a custom metric to view memory utilization data.

2. **CloudWatch alarm**

    You can use CloudWatch alarms to initiate actions based on the metric values. A metric alarm watches a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. The alarm performs one or more actions based on the value of the metric or expression relative to a threshold over a number of time periods. For example, the action can be an Amazon EC2 action, an auto scaling action, or a notification sent to an Amazon SNS topic.

3. **Amazon SNS email notification**

    CloudWatch alarms can send data to an Amazon SNS topic. The topic can then send an email, text message, or push notification to users who subscribe to the topic.

4. **Amazon EC2 Auto Scaling**

    You can configure CloudWatch alarm actions to initiate an Amazon EC2 Auto Scaling policy when certain criteria are met. For example, you can use an alarm to launch a new instance if CPU utilization in an Auto Scaling group is greater than 80 percent.

5. **Statistics and data visualization**

    Statistics are metric data aggregations over specified periods of time. CloudWatch provides statistics based on the metric data points provided by your custom data or provided by other AWS services to CloudWatch. The available statistic types are Minimum, Maximum, Sum, Average, and SampleCount.

    You can use metrics to calculate statistics and then present the data graphically in the CloudWatch console. CloudWatch monitoring also integrates with several third-party tools, such as Splunk.

For more information, see [Amazon CloudWatch Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) in the *Amazon CloudWatch User Guide*.

#### Basic monitoring and detailed monitoring

CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. Detailed monitoring is only offered by some services, and options differ based on the services that offer it.

##### Basic monitoring

* This default monitoring option is enabled automatically when you start using many AWS services, such as EC2 instances, EBS volumes, and Elastic Load Balancing (ELB).
* Metrics for EC2 instances are collected and aggregated at 5-minute intervals.
* This provides basic system-level metrics like CPU utilization, network in/out, and disk reads/writes.
* Basic monitoring is offered at no additional charge.

##### Detailed monitoring

* This optional paid monitoring mode is available for some services, including Amazon API Gateway, Amazon EC2, and Amazon S3.
* When detailed monitoring is enabled for EC2 instances, metrics are collected and aggregated with 1-minute metric granularity.
* This provides more granular metrics compared to basic monitoring, for example, metrics per CPU core and Amazon EBS bandwidth used for Amazon EC2.
* Detailed monitoring can be enabled by a check box for supported resources.
* This mode is useful for auto scaling configurations and closely monitoring performance.
* Detailed monitoring is charged per month for each resource monitored, with different costs depending on the AWS service.

For more information, see [Basic Monitoring and Detailed Monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html) in the Amazon CloudWatch User Guide.

#### Cost considerations for CloudWatch

Although it might be critical to enable CloudWatch monitoring on all your resources, there are additional charges when enabling detailed monitoring. Basic monitoring for EC2 instances provides metrics at 5-minute intervals, and detailed monitoring for EC2 instances provides that information at 1-minute intervals for an additional charge. This might be important for production workloads, but not as important for nonproduction. Note that some nonproduction workloads might need detailed monitoring for testing, but they should be reviewed to determine if detailed monitoring can be disabled after tests are completed.

CloudWatch Logs can incur significant storage costs if left unchecked, particularly when you collect virtual private cloud (VPC) flow logs or application-level logs. Consider creating a retention policy for your logs to archive to Amazon S3 so that you only use CloudWatch Logs to maintain a recent history.

The retention should be based on your operational needs. For example, if you only review the last two weeks of logs when an incident occurs and rarely review logs older than the last 30 days, it might make sense to archive anything over 30 days to Amazon S3. This way, you are not paying for years of logs in CloudWatch Logs when you might not actually refer to them.

## Determining a Monitoring Strategy

### Creating a monitoring plan

Before you start building in AWS, it's a good idea to consider how you will monitor your cloud environment. A thoughtful monitoring strategy provides essential visibility and diagnostics that allow you to optimize, secure, and automate your AWS workloads. When you create a monitoring plan, you determine the strategies, tools, and processes that you will use to observe and track the performance and availability of cloud-based resources like servers, applications, and services.

* What are your goals for monitoring?
* Which resources will you monitor?
* How often will you monitor these resources?
* Which monitoring tools will you use?
* Who will perform the monitoring tasks?
* Who should be notified when something goes wrong?

#### Goals for monitoring

* Customer experience
* Performance and cost
* Trends
* Troubleshooting and remediation

#### Resources to monitor

* Applications
* End users abd access
* Operating systems
* AWS foundational services
  * Compute
  * Storage
  * Databases
  * Networking
* AWS Global Infrastructure
  * AWS Regions
  * Availability Zones
  * Edge locations

#### How often to monitor the resources?

* Continuous monitoring
* Alerts and notifications
* Stored logs

#### Which monitoring tools to use?

* Amazon CloudWatch
* AWS CloudTrail
* AWS X-Ray
* Service specific features

#### Who will perform the monitoring tasks?

* Operations
* Developers and engineers
* Management

#### Who and how should be notified when something goes wrong?

* Alert: Take action
* Inform: Email or dashboard

## Establishing a baseline with Amazon EC2 Metrics

### Amazon EC2 metrics

Amazon EC2 provides a wide range of performance metrics. You can use these metrics to monitor and analyze the performance of your EC2 instances and the underlying infrastructure, and establish a baseline for normal Amazon EC2 performance in your environment.

* CPU utilization
* Network In and Out
* Disk read and Write
* Status checks
  * System status
  * Instance status
  * Attached EBS status
* Memory Usage - CloudWatch custom metrics
* Disk space utilization
* Auto scaling metrics
  * Desired capacity
  * Scaling policies
  * Instances in-service
* Custom metrics

### Determine a baseline

After you define your monitoring goals and create your monitoring plan, you can establish a baseline for normal Amazon EC2 performance in your environment. It is a good practice to measure Amazon EC2 performance at various times and under different load conditions. And then, store a history of this data. You can then compare current Amazon EC2 performance to the historical data to help you identify performance patterns and anomalies, and develop methods to address them.

With a baseline in place, you can easily identify anomalies, and understand what's normal for your specific application. For example, let's say your baseline CPU utilization usually hovers around 50 percent, but suddenly spikes to 90 percent. This is a clear sign of increased demand that can initiate an automatic scaling action.

### Amazon EC2 metrics to monitor

Amazon EC2 sends metrics to Amazon CloudWatch. You can use the AWS Management Console, the AWS CLI, or an API to list the metrics that Amazon EC2 sends to CloudWatch. By default, each data point covers the 5 minutes that follow the start time of activity for the instance. If you've enabled detailed monitoring, each data point covers the next minute of activity from the start time. Note that for the Minimum, Maximum, and Average statistics, the minimum granularity for the metrics that Amazon EC2 provides is 1 minute.

#### Instance metrics

Amazon EC2 instance metrics are in the **AWS/EC2** namespace.

* CPUUtilization
* DiskReadOps
* DiskWriteOps
* DiskReadBytes
* DiskWriteBytes
* NetworkIn
* NetworkOut
* NetworkPacketsIn
* NetworkPacketsOut

#### Amazon EC2 Auto Scaling group metrics

Amazon EC2 Auto Scaling metrics that collect information about Auto Scaling groups are in the **AWS/AutoScaling** namespace. Amazon EC2 instance metrics that collect CPU and other usage data from Auto Scaling instances are in the **AWS/EC2** namespace.

The Amazon EC2 Auto Scaling console displays a series of graphs for the group metrics and the aggregated instance metrics for the group. Depending on your needs, you might prefer to access data for your Auto Scaling groups and instances from Amazon CloudWatch instead of the Amazon EC2 Auto Scaling console.

With the following Auto Scaling group metrics, you get nearly continuous visibility into the history of your Auto Scaling group, such as changes in the size of the group over time. The following metrics are reported if metrics collection is enabled.

| Metric | Description |
| ------ | ----------- |
| GroupMinSize | This shows the minimum size of the Auto Scaling group. |
| GroupMaxSize  | This shows the maximum size of the Auto Scaling group. |
| GroupDesiredCapacity | This shows the number of instances that the Auto Scaling group attempts to maintain. |
| GroupInServiceInstances | This shows the number of instances that are running as part of the Auto Scaling group. This metric does not include instances that are pending or terminating. |
| GroupPendingInstances | This shows the number of instances that are pending. A pending instance is not yet in service. This metric does not include instances that are in service or terminating. |
| GroupStandbyInstances | This shows the number of instances that are in a Standby state. Instances in this state are still running but are not actively in service. |
| GroupTerminatingInstances | This shows the number of instances that are in the process of terminating. This metric does not include instances that are in service or pending. |
| GroupTotalInstances | This shows the total number of instances in the Auto Scaling group. This metric identifies the number of instances that are in service, pending, and terminating. |

#### Status checks for your instance

With instance status monitoring, you can quickly determine whether Amazon EC2 has detected any problems that might prevent your instances from running applications. Amazon EC2 performs automated checks on every running EC2 instance to identify hardware and software issues. You can view the results of these status checks to identify specific and detectable problems. The event status data augments the information that Amazon EC2 already provides about the state of each instance (such as pending, running, and stopping) and the utilization metrics that CloudWatch monitors (CPU utilization, network traffic, and disk activity).

Status checks are performed every minute, returning a pass or fail status. If all checks pass, the overall status of the instance is *OK*. If one or more checks fail, the overall status is *impaired*. Status checks are built into Amazon EC2, so they cannot be disabled or deleted.

When a status check fails, the corresponding CloudWatch metric for status checks is incremented. You can use these metrics to create CloudWatch alarms that are invoked based on the result of the status checks. For example, you can create an alarm to warn you if status checks fail on a specific instance.

##### Status check metrics

The AWS/EC2 namespace includes the following status check metrics.

| Metric | Description |
| ------ | ----------- |
| StatusCheckFailed | This metric reports whether the instance has passed both the instance status check and the system status check in the last minute.\\It can be either 0 (passed) or 1 (failed).\\By default, this metric is available at a 1-minute frequency at no charge. |
| StatusCheckFailed_Instance | This metric reports whether the instance has passed the instance status check in the last minute.\\It can be either 0 (passed) or 1 (failed).\\By default, this metric is available at a 1-minute frequency at no charge. |
| StatusCheckFailed_System | This metric reports whether the instance has passed the system status check in the last minute.\\It can be either 0 (passed) or 1 (failed).\\By default, this metric is available at a 1-minute frequency at no charge. |
| StatusCheckFailed_AttachedEBS | This metric reports whether the instance has passed the attached EBS status check in the last minute.\\It can be either 0 (passed) or 1 (failed).\\By default, this metric is available at a 1-minute frequency at no charge. |

##### Types of status checks

* **System status checks**

    System status checks monitor the AWS systems on which your instance runs. These checks detect underlying problems with your instance that require AWS involvement to repair. When a system status check fails, you can choose to wait for AWS to fix the issue, or you can resolve it yourself.

    For instances backed by Amazon EBS, you can stop and start the instance yourself, which in most cases results in the instance being migrated to a new host. For Linux instances backed by instance store, you can terminate and replace the instance. For Windows instances, the root volume must be an Amazon EBS volume; instance store is not supported for the root volume. Note that instance store volumes are ephemeral, and all data is lost when the instance is stopped.

    The following are examples of problems that can cause system status checks to fail:

  * Loss of network connectivity
  * Loss of system power
  * Software issues on the physical host
  * Hardware issues on the physical host that impact network reachability

* **Instance status checks**

    Instance status checks monitor the software and network configuration of your individual instance. Amazon EC2 checks the health of the instance by sending an Address Resolution Protocol (ARP) request to the network interface (NIC). These checks detect problems that require your involvement to repair. When an instance status check fails, you typically must address the problem yourself (for example, by rebooting the instance or by making instance configuration changes).

    The following are examples of problems that can cause instance status checks to fail:

  * Failed system status checks
  * Incorrect networking or startup configuration
  * Exhausted memory
  * Corrupted file system
  * Incompatible kernel

* **Attached EBS status checks**

    Attached EBS status checks monitor if the EBS volumes attached to an instance are reachable and able to complete I/O operations. The **StatusCheckFailed_AttachedEBS** metric is a binary value that indicates impairment if one or more of the EBS volumes attached to the instance are unable to complete I/O operations.

    These status checks detect underlying issues with the compute or Amazon EBS infrastructure. When the attached EBS status check metric fails, you can either wait for AWS to resolve the issue, or you can take actions, such as replacing the affected volumes or stopping and restarting the instance.

    The following are examples of issues that can cause attached EBS status checks to fail:

  * Hardware or software issues on the storage subsystems underlying the EBS volumes
  * Hardware issues on the physical host that impact reachability of the EBS volumes
  * Connectivity issues between the instance and EBS volumes

    You can use the **StatusCheckFailed_AttachedEBS** metric to help improve the resilience of your workload. You can use this metric to create Amazon CloudWatch alarms that are invoked based on the result of the status check. For example, you could fail over to a secondary instance or Availability Zone when you detect a prolonged impact.

## Monitoring with the CloudWatch Agent

### Monitoring with and without an agent

When using CloudWatch to monitor your Amazon EC2 instances, agentless monitoring is limited to collecting basic OS-level metrics like CPU, network, and disk usage.

You can use the unified CloudWatch agent to collect system-level metrics from EC2 instances and on-premises servers and send them to CloudWatch. The CloudWatch agent is a lightweight, open-source software component that you can install on EC2 instances and on-premises servers. The agent can run on supported Linux, Windows Server, or macOS operating systems.

Because the agent can collect metrics at the system level, it can provide greater insight and granular detail than using CloudWatch without an agent.

#### Agentless monitoring

By default, Amazon EC2 provides metrics that measure CPU, disk, and network performance. This includes the following metrics:

* CPU utilization
* Whether the instance has passed the instance status check and the system status check in the last minute
* Bytes read from and written to all instance store volumes available to the instance
* Completed read and write operations to instance store volumes in a specified period of time
* The number of bytes sent in and out by the instance on all network interfaces
* The number of packets received by and sent from the instance on all network interfaces

Additionally, agentless monitoring can provide volume read and write metrics for EBS volumes attached to EC2 instances.

#### CloudWatch agent

You can install the CloudWatch agent on EC2 instances and on-premises servers running supported Linux, Windows Server, or macOS operating systems.

On a server running Windows Server, the agent collects metrics associated with the counters in Windows Performance Monitor.

On Linux servers and macOS computers, metrics collected by the agent include the following:

* CPU usage, such as how long it spends running various processes
* Disk space and disk read and write data
* Packets queued and dropped for various reasons
* Memory usage, such as the amount of memory being used during a period of time
* Bytes and packets received and sent and errors detected by the network interface
* TCP and UDP connection statuses
* Process statuses
* Swap space usage

If you install the CloudWatch agent on an EC2 instance, the metrics it collects are in addition to the agentless metrics enabled by default on EC2 instances. The agent can also send traces to AWS X-Ray.

For more information, see [Metrics Collected by the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html) in the Amazon CloudWatch User Guide.

### When to use a CloudWatch agent

In some situations, it's necessary to use a CloudWatch agent to collect the metrics that you need from a particular service or environment. The following are some examples of things that the CloudWatch agent can do that wouldn't be possible with standard EC2 monitoring with CloudWatch.

* The agent can collect log files, such as Apache logs, application logs, and system logs.
* The agent allows you to specify custom metrics and logs that you want to collect from services.
* The agent can collect metrics and logs from servers in non-AWS environments, such as hybrid environments and on-premises data centers.
* The agent integrates with Docker and Kubernetes, and can collect metrics from Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS).

![CloudWatch agent diagram](./images/W06Img018LoggingCloudWatchAgentUse.png)

This diagram shows how the CloudWatch agent collects information, and then sends metrics to CloudWatch and logs to CloudWatch Logs. In this example, the agent is installed on an EC2 instance and an on-premises server. The EC2 instance has an IAM role attached that gives the agent permissions for reading information from the instance and writing it to CloudWatch. The on-premises server has an IAM user that provides the same permission to read and write information. The IAM role and IAM user can optionally include permissions to set the retention policy for the log groups that they send log events to.

The agent collects metrics by using data from the operating system. These metrics are sent to a CloudWatch metrics namespace (by default this will be named CWAgent). You can configure dimensions to organize and aggregate your metrics.  

The agent can collect log files specified as an individual file or group of files. It then sends them to a log stream (by default, this is named using the instance ID) in a log group that you have configured.

### Installing the CloudWatch agent

You can install the CloudWatch agent by using the command line, AWS Systems Manager, or an AWS CloudFormation template. The steps will vary depending on the operating system of the server on which you are installing the agent.

The following steps provide a general overview of the agent installation process:

1. To run the CloudWatch agent on an EC2 instance or server, create an IAM role using the **CloudWatchAgentServerPolicy** policy, and then attach the role to the instance. If you're running the agent on an on-premises server, create an IAM user with the **CloudWatchAgentServerPolicy** policy.
2. Download the agent package. On all supported operating systems, you can download and install the CloudWatch agent by using the command line. If you're using Amazon Linux 2, you can install the package by entering the **sudo yum install amazon-cloudwatch-agent** command.
3. Create and edit a CloudWatch agent JSON configuration file to configure the agent and specify the metrics and logs that you want to collect. You can use the agent configuration file wizard, **amazon-cloudwatch-agent-config-wizard**, to create the file. At a minimum, you should specify the AWS Region and AWS access key of an IAM user with permissions to publish to CloudWatch.
4. Start and enable the CloudWatch agent service.

For more detailed information and step-by-step instructions for each CloudWatch agent installation method, see [Installing the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html).

## Dashboards for Monitoring EC2 Instances

### Using the console to monitor instances

#### The Amazon EC2 console

The Amazon EC2 console and the CloudWatch dashboard both provide different ways to monitor EC2 instances, both historically and in real time. Each dashboard has its own advantages.

The Amazon EC2 dashboard displays service health and scheduled events by Region, instant state, status checks, and alarm status. The Amazon EC2 instance Monitoring tab displays a series of graphs based on the raw data from CloudWatch.

* To display instance metric details, in the navigation pane, choose **Instances**. Select an instance, and then choose the **Monitoring** tab.
* To display metric details for your storage volumes, in the navigation pane, choose **Volumes**. Select a volume, and then choose the Monitoring tab.

#### The CloudWatch dashboard

The CloudWatch dashboard displays current alarms and status, graphs of alarms and resources, and service health status.

You can also use CloudWatch to graph Amazon EC2 monitoring data, to troubleshoot issues, and discover trends over time. Here you can search and browse all of your AWS metrics. You can create and edit alarms to notify you of problems. You can see at-a-glance overviews of your alarms and AWS resources.

## Logging Activities with CloudTrail

### Following the trail

AWS CloudTrail provides insights into who did what and when by tracking user activity and API usage. With CloudTrail, you can get a history of AWS API calls in your account. These calls can be made through the console, AWS Command Line Interface (AWS CLI), AWS SDKs, and higher-level AWS services. CloudTrail records the AWS API calls and delivers the log files to you. The information includes the source IP address and identity of the API caller. It also includes the time of the call, the request parameters, and the response elements that the AWS service returns.

CloudTrail is active in your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. You can view the past 90 days of recorded API activity (management events) in an AWS Region in the CloudTrail console by going to **Event history**.

For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

### Benefits of monitoring with CloudTrail

The AWS API call history that CloudTrail produces can facilitate security analysis, tracking of resource changes, and compliance auditing.

CloudTrail helps you answer questions that require detailed analysis. You can store and view your CloudTrail API usage logs in an Amazon S3 bucket. Later, you can analyze those logs to answer compelling questions. For example, consider the following:

* Why was a long-running instance terminated and who terminated it? The answer can provide organizational traceability and accountability.
* Who changed a security group configuration? The answer can provide accountability and facilitate security auditing.
* What activities were denied due to lack of permissions? The answer can expose a potential internal or external attack against the network.

### CloudTrail logs

CloudTrail produces logs that you can analyze to determine the following:

* Who made the API request?
* What was the focus of the request?
* When did the request occur?
* What was the API call?
* What was the response?
* In what AWS Region did the request occur?

The following example shows the first section of a CloudTrail log. This section shows who performed an API request.

```json
{"Records": [{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EXAMPLE6E4XEGITWATV6R",
        "arn": "arn:aws:iam::123456789012:user/Mateo",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Mateo",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-07-19T21:11:57Z",
                "mfaAuthenticated": "false"
            }
        }
    },
```

In the preceding example, the **userIdentity** section of the log file shows that an AWS Identity and Access Management (IAM) user with **"userName": "Mateo"** performed an action. The section also shows that the IAM user was created on **"creationDate": "2023-07-19T21:11:57Z"**. The date and time are separated with a T. The Z at the end of the timestamp indicates that it is in Zulu time, more commonly known as Coordinated Universal Time (UTC).

The following example shows the next section of the same CloudTrail log. This section shows the action that was performed, when it occurred, and the Region in which it took place.

```json
    "eventTime": "2023-07-19T21:17:28Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "StartInstances",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.13.5 Python/3.11.4 Linux/4.14.255-314-253.539.amzn2.x86_64 exec-env/CloudShell exe/x86_64.amzn.2 prompt/off command/ec2.start-instances",
    "requestParameters": {
        "instancesSet": {
            "items": [
                {
                    "instanceId": "i-EXAMPLE56126103cb"
                },
                {
                    "instanceId": "i-EXAMPLEaff4840c22"
                }
            ]
        }
    },
```

In the preceding example, you can see that the **"eventTime"** took place at **"2023-07-19T21:17:28Z"**. The **aws ec2 start-instances** command, **"eventName": "StartInstances"**, was used to call **"eventSource": "ec2.amazonaws.com"** (meaning Amazon EC2) in **"awsRegion": "us-east-1"** from **"sourceIPAddress": "192.0.2.0"**. The command was used to start two EC2 instances with IDs **i-EXAMPLE56126103cb** and **i-EXAMPLEaff4840c22**.

The following example shows the next section of the CloudTrail log, which shows the response.

```json
    },
    "responseElements": {
        "requestId": "e4336db0-149f-4a6b-844d-EXAMPLEb9d16",
        "instancesSet": {
            "items": [
                {
                    "instanceId": "i-EXAMPLEaff4840c22",
                    "currentState": {
                        "code": 0,
                        "name": "pending"
                    },
                    "previousState": {
                        "code": 80,
                        "name": "stopped"
                    }
                },
                {
                    "instanceId": "i-EXAMPLE56126103cb",
                    "currentState": {
                        "code": 0,
                        "name": "pending"
                    },
                    "previousState": {
                        "code": 80,
                        "name": "stopped"
                    }
                }
            ]
        }
    },
```

The preceding example shows that both instances changed from a **previousState** of *stopped* to a **currentState** of *pending* in response to the **aws ec2 start-instances** command. This means both instances are preparing to enter the running state.

The following example shows the remaining section of the same CloudTrail log. It contains additional data about the event.

```json
    "requestID": "e4336db0-149f-4a6b-844d-EXAMPLEb9d16",
    "eventID": "e755e09c-42f9-4c5c-9064-EXAMPLE228c7",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
     "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "ec2.us-east-1.amazonaws.com"
    },
    "sessionCredentialFromConsole": "true"
}]}
```

As you read through the CloudTrail log, you can start to get a picture of what happened.

* An IAM user named Mateo was created on July 19, 2023.
* About 6 minutes after the user was created, Mateo made an API call from the IP address 192.0.2.0.
* Mateo used the aws ec2 start-instances command to start two EC2 instances in the us-east-1 Region that were previously in the stopped state.
* The command was successful, and the EC2 instances began to spin up.

CloudTrail logs are one way to understand the activity within your AWS environment. You can use these logs for troubleshooting and locating potential security risks.

### Knowledge Check

#### A cloud administrator is tasked with creating a monitoring plan for a company's AWS resources. What should the plan address first?

* The monitoring goals

Wrong answers:

* The time allocated for viewing metrics and dashboards each week
* The specific metrics that must be monitored
* Whether to use basic monitoring or detailed monitoring

##### Explanation

The first thing that a monitoring plan should address is your goals for monitoring. When you consider this, you should focus on operational outcomes instead of specific metrics. The goals that you identify will inform the rest of the monitoring plan.

#### A software developer is analyzing an AWS CloudTrail log to determine how the permissions associated with an Amazon S3 bucket were changed. What is an example of information that the CloudTrail log might provide?

* The identity of the person or service that changed the bucket permissions and when the change was made

Wrong answers:

* A list of objects in the bucket that have public read access as a result of the changed permissions
* The public IP address of the static website associated with the bucket
* A list of the users, roles, and services that have permission to change the bucket permissions

##### Explanation

WS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs.

The other options are incorrect for the following reason:

* CloudTrail records the AWS API calls and delivers the log files to you. The information includes the source IP address and identity of the API caller. It also includes the time of the call, the request parameters, and the response elements that the AWS service returns.

#### What is an example of an Amazon EC2 metric provided with Amazon CloudWatch basic monitoring?

* Completed disk reads and writes within a specified period of time

Wrong answers:

* Response times for applications connecting to the instance
* The identities of users who have made changes to the instance permissions
* Custom metrics for applications running on the instance

##### Explanation

Amazon CloudWatch basic monitoring for Amazon EC2 instances includes metrics for CPU utilization, network in and out, and disk reads and writes.

The other options are incorrect because they are not metrics provided with basic monitoring.

### Summary

#### What logging is and why it's important

Log files are software-generated files containing information about the operations, activities, and usage patterns of an application, server, or IT system.

Logs provide visibility into cloud operations that isn't possible otherwise. Logging is important for the following use cases:

* Troubleshooting issues
* Security and compliance
* Performance monitoring
* Billing audits
* Incident response
* Auto scaling
* Analytics

#### Amazon CloudWatch Logs

You can use the Amazon CloudWatch Logs service to collect and store logs from your resources, applications, and services in near real time. The following are the three main categories of logs:

* **Vended logs** – These are natively published by AWS services on your behalf. Currently, Amazon VPC flow logs and Amazon Route 53 logs are the two supported types.
* **Logs published by AWS services** – Currently, more than 30 AWS services publish logs to CloudWatch. They include Amazon API Gateway, AWS Lambda, AWS CloudTrail, and many others.
* **Custom logs** – These are logs from your own application and on-premises resources, and from other clouds.

#### Monitoring with CloudWatch

You can use CloudWatch to collect metrics and store logs. You can use CloudWatch to monitor a near real-time stream of system events. And you can create CloudWatch alarms that watch metrics and initiate actions like sending notifications or auto scaling when certain conditions are met. You can also use CloudWatch dashboards to create customizable views of metrics and alarms across multiple AWS resources.

CloudWatch provides two categories of monitoring:

* **Basic monitoring** provides metrics at 5-minute intervals.
* **Detailed monitoring** provides information at 1-minute intervals for services that offer it.

#### Creating a monitoring plan

A thoughtful monitoring strategy provides essential visibility and diagnostics that you can use to optimize, secure, and automate your AWS workloads. When you create a monitoring plan, you determine the strategies, tools, and processes that you will use to observe and track the performance and availability of cloud-based resources like servers, applications, and services.

#### Amazon EC2 metrics

Amazon EC2 provides a wide range of performance metrics. You can use these metrics to monitor and analyze the performance of your EC2 instances and the underlying infrastructure, and establish a baseline for normal Amazon EC2 performance in your environment.

The Amazon EC2 console and the CloudWatch dashboard both provide different ways to monitor EC2 instances both historically and in real time.

#### Logging activities with AWS CloudTrail

With CloudTrail, you can get a history of AWS API calls in your account. The AWS API call history that CloudTrail produces can facilitate security analysis, tracking of resource changes, and compliance auditing.

CloudTrail produces logs that you can analyze to determine the following:

* Who made the API request?
* What was the focus of the request?
* When did the request occur?
* What was the API call?
* What was the response?
* In what AWS Region did the request occur?

### Additional Resources

* [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
* [Monitor Amazon EC2 ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_ec2.html)

## Monitoring Application Health

### Pre-assessment

#### Which Amazon CloudWatch dashboard provides aggregated performance monitoring for multiple AWS Lambda functions, with metrics like cost, duration, errors, and throttles graphed over time? 

* Amazon CloudWatch Lambda Insights

Wrong answers:

* AWS X-Ray service map
* Amazon CloudWatch Container Insights
* Amazon CloudWatch Logs Insights

##### Explanation

The CloudWatch Lambda Insights multi-function dashboard in CloudWatch displays aggregated performance metrics for Lambda functions to help optimize utilization over time.

The other options are incorrect for the following reasons:

* AWS X-Ray service maps show information about your API and all of its downstream services.  
* CloudWatch Container Insights is used to collect, aggregate, and summarize metrics and logs from the containerized applications and microservices.
* With CloudWatch Logs Insights, you can interactively search and analyze your log data in Amazon CloudWatch Logs. You can perform queries to help you more efficiently and effectively respond to operational issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes.

#### Which services does Amazon CloudWatch Container Insights support for collecting metrics?

* Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and Kubernetes on Amazon EC2

Wrong answers:

* Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) only
* Amazon Elastic Kubernetes Service (Amazon EKS) and Kubernetes on Amazon EC2 only
* Amazon Elastic Container Service (Amazon ECS) on AWS Fargate only

##### Explanation

The other options are incorrect for the following reasons:

* CloudWatch Container Insights is available for Amazon ECS, Amazon EKS, and Kubernetes platforms on Amazon EC2.
* CloudWatch Container Insights supports collecting metrics from clusters deployed on AWS Fargate for both Amazon ECS and Amazon EKS.

#### What is a key benefit of proactive anomaly detection in cloud environments?

* It ensures efficient utilization of resources.

Wrong answers:

* It enables rapid scaling of workloads.
* It allows for frequent system upgrades.
* It provides real-time usage monitoring.

##### Explanation

Proactive anomaly detection is crucial in cloud environments where workloads can fluctuate rapidly. It helps identify abnormal usage patterns early, so organizations can optimize resources and manage costs efficiently.

The other options are incorrect because they are not the primary benefits of proactive anomaly monitoring.

### Keeping Your Applications Healthy

#### Observability and application health

Increasingly, downtime in applications and services costs money. Therefore, it is critical to resolve real issues as close to real time as possible to help you to maintain availability, reliability, and latency.

Observability describes how well you can understand what is happening in a system. It involves collecting and analyzing data such as metrics, logs, and traces to gain insights into system's behavior, performance, and health.

To achieve operational excellence and meet business objectives, you need to understand how your systems are performing.

Monitoring application logs and metrics can help you with the following:

* Understanding your application and infrastructure health
* Improving performance and availability
* Reducing operational cost
* Improving end-user experience and increasing customer satisfaction

#### Observability across service categories

When you create your monitoring plan, you identify all the resources that you need to monitor

* compute instances
* serverless applications
* containerized workloads

### Serverless Observability

#### Challenges of monitoring serverless resources

Transitioning from monolithic architectures to building modern applications requires the use of microservices composed of loosely coupled systems. Designing your applications in this way can benefit from fewer dependencies, fault isolation, and evolvable architecture to achieve previously unrealized agility, scalability, and cost efficiencies.

AWS offers serverless resources that provide secure, reliable, high-performing, and cost-effective capabilities that you can use to build applications for the asynchronous and event-driven world. For example, AWS Lambda is a serverless event-driven compute service that you can use to run code for virtually any type of application or backend service without provisioning or managing servers. You can use Lambda for a variety of use cases, including file and stream processing, web applications, Internet of Things (IoT) and mobile backends, and more.

However, the efficiency and effectiveness gains created through Lambda lead to new observability challenges. Your monitoring plan should include observing Lambda workloads, including recommendations for cost optimization, deriving insights, and meeting business goals.

##### Data collection for Lambda workloads differs from traditional infrastructure

Design patterns of Lambda workloads can include hundreds or thousands of microservices and components generating billion of metrics and events, and a never-ending stream of data.

With Lambda, you don't need to prioritize collecting and analyzing traditional infrastructure metrics, such as CPU utilization or memory usage, because AWS handles these resources. Instead, you must identify relevant business and customer experience metrics, sort through often overwhelming quantities of data, and determine a way to view, analyze, and take action on the data points that matter.

##### Lambda workloads are short lived

Lambda functions are highly ephemeral, and are spun up and down in seconds. Ideally, you should try to proactively identify and resolve potential issues before customers are impacted.

##### Traditional alerting approaches are insufficient for Lambda workloads

Microservices by nature create more data than traditional monolithic architectures. Using traditional alerting approaches will create false notifications and alert storms for Lambda developers. Instead, you need to identify meaningful outliers that highlight suboptimal customer experiences or poor business results for immediate remediation. You must create a thoughtful alarm strategy that focuses on performance outliers to prevent overalarming.

##### Lambda workloads support a faster pace of innovation

Modern applications are updated frequently, and their dependencies and architecture can change just as often. Without a holistic observability strategy in place, you might lose sight into the performance data associated with previous application versions. You need a mechanism to optimize your current application’s performance while also providing visibility into previous performance data to support deep dives and accurate root-cause analysis.

#### Monitoring with Lambda Insights

You can use CloudWatch Lambda Insights to monitor dependencies and performance metrics that impact the health and availability of your Lambda functions.

Lambda Insights uses a CloudWatch Lambda extension, which is provided as a Lambda layer. When you install this extension on a Lambda function, it collects system-level metrics and emits a single performance log event for every invocation of that Lambda function. CloudWatch uses embedded metric formatting to extract metrics from the log events.

Lambda Insights is compatible with any Lambda function that uses a Lambda runtime that supports Lambda extensions.

Lambda Insights provides the following features:

* Deep linking and correlations across metrics, logs, and traces
* Curated automated dashboards summarizing the performance and health of your Lambda functions
* Deeper integration with Amazon CloudWatch Logs for deeper analysis of log data through CloudWatch Logs Insights to analyze trace dependencies
* Performance metrics from AWS Lambda with observable context for each running function

You can use Lambda Insights to identify the following:

* Function issues such as memory leaks
* High-cost functions
* Performance changes caused by new function versions
* Latency drivers in functions

For more information, see [Using Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html) in the Amazon CloudWatch User Guide.

#### Lambda Insights dashboards

After you have installed the Lambda Insights extension on a Lambda function that has been invoked, you can use the CloudWatch console to see your metrics using either a multi-function dashboard or a single-function dashboard.

##### Multi-function dashboard

* Aggregated view across multiple Lambda functions
* Provides visibility into interconnected issues within a serverless architecture

##### Single-function dashboard

* View of one single Lambda function
* Ideal for troubleshooting root causes of a Lambda issue

#### Multi-function dashboard

The Lambda Insights multi-function dashboard displays an aggregated view of multiple Lambda functions. You can search by name or tag to focus on a specific Lambda function or a subset of functions.

You can use this dashboard to understand how compute, memory allocation, and function duration change over a period of time to help optimize Lambda function utilization.

The following image shows a Lambda Insights multi-function performance monitoring dashboard in the CloudWatch console. The dashboard includes metrics and alarms for function cost, duration, invocations, errors, memory usage, network usage, concurrent executions, and throttles. The metrics are graphed over a 6-hour period.

![Example of Lambda Insights multi-function performance monitoring dashboard.](./images/W06Img020LoggingServerlessMultifunctionDashboard.png)

#### Single-function dashboard

The single-function dashboard shows predefined performance metrics for a single Lambda function.

The following image shows a Lambda Insights single-function performance monitoring dashboard. It includes metrics and alarms for invocations and errors, duration, throttles, memory usage, CPU usage, and network usage over a 6-hour period.

![Example of Lambda Insights single-function performance monitoring dashboard.](./images/W06Img022LoggingServerlessSinglefunctionDashboard.png)

### CloudWatch Container Insights

#### Enhanced observability

Imagine that your team has embraced containerized applications, using Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) to efficiently deploy and manage your microservices architecture. In the dynamic world of containers, the operation teams can face challenges in gaining comprehensive insights into the health and performance of these distributed applications.

Here is where Amazon CloudWatch Container Insights becomes valuable. For example, during a high-traffic period, your team notices a sudden increase in latency across several containers and identifies spikes in resource utilization. Without CloudWatch Container Insights, pinpointing the root causes of these performance issues would be like finding a needle in a haystack.

By implementing CloudWatch Container Insights, your team can gain real-time visibility into containerized applications. The service aggregates and analyzes metrics like CPU and memory usage, network performance, and error rates across the entire container environment.

It provides actionable insights, such as diagnostic information that help your team troubleshoot and optimize the containerized environment for improved efficiency.

#### Using CloudWatch Container Insights

CloudWatch Container Insights is available for Amazon ECS, Amazon EKS, and Kubernetes platforms on Amazon Elastic Compute Cloud (Amazon EC2). CloudWatch Container Insights supports collecting metrics from clusters deployed on AWS Fargate for both Amazon ECS and Amazon EKS.

CloudWatch Container Insights collects data as *performance log* events using embedded metric format. With embedded metric format, you can generate custom metrics asynchronously in the form of logs written to Amazon CloudWatch Logs. You can embed custom metrics with detailed log event data, and CloudWatch automatically extracts the custom metrics so that you can visualize and alarm on them, for real-time incident detection.

The performance log events are entries that use a structured JSON schema that permits high-cardinality data to be ingested and stored at scale. From this data, CloudWatch creates aggregated metrics at the cluster, node, pod, task, and service level as CloudWatch metrics. The metrics that CloudWatch Container Insights collects are available in CloudWatch automatic dashboards, and are also viewable in the **Metrics** section of the CloudWatch console. When you deploy CloudWatch Container Insights, it automatically creates a log group for the performance log events. You don't need to create this log group yourself.

**Metrics are not visible until the container tasks have been running for some time.**

The following example is a cluster-wide performance dashboard that you can use to get a high-level perspective. The different views permit you to methodically narrow down to find the root cause, from cluster to node to pod to container.

![Screenshot of CloudWatch Container Insights with performance monitoring on the clusters level.](./images/W06Img024LoggingCloudWatchContainerInsights.png)

You can use the CloudWatch Container Insights dashboards to drill down into more detailed views to gain additional insights. For example, in the following image, the containers view shows CPU and memory utilization relative to the pod limits. This view reveals that the fluent-bit container was peaking at 77 percent utilization. By diving into these different views, you can more easily identify the root cause of issues. The dashboards also provide various views to analyze telemetry data from different dimensions.

When you drill into container-level details, the filters automatically populate with related components for that container. This helps users to quickly identify which node a failing container is on, and explore potential risks to other neighboring components on that node. Using the nested views and automatic filtering makes root-cause analysis highly efficient. This gives visibility into containerized workloads from high-level monitoring to pod and container metrics. This visibility helps troubleshoot and optimize container performance.

![Screenshot of CloudWatch Container Insights on the Containers level.](./images/W06Img026LoggingCloudWatchContainerInsightsContainerLevel.png)

To help you manage your CloudWatch Container Insights costs, CloudWatch doesn't automatically create all possible metrics from the log data. However, you can view additional metrics and additional levels of granularity by using CloudWatch Logs Insights to analyze the raw performance log events.

CloudWatch Container Insights in Amazon EKS and Kubernetes uses a containerized CloudWatch agent to detect all running containers in a cluster. It then collects performance data at each layer of the performance stack.

It can use an AWS KMS key to encrypt the collected logs and metrics. To allow this encryption, you must manually enable AWS KMS encryption for the log group that receives CloudWatch Container Insights data. This results in CloudWatch Container Insights encrypting this data with the provided KMS key. Only symmetric KMS keys are supported for encrypting log groups, and asymmetric keys cannot be used.

#### Setting up CloudWatch Container Insights on Amazon ECS

You can use one or both of the following options to enable CloudWatch Container Insights on Amazon ECS clusters:

* Use the AWS Management Console or the AWS Command Line Interface (AWS CLI) to start collecting cluster-level, task-level, and service-level metrics.
* Deploy the CloudWatch agent as a daemon service to start collecting instance-level metrics on clusters that are hosted on Amazon EC2 instances.

For new clusters, you can use either the Amazon ECS console or the AWS CLI. For existing clusters, you use the AWS CLI. The following examples show you how to use the AWS CLI to set up CloudWatch Container Insights.

##### New Amazon ECS cluster

You can use the AWS CLI to set account-level permission to enable CloudWatch Container Insights for any new Amazon ECS clusters created in your account. To do so, enter the following command.

```shell
aws ecs put-account-setting --name "containerInsights" --value "enabled"
```

##### Existing Amazon ECS cluster

To enable CloudWatch Container Insights on an existing Amazon ECS cluster, enter the following command.  

```shell
aws ecs update-cluster-settings --cluster myCICluster --settings name=containerInsights,value=enabled
```

#### Setting up CloudWatch Container Insights on Amazon EKS

You can use the Amazon EKS add-on to install CloudWatch Container Insights with enhanced observability for Amazon EKS. Amazon EKS add-on provides installation and management of operational capabilities for Amazon EKS clusters. The add-on installs the CloudWatch agent to send infrastructure metrics from the cluster and installs Fluent Bit to send container logs.

To install the Amazon EKS add-on, use the following steps.

1. Set up the necessary permissions by attaching the **CloudWatchAgentServerPolicy** to your worker nodes. To do so, enter the following command. Replace **my-worker-node-role** with the IAM role used by your Kubernetes worker nodes.

    ```shell
    aws iam attach-role-policy \
    --role-name my-worker-node-role \
    --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
    ```

2. Run the following add-on command and replace **my-cluster-name** with the name of your cluster.

    ```shell
    aws eks create-addon --cluster-name my-cluster-name --addon-name amazon-cloudwatch-observability
    ```

When the Amazon EKS add-on is enabled, the enhanced **Container Insights** page looks like the following image, with the high-level summary of your clusters. The CloudWatch Container Insights dashboard shows cluster status and alarms. It uses predefined thresholds for CPU and memory to quickly identify which resources are having higher consumption, so you can take proactive actions to avoid performance impact.

![Screenshot of enhanced Amazon CloudWatch Container Insights.](./images/W06Img028LoggingCloudWatchContainerInsightsEKS.png)

### Performance log reference

The following section includes reference information about how CloudWatch Container Insights uses performance log events to collect metrics. Remember, when you deploy CloudWatch Container Insights, it automatically creates a log group for the performance log events. You don't need to create this log group yourself.

#### CloudWatch Container Insights performance log events for Amazon ECS

The following example shows the performance log events that CloudWatch Container Insights collects from Amazon ECS.

This log is in CloudWatch Logs, in a log group named **/aws/ecs/containerinsights/CLUSTER_NAME/performance**. Within that log group, each container instance will have a log stream named **AgentTelemetry-CONTAINER_INSTANCE_ID**.

You can query the logs using queries such as **{ $.Type = "Container" }** to view all container log events.

```json
{
    "Version":"0",
    "Type":"Container",
    "ContainerName":"sleep",
    "TaskId":"7ac4dfba69214411b4783a3b8189c9ba",
    "TaskDefinitionFamily":"sleep360",
    "TaskDefinitionRevision":"1",
    "ContainerInstanceId":"0d7650e6dec34c1a9200f72098071e8f",
    "EC2InstanceId":"i-0c470579dbcdbd2f3",
    "ClusterName":"MyCluster",
    "Image":"busybox",
    "ContainerKnownStatus":"RUNNING",
    "Timestamp":1623963900000,
    "CpuUtilized":0.0,
    "CpuReserved":10.0,
    "MemoryUtilized":0,
    "MemoryReserved":10,
    "StorageReadBytes":0,
    "StorageWriteBytes":0,
    "NetworkRxBytes":0,
    "NetworkRxDropped":0,
    "NetworkRxErrors":0,
    "NetworkRxPackets":14,
    "NetworkTxBytes":0,
    "NetworkTxDropped":0,
    "NetworkTxErrors":0,
    "NetworkTxPackets":0
}
```

#### CloudWatch Container Insights performance log events for Amazon EKS and Kubernetes

The following example shows the performance log events that CloudWatch Container Insights collects from Amazon EKS and Kubernetes clusters.

```json
{
  "AutoScalingGroupName": "eksctl-myCICluster-nodegroup-standard-workers-NodeGroup-1174PV2WHZAYU",
  "CloudWatchMetrics": [
    {
      "Metrics": [
        {
          "Unit": "Percent",
          "Name": "node_cpu_utilization"
        },
        {
          "Unit": "Percent",
          "Name": "node_memory_utilization"
        },
        {
          "Unit": "Bytes/Second",
          "Name": "node_network_total_bytes"
        },
        {
          "Unit": "Percent",
          "Name": "node_cpu_reserved_capacity"
        },
        {
          "Unit": "Percent",
          "Name": "node_memory_reserved_capacity"
        },
        {
          "Unit": "Count",
          "Name": "node_number_of_running_pods"
        },
        {
          "Unit": "Count",
          "Name": "node_number_of_running_containers"
        }
      ],
      "Dimensions": [
        [
          "NodeName",
          "InstanceId",
          "ClusterName"
        ]
      ],
      "Namespace": "ContainerInsights"
    },
    {
      "Metrics": [
        {
          "Unit": "Percent",
          "Name": "node_cpu_utilization"
        },
        {
          "Unit": "Percent",
          "Name": "node_memory_utilization"
        },
        {
          "Unit": "Bytes/Second",
          "Name": "node_network_total_bytes"
        },
        {
          "Unit": "Percent",
          "Name": "node_cpu_reserved_capacity"
        },
        {
          "Unit": "Percent",
          "Name": "node_memory_reserved_capacity"
        },
        {
          "Unit": "Count",
          "Name": "node_number_of_running_pods"
        },
        {
          "Unit": "Count",
          "Name": "node_number_of_running_containers"
        },
        {
          "Name": "node_cpu_usage_total"
        },
        {
          "Name": "node_cpu_limit"
        },
        {
          "Unit": "Bytes",
          "Name": "node_memory_working_set"
        },
        {
          "Unit": "Bytes",
          "Name": "node_memory_limit"
        }
      ],
      "Dimensions": [
        [
          "ClusterName"
        ]
      ],
      "Namespace": "ContainerInsights"
    }
  ],
  "ClusterName": "myCICluster",
  "InstanceId": "i-1234567890123456",
  "InstanceType": "t3.xlarge",
  "NodeName": "ip-192-0-2-0.us-west-2.compute.internal",
  "Sources": [
    "cadvisor",
    "/proc",
    "pod",
    "calculated"
  ],
  "Timestamp": "1567096682364",
  "Type": "Node",
  "Version": "0",
  "kubernetes": {
    "host": "ip-192-168-75-26.us-west-2.compute.internal"
  },
  "node_cpu_limit": 4000,
  "node_cpu_request": 1130,
  "node_cpu_reserved_capacity": 28.249999999999996,
  "node_cpu_usage_system": 33.794636630852764,
  "node_cpu_usage_total": 136.47852169244098,
  "node_cpu_usage_user": 71.67075111567326,
  "node_cpu_utilization": 3.4119630423110245,
  "node_memory_cache": 3103297536,
  "node_memory_failcnt": 0,
  "node_memory_hierarchical_pgfault": 0,
  "node_memory_hierarchical_pgmajfault": 0,
  "node_memory_limit": 16624865280,
  "node_memory_mapped_file": 406646784,
  "node_memory_max_usage": 4230746112,
  "node_memory_pgfault": 0,
  "node_memory_pgmajfault": 0,
  "node_memory_request": 1115684864,
  "node_memory_reserved_capacity": 6.7109407818311055,
  "node_memory_rss": 798146560,
  "node_memory_swap": 0,
  "node_memory_usage": 3901444096,
  "node_memory_utilization": 6.601302600149552,
  "node_memory_working_set": 1097457664,
  "node_network_rx_bytes": 35918.392817386324,
  "node_network_rx_dropped": 0,
  "node_network_rx_errors": 0,
  "node_network_rx_packets": 157.67565245448117,
  "node_network_total_bytes": 68264.20276554905,
  "node_network_tx_bytes": 32345.80994816272,
  "node_network_tx_dropped": 0,
  "node_network_tx_errors": 0,
  "node_network_tx_packets": 154.21455923431654,
  "node_number_of_running_containers": 16,
  "node_number_of_running_pods": 13
}
```

### CloudWatch Application Insights

#### Detecting common application problems

Application monitoring is fundamental for maintaining the application's health, reliability, and security. It empowers you to proactively address issues, optimize performance, and deliver a positive user experience.

To gain comprehensive insights into the performance and health of your applications that were built with technologies such as Microsoft IIS, .NET, and Microsoft SQL Server, you can use Amazon CloudWatch Application Insights.

CloudWatch Application Insights simplifies the monitoring and troubleshooting of applications by automatically detecting common problems, correlating data from various AWS resources, and providing a consolidated view of application health.

* Automatic problem detection
    CloudWatch Application Insights automates the detection of common application issues, such as latency spikes, error rates, and resource constraints. The automated approach accelerates the identification of problems and reduces the mean time to repair (MTTR) to troubleshoot your application issues.
* Correlation across resources
    CloudWatch Application Insights correlates data from various AWS resources, including Amazon EC2 instances, databases, and load balancers. This correlation provides a holistic view of how different components contribute to application performance, thus streamlining troubleshooting efforts.
* Preconfigured dashboards
    CloudWatch Application Insights generates preconfigured dashboards that display key performance metrics and logs related to detected issues. These dashboards offer a centralized and visualized overview. This facilitates quick analysis and decision-making.
* Intelligent anomaly detection
    CloudWatch Application Insights employs intelligent anomaly detection algorithms to identify abnormal patterns in application data. This helps organizations proactively address issues before they impact the end-user experience.

#### CloudWatch Application Insights

When you add your applications to Amazon CloudWatch Application Insights, it scans the resources in the applications and recommends and configures metrics and logs on CloudWatch for application components. Example application components include SQL Server backend databases and Microsoft IIS - web tiers.

CloudWatch Application Insights uses historical data to analyze metric patterns and detect anomalies. It continuously detects errors and exceptions from your application, operating system, and infrastructure logs. It correlates these observations by using a combination of classification algorithms and built-in rules.

When errors and anomalies are detected, CloudWatch Application Insights generates CloudWatch Events that you can use to set up notifications or take actions. Then it automatically creates dashboards that show the relevant observations and problem severity information to help you prioritize your actions.

For common problems in .NET and SQL application stacks, such as application latency, SQL Server failed backups, memory leaks, large HTTP requests, and canceled I/O operations, it provides additional insights that point to a possible root cause and steps for resolution.

The following concepts are important for understanding how CloudWatch Application Insights monitors your application.

##### Component

A component is an auto-grouped, standalone, or custom grouping of similar resources that make up an application. We recommend grouping similar resources into custom components for better monitoring.

##### Observation

An observation is an individual event (metric anomaly, log error, or exception) that is detected with an application or application resource.

##### Problem

Problems are detected by correlating, classifying, and grouping related observations.

#### How CloudWatch Application Insights works

CloudWatch Application Insights monitors applications by employing an automated and intelligent approach to detect, correlate, and analyze data from various AWS resources in the following four steps.

1. **Application discovery and configuration**: When you initially configure an application with CloudWatch Application Insights, it examines the various components of the application to suggest important metrics, log files, and other information sources. You can then configure your application based on these recommendations.
2. **Data preprocessing**: CloudWatch Application Insights continuously analyzes the data sources being monitored across the application resources. This is to discover metric anomalies and log errors (also called observations).
3. **Intelligent problem detection**: The CloudWatch Application Insights engine detects problems in your application by correlating observations with classification algorithms and built-in rules. It creates automated CloudWatch dashboards, which include contextual information about the problems, to help you troubleshoot.
4. **Alert and action**: When CloudWatch Application Insights detects a problem with your application, it generates CloudWatch Events to notify you of the problem.

CloudWatch Application Insights retains problems for 55 days and observations for 60 days.

##### Example scenario

Let's say you have an ASP.NET application that is backed by a SQL Server database. Suddenly, your database begins to malfunction because of high memory pressure. This leads to application performance degradation and possibly HTTP 500 errors in your web servers and load balancer.

With CloudWatch Application Insights and its intelligent analytics, you can identify the application layer that is causing the problem by checking the dynamically created dashboard that shows the related metrics and log file snippets. In this case, the problem might be at the SQL database layer.

#### Events and notifications

When issues arise with your application, CloudWatch Application Insights can identify these problems and create CloudWatch Events to alert you about them. For each application that is added to CloudWatch Application Insights, a CloudWatch event is published for the following events on a best effort basis.

##### Problem creation

This event is invoked when CloudWatch Application Insights detects a new problem.

* Detail type: **"Application Insights Problem Detected"**
* Detail:
  * **problemId**: The detected problem ID.
  * **region**: The AWS Region where the problem was created.
  * **resourceGroupName**: The resource group for the registered application for which the problem was detected.
  * **status**: The status of the problem. Possible status and definitions are as follows:
    * **In progress**: A new problem has been identified. The problem is still receiving observations.
    * **Recovering**: The problem is stabilizing. You can manually resolve the problem when it is in this state.
    * **Resolved**: The problem is resolved. There are no new observations about this problem.
    * **Recurring**: The problem was resolved within the past 24 hours. It has reopened as a result of additional observations.
  * **severity**: The severity of the problem.
  * **problemUrl**: The console URL for the problem.

##### Problem update

This event is invoked when the problem is updated with a new observation or when an existing observation is updated and the problem is subsequently updated. The updates include a resolution or closure of the problem.

* Detail type: **"Application Insights Problem Updated"**
* Detail:
  * **problemId**: The created problem ID.
  * **region**: The AWS Region where the problem was created.
  * **resourceGroupName**: The resource group for the registered application for which the problem was detected.
  * **status**: The status of the problem.
  * **severity**: The severity of the problem.
  * **problemUrl**: The console URL for the problem.

#### Viewing and troubleshooting problems detected

CloudWatch Application Insights detects problems with your applications and infrastructure and provides insights to help troubleshoot issues.

##### CloudWatch Application Insights overview pane

The CloudWatch Application Insights overview pane displays the following:

* The severity of the problems detected: High, Medium, or Low
* A short summary of the problem
* The problem source
* The time that the problem started
* The resolution status of the problem
* The affected resource group

To view the details of a specific problem, under **Problem Summary**, select the description of the problem. A detailed dashboard displays insights into the problem and related metric anomalies and snippets of log errors. You can provide feedback on the relevance of the insight by selecting whether it is useful.

If a new resource is detected that is not configured, the problem summary description takes you to the **Edit configuration** wizard to configure your new resource.

![Example screenshot of detected problems dashboard in CloudWatch Application Insights.](./images/W06Img030LoggingCloudWatchAppInsights.png)

##### CloudWatch Application Insights Problem summary page

CloudWatch Application Insights provides the following information about detected problems on the **Problem summary** page:

* A short summary of the problem
* The start time and date of the problem
* The problem severity: High, Medium, or Low
* The status of the detected problem: In progress or Resolved
* Insight: Automatically generated insights on the detected problem and possible root cause
* Feedback on insights: Feedback that you have provided about the usefulness of the insights generated by CloudWatch Application Insights
* Related observations: A detailed view of the metric anomalies and error snippets of relevant logs related to the problem across various application components

![Example screenshot of detailed detected problem summary in CloudWatch Application Insights.](./images/W06Img032LoggingCloudWatchAppInsightsProblemSum.png)

##### CloudWatch agent merge conflict failures

CloudWatch Application Insights installs and configures the CloudWatch agent on customer instances. This includes creation of a CloudWatch agent configuration file with configurations for metrics or logs. A merge conflict can occur if a customer's instance already has a CloudWatch agent configuration file with different configurations defined for the same metrics or logs.

To resolve the merge conflict, use the following steps:

1. Identify the CloudWatch agent configuration files on your system.
2. Remove the resource configurations that you want to use in CloudWatch Application Insights from the existing CloudWatch agent configuration file. If you want to only use Application Insights configurations, delete the existing CloudWatch agent configuration files.

##### Alarms not created

For some metrics, CloudWatch Application Insights predicts the alarm threshold based on previous data points for the metric. To enable this prediction, the following criteria must be met.

* **Recent data points**: There must be a minimum of 100 data points from the last 24 hours. The data points don't have to be continuous and can be scattered throughout the 24-hour time frame.
* **Historical data**: There must be a minimum of 100 data points spanning the time frame from 15 days before the current date to 1 day before the current date. The data points don't have to be continuous and can be scattered throughout the 15-day time frame.

##### Feedback

You can provide feedback on the automatically generated insights on detected problems by designating them useful or not useful. Your feedback on the insights, along with your application diagnostics (metric anomalies and log exceptions), are used to improve the future detection of similar problems.

##### Configuration errors

CloudWatch Application Insights uses your configuration to create monitoring telemetries for the components. When Application Insights detects an issue with your account or your configuration, information is provided in the **Remarks** field of the **Application summary** about how to resolve the configuration issue for your application.

Overall, CloudWatch Application Insights aims to proactively detect problems, provide actionable insights to troubleshoot issues, and collect feedback to continuously improve. The console overview and detailed dashboards help you monitor and resolve application and infrastructure problems effectively.

### CloudWatch Anomaly Detection

#### Anomaly detection

In a dynamic and scalable cloud environment, where workloads can fluctuate rapidly, proactive anomaly detection becomes crucial for identifying abnormal patterns that might indicate potential problems. It's also an essential component in ensuring the reliability and performance of cloud-based systems.

Early detection of anomalies let organizations address issues before they impact end users. This reduces downtime and prevents potential revenue loss. Proactive monitoring also facilitates resource optimization to ensure that resources are efficiently used and costs are well managed.

#### Benefits of CloudWatch anomaly detection

Anomaly detection in CloudWatch is grounded in statistical methods that establish a baseline for normal behavior. By continuously analyzing metric data, CloudWatch identifies deviations from this baseline to signal potential anomalies.

For example, a financial services organization might use CloudWatch anomaly detection to strengthen its cybersecurity measures. By monitoring network traffic, access logs, and system behavior, the organization can set up anomaly detection alarms to identify unusual patterns that might indicates a security threat. For example, a sudden increase in failed login attempts or anomalous data access patterns invokes alerts, and this prompts the security team to investigate and respond quickly.

CloudWatch anomaly detection acts as a proactive security layer. The organization can use it to detect and mitigate potential security incidents before they escalate. This not only enhances the overall security posture but also safeguards sensitive financial data and maintains customer trust in the organization's services.

#### Using CloudWatch anomaly detection

CloudWatch anomaly detection uses machine learning algorithms. These algorithms continuously analyze the metrics of systems and applications, determine normal baselines, and display anomalies with minimal user intervention.

The algorithms generate an anomaly detection model. The model generates a range of expected values that represent normal metric behavior.

You can use the model of expected values in two ways:

* Create anomaly detection alarms based on a metric's expected value. These types of alarms don't have a static threshold for determining alarm state. Instead, they compare the metric's value to the expected value based on the anomaly detection model. You can choose whether the alarm is invoked when the metric value is above the band of expected values, below the band, or both.
* When viewing a graph of metric data, overlay the expected values onto the graph as a band. This makes it visually clear which values in the graph are out of the normal range.

Anomaly detection algorithms can adjust for the seasonality and trend changes of metrics. Seasonality changes could be hourly, daily, or weekly. After it is built, the model will be updated every 5 minutes with any new metric data. In a graph with anomaly detection, the gray bands indicate the expected values according the CloudWatch machine learning models, and the anomalous values are red lines that go beyond the bands.

![Example screenshot of a graph with anomaly detection.](./images/W06Img034LoggingCloudWatchAnomalyDetection.png)

#### How CloudWatch anomaly detection works

When you enable anomaly detection for a metric, CloudWatch applies machine learning algorithms to the metric's past data to create a model of the metric's expected values. The model assesses both trends and hourly, daily, and weekly patterns of the metric. The algorithm trains on up to 2 weeks of metric data, but you can enable anomaly detection on a metric even if the metric does not have a full 2 weeks of data.

You specify a value for the anomaly detection threshold that CloudWatch uses, along with the model to determine the normal range of values for the metric. A higher value for the anomaly detection threshold produces a thicker band of normal values.

The machine learning model is specific to a metric and a statistic. For example, if you enable anomaly detection for a metric using the **AVG** statistic, the model is specific to the **AVG** statistic.

When CloudWatch creates a model for many common metrics from AWS services, it ensures that the band doesn’t extend outside of logical values. For example, a band for a statistic that can’t be negative will never extend below zero, and a band for a percentage metric will stay between 0 and 100.

After you create a model, CloudWatch anomaly detection continually evaluates the model and makes adjustments to it to ensure that it is as accurate as possible. This includes retraining the model to adjust if the metric values evolve over time or have sudden changes. And it also includes predictors to improve the models of metrics that are seasonal, spiky, or sparse.

After you enable anomaly detection on a metric, you can choose to exclude specified time periods of the metric from being used to train the model. This way, you can exclude deployments or other unusual events from being used for model training, to ensure that the most accurate model is created.

Using anomaly detection models for alarms incurs charges on your AWS account.

### CloudWatch Metric Streams

#### Use case

AWS Partners have used the Amazon CloudWatch metrics to create various monitoring, alerting, and cost management tools. To access the metrics, the Partners used to create polling fleets that called the **ListMetrics** and **GetMetricDatafunctions** for each of their customers.

These fleets must scale in proportion to the number of AWS resources created by each of the Partners’ customers and the number of CloudWatch metrics that are retrieved for each resource. This polling is simply undifferentiated heavy lifting that each Partner must do. It adds no value, and takes time that could be better invested in other ways.

With CloudWatch metric streams, instead of polling (which can result in 5 to 10 minutes of latency), metrics are delivered to an Amazon Data Firehose stream. This helps Partners to scale down their polling fleets substantially, and lets them build tools that can respond more quickly when key cost or performance metrics change in unexpected ways.

![Screenshot of the Create a metric stream page in the CloudWatch console.](./images/W06Img036LoggingCloudWatchMetricStreams.png)

#### CloudWatch metric streams

CloudWatch metric streams are a feature that you can use to continually stream CloudWatch metrics to other AWS destinations and several third-party provider destinations.  

CloudWatch metric streams provides near real-time delivery and low latency. This provides immediate access to critical performance and operational data.

##### Custom setup with Amazon Data Firehose

You can create a metric stream and direct it to a Firehose delivery stream. It then delivers your CloudWatch metrics to where you want them to go. Amazon Data Firehose is a fully managed service that you can use to capture, transform, and load massive volumes of streaming data from hundreds of thousands of sources into AWS services.

You can stream them to a data lake such as Amazon Simple Storage Service (Amazon S3), or to any destination or endpoint supported by Firehose, including third-party providers. JSON and OTEL 0.7.0 formats are supported natively. Or you can configure transformations in your Firehose delivery stream to convert the data to a different format, such as Parquet.

With a metric stream, you can continually update monitoring data, or combine this CloudWatch metric data with billing and performance data to create rich datasets. You can then use tools such as Amazon Athena to get insight into cost optimization, resource performance, and resource utilization.

##### Quick Amazon S3 setup

You can stream to Amazon S3 with a quick setup process. By default, CloudWatch creates the resources needed for the stream. Both JSON and OTEL 0.7.0 formats are supported.

##### Quick AWS Partner setup

CloudWatch provides a quick setup experience for some third-party Partners. You can use third-party service providers to monitor, troubleshoot, and analyze your applications by using the streamed CloudWatch data. When you use the quick partner setup workflow, you need to provide only a destination URL and API key for your destination, and CloudWatch handles the rest of the setup. Quick partner setup is available for the following third-party providers:

* Datadog
* Dynatrace
* New Relic
* Splunk Observability Cloud
* Sumo Logic

CloudWatch metric streams are fully managed and convenient to set up. Streams can scale to handle any volume of metrics, with delivery to the destination within 2 or 3 minutes. You can choose to send all available metrics to each stream that you create, or you can opt-in to any of the available AWS (EC2, S3, and others) or custom namespaces. You can also use filters to stream only specified metrics. Each metric stream can include up to 1,000 filters that either include or exclude metric namespaces or specific metrics.

**A single metric stream can have only include or exclude filters, but not both.**

After a metric stream is created, if new metrics are created that match the filters in place, the new metrics are automatically included in the stream. There is no limit on the number of metric streams per account or per Region. There is also no limit on the number of metric updates being streamed.

Metric streams always include the **Minimum**, **Maximum**, **SampleCount**, and **Sum** statistics. You can also choose to include additional statistics at an additional charge.

* [Metric steams statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-statistics.html)

Metric streams are always in one of two states: *Running* or *Stopped*.

* **Running**: The metric stream is running correctly. There might not be any metric data streamed to the destination because of the filters on the stream.
* **Stopped**: The metric stream has been explicitly stopped by someone, and not because of an error. It might be useful to stop your stream to temporarily pause the streaming of data without deleting the stream.

If you stop and restart a metric stream, the metric data that was published to CloudWatch while the metric stream was stopped is not backfilled to the metric stream.

### AWS X-Ray

AWS X-Ray is a distributed tracing service that you can use to analyze and monitor applications running on AWS. It provides a detailed view of requests as they travel through various components of a distributed application. This becomes very important for microservice applications where a single action, like adding an item to your shopping cart, can travel through many microservices.

X-Ray helps you to identify performance slowdowns, troubleshoot errors, and optimize overall system efficiency. X-Ray can enhance the visibility and management of your application's performance. This ultimately leads to better user experiences and more efficient resource utilization.

#### Analyzing Applications with AWS X-Ray

With X-Ray, you can determine the root cause of performance issues or errors. It can help you understand how your application is used, monitor its response times, and detect and troubleshoot security and abuse issues. You can use X-Ray to analyze and debug distributed applications in both development and production environments. This includes architectures ranging from straightforward three-tier applications to those that are built using microservices.

Amazon CloudWatch provides metrics and logs for monitoring applications and infrastructure. Conversely, X-Ray traces requests as they flow through your application components. With X-Ray, developers can visualize the path of a request, identify slow or failed requests, and optimize the performance of the application. X-Ray is especially useful for developers who need to analyze and troubleshoot the performance of their applications. It is also useful for operations teams that need to monitor the health and usage of AWS resources.

X-Ray integrates with Amazon CloudWatch and many of its features, including CloudWatch ServiceLens, CloudWatch RUM, or Real-User Monitoring, and CloudWatch Synthetics. The AWS X-Ray Developer Guide has the most current list of services that integrate directly with X-Ray.

#### X-Ray's Service map

X-Ray traces and records requests to create what is called a *service map*. A service map displays the architecture of your application and the services that it uses. The service map shows the relationship between your applications, microservices, and containers, and underlying infrastructure. You can use the service map to identify the services that your application depends on and analyze their performance. X-Ray highlights trouble spots, such as areas of latency, and it provides details about components.

In addition to measuring latency, X-Ray records three types of errors.

1. Client-side errors, which are 400-series errors.
2. Faults on the server side or from AWS, which are 500-series errors.
3. Throttling errors for too many requests, which are 429 errors.

#### An example using AWS X-Ray

Now, let's review an example using AWS X-Ray. In this example, there is a serverless application that uses an Amazon API Gateway to communicate with a backend AWS Lambda function. The X-Ray tracing feature has been enabled in both services so that transactions and other details that occur within the application can be added to a trace.

Once a request is made, within a few seconds, you can open up Amazon CloudWatch and go the X-Ray traces section to view the results. Traces will allow you to see the events that occurred within a 6-hour time period any time within the last 30 days. When you choose a trace, you can view trace details that include status, response codes, and duration information about each service or application segment.

In the **Segments Timeline** section, you can choose a specific segment to view more specific information about the service or node. If you like visuals, you can choose **Go to service map** at the top of the **Trace details** page. From here, you can see a map of the group of nodes that make up your application.

If you expand the **Legend and options** menu, you will see what each item on the map represents. You can choose a node to see metrics, such as requests, latency, alerts, and response times. You can choose **Analyze traces** to show a detailed analytics page with information related to that specific trace group.

For example, consider an application that displays a photo to the user. The application uses an API call that invokes a Lambda function, which then retrieves the storage location of the photo from a database. If the response takes a long time, you can review the X-Ray service map to find the underlying issue. It might be a database with under-provisioned capacity that can't manage the number of requests it's receiving. Or, it might be that the Lambda function is reaching concurrency limits.

X-Ray can be useful in an event-driven architecture where one application is broken into many small parts because it can help identify issues in a microservices environment. Instead of parsing through logs to find issues, you can use X-Ray to identify if the issue is coming from the client or server side, and what service or services are contributing to the root cause.

### Knowledge Check

#### Which AWS service provides distributed tracing for applications running on AWS infrastructure?

* AWS X-Ray

Wrong answers:

* AWS CloudTrail
* AWS Lambda
* Amazon CloudWatch

##### Explanation

AWS X-Ray is a distributed tracing service that you can use to analyze and monitor applications running on AWS. It provides a detailed view of requests as they travel through various components of a distributed application.

The other options are incorrect for the following reasons:

* AWS CloudTrail is a service that records API calls on your account. It doesn't provide distributed tracing capabilities like AWS X-Ray.
* AWS Lambda is a serverless computing service that let you run code without provisioning or managing servers. While Lambda can be instrumented with AWS X-Ray to trace requests, Lambda itself is not a tracing service.
* Amazon CloudWatch is a monitoring and observability service for AWS resources and applications. It collects and tracks metrics, monitoring log files, and set alarms. It doesn't provide distributed tracing capabilities like AWS X-Ray.

#### Which Amazon CloudWatch feature provides the ability to stream near real-time CloudWatch metrics for applications to destinations like Amazon S3?

* Amazon CloudWatch metric streams

Wrong answers:

* Amazon CloudWatch Container Insights
* Amazon CloudWatch Lambda Insights
* Amazon CloudWatch Application Insights

##### Explanation

CloudWatch metric streams provide near real-time delivery of CloudWatch metrics to destinations like Amazon S3 with low latency. Metric streams are fully managed and can handle any volume of metrics, and new metrics matching the stream filters are automatically included.

The other options are incorrect for the following reasons:

* CloudWatch Container Insights supports collecting metrics from clusters deployed on AWS Fargate for both Amazon ECS and Amazon EKS. It doesn't steam metrics to destinations like Amazon S3.
* CloudWatch Lambda Insights collects system-level metrics and emits a single performance log event for every invocation of that Lambda function. It doesn't steam metrics to destinations like Amazon S3.
* CloudWatch Application Insights scans the resources in the applications and recommends and configures metrics and logs on CloudWatch for application components. It doesn't steam metrics to destinations like Amazon S3.

#### How does Amazon CloudWatch Application Insights contribute to troubleshooting issues within applications?

* By providing a unified view and automated discovery of issues

Wrong answers:

* By focusing solely on metrics
* Through manual analysis of distributed traces
* By relying on third-party tools for root cause analysis

##### Explanation

The other options are incorrect for the following reason:

* CloudWatch Application Insights contributes to troubleshooting by providing a unified view of application health. It offers automated discovery of issues to simplify the identification of root causes.

### Summary

#### Observability and application health

Observability describes how well you can understand what is happening in a system, often with the use of metrics, logs, and traces. To achieve operational excellence and meet business objectives, you need to understand how your systems are performing.

#### Monitoring with CloudWatch Lambda Insights

CloudWatch Lambda Insights uses a CloudWatch Lambda extension, which is provided as a Lambda layer. When you install this extension on a Lambda function, it collects system-level metrics and emits a single performance log event for every invocation of that Lambda function. CloudWatch uses embedded metric formatting to extract metrics from the log events.

Lambda Insights is compatible with any Lambda function that uses a Lambda runtime that supports Lambda extensions.

After you have installed the Lambda Insights extension on a Lambda function that has been invoked, you can use the CloudWatch console to see your metrics with either a multi-function dashboard or a single-function dashboard.

#### CloudWatch Container Insights

CloudWatch Container Insights is available for Amazon ECS, Amazon EKS, and Kubernetes platforms on Amazon EC2. CloudWatch Container Insights supports collecting metrics from clusters deployed on AWS Fargate for both Amazon ECS and Amazon EKS. CloudWatch Container Insights collects data as performance log events using embedded metric format. With the performance log events, CloudWatch creates aggregated metrics at the cluster, node, pod, task, and service level as CloudWatch metrics.

#### CloudWatch Application Insights

CloudWatch Application Insights simplifies the monitoring and troubleshooting of applications by automatically detecting common problems, correlating data from various AWS resources, and providing a consolidated view of application health. When you add your applications to CloudWatch Application Insights, it scans the resources in the applications and recommends and configures metrics and logs on CloudWatch for application components. CloudWatch Application Insights uses historical data to analyze metric patterns and detect anomalies.

CloudWatch Application Insights includes the following three concepts:

* **Components** are auto-grouped, standalone, or custom groupings of similar resources that make up an application. It is a best practice to group similar resources into custom components for better monitoring.
* **Observations** are individual events that are detected with an application or application resource.
* **Problems** are detected by correlating, classifying, and grouping related observations.

#### CloudWatch anomaly detection

CloudWatch anomaly detection applies statistical and machine learning algorithms to CloudWatch metrics, calculates normal baselines, and minimizes surface anomalies with minimal user intervention. CloudWatch anomaly detection is available with any AWS service metric or custom CloudWatch metric that has a discernible trend or pattern. It analyzes the historical values for the chosen metric for predictable patterns that repeat over time to create a baseline. This baseline model is updated when new metric data is observed, thus reducing the need for frequent manual intervention. Furthermore, it will periodically assess the model’s performance and retrain it to adjust to changing business metrics.

#### CloudWatch metric steams

CloudWatch metric streams let you stream CloudWatch metrics to AWS destinations and third-party providers with minimal delay. The low latency helps you to promptly access vital performance and operational data.

The following are three main usage scenarios for CloudWatch metric streams:

* **Custom setup with Amazon Data Firehose**: Create a metric stream and direct it to a Firehose delivery stream that delivers your CloudWatch metrics to where you want them to go.
* **Quick Amazon S3 setup**: Stream your metrics to an Amazon S3 bucket with one click. By default, CloudWatch creates the resources for you and streams the metrics with the JSON format.
* **Quick AWS Partner setup**: Stream your metrics to an AWS Partner with one click. CloudWatch creates all necessary resources for you and streams the metrics to the selected AWS Partner destination.

#### AWS X-Ray

You can use X-Ray to analyze and debug distributed applications in both development and production environments. This includes architectures ranging from straightforward three-tier applications to those that are built using microservices.

CloudWatch provides metrics and logs for monitoring applications and infrastructure. Conversely, X-Ray traces requests as they flow through application components. With X-Ray, developers can visualize the path of a request, identify slow or failed requests, and optimize the performance of the application. X-Ray is especially useful for developers who need to analyze and troubleshoot the performance of their applications. It is also useful for operations teams that need to monitor the health and usage of AWS resources.

### Additional Resources

* [Get Started with Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-getting-started.html)

* [Set Up a Metric Stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup.html)

## CloudWatch for Health, Availability, and Security

### Pre-assessment

#### A developer needs to analyze and visualize real user performance metrics for their web applications. Which Amazon CloudWatch feature is designed specifically for real user monitoring?

* Amazon CloudWatch RUM

Wrong answers:

* Amazon CloudWatch Contributor Insights
* Amazon CloudWatch Metrics Insights
* Amazon CloudWatch Synthetics

##### Explanation

CloudWatch RUM is tailored for real user monitoring. With CloudWatch RUM, you can perform real user monitoring to collect and view client-side data about your web application performance from actual user sessions in near real time. The data that you can visualize and analyze includes page load times, client-side errors, and user behavior.

The other options are incorrect for the following reasons:

* CloudWatch Contributor Insights analyzes time-series data to provide a view of the top contributors that influence system performance. It doesn't provide real user monitoring.
* CloudWatch Metrics Insights is a fast, flexible, SQL-based query engine that you can use to identify trends and patterns within millions of operational metrics. It doesn't provide real user monitoring.
* CloudWatch Synthetics allows for the creation of canary tests to monitor APIs and other endpoints proactively. Canaries follow the same routes and perform the same actions as a customer to simulate user interaction.

#### A team wants to use a query to deep dive into log data to troubleshoot application issues and discover patterns. Which Amazon CloudWatch feature would be most suitable for this?

* Amazon CloudWatch Logs Insights

Wrong answers:

* Amazon CloudWatch Evidently
* Amazon CloudWatch Synthetics
* Amazon CloudWatch Metrics Insights

##### Explanation

CloudWatch Logs Insights helps users efficiently identify patterns, interactively search, and analyze log data with bar charts, line charts, and stacked area charts. Users can perform queries to efficiently and effectively respond to operational or network issues. If an issue occurs, they can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes.

The other options are incorrect for the following reasons:

* You can use Amazon CloudWatch Evidently to safely validate new features by serving them to a specified percentage of your users while you roll out the features.
* CloudWatch Synthetics allows for the creation of canary tests to monitor APIs and other endpoints proactively. Canaries follow the same routes and perform the same actions as a customer to simulate user interaction.
* CloudWatch Metrics Insights is a fast, flexible, SQL-based query engine that you can use to identify trends and patterns within millions of operational metrics in near real time.

#### Why might an organization choose to use high-resolution metrics and alarms in Amazon CloudWatch?

* To increase granularity and precision in monitoring

Wrong answers:

* To reduce overall storage costs
* To limit the number of alarms that can be set up
* To facilitate seamless integration with third-party monitoring tools

##### Explanation

High-resolution metrics and alarms in CloudWatch are used to increase the granularity and precision of monitoring. These metrics give users more immediate visibility and greater granularity into the state and performance of their custom applications, such as observing short-lived spikes and functions.

The other options are incorrect for the following reasons:

* High-resolution metrics don't reduce overall storage costs.
* High-resolution metrics don't limit the number of alarms that can be set up.
* High-resolution metrics don't facilitate integration with third-party monitoring tools.

### CloudWatch Dashboards

Imagine that you are overseeing mission-critical applications where unexpected spikes in user activity occur, leading to potential performance issues. Without real-time insights, identifying the root cause becomes difficult.

Now, let's consider having a unified visual interface that offers an immediate comprehensive view of your entire cloud environment. You can pinpoint anomalies, optimize resource allocation, and ensure the seamless functioning of your applications. This is where Amazon CloudWatch dashboards can be useful.

### Using CloudWatch dashboards

Amazon CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view, even those resources that are spread across different Regions. You can use CloudWatch dashboards to create customized views of the metrics and alarms for your AWS resources.

With dashboards, you can create the following:

* A single view for selected metrics and alarms to help you assess the health of your resources and applications across one or more Regions. You can use different visual settings for each metric on each graph, so that you can readily track the same metric across multiple graphs.
* An operational playbook that provides guidance for team members during operational events about how to respond to specific incidents.
* A common view of critical resource and application measurements that can be shared by team members for faster communication flow during operational events.

![Example of a CloudWatch dashboard view.](./images/W06Img040LoggingCloudWatchDashboardExample.png)

You can create dashboards from the console or by using the AWS Command Line Interface (AWS CLI) or **PutDashboard** API operation. You can add dashboards to a favorites list, where you can access not only your favorite dashboards, but also your recently visited dashboards.

#### Cross-account observability dashboards

If you have multiple AWS accounts, you can set up CloudWatch cross-account observability and then create rich cross-account dashboards in your monitoring accounts. These dashboards can include graphs of metrics from source accounts and CloudWatch Logs Insights widgets with queries of log groups from source accounts. Additionally, alarms that you create in the monitoring account can watch metrics in source accounts.

You can monitor and troubleshoot applications that span multiple accounts within a Region. You can seamlessly search, visualize, and analyze your metrics, logs, traces, and Amazon CloudWatch Application Insights applications in any of the linked accounts without account boundaries.

You can set up one or more AWS accounts as monitoring accounts and link them with multiple source accounts. A monitoring account is a central AWS account that can view and interact with observability data generated from source accounts. A source account is an individual AWS account that generates observability data for the resources that reside in it. Source accounts share their observability data with the monitoring account.

With CloudWatch cross-account observability, you can do the following in a dashboard of a monitoring account:

* Search, view, and create graphs of metrics that reside in source accounts. A single graph can include metrics from multiple accounts.
* Create alarms in the monitoring account that watch metrics in source accounts.
* View the log events from log groups located in source accounts, and run CloudWatch Logs Insights queries of log groups in source accounts. A single CloudWatch Logs Insights query in a monitoring account can query multiple log groups in multiple source accounts at once.
* View nodes from source accounts in a trace map in X-Ray. You can then filter the map to specific source accounts.

#### Cross-account cross-Region dashboards

You can create cross-account cross-Region dashboards, which summarize your CloudWatch data from multiple AWS accounts and multiple Regions into one dashboard. From this high-level dashboard you can get a view of your entire application, and also drill down into more specific dashboards without having to sign in and out of accounts or switch Regions.

You can create cross-account cross-Region dashboards on the AWS Management Console and programmatically. Before you can create a **cross-account cross-Region dashboard**, you must **enable at least one sharing account** and **at least one monitoring account**. Additionally, to be able to use the CloudWatch console to create a **cross-account dashboard**, you must **enable the console for cross-account functionality**.

#### Creating a CloudWatch dashboard

You can create multiple dashboards, and you can add dashboards to a favorites list. You aren't limited to the number of dashboards that you can have in your AWS account. All dashboards are global. They are not Region-specific.

The following example shows you how to create a dashboard from the CloudWatch console.

1. Open the CloudWatch console. In the left navigation pane, choose **Dashboards**.

    ![Screenshot of the CloudWatch console with the Dashboards link highlighted in the navigation pane.](./images/W06Img041LoggingCloudWatchCreateDashboardStep1.png)

2. On the **Dashboards** page, choose **Create dashboard**.

    ![Screenshot of CloudWatch Dashboards page. In the Custom Dashboards section, the Create dashboard button is highlighted.](./images/W06Img042LoggingCloudWatchCreateDashboardStep2.png)

3. In the **Create new dashboard** dialog box, enter a name for the dashboard, and then choose **Create dashboard**.

    ![Create new dashboard dialog box.](./images/W06Img043LoggingCloudWatchCreateDashboardStep3.png)

4. The **Add widget** dialog box appears. Choose the types of widgets that you want to add. In this example, the **Bar** widget is selected. Choose **Next**.

    ![Add widget dialog box with Bar widget selected.](./images/W06Img044LoggingCloudWatchCreateDashboardStep4.png)

5. Following the **Bar** widget example, the **Add metric graph** dialog box appears. Select the metrics that you want to add, and then choose **Create widget**.

    ![Add metric graph dialog box.](./images/W06Img045LoggingCloudWatchCreateDashboardStep5.png)

6. Choose **Save** to save the dashboard settings.

    ![Save dashboard page is displayed with the Save button highlighted.](./images/W06Img046LoggingCloudWatchCreateDashboardStep6.png)

### Sharing your dashboards

You can share your CloudWatch dashboards with people who don't have direct access to your AWS account. You can share dashboards across teams, with stakeholders, and with people external to your organization.

When you share dashboards, you can designate who can view the dashboard in the following three ways:

* Share a single dashboard and designate specific email addresses of the people who can view the dashboard. Each of these users creates their own password that they must enter to view the dashboard.
* Share a single dashboard publicly, so that anyone who has the link can view the dashboard.
* Share all the CloudWatch dashboards in your account and specify a third-party single sign-on (SSO) provider for dashboard access. All users who are members of this SSO provider's list can access all the dashboards in the account. To enable this, you integrate the SSO provider with Amazon Cognito. The SSO provider must support SAML 2.0.

When you share a dashboard, by default the permissions that CloudWatch creates restrict access to only the alarms and CloudWatch Contributor Insights rules that are on the dashboard when it is shared. If you add new alarms or Contributor Insights rules to the dashboard, and you want them to be seen by the people whom you shared the dashboard with, you must update the policy to allow these resources.

**All people that you share the dashboard with are granted these permissions for the account. If you share the dashboard publicly, everyone who has the link to the dashboard has these permissions.**

#### Sharing a single dashboard with specific users

The following example shows you how to share a dashboard with specific email addresses that you choose.

1. Go to the CloudWatch **Dashboards** page and choose the name of your dashboard.

    ![CloudWatch Dashboards page with two dashboard names. One of the dashboard names is highlighted.](./images/W06Img051LoggingCloudWatchShareDashboardStep1.png)

2. Choose **Actions** > **Share dashboard**.

    ![On the test-dashboard-12345 dashboard page, the Share dashboard link is highlighted on the Actions drop-down menu.](./images/W06Img052LoggingCloudWatchShareDashboardStep2.png)

3. In the **Share your dashboard and require a username and password** section, choose **Start sharing**.

    |[Share your dashboard and require a username and password section is highlighted.](./images/W06Img053LoggingCloudWatchShareDashboardStep3.png)

4. In the **Add email addresses** text box, enter the email addresses that you want to share the dashboard with. When you have all the email addresses entered, read the agreement, and then choose **Confirm and preview policy**.

    ![Username and password protected dashboard page, with the Confirm and preview policy button highlighted.](./images/W06Img054LoggingCloudWatchShareDashboardStep4.png)

5. The **Accept dashboard sharing policy** dialog box appears. Confirm that the resources that will be shared are correct, and choose **Accept policy and generate shareable link**.

    ![Accept dashboard sharing policy dialog box with Accept policy and generate shareable link button highlighted.](./images/W06Img055LoggingCloudWatchShareDashboardStep5.png)

6. On the next page, choose **Copy link**. You can then paste this link into an email message and send it to the invited users. They automatically receive a separate email with their username and a temporary password to use to connect to the dashboard.

    ![Copy link button is highlighted.](./images/W06Img056LoggingCloudWatchShareDashboardStep6.png)

### CloudWatch Synthetics and CloudWatch RUM

#### Performance monitoring

Customer experience directly influences the success and adoption of cloud-based solutions. A positive customer experience ensures that end users can seamlessly interact with and derive value from the applications and services hosted in the cloud. But how can you monitor the performance of your applications and check the customer experience?

Synthetic monitoring and real user monitoring (RUM) are two approaches for monitoring and providing insight into web performance. Synthetic and RUM monitoring provide for different views of performance, and each have their own benefits. Synthetic monitoring is very well suited to regression testing and mitigating shorter-term performance issues during development. RUM is generally best suited for understanding long-term trends.

##### Synthetic monitoring

Synthetic monitoring involves monitoring the performance of a page in a laboratory setting, typically with automation tooling in a consistent-as-possible environment. Synthetic monitoring involves deploying scripts to simulate the path that an end-user might take through a web application. It will then report back the performance that the simulator experiences. The traffic measured is not of your actual users, but rather synthetically generated traffic collecting data on page performance.

Synthetic monitoring can be an important component of regression testing and production site monitoring. Regression testing is performed after an update to ensure that changes haven't impacted existing functionality. You should test the site at every stage of development and regularly in production.

If an issue arises in production, synthetic monitoring can provide insight. It helps identify, isolate, and resolve problems before these problems negatively affect user experience.

##### Real user monitoring (RUM)

RUM measures the performance of a page from real users' devices. Generally, a third-party script injects a script on each page to measure and report back on page load data for every request made. This technique monitors an application's actual user interactions.

In RUM, the browsers of real users report back performance metrics experienced. RUM helps identify how an application is being used, including the geographic distribution of users and the impact of that distribution on the end-user experience.

Unlike synthetic monitoring, RUM captures the performance of actual users regardless of device, browser, network, or geographic location. As users interact with an application, all performance timings are captured, regardless of what actions are taken or pages viewed.

By using RUM, a business can better understand its users and identify the areas on its site that require the most attention. Also, RUM can help to understand the geographic or channel-distribution trends of your users. Knowing your user trends helps you better define your business plan and, from a monitoring perspective, helps you to identify key areas to target for optimization and performance improvements.

### CloudWatch Synthetics

You can use Amazon CloudWatch Synthetics to continually monitor your endpoints and APIs, and you can use CloudWatch Synthetics to create canaries. Canaries are configurable scripts written in Node.js or Python. They create AWS Lambda functions in your account that use Node.js or Python as a framework. Canaries work over both HTTP and HTTPS protocols.

Canaries follow the same routes and perform the same actions as a customer. For example, an ecommerce site could write a canary script to simulate a user adding and removing an item to a shopping cart.

This makes it possible for you to continually verify your customer experience even when you don't have any customer traffic on your applications. By using canaries, you can discover issues before your customers do.

You can run a canary once or on a regular schedule. Canaries can run as often as once per minute. You can use both cron and rate expressions to schedule canaries. Some common uses for synthetics canaries include the following:

* Monitoring for page-load errors
* Providing load latency for application UI
* Monitoring flow in your webpages
* Checking for broken or dead links

![Screenshot of CloudWatch console with Canaries page displayed.](./images/W06Img060LoggingCloudWatchCanaries.png)

Canaries example in the CloudWatch console shows that the current running canary named lab-login-canary has 100 percent success rate for one test run.

By default, canaries create several CloudWatch metrics in the **CloudWatchSynthetics** namespace. These metrics have **CanaryName** as a dimension. Canaries that use the **executeStep()** or **executeHttpStep()** function from the function library also have **StepName** as a dimension.

* [**Library Functions Available for Canary Scripts**](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Function_Library.html)

#### Sample code for canary scripts

The following sample code is a canary that fails with a custom error message when a target element is not loaded.

```python
from aws_synthetics.selenium import synthetics_webdriver as webdriver
from aws_synthetics.common import synthetics_logger as logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def custom_selenium_script():
    # create a browser instance
    browser = webdriver.Chrome()
    browser.get('https://www.example.com/')
    logger.info('navigated to home page')
    # set cookie
    browser.add_cookie({'name': 'foo', 'value': 'bar'})
    browser.get('https://www.example.com/')
    # save screenshot
    browser.save_screenshot('signed.png')
    # expected status of an element
    button_condition = EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-button'))
    # add custom error message on failure
    WebDriverWait(browser, 5).until(button_condition, message='Submit button failed to load').click()
    logger.info('Submit button loaded successfully')
    # browser will be quit automatically at the end of canary run, 
    # quit action is not necessary in the canary script
    browser.quit()

# entry point for the canary
def handler(event, context):
    return custom_selenium_script()
```

### CloudWatch RUM

With Amazon CloudWatch RUM, you can perform real user monitoring to collect and view client-side data about your web application performance from actual user sessions in near real time. The data that you can visualize and analyze includes page-load times, client-side errors, and user behavior. When you view this data, you can see it all aggregated together and also see breakdowns by the browsers and devices that your customers use.

You can use the collected data to quickly identify and debug client-side performance issues. CloudWatch RUM helps you visualize anomalies in your application performance and find relevant debugging data such as error messages, stack traces, and user sessions. You can also use CloudWatch RUM to understand the range of end user impact, including the number of users, geolocations, and browsers used.

To use CloudWatch RUM, you create an *app monitor* and provide some information. CloudWatch RUM generates a JavaScript snippet for you to paste into your application. The snippet pulls in the RUM web client code. The RUM web client captures data from a percentage of your application's user sessions, which is displayed in a pre-built dashboard. You can specify what percentage of user sessions to gather data from.

End-user data that you collect for CloudWatch RUM is retained for 30 days and then automatically deleted. If you want to keep the RUM events for a longer time, you can choose to have the app monitor send copies of the events to Amazon CloudWatch Logs in your account. Then, you can adjust the retention period for that log group.

With CloudWatch RUM, you incur charges for every RUM event that CloudWatch RUM receives. Each data item collected using the RUM web client is considered a RUM event. Examples of RUM events include a page view, a JavaScript error, and an HTTP error. You have options for which types of events are collected by each app monitor. You can activate or deactivate options to collect performance telemetry events, JavaScript errors, HTTP errors, and X-Ray traces.

#### Performance considerations of using CloudWatch RUM

##### Load performance impact

The RUM web client can be installed in your web application as a JavaScript module, or it can be loaded into your web application asynchronously from a content delivery network (CDN). It does not block the application’s load process. CloudWatch RUM is designed for there to be no perceptible impact to the application’s load time.

##### Runtime impact

The RUM web client performs processing to record and dispatch RUM data to the CloudWatch RUM service. Because events are infrequent and the amount of processing is small, CloudWatch RUM is designed for there to be no detectable impact to the application’s performance.

##### Network impact

The RUM web client periodically sends data to the CloudWatch RUM service. Data is dispatched at regular intervals while the application is running, and also immediately before the browser unloads the application. Data sent immediately before the browser unloads the application is sent as beacons, which are designed to have no detectable impact on the application’s unload time.

#### Regionalization

The following examples illustrate strategies for using CloudWatch RUM with applications in different Regions.

##### Your web application is deployed in multiple AWS Regions

If your web application is deployed in multiple AWS Regions, you have three options:

* Deploy one app monitor in one Region, in one account, serving all Regions.
* Deploy separate app monitors for each Region, in unique accounts.
* Deploy separate app monitors for each Region, all in one account.

The advantage of using one app monitor is that all data will be centralized into one visualization, and all logs are written to the same log group in CloudWatch Logs. With a single app monitor, there is a small amount of extra latency for requests, and a single point of failure.

Using multiple app monitors removes the single point of failure but prevents all data from being combined into one visualization.

##### CloudWatch RUM hasn't launched in some Regions that your application is deployed in

CloudWatch RUM is launched into many Regions and has wide geographical coverage. By setting up CloudWatch RUM in the Regions where it is available, you can get the benefits. End users can be anywhere and still have their sessions included if you have set up an app monitor in the Region that they are connecting to.

However, CloudWatch RUM is not yet launched in AWS GovCloud (US-East), AWS GovCloud (US-West), or any Regions in China. You are not able to send data to CloudWatch RUM from these Regions.

### CloudWatch Logs Insights

Let's consider a scenario where an ecommerce organization aims to enhance the performance and security of its online platform. As the company experiences a surge in user traffic during a major sale, the development and operations team notices a sudden increase in error messages within the application logs. What tool could they use to address this issue and ensure a seamless shopping experience for their users?

#### Analyzing log data with CloudWatch Logs Insights

Amazon CloudWatch Logs Insights helps you efficiently identify patterns, interactively search, and analyze your log data with bar charts, line charts, and stacked area charts. You can perform queries to respond to operational or network issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes.

CloudWatch Logs Insights generates visualizations for queries that use the stats function and one or more aggregation functions.

After you have created a query, you can save the following:

* Queries, and you can run them again later
* Queries in a folder structure to help you keep them organized
* 1,000 CloudWatch Logs Insights queries, per Region per account

After you run a query, you can add the query to a CloudWatch dashboard or copy the results to the clipboard. Queries added to dashboards run every time you load the dashboard and every time that the dashboard refreshes. These queries count toward your limit of 10 concurrent CloudWatch Logs Insights queries.

##### Identification

Performing queries helps you more efficiently and effectively respond to operational issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes.

##### Purpose-built query language

CloudWatch Logs Insights includes a purpose-built query language with a few simple but powerful commands. CloudWatch Logs Insights provides sample queries, command descriptions, query autocompletion, and log field discovery to help you get started. Sample queries are included for several types of AWS service logs.

##### Automatic discovery

CloudWatch Logs Insights automatically discovers fields in logs from AWS services, such as Amazon Route 53, AWS Lambda, AWS CloudTrail, and Amazon Virtual Private Cloud (Amazon VPC), and any application or custom log that emits log events as JSON.

A single request can query up to 50 log groups. Queries time out after 60 minutes, if they have not completed. Query results are available for 7 days.

You can save queries that you have created. This can help you run complex queries when you need to, without having to re-create them each time that you want to run them.

**Note**: CloudWatch Logs Insights queries incur charges based on the amount of data that is queried.

##### Logs

CloudWatch Logs Insights supports different log types. For every log that's sent to CloudWatch Logs, CloudWatch Logs Insights automatically generates five system fields:

* **@message** contains the raw, unparsed log event. This is the equivalent of the **message** field in [InputLogEvent](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.html).
* **@timestamp** contains the event timestamp in the log event's timestamp field. This is the equivalent of the **timestamp** field in [InputLogEvent](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.html).
* **@ingestionTime** contains the time when CloudWatch Logs received the log event.
* **@logStream** contains the name of the log stream that the log event was added to. Log streams group logs through the same process that generated them.
* **@log** is a log group identifier in the form of **account-id:log-group-name**. When you query multiple log groups, this can be useful to identify which log group a particular event belongs to.

CloudWatch Logs Insights inserts the **@** symbol at the start of fields for logs that it automatically processes. Logs not automatically processed by CloudWatch can be processed by using the **parse** command to extract and create ephemeral fields for use in that query.

If the name of a discovered log field starts with the **@** character, CloudWatch Logs Insights displays it with an additional @ appended to the beginning. For example, if a log field name is **@example.com**, this field name is displayed as **@@example.com**.

**If your network security team doesn't allow the use of web sockets, you can't currently access the CloudWatch Logs Insights portion of the CloudWatch console. You can use the CloudWatch Logs Insights query capabilities by using APIs. For more information, see [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html) in the Amazon CloudWatch Logs API Reference.**

#### CloudWatch Logs Insights query syntax

With CloudWatch Logs Insights, you use a query language to query your log groups. The query syntax supports different functions and operations that include, but aren't limited to general functions, arithmetic and comparison operations, and regular expressions.

To create queries that contain multiple commands, separate the commands with the pipe character (**|**). To create queries that contain comments, set off the comments with the hash character (**#**).

##### The following table describes each command

| Command | Description |
| ------- | ----------- |
| **display** | Displays a specific field or fields in query results. |
| **fields** | Displays specific fields in query results and supports functions and operations that you can use to modify field values and create new fields to use in your query. |
| **filter** | Filters the query to return only the log events that match one or more conditions. |
| **pattern** | Automatically clusters your log data into patterns. A pattern is shared text structure that recurs among your log fields. |
| **parse** | Extracts data from a log field to create an extracted field that you can process in your query. It supports glob mode using wildcards, and also regular expressions. |
| **sort** | Displays the returned log events in ascending (asc) or descending (desc) order. |
| **stats** | Calculates aggregate statistics using values in the log fields. |
| **limit** | Specifies a maximum number of log events that you want your query to return. Useful with sort to return "top 20" or "most recent 20" results. |
| **dedup** | Removes duplicate results based on specific values in fields that you specify. |
| **unmask** | Displays all the content of a log event that has some content masked because of a data protection policy. |

#### Sample queries

The following section demonstrates five general and useful query commands that you can run in the CloudWatch console.

##### Example 1: Find the 25 most recently added log events

```sql
fields @timestamp, @message | sort @timestamp desc | limit 25
```

##### Example 2: Get a list of the number of exceptions per hour

```sql
filter @message like /Exception/
    | stats count(*) as exceptionCount by bin(1h)
    | sort exceptionCount desc
```

##### Example 3: Get a list of log events that aren't exceptions

fields @message | filter @message not like /Exception/

##### Example 4: Get the most recent log event for each unique value of the **server** field

```sql
fields @timestamp, server, severity, message
| sort @timestamp desc
| dedup server
```

##### Example 5: Get the most recent log event for each unique value of the **server** field for each **severity** type

```sql
fields @timestamp, server, severity, message
| sort @timestamp desc
| dedup server, severity
```

### CloudWatch Metrics Insights

In the previous scenario, an ecommerce organization faces increased user traffic during a major sale. The team also wants to optimize their online platform's performance. They will need to explore hundreds of metrics like latency, error rates, database response times, and resource utilization. How can they easily gain a comprehensive understanding of how different components of the system are behaving during the surge in traffic? For example, how can they identify which servers are experiencing increased load or if there is a spike in error rates for specific API calls?

#### Querying your metrics with CloudWatch Metrics Insights

Amazon CloudWatch Metrics Insights is a powerful high-performance SQL query engine that you can use to query your metrics at scale. You can identify trends and patterns within all of your CloudWatch metrics in real time.

You can also set alarms on any CloudWatch Metrics Insights queries that return a single time series. This is especially useful when you create alarms that watch aggregated metrics across a fleet of your infrastructure or applications. You create the alarm once, and the alarm dynamically adjusts as resources are added to or removed from the fleet.

You can use the CloudWatch console to perform a CloudWatch Metrics Insights query, or you can use **GetMetricData** or **PutDashboard** with the AWS CLI or the AWS SDKs. Queries run in the console are free of charge.

When you use the CloudWatch console, you can choose from a wide variety of pre-built sample queries and also create your own queries. When you create a query, you can use the builder view, the editor view, or a combination of both. An interactive builder view lets you browse through your existing metrics and dimensions to build a query. An editor view helps you write new queries. You can also use the editor view to edit the queries that you build in the builder view, and edit sample queries to customize them.

![Screenshot of CloudWatch Metrics Insights - query builder page on the Multi-source query tab in the console.](./images/W06Img062LoggingCloudWatchMetricsInsights.png)

You can create your queries on the **All metrics page** in the CloudWatch console. The query builder is on the **Multi source query** tab, and you can use the **Builder** view or the **Editor** view.

By using the **GROUP BY** clause, you can flexibly group your metrics in real time into separate time series per specific dimension value, based on your use cases. Because CloudWatch Metrics Insights queries include an **ORDER BY** ability, you can use CloudWatch Metrics Insights to make *Top N* type queries. For example, you can scan millions of metrics in your account, and return only the top 10 most CPU consuming instances. This helps you pinpoint and remedy latency issues in your applications.

#### Query components and syntax

CloudWatch Metrics Insights syntax is as follows.

```sql
SELECT FUNCTION(metricName)
FROM namespace | SCHEMA(...)
[ WHERE labelKey OPERATOR labelValue [AND ... ] ]
[ GROUP BY labelKey [ , ... ] ]
[ ORDER BY FUNCTION() [ DESC | ASC ] ]
[ LIMIT number ]
```

**None of the keywords are case-sensitive, but the identifiers such as the names of metrics, namespaces, and dimensions are case-sensitive.**

#### The possible clauses in a CloudWatch Metrics Insights query

##### SELECT

**SELECT** is required. It specifies the function to use to aggregate observations in each time bucket (determined by the provided period). It also specifies the name of the metric to query.

The valid values for **FUNCTION** are **AVG**, **COUNT**, **MAX**, **MIN**, and **SUM**.

* **AVG** calculates the average of the observations matched by the query.
* **COUNT** returns the count of the observations matched by the query.
* **MAX** returns the maximum value of the observations matched by the query.
* **MIN** returns the minimum value of the observations matched by the query.
* **SUM** calculates the sum of the observations matched by the query.

##### FROM

**FROM** is required. It specifies the source of the metric. You can specify either the metric namespace that contains the metric that is to be queried, or a **SCHEMA** table function. Examples of metric namespaces include **"AWS/EC2"**, **"AWS/Lambda"**, and metric namespaces that you have created for your custom metrics.

Metric namespaces that include **/** or any other character that is not a letter, number, or underscore must be surrounded by double quotation marks.

**SCHEMA** is an optional table function that can be used within a **FROM** clause. Use **SCHEMA** to scope down the query results to only the metrics that exactly match a list of dimensions, or to metrics that have no dimensions.

If you use a **SCHEMA** clause, it must contain at least one argument, and this first argument must be the metric namespace being queried. If you specify **SCHEMA** with only this namespace argument, the results are scoped down to only metrics that do not have any dimensions.

If you specify **SCHEMA** with additional arguments, the additional arguments after the namespace argument must be label keys. Label keys must be dimension names. If you specify one or more of these label keys, the results are scoped down to only those metrics that have that exact set of dimensions. The order of these label keys does not matter.

For example:

* **SELECT AVG(CPUUtilization) FROM "AWS/EC2"** matches all **CPUUtilization** metrics in the **AWS/EC2** namespace, no matter their dimensions, and returns a single aggregated time series.
* **SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2")** matches only the **CPUUtilization** metrics in the **AWS/EC2** namespace that **do not have any dimensions defined**.
* **SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2", InstanceId)** matches only the **CPUUtilization** metrics that were reported to CloudWatch with exactly one dimension, **InstanceId**.
* **SELECT SUM(RequestCount) FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone)** matches only the **RequestCount** metrics that were reported to CloudWatch from **AWS/ApplicationELB** with exactly two dimensions, **LoadBalancer** and **AvailabilityZone**.

##### WHERE

**WHERE** is optional. It filters the results to only those metrics that match your specified expression using specific label values for one or more label keys. For example, **WHERE InstanceType = 'c3.4xlarge'** filters the results to only **c3.4xlarge** instance types, and **WHERE InstanceType != 'c3.4xlarge'** filters the results to all instance types **except c3.4xlarge**.

Label values must always be enclosed with single quotation marks.

The **WHERE** clause supports the following operators:

* **=** Label value must match the specified string.
* **!=** Label value must not match the specified string.
* **AND** Both conditions that are specified must be true to match. You can use multiple AND keywords to specify two or more conditions.

##### GROUP BY

**GROUP BY** is optional. It groups the query results into multiple time series, each one corresponding to a different value for the specified label key or keys. For example, using **GROUP BY InstanceId** returns a different time series for each value of **InstanceId**. Using **GROUP BY ServiceName, Operation** creates a different time series for each possible combination of the values of **ServiceName** and **Operation**.

With a **GROUP BY** clause, by default the results are ordered in alphabetical ascending order, using the sequence of labels specified in the **GROUP BY** clause. To change the order of the results, add an **ORDER BY** clause to your query.

##### ORDER BY

**ORDER BY** is optional. It specifies the order to use for the returned time series, if the query returns more than one time series. The order is based on the values found by the **FUNCTION** that you specify in the **ORDER BY** clause. The **FUNCTION** is used to calculate a single scalar value from each returned time series, and that value is used to determine the order.

You also specify whether to use ascending **ASC** or descending **DESC** order. If you omit this, the default is ascending **ASC**.

For example, adding an **ORDER BY MAX() DESC** clause orders the results by the maximum data point observed within the time range, in descending order, meaning that the time series that has the highest maximum data point is returned first.

The valid functions to use within an **ORDER BY** clause are **AVG()**, **COUNT()**, **MAX()**, **MIN()**, and **SUM()**.

If you use an **ORDER BY** clause with a **LIMIT** clause, the resulting query is a *Top N* query. **ORDER BY** is also useful for queries that might return a large number of metrics, because each query can return no more than 500 time series. If a query matches more than 500 time series, and you use an **ORDER BY** clause, the time series are sorted and then the 500 time series that come first in the sort order are the ones that are returned.

##### LIMIT

**LIMIT** is optional. It limits the number of time series returned by the query to the value that you specify. The maximum value that you can specify is 500, and a query that does not specify a **LIMIT** can also return no more than 500 time series. Using a **LIMIT** clause with an **ORDER BY** clause gives you a *Top N* query.

##### Quotation marks or escape characters

In a query, label values must always be surrounded with single quotation marks. For example, **SELECT MAX(CPUUtilization) FROM "AWS/EC2" WHERE AutoScalingGroupName = 'my-production-fleet'**.

Metric namespaces, metric names, and label keys that contain characters other than letters, numbers, and underscore (**_**) must be surrounded by double quotation marks. For example, **SELECT MAX("My.Metric")**.

If one of these contains a double quotation mark or single quotation mark itself (such as **Bytes"Input"**), you must escape each quotation mark with a backslash, as in **SELECT AVG("Bytes\"Input\"")**.

If a metric namespace, metric name, or label key contains a word that is a reserved keyword in CloudWatch Metrics Insights, these must also be enclosed in double quotation marks. For example, if you have a metric named **LIMIT**, you would use **SELECT AVG("LIMIT")**. It is also valid to enclose any namespace, metric name, or label in double quotation marks even if it does not include a reserved keyword.

* [**Reserved Keywords**](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-reserved-keywords.html)

#### Sample queries

The following five examples show you some useful CloudWatch Metrics Insights queries that you can use.

##### Example 1: CPU utilization of EC2 instances sorted by highest

```sql
SELECT AVG(CPUUtilization)
  FROM SCHEMA("AWS/EC2", InstanceId)
  GROUP BY InstanceId
  ORDER BY AVG() DESC
```

##### Example 2: Average CPU utilization across the entire fleet

```sql
SELECT AVG(CPUUtilization)
FROM SCHEMA("AWS/EC2", InstanceId)
```

##### Example 3: Top 10 instances by highest CPU utilization

```sql
SELECT MAX(CPUUtilization)
FROM SCHEMA("AWS/EC2", InstanceId)
GROUP BY InstanceId
ORDER BY MAX() DESC
LIMIT 10
```

##### Example 4: Total requests across all load balancers

```sql
SELECT SUM(RequestCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer)
```

##### Example 5: Top 10 most active load balancers

```sql
SELECT MAX(ActiveConnectionCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer)
GROUP BY LoadBalancer
ORDER BY SUM() DESC
LIMIT 10
```

### [Lab: Collecting and Analyzing Logs with Amazon CloudWatch Logs Insights](./labs/W060Lab1LoggingCloudWatchLogsInsights.md)

In this lab, you learn to use Amazon CloudWatch Logs Insights to interactively search and analyze log data in Amazon CloudWatch Logs. You set up log groups and log streams in CloudWatch Logs and run queries against Amazon Virtual Private Cloud (Amazon VPC) flow logs and database logs to detect potential security vulnerabilities.

In this lab, you perform the following tasks:

* Install and configure the Amazon CloudWatch agent on the Amazon Elastic Compute Cloud (Amazon EC2) instances by using AWS Systems Manager.
* Collect web server and system logs from an Amazon EC2 instance and publish them into CloudWatch Logs.
* Enable Amazon VPC Flow Logs across virtual private clouds (VPCs) and subnets.
* Enable CloudWatch Logs for an Amazon Relational Database Service (Amazon RDS) database instance.
* Use CloudWatch Logs Insights to explore logs.
* Use CloudWatch Logs Insights and CloudWatch metrics to inspect logs.

### CloudWatch Contributor Insights for Security

#### CloudWatch Contributor Insights

Amazon CloudWatch Contributor Insights is a tool designed to help organizations gain a deeper understanding of their system and application behavior by analyzing log data. CloudWatch Contributor Insights analyzes time-series data to provide a view of the top contributors that influence system performance. This can be beneficial for troubleshooting, optimizing performance, and enhancing the overall reliability of applications and systems. After it is set up, CloudWatch Contributor Insights runs continuously without requiring additional user intervention. This helps developers and operators more quickly isolate, diagnose, and remediate issues during an operational event.

You can use CloudWatch Contributor Insights to analyze log data and create time series that display contributor data. You can see metrics about the Top-N contributors, the total number of unique contributors, and their usage. This helps you find the most active users and understand who or what is impacting system performance. For example, you can find bad hosts, identify the heaviest network users, or find the URLs that generate the most errors.

You can build your rules from scratch. When you use the AWS Management Console, you can also use sample rules that AWS has created. Rules define the log fields that you want to use to define contributors, such as **IpAddress**. All rules analyze incoming data in real time. You can also filter the log data to find and analyze the behavior of individual contributors.

CloudWatch also provides built-in rules that you can use to analyze metrics from other AWS services. If you are signed in to an account that is set up as a monitoring account in CloudWatch cross-account observability, you can create CloudWatch Contributor Insights rules in that monitoring account that analyze log groups in both source accounts and in the monitoring account. You can also create a single rule that analyzes log groups in multiple accounts.

**If you use CloudWatch Contributor Insights, you are charged for each occurrence of a log event that matches a rule.**

### Analyzing VPC flow logs with CloudWatch Contributor Insights to improve security

You can use rules in CloudWatch Contributor Insights to gain security visibility into your VPC flow logs. The rules analyze flow logs in targeted groups in Amazon CloudWatch Logs and display the Top-N contributors for a given log field or combination of log fields.

For example, you can produce a list of the Top-N contributors based on data transferred or blocked requests. You can add filters to these rules to count only those log events that meet a certain criteria (for example, blocked requests by source IP when the destination port is 22).

#### VPC Flow Logs

VPC Flow Logs is a feature that you can use to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to the following locations: CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), or Amazon Data Firehose. After you create a flow log, you can retrieve and view the flow log records in the log group, bucket, or delivery stream that you configured.

Flow logs can help you with a number of tasks, such as the following:

* Diagnosing overly restrictive security group rules
* Monitoring the traffic that is reaching your instance
* Determining the direction of the traffic to and from the network interfaces

Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance.

##### the default logging format of a flow log

```log
<version> <account-id> <interface-id> <srcaddr> <dstaddr> <srcport> <dstport> <protocol> <packets> <bytes> <start> <end> <action> <log-status>
```

VPC Flow Logs supports the addition of metadata to log entries, such as VPC ID, instance ID, and TCP flags. You can customize the order of these fields. Rules in CloudWatch Contributor Insights are built by matching the field position in the log event with the name of the field or alias. In the default logging format, the position of the **\<interface-id\>** field is 3, but this might not be the case if you are using a customized logging format.

For example, with the default logging format, if you want to track the Top-N contributors for the number of bytes transferred by unique source IP addresses, you need to change the positions of the **\<bytes\>** and **\<srcaddr\>** fields. In the default logging format, **\<srcaddr\>** maps to position 4 and **\<bytes\>** maps to position 10.

* [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

### Using a CloudWatch Contributor Insights rule to evaluate VPC flow log groups

A CloudWatch Contributor Insights rule is applied to one or many CloudWatch log groups. You can have a single rule apply to VPC flow logs for an entire AWS account in a selected AWS Region or across an AWS Organizations account in a selected Region. 

This is valuable because you can use a single rule to track the Top-N contributors across all of your flow logs in a Region. For example, you can track the Top-N contributors by aggregating the number of rejected requests by source IP and destination port. You can add more contributors to show the top rejected requests by source IP, destination port, interface ID, or subnet ID.

If all of your VPC flow logs share a prefix name in CloudWatch Logs, such as **/vpc/flowlogs/\***, you can create a rule that applies to every CloudWatch log group that shares this prefix name.

#### Creating a custom rule to track top SSH connections by source address and action

Using security-focused rules, you can get a better understanding about which source IPs are generating the largest number of accepted or rejected requests on a given port. This allows security teams to quickly identify and react to a potential security incident.

The following example shows how you can create a custom rule that counts the number of requests over port 22 by source IP address and action. But you can edit the rule to show denied actions for any port number.

To create a custom rule, follow these steps:

1. Open the CloudWatch console.
2. In the navigation pane, choose **Contributor Insights**.
3. Choose **Create rule**.

You can either use the wizard or syntax to create the custom rule. The following syntax is used for this example.

```json
{
    "Schema": {
        "Name": "CloudWatchLogRule",
        "Version": 1
    },
    "AggregateOn": "Count",
    "Contribution": {
        "Filters": [
            {
                "Match": "dstport",
                "EqualTo": 22
            }
        ],
        "Keys": [
            "srcaddr",
            "dstaddr",
            "action"
        ]
    },
    "LogFormat": "CLF",
    "LogGroupNames": [
        "/vpc/flowlogs/*"
    ],
    "Fields": {
        "4": "srcaddr",
        "5": "dstaddr",
        "7": "dstport",
        "10": "bytes",
        "13": "action"
    }
}
```

For the rule name, let's assume that this example is named **SSH-by-source-ip-and-action**.

#### Viewing the rule report

Now you’re ready to view the reports from the **SSH-by-source-ip-and-action** rule. Depending on the aggregation interval of your VPC flow logs (1 minute or 10 minutes), it might take some time before the results appear on the graph.

To view your rule report, you can go back to the CloudWatch console and choose **Contributor Insights**. You can then choose the rule that you want to review. The following example demonstrates the custom rule that counts the number of requests over port 22 by source IP address and action with the following filters:

* **Contributors**: Top 10
* **Period**: 1 minute
* **Order by**: Sum
* **Widget type**: Line
* **Time range**: 3h

The following Contributor Insights custom rule graph shows Top 10 contributors with a 1 minute period, ordered by Sum with time range 3h enabled.

![Screenshot of Contributor Insights custom rule graph](./images/W06Img064LoggingCloudWatchContributorInsights.png)

The **srcaddr** field displays the private IP address of the NAT gateway network interface and the action displays **REJECT**.

#### Using rule metrics to track accepted or rejected traffic

You can use the **INSIGHT_RULE_METRIC** metric match expression to display metrics from the Contributor Insights rule, and you can use it to track accepted and rejected traffic across VPCs by applying the following built-in rules:

* Traffic by Source Address and Rejected Action
* Traffic by Source Address and Action

To use these built-in rules, you can open the CloudWatch console. In the navigation pane, choose **All metrics**, and then use the following JSON on the **Source** tab.

![Screenshot of CloudWatch console with All metrics page displayed and Source tab chosen.](./images/W06Img066LoggingCloudWatchAllMetricsSource.png)

```json
{
          "metrics": [
                  [
                        {
                               "expression": "INSIGHT_RULE_METRIC('Traffic-by-Source Address-and-Rejected-Action’, 'Sum')",
                               "label": "Rejects",
                               "id": "e1",
                               "period": 60,
                               "color": "#ff7f0e"
                         }
                  ],
                 [
                        {
                                "expression": "INSIGHT_RULE_METRIC('Traffic-by-Source-Address-and-Action', 'Sum')",
                                "label": "Requests",
                                "id": "e2",
                                "period": 60,
                                "visible": false
                         }
                  ],
                  [
                        {
                                 "expression": "e2-e1",
                                 "label": "Accepts ",
                                 "id": "e3",
                                 "color": "#1f77b4"
                        }
                  ]
           ],
           "region": "us-east-2",
           "view": "timeSeries",
           "stacked": true,
           "stat": "Average",
           "period": 60
}
```

You would replace the rule names of **Traffic-by-Source Address-and-Rejected-Action** and **Traffic-by-Source-Address-and-Action** with the names that you defined when you created the rule.

Then, you would see a result graph similar to the following.

![Example screenshot of Metric math expression showing accepted and rejected VPC connections.](./images/W06Img068LoggingCloudWatchContrubutionRuleDashboard.png)

CloudWatch Contributor Insights report views can be a valuable addition to a new or existing operational or security dashboard. The CloudWatch dashboard views are powerful because you can scope these rules to a workload or track contributors for all VPC flow logs across an organization.

Remember that charges for CloudWatch Contributor Insights are based on the number of rules and the number of events that match a given rule. A higher volume of VPC flow log data will result in higher charges. Disabling a rule will prevent service charges due to matched events, and deleting a rule will prevent both service charges from **matched events** and for **the existence of a rule**.

### Amazon CloudWatch Evidently

Let's think about this scenario. You are part of a dynamic development team striving to roll out new features for a web application. As the team prepares for a major update, the challenges arise. How can you seamlessly introduce and test these features without disrupting the user experience or risking unforeseen issues?

#### Performing launches and A/B experiments

You can use Amazon CloudWatch Evidently to safely validate new features by serving them to a specified percentage of your users while you roll out the features. You can monitor the performance of a new feature to help you decide when to ramp up traffic to your users. This helps you reduce risk and identify unintended consequences before you fully launch the feature.

You can also conduct A/B experiments to make feature design decisions based on evidence and data. An experiment can test as many as five variations at once. CloudWatch Evidently collects experiment data and analyzes it using statistical methods. It also provides clear recommendations about which variations perform better. You can test both user-facing features and backend features.

Evidently charges your account based on Evidently events and Evidently analysis units. Evidently events include data events such as clicks and page views, and assignment events that determine the feature variation to serve to a user. Evidently analysis units are generated from Evidently events, based on rules that you have created in Evidently. Analysis units are the number of rule matches on events.

For example, a user click event might produce a single Evidently analysis unit, a click count. Another example is a user checkout event that might produce two Evidently analysis units: checkout value and the number of items in a cart.

![Checkout page screenshot](./images/W06Img070LoggingCloudWatchEvidentlyCheckoutPageExample.png)

#### How Evidently calculates results

In an A/B test, users are randomly assigned to either the control group (also called the default variation), or one of the treatment groups (also called the tested variations). For example, users in the control group might experience the website, service, or application in the same way that they did before the experiment started. Meanwhile, users in the treatment group might experience the change.

Evidently supports up to five different variations in an experiment, and it randomly assigns traffic to these variations. This way, you can track business metrics (such as revenue) and performance metrics (such as latency) for each group. Evidently does the following:

* Compares the treatment with the control (for example, compares whether revenue increases or decreases with a new checkout process).
* Indicates whether the observed difference between the treatment and the control is significant. For this, Evidently offers two approaches: *frequentist significance levels* and *Bayesian probabilities*.

So why should you use frequentist and Bayesian approaches? Consider a case where the treatment has no effect compared to the control, or a case where the treatment is identical to the control (an A/A test). You would still observe a small difference between the treatment and the control in the data. This is because the test participants consist of a finite sample of users, representing a small percentage of all users of the website, service, or application. Frequentist significance levels and Bayesian probabilities provide insights into whether the observed difference is significant or due to chance. Evidently considers the following to determine whether the observed difference is significant:

* How big the difference is
* How many samples are part of the test
* How the data is distributed

#### Frequentist analysis in Evidently

Evidently uses sequential testing, which avoids the usual problems of *peeking*, a common pitfall of frequentist statistics. Peeking is the practice of checking the results of an ongoing A/B test to stop it and make a decision based on the observed results.

Because the results from Evidently are valid at any time (anytime-valid results), you can peek at results during the experiment and still draw sound conclusions. This can reduce some of the costs of experimentation, because you can stop an experiment before the scheduled time if the results already have significance.

Evidently generates anytime-valid significance levels and anytime-valid 95-percent confidence intervals of the difference between the tested variation and the default variation in the target metric. The **Result** column in the experiment results indicates the tested variation performance.

##### Inconclusive

The significance level is less than 95 percent.

##### Better

The significance level is 95 percent or higher and one of the following is true:

* The lower bound of the 95 percent confidence interval is higher than zero and the metric should increase.
* The upper bound of the 95 percent confidence interval is lower than zero and the metric should decrease.

##### Worse

The significance level is 95 percent or higher and one of the following is true:

* The upper bound of the 95 percent confidence interval is higher than zero and the metric should increase.
* The lower bound of the 95 percent confidence interval is lower than zero and the metric should decrease.

##### Best

The experiment has two or more tested variations in addition to the default variation, and the following conditions are met:

* The variation qualifies for the Better designation.
* One of the following is true:
  * The lower bound of the 95 percent confidence interval is higher than the upper bound of the 95 percent confidence intervals of all the other variations and the metric should increase.
  * The upper bound of the 95 percent confidence interval is lower than the lower bound of the 95 percent confidence intervals of all the other variations and the metric should decrease.

#### Bayesian analysis in Evidently

With Bayesian analysis, you can calculate the probability that the mean in the tested variation is larger or smaller than the mean in the default variation. Evidently performs Bayesian inference for the mean of the target metric by using conjugate priors. With conjugate priors, Evidently can more efficiently infer the posterior distribution needed for the Bayesian analysis.

Evidently waits until the end date of the experiment to compute the results of the Bayesian analysis. The results page displays the following:

* **Probability of increase**: The probability that the mean of the metric in the tested variation is at least 3 percent larger than the mean in the default variation
* **Probability of decrease**: The probability that the mean of the metric in the tested variation is at least 3 percent smaller than the mean in the default variation
* **Probability of no change**: The probability that the mean of the metric in the tested variation lies within ±3 percent of the mean in the default variation

The **Result** column indicates the performance of the variation.

##### Better

The probability of increase is at least 90 percent and the metric should increase, or the probability of decrease is at least 90 percent and the metric should decrease.

##### Worse

The probability of decrease is at least 90 percent and the metric should increase, or the probability of increase is at least 90 percent and the metric should decrease.

#### How Evidently collects and stores data

Evidently collects and stores data related to project configurations so that customers can run experiments and launches. The data includes the following:

* Metadata about projects, features, launches, and experiments
* Metric events
* Evaluation data

Resource metadata is stored in Amazon DynamoDB. The data is encrypted at rest by default, using AWS owned keys. These keys are a collection of AWS Key Management Service (AWS KMS) keys that an AWS service owns and manages for use in multiple AWS accounts. Customers can’t view, manage, or audit the use of these keys. Customers are also not required to take action or change programs to protect the keys that encrypt their data.

Evidently metric events, and evaluation events are delivered directly to customer-owned locations. Data in transit is automatically encrypted with HTTPS. This data will be delivered to customer-owned locations. You can also choose to store evaluation events in Amazon S3 or CloudWatch Logs.

#### Retrieving data using Evidently APIs

##### Project data

To retrieve project data, you can use the following APIs:

* [GetProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetProject.html)
* [ListProjects](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListProjects.html)

##### Feature data

To retrieve feature data, you can use the following APIs:

* [GetFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetFeature.html)
* [ListFeatures](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListFeatures.html)

##### Launch data

To retrieve launch data, you can use the following APIs:

* [GetLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetLaunch.html)
* [ListLaunches](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListLaunches.html)

##### Experiment data

To retrieve experiment data, you can use the following APIs:

* [GetExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperiment.html)
* [ListExperiments](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListExperiments.html)
* [GetExperimentResults](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperimentResults.html)

#### Modifying and deleting data using Evidently APIs

##### Project data

To modify and delete project data, you can use the following APIs:

* [UpdateProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProject.html)
* [DeleteProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteProject.html)

##### Feature data

To modify and delete feature data, you can use the following APIs:

* [UpdateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateFeature.html)
* [DeleteFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteFeature.html)

##### Launch data

To modify and delete launch data, you can use the following APIs:

* [UpdateLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateLaunch.html)
* [DeleteLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteLaunch.html)

##### Experiment data

To modify and delete experiment data, you can use the following APIs:

* [UpdateExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateExperiment.html)
* [DeleteExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteExperiment.html)

### Evidently use cases

Evidently can be used for two similar but distinct use cases: implementing dark launches, also known as feature flags, and A/B testing.

#### Feature flags

Features flags is a software development technique that lets you enable or disable features without needing to deploy your code. It decouples the feature deployment from the release. Features in your code are deployed in advance of the actual release. They stay hidden behind **if-then-else** statements. At runtime, your application code queries a remote service. The service decides the percentage of users who are exposed to the new feature. You can also configure the application behavior for some specific customers, your beta testers for example.

When you use feature flags, you can deploy new code in advance of your launch. Then you can progressively introduce a new feature to a fraction of your customers. During the launch, you monitor your technical and business metrics. If all goes well, you can increase traffic to expose the new feature to additional users. If something goes wrong, you can modify the server-side routing with just one click or API call to present only the old (and working) experience to your customers. This lets you revert back user experience without requiring rollback deployments.

![Feature flags example](./images/W06Img072LoggingCloudWatchEvidentlyFeatureFlags.png)

#### A/B testing

A/B testing shares many similarities with feature flags while still serving a different purpose. A/B tests consist of a randomized experiment with multiple variations. A/B testing lets you compare multiple versions of a single feature, typically by testing the response of a subject to variation A against variation B and determining which of the two is more effective.

For example, let’s imagine an ecommerce website. You might want to experiment with different shapes, sizes, or colors for the checkout button, and then measure which variation has the most impact on revenue.

![A/B Testing example](./images/W06Img074LoggingCloudWatchEvidentlyABTesting.png)

The infrastructure required to conduct A/B testing is similar to the one required by feature flags. You deploy multiple scenarios in your application, and you control how to route part of the customer traffic to one scenario or the other. Then you perform deep-dive statistical analysis to compare the impacts of variations.

Evidently assists in interpreting and acting on experimental results without the need for advanced statistical knowledge. You can use the insights provided by the Evidently statistical engine, such as anytime p-value and confidence intervals, for decision-making while an experiment is in progress.

### [Lab: Monitoring Security with Amazon CloudWatch](./labs/W062Lab2LoggingCloudWatchSecurityMonitoring.md)

As a security engineer at AnyCompany, you are responsible for monitoring the company network and Amazon Elastic Compute Cloud (Amazon EC2) instances for abnormal activity.

In this lab, you will monitor security on the database server with Amazon CloudWatch. You configure the database server to send log files to Amazon CloudWatch. You then create CloudWatch alarms and notifications to alert you to a specified number of login failures on your database server. Finally, you create a CloudWatch alarm and notification to monitor outgoing traffic through a NAT gateway.

In this lab, you perform the following tasks:

* Configure an Amazon Linux 2 instance to send log files to CloudWatch.
* Create CloudWatch alarms and notifications to monitor for failed login attempts.
* Create CloudWatch alarms to monitor network traffic through a NAT gateway.

### High-Resolution Metrics and Alarms and Composite Alarms

#### Metric resolution

In Amazon CloudWatch, each metric is one of the following:

* Standard resolution, with data having a 1-minute granularity
* High resolution, with data at a granularity of 1 second

Metrics produced by AWS services are standard resolution by default. When you publish a custom metric, you can define it as either standard resolution or high resolution. When you publish a high-resolution metric, CloudWatch stores it with a resolution of 1 second, and you can read and retrieve it with a period of 1 second, 5 seconds, 10 seconds, 30 seconds, or any multiple of 60 seconds.

High-resolution metrics give you more immediate visibility and greater granularity into the state and performance of your custom applications, such as observing short-lived spikes and functions. 

If you set an alarm on a high-resolution metric, you can specify a high-resolution alarm with a period of 10 seconds or 30 seconds. Or you can set a regular alarm with a period of any multiple of 60 seconds. There is a higher charge for high-resolution alarms with a period of 10 or 30 seconds. With high-resolution alarms, you can react and take actions faster, and they support the same actions available with standard 1-minute alarms.

Imagine the scenario of invoking alarms when your application's available memory gets low. This is often a transient condition that can be hard to catch with infrequent samples. With high-resolution metrics, you can see, detect (through an alarm), and act on it within seconds.

![Screenshot of low-memory alarm in both standard resolution and high resolution. See image caption for details.]()

This example shows that when you use a high-resolution alarm that is evaluated every 10 seconds, you can see that the alarm gets invoked when available memory gets low. You would not be able to observe this issue when the alarm is evaluated every 1 minute.

You can add these high-resolution metrics and alarm widgets to your CloudWatch dashboards so that you can readily observe the critical components.

#### Publishing high-resolution metrics

You can publish high-resolution metrics in the following ways:

* **API**: The **PutMetricData** function accepts an optional StorageResolution parameter. Set this parameter to 1 to publish high-resolution metrics; omit it (or set it to 60) to publish at standard 1-minute resolution. Note that every **PutMetricData** call for a custom metric is charged, so calling **PutMetricData** more often on a high-resolution metric can lead to higher charges.
* **collectd plugin**: The CloudWatch plugin for **collectd** supports collection and publication of high-resolution metrics. You will need to set the **enable_high_resolution_metrics** parameter in the config file for the plugin.

#### Combining alarms

With CloudWatch, you can combine several alarms into one *composite alarm* to create a summarized, aggregated health indicator over a whole application or group of resources. Composite alarms are alarms that determine their state by monitoring the states of other alarms. You define rules to combine the status of those monitored alarms using Boolean logic.

You can use composite alarms to reduce alarm noise by taking actions only at an aggregated level. For example, you can create a composite alarm to send a notification to your web server team if any alarm related to your web server activates. When any of those alarms goes into the *ALARM* state, the composite alarm goes into the *ALARM* state and sends a notification to your team. If other alarms related to your web server also go into the *ALARM* state, your team does not get overloaded with new notifications because the composite alarm has already notified them about the situation.

You can also use composite alarms to create complex alarming conditions and take actions only when many different conditions are met. For example, you can create a composite alarm that combines a CPU alarm and a memory alarm, and would only notify your team if both the CPU and the memory alarms have activated.

#### Using composite alarms

When you use composite alarms, you have the following two options:

* Configure the actions that you want to take only at the composite alarm level, and create the underlying monitored alarms without actions.
* Configure a different set of actions at the composite alarm level. For example, the composite alarm actions could engage a different team in case of a widespread issue.

Composite alarms can take only the following actions:

* Notify Amazon Simple Notification Service (Amazon SNS) topics
* Create OpsItems in OpsCenter, a capability of AWS Systems Manager
* Create incidents in Incident Manager, a capability of AWS Systems Manager

All the underlying alarms in your composite alarm must be in the same account and the same Region as your composite alarm. However, if you set up a composite alarm in a CloudWatch cross-account observability monitoring account, the underlying alarms can watch metrics in different source accounts and in the monitoring account itself.

A single composite alarm can monitor 100 underlying alarms, and 150 composite alarms can monitor a single underlying alarm.

#### Rule expressions

All composite alarms contain rule expressions. Rule expressions tell composite alarms which other alarms to monitor and determine their states from. Rule expressions can refer to metric alarms and composite alarms. When you reference an alarm in a rule expression, you designate a function to the alarm that determines the three states for the alarm.

1. **ALARM**. ALARM ("alarm-name or alarm-ARN") is TRUE if the alarm is in ALARM state.
2. **OK**. OK ("alarm-name or alarm-ARN") is TRUE if the alarm is in OK state.
3. **INSUFFICIENT_DATA**. INSUFFICIENT_DATA (“alarm-name or alarm-ARN") is TRUE if the alarm is in INSUFFICIENT_DATA state.

#### Example expressions

The request parameter **AlarmRule** supports the use of the logical operators **AND**, **OR**, and **NOT**, so you can combine multiple functions into a single expression. The following example expressions show how you can configure the underlying alarms in your composite alarm.

##### ALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh)

The expression specifies that the composite alarm goes into *ALARM* only if **CPUUtilizationTooHigh** and **DiskReadOpsTooHigh** are in *ALARM*.

##### ALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress)

The expression specifies that the composite alarm goes into *ALARM* if **CPUUtilizationTooHigh** is in *ALARM* and **DeploymentInProgress** is not in *ALARM*. This is an example of a composite alarm that reduces alarm noise during a deployment window.

##### (ALARM(CPUUtilizationTooHigh) OR ALARM(DiskReadOpsTooHigh)) AND OK(NetworkOutTooHigh)

The expression specifies that the composite alarm goes into *ALARM* if **(ALARM(CPUUtilizationTooHigh) OR (DiskReadOpsTooHigh))** is in *ALARM* and **(NetworkOutTooHigh)** is in *OK*. This is an example of a composite alarm that reduces alarm noise by not sending you notifications when either of the underlying alarms aren’t in *ALARM* while a network issue is occurring.

### Scaling with CloudWatch Alarms

#### Using CloudWatch Alarms to Invoke Scaling

You can use the CloudWatch console to create two alarms, one for scaling out and the other for scaling in. When the threshold of an alarm is breached, for example, because the traffic has increased, the alarm goes into the *ALARM* state. This state change invokes the scaling policy associated with the alarm. The policy then instructs Amazon EC2 Auto Scaling about how to respond to the alarm breach, such as by adding or removing a specified number of instances.

##### Creating a CloudWatch alarm for the metric high threshold

1. Open the CloudWatch console.
2. If necessary, change the AWS Region. On the navigation bar, select the Region where your EC2 Auto Scaling group is located.
3. In the navigation pane, choose **Alarms**, and then choose **All alarms**.
4. Choose **Create alarm**. Choose **Select metric**. On the **All metrics** tab, choose **EC2**, and then choose **By Auto Scaling Group**. Enter the name of the Auto Scaling group in the search field.
    For this demonstration, an Auto Scaling group named **example-auto-scaling-group** was already created.
5. Select **CPUUtilization**, and choose **Select metric**.
6. The **Specify metric and conditions** page appears, showing a graph and other information about the metric. For **Period**, choose the evaluation period for the alarm, for example, *1 minute*. When evaluating the alarm, each period is aggregated into one data point. A shorter period creates a more sensitive alarm. This is something you might need to adjust later to create the alarm to behave the way you want it to.
7. Under **Conditions**, for **Threshold type**, choose **Static**. For the alarm condition related to **Whenever CPUUtilization is...**, specify whether you want the value of the metric to be **greater than**, **greater than or equal to**, **less than**, or **less than or equal** to the threshold to breach the alarm. Then, under **than...**, enter the threshold value that you want to breach the alarm. For this example, an alarm to scale out the instances when the CPU utilization is **greater than or equal to 80 percent** is being created.
8. A second alarm to scale in the instances needs to be created. For that alarm, the metric can be set up to **less than or equal to 40 percent**, for example. Under **Additional configuration**, for **Data points to alarm**, enter the number of data points during which the metric value must exceed the threshold conditions for the alarm. These are the evaluation periods. For example, two consecutive periods of 5 minutes would take 10 minutes to invoke the alarm state. For this example, set the value to **1 minute**.
9. With the **Missing data treatment setting**, you can choose what the alarm does if it doesn't receive the expected data point, in this case CPU utilization. For example, the alarm might not receive the expected data point for CPU utilization if connection to the EC2 instance is lost. For this example, use the default setting, **Treat missing data as missing**. Then choose **Next**.
10. On the **Configure actions page**, under **Notification**, select an **Amazon Simple Notification Service**, or **Amazon SNS**, topic to notify the alarm is in *alarm state*, *OK state*, or *insufficient data state*. You can use Amazon SNS to automatically send texts, push notifications, or emails to subscribers when an event happens. In this case, an Amazon EC2 Auto Scaling event. It can also send messages to other applications, like AWS Lambda. For this demonstration, choose **Remove** not to receive notifications for scaling events. The other sections of the **Configure actions page** van be left empty. Leaving the other sections empty creates an alarm without associating it to a scaling policy. You can then associate the alarm with a scaling policy from the Amazon EC2 Auto Scaling console. Choose **Next**.
11. Enter a name of your CloudWatch alarm. For this example, call it **StepScalingAlarmHigh**. You can also add a description for the alarm. Then choose **Next**.
12. Choose Create alarm.

As mentioned previously, you will need to create a second alarm to scale instances in when the CPU utilization is less than a particular threshold. The steps are the same. Except for the scale in alarm, you will need to choose a CPU utilization metric that is **less than** or **less than or equal to** a particular value. For this demo, a second alarm will scale in instances when CPU utilization is **less than or equal to 40 percent**.

##### Connecting a CloudWatch alarm to an Auto Scaling group

1. Navigate to the Amazon EC2 Auto Scaling console.
2. Create a step scaling policy to scale the instances out. In the Amazon EC2 console, in the navigation pane, choose **Auto Scaling Groups**.
3. Create a dynamic scaling policy to connect it to the CloudWatch alarms you just set up. Select the check box next to the Auto Scaling group. Verify that the minimum and maximum size limits are appropriately set. For example, if the group is already at its maximum size, specify a new maximum to scale out. Amazon EC2 Auto Scaling does not scale the group below the minimum capacity or above the maximum capacity.
 3.1. To update the group, on the **Details** tab, you can choose **Edit** to change the current settings for minimum and maximum capacity.
 3.2. For Dynamic scaling policies, choose **Create dynamic scaling policy**. For **Policy type**, choose **Step scaling**. Specify a name for the policy. For CloudWatch alarm, choose the alarm that was created to scale out. If you haven't already created a CloudWatch alarm, you can create it here and follow the steps you went through previously in the CloudWatch console.
 3.3. Specify the change in the current group size that this policy will make when invoked using **Take the action**. You can add a specific number of instances or a percentage of the existing group size, or you can set the group to an exact size. For this example, choose **Add**, enter *30* in the next field, and then choose **Percent of group**. By default, the lower bound for this step adjustment is the alarm threshold, and the upper bound is the positive infinity.
 3.4. To add another step, you can choose **Add step**. You can then define the amount by which to scale and the lower and upper bounds of the step relative to the alarm threshold. To set a minimum number of instances to scale, update the number field to *1*.
 3.5. For instances need, update the instance warm-up value as needed. Your instances might take about 5 minutes to spin up before you can start directing traffic to them, so set this value to 300 seconds. Choose **Create**.
4. To define a policy for scale in, go through the same steps. However, you will select the second CloudWatch alarm you created to scale in instances when CPU utilization is **less than or equal to 40 percent**. You can set the policy to remove 30 percent of the group, or at least one instance, when the alarm is breached.

### Knowledge Check

#### An organization wants to proactively monitor the health of its critical APIs and set up automated tests to simulate user interactions. Which Amazon CloudWatch feature can help achieve this?

* Amazon CloudWatch Synthetics

Wrong answers:

* Amazon CloudWatch Logs Insights
* Amazon CloudWatch Metrics Insights
* Amazon CloudWatch Evidently

##### Explanation

CloudWatch Synthetics allows for the creation of canary tests to monitor APIs and other endpoints proactively. Canaries follow the same routes and perform the same actions as a customer to simulate user interaction.

The other options are incorrect for the following reasons:

* CloudWatch Logs Insights helps identify patterns, interactively search, and analyze your log data with bar charts, line charts, and stacked area charts.  It doesn't simulate user interaction.
* CloudWatch Metrics Insights is a fast, flexible, SQL-based query engine that you can use to identify trends and patterns within millions of operational metrics in near real time. It doesn't simulate user interaction.
* With Amazon CloudWatch Evidently, application developers can conduct experiments and identify unintended consequences of new features before rolling them out for general use. It doesn't simulate user interaction.

#### What is a key advantage of using composite alarms in Amazon CloudWatch?

* To reduce alarm noise by combining multiple alarms

Wrong answers:

* To reduce the overall number of alarms in the system
* To simplify the visualization of metric data in the CloudWatch dashboard
* To create hierarchical alarm structures for better organization

##### Explanation

Users can use composite alarms to reduce alarm noise by taking actions only at an aggregated level. If an issue affects several resources in an application, users will receive a single alarm notification for the entire application instead of one for each affected resource. This helps them focus on finding the root cause of operational issues to reduce application downtime.

The other options are incorrect because they are not the advantages of using composite alarms.

#### An application developer wants to conduct experiments and identify unintended consequences of new features before rolling them out for general use. Which Amazon CloudWatch feature can they use? 

* Amazon CloudWatch Evidently

Wrong answers:

* CloudWatch high-resolution alarms
* Amazon CloudWatch Contributor Insights
* Amazon CloudWatch Logs Insights

##### Explanation

Developers can use Evidently to safely validate new features by serving them to a specified percentage of their users while they roll out the features. They can monitor the performance of a new feature to help them decide when to ramp up traffic to the users. This helps reduce risk and identify unintended consequences before they fully launch the feature.

The other options are incorrect for the following reasons:

* If developers set an alarm on a high-resolution metric, they can specify a high-resolution alarm with a period of 10 seconds or 30 seconds. With high-resolution alarms, they can react and take actions faster. High-resolution alarms don't help with identifying unintended consequences of new features.
* CloudWatch Contributor Insights analyzes time-series data to provide a view of the top contributors influencing system performance. It doesn't help with identifying unintended consequences of new features0
* CloudWatch Logs Insights helps developers efficiently identify patterns, interactively search, and analyze their log data with bar charts, line charts, and stacked area charts. CloudWatch Logs Insights doesn't help with identifying unintended consequences of new features.

### Summary

#### Amazon CloudWatch dashboards

Amazon CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view, even those resources that are spread across different Regions. You can also create cross-account observability dashboards and cross-account cross-Region dashboards.

#### CloudWatch Synthetics

You can use CloudWatch Synthetics to monitor application endpoints more easily. It runs tests on your endpoints continuously and alerts you if they don’t behave as expected. These tests can be customized to check your applications for a number of issues. Tests include availability, latency, transactions, broken links, step-by-step task completions, page load errors, load latencies for UI assets, complex wizard flows, and checkout flows.

#### CloudWatch RUM

CloudWatch RUM gives you visibility into your applications’ client-side performance. It helps you collect client-side data on web application performance in near real time to identify and debug issues. CloudWatch RUM complements the CloudWatch Synthetics data to give you more visibility into your end-user experience. You can visualize anomalies in performance and use the relevant debugging data (such as error messages, stack traces, and user sessions) to fix performance issues (such as JavaScript errors, crashes, and latencies). You can gain insight into the range of end-user impacts, including number of users, geolocations, and browsers. CloudWatch RUM aggregates data on your users' journey through your application, which can help you determine which features to launch and bug fixes to prioritize.

#### CloudWatch Logs Insights

CloudWatch Logs Insights helps you efficiently identify patterns, interactively search, and analyze your log data with bar charts, line charts, and stacked area charts. You can perform queries to efficiently and effectively respond to operational or network issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes.

#### CloudWatch Metrics Insights

CloudWatch Metrics Insights is a fast, flexible, SQL-based query engine that you can use to identify trends and patterns within millions of operational metrics in near real time. You can use CloudWatch Metrics Insights to gain better visibility on your infrastructure and large-scale application performance with flexible querying and on-the-fly metric aggregations. CloudWatch Metrics Insights queries can be used to create powerful visualizations and help you proactively monitor and pinpoint issues quickly.

#### CloudWatch Contributor Insights

CloudWatch Contributor Insights analyzes time-series data to provide a view of the top contributors influencing system performance. After it is set up, CloudWatch Contributor Insights runs continuously without additional user intervention. This helps developers and operators more quickly isolate, diagnose, and remediate issues during an operational event. CloudWatch Contributor Insights helps you understand who or what is impacting your system and application performance, such as a specific resource, customer account, or API call.

A contributor is an aggregate metric based on dimensions contained as log fields in CloudWatch Logs, such as account-id or interface-id in VPC Flow Logs, or any other custom set of dimensions. You can sort and filter contributor data based on your own custom criteria. CloudWatch Contributor Insights report data can be displayed on CloudWatch dashboards, graphed alongside CloudWatch metrics, and added to CloudWatch alarms.

#### Evidently

With Amazon CloudWatch Evidently, application developers can conduct experiments and identify unintended consequences of new features before rolling them out for general use, thereby reducing risk related to new feature roll-out.

You can use Evidently to validate new features across the full application stack before release, which makes for a safer release. When launching new features, you can expose them to a small user base, monitor key metrics, such as page load times or conversions, and then dial up traffic. With Evidently, you can also try different designs, collect user data, and release the most effective design into production.

#### High-resolution metrics and alarms and composite alarms

Metrics produced by AWS services are standard resolution by default. When you publish a custom metric, you can define it as either standard resolution or high resolution. When you publish a high-resolution metric, CloudWatch stores it with a resolution of 1 second, and you can read and retrieve it with a period of 1 second, 5 seconds, 10 seconds, 30 seconds, or any multiple of 60 seconds.

If you set an alarm on a high-resolution metric, you can specify a high-resolution alarm with a period of 10 seconds or 30 seconds. With high-resolution alarms, you can react and take actions faster.

With CloudWatch composite alarms, you can combine multiple alarms and reduce alarm noise. If an issue affects several resources in an application, you will receive a single alarm notification for the entire application instead of one for each affected resource. This helps you focus on finding the root cause of operational issues to reduce application downtime. You can provide an overall state for a grouping of resources, such as an application, AWS Region, or Availability Zone.

#### Using CloudWatch alarms to invoke scaling

When a CloudWatch alarm transitions to a new alarm state (*OK*, *ALARM*, or *INSUFFICIENT_DATA*), the alarm invokes any configured actions for that state. Amazon EC2 Auto Scaling only uses the period configured on the alarm to determine if the state should change. For scaling actions, the alarm continues to invoke the configured action for every minute that the alarm remains in the new state, regardless of the configured period. For a CloudWatch alarm to invoke an Amazon EC2 Auto Scaling policy, the **ActionsEnabled** parameter must be enabled in the alarm's configuration. Be sure that the **ActionsEnabled parameter** is true in your alarm's configuration.

### Additional Resources

* [Suppressing Composite Alarm Actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm_Suppression.html)
* [Using Synthetic Monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
* [Setting Up an Application to Use CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started.html)
