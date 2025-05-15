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
