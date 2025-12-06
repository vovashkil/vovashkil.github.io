# Week 8: Compute 3 Part 1: Using Amazon EC2 and Lambda for Applications

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Fundamentals 2](./aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../README.md)

## Using Amazon EC2 for Applications

### Knowledge Check

#### A company wants to migrate their on-premises application workload to the cloud. The application is CPU intensive and memory intensive. What benefit of Amazon EC2 would enables the company to efficiently run their application in the cloud?

* Ability to configure compute resources to match application workload

Wrong answers:

* Persistent block storage for databases
* Managed database services like Amazon RDS and Amazon DynamoDB
* Serverless compute with AWS Lambda

##### Explanation

Amazon EC2 provides configurable compute capacity, allowing you to select instance types optimized for your workload. This lets you match the compute resources to your application's specific CPU and memory requirements for efficient resource utilization.

The other options are incorrect because:

* Amazon Elastic Block Store (Amazon EBS) provides persistent block storage, which is useful for databases, but does not directly address optimizing compute resources for an application workload.
* Managed database services can offload database administration, but do not help optimize compute resources for an application workload.
* AWS Lambda provides event-driven serverless compute. But it is not the optimal choice for running a continuously running CPU and memory-intensive application workload.

#### A developer is setting up an Amazon EC2 instance and wants to connect to it by using Secure Shell (SSH). What must be configured to allow the SSH connection?

* The security group associated with the EC2 instance must allow inbound connections on port 22.

Wrong answers:

* The subnet associated with the EC2 instance must allow inbound connections on port 22.
* The network access control list (network ACL) associated with the EC2 instance must allow inbound connections on port 22.
* The route table associated with the EC2 instance must allow inbound connections on port 22.

##### Explanation

Because the SSH connection goes through port 22, you must make sure that the security group of your instance has an inbound rule that allows connections on port 22 from your computer. Security groups act as a virtual firewall for associated EC2 instances.

The other options are incorrect because:

* Subnets specify the IP address range and Availability Zone for the instance, but do not control inbound connections.
* Network ACLs control traffic in and out of subnets, not specific instances.
* Route tables control where network traffic is directed, not inbound connections to specific instances.

#### A systems administrator needs to install and manage software packages on Amazon EC2 instances running Amazon Linux 2. What is the recommended package manager for this task?

* Yum

Wrong answers:

* Apt
* RPM
* Git

##### Explanation

It is the recommended package manager for Red Hat-based Linux distributions like Amazon Linux. It allows installing, updating, removing, and managing software packages from official repositories. Yum can install a package with **yum install package** and update all packages with **yum update**.

The other options are incorrect because:

* Apt is the package manager for Debian-based Linux distributions, not Amazon Linux, which is Red Hat based.
* RPM is a package format, not a package manager. Yum uses RPM packages but provides additional functionality for managing packages.
* Git is a version control system, not a package manager. It is used for source code management, not installing OS packages.

### Summary

#### Amazon EC2 overview

With Amazon EC2, you can host applications while providing secure, resizable compute capacity. You can use Amazon EC2 to avoid buying hardware up front, so you only pay for capacity that you actually use. With Amazon EC2, you can quickly scale capacity up or down to meet changes in demand while building highly available architectures by distributing applications across multiple Availability Zones.

Overall, the flexible and low-cost capacity of Amazon EC2 helps you rapidly deploy applications on AWS.

#### Amazon EC2 instance profiles

Instance profiles let EC2 instances access other AWS services. To use a profile, assign an IAM role that defines the allowed actions to the instance when launched. The profile passes temporary security credentials to the instance, which come from the linked role.

With a profile, code running on the instance can access permitted resources like Amazon S3 buckets. The instance does not store long-term credentials and each role can be used by multiple profiles. One instance can have only one profile and role at a time.

#### Remote administration

Key pairs can be used to securely connect to your Linux instances over SSH or to Windows instances with RDP. Session Manager is another option to start remote sessions without opening inbound ports. When accessing instances remotely, it's critical to control access. Use security groups to restrict source IPs that can connect.

For additional security, use IAM policies to limit which IAM users or roles can start sessions. Proper identity and access management is key for securely administering cloud resources.

#### Package management

You can utilize managing software packages on your EC2 instance by using the built-in package manager for your operating system, like Yum for Red Hat Enterprise Linux (RHEL) or APT for Ubuntu. Only install packages from official repositories and review package dependencies that must be resolved, while understanding that upgrading one package might require upgrading others.

Setting up automatic security updates ensures that you get fixes as they become available. For managing your own packages, you can use AWS CodeArtifact as a secure, scalable option that integrates with familiar tools like pip and npm.

Python package management using pip can be used for installing and removing packages.

---

## Using AWS Lambda for Applications

### Knowledge Check

#### Which of these is the best case for using an AWS Lambda function?

* You need to provide users of your site with an official postal service address matching an address that they entered before they submit a form.

Wrong answers:

* You need to provide a chatbot for users of your site to help them troubleshoot.
* You need to filter incoming requests so that only those with an issue ID starting with TN are processed.
* You need to coordinate calls to multiple APIs to perform a complex operation requiring all of them.

##### Explanation

This is a validation task that has all of the properties for best use case.

It is isolated and only needs to work with the initial form data, operates on an external API and thus needs a degree of custom code, requires very little time beyond the single API call, needs to scale through a wide range of concurrent use, addresses a cross-cutting concern that many applications in your system would need.

The other options are incorrect because:

* A chatbot would need either persistent state, so that multiple user messages could be treated together, or interaction with the user over time. The latter would mean that the function would both need more than its initial entity data to do its work and then it would have a lot of downtime waiting for the user to respond. This would increase costs and possibly result in timeouts.
* Basic filtering can usually be performed more efficiently before a Lambda function is called, reducing invocations and cost.
* AWS Step Functions is designed to be a simpler and more cost-effective way of coordinating processes involving multiple API calls.

#### What is the event parameter to a Python AWS Lambda function handler?

* A Python dictionary of arguments and values

Wrong answers:

* A Python List of arguments
* A JSON string
* A Python object of class Event

##### Explanation

The other options are incorrect because:

* The trigger will send a JSON string to Lambda, but Lambda converts this to the language-specific parameter that the handler function needs.
* There is no Python Event object in this context.
* A List is not used here.

#### Which tool would you use to review metrics on invocations, errors, and throttling for an AWS Lambda function?

* Amazon CloudWatch

Wrong answers:

* AWS X-Ray
* AWS CloudTrail
* Dead-letter queue

##### Explanation

The other answers are incorrect because:

* Dead-letter queues are for reviewing invocations that failed but must be addressed.
* AWS X-Ray provides trace details about the steps in an invocation.
* AWS CloudTrail is for auditing API actions made against your applications.

### Summary

#### Authoring Lambda functions

You learned how Lambda functions are written. In particular, you learned many of the things that need to be considered in determining whether providing functionality with a Lambda function makes sense for a particular problem.

You also learned about triggers and some of the configuration options that must be defined for a Lambda function in addition to the code that it runs.

#### Managing Lambda packages

You learned about how the code for a Lambda function is packaged and deployed. Although containers were mentioned as an option, you particularly learned about deployment packages and the layers that can be added to them. You learned that all your Lambda code can be uploaded as a single package in a .zip file. You also learned that it can be preferable to put some code not related to your core logic into separate packages called Layers.

#### Monitoring Lambda functions

You learned how to monitor your Lambda functions using CloudWatch Lambda Insights or AWS X-Ray.

A CloudWatch dashboard lets you view a variety of metrics either about a single Lambda function or aggregated across all Lambda functions running on a particular account and region. X-Ray, on the other hand, provides details on the time Lambda spends in different operations once a Lambda function has been invoked, which can provide key data when diagnosing performance issues or searching for bottlenecks.

---
