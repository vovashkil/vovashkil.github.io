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
