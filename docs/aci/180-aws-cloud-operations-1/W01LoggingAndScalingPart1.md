###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Logging and Scaling Part 1

## Monitoring and Amazon CloudWatch

### Monitoring with and without an agent
When using CloudWatch to monitor your Amazon EC2 instances, agentless monitoring is limited to collecting **basic OS-level** metrics like **CPU**, **network**, and **disk usage**.

The CloudWatch agent is a lightweight, open-source software component that you can install on EC2 instances and on-premises servers. The agent can run on supported Linux, Windows Server, or macOS operating systems.

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

When the agent is installed on an EC2 instance and an on-premises server, the EC2 instance has an IAM role attached that gives the agent permissions for reading information from the instance and writing it to CloudWatch. The on-premises server has an IAM user that provides the same permission to read and write information. The IAM role and IAM user can optionally include permissions to set the retention policy for the log groups that they send log events to.

The agent collects metrics by using data from the operating system. These metrics are sent to a CloudWatch metrics namespace (by default this will be named CWAgent). You can configure dimensions to organize and aggregate your metrics.  

The agent can collect log files specified as an individual file or group of files. It then sends them to a log stream (by default, this is named using the instance ID) in a log group that you have configured. 

### Installing the CloudWatch agent
You can install the CloudWatch agent by using the command line, AWS Systems Manager, or an AWS CloudFormation template. 

The following steps provide a general overview of the agent installation process:
1. To run the CloudWatch agent on an EC2 instance or server, create an IAM role using the **CloudWatchAgentServerPolicy** policy, and then attach the role to the instance. If you're running the agent on an on-premises server, create an IAM user with the **CloudWatchAgentServerPolicy** policy.
2. Download the agent package. On all supported operating systems, you can download and install the CloudWatch agent by using the command line. If you're using Amazon Linux 2, you can install the package by entering the **sudo yum install amazon-cloudwatch-agent** command.
* Create and edit a CloudWatch agent JSON configuration file to configure the agent and specify the metrics and logs that you want to collect. You can use the agent configuration file wizard, **amazon-cloudwatch-agent-config-wizard**, to create the file. At a minimum, you should specify the AWS Region and AWS access key of an IAM user with permissions to publish to CloudWatch.
* Start and enable the CloudWatch agent service.

For more detailed information and step-by-step instructions for each CloudWatch agent installation method, see [Installing the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html).

### Using the console to monitor instances
The Amazon EC2 console and the CloudWatch dashboard both provide different ways to monitor EC2 instances, both historically and in real time. Each dashboard has its own advantages.

### Logging Activities with CloudTrail
#### Following the trail
AWS CloudTrail provides insights into who did what and when by tracking user activity and API usage. With CloudTrail, you can get a history of AWS API calls in your account. These calls can be made through the console, AWS Command Line Interface (AWS CLI), AWS SDKs, and higher-level AWS services. CloudTrail records the AWS API calls and delivers the log files to you. The information includes the source IP address and identity of the API caller. It also includes the time of the call, the request parameters, and the response elements that the AWS service returns. 

CloudTrail is active in your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. You can view the past 90 days of recorded API activity (management events) in an AWS Region in the CloudTrail console by going to Event history.

For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

#### Benefits of monitoring with CloudTrail
The AWS API call history that CloudTrail produces can facilitate security analysis, tracking of resource changes, and compliance auditing.

CloudTrail helps you answer questions that require detailed analysis. You can store and view your CloudTrail API usage logs in an Amazon S3 bucket. Later, you can analyze those logs to answer compelling questions. For example, consider the following:
* Why was a long-running instance terminated and who terminated it? The answer can provide organizational traceability and accountability.
* Who changed a security group configuration? The answer can provide accountability and facilitate security auditing.
* What activities were denied due to lack of permissions? The answer can expose a potential internal or external attack against the network.

#### CloudTrail logs
CloudTrail produces logs that you can analyze to determine the following:
* Who made the API request?
* What was the focus of the request?
* When did the request occur?
* What was the API call?
* What was the response?
* In what AWS Region did the request occur?

The following example shows the first section of a CloudTrail log. This section shows who performed an API request.

```
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

In the preceding example, the **userIdentity** section of the log file shows that an AWS Identity and Access Management (IAM) user with **"userName"**: **"Mateo"** performed an action. The section also shows that the IAM user was created on **"creationDate"**: **"2023-07-19T21:11:57Z"**. The date and time are separated with a T. The Z at the end of the timestamp indicates that it is in Zulu time, more commonly known as Coordinated Universal Time (UTC).

The following example shows the next section of the same CloudTrail log. This section shows the action that was performed, when it occurred, and the Region in which it took place.

```
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

In the preceding example, you can see that the **"eventTime"** took place at **"2023-07-19T21:17:28Z"**. The aws ec2 start-instances command, **"eventName"**: **"StartInstances"**, was used to call **"eventSource"**: **"ec2.amazonaws.com"** (meaning Amazon EC2) in **"awsRegion"**: **"us-east-1"** from **"sourceIPAddress"**: **"192.0.2.0"**. The command was used to start two EC2 instances with IDs **i-EXAMPLE56126103cb** and **i-EXAMPLEaff4840c22**.

The following example shows the next section of the CloudTrail log, which shows the response.

```
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

```
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
* Mateo used the **aws ec2 start-instances** command to start two EC2 instances in the us-east-1 Region that were previously in the stopped state.
* The command was successful, and the EC2 instances began to spin up.

CloudTrail logs are one way to understand the activity within your AWS environment. You can use these logs for troubleshooting and locating potential security risks.

### Knowledge Check
#### A cloud administrator is tasked with creating a monitoring plan for a company's AWS resources. What should the plan address first?
* The monitoring goals

Wrong answers:
* The time allocated for viewing metrics and dashboards each week
* The specific metrics that must be monitored
* Whether to use basic monitoring or detailed monitoring

The first thing that a monitoring plan should address is your goals for monitoring. When you consider this, you should focus on operational outcomes instead of specific metrics. The goals that you identify will inform the rest of the monitoring plan.

#### A software developer is analyzing an AWS CloudTrail log to determine how the permissions associated with an Amazon S3 bucket were changed. What is an example of information that the CloudTrail log might provide?
* The identity of the person or service that changed the bucket permissions and when the change was made

Wrong answers:
* A list of objects in the bucket that have public read access as a result of the changed permissions
* The public IP address of the static website associated with the bucket
* A list of the users, roles, and services that have permission to change the bucket permissions

AWS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS CLI, and AWS SDKs and APIs.

The other options are incorrect for the following reason: 
* CloudTrail records the AWS API calls and delivers the log files to you. The information includes the source IP address and identity of the API caller. It also includes the time of the call, the request parameters, and the response elements that the AWS service returns.

#### What is an example of an Amazon EC2 metric provided with Amazon CloudWatch basic monitoring?
* Completed disk reads and writes within a specified period of time

Wrong answers:
* Response times for applications connecting to the instance
* The identities of users who have made changes to the instance permissions
* Custom metrics for applications running on the instance

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
* **Vended logs** – These are natively published by AWS services on your behalf. Currently, **Amazon VPC flow logs** and **Amazon Route 53 logs** are the two supported types.
* **Logs published by AWS services** – Currently, more than 30 AWS services publish logs to CloudWatch. They include Amazon API Gateway, AWS Lambda, AWS CloudTrail, and many others.
* **Custom logs** – These are logs from your own application and on-premises resources, and from other clouds.

#### Monitoring with CloudWatch
You can use CloudWatch to collect metrics and store logs. You can use CloudWatch to monitor a near real-time stream of system events. And you can create CloudWatch alarms that watch metrics and initiate actions like sending notifications or auto scaling when certain conditions are met. You can also use CloudWatch dashboards to create customizable views of metrics and alarms across multiple AWS resources.

CloudWatch provides two categories of monitoring: 
* Basic monitoring provides metrics at 5-minute intervals.
* Detailed monitoring provides information at 1-minute intervals for services that offer it.

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

#### [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

#### [Monitor Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_ec2.html)

## Monitoring Application Health
