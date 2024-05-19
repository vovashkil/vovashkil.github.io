###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Cloud Cost Management
## Business Needs
### Choosing the right deployment model
When selecting a cloud strategy, a company must consider factors such as required cloud application components, preferred resource management tools, and any legacy information technology (IT) infrastructure requirements.

The three cloud computing deployment models are:
* cloud-based, 
* on-premises, 
* and hybrid. 

#### CLOUD-BASED DEPLOYMENT
With cloud-based deployment, you can do the following:
* Run all parts of the application in the cloud.
* Migrate existing applications to the cloud.
* Design and build new cloud-native applications in the cloud.

In a **cloud-based deployment** model, you can migrate existing applications to the cloud, or you can design and build new applications in the cloud. You can build those applications on low-level infrastructure that requires your IT staff to manage them. Alternatively, you can build them using higher-level services that reduce the management, architecting, and scaling requirements of the core infrastructure.

For example, a company might create an application consisting of virtual servers, databases, and networking components that are fully based in the cloud.

#### ON-PREMISES DEPLOYMENT
With on-premises deployment, you can do the following:
* Deploy resources by using virtualization and resource management tools.
* Increase resource use by using application management and virtualization technologies.
* On-premises deployment is also called private cloud deployment. In this model, resources are deployed on premises by using virtualization and resource management tools.

For example, you might have applications that run on technology that is fully kept in your on-premises data center. Although this model is much like legacy IT infrastructure, incorporating application management and virtualization technologies helps increase resource use.

Most of the time, on-premises deployment is a launching-off point but not a long-term direction for a company.

#### HYBRID DEPLOYMENT
With hybrid deployment, you can do the following:
* Connect cloud-based resources to on-premises infrastructure.
* Integrate cloud-based resources with legacy IT applications.

In a hybrid deployment, cloud-based resources are connected to on-premises infrastructure. You might want to use this approach in a number of situations.

For example, suppose a company wants to use cloud services that can automate batch data processing and analytics. However, the company has several legacy applications that are more suitable on premises and will not be migrated to the cloud. With a hybrid deployment, the company can keep the legacy applications on premises while benefiting from the data and analytics services that run in the cloud.

### Benefits of cloud computing
Consider why a company might choose to take a particular cloud computing approach when addressing business needs.

#### Trade upfront expense for variable expenses
Upfront expenses refer to data centers, physical servers, and other resources you need to invest in before using them. Variable expenses mean you only pay for computing resources you consume. With variable expenses, you do not need to invest heavily in data centers and servers before you know how you’re going to use them.

When a company can turn resources on and off, they can experiment more than they would if they needed to provision upfront resources for each new trial. By taking a cloud computing approach that offers the benefit of variable expenses, companies can implement innovative solutions while saving on costs.

#### Stop spending money to run and maintain data centers
Computing in data centers often requires you to spend more money and time managing infrastructure and servers. 

A benefit of cloud computing is the ability to focus less on these tasks and more on your applications and customers.

#### Stop guessing capacity
With cloud computing, you don’t need to predict how much infrastructure capacity you need before deploying an application. 

For example, you can launch Amazon Elastic Compute Cloud (Amazon EC2) instances when needed and pay only for the compute time you use. Instead of paying for unused resources or dealing with limited capacity, you access only the capacity you need. You can also scale in or scale out in response to demand.

#### Benefit from massive economies of scale
By using cloud computing, you can achieve a lower variable cost than you can get on your own.

Because usage from hundreds of thousands of customers can aggregate in the cloud, providers, such as AWS, can achieve higher economies of scale. The economy of scale translates into lower pay-as-you-go prices. 

#### Increase speed and agility
The flexibility of cloud computing makes it easier for you to develop and deploy applications.

This flexibility provides you with more time to experiment and innovate. When computing in data centers, it might take weeks to obtain the new resources you need. By comparison, with cloud computing, you can access new resources in minutes.

#### Go global in minutes
The global footprint of the AWS Cloud means you can deploy applications to customers around the world quickly while providing them with low latency. This means that even if you are located in a different part of the world than your customers, your customers can access your applications with minimal delays. 

### Benefits of the cloud computing economy model
Most organizations are not in the business of running data centers. However, they spend a significant amount of time doing that instead of focusing on other tasks. 

#### COST SAVINGS
Cost savings benefits of the cloud computing economy model include the following: 
* Match supply and demand, improving usage.
* Take advantage of elastic cost base driven by usage patterns.
* Eliminate hardware refresh and maintenance programs.

#### STAFF PRODUCTIVITY
Staff productivity benefits of the cloud computing economy model include the following: 
* Drive maintenance efficiencies through automation and managed services. 
* Eliminate hardware support tasks. 
* Increase developer productivity.

#### OPERATIONAL RESILIENCE
Operational resilience benefits of the cloud computing economy model include the following: 
* Reduced cost of planned and unplanned outages.
* Reduced risk profile and cost of risk mitigation.
* Improved service level agreement (SLA). 

#### BUSINESS AGILITY
Business agility benefits of the cloud computing economy model include the following: 
* Reduced time to market.
* Increased operational agility (new market penetration, divestiture, and acquisition).
* Reduced cost and increased pace of innovation.

### Concepts of capex and opex
**Capex** stands for **capital expenditure**. This term groups all the expenses that have a value in the long term. In contrast, the term **opex**, or **operational expenditure**, corresponds to running expenses needed for the business to work on a daily basis.

### Concept of total cost of ownership
**The total cost of ownership (TCO**) is the addition of the capex and the opex. It corresponds to the price for buying infrastructure components added to the cost of running them.

### Comparison of TCO elements for both on-premises or co-location and AWS infrastructures
|            | On-premeses / Co-location | AWS |
| ---------- | ------------------------- | --- |
| Server / Compute | Purchase cost + annual maintenance fee | EC2 |
| Storage | Purchase software and hardware + annual maintenance fee | EBS/S3/Glacier |
| Networking | Purchase + annual maintenance | Direct connect + data transfer |
| Software | OS + Virtualization solution - licensing + support | Not required / included in EC2 |
| Application | Application licensing and support | Application licensing and support |
| Management | Manpower + managed services | Manpower + managed services |

#### Scaling
When running an on-premises business, you need to provision enough resources to manage peaks of traffic and meet your business needs. However, this incurs high costs that are not necessary most of the time. With cloud computing, you don’t need to overprovision resources up front to handle peak levels of business activity. Instead, you provision the number of resources you actually need. You can scale these resources up or down to instantly grow and shrink capacity as your business needs change. 

#### Using managed services
By using managed services, AWS helps you reduce the costs of managing and maintaining your resources.

#### Satisfying compliance requirements
AWS supports more security standards and compliance certifications than any other offering, including the following:
* Payment Card Industry Data Security Standard (PCI DSS)
* Health Insurance Portability and Accountability (HIPAA) Act or Health Information Technology for Economic and Clinical Health (HITECH) Act 
* Federal Risk and Authorization Management Program (FedRAMP)
* General Data Protection Regulation (GDPR)
* Federal Information Processing Standard Publication 140-2 (FIPS 140-2)
* National Institute of Standards and Technology 800-171 (NIST 800-171)

This helps customers satisfy compliance requirements for most regulatory agencies around the globe. 

## Cloud Strategy
### Cloud Financial Management
Cloud Financial Management (CFM) is a set of activities that make it possible for finance and technology organizations to manage, optimize, and plan costs as they run more workloads on AWS. By using a disciplined Cloud Financial Management approach, customers can find the right balance between agility and control, while improving unit economics and cost efficiencies. Cloud Financial Management is more than cost optimization. 

Effective Cloud Financial Management requires a partnership between a customer’s finance and technology teams. It spans activities across the following four pillars: See (measurement and accountability), Save (cost optimization), Plan (planning and forecasting), and Run (cloud financial operations). 

#### See (measurement and accountability)
What is your account strategy? How are you measuring, monitoring, and accounting for your spending in the cloud? What metric tracking are you doing? Are you using tools, such as a tagging strategy, to assist you? 

#### Save (cost optimization)
Which cost-optimization levers are you using to optimize your spend? Make sure that your organization is only paying for the resources you need. Work through your cost-optimization strategy with architecture, design, pricing models, and resource management.

#### Plan (planning and forecasting)
How are you currently planning for future cloud usage and spend? Understand the costs associated to drive more accurate financial and business planning with budgeting, cost and usage forecasting, and strategic business planning.

#### Run (cloud financial operations)
What are some of the operational processes and tools you use to manage your cloud expenditures and who is leading the effort? For a successful financial management and business strategy, ensure that you consider people, process, automation, and governance. 

### Activities and outcomes
#### MEASUREMENT AND ACCOUNTABILITY
Measurement and accountability focus on creating an appropriate level of granularity with respect to cost and usage visibility. They also influence cloud consumption behaviors through cost allocation reporting and metric tracking. 

| Activities               | Outcomes                      |
| ------------------------ | ----------------------------- |
| Implement an account structure and tagging dictionary. | Map cost and usage to workloads and organization structure. |
| Establish cost reporting and monitoring processes. | Proactively detect and address cost variances. |
| Perform show / chargeback for business units. | Drive cost-aware cloud consumption. |
| Measure and circulate efficiency. | Validate cloud investment decisions and outcomes. |

#### COST OPTIMIZATION
Make sure your organization pays only for the resources it needs through architecture, design, pricing models, and resource management. The Save pillar focuses on reducing the cost of your AWS footprint through technical and commercial optimizations. 

| Activities               | Outcomes                      |
| ------------------------ | ----------------------------- |
| Select cost-aware architecture and resources. | Increase staff productivity and operational resiliency. |
| Match capacity with demand. | Reduce overprovisioned spend. |
| Choose the right procing model. | Improve unit economics. |
| Implement processes to identify resource waste. | Reinvest cost savings into innovation and experimentation. |

#### PLANNING AND FORECASTING
It is valuable to understand costs associated with current and future technology needs to drive more accurate financial and business planning. Planning and forecasting focuses on setting expectations, improving business and financial predictability, and using AWS as an enabling agent for strategic, long-term business transformation. 

| Activities               | Outcomes                      |
| ------------------------ | ----------------------------- |
| Establish a process for budgeting and forecasting variable cloud usage, leveraging business drivers and unit costs. | Increase business and usage predictability. |
| Estimate costs with proof of concept. | Make cost-based decisions faster. |
| Build a business case and articulate expected value. | Prioritize spend/project based on expected value. |
| Understand how the cloud can enable/support strategic initiatives. | Gain executive buy-in and establish long-term cloud strategy. |

#### CLOUD FINANCIAL OPERATIONS
Cloud financial operations focuses on operational, people-related, and technological enablers of continuous Cloud Financial Mnagement that scale with your cloud journey.

| Activities               | Outcomes                      |
| ------------------------ | ----------------------------- |
| Secure executive sponsorship. | Remove barriers that could decrease or delay success. |
| Establish a partnership between finance and technology organizations. | Enable effective collaboration amongst the organizations. |
| Invest in people, governance, and tools. | Maximize cost efficiency and agility in a continuous manner at scale. |
| Celebrate cloud efficiency accomplishments. | Establish cost-aware behaviors and culture. |

### Key concepts around Cloud Financial Management
The following are key concepts related to Cloud Financial Management:
* Functional ownership
* Finance and technology partnership
* Cloud budgets and forecasts
* Cost-aware processes
* Cost-aware culture
* Business value delivered through cost optimization

## AWS Pricing Calculator
### AWS Pricing Calculator overview
The AWS Pricing Calculator is a tool that's available on the AWS website.

You can access it by navigating to calculator. aws and it allows you to generate estimates for architectures that you would build out and operate in the cloud.

You can build complex estimates including a variety of different resources such as EC2 instances, load balancers to distribute traffic across them, databases to help support our data storage requirements, and even S3 Standard, in order to store backups associated with our database environment.

We can use the calculator to identify our usage requirements. It will apply the applicable price rates for the Region that I've selected, and generates an estimate that we can then save and access later, or even share with others to review. In this demo, we're going to use the AWS Pricing Calculator to create an estimate for an architecture. 

We'll get insight into how to configure the Pricing Calculator with the available options for each service to determine the price of operation. To start, we'll go ahead and click on Create Estimate. Once we're in the Pricing Calculator, we can identify the service that we want to use. In this case, Amazon EC2.

Once we locate that service, we select the Configure button, and we're presented with options regarding the Region that we want to price this service out in.

For this particular example, we want to use US East one, North Virginia. We're asked to confirm that we want to change our region. Go ahead and select yes, Change Region.

Now we have two different options for creating an EC2 estimate. We have a quick estimate, which allows us to put some information in regarding instance size, pricing type, and block storage volumes. In this case, we want a little bit more detail. We're going to use the Advanced Estimate option. This is going to give us additional configuration items that we can determine for the long-term operation of this resource.

Now for this particular example, we're going to use a Linux operating system, so no changes are required there.

We have the ability to define workload variances, whether it's constant usage, a daily spike of traffic, weekly spike of traffic, or a monthly spike of traffic. In this case, we're using Constant Usage, and we want four instances, so we can adjust our instance count and next, we have to select the instance type that we want to run.

Now we have the ability to filterbased on the number of virtual CPUs, the amount of memory that's required for each of these instances, or maybe specify the network performance.

In this case, I already know the instance type I want to select, so I can start typing that information in, and my results are filtered down. I'm going to select the m5a.large instance. 

Scrolling down to additional options, I have different pricing models available. For this example, we're going to use On-Demand.

We're going to keep it simple. It's something that we want to run, but maybe it's for a short period of time.

Scrolling down, we can determine which EBS volume type we want to include. We're going to use a general purpose SSD or GP2 volume here. We only need four gigs of storage. However, we want to take daily snapshots of our volume and it's estimated that one gig of data is going to change per snapshot.

We're not going to specify any data transfer options in this case.

We want to go ahead and just add this to our estimate. Now, here I can review my estimate and see that the monthly cost to operate this solution consisting of four EC2 instances would be just over $256 a month, resulting in an annual cost for the first 12 months of $3,078.24.

But we're not done there. We want to be able to distribute traffic to these different instances. We're going to go ahead and add a service here. In this case, we're looking for the Elastic Load Balancer.

As we put in elastic, we can scroll down, and here we find Elastic Load Balancing. We can select Configure, and now we have to choose which type of elastic load balancer we want to use.

In this case, our architect has told us that we're using the Classic Load Balancer.

We only need one, and based on his estimates, we're going to be processing one gigabyte per hour of data.

We can add that to our estimate. Now that we have our web tier stood up with a mechanism for directing traffic across our various EC2 instances, we want to go ahead and add a data tier.

So we're going to go ahead and add, in this case, an RDS database for MySQL. So, putting in MySQL as a filter, I see Amazon RDS for MySQL, select Configure. I have the ability to determine whether I want to use a Single-AZ deployment or a Multi-AZ deployment. In this case, I have a pretty critical workload. This is my primary web presence, so I want to make this a Multi-AZ deployment. I want to provide for high availability. Now, the data that I'm dealing with here is pretty small in nature, so rather than the db.m5.12lx that defaulted in here, we're going to go ahead and look for a db.t3.micro. Relatively small database instance. We only need one of those. We're going to use On-Demand pricing here because this is a temporary situation, temporary website that we're standing up. And for our storage, we're going to adjust this to 20 gigabytes of storage, and then we can go ahead and add our database to our estimate.

Now finally, we want to make sure that we estimate the storage cost associated with things like backups. As a result, we're going to add one more service to our estimate and that's going to be S3. And in this case, we're using Simple Storage Service, S3 Standard.

We don't need to include data transfer. 

For S3 Standard, we're estimating that we're going to be storing one not gigabyte per month, but terabyte per month. 

So, as you're building out your estimates in the calculator, it's important that you review and adjust those different mechanisms as needed. In addition, we're estimating that we will have 30 put requests, one per day, to put our database backups into S3, and then we can go ahead and add that to our estimate. This brings our total estimated annual cost to just over $4,000 to operate this architecture.

Now, if I wanted to share this back, maybe with my architect to get their review and sign off that I've configured each of these different selections properly and accurate representation of the cost,

I can come up here to Save and Share. I have a public server acknowledgement that I have to agree to in order to continue, and here I have calculations have been saved.

I can copy the public link, and if I go to a new browser tab and paste that link, it brings up that estimate.

The link and the saved data is good for three years. Now if my enterprise architect receives this information, reviews it, and determines that some changes or adjustments need to be made, it's very simple. They can go in and edit any one of these individual items. Perhaps our estimate on the amount of data to be transferred per hour was wrong. Maybe we missed a zero there, and it's 10 gigs per hour. We can make that update and instantly save that to our estimate. The only nuance there is we would have to generate a new URL for that new estimate with our edited selection.

### Pricing components and related cost drivers
In the real world, AWS services usually don't run by themselves. For instance, Amazon EC2 provides compute capacity in the cloud, but EC2 instance costs vary depending on a number of factors.

#### AMAZON EC2 PRICING COMPONENTS
Pricing components for Amazon EC2 include the following:
* AWS Region
* Instance type
* Runtime per hour or second
* Number of instances
* Pricing model, which includes the following:
  * On-Demand Instances
  * Spot Instances
  * Compute Savings Plans
  * Reserved Instances
  * Dedicated Hosts

#### RELATED COST DRIVERS
Related cost drivers for EC2 instances include the following:
* Amazon Elastic Block Store (Amazon EBS)
* Load balancing
* Auto Scaling groups (provision additional EC2 instances)
* Elastic IP addresses
* Operating system (OS)
* Additional preinstalled software, such as the following:
  * Example: Amazon Machine Image (AMI) with Microsoft SQL Server preinstalled

### Estimate cost for a workload
In this activity, you will simulate the cost of the architecture displayed on the following diagram.

#### Amazon EC2
Use the following Amazon EC2 parameters:
* Linux
* m5a.large x4
* On-Demand
* Amazon EBS gp2 with 4 GB storage
* Daily snapshot where 1 GB of data changes each day 

#### Application Load Balancer
Use the following Application Load Balancer parameter:
* 1 GB per hour

#### Amazon Relational Database Service for MySQL
Use the following Amazon Relational Database Service (Amazon RDS) for MySQL parameters:
* Multi-AZ
* db.t3.micro
* On-Demand
* 20 GB storage

#### S3 Standard
Use the following S3 Standard parameters:
* 1 TB per month
* 3,000 PUT requests

## Planning for Data Transfer Charges
### Data transfer charges
When architecting for cost in AWS, it's important to consider networking and data-transfer cost. These costs can seem somewhat elusive. They're not necessarily tied directly to something that we provision or operate inside of our environment, but frequently we see cost associated with the movement of information between resources that we've provisioned.

In this module, we're going to talk about how data transfer is charged, trying to build visibility into your understanding of how those costs are incurred.

We're also going to talk about some strategies that you can use in order to help reduce data-transfer cost.

When thinking about data transfer, it's important to think about data transfer between services. Those services frequently sit at different levels within the AWS global infrastructure.

As we think about those different resources and whether they are deployed inside of a VPC, that either spans or is included in a single Availability Zone, or perhaps resources that are deployed at the Region level, we need to understand the cost implications of moving information across or between these different components in our infrastructure.

First, let's consider data transfer within an Availability Zone. Here we see several different services, between which we can transfer data in the same Availability Zone at no additional cost. Things like EC2 instances, RDS deployments, Redshift clusters, ElastiCache instances. Whenever we're transferring data into or out of, either a public or elastic IPv4 address, we are charged for data in each direction. That is one charge for the data transferred out of the source and a second charge for data transferred in to the destination. IPv6 results in data transferred into and out from an IPv6 address in a different VPC, and you have charges again in each direction. Where you are transferring data within the same Availability Zone, using private IPv4 addresses, there is no charge incurred.

When considering data transfer between Availability Zones in the same Region, we have a list of several services. Transfer between these services in the same Region is free.

For other services, data transferred in and out within the same region is charged in each direction.

With a charge out from the source and in to the destination. In the example shown here, it's moving from one EC2 instance and one Availability Zone to an EC2 instance in a second Availability Zone in the same Region.

When moving data between Regions in AWS, the data transfer between regions

is going to have the same cost as data transferred out to the internet.

This means that we will be charged for data coming out of our source Region, but not charged for data moving into our destination Region.

In the example that we have on this slide, we see data transfer coming out of the US East Region and that data transferring in to the Singapore Region.

There's no cost for data transfer in, the cost is associated with transferring data out of our North Virginia Region.

So, the pricing applied to this region-to-region data transfer is based on the source where the data is being transferred out of. Here we have representative pricing, from May, 2020, with data transfer prices to and from the internet for five different AWS Regions. You can see here that prices vary by Region and we also see an example of our tiered pricing, which yields volume discounts for greater volumes of data being transferred out of our AWS environment.

### AWS Global Infrastructure
When considering data transfer costs, it’s important to think about how services are positioned in the AWS Global Infrastructure. Data transfer charges vary depending on the direction of transfer, the source, and the destination.

### Data transfer in an Availability Zone
#### FREE
Data transferred between the following services in the same Availability Zone is free:
* Amazon EC2
* Amazon RDS
* Amazon Redshift
* Amazon ElastiCache instances
* Elastic network interfaces

Note: AWS services accessed through AWS PrivateLink endpoints will incur standard PrivateLink charges.

#### PUBLIC IPV4 AND IPV6
* IPv4: Data transferred in to and out from a public or Elastic IPv4 address is charged in each direction.
* IPv6: Data transferred in to and out from an IPv6 address in a different VPC is charged in each direction.

#### PRIVATE IPV4
There is no charge for data transfer within the same Availability Zone using a private IPv4 address.


### Data transfer between Availability Zones in the same Region
#### FREE
Transfer between the following services in the same AWS Region is free:
* Amazon Simple Storage Service (Amazon S3)
* Amazon S3 Glacier
* Amazon DynamoDB
* Amazon Simple Email Service (Amazon SES)
* Amazon Simple Queue Service (Amazon SQS)
* Amazon Kinesis
* Amazon Elastic Container Registry (Amazon ECR)
* Amazon Simple Notification Service (Amazon SNS)
* Amazon SimpleDB

Note: AWS services accessed through PrivateLink endpoints will incur standard PrivateLink charges.

#### OTHER SERVICES
For other services, data transferred in and out within the same Region is charged in each direction. 


### Data transfer between Regions
Data transfer between Regions has the same cost as data transferred out to the internet. Consider the following:
* You only pay for data transferred out; there is no cost for data transferred in.
* Price per gigabyte varies depending on the Region from which it is being transferred.

Pricing as of May 2020. 1 GB data transferred between EC2 instances in different Regions is charged at $0.02 out and $0 in.

### Knowledge Check
### Business case
AnyCompany is a fictious on-premises company selling online tickets for big partners events such as concerts, exhibitions, etc. 

AnyCompany considers moving to the AWS Cloud. Because of its business model relying on point-in-time events, AnyCompany, does not sell tickets everyday but rather has very high traffic peaks during short durations. 

In order to handle these peaks, the company had to provision a large number of servers. The company also needs to store large amounts of archive files corresponding to perviously organized events that they need to access several times a week.

#### Which benefit does AWS Cloud bring to the AnyCompany business model?
AnyCompany **can provision compute resources only when needed**.  Flexibility is one of the key components of the cloud and helps reducing companies' costs by provisionning only what is required. 

AnyCompany could be using some services eligible to AWS Free Tier but there is no guarantee that in the event of a traffic peak, the resources will stay within the Free Tier. Also not all AWS services are eligible to Free Tier. 

AWS never manages customer data security. It is a shared responsibility and users are responsible for customer data security. 

AWS manages security of the cloud, however AWS does not manage security in the cloud, thus operating system or firewall updates have to be performed by users.

#### Which product should AnyCompany use to store archive files and optimize costs in the event of a transition to AWS Cloud?
**Amaazon S3i**. Indeed S3 is very cost efficient and using the different tiering pricing, storage can be optimized depending on the frequency of access. 

Amazon EC2 instance store is incorrect as this is not persistant. If the instance reboots or is turned off, all the data is lost. Thus, this is not an appropriate storage option for archive files.

Amazon EBS could work as a storage option, however, it is more expensive if lots of data has to be stored compared to Amazon S3. 

Amazon EFS is not an appropriate storage as AnyCompany does not require a file system for its storage.  Also, Amazon S3 is less expensive and more scalable than Amazon EFS.

#### Which of the following configurations is the most cost effective to handle traffic peaks?
**Use EC2 Reserved Instances for the regular workload and provision additional EC2 On-Demand Instances to handle the peaks**. 

Using Reserved Instances to handle the peak is not possible as you do not want to keep the instance after the peak to optimize your costs.

Using Spot Instances to handle the peak is dangerous as if the same Instance type is required by AWS, your Instance will be terminated, resulting in a potential failure of your application. For the same reason, it is not possible to use Spot Instances

### Summary
#### Benefits of cloud computing
Consider why a company might choose to take a particular cloud computing approach when addressing business needs.

##### Trade upfront expense for variable expenses
Upfront expenses refer to data centers, physical servers, and other resources you need to invest in before using them. Variable expenses mean you only pay for computing resources you consume. With variable expenses, you do not need to invest heavily in data centers and servers before you know how you’re going to use them.

When a company can turn resources on and off, they can experiment more than they would if they needed to provision upfront resources for each new trial. By taking a cloud computing approach that offers the benefit of variable expenses, companies can implement innovative solutions while saving on costs.

##### Stop spending money to run and maintain data centers
Computing in data centers often requires you to spend more money and time managing infrastructure and servers. 

A benefit of cloud computing is the ability to focus less on these tasks and more on your applications and customers.

##### Stop guessing capacity
With cloud computing, you don’t need to predict how much infrastructure capacity you need before deploying an application. 

For example, you can launch Amazon Elastic Compute Cloud (Amazon EC2) instances when needed and pay only for the compute time you use. Instead of paying for unused resources or dealing with limited capacity, you access only the capacity you need. You can also scale in or scale out in response to demand.

##### Benefit from massive economies of scale
By using cloud computing, you can achieve a lower variable cost than you can get on your own.

Because usage from hundreds of thousands of customers can aggregate in the cloud, providers, such as AWS, can achieve higher economies of scale. The economy of scale translates into lower pay-as-you-go prices. 

##### Increase speed and agility
The flexibility of cloud computing makes it easier for you to develop and deploy applications.

This flexibility provides you with more time to experiment and innovate. When computing in data centers, it might take weeks to obtain the new resources you need. By comparison, with cloud computing, you can access new resources in minutes.

##### Go global in minutes
The global footprint of the AWS Cloud means you can deploy applications to customers around the world quickly while providing them with low latency. This means that even if you are located in a different part of the world than your customers, your customers can access your applications with minimal delays. 

#### Key concepts around Cloud Financial Management
* Functional ownership
* Finance and technology partnership
* Cloud budgets and forecasts
* Cost-aware processes
* Cost-aware culture
* Business value delivered through cost optimization

#### What is AWS Pricing Calculator
AWS Pricing Calculator is a web-based planning tool that you can use to create estimates for your AWS use cases. You can use it to model your solutions before building them, explore the AWS service price points, and review the calculations behind your estimates. You can use it to help you plan how you spend, find cost saving opportunities, and make informed decisions when using Amazon Web Services. 

### Additional Resources
#### [Cost Optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)

#### [AWS Pricing Calculator](https://calculator.aws/)

## Cloud Cost Analyses and Tracking
### Pre-assessment
#### Which of these tools is part of the AWS Billing console?
**Purchase orders**. The purchase orders tool is part of the AWS Billing console, all the other entries are part of the AWS Cost Mangement console.

#### What is the delay for a tag to appear on the AWS Cost and Usage Report when you activate a user-defined tag for a given resource?
**24 hours**. There is a 24 hour delay for an activated tag to appear on the Cost and Usage report.

#### Which of these tools can you use to forecast your costs for your entire infrastructure?
**AWS Cost Explorer**. You can use the AWS Cost Explorer to forecast your costs for your entire infrastructure, by product, and much more.

### AWS Billing console
With AWS Billing and Cost Management, you can pay your AWS bill, monitor your usage, and analyze and control your costs.

The Billing and Cost Management service provides features that you can use to do the following: 
* Estimate and plan your AWS costs.
* Receive alerts if your costs exceed a threshold that you set.
* Assess your biggest investments in AWS resources.
* Simplify your accounting if you work with multiple accounts.

**AWS account owners can delegate access to specific AWS Identity and Access Management (IAM) users who need to view or manage the billing and cost management data for an AWS account. If you create a single AWS account, only the AWS account owner (AWS account root user) has access to view and manage billing information. IAM users cannot access billing data until the account owner activates IAM access and attaches policies that provide billing actions to the user or role.**

### AWS Billing console dashboard
#### Menu
Within the menu, you can navigate through the different features of Billing and Cost Management. 

From here, you can visualize the number of available credits. You can also create an AWS Cost & Usage Report or use to create AWS Budgets. 

#### Cost trend
This space highlights the trends over a number of months that you chose (the last 3 or 6 months) so that you can see the evolution of your costs for the five most-used services. 

You can customize the display to get another type of diagram or to extend or reduce the period of time that you want to view.

#### Current costs
This part displays your current costs at the current time of the month.

#### Variation
This part indicates the cost variation compared to the previous month.

#### Previous month cost
This part indicates the cost of the previous month at the same period of the month. This helps you to have an idea of the evolution of your costs and to forecast your final monthly costs.

#### Your bill
You can view your bill by choosing this button.

### Features of AWS Billing
To learn more about the AWS Billing console features, choose the arrow buttons to display each of the following seven steps.

1. Manage your account

Manage your account settings using the AWS Management Console and Billing console. This includes designating your default currency, editing alternate contacts, adding or removing Regions, updating your tax information, and closing your AWS account. The Close your account section calls out considerations such as terminating resources before you proceed with closing an account. This way, you aren't charged for unused services.

2. View your bill

You can use the Billing console to view your past bill details or your estimated charges for your current month. This section outlines how you can view your bills, download PDF copies of your charges, and set up monthly emails to receive your invoices. It also covers how you can use other resources such as AWS Cost and Usage Reports. 

3. Managing your payments

You can view your estimated bills and pay your AWS invoices in your preferred currency by setting a payment currency. AWS converts your bill to your preferred currency after your bill is finalized. Until then, all of the preferred currency amounts shown in the console are estimated in US dollars (USD). AWS guarantees your exchange rate. This is so that refunds use the same exchange rate as your original transaction.

4. AWS Purchase Order Management

Manage your AWS purchase orders in a self-service way by taking care of multiple purchase orders all in one place. This can help to reduce your overhead costs and increase the accuracy and efficiency of your overall procure-to-pay process. Use the Billing console to manage your purchase orders and configure how they reflect on your invoices.

5. AWS Cost Categories

Manage your AWS costs with AWS Cost Categories by mapping your cost and usage into meaningful categories. This section defines terms that are used in the console for supported dimensions, operations, rule types, and status. The section also provides more information on how you can create, edit, delete, and split the charges within cost categories.

6. Payment profile

You can use payment profiles to assign more than one payment method to your automatic payments. If you receive invoices from more than one AWS service provider (seller of record), you can use payment profiles to assign a unique payment method for each one. After you create a payment profile for a service provider, your payment profile pays your AWS bills automatically. In this section, learn how to use the Billing console to set up a custom payment profile.

7. Consolidate billing for AWS Organizations

Use the consolidated billing feature for AWS Organizations to combine your billing for multiple AWS accounts. This outlines the consolidated billing process, differences for Amazon Internet Services Pvt. Ltd accounts, and details for discounts.

### Bills in AWS Billing console: Visualization
1. Access your bill

You can see details about your bill by selecting Bills in the menu.

2. Download or print

You can download your bill as a CSV file or print it.

3. Expand for more details

To obtain more details about the billing of the different services you used, you can choose Expand All.  For example, you can see your bill per service, per Region, which can be very useful to optimize your architecture.

### AWS Purchase Order Management
With the AWS Purchase Order Management service, you can manage your AWS purchase orders (POs) in a self-service manner. Centralize the management of multiple POs, reduce overhead costs in matching invoices with POs, and increase the accuracy and efficiency in your procure-to-pay process.

AWS Purchase Order Management gives you the ability to define and manage POs in a way that meets your unique business needs. Manage your PO information from the Purchase Orders dashboard in the AWS Billing console, configure multiple POs, and define the rules of how they map to your AWS invoices. Monitor your PO status and balance on your Purchase Orders dashboard. Stay informed with email notifications when your POs approach expiration or run out of balance.

#### Add a purchase order
You can use the Billing and Cost Management console to add purchase orders to use in your invoices. Adding a purchase order is a two-step process involving purchase orders and line item configurations. First, you enter your purchase order details (for example, purchase order ID, shipping address, effective and expiration month). Then, you define the purchase order line item configurations that are used to match the purchase order with an invoice. If you add multiple purchase orders, we use the purchase order that has the line item best matching the invoice being generated.

### AWS Cost Management Console
The Billing console works closely with the AWS Cost Management console. The AWS Cost Management console features are useful to optimize your future costs. 

#### Understanding your reports
AWS Cost Explorer provides default reports, which you cannot modify, but you can use to create your own custom reports. 
The default reports provided in AWS Cost Explorer are as follows:
* Cost and usage reports
* Reservation reports
* Savings plans reports

**An important difference between AWS Cost Explorer and AWS Cost and Usage Report (CUR) is that AWS Cost Explorer shows daily or monthly data granularity, whereas AWS CUR can have hourly data granularity. In addition, AWS CUR provides individual resource-level data for all services.**

#### AWS Cost Explorer
AWS Cost Explorer is a no-charge, data visualization tool that you can use to view graphs of your AWS costs (also known as your spend data). You can use it to view costs based on your AWS usage.

### Control and monitor cloud costs
#### AWS Cost Anomaly Detection 
AWS Cost Anomaly Detection uses advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. With three simple steps, you can create your own contextualized monitor and receive alerts when any anomalous spend is detected. Let builders build and let AWS Cost Anomaly Detection monitor your spend and reduce the risk of billing surprises.

##### Create pre-built or custom monitors
With the cost monitor creation process, you can create spend segments and evaluate spend anomalies at a preferred, granular level. For example, you can build monitors for specific services, linked accounts, cost categories, or tags.

##### Set alert subscription
After you have created your cost monitor, you can choose your alerting preference by setting up a dollar threshold. For example, only alert on anomalies with impact greater than $1,000. You don’t need to define an anomaly, such as a percent or dollar increase, as Anomaly Detection does this automatically for you and adjusts over time.

##### Receive alerts when anomalous spend is detected
After cost monitors and alert subscriptions are created, you’re all set! Anomaly Detection will begin to work within 24 hours, and you will be notified if any anomaly meets your alert threshold. You can visit your Anomaly Detection dashboard to monitor the activities, including anomalies detected that are below your alert threshold.

### AWS Budgets overview
With AWS Budgets, you can set custom budgets to track your costs and usage and respond quickly to alerts received from email or Amazon Simple Notification Service (Amazon SNS) notifications when you exceed, or when you are forecasted to exceed, your thresholds. Another key feature of Budgets is that it also alerts on projected underutilization of usage of Reserved Instances (RIs) and Savings Plans.

### Use cases
#### Monitor costs and usage
Set your preferred budget period to daily, monthly, quarterly, or annually, and create specific budget limits.

#### Create scheduled reports
Stay informed on how actual or forecasted costs and usage progress toward your budget threshold.

#### Respond to thresholds
Set up custom actions to run automatically, or through an approval process, when a budget target is exceeded.

### Demo–Setting up a budget with AWS Budgets
AWS Budgets is a tool that allows us to define and set expectations associated with spend inside of our account. With Budgets, we can manage the costs associated with different types of resources or architectures in our environment. We can plan our service usage, our service costs. We can look at information related to our reserved instances and savings plans, and provide alerts when something is not meeting our budget expectations.

Here, we have an example of the AWS Budgets dashboard showing a list of the various budgets that have been configured for this account. And, based on the information provided, we can see which budgets are at risk of not meeting their budget expectations.

Now, one of the great features of Budgets is that we can set up alerts. A best practice around budget alerts is to create notifications for those items, route them to SNS, where you can manage subscriptions on who should be receiving those individual budget alerts. Recommend that you set Budgets to alert for actual or forecasted values, depending on which of those different options makes the most sense for you.

Where you're setting a budget alert for an actual amount, consider setting that threshold slightly lower than what you would for a forecasted amount. It gives you more time to react and make adjustments to hopefully meet your budget expectations.

AWS requires approximately five weeks of usage data to generate your budget forecast, but as you are configuring your forecast, if it's related to resources already running in your environment for that period of time, it will provide you with data for what your prior usage or spend has been, and it provides a good measuring stick for determining where you should set your budget.

Is your objective to reduce cost? If so, consider setting your budget threshold lower than that spend amount.

If it's to contain or manage growth, consider which percentage of growth you want to accommodate, and then set your alerts accordingly.

Remember that a budget must have permissions to send a notification to your topic.

Permissions are required for a number of different services throughout AWS, and this one is no different.

You can also configure your budget alerts to go to Amazon Chime or Slack.

You can integrate the AWS Budgets with AWS Chatbot service to receive those alerts.

You configure an SNS topic, navigate to the Chatbot console, and then map your topic to the appropriate channel or Chime room. Inside of the latest AWS account billing information, there are step-by-step instructions on how to integrate those services.

AWS Budgets is a tool that allows us to define expectations around spend or usage in our AWS accounts.

To access AWS Budgets, we can go directly from the AWS Management Console and search for AWS Budgets. We're presented with a dashboard of all the various budgets that have been established inside of our account. The dashboard lists individual budgets by name and by type, and gives us information related to current spend or usage, the budgeted spend or usage, and also the forecasted spend or usage for this period.

We also have visual indicators comparing the variants for current versus budgeted and forecasted versus budgeted spend or usage.

Now, to create a budget is very simple. Simply press the Create Budget button at the top right and select the type of budget that you'd like to create.

We have the ability to create cost budgets, usage budgets, and also budgets related to reserved instances or savings plans.

In this case, we're gonna create a usage budget. Simply select the type of budget you'd like to create, and press Set Your Budget. We have to provide it with a name. In this case, we're going to call it a demo budget. We define the period that this budget is valid for. In this case, we're looking to establish a monthly budget for usage.

We can also determine whether this is a recurring budget, something that we want to track progress against every single month, or if it's something that expires, it's a short-term budget that we want to establish and track our spend or usage against.

In this case, we're going to leave it as recurring. We have a default usage unit that is selected for us. In this case, it's EC2 running hours. We're going to go ahead and leave that there. If you wanted to use a different usage unit, maybe something like S3 storage, you can simply search for the service or unit that you'd like to track. For our budget amount, we have the ability to leverage a fixed amount, or we can specify individual amounts that are relevant for each month. We're going to select monthly budget planning. We wanna get a little bit more granular in the tracking of this information.

Now, because we have EC2 usage going back for some time in this account, we have an estimate for what the last month's usage was. In this case, coming in just under 11,000 hours. I can take that information, break it up across the 12 months, and populate that data manually, or I can use an auto-fill feature to fill the budgeted amounts.

So, based on last month's usage, I can use 11,000 hours as a starting point, and then I have the ability to include budget growth. In this case, I want to keep growth relatively small, so we're going to put 5% growth into our calculation. Press the auto-fill button, and the calculations are performed for us, and that data is populated in each of the individual monthly budgets.

We press Apply. And, we have a visualization of what usage has been in the past that we can use in order to track against our budgeted amounts. If I had individual filters that I wanted to apply, restricting this budget data to a particular department, or environment, or workload,

I have different filters that are available, including tags that I could use to tailor this to my specific use case.

Once we've set up our budget amounts, we can press configure alerts to determine what we want to alert on. I have the ability to alert on actual usage or on forecasted usage. Remember that if you're using actual usage, you may want to have an earlier alert, set that threshold slightly lower, so that you have ample time to investigate and then remediate any situations which may have driven that alert.

In this case, we're going to use a forecasted usage amount and we want to be alerted when we hit the 85% threshold of our budgeted amount. I can add email contacts directly into this particular alert.

So, I'm going to go ahead and enter my email address. And then I can also leverage an SNS topic. If I would rather more centrally manage notifications based on SNS topics and subscriptions, I can also send those alerts to an SNS topic, if I would prefer.

We're going to go ahead and click Confirm Budget here where we can review the information based on the configuration items that we've set, and then create that budget. We also have the ability with AWS Budgets to establish budget reports.

And, budget reports can be created to present information related to different budgets that we select and email that data directly to a set of recipients.

So here, for this particular daily report, I have selected four different budgets from inside of my account. And if I review the delivery settings, I can see that this report is delivered daily to my email address. So, each day that information would be sent to me.

I don't have to log into the console to try to identify or review where I stand from a budgetary perspective.


### Resource tagging
You can assign metadata to your AWS resources in the form of tags. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. You can create tags to categorize resources by purpose, owner, environment, or other criteria. 

Note that the maximum number of active cost allocation tag keys for each payer account is 500 tags, and that each AWS resource can have a maximum of 50 user created tags. System created tags that begin with aws: are reserved for AWS use, and do not count against this limit.

### AWS tagging strategies
#### TAGS FOR RESOURCE ORGANIZATION
Tags are a good way to organize AWS resources in the AWS Management Console. You can configure tags to display with resources, and you can search and filter by tag. 

With the AWS Resource Groups service, you can create groups of AWS resources based on one or more tags or portions of tags. You can also create groups based on their occurrence in an AWS CloudFormation stack. Using Resource Groups and Tag Editor, you can consolidate and view data for applications that consist of multiple services, resources, and Regions in one place. 

#### TAGS FOR COST ALLOCATION
With AWS Cost Explorer and detailed billing reports, you can break down AWS costs by tag. Typically, you use business tags such as cost center or business unit, customer, or project to associate AWS costs with traditional cost-allocation dimensions.

In the AWS Cost and Usage report, you can use the Resource columns to find information about the specific resources covered by a line item. These columns include user-defined cost allocation tags.

#### TAGS FOR AUTOMATION
Resource or service-specific tags are used to filter resources during automation activities. Automation tags opt in or opt out of automated tasks. They also identify specific versions of resources to archive, update, or delete. For example, you can run automated start or stop scripts that turn off development environments during nonbusiness hours to reduce costs. 

In this scenario, Amazon Elastic Compute Cloud (Amazon EC2) instance tags are a simple way to identify instances to opt out of this action. For scripts that find and delete stale, out-of-date, or rolling Amazon Elastic Block Store (Amazon EBS) snapshots, snapshot tags can add an extra dimension of search criteria. 

#### TAGS FOR ACCESS CONTROL
AWS IAM policies support tag-based conditions, letting you constrain IAM permissions based on specific tags or tag values. For example, IAM user or role permissions can include conditions to limit Amazon EC2 API calls to specific environments (such as development, test, or production) based on their tags. 

The same strategy can be used to limit API calls to specific Amazon Virtual Private Cloud (Amazon VPC) networks. Support for tag-based, resource-level IAM permissions is service specific. When you use tag-based conditions for access control, be sure to define and restrict who can modify the tags.

### Tagging: Best practices
#### Best practice: Identifying tag requirements
* Employ a cross-functional team to identify tag requirements.
* Use tags consistently.
* Assign owners to define tag value propositions.
* Focus on required and conditionally required tags.
* Start small; less is more.

#### Best practice: Naming tags and resources
* Adopt a standardize approach for tag names.
* Standardize names for AWS resources.

#### AWS-defined tag examples
##### aws:createdBy
aws:createdBy defined and applies to supported AWS resources for cost allocation purposes.

##### aws:ec2spot:fleet-request-id 
aws:ec2spot:fleet-request-id identifies the Amazon EC2 Spot Instance request that launched the instance.

##### lambda-console:blueprint
lambda-console:blueprint identifies the blueprint used as a template for an AWS Lambda function.

##### aws:cloudformation:stack-name
aws:cloudformation:stack-name identifies the AWS CloudFormation stack that created the resource.

#### Best practice: Cost allocation tags
* Align cost allocation tags with financial reporting dimensions.
* Use linked accounts and cost allocation tags.
* Avoid multi-valued cost allocation tags.
* Tag everything possible.

#### Align tags with financial reporting
AWS provides detailed cost reports and data extracts to help you monitor and manage your AWS spend. When you designate specific tags as cost allocation tags in the AWS Billing and Cost Management console, billing data for AWS resources will include them. 

Remember, billing information is point-in-time data, so cost allocation tags appear in your billing data only after you have performed the following:
* Specified them in the AWS Billing and Cost Management console
* Tagged resources with them

A natural way to identify the cost allocation tags you need is by looking at your current IT financial reporting practices. Typically, financial reporting covers a variety of dimensions, such as business unit, cost center, product, geographic area, or department. Aligning cost allocation tags with these financial reporting dimensions simplifies and streamlines your AWS cost management. 

#### Best practice: Tag governance and data management
* Integrate with authoritative data sources.
* Use compound tag values judiciously.
* Use automation to proactively tag resources.
* Constrain tag values with AWS Service Catalog.
* Propagate tag values across related resources.
* Lock down tags used for access control.
* Remediate untagged resources.
* Implement a tag governance process.

### Using AWS Cost Explorer
#### AWS Cost Management
AWS Cost Management tools give you visibility into your AWS costs and usage. There are a range of AWS Cost Management tools to help you access, organize, understand, control and optimize your costs.

#### Cost Explorer
Cost Explorer is a tool you can use to view and analyze your costs and usage. You can explore your usage and costs using the main graph, the Cost Explorer cost and usage reports, or the Cost Explorer reserved instance reports. You can view data for the past 12 months, and forecast how much you're likely to spend for the next 12 months. You can also get recommendations for which reserved instances to purchase. 

You can use Cost Explorer to identify areas that need further inquiry, and see trends you can use to understand your costs.

First, let's go to Cost Explorer. To do so, in your account, choose Billing Dashboard, this brings you to your AWS Billing Dashboard.

Now let's look at the left panel and more precisely the Cost management section. Choose Cost Explorer, and then choose Launch Cost Explorer. You can now create a new cost and usage report.

By default, the report highlights the past six months. It gives you an overview of your cost per month per product.

If you scroll down, you can get more details about your costs per products. You might want to customize your report. Imagine you want to generate a report for the past year. Go to date range, and modify the start date so that it corresponds to a period of one year.

Choose Apply.

You now have a view of your costs per month over the past year.

Now let's focus on a shorter period of time. From April, 2022 to the end of May, 2022, for example.

First, go to date range and select the corresponding period. Then for granularity, choose daily.

You now have a view of your cost per day per service. You can zoom in by choosing hourly as the granularity.

However, choosing hourly will reduce your data set to the past 14 days.

You will need to turn on this feature through the Payer accounts Cost Explorer preferences page.

To do so, go back to AWS Cost Management. In the navigation pane, choose Preferences.

From there, you can select the corresponding checkbox and activate the hourly granularity level.

You can also activate the right sizing recommendations for Amazon Elastic Compute Cloud or Amazon EC2 instances.

Here, we will activate the two features. After you are done, choose Save preferences.

A great advantage of Cost Explorer is that it lets you select precisely the services you want to investigate.

Imagine we want to see the costs from the usage of Amazon Kinesis. For service, choose Includes. Select Kinesis, and then choose Apply. Now the dashboard displays only costs for Kinesis.

Because this account mainly used Amazon SageMaker, we will use a filter to exclude SageMaker from the report, so we can better see the other products.

One of the features of Cost Explorer is that you can select one, several, or all the linked accounts to visualize data more specifically. To do so, choose Linked account, and then select the account you are interested in visualizing. Now let's say you want to investigate a specific AWS region.

You can select it by choosing the Region you want to visualize, for example, London.

Another interesting feature is to select resources using their tags.

For example, if we choose Amazon SageMaker, and then choose Notebook instances, we can see its associated tag at the bottom of the page.

Here the key is machine_learning and its value is exploration_notebook_Python3.

If we want to know precisely how much this instance cost, we need to go back to Cost Explorer.

Here we can select the appropriate tag. We now have a precise view of the cost of one specific instance using its tag.

AWS Cost Management also offers the possibility to generate reports for savings plans and reserved instances.

Go back to the AWS Cost Management. In the navigation pane, choose Reports. Choose Create New Report.

Here you will be asked to choose a report type. By default, the cost and usage type is selected.

This is the same report type we used previously in this video, however you can see two additional categories, one for savings plans reports and another for reservation reports.

In each of these two categories, you can choose between two types of reports.

One is utilization and the other is coverage. Utilization will give you insights about the costs and usage of your savings plans or reserved instances.

The coverage report, however, will indicate how much of your eligible spend was covered by your savings plans or reserved instances, based on the selected time period.

This feature can be very useful to set target coverage and identify targets for savings.

We are now reaching the end of this video. Let's review what you learned so far.

You learned how to generate reports using Cost Explorer. You learned how to customize your report by changing the granularity, selecting specific services, accounts, or Regions and you learned to visualize resources using their tags. 

Finally, you learned the differences between utilization and coverage reports for both savings plans and reservation reports.

### Knowledge Check
#### Which of these statements best describes AWS Budgets?
**With AWS Budgets, you can set alarms that trigger when a cost limit is reached for a given resource.**  AWS Budgets lets you set alarms that trigger in the event of a resource exceeding your planned budget.  This tool does not only provide alerts for overutilization but also for underutilization of your resources. §

#### Why is resource tagging part of the good practices for cost management?
**With resource tagging, you can generate cost reports on specific parts of your architecture (a system for example).**

With resource tagging, you can precisely identify resources that are part of a system of your architecture. For example, you might want to identify different resources used for a recommendation engine and resources used to host a web application. This way, you will be able to precisely track the cost of either your web app or your recommendation engine. 

Resource tagging does not help you to visualize if your resources are right-sized or not and the same tag can be added to different product. For example, you can configure an Amazon Relational Database Service (Amazon RDS) database and an Amazon Elastic Compute Cloud (Amazon EC2) instance with the tag "webapp" to help you track that system in the costs reports.

### Summary
#### What is AWS Billing Console
With AWS Billing and Cost Management, you can pay your AWS bill, monitor your usage, and analyze and control your costs. The Billing and Cost Management service provides features that you can use to do the following: 
* Estimate and plan your AWS costs.
* Receive alerts if your costs exceed a threshold that you set.
* Assess your biggest investments in AWS resources.
* Simplify your accounting if you work with multiple accounts.

#### What is AWS Budget
With AWS Budgets, you can set custom budgets to track your costs and usage and respond quickly to alerts received from email or Amazon Simple Notification Service (Amazon SNS) notifications when you exceed, or when you are forecasted to exceed, your thresholds. Another key feature of Budgets is that it also alerts on projected underutilization of usage of Reserved Instanecs (RIs) and Savings Plans.

#### What is resource tagging
You can assign metadata to your AWS resources in the form of tags. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. You can create tags to categorize resources by purpose, owner, environment, or other criteria.

### Additional Resources
#### [Resource tagging](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)

#### [AWS Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html)

#### [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/?nc1=h_ls)

## Optimizing Cloud Costs
### Pre-assessment
#### Which of the following options does AWS Compute Optimizer provide recommendations to rightsize? 
**Amazon EC2 instances.**

Compute Optimizer provides recommendations for four different products: Amazon EC2, AWS Fargate, AWS Lambda, and Amazon Elastic Block Store (Amazon EBS).

#### Which of these statements is true about the Amazon EC2 pricing model? 
**Compute Savings Plans are flexible across any instance family.**

Compute Saving Plans are flexible across any instance family,  in contrast to EC2 Instance Saving Plans.

Compute Saving Plans provides discounts of up to 66 percent.

Savings Plans apply to usage after the Amazon EC2 Reserved Instances (RIs) are applied.

### AWS Pricing Models
### AWS Free Tier
#### Always free
These free-tier offers do not expire and are available to all AWS customers.

#### 12 months free
Enjoy these offers for 12 months following your initial sign-up date to AWS.

#### Trials
These short-term free trial offers start from the date you activate a particular service.

* Exceeding free tier limits can result in charges. When you exceed the free tier or a free trial ends, standard rates apply.
* Not all features are included in the AWS Free Tier offerings.
* AWS Free Tier offerings might provision or use other services that are not free.

### Basic pricing concepts
AWS offers a range of cloud computing services with pay-as-you-go pricing.

**Pay for what you use.** For each service, you pay for exactly the number of resources you actually use without requiring long-term contracts or complex licensing. 

**Pay less when you reserve.** Some services offer reservation options that provide a significant discount compared to On-Demand pricing. For more information, [Amazon EC2 Reserved Instances and Other Reservation Models.](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/introduction.html)

**Pay less with volume-based discounts when you use more.** Some services offer tiered pricing, so the per-unit cost is incrementally lower with increased usage.

**Pay even less as AWS grows.** AWS passes savings back to you in the form of lower pricing. AWS does this by working to reduce data center hardware costs, improving operational efficiencies, lowering power consumption, and generally lowering the cost of doing business. These optimizations and growing economies of scale have resulted in AWS lowering pricing over 70 times since 2006. For more information, see [AWS Pricing.](https://aws.amazon.com/pricing/)

When architecting for cost, make sure to consider the AWS Regions where your services are located. AWS service prices and data transfer costs vary by Region because of the costs associated with doing business in those different Regions.

**Not all services are available in all Regions.**

### Volume discount
#### TIERED PRICING MODELS
Considerations for tiered pricing models include the following:
* Some services include automatic volume-based discounts, such as Amazon Simple Storage Service (Amazon S3), and Reserved Instances.
* The more you use, the greater the discount.
* With AWS Organizations, you can consolidate billing for multiple accounts. Tiered pricing is applied based on usage across accounts.

#### AMAZON S3
Amazon S3 offers different pricing tiers:

S3 Standard as follows:
* First 50 TB per month
* Next 450 TB per month
* Over 500 TB per month

S3 Intelligent-Tiering as follows:
* Frequent Access tier, first 50 TB per month    
* Frequent Access tier, next 450 TB per month
* Frequent Access tier, over 500 TB per month
* Infrequent Access tier, all storage per month
* Monitoring and automation, all storage per month

Pricing varies depending on the Region.

**Note:** S3 Intelligent-Tiering has a minimum eligible object size of 128 KB for auto-tiering. Smaller objects can be stored but will always be charged at the Frequent Access tier rates.

#### DATA TRANSFER
Data transferred out of AWS services to the internet is tiered for the following services:
* Amazon S3
* Amazon Elastic Compute Cloud (Amazon EC2)
* Amazon Simple Queue Service (Amazon SQS)
* Amazon Relational Database Service (Amazon RDS)
* Amazon Virtual Private Cloud (Amazon VPC)
* CloudFront

For instance, price per gigabyte transferred out to the internet is reduced after the following:
* 10 TB per month   
* Next 40 TB per month
* Next 100 TB per month
* Over 150 TB per month

### AWS pricing models
#### On-demand pricing
Most AWS services are available on demand. With Amazon EC2 On-Demand Instances, you can pay for compute capacity by the second or hour with no long-term commitments. On-Demand Instances are ideal for short-term, irregular workloads that cannot be interrupted. You can also choose on-demand pricing initially to determine your needs based on usage.

On-demand pricing provides the following benefits:
* It's flexible. You can use it any time.
* There are no long-term commitments.
* You pay only for what you consume.
* It is priced at a premium compared to other options.

#### Spot pricing
Amazon EC2 Spot Instances are unused EC2 instance capacity in the AWS Cloud. Prices fluctuate with demand and can provide up to a 90-percent discount compared to the On-Demand Instance price. Spot Instances are ideal for fault-tolerant, instance-flexible, or time-insensitive workloads.

Spot pricing provides the following benefits:
* It offers the deepest discount for EC2 instances and AWS Fargate.
* It provides variable price and availability.

#### Commitment-based pricing
Some AWS services offer commitment-based consumption models that provide a significant discount compared to on-demand pricing. For this purchase option, you commit to a specified amount of usage over a 1-year or 3-year period. You have the option to pay nothing up front, partial up front, or all up front. The more you pay up front, the greater the discount. The commitment-based consumption model is ideal for steady-state applications or predictable usage.

#### Reserved Instances pricing
The Reserved Instances (RIs) pricing model can provide significant discounts for several AWS services compared to on-demand pricing. AWS services that offer a reservation pricing model include the following:
* Amazon EC2
* Amazon RDS
* DynamoDB
* Amazon Redshift
* Amazon ElastiCache Reserved Cache Nodes 
* Amazon OpenSearch Service 
* AWS Elemental MediaConvert (reserved transcode slots and reserved queues)

### Savings Plans
Savings Plans provide significant savings, similar to Amazon EC2 Reserved Instances, in exchange for a monetary commitment of 1 year or 3 years.

#### Compute Savings Plans
They offer the greatest flexibility, up to a 66 percent discount, and apply to Fargate and Lambda usage.

Compute Savings Plans are flexible across the following:
* Instance family, such as a move from a C5 to an M5 instance
* Region, such as a change from Europe (Ireland) to Europe (London)
* Operating system (OS)
* Tenancy 
* Compute options, such as a move from Amazon EC2 to Fargate

#### EC2 Instance Savings Plans
They provide the lowest prices and up to a 72-percent discount on the selected instance family in a specific Region.

EC2 Instance Savings Plans are flexible across the following:
* Size, such as a move from an m5.xlarge instance size to m5.4xlarge
* OS, such as a change from m5.xlarge Windows to m5.xlarge Linux
* Tenancy, such as modifying m5.xlarge Dedicated Instance tenancy to m5.xlarge default tenancy

### How Savings Plans are applied
In a Consolidated Billing Group, Savings Plans are applied to the owner account and then all other accounts combined. Amazon EC2 Reserved Instances are applied first, then EC2 Instance Savings Plans, and then Compute Savings Plans.

Consolidated Billing Group (Owner account -> All other accounts combined]

Amazon EC2 Reserved Instances -> EC2 Instance Savings Plans -> Compute Savings Plans

Savings Plans apply to your usage after the Amazon EC2 Reserved Instances (RI) are applied.

Your current Savings Plans are grouped together and applied to the eligible usage. EC2 Instance Savings Plans are applied before Compute Savings Plans because Compute Savings Plans have broader applicability.

In a consolidated billing family, Savings Plans are applied first to the owner account's usage and then to other accounts' usage. This occurs only if you have sharing enabled.

Your Savings Plans are applied to your highest savings percentage first. If there are multiple usages with equal savings percentages, Savings Plans are applied to the first usage with the lowest Savings Plans rate. Savings Plans continue to apply until there are no more remaining usages or your commitment is exhausted. Any remaining usage is charged at the On-Demand Instance rates.

### Rightsizing Compute Resources
Before rightsizing its important to understand the meaning of instance names and instance families. According to your application needs, the naming conventions will help you to choose the most appropriate instance.

### Amazon EC2 naming
c5n.xlarge

* **c** - Instance family
* **5** - Instance generation
* **n** - Attribute
* **xlarge** - Instance size

### Amazon EC2 instance families
Pick the optimal instance family for the type of workload you plan to deploy. Doing this from the start saves time and cost, and reduces the need to resize later.

**Some instance types are only available in certain Regions.**

#### General purpose
Use cases for general purpose EC2 instances include the following:
* Workloads requiring a balance of compute, memory, and networking
* Diverse workloads
* Web applications

#### Compute optimized
Use cases for compute optimized EC2 instances include the following:
* Compute-bound applications
* High performance processors
* Media transcoding
* Scientific modeling
* Machine learning

#### Memory optimized
Use cases for memory optimized EC2 instances include the following:
* Fast delivery of large datasets in memory
* Database servers
* Web caches
* Data analytics

#### Accelerated computing
Use cases for accelerated computing EC2 instances include the following:
* High-graphics processing
* Graphics processing unit (GPU) bound
* Machine learning
* High-performance computing
* Autonomous vehicles

#### Storage optimized
Use cases for storage optimized EC2 instances include the following:
* High sequential read/write
* Large datasets
* NoSQL databases
* Elasticsearch

### Upgrade to the latest generation
Upgrading to the latest generation instances can yield the following cost benefits:
* Newer generations have a lower price per hour to operate compared to older generations.
* Newer generations provide better performance, which can result in using fewer instances.

Choosing the right resource from the beginning requires minimal effort. Upgrading later requires operational overhead and analysis that might not be financially feasible.

### Instance sizing
Instance types are available in different sizes. Each size has different number of resources allocated, such as CPU, memory, and network bandwidth. Benchmark your application and select the right size to balance performance and cost.

When using an Amazon EC2 Auto Scaling group, smaller instances make it possible for your capacity to better match demand.

### Rightsizing recommendations
AWS Compute Optimizer and AWS Cost Explorer provide optimal EC2 instance recommendations for your workloads. Both tools use the same machine learning engine to analyze historical use metrics.

#### AWS Compute Optimizer
Compute optimizer provides recommendations from a performance perspective.

It recommends changes that might result in a cost increase.

#### AWS Cost Explorer
Cost Explorer provides recommendations from a cost savings perspective.

It only recommends changes that will yield estimated cost savings greater than or equal to $0.

### AWS Compute Optimizer
Based on your usage data, Compute Optimizer helps avoid overprovisioning and under provisioning the following four types of AWS resources:
* EC2 instance types
* Amazon Elastic Block Store (Amazon EBS) volumes
* Amazon Elastic Container Service (Amazon ECS) services on AWS Fargate
* AWS Lambda functions

This process takes place in the cost optimization cycle. You need to continually refine your resources and optimize cost and performance according to your needs as they evolve.

### Use cases
#### Evaluate rightsizing recommendations
Evaluate estimated savings and performance improvement opportunities at the account level for Amazon EC2, Amazon ECS, Amazon EBS, and Lambda resources. 

#### Configure enhanced infrastructure metrics
Get improved recommendations for optimizing EC2 instances and Auto Scaling groups by using 3 months of historical data.

#### Streamline migration to AWS Graviton CPUs
Find the Amazon EC2 workloads that will deliver the biggest return for the smallest migration effort in a shift to AWS Graviton CPUs.

#### Configure external metrics
Increase savings and performance awareness by configuring third-party metrics from your application performance monitoring (APM) tools.§

### Using AWS Credits
AWS credits are automatically applied to bills to help cover costs associated with eligible services. You can visualize your available credits in the Credits section of AWS Billing and Cost Management.

### Selecting credits to apply
If an AWS account has more than one credit, the available credits apply in the following order:
1. The credits that expire soonest
2. The credits with the least number of eligible services
3. The oldest credits

For example, John Doe has two credits available to him. Credit one is for $10. It expires in January 2024, and it can be used for either Amazon S3 or Amazon EC2. Credit two is for $5. It expires in December 2024, and it can be used only for Amazon EC2. John has sufficient AWS charges to apply all credits. AWS selects credit one for application first because it expires sooner than credit two.

**If you have remaining, eligible usage after a credit is consumed, the process will repeat until your credits are consumed or your usage is covered.

Credits are applied to the largest services charge (for example, Amazon EC2 or Amazon S3). Consumption will continue in a descending pattern for the remainder of the service charges.

Credits don't require customer selection to apply during the billing process. AWS will automatically apply eligible credits to applicable services.***

### Selecting where to apply credits
When credit sharing is activated, credits are applied in AWS Organizations in the following order:
1. The account that owns the credit is covered for the service charges.
2. Credits are applied toward the AWS account with the highest spend.
3. Credits are applied to the service with the highest spend in that account.
4. Credits are applied to the Stock-Keeping Unit (SKU) with the highest spend in that service.

The process repeats until the credit is consumed or all customer spend is covered.

AWS applies the credit to the largest available charge across all eligible sellers of record. This means that AWS tries to apply your credits before they expire, so AWS might use a generic credit for a specific service.

**Credits can be applied across single or multiple AWS accounts. It is also possible for an organization to stop sharing credits.**

### AWS Activate
Imagine you have an idea, and you want to launch a startup. You can build it with AWS Activate. As an AWS Activate member, you get free tools, resources, content, and expert support to accelerate your startup at every stage. Benefits include the following:
* More than 40 solution templates to build and deploy your product
* AWS expert curated tips for your business and technical needs
* Best-practices training

Startups can apply for up to $100,000 in AWS Activate credits. 

### AWS Activate Console
The AWS Activate Console is a personalized hub of tools, resources, and content tailored to startups’ needs. It is designed to support startups through every stage of their journey, from ideating to building, and beyond. AWS Activate Console is a one-stop-shop that delivers the tailored solutions needed to quickly get started on AWS and grow a business.

In the AWS Activate Console, startups can get answers to technical problems and learn best practices. By matching AWS content with an AWS Activate profile's interests and AWS usage, the AWS Activate Console provides personalized content recommendations on a range of topics. After a startup has applied for and received AWS Activate credits, the AWS Activate Console makes it easy to do the following:
* Track and monitor the AWS Activate credits and costs.
* Deploy proven architectures, even with no previous infrastructure experience.
* Take advantage of exclusive offers.
* Get real-time updates about the health of your AWS environment.

### AWS Activate credits
Based on their stage, startups are eligible for different credit packages. They can select the package tier that best matches their profile. 

#### FOUNDERS REQUIREMENTS
Requirements for AWS Activate Founders include the following:
* Must be new to AWS Activate Founders
* Must not have previously received credits from an AWS Activate Portfolio partner
* Must have an AWS Activate account
* Must be an early-stage startup that is unfunded or funded up to and including Series A
* Must not have institutional funding or affiliation with an AWS Activate Provider
* Must have a company website or public company profile
* Must have been founded in the past 10 years

#### FOUNDERS BENEFITS
AWS Activate Founder benefits include the following:
* $1,000 in AWS Activate credits, which are valid for 2 years 
* $350 in AWS Support Developer Support credits, which are valid for 1 year 
* 7 core AWS Trusted Advisor best practice checks 
* Email access to one primary cloud support associate and general architectural guidance

#### PORTFOLIO REQUIREMENTS
Requirements for AWS Activate Portfolio include the following:
* Must be affiliated with an AWS Activate Provider that is unfunded or funded up to and including Series A
* Must have an AWS Activate Provider organization ID (Org ID)
* Must have a fully functioning company website
* Must have an AWS Activate account
* Must not have previously received AWS Activate credits at equal or greater value from the same AWS Activate Provider
* Must not have exceeded $100,000 in redeemed AWS Activate credits
* Must have been founded in the past 10 years

#### PORTFOLIO BENEFITS
AWS Activate Portfolio benefits include the following:
* Up to $100,000 in AWS Activate credits that are valid for 1 year
* AWS Support Business Support credits that are valid for 1 year
* 24x7 phone, email, and chat access to cloud support engineers and premium response speed
* AWS Support API, interoperability, and configuration guidance and troubleshooting

### Knowledge Check
#### Why did AnyCompany choose to use a lift-and-shift approach when moving to the AWS Cloud?
It is the most straightforward approach because AnyCompany can follow an existing on-premises architecture.

**Lifting and shifting** an architecture might not be the quickest approach, but it is straightforward because you can reproduce your on-premises architecture. However, it is not cost-optimized and you might not need all these resources all the time. With the AWS Cloud, your infrastructure will become agile, and you can scale up or down your resources based on demand, which is not possible using on-premises resources.

#### Which tool can help AnyCompany optimize its cloud costs based on resource usage?
**AWS Compute Optimizer.**

With Compute Optimizer, you can avoid overprovisioning your resources. In the case of a lift and shift from an on-premises architecture, your architecture must handle traffic peak, so it might be overprovisioned for the usual demand. 

Trusted Advisor is a serverless compute product. It will not help you optimize costs.

With CloudWatch, you can program metrics that you need to monitor. Although it might help you visualize your traffic, it will not provide recommendations for downsizing your compute resources. 

AWS Pricing Calculator is a simulation tools that helps you visualize the costs of your architecture before you build it. This won't help you here.

#### What is the most cost-effective way for AnyCompany to provision its compute resources?
**Using two Reserved Instances (RIs) for regular traffic and three additional On-Demand Instances for peak traffic.**

Indeed, Spot Instances can give discounts of up to 90 percent compared to On-Demand Instances. However, Spot Instances can be terminated by AWS when being requested. 

In this situation, because we have no information about the fault-tolerance of the infrastructure, we should choose On-Demand Instances for scaling. Because peak traffic does not appear every day, using Reserved Instances for this purpose doesn't work.

### Summary
#### AWS basic pricing concepts
AWS offers a range of cloud computing services with pay-as-you-go pricing.

**Pay for what you use.** For each service, you pay for exactly the number of resources you actually use without requiring long-term contracts or complex licensing. 

**Pay less when you reserve.** Some services offer reservation options that provide a significant discount compared to On-Demand pricing. For more information, [Amazon EC2 Reserved Instances and Other Reservation Models.](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/introduction.html)

**Pay less with volume-based discounts when you use more.** Some services offer tiered pricing, so the per-unit cost is incrementally lower with increased usage.

**Pay even less as AWS grows.** AWS passes savings back to you in the form of lower pricing. AWS does this by working to reduce data center hardware costs, improving operational efficiencies, lowering power consumption, and generally lowering the cost of doing business. These optimizations and growing economies of scale have resulted in AWS lowering pricing over 70 times since 2006. For more information, see [AWS Pricing.](https://aws.amazon.com/pricing/)

#### Which products offer right-sizing recommendations
**AWS Compute Optimizer** and **AWS Cost Explorer** provide optimal EC2 instance recommendations for your workloads. Both tools use the same machine learning engine to analyze historical use metrics.

#### AWS credits
AWS credits are automatically applied to bills to help cover costs associated with eligible services.

### Additional Resources
#### [AWS Credits](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilling-credits.html)
#### [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/?nc1=h_ls)
#### [AWS pricing models](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/pricing-models.html)
#### [Right-sizing AWS resources](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/)

## Cloud Cost Management: AWS Organizations
### Pre-assessment
#### Which of these statements is true regarding AWS Organizations?
**The management account can be inside of an organization unit (OU).**

The other items are incorrect because: 
* there can only be one management account
* member accounts cannot be located in the root
* the payer account is the same as the management account.

### AWS Organizations
AWS Organizations enables customers to manage a multi-account structure within AWS. This is great for viewing the billing associated with our different accounts and also for centrally managing security and controls for our account structure.

You do this by building a hierarchical grouping of accounts inside of Organizations. There are several key components to consider when creating Organizations. 

#### Management account
This is also the **payer account**. This is the account that will be creating the Organization and its structure.

#### Organization
The Organization itself is created by the management account. This entity holds your consolidated AWS accounts, so that you can administer them as a single unit. 

##### Root
The root is a parent container for all of the accounts inside of your Organization.

Organizations automatically creates it for you when you create an organization. 

##### Organizational units (OUs)
Organizational units are containers for the accounts inside of our organization. This allows us to group accounts together that will have similar controls applied to them.

#### Member accounts
Member accounts are standard AWS accounts that are deployed inside of the organization's structure that we have established. 

One of the benefits of using Organizations is that we have the ability to apply policies to groups of accounts based on our organization's structure.

While we do have the ability to apply policies to individual accounts, that would require maintenance of those policies for different individual accounts, resulting in multiple policies that have to be maintained to essentially achieve the same end result. 

We do have the ability to apply policies to individual accounts. In this case, policy one would only impact a single account.

We also have the ability to apply a policy to an OU. In this case, policy two will impact all of the accounts inside of OU1. If you apply a policy to an OU that has branch OUs, this policy applies to all the accounts in that sub-tree, meaning that OU, as well as the accounts in the branched OUs. So here policy three would impact the four accounts that make up OU2 and OU3. Here, we have applied policy four to just the three accounts that make up OU3. Finally, we have the ability to apply policies at the root level as well. This means that this policy will affect all of the accounts inside of our organization structure. 

At the beginning of this module, we mentioned that Example Corp is doing well with their AWS deployment, so well that they've now created three different accounts that are supporting different workloads.

Inline with best practices, Example Corp wants to deploy an organization structure. In order to do this, they create a fourth account. Here, it's labeled Account D. That will be the management payer account. Also, the account that's responsible for creating and defining the organization's structure. Now that we've established Organizations for Example Corp, our individual accounts will not be receiving an invoice. Instead, we'll get a consolidated bill that gets sent to the paying account. That paying account will be able to view a breakdown of spend associated with each account, but also the total spend for AWS. It's important to note in this diagram that the paying account does have some charges associated with it.

From a best-practices perspective, we don't want to deploy and operate resources inside of that payer account. However, there are some components that will likely be deployed in order to support things, like consolidated logging and auditing, and therefore there will be some small charges associated with the operations of that account. 

#### Benefits of using AWS Organizations
* Consolidated billing.
* We get to look at aggregate usage across the individual accounts in our organization in order to calculate the benefits associated with volume discounts for some products and services.
* Where we have credits that are applied those are shared across the organization, and reserved instances can be leveraged by other accounts inside of our organizational structure, hopefully leading to better utilization rates of those RIs.

### Components of AWS Organizations
#### Management account and payer account
The account that creates the organization. This is the account that manages the organization, adds organizational units (OUs) and accounts, pays charges accrued by the accounts, and applies policies to the entities. It is best practice to use your management account only for handling organizations, policies, and billing. You should not use it to create infrastructure. 

NOTE: The account you use to create the organization is the management account; you can't change an organization's management account after it is created.

#### Organization
Created by the management account, this entity holds your consolidated AWS accounts so that you can administer them as a single unit. From the management account, you can centrally view and manage all of your accounts within your organization. You can organize the accounts in a hierarchical, tree-like structure with a root at the top and OUs nested under the root. 

#### Root
Root created at the start of an organization by the management account.

The root is a parent container for all of the accounts for your organization. AWS Organizations automatically creates it for you when you create an organization. 

Note: This organizational root is the top of your hierarchical tree in AWS Organizations; it has nothing to do with AWS root account users. Because the root is the top of the tree, if you apply a policy to the root, it applies to all OUs and accounts in the organization.

#### OU
This is a container for accounts within the organization. An OU can contain other OUs, so you can create a hierarchy that resembles an upside-down tree, with a root at the top and branches of OUs that reach down, ending in accounts that are the leaves of the tree. When you attach a policy to one of the nodes in the hierarchy, it flows down and affects all of the branches (OUs) and leaves (accounts) beneath it. An OU can have exactly one parent, and currently each account can be a member of exactly one OU.

#### Member account
This is a standard AWS account (that is not the management or paying account) that contains your AWS resources. You can attach a policy to an account to apply controls to only that account. An account can be a member of only one organization at a time. Each account can be directly in the root or placed in one of the OUs in the hierarchy.

### Consolidated billing
Now that you have an organization set up, you will use consolidated billing. This means that instead of each account receiving and paying its own bill, the management (or paying) account receives  and pays a single bill for all the member accounts in the organization. The bill includes a breakdown of all the spending for each account.

In our example, this means that all billing goes to the management or paying account D with a summary of the spending per linked account: A, B, C.

**The solution is designed to be a production-ready reference implementation that you can use as a starting point for deploying an AWS environment to run your scale-out workloads. For additional details, go to [Architecture overview.](https://docs.aws.amazon.com/solutions/latest/scale-out-computing-on-aws/overview.html)**

### Volume discounts, credits, and RIs
You can save money with AWS Organizations by doing the following:
* Get volume discount rates based on total usage from all accounts in your organization. For example, if you use Amazon S3 storage across all of your accounts, you can receive a volume discount for your total usage instead of based on usage of individual accounts.
* Share credits across all accounts in the organization.
* Share Reserved Instances (RIs) and savings plans across the organization. You can receive the hourly cost benefit of Reserved Instances that are purchased by one account with any other account in the organization. For example, if one account has five RIs, but it only uses three, another account in the organization can use the last two. Note: To share the RI discount, the attributes of the instance you launch must match exactly to the attributes of the RI that the original account purchased.

### Knowledge Check
#### Which of these statements is true regarding AWS Organizations? (Select TWO.)
**An OU can contain several OUs, and an OU can contain the payer account.** 

The root is above all your OUs, it is created within the organization level. 

An OU cannot contain several organizations, but an organization can contain several OUs.

### Summary
#### What is AWS Organizations
AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.

#### What is consolidated billing
Consolidated billing means instead of each account receiving and paying its own bill, the management (or paying) account receives and pays a single bill for all the member accounts in the organization. The bill includes a breakdown of the spending for each account.

### Additional Resources
#### [AWS Organizations](https://aws.amazon.com/organizations/?nc1=h_ls)

## Cloud Cost Management: AWS Support plans
### Pre-assessment
#### Which support plan gives access to a designated Technical Account Manager to provide proactive guidance and coordinate access to programs and AWS experts
**Enterprise.** The Enterprise plan gives you access to a dedicated TAM.

### AWS Support Plans Overview
Every customer automatically gets AWS Basic support, no cost at all. Any customer can access support functions like 24/7 access to customer service, documentation, whitepapers, support forums, AWS Trusted Advisor, and the AWS Personal Health Dashboard. It's a personalized view of the health of AWS services and any alerts when your resources might be impacted. These functions are free for everyone, but as you begin to move mission-critical workloads into AWS, we offer higher levels of support to match your levels of need. 

The next tier is our Developer tier, which includes everything in the Basic support level. Plus, you can now email customer support directly with a 24-hour response time on any questions you have. And responses of less than 12 hours in case your systems are impaired. This is a great tier for businesses that are experimenting with AWS or setting up tests or proofs of concept. 

Now, as you begin to take production workloads live, we find customers are more successful advancing to the Business tier. Everything in the previous tiers, plus Trusted Advisor now opens up the entire suite of checks for your account. You are given direct phone access to our support team that has a four-hour response SLA. If your production system is impaired, and a one-hour SLA for production systems down. Additionally, as part of the Business tier, we provide access to infrastructure event management, where for an extra fee, we can help you plan for massive events like brand-new launches or global advertising blitzes. 

Finally, for companies running mission-critical workloads, we recommend the Enterprise level support. It has everything in the previous tiers. Plus a 15-minute SLA for business-critical workloads, a dedicated technical account manager, or TAM. They will coordinate access to programs and other AWS experts as needed. 

Let's talk a bit more specifically about the job of a TAM. TAMs are part of the concierge support team that comes with Enterprise level support. They specialize not only in proactively monitoring your environment and assisting with optimizations, but provide infrastructure event management, Well-Architected reviews, and operations reviews. 

What's a Well-Architected review, you ask? Well, keeping it simple, TAMs work with customers to review architectures using the Well-Architected Framework. Architectures are checked against the five pillars of the Well-Architected Framework: Operational Excellence, Security, Reliability, Performance Efficiency, and Cost Optimization. As you can see, the job of a TAM is much more than just handling trouble tickets. AWS Support looks at the customer holistically, not just if they have problems, but how can we help them be successful? 

And that's the mission of AWS Support. To learn more about AWS Support, including pricing structures for the plans, go to [aws.amazon.com/premiumsupport](https://aws.amazon.com/premiumsupport).

### AWS Support
AWS offers four different Support plans(opens in a new tab) to help you troubleshoot issues, lower costs, and efficiently use AWS services. You can choose from the following Support plans to meet your company’s needs: 
* Basic
* Developer
* Business
* Enterprise On-Ramp
* Enterprise

#### Basic Support
Basic Support is free for all AWS customers. It includes access to whitepapers, documentation, and support communities. You can also contact AWS for billing questions and service limit increases.

With Basic Support, you have access to a limited selection of AWS Trusted Advisor checks. Additionally, you can use the AWS Health Dashboard, a tool that provides alerts and remediation guidance when AWS is experiencing events that may affect you. 

#### Developer, Business, Enterprise On-Ramp, and Enterprise Support
The Developer, Business, Enterprise On-Ramp, and Enterprise Support plans include all the benefits of Basic Support, in addition to the ability to open an unrestricted number of technical support cases. These Support plans have pay-by-the-month pricing and require no long-term contracts.

The information in this course highlights only a selection of details for each Support plan. A complete overview of what is included in each Support plan, including pricing for each plan, is available on the [AWS Support](https://aws.amazon.com/premiumsupport/plans/) site.

In general, for pricing, the Developer plan has the lowest cost, the Business and Enterprise On-Ramp plans are in the middle, and the Enterprise plan has the highest cost.

#### Developer Support
Customers with the Developer Support plan have access to the following features:
* Best practice guidance
* Client-side diagnostic tools
* Building-block architecture support, which consists of guidance for how to use AWS offerings, features, and services together

For example, suppose that your company is exploring AWS services. You’ve heard about a few different AWS services. However, you’re unsure of how to use them together to build applications that can address your company’s needs. In this scenario, the building-block architecture support that is included with the Developer Support plan could help you to identify opportunities for combining specific services and features.

#### Business Support
Customers with a Business Support plan have access to additional features, including the following: 
* Use-case guidance to identify AWS offerings, features, and services that can best support your specific needs
* All Trusted Advisor checks
* Limited support for third-party software, such as common operating systems and application stack components

Suppose that your company has the Business Support plan, and you want to install a common third-party operating system onto your Amazon Elastic Compute Cloud (Amazon EC2) instances. You could contact AWS Support for assistance with installing, configuring, and troubleshooting the operating system. For advanced topics, such as optimizing performance, using custom scripts, or resolving security issues, you may need to contact the third-party software provider directly.

#### Enterprise On-Ramp Support
In November 2021, AWS opened enrollment into the AWS Enterprise On-Ramp Support plan. In addition to all the features included in the Basic, Developer, and Business Support plans, customers with the Enterprise On-Ramp Support plan have access to the following:
* A pool of Technical Account Managers to provide proactive guidance and coordinate access to programs and AWS experts
* A Cost Optimization workshop (one per year)
* A Concierge support team for billing and account assistance
* Tools to monitor costs and performance through Trusted Advisor and the Health API and Dashboard

The Enterprise On-Ramp Support plan also provides access to a specific set of proactive support services, which are provided by a pool of Technical Account Managers:
* Consultant review and architecture guidance (once per year)
* Infrastructure Event Management support (once per year)
* Support automation workflows
* **Thirty minutes** or less response time for business-critical issues

#### Enterprise Support
In addition to all features included in the Basic, Developer, Business, and Enterprise On-Ramp support plans, customers with Enterprise Support have access to the following:
* Designated Technical Account Manager to provide proactive guidance and coordinate access to programs and AWS experts
* Concierge support team for billing and account assistance
* Operations reviews and tools to monitor health
* Training and game days to drive innovation
* Tools to monitor costs and performance through Trusted Advisor and the Health API and Dashboard

The Enterprise plan also provides full access to proactive services, which are provided by a designated Technical Account Manager:
* Consultative review and architecture guidance
* Infrastructure Event Management support
* Cost Optimization Workshop and tools
* Support automation workflows
* **Fifteen minutes** or less response time for business-critical issues

### Technical Account Manager (TAM)
The Enterprise On-Ramp and Enterprise Support plans include access to a Technical Account Manager (TAM).

The TAM is your primary point of contact at AWS. If your company subscribes to Enterprise Support or Enterprise On-Ramp, your TAM will guide, empower, and evolve your cloud journey across the full range of AWS services. TAMs provide expert engineering guidance, help you design solutions that efficiently integrate AWS services, assist with cost-effective and resilient architectures, and provide direct access to AWS programs and a broad community of experts.

For example, suppose that you are interested in developing an application that uses several AWS services together. Your TAM could provide insights into how to best use the services together in a way that aligns with the specific needs that your company is hoping to address through the new application.

### Knowledge Check
#### Which Support plan includes all AWS Trusted Advisor checks at the lowest cost?
**Business.**

Only the Business, Enterprise On-Ramp, and Enterprise Support plans include all AWS Trusted Advisor checks. Of these three Support plans, the Business Support plan has a lower cost.

Learn more at the following link:
* [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/)

### Summary
AWS offers four different [Support plans](https://aws.amazon.com/premiumsupport/plans/) to help you troubleshoot issues, lower costs, and efficiently use AWS services. 

You can choose from the following Support plans to meet your company’s needs: 
* Basic
* Developer
* Business
* Enterprise On-Ramp
* Enterprise

### Additional Resources
#### [AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/)

## Module Summary
### Define business needs
Identify the needs of an organization to choose the right deployment for an infrastructure.

### Establish cloud strategy
* Apply cloud financial management principles. 
* Use AWS Pricing Calculator to simulate the cost of an infrastructure
* Plan for data transfer charges.

### Cloud cost analysis and tracking
* Use the AWS Billing and Cost Management consoles.
* Use AWS Purchase Order Management.
* Use resource tagging for cost optimization.
* Use AWS Cost Explorer.

### Optimize cloud costs
* Right-size AWS resources.
* Use AWS Credits.
* Choose the appropriate pricing models for your needs.
* Use AWS Compute Optimizer.

### AWS Organizations
Centrally manage your AWS resources using AWS Organizations

### AWS Support Plans
AWS offers four different Support plans (Basic, Developer, Business, Enterprise) to help you troubleshoot issues, lower costs, and efficiently use AWS services.

## Assessment
### Which statement best describes data transfer between Regions?
**Data transferred in does not vary per Region, as the transfer in cost is always 0.**

The other options are incorrect because:
* Data transferred out to the internet starts at 9 cents/GB.
* Data transfer between Regions does not require VPC endpoints at the destination.
* Data transfer between Regions is not prived per LCU-hour.

### Which of the following are components of the Cloud Financial Management pillars? (Select TWO).
* **Planning and forecasting**
* **Cost optimization**

The other options are incorrect because:
* Business agility is not a component of the Cloud Financial Management pillars.
* Right-sizing resources is a part of good practices for financial management, but it is not a component of the Cloud Financial Management pillars.
* Smart purchasing is not a component of the Cloud Financial Management pillars.

### Which statement is true regarding the concept of CAPEX, OPEX and TCO?
** TCO corresponds to CAPEX + OPEX.**

The other options are incorrect because:
* TCP stands for Total Cost of Ownership. This corresponds to the sum of capital expenditures (CAPEX) and operational expenditures (OPEX).

### Which of the following has a charge associated with data transfer in?
***Data transferres between AWS services in the same Availability Zone using a public IPv4 address.**

The other options are incorrect because:
* AWS Snowball Edge, Amazon EC2, and AWS Direct Connect are not charged for data transferred in.

### Which of the following statements is true regarding cloud computing?

**Cloud computing allows you to increase speed and agility.**

The other options are incorrect because:
* Cloud computing allows you to trade upfront expense for variable expense.
* Cloud computing allows you to stop guessing the capacity you need.
* Cloud computing allows you to avoid running and maintaining data centers.

### Which tool allows you to visualize the costs of your infrastructure before building it with AWS?
**AWS Pricing Calculator.**

The other options are incorrect because:
* AWS Trusted Advisor helps you optimize your infrastructure in terms of security and good practices.
* AWS Budgets helps you set alarms and budgets per service.
* AWS Compute Optimizer helps you get recommendations to optimize your compute resources according to your usage.

### Which component of the Cloud Financial Management pillars focuses on operational, people-related, and technological enablers of continuous cloud financial management?
**Cloud financial operations.** To enable a successful financial management and business strategy, you need to ensure that people, process, automation, and governance are considered.

The other options are incorrect because:
* Measurement and accountability do not focus on people involved in running the financial operations tasks.
* Planning and forecasting do not focus on people involved in running the financial operations tasks.
* Cost optimization does not focus on people involved in running the financial operations tasks.

### Which of the following statements are true about cost allocation tags? (Select TWO.)
**Accounts are limited to 500 tags** and **Cost allocation tag keys are case sensitive**.

The other options are incorrect because:
* AWS generated tags are not activated by default.
* User-defined cost allocation tags are not retroactive.
* AWS generated cost allocation tags cannot be changed by the master account.

### When are tags visible in the AWS Cost and Usage Reports?
**After you activate the AWS-generated tags in Billing and Cost Management.**

The other options are incorrect because:
* After you create the tag, it needed to be activated to be visible.
* To activate the AWS-generated tags you need to go in Billing and Cost Management, not in AWS Config.
* Creating an AWS account does not create nor activate tags.

### Which of the following statements are benefits of resource tagging? (Select TWO.)
**Control and compliance** and **Cost and usage allocations**.

The other options are incorrect because:
* There is a limit of tagging per service.
* There is no specific discount for tagged resources.
* There is no specific economy of scale for tagged resources.

### How long after you activate a tag will it take to appear on the Cost and Usage Report?
**24 hours.**

The other options are incorrect because:
* The time it takes for a tagged resource to appear in the Cost and Usage Reports is 24 hours.

### Which compute pricing model can provide the lowest resource cost?
**Spot instances.**

The other options are incorrect because:
* Despite all these procing models provide substantial discounts, spot instances will always be cheaper. The drawback of spot instances is that they can be terminated at any time by AWS if there is a high demand.

### Which of the following are requirements to get AWS Compute Optimizer recommendations?
**Compute optimizer generates recommendations only for certain instance type (such as M, C, X etc.)**

The other options are incorrect because:
* Compute Optimizer requires at least 30 consecutive hours (not days) of metric data from your resource to generate recommendations.
* Compute Optimizer does not require that CloudWatch is enabled for detailed monitoring.

###  Which of the following is true regarding AWS Budgets? (Select TWO.)
**Billing forecasts take approximately 5 weeks of historical data** abd **AWS billing data, which Budgets uses to monitor resources, is updated at least one per day**.

The other options are incorrect because:
* Usage alarms can only trigger once per billing cycle.
* Budget Alerts cannot be sent to multiple Amazon SNS topics or to up to 20 individual email addresses.

## In certain cases, a tiered orice reduction is available for data transfer out to the internet. Which of the following statements is true about the tiered pricing?
**Tiered pricing is applied automatically starting at 10 TB of data transferred out to the internet per month.**

The other options are incorrect because:
* Tiered pricing is not included with Compute Saving Plans.
* Tiered pricing does not relate to inbound data ytansfer but rather to outboud data trabsfer to the internet.
* Using three qualifying services won't help to obtain tiered price reduction.

### Which of the following is true about AWS Free Tier services?
**Free Tier offerings might provision other services that aren't free.**

The other options are incorrect because:
* Trials are not activated when you create your AWS account.
* Free Tier services are not always limited to 12 months, there are several free tier conditions, depemding on the service.
* Free Tier services do incur outbound data transfer charges.

### Which service provides right-sizing recommendations for cost savings?
**AWS Cost Explorer.**

The other options are incorrect because:
* AWS Trusted Advisor helps you optimize your infrastructure in terms of security and good practices.
* AWS Compute Optimizer helps you get recommendations to optimize your compute resources according to your usage.
* Amazon CloudWatch allows you to create metrics to track usage, but it does not provide recommendations.

### Which of the following statements is true about Compute Savings Plans?
**They apply to Fargate and Lambda usage.**

The other options are incorrect because:
* Compute Savings Plans are applied after EC2 Instance Savings Plans.
* Compute Savings Plans are more flexible than EC2 Instance Savings Plans as you can switch an instance family to another one.
* Compute Savings Plans provide up to 66% off.

### Spot instances are good choice if your architecture has which of the following characteristics? (Select TWO.)
**Can withstand interruptions** and **has the flexibility to use multiple instance types**.

The other options are incorrect because:
* Stability, predictable or spiky traffic are not ideal for using Spot Instances.

### AWS Cost Explorer provides which of the following default report types? (Select TWO.)
**AWS Cost and Usage report** and **Savings Plans report**.

The other options are incorrect because:
* Compute, Storage or Spot Instances reports do not exist. However, another option is available: Reserved Instance utilization and coverage.

### Which of the following statements are true about AWS Cost Explorer? (Select TWO.)
**Cost Explorer recommneds downsizing instances only within the same instance family** and **The Cost Explorer API is charged per paginated request**.

The other options are incorrect because:
* Cost Explorer cannot recommend downsizing instances accross different instance families.
* Cost and Usage reports do not automatically integrate with Athena and QuickSight; this needs to be manually configured.
* You do not need to create a custom report to see multiple accounts within Cost Explorer.

### Which additional services can you use with AWS Cost and Usage Reports to view, manage, monitor, or analyze data?
**Amazon QuickSight.** QuickSight is a dashboard tool that allows you to create visualizations or analyses.

The other options are incorrect because:
* None of these services will help you to view, manage, monitor, or analyze data.

### Which of the following features in AWS Organizations will help you to accomplish shared billing functionality and track resource deployment? (Select TWO.)
**Tag policy** and **Consolidated billing**.

The other options are incorrect because:
* Service control Plicy won't help you to obtain shared billing functionality neither to track resource deployment.
* Root account usage restrictions won't help you to obtain shared billing functionality neither to track resource deployment.
* Compute Optimizer detailed monitoring won't help you to obtain shared billing functionality neither to track resource deployment.

### Which account are included in the core organization unit (OU)? (Select TWO.)
**Audit member account** and **Log archive account**.

The other options are incorrect because:
* Master and paying account are not part of any OU.
* Other member accounts need to be placed in specific OUs, and not in the core OU.

### Which of these statements is true regarding AWS Organizations (OUs)?
**An OU can contain several other OUs.** Each sub OUs could also contain other OUs.

The other options are incorrect because:
* The root is above all your OUs, and is created at the Organizational level.
* An OU cannot contain several Organizations, but and Organization can contain several OUs.
* An OU can have only one management account.
