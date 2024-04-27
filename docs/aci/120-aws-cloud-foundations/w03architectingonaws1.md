###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Architecting on AWS 1
## Well-Architected Framework
The AWS Well-Architected Framework is designed to help customers build the most secure, high-performing, resilient, efficient, and sustainable infrastructure possible.

The framework provides a set of design principles and questions for customers to measure their architecture against AWS best practices. It also helps them identify how to address any shortcomings through a set of foundational questions across six pillars: 
* Operational excellence
* Security
* Reliability
* Performance efficiency
* Cost optimization
* Sustainability

### Operational excellencei
Focuses on running and monitoring systems to deliver business value, and with that, continually improving processes and procedures. For example, this could mean automating changes with deployment pipelines or responding to events that are triggered.

### Security
Security is priority number one at AWS and the security pillar exemplifies this by checking the integrity of data and, for example, protecting systems by using encryption.

### Reliability
Focuses on recovery planning. This means recovery from things like a database disruption or an instance failure. It may include how you handle change to meet business and customer demands.

### Performance efficiency
It's about using IT and computing resources efficiently. For example, using the right Amazon EC2 type, based on workload and memory requirements, as well as making informed decisions to maintain efficiency as business needs evolve.

### Optimizing for cost
This is controlling where money is spent. For example, you can check to see if you have overestimated your EC2 service size, and you could then lower cost by choosing a more cost effective size.

### Sustainability
Focuses on environmental sustainability. This is reducing the impact of your cloud workload by maximizing utilization and minimizing waste. An example of this is using the minimum amount of hardware required to meet your needs.


The Well-Architected Framework was constructed by reviewing thousands of customers' architectures on AWS. From this experience, AWS has identified best practices and core strategies for architecting systems in the cloud.

## The evolution of the Well-Architected Framework
### 2012 Framework started
AWS solutions architects (SAs) noted recurring architectural problems from customers. They started thinking about ways that AWS could help customers avoid these reoccurring issues.

### 2013 AWS solutions architects reviews
AWS solutions architects started doing Well-Architected Framework reviews. At the time, this consisted of an assessment of customer workloads and how they were performing against trends that SAs were seeing in the field. These insights began to be documented.

### 2014 Questions across four pillars
Over time, these insights evolved into a set of questions across four pillars (security, reliability, performance efficiency, and cost optimization).

### 2015 First version of Well-Architected Framework
The first version of the Well-Architected Framework whitepaper was published in 2015.

### 2016 Operational excellence pillar
Through additional customer interaction and feedback, the operational excellence pillar was added. The framework was organized accordingly.

### 2017 AWS Partners, first lens
AWS Partners started performing Well-Architected reviews. The first set of AWS Well-Architected Framework lens whitepapers launched. This included high performance computing (HPC), Internet of Things (IoT), and serverless computing.

### 2018 Self-service improvement plans
At re:Invent 2018, AWS Well-Architected launched the AWS Well-Architected Tool in the AWS Management Console. Customers could perform framework reviews on their own.

### 2019 Region launches
The AWS Well-Architected Tool launched in several Regions such as the AWS Europe (London) Region and Asia Pacific (Sydney, Tokyo) Region.

### 2020 Localization and API
The AWS Well-Architected Tool launched in multiple Regions globally, with localized content in nine key languages.

The AWS Well-Architected APIs became available to customers at no additional charge.

### 2021 Sustainability pillar
AWS introduced the sustainability pillar during re:Invent 2021 to help customers minimize the environmental impacts of running cloud workloads.

Today, the sustainability pillar is available for customers to use during workload reviews in the AWS Well-Architected Tool, a central place for cloud architecture best practices and guidance.


Integrating the Well-Architected Framework into your organization's processes can help your teams in the following ways:
* Build and deploy faster
* Lower or mitigate risks
* Make informed decisions
* Learn AWS best practices

## Well-Architected reviews
Reviews of your architecture should take place early in the application development lifecycle, during the initial architecture development. Although a review before an application goes into production is a good idea, this is not enough. Any issues detected right before production would take longer to fix than if they were caught earlier during development.

Ideally, a Well-Architected review should be conducted periodically over the lifetime of an application. This is because with a continuous approach, your team members can update answers as the architecture evolves, and improve the architecture as you deliver features.

AWS also frequently releases new services. And we, as a community, are constantly learning better ways to architect and take advantage of the cloud. This means that even after an application is in production, periodic reviews can identify missed opportunities.

To review your architecture, the questions and best practices of the Well-Architected Framework are available in the following forms. To learn more, expand each of the following two categories. 

### AWS Well-Architected whitepapers
The AWS Well-Architected whitepapers are available as HTML documentation or PDFs. They provide an overview of the pillars, as well as questions and best practices that you can use to evaluate and improve your architecture.

### AWS Well-Architected Tool
Navigating design principles and best practices can be complicated. This is why AWS released the AWS Well-Architected Tool. It is a self-service review tool available on the AWS Management Console that provides customers and Partners with a consistent approach to reviewing their architectures against current AWS best practices. You will answer questions associated with the six pillars, and get advice on how to improve your architecture. You will learn more about the AWS Well-Architected Tool later in the course.

## AWS Well-Architected Lenses
The AWS Well-Architected Lenses extend the guidance that the Well-Architected Framework offers to specific industry and technology domains with additional sets of questions and practices. Examples include machine learning (ML), data analytics, serverless, high-performance computing (HPC), Internet of Things (IoT), SAP, streaming media, the games industry, hybrid networking, and financial services. To fully evaluate workloads, use applicable lenses together with the AWS Well-Architected Framework and its six pillars.

### AWS Well-Architected Game Industry
This is an example of a question that is specific to the gaming industry, and is available in the Games Industry Lens whitepaper: "GAMEREL01 — How does your game infrastructure scale to changes in player demand?"

Many lenses are available in the form of HTML whitepapers on the AWS website. 

### Two lenses are integrated in the AWS Well-Architected Tool: 
* The Serverless Lens that focuses on designing, deploying, and architecting your serverless application workloads in the AWS Cloud.
* The SaaS Lens that focuses on designing, deploying, and architecting your software as a service (SaaS) workloads in the AWS Cloud.

## AWS Well-Architected Labs
To help you apply best practices, AWS has created AWS Well-Architected Labs. These labs provide you with a repository of code and documentation to give you hands-on experience implementing best practices.

### Pillar
Select the pillar for which you want to find a lab.

### Proficiency
Select the proficiency level:
* 100: Foundational level
* 200: Intermediate level
* 300: Advanced level

## AWS Well-Architected Partner Program
AWS has teamed up with select AWS Partners who are members of the AWS Well-Architected Partner Program. These AWS Partners have deep AWS knowledge, and can help you review and improve your workloads. 

## Well-Architected Framework Overview
### AWS Well-Architected Labs
AWS Well-Architected Labs is a repository that contains documentation and code in the form of hands-on labs to help you learn, measure, and build using architectural best practices. The labs are categorized into levels. 100 is foundational, 200 is intermediate, 300 is advanced, and 400 is expert.

### AWS Well-Architected documentation
* The AWS Well-Architected Framework documentation describes key concepts, design principles, and architectural best practices for designing and running workloads in the cloud.
* The AWS Well-Architected Lenses whitepapers extend the guidance offered by AWS Well-Architected to specific industry and technology domains.
* AWS Well-Architected Guidance whitepapers focus on a specific use case, technology, or implementation scenario.

### The AWS Well-Architected Tool
Use the AWS Well-Architected Tool to start your Well-Architected Framework reviews.

### AWS Partners
AWS Well-Architected Partner Program members have in-depth training on the AWS Well-Architected Framework, and are empowered to implement best practices, measure workload states, and make improvements where required.

## AWS Cloud Architecture Design Principles
Applying these cloud principles will help you to build highly available, scalable architectures within AWS. The cloud principles are as follows:
* Designing for failure
* Decoupled components instead of monolithic architecture
* Implementing elasticity in the cloud as opposed to on-premises environments
* Thinking parallel

### Designing for failure
An example of designing for failure is the use of a load balancer. Elastic Load Balancing (ELB) is a managed load balancing service that automatically distributes incoming application traffic across multiple targets. Examples of such targets include Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, IP addresses, and AWS Lambda functions. A load balancer only sends traffic to healthy targets. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones.

An ELB load balancer distributes traffic between EC2 instances in two Availability Zones.

#### Example of a load balancer
In this example, the ELB load balancer distributes incoming requests between the Amazon EC2 instances:
* If an instance is unhealthy, the load balancer redirects traffic to the other instance.
* The load balancer works with Amazon EC2 Auto Scaling to ensure that the right amount of instances are available at any time. The load balancer also helps to ensure that no instance is overwhelmed.

### Loosely coupling
Traditional infrastructures have chains of tightly integrated components. Each component has a specific purpose.

Components are strongly connected to each other, which impedes scaling and makes the system more likely to experience failures.

With loose coupling, you reduce dependencies in your system by using managed solutions as intermediaries between the layers of your system. In this way, the intermediary automatically handles failures and the scaling of components or layers.

One way to achieve loose coupling is by using asynchronous messages that use Amazon Simple Queue Service (Amazon SQS), for example. Separating processes into different pieces that are connected by messages in queues creates clear transaction boundaries and allows services to operate more independently.

Consider the following diagram that shows an example of a queue-based architecture resulting in a loosely coupled system.
1. Multiple users submit jobs with the AWS Command Line Interface (AWS CLI) or AWS SDKs.
2. The jobs are queued as messages in Amazon SQS.
3. EC2 instances poll the queue and start processing jobs.
4. Amazon SQS emits metrics based on the number of messages (jobs) in the queue.
5. An Amazon CloudWatch alarm is configured to notify Amazon EC2 Auto Scaling if the queue is longer than a specified length. Amazon EC2 Auto Scaling increases the number of EC2 instances.
6. The EC2 instances pull source data and store result data in an Amazon Simple Storage Service (Amazon S3) bucket.

In this architecture, Amazon SQS decouples the users' requests and the EC2 instances to avoid bottlenecks. Imagine that the request is to upload images, process them, create thumbnails, and upload them to a storage service such as Amazon S3. The EC2 instances can manage a limited number of requests at a time. One of the solutions is to send messages to the queue so that EC2 instances fetch messages and process them when they have finished processing the previous requests.

### Embracing elasticity and automating
A common cause of failure in on-premises workloads is resource saturation, or when the demands placed on a workload exceed the capacity of that workload (this failure is often the objective of denial-of-service attacks). In the cloud, you can monitor demand and workload utilization (by using Amazon CloudWatch, for example). You can automate the addition or removal of resources to maintain the optimal level to satisfy demand without overprovisioning or underprovisioning.

An example of automation that leads to elasticity is the use of an Auto Scaling group to scale in or scale out EC2 instances.

### Using parallelism
Parallelism means breaking down larger tasks into smaller, yet similar, subtasks. These subtasks are processed independently. The respective results are then combined at the end as a single process, which allows for increased efficiencies.

There are different types of parallelism. Data parallelism means multiple instances of the same task operating on different sections of data. Task parallelism means different tasks operating on the same or different data.

Elastic Load Balancing ensures that the traffic is evenly distributed across instances so that requests are handled in parallel.

## Designing for High Availability
### Definition
In any system of reasonable complexity, it is expected that failures will occur. While designing your architecture, you should think about the resiliency of your system, which is the ability of a workload to recover from infrastructure, service, or application disruptions.

The components of resiliency are high availability and disaster recovery. Disaster recovery focuses on disaster events. Availability focuses on more common disruptions of a smaller scale, such as component failures, network issues, software bugs, and load spikes.

### Fault tolerance
Fault tolerance is the ability to withstand subsystem failure and maintain availability.

Workloads with a requirement for high availability must be architected for resiliency with the following practices:
* Monitor all components of the workload to detect failures.
* Fail over to healthy resources.
* Automate healing on all layers.
* Send notifications when events impact availability.

### Fault isolation
Fault isolation minimizes the scope of impact when a failure does occur. Workloads are broken down into small subsystems that fail independently and can be repaired in isolation. The failure of a module does not propagate beyond the module.

Best practices for fault isolation include the following:
* Distribute workload data and resources across multiple Availability Zones or, where necessary, across AWS Regions.
* Automate recovery for components constrained to a single Availability Zone.

### Building a highly available architecture
#### Evaluating an architecture
In the following example, you can see an architecture of a web application. Users connect to an EC2 instance that is located in a public subnet by using a Classic Load Balancer. The EC2 instance communicates with a storage tier that consists of an Amazon Relational Database Service (Amazon RDS) instance.

First, the design has no redundancy. It provides no failover mechanism in the event of component failure, which means that if a single component fails, the entire application goes down. It is important to mention that, because the application is deployed in a single Availability Zone, it will stop working if the Availability Zone fails.

#### Improving the architecture
##### Increasing redundancy
The first step to make this application more available is to improve the redundancy of the services, which can be achieved by using several EC2 instances and duplicating the architecture. In the following example, the duplicated architecture has been placed in a second Availability Zone to ensure business continuity if an Availability Zone fails. Elastic Load Balancing splits the traffic between the two instance fleets. Several EC2 instances are running, and the load balancer routes requests to healthy instances.

However, the primary database instance still manages all of the traffic. A standby instance is created to duplicate the primary database in another Availability Zone, which protects application data if the primary database Availability Zone fails. Snapshots of the database are stored in Amazon S3.

##### Making the application ready for large traffic increases
To handle large increases in traffic, your system must be elastic and able to scale. The following example shows the EC2 instances, which are grouped in an Auto Scaling group. Adding an Amazon EC2 Auto Scaling group helps to ensure that you have the correct number of Amazon EC2 instances running at any time. Using different scaling options can initiate auto scaling. One way of using dynamic scaling is to use metrics from CloudWatch.

To preserve the capacity of the primary database instance, it is possible to offload the read requests by creating Amazon RDS read replicas. This technique helps to manage read-heavy workloads. The standby instances help overcome the potential loss of Availability Zone A.

In the following diagram, a multi-AZ architecture uses an Elastic Load Balancer to distribute traffic to EC2 instances over two AZs. The first AZ has a primary instance DB and a read replica. The second AZ has a primary instance DB and a read replica instance DB that contains copy of the data of the first DB. Both are in standby mode.

## Disaster Recovery of Workloads on AWS: Recovery in the Cloud
## Disaster recovery
Disaster recovery (DR) is the process of preparing for and recovering from a disaster. A disaster is an event that prevents a workload or system from fulfilling its business objectives in its primary deployed location.

The following are examples of disaster:
* Natural disasters, such as earthquakes or floods
* Technical failures, such as power failure or network connectivity
* Human actions, such as inadvertent misconfiguration or unauthorized or outside party access or modification

DR is an important part of your resiliency strategy, and It affects how your workload responds when a disaster strikes.

### RTO and RPO
The response to an event must be based on your business objectives, which specifies your workload's strategy for :
* Avoiding loss of data, known as the recovery point objective (RPO).
* Reducing downtime where your workload is not available for use, known as the recovery time objective (RTO).

## Disaster recovery and availability
Disaster recovery can be compared to availability, which is another important component of your resiliency strategy.

The objective of disaster recovery is business continuity. Availability concerns maximizing the time that a workload is available to perform its intended business function. Both should be part of your resiliency strategy.

### Resiliency
Resiliency is the ability of a workload to achieve the following:
* Recover from infrastructure, service, or application disruptions.
* Dynamically acquire computing resources to meet demand.
* Mitigate disruptions, such as misconfigurations or transient network issues.

### RPO and RTO
When creating a DR strategy, organizations commonly plan for RTO and RPO.
* Recovery time objective (RTO) is the maximum acceptable delay between the interruption of service and restoration of service.
* Recovery point objective (RPO) is the maximum acceptable amount of time since the last data recovery point.  

### MTBF and MTTR
Availability is calculated as follows:
MTBF/(MTBF+MTRR)
* MTBF is mean time between failures. It is the average time that passes without any failures.
* MTTR is mean time to recovery. It is the average time needed for the system to become operational again after a failure happens.

Disaster recovery focuses on disaster events. Availability focuses on more common disruptions of a smaller scale, such as component failures, network issues, software bugs, and load spikes.

Both availability and disaster recovery rely on some of the same best practices, such as monitoring for failures, deploying to multiple locations, and automatic failover. However, availability focuses on components of the workload, whereas disaster recovery focuses on discrete copies of the entire workload. Your disaster recovery strategy requires different approaches than those for availability. You can focus on deploying discrete systems to multiple locations, so that you can fail over the entire workload if necessary.

For example, you can mitigate a local flooding issue that causes a data center outage by employing a Multi-AZ strategy, because it would not affect more than one Availability Zone. However, an attack on production data would require you to invoke a disaster recovery strategy that fails over to backup data in another AWS Region. 

You must consider the availability of your workload in disaster recovery planning, because it will influence the approach that you take. A workload that runs on a single EC2 instance in one Availability Zone does not have high availability. If a local flooding issue affects that Availability Zone, this scenario requires failover to another zone to meet DR objectives. Compare this scenario to a highly available workload deployed across multiple active Regions and all Regions are serving production traffic. In this case, even in the unlikely event that a massive disaster makes a Region unusable, the DR strategy is accomplished by routing all traffic to the remaining Regions.

### Business continuity plans
A business continuity plan (BCP) is a document that describes how an organization will continue to operate if a disaster happens.

Your disaster recovery plan should be a subset of your organization’s BCP. The disaster recovery plan should not be a standalone document.

For example, an earthquake might prevent you from transporting products purchased on your ecommerce application. Even if effective DR keeps your workload functioning, your BCP needs to accommodate transportation needs.

### Disaster recovery in the cloud 
A disaster recovery plan on-premises might involve physically transporting tapes or replicating data to another site. A disaster recovery in the cloud is different and includes the following advantages over traditional environments:
* Recover quickly from a disaster with reduced complexity.
* With simple and repeatable testing, you can test more easily and more frequently.
* Lower management overhead decreases operational burden.
* Opportunities to automate decrease chances of error and improve recovery time.
* Lower costs by trading the fixed capital expense of a physical backup data center for the variable operating expense of a right-sized environment in the cloud.

### AWS Regions and Availability Zones
You can use the AWS infrastructure to your advantage when you implement a disaster recovery plan. 

#### AWS Regions
AWS has the concept of a Region, which is a physical location in the world where we cluster data centers. We call each group of logical data centers an Availability Zone. Each AWS Region consists of a minimum of three isolated and physically separate Availability Zones within a geographic area.

#### Availability Zones
Availability Zones consist of one or more discrete data centers, each with redundant power, low-latency networking, and connectivity, housed in separate facilities. AWS customers focused on high availability can design their applications to run in multiple AZs to achieve even greater fault tolerance.

By deploying across multiple Availability Zones in a single AWS Region, your workload is better protected against the failure of a single or even multiple data centers. For extra assurance with your single-Region deployment, you can back up data and configuration (including infrastructure definition) to another Region. This strategy reduces the scope of your disaster recovery plan to only include data backup and restoration.

For a disaster event that includes the risk of losing multiple data centers at a significant distance away from each other, you can also implement multi-Region architectures to protect against such disasters.

### Disaster recovery strategies
Disaster recovery strategies that are available to you within AWS can be broadly categorized into four approaches. They range from the low cost and low complexity of making backups to more complex strategies that use multiple, active Regions.

#### Backup and restore
This approach is suitable for mitigating against data loss or corruption.

Backups are created in the same Region as their source, and are also copied to another Region. This gives you the most effective protection from disasters of any scope of impact.

For Region failover, in addition to data recovery from backup, you must also be able to restore your infrastructure in the recovery Region. With infrastructure as code, such as AWS CloudFormation or AWS Cloud Development Kit (AWS CDK), you can deploy consistent infrastructure across Regions.

The backup and recovery strategy is considered the least efficient for RTO.

A Multi-AZ strategy, which replicates resources across Availability Zones, is necessary to provide high availability (HA). However, disaster events include human actions and software bugs that can erase or corrupt your data. If this happens, HA strategies will replicate these types of data errors. So for DR, you must additionally back up your data stores within the Region. By copying your data to another Region, you can handle the largest scope of disasters where a Region is affected. If a disaster prevents your workload from operating in a Region, the workload can be restored to a recovery Region and operate from there.

In addition to user data, be sure to back up code and configurations, including Amazon Machine Images (AMIs) that you use to create EC2 instances.

The following diagram illustrates how data can be saved, backed-up and restored. In an AZ, an EC2 instance is connected to an EBS volume and an EFS file system. The AZ also contains an Amazon RDS database. This infrastructure is copied into another AZ in the same Region and an AZ in another Region. These infrastructures are idle. Snapshots of the EBS volume and the RDS database are created and saved onto two Amazon S3 buckets. The EFS volume is backed up using AWS backup. Should a disaster occur to an AZ in the first Region, data can be restored from the backups in the infrastructure of the other AZ of the same Region. Cross-Region backup adds more resilience because data is copied to another Region and can be restored to an AZ located in a different Region.

##### Snapshots and backup
Your workload data will require a backup strategy that runs periodically or is continuous. How often you run your backup will determine your achievable recovery point (which should align to meet your RPO). The backup should also offer a way to restore it to the point at which it was taken.

Amazon Elastic Block Store (Amazon EBS) and Amazon Relational Database Service (Amazon RDS) can save data at different times (snapshots) in Amazon S3. Amazon Elastic File System (Amazon EFS) can be backed up using the AWS Backup service that also offers to create snapshots.

##### Cross-Region backup
Amazon S3 and AWS Backup both offer cross-Region replication, where the data is asynchronously replicated from one Region to another.

##### Redeployment
In addition to data, you must redeploy the infrastructure, configuration, and application code in the recovery Region. To permit infrastructure to be redeployed quickly without errors, you should always deploy using infrastructure as code (IaC) with services such as AWS CloudFormation.

#### Pilot light
This approach replicates your data from one Region to another, and provisions a copy of your core workload infrastructure in that Region. Resources that are required to support data replication and backup are always on. Other elements, such as application servers, are loaded with application code and configurations. However, they are switched off, and are used only when disaster recovery failover is invoked.

With the pilot light approach, you replicate your data from one Region to another and provision a copy of your core workload infrastructure. Resources required to support data replication and backup, such as databases and object storage, are always on. Other elements, such as application servers, are loaded with application code and configurations, but are turned off and are only used during testing or when disaster recovery failover is invoked.

In the following diagram, a multi-AZ architecture uses an Elastic Load Balancer that serves traffic to EC2 instances located in Auto Scaling groups that span multiple AZs. EC2 instances are connected to a primary instance of an Amazon Aurora DB instance located in an AZ and a read replica located onto another AZ. The application infrastructure is duplicated in another region but is turned off. The second infrastructure only has a read replica instance of the primary database instance turned on where data is copied asynchronously.

#### Warm standby
This approach involves the use of a scaled down, but fully functional, copy of your production environment in another Region. It extends the pilot light concept and decreases the time to recovery because your workload is always on in another Region.

The warm standby approach involves ensuring that there is a scaled down, but fully functional, copy of your production environment in another Region. This approach extends the pilot light concept and decreases the time to recovery because your workload is always on in another Region. With this approach, you can also more easily perform testing or implement continuous testing to increase confidence in your ability to recover from a disaster.

In the following diagram, very close to the previous pilot light infrastructure, a multi az architecture uses an Elastic Load Balancer that serves traffic to EC2 instance located in Auto Scaling groups that span multiple AZs. EC2 instances are connected to a primary instance of an Aamazon Aurora DB instance located in an AZ and a read replica located onto another AZ.  The application infrastructure is duplicated in another region but is turned on in only on AZ. The second infrastructure only has a read replica instance of the primary database instance turned on where data is copied asynchronously.

#### Active/active configuration
This approach runs your application workload simultaneously in multiple Regions by using one of the following configurations:

An active/active configuration where all Regions host the workload and serve traffic.
An active/passive configuration where the passive site does not actively serve traffic until a failover event occurs.
An active/active configuration serves application traffic from all Regions to which it is deployed. It is the most complex and costly approach to disaster recovery. However, it reduces recovery time to near zero for most disasters with the correct technology choices and implementation.

You can run your workload simultaneously in multiple Regions as part of a multi-site active/active strategy. Users are able to access your workload in any of the Regions in which it is deployed. This approach is the most complex and costly approach to disaster recovery. But it can reduce your recovery time to near zero for most disasters (however, data corruption mighty need to rely on backups, which usually results in a non-zero recovery point).

In the following diagram, a multi-AZ architecture uses an Elastic Load Balancer that serves traffic to EC2 instances located in Auto Scaling groups that span multiple AZs. EC2 instances are connected to a primary instance of an Amazon DynamoDB instance located in an AZ. A second instance of a DynamoDB instance in another AZ serves as a backup. The infrastructure is duplicated in another Region and is active.


Hot standby active/passive configurations serve traffic only from a single Region, and the standby Regions are used only for disaster recovery. It is a less operationally complex and costly approach than active/active. However, recovery times are longer because of the time needed to redirect the application from the failed active site to the now-active, former hot standby site.

### AWS Elastic Disaster Recovery
Elastic Disaster Recovery uses the pilot light strategy, and maintains a copy of data and turned-off resources in a virtual private cloud (VPC).

AWS Elastic Disaster Recovery minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery. It also offers automated failback capabilities for cloud workloads.

You can increase IT resilience when you use Elastic Disaster Recovery to replicate on-premises or cloud-based applications running on supported operating systems. Use the AWS Management Console to configure replication and launch settings, monitor data replication, and launch instances for drills or recovery.

#### AWS Elastic Disaster Recovery
Quickly and reliably recover your on-premises or cloud-based applications.

#### Set up
Set up Elastic Disaster Recovery on your source servers to initiate secure data replication. Your data is replicated to a staging area subnet in your AWS account, in the AWS Region that you select. The staging area design reduces costs by using affordable storage and minimal compute resources to maintain ongoing replication.

#### Testing
You can perform non-disruptive tests to confirm that implementation is complete.

#### Operation
During normal operation, maintain readiness by monitoring replication and periodically performing non-disruptive recovery and failback drills.

## Summary
* The AWS Well-Architected Framework provides a consistent approach to evaluate cloud architectures and guidance to help implement designs.
* The Well-Architected Framework is organized into six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.
* Each pillar documents a set of foundational questions that help you to understand whether a specific architecture aligns well with cloud best practices.
* There are four cloud architecture principles that help you take advantage of a cloud infrastructure for your business, while complying with the Well-Architected Framework:
 * Design for failure
 * Decouple components
 * Implement elasticity
 * Think parallel
* We also discussed the following additional best practices:
 * How to design highly available and scalable architectures
 * How a disaster recovery strategy is part of a business continuity plan
 * The different types of disaster recovery strategies
 * How AWS Elastic Disaster Recovery can help implement a disaster recovery strategy

## Additional Resources
### [AWS Well Architected](https://aws.amazon.com/architecture/well-architected)
AWS Well-Architected helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for a variety of applications and workloads. Built around six pillars—operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

### [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
To review the Well-Architected Framework.

### [Questions](https://docs.aws.amazon.com/wellarchitected/latest/framework/appendix.html)
For more information about the AWS Well-Architected Framework foundational questions and best practices.

### [Labs](https://www.wellarchitectedlabs.com/)
To engage in a collection of workshops and hands-on labs to help you learn, measure, and build using architectural best practices.

### [Architecture Blogs](https://aws.amazon.com/blogs/architecture/)
To read AWS Architecture blog posts.

### [AWS Architecture Center](https://aws.amazon.com/architecture)
To view reference architecture examples and diagrams.

### [AWS Well-Architected Lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses.html)
For more information about the lenses.

### [AWS Partners](https://partners.amazonaws.com/)
For more information about AWS Partners.

## AWS Well-Architected (WA) Tool
The Well-Architected Framework was created by AWS to help customers learn best practices, measure their architecture against these best practices, and identify areas that can be improved.

When using the AWS WA Tool, you will be using the six pillars of the Well-Architected Framework while reviewing your workload. You will answer a set of questions, based on how the business approaches that area. The sustainability pillar was introduced in 2021. Similar to the other pillars, it contains questions that can help you understand the energy consumption and environmental impact of your workload, helping your organization meet its sustainability goals.

### Operational excellence
The operational excellence pillar describes the ability to support development and run workloads effectively, gain insight into their operations, and continuously improve supporting processes and procedures to deliver business value.

### Security
The security pillar describes how to take advantage of cloud technologies to protect data, systems, and assets in a way that can improve your security posture.

### Reliability
The reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently when it’s expected to. This includes the ability to operate and test the workload through its total lifecycle. This pillar provides in-depth best practice guidance for implementing reliable workloads on AWS.

### Performance efficiency
The performance efficiency pillar describes the ability to use computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve.

### Cost optimization
The cost optimization pillar describes the ability to run systems to deliver business value at the lowest price point.

### Sustainability
The sustainability pillar describes the ability to continually improve sustainability impacts by reducing energy consumption and increasing efficiency across all components of a workload by maximizing the benefits from the provisioned resources and minimizing the total resources required.

#### AWS Well-Architected Lenses
The AWS Well-Architected Lenses extend the guidance that the AWS Well-Architected Framework offers to specific industry and technology domains with additional sets of questions and practices.

The AWS WA Tool provides the following:
* The Serverless Lens for serverless application workloads in the AWS Cloud
* The SaaS Lens for your software as a service (SaaS) workloads in the AWS Cloud

You can create custom lenses with your own pillars, questions, and best practices, and can apply custom lenses to a workload in the same way that you apply AWS provided lenses. You can tailor the questions in a custom lens to be specific to a particular technology, help you meet the governance needs within your organization, or extend the guidance provided by the Well-Architected Framework and the AWS lenses.

#### AWS Regions
The AWS WA Tool is available in many Regions, including AWS GovCloud (US) Regions, that are isolated Regions designed to host sensitive data and regulated workloads in the cloud.

With this Region expansion, customers with specific regulatory and compliance requirements and AWS Partners in both the public and commercial sectors can now conduct self-service Well-Architected Reviews.

#### Workload
The subject of an architectural review is a workload. We use the term workload to identify a set of components that together deliver business value, such as a customer-facing application like a website or a backend process like a payment service. A workload might consist of a subset of resources in a single AWS account or be a collection of multiple resources spanning multiple AWS accounts. Examples are websites, mobile applications, and analytic platforms. Resources can be located in a single AWS account or span multiple AWS accounts.

#### Milestone
You can keep track of how your workload changes over time to better understand how

your architecture has improved using milestones. Milestones keep a record of a review at a point in time.

### Reviewing Workloads
Welcome to the AWS Well-Architected Tool. When you're ready to review your workload, choose Define workload. Enter your workload details, such as the name of the workload and the environment, or the AWS regions in which your workload runs.


Choose next. Select an additional lens if needed, and choose Define workload.
 The Workload overview screen appears to review your workload, choose Start reviewing. This starts the question and answer experience. You can explore and choose the questions that appear in the left-navigation pane. When you choose a question, more information appears on the right side of the screen.

Additional context and answer choices are listed below. Select each of the best practices that you are following for your workload. Or if the question is not relevant to your workload at this time, you can choose Question does not apply to this workload. This will exclude the question from the review. 

For more information about an answer, choose the info link next to the answer. Each question is explained in more detail on the right side of the screen. You can hover over a term for a quick definition, or you can choose a term to see the full definition.

 A full definition of the term appears with links to additional information, such as service documentation. When you are ready to answer the next question, choose Next. This saves your response and moves to the next question. All of the questions for each pillar have now been answered for this example.

### Reviewing Improvement Plans
The Well-Architected Tool has an improvement plan that provides advice about AWS best practices. The Well-Architected Tool identifies areas of high and medium risk, as measured against the best practices in the AWS Well-Architected Framework.

Choose a question within a pillar and more information will appear, including steps to reduce risk. Choose a step to see the full improvement plan.

If you need help implementing the improvement plan, the Well-Architected Tool recommends using AWS re-Post to access a set of Q and As, as well as AWS IQ to connect with certified freelancers and AWS partners.

### Saving a Milestone
A milestone captures the current status of a workload review. You should save a milestone after you initially complete the question and answer portion of the workload review. As you make changes to your workload, based on items in your improvement plan, you can save additional milestones to measure progress.

A best practice is to save a milestone after major changes are made to your workload and you perform a workload review. To save a milestone, choose Save milestone from the Workload details page. In the milestone name field, enter a name for your milestone. In this example, we create a milestone named version 1.3. This creates a read-only record of the review at this point in time.

Then, choose save to save the milestone. After a milestone is saved, you cannot change the workload review data that was captured. When you delete a workload, its associated milestones are also deleted. You can create multiple milestones as your architecture evolves, and see what the review looks like for any previous milestone.

### Generating Reports
You can generate a workload report, which produces a PDF file containing the responses to the workload, review questions, your notes, and the current number of high and medium risks identified in your workload.

A report allows you to share details about your workload, review with others who do not have access to the AWS Well-Architected Tool.

To generate a workload report, choose Workloads in the left-navigation pane, select the workload you wish to generate a report for, and choose Generate Report.

The PDF file is generated and opens in your PDF viewer.

## Trusted Advisor
When running a business, you might need some advisers who can come in from the outside and say, hey, this process should be streamlined. Or, hey, I have some good tips on how to save money on your overhead. Or even, hey, I noticed I was able to waltz right in, go behind your cash register, and open the drawer without anyone noticing. Not good. 

The point I'm trying to make is, sometimes it's nice to have someone who knows the industry best practices, and knows what to look for, come in, and tell you what you need to change in order to run more efficiently, be more secure, or to save some money.

AWS has an automated advisor called AWS Trusted Advisor. This is a service that you can use in your AWS account that will evaluate your resources against five pillars. The pillars are cost optimization, performance, security, fault tolerance, and service limits. Trusted Advisor in real time runs through a series of checks for each pillar in your account, based on AWS best practices, and it compiles categorized items for you to look into, and you can view them directly in the AWS console. 

Some checks are free and are included in your AWS account, and others are available depending on the level of your support plan. Some examples of checks are, if you don't have multi-factor authentication turned on for your root user, it's going to let you know. If you have underutilized EC2 instances that might be able to be turned off in order to save money, or if you have EBS volumes that haven't been backed up in a reasonable amount of time, it will let you know that, too. To get a better idea, let's look at AWS Trusted Advisor in my own account. 

I'm already logged into the console, and I'm going to type in Trusted Advisor into the search. This brings me to the Trusted Advisor dashboard and I'm going to click on the cost optimization pillar first to view what it has found. You can see right away there are three levels of items it is showing me. There was the red circle, which means action recommended. The orange triangle, which means investigation recommended. And the green square, which means that there were no problems detected. 

Lucky for me, I don't have any red items for cost optimization, but I do have some orange items. Under cost optimization checks, I can read more about each check that Trusted Advisor ran. In this account, I do have some RDS instances that are idle, as well as some underutilized EC2 instances and EBS volumes. I could decide to scale these instances down vertically to save on cost, or if they aren't being used at all, I could decide to delete those instances and those EBS volumes altogether. It would require some investigation for me to determine what to do here. 

Now, let's click on the performance pillar. On this one, I don't have any warnings, but we can still read what checks Trusted Advisor performed. Like this one, for example, which checks for EBS volumes whose performance might've been affected by the throughput capability of the EC2 instance that it's attached to. 

Next, let's select the security pillar. In this demo account, you can see there are four alerts that are at the action recommended level. Trusted Advisor is trying to alert me, telling me I have weak password policies for IAM users, multi-factor authentication is not turned on for the root user, and there are security groups allowing public access to EC2 instances. All of these items are putting the resources in this account at risk, and should be dealt with as soon as possible. 

Now let's move on to fault tolerance. For this, there were a few things that are found to be insufficient. First, Trusted Advisor is telling me that there are EBS volumes without snapshots in this account. Remember, a snapshot is a backup. So without backups, if I had an EBS volume fail, I would lose that data. 

Another alert we have here is that my EC2 AZ balance is at the action recommended level. This means that my EC2 instances are not properly launched across AZs. So if one AZ has trouble, my application might incur an outage. Deploying across AZs would be the answer to this one.

Finally, let's check out service limits. This pillar will tell you when you are approaching or hitting AWS service limits. A lot of service limits are soft limits, meaning they are restrictions that can be lifted to some degree. It's good to know when you are approaching one of those limits, and when it's time to turn in a support ticket with AWS to get them changed. In this account, I can see that I have five VPCs, which is the regional limit. So I've hit that specific service limit. 

Trusted Advisor can help point you in the right direction when it comes to the five pillars. You can set up email alerts that go out to billing, operations, and security contacts, as checks get run in your account. Make sure you have Trusted Advisor turned on so that you too can start taking action to optimize your AWS account.


Trusted Advisor is a web service that inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices such as :
* The following security groups have unrestricted access. You should restrict access to only those IP addresses that require it.
* Trusted Advisor has identified four cost optimization checks that could save you money. You could save $3,290 a month.
* The following Amazon EBS volumes does not have any recent snapshots.

Trusted Advisor compares its findings to AWS best practices in six categories.
* **Cost optimization**: Recommendations that can potentially save you money. These checks highlight unused resources and opportunities to reduce your bill.
* **Performance**: Recommendations that can improve the speed and responsiveness of your applications.
* **Security**: Recommendations for security settings that can make your AWS solution more secure.
* **Fault tolerance**: Recommendations that help increase the resiliency of your AWS solution.
* **Service limits**: Checks the usage for your account and whether your account approaches or exceeds the limits (also called quotas) for AWS services and resources.
* **Operational excellence**: Checks your AWS environment using AWS Config rules to improve operational readiness. 

For the checks in each category, Trusted Advisor offers a list of recommended actions and additional resources available to learn more about AWS best practices. 

Trusted Advisor recommendations allows you to reduce your bill, improve the speed and responsiveness of your applications, make your applications more secure and increase their resiliency, and check whether your account approaches or exceeds the limits (also known as quotas) for AWS services and resources.

### Scanning the infrastructure
Trusted Advisor inspects your AWS environment and then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps. 

Depending on your level of support, the number of checks or types of verification varies.

### Checks
Trusted Advisor performs checks in the following categories:
* Cost optimization
* Performance
* Security
* Fault tolerance
* Service limits

### Recommendations
Trusted Advisor gives you a summary with the following checks categories:
* Action recommended
* Investigation recommended
* No problems detected

The guidance provided by Trusted Advisor can benefit your company at all stages of deployment. For example, you can use Trusted Advisor to assist you while you are creating new workflows and developing new applications. Or, you can use it while you are making ongoing improvements to existing applications and resources.

Overall, you can use Trusted Advisor for the following:
* To give you real-time analysis on your AWS environments
* To give you insights on your AWS Well-Architected workloads and run Well-Architected Reviews in less time, with more accuracy, accelerating the improvement cycle of your architecture

## Accessing Trusted Advisor

## Trusted Advisor checks
A check is a type of verification that Trusted Advisor performs on your AWS Resources. For instance, MFA on Root Account is a check of the Security category that verifies the root account and warns if multi-factor authentication (MFA) is not activated. 

The number and types of checks, and the way to access Trusted Advisor, depends on your AWS Support plan. If you have a Basic Support or Developer Support plan, you can use the Trusted Advisor console to access all checks in the service limits category and the following checks in the security category.

### Amazon EBS public snapshots
Checks the permission settings for your Amazon Elastic Block Store (Amazon EBS) volume snapshots, and alerts you if any snapshots are marked as public.

### Amazon RDS public snapshots
Checks the permission settings for your Amazon Relational Database Service (Amazon RDS) database snapshots, and alerts you if any snapshots are marked as public.

### Amazon S3 bucket permissions
Checks buckets in Amazon Simple Storage Service (Amazon S3) that have open access permissions or that allow access to any authenticated AWS user. 

### IAM use
Checks for your use of AWS Identity and Access Management (IAM). You can use IAM to create users, groups, and roles in AWS. You can also use permissions to control access to AWS resources.

### MFA on root account
Checks the root account and warns if MFA is not activated.

### Security groups – specific ports unrestricted
Checks security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports.

If you have a Business, Enterprise On-Ramp, or Enterprise Support plan, you can use the Trusted Advisor console and the AWS Support API to access all Trusted Advisor checks.

## Trusted Advisor and the Well-Architected Framework
In addition to providing analysis on your AWS environments, Trusted Advisor is also integrated into the AWS WA Tool. It can provide insights on your Well-Architected workloads and run Well-Architected Reviews in less time, with more accuracy, accelerating the improvement cycle of your architecture.

The Trusted Advisor checks sourced from the AWS WA Tool will contain an aggregated count of the number of high-risk issues discovered for each pillar and workload, based on the self-assessment that customers performed during the Well-Architected Review.

Previously, customers conducting Well-Architected Reviews had to spend time verifying their answers by double-checking their workloads to see if they were following best practices; there wasn’t a clear link between the workload being reviewed and it’s associated resources. With Trusted Advisor integration, the AWS WA Tool now presents findings based on automated Trusted Advisor resource checks, providing you with further contextual information during your reviews.

## Summary
### AWS WA Tool
The AWS WA Tool brings the best practices of the Well-Architected Framework into the AWS Management Console to help you review, measure, and improve your workloads. When using the AWS WA Tool, you will be using the six pillars of the Well-Architected Framework while reviewing your workload. You will answer a set of questions, based on how the business approaches that area. The sustainability pillar was introduced in 2021. Similar to the other pillars, it contains questions that can help you understand the energy consumption and environmental impact of your workload, helping your organization meet its sustainability goals.

### Trusted Advisor
Trusted Advisor is a web service that inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices. 

Trusted Advisor compares its findings to AWS best practices in five categories. For the checks in each category, Trusted Advisor offers a list of recommended actions and additional resources to learn more about AWS best practices.

#### Category: Recommendation Description
* **Cost optimization**: Recommendations that can potentially save you money. These checks highlight unused resources and opportunities to reduce your bill.
* **Performance**: Recommendations that can improve the speed and responsiveness of your applications.
* **Security**: Recommendations for security settings that can make your AWS solution more secure.
* **Fault tolerance**: Recommendations that help increase the resiliency of your AWS solution.
* **Service limit**: Checks the usage for your account and whether your account approaches or exceeds the limits (also called quotas) for AWS services and resources.

## Additional Resources
### [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
### [What is  the AWS Well-Architected Tool ?](https://aws.amazon.com/well-architected-tool)
### [Diving deeper into the AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html)
### [Creating a Custom Lens](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-create.html)

## Continuous Integration and Continuous Delivery
Continuous integration (CI) and continuous delivery (CD) are methods and processes to automate code build, tests, and deployments through a deployment pipeline. The goals are to improve the productivity and efficiency of an organization and lower the probability of human error.

### Continuous integration
Continuous integration most often refers to the build or integration stage of the software release process. It requires both an automation component (for example, a CI or build service) and a cultural component (for example, learning to integrate frequently). The key goals of continuous integration are to find and address bugs quickly, improve software quality, and reduce the time it takes to validate and release new software updates.

Why is continuous integration needed? 

In the past, developers on a team might work in isolation for an extended period of time and only merge their changes to the master branch when their work was completed. This made merging code changes difficult and time consuming. And it also resulted in bugs accumulating for a long time without correction. These factors made it more difficult to deliver updates to customers quickly.

The main purpose of continuous integration is to run unit tests that help make sure that the different components of the product still work individually as expected. This helps find and address bugs.

### Continuous delivery
Continuous delivery is a software development practice where every code change is automatically built, tested, and then deployed to a non-production testing or staging environment.

Continuous delivery expands on continuous integration by deploying all code changes to a testing environment or a production environment after the build stage.

Manual approval is required before pushing to production. When properly implemented, developers will always have a deployment-ready build artifact that has passed through a standardized test process.

Continuous delivery also runs functional and performance tests of the complete product. All components that were individually tested in the continuous integration phase are integrated on a test platform where functional tests are performed.

### Continuous deployment
Continuous deployment is similar to continuous delivery, but with automatic deployment to production. Tested code does not require an explicit approval before being pushed to production.


1. **Commit changes**. In the commit changes phase, the developer commits their code to source control management (SCM) systems such as Git.
2. **Source control**. Source control (or version control) is the practice of tracking and managing changes to code. SCM systems track changes in the code and initiate the build phase of the product.
3. **Build and test**. The build phase consists of building the different components of the product. This could include compiling things such as code in Java or creating some AWS resources. In the test phase, tests written by the development team are run. These tests are called unit tests and they aim to verify that the different components are individually working. If a test fails, the development team is notified so they can fix the issue.
4. **Deploy and test**. In the staging phase, all code and changes are deployed to a testing environment so the product can be tested as a whole. Integration tests are run that verify that the components work together. Performance tests and functional tests are also run to test actual use of the complete product. If all the tests are successful (and in the case of continuous delivery, they receive human approval), the product can be released into a production environment.

### Continuous integration benefits
#### Improve developer productivity
Continuous integration helps your team be more productive by freeing developers from manual tasks and encouraging behaviors that help reduce the number of errors and bugs released to customers.

#### Find and address bugs more quickly
With more frequent testing, your team can discover and address bugs earlier before they grow into larger problems later. 

#### Deliver updates faster
Continuous integration helps your team deliver updates to their customers faster and more frequently. 

### Continuous delivery benefits
#### Automate the software release process
With continuous delivery, your team can automatically build, test, and prepare code changes for release to production so that your software delivery is more efficient and rapid.

#### Improve developer productivity
These practices help your team be more productive by freeing developers from manual tasks and encouraging behaviors that help reduce the number of errors and bugs deployed to customers.

#### Find and address bugs more quickly
Your team can discover and address bugs earlier before they grow into larger problems with more frequent and comprehensive testing. With continuous delivery, you can more readily perform additional types of tests on your code because the entire process has been automated.

#### Deliver updates faster
Continuous delivery helps your team deliver updates to customers faster and more frequently. When continuous delivery is implemented properly, you will always have a deployment-ready build artifact that has passed through a standardized test process.

### Achieving operational excellence using CI/CD
The operational excellence pillar of the AWS Well-Architected Framework highlights the importance of adopting approaches that accomplish the following:
* Improve the flow of changes into production.
* Help achieve refactoring, fast feedback on quality, and bug fixing.
* Recover rapidly from changes that do not have desired outcomes.

This not only limits and helps to rapidly identify and remediate issues, but it also mitigates the impact of issues introduced through the deployment of changes.

Some best practices include the following, which are all made possible through a CI/CD pipeline:

* Use version control.
* Test and validate changes.
* Make small, reversible changes.
* Use build and deployment management systems.
* Fully automate integration and deployment.

The following examples illustrate how adopting CI/CD best practices can help you achieve operational excellence. To learn more, expand each of the following two categories.

#### Use build and deployment management systems
By providing mechanisms to manage build and deployment activities, you reduce the level of effort to perform repetitive tasks. You free your team members to focus on their high-value creative tasks and limit the introduction of error from manual procedures.

#### Fully automate integration and deployment
By implementing automated build and deployment management systems, you reduce errors caused by manual processes and reduce the effort to deploy changes, so your team members can focus on delivering business value.

## CI/CD on AWS
The AWS developer tools help you securely store and version your application's source code and automatically build, test, and deploy your application to AWS or your on-premises environment. Start with AWS CodePipeline to build a continuous integration or continuous delivery workflow that uses AWS CodeBuild, AWS CodeDeploy, and other tools, or use each service separately.

### AWS CodePipeline
AWS CodePipeline is a continuous integration and continuous delivery service for fast and reliable application and infrastructure updates. CodePipeline orchestrates the building, testing, and deploying of your code every time there is a code change, based on the release process models that you define. This helps you to rapidly and reliably deliver features and updates.

### AWS CodeBuild
AWS CodeBuild is a fully managed build service that compiles source code, runs tests, and produces software packages that are ready to deploy. With CodeBuild, you don’t need to provision, manage, and scale your own build servers. CodeBuild scales continuously and processes multiple builds concurrently, so your builds are not left waiting in a queue.

### AWS CodeDeploy
AWS CodeDeploy automates code deployments to any instance, including Amazon Elastic Compute Cloud (Amazon EC2) instances and on-premises servers. CodeDeploy simplifies rapid release of new features, helps you avoid downtime during application deployment, and handles the complexity of updating your applications.

### AWS CodeStar
With AWS CodeStar, you can quickly develop, build, and deploy applications on AWS. AWS CodeStar provides a unified user interface, so you can manage your software development activities in one place. With AWS CodeStar, you can set up your entire continuous delivery tool chain in minutes, so you can start releasing code faster.

### AWS CodeCommit
AWS CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories. CodeCommit eliminates the need for you to manage your own source control system or worry about scaling its infrastructure. You can use CodeCommit to store anything from code to binaries. It supports the standard functionality of Git, so it works seamlessly with your existing Git-based tools. 

## Setting up a CI/CD pipeline on AWS 
A pipeline helps you automate steps in your software delivery process, such as initiating automatic builds and then deploying to Amazon EC2 instances. You can use the AWS CodePipeline service to build, test, and deploy your code, based on the release process models that you define, and to orchestrate each step in your release process.

### AWS CodePipeline
You use CodePipeline to deploy code maintained in a CodeCommit or Amazon S3 repository to a single EC2 instance.

### Source stage
Your pipeline is initiated when you push a change to the CodeCommit repository or Amazon Simple Storage Service (Amazon S3) bucket.

### Staging
The pipeline uses AWS CodeBuild to build code, deploy artifacts to an Amazon S3 bucket, and run tests.

If tests are successful, AWS CodeDeploy deploys artifacts to your EC2 instances in your development environment.

### Production
If the previous deployment is successful, the pipeline will use AWS CodeDeploy to deploy artifacts on the production EC2 instances.

## Summary
### CI and CD Definitions 
Continuous integration (CI) and continuous delivery (CD) are methods and processes to automate code build, tests, and deployments through a deployment pipeline. The goals are to improve the productivity and efficiency of an organization and lower the probability of human error.

#### Continuous integration
Continuous integration most often refers to the build or integration stage of the software release process. It requires both an automation component (for example, a CI or build service) and a cultural component (for example, learning to integrate frequently). The key goals of continuous integration are to find and address bugs quickly, improve software quality, and reduce the time it takes to validate and release new software updates.

#### Continuous delivery
Continuous delivery is a software development practice where every code change is automatically built, tested, and then deployed to a non-production testing or staging environment.

Continuous delivery expands on continuous integration by deploying all code changes to a testing environment or a production environment after the build stage.

Manual approval is required before pushing to production. When properly implemented, developers will always have a deployment-ready build artifact that has passed through a standardized test process.

Continuous delivery also runs functional and performance tests of the complete product. All components that were individually tested in the continuous integration phase are integrated on a test platform where functional tests are performed.

#### Continuous deployment
Continuous deployment is similar to continuous delivery, but with automatic deployment to production. Tested code does not require an explicit approval before being pushed to production.

### CI Benefits
1. Improve developer productivity
2. Find and address bugs quickly
3. Deliver updates faster

### CD Benefits
1. Automate the software release process
2. Improve developer productivity
3. Find and address bugs quickly
4. Deliver updates faster

### Setting up a CI/CD pipeline on AWS 
A pipeline helps you automate steps in your software delivery process, such as initiating automatic builds and then deploying to Amazon EC2 instances. You can use the AWS CodePipeline service to build, test, and deploy your code, based on the release process models that you define, and to orchestrate each step in your release process.

## Additional Resources
### [What Is source control?](https://aws.amazon.com/devops/source-control/)
### [What Is Continuous Integration?](https://aws.amazon.com/devops/what-is-devops/#integration)
### [What Is Continuous Delivery?](https://aws.amazon.com/devops/what-is-devops/#cd)
### [Set Up a CI/CD Pipeline on AWS](https://aws.amazon.com/getting-started/hands-on/set-up-ci-cd-pipeline/)
### [Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html)
### [More information](https://aws.amazon.com/products/developer-tools/)

# Module Summary
## Architecting Best Practices
## Well-Architected Framework
* The AWS Well-Architected Framework provides a consistent approach to evaluate cloud architectures and guidance to help implement designs.
* Each pillar documents a set of foundational questions that help you to understand whether a specific architecture aligns well with cloud best practices.
* The Well-Architected Framework is organized into six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

## Architecting Best Practices
## Four Cloud Architecture Principles
1. Design for failure
2. Decouple components.
3. Implement elasticity
4. Think parallel

## Architecting Best Practices
## Additional Architecting Best Practices
* Design highly available and scalable architectures
* Disaster recovery strategy is part of a business continuity plan
* Enable different types of disaster recovery strategies
* AWS Elastic Disaster Recovery can help implement a disaster recovery strategy

## Cloud Architecture Tools
## AWS WA Tool and Trusted Advisor
* **AWS WA Tool**:  The AWS WA Tool brings the best practices of the Well-Architected Framework into the AWS Management Console to help you review, measure, and improve your workloads. The WA tool uses the six pillars of the Well-Architected Framework while reviewing your workload.
* **Trusted Advisor**: Trusted Advisor is a web service that inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices. Trusted Advisor compares its findings to AWS best practices in five categories - cost optimization, performance, security, fault tolerance, service limit. For the checks in each category, Trusted Advisor offers a list of recommended actions and additional resources to learn more about AWS best practices.

## Cloud Architecture, Continuous Integration and Continuous Delivery
## Continuous Integration and Continuous Delivery
Continuous integration (CI) and continuous delivery (CD) are methods and processes to automate code build, tests, and deployments through a deployment pipeline. The goals are to improve the productivity and efficiency of an organization and lower the probability of humans errors.

## Cloud Architecture, Continuous Integration and Continuous Delivery
## CI/CD on AWS
The AWS developer tools help you securely store and version your application's source code and automatically build, test, and deploy your application to AWS or your on-premises environment. Start with AWS CodePipeline to build a continuous integration or continuous delivery workflow that uses AWS CodeBuild, AWS CodeDeploy, and other tools, or use each service separately.

# Assessment
## What is true about fault isolation? **Fault isolation focuses on preventing the propagation of a failure**.
## What does AWS Well-Architected Tool use to assess workloads? (SELECT TWO) **AWS Well-Architected Lenses and AWS Well-Architected Framework Pillars**.
## What is the role of yje AWS Well-Architected Tool? **Help teams review AWS workloads**.
## What is the relationship between continuous integration and continuous deployment? **Continuous integration is a part of continuous deployment**.
## When is ir advised to conduct Well-Architected Reviews? **Periodically**.
## Which of the following statements is true about fault tolerance? **Fault tolerance focuses on maintaining availability**.
