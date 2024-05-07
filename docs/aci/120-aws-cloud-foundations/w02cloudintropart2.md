###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Cloud Intro Part 2
## AWS Infrastructure
### Regions, Availability Zones, and Edge locations
#### REGION
An edge location is a site that Amazon CloudFront uses to store cached copies of your content closer to your customers for faster delivery. 

Edge locations are outside of the Region network, and are often in major cities. 

#### AVAILABILITY ZONE
An Availability Zone is one or more separated or isolated data centers with redundant power, ultra-low-latency networking, and connectivity. Availability Zones are located tens of miles apart from each other to protect against natural disasters.

#### EDGE LOCATION
An edge location is a site that Amazon CloudFront uses to store cached copies of your content closer to your customers for faster delivery. 

Edge locations are outside of the Region network, and are often in major cities. 

Edge locations are separate from Regions, so you can push content from inside a Region to a collection of Edge locations, in order to accelerate communication and content delivery. Edge locations run more than just CloudFront. They are also used by AWS Global Accelerator to direct traffic to the closest regional endpoints to the end-users. 

Regions and their Availability Zones work together to deliver the best performance to meet customer demands. Edge locations and their associated services can be used to further support application and content performance by caching content and finding the ideal routing for traffic.

### Using multiple Regions
Sometimes businesses may deploy their content in multiple regions. For example, with the multi-region deployment, the workloads operate primary and secondary Regions with full capacity. The main traffic flows through the primary Region, and the secondary Regions are available for recovery in case of a disaster event. This ensures that the infrastructure is resilient and highly available, offering business continuity with minimal impact on production workloads.

It's also common for businesses to deploy their applications in multiple Regions to help provide a fast and smooth experience for users globally. Here’s an example from the gaming industry: a game may include player-friendly logical game Regions that represent a collection of game-server hosting locations that are geographically grouped, such as North America, or Asia Pacific. The business might also choose to create more granular regions, such as North America East and North America West.

To reduce latency and increase geographic coverage, a combination of different game-server hosting solutions can be used to improve the player experience. 

A business may also be required to use multiple Regions due to data sovereignty. Some countries or regions, have laws that govern how their citizens' data can be treated. Europe, for example, has a regulation called the General Data Protection Regulation, or GDPR, which governs how their citizens' data can be stored and processed. To meet this regulation, businesses will store European data only within data warehouses in Europe that follow GDPR guidelines.

#### Disaster recovery and business continuity
With the multi-region deployment, the workloads operate primary and secondary Regions with full capacity. The main traffic flows through the primary Region, and the secondary Region acts as a recovery Region in case of a disaster event. 

#### Low latency for end-users
Deploying in multiple Regions is a common practice for businesses that have users all over the world, and need to access their applications and content with near-immediate response times.

#### Data sovereignty
Some countries or regions have laws that govern how their citizens' data can be treated. Europe, for example, has GDPR that governs how their citizens' data can be stored and processed. To meet this regulation, businesses will store European data only within data warehouses in Europe that follow GDPR guidelines. 

### Using multiple Availability Zones
When a company uses multiple Availability Zones, its content can be stored across those Availability Zones. This strategy makes the content highly available and less prone to natural and man-made disasters. A business's content or application is highly available when it has no single point of failure, and it can operate without failure for a specific period of time.

### Benefits of edge locations
1. Security
AWS Shield Standard protects your website and its traffic from Distributed denial of service, or DDoS, and other malicious web attacks at no extra cost. A DDoS attack is a type of cyber-attack where multiple computers flood a server or website with fake requests, overwhelming it and causing it to shut down. This makes it impossible for the legitimate users to access the site. To enhance protection, you can use a web application firewall such as AWS WAF with customized rules. Or, you can use pre-configured rules managed by AWS or AWS Marketplace sellers.

2. Performance
AWS helps you improve your application performance by giving you access to its widespread and connected infrastructure through global locations called Points of Presence (or PoPs). These global PoPs are connected by a fast and reliable fiber network from AWS Global Infrastructure, resulting in very low network latency between applications in an AWS Region and the Edge locations.

3. Ease of use
AWS edge networking services can be set up in minutes within the AWS management console, either manually with one-click setup, or by following the AWS SDKs. The services offer seamless integration with other AWS resources, and you can also benefit from the collective knowledge and experience of a large community of users who use the same tools.

4. Cost savings
Delivering data through edge locations reduces your application costs by limiting and consolidating requests. Any cache-able data transferred to AWS edge locations from an AWS resource incurs no additional charge. All AWS edge networking services are pay-as-you-go, with no upfront costs, and no minimum usage.

### Amazon CloudFront edge locations
Amazon CloudFront is a web service that gives businesses and web application developers an easy and cost effective way to distribute content with low latency and high data-transfer speeds. Like other AWS services, Amazon CloudFront is a self-service, pay-as-you-go offering, requiring no long-term commitments or minimum fees. With CloudFront, your files are delivered to end-users using a global network of edge locations. Amazon CloudFront uses a global network of 450+ Points of Presence and 13 regional edge caches in 90+ cities across 48 countries. 

### Benefits of Amazon CloudFront edge locations
1. **Security of the content**. Amazon CloudFront improves security with traffic encryption and access controls, and uses AWS Shield Standard to defend against DDoS attacks.
2. **High performance**. CloudFront employs a global network of edge locations and regional edge caches that cache copies of your content close to your customers. CloudFront ensures that end-user requests are served by the closest edge location, which helps to minimize the distance that requests must travel, resulting in improved performance. For files not cached at edge locations and the regional edge caches, CloudFront keeps persistent connections with the origin servers so that those files can be retrieved as quickly as possible. 
3. **Cost effective**. Like other AWS services, CloudFront has no minimum commitments and you only pay for what you use. It saves you money and eliminates the hassle of managing a network of cache servers in multiple sites across the internet, while also eliminating the need to prepare for unexpected traffic increases. CloudFront also reduces the workload on the origin servers by combining multiple requests for the same file into one request. This minimizes the need to scale your origin servers, which saves you even more money.
4. **It’s programmable**. With edge compute features, you can easily run code across AWS locations globally, allowing you to personalize content and respond to your end users with improved latency. For example, you can use CloudFront Functions to redirect people to the correct language version of your website, based on language preferences on their devices. Because these functions run at all CloudFront locations, they can instantly handle large amounts of requests, typically in less than a millisecond.

### AWS Global Accelerator Edge locations
AWS Global Accelerator is a networking service that helps you improve the availability, performance, and security of your public applications. Global Accelerator uses a global network of 104 Points of Presence in 88 cities across 48 countries. 

### Benefit of AWS Global Accelerator edge locations
AWS Global Accelerator is a networking service that helps you improve the availability and performance of the applications that you offer to your local and global users. Global Accelerator is easy to set up, configure, and manage. With Global Accelerator, you don't have to worry about managing different IP addresses for different AWS Regions and Availability Zones, since it always directs user traffic to the best endpoint, based on performance. It also reacts instantly to changes in application health, your user’s location, and policies that you configure.

These are the six main benefits of using Global Accelerator edge locations: 
1. **Instant regional failover**. Global Accelerator automatically checks the health of your applications and routes user traffic only to healthy application endpoints. If the health status changes, or you make configuration updates, Global Accelerator reacts instantly to route your users to the next available endpoint.
2. **High availability**. Global Accelerator has a fault-isolating design that increases the availability of your application. It gives you two unique IP addresses that are serviced by separate physical infrastructure. This means that if one IP address becomes unavailable, your users can still access your application through the other healthy IP address. 
3. **No variability around clients that cache IP addresses**. Some client devices cache DNS records for long periods of time. So, if you make a configuration change, there’s an application failure, or there’s a change in your routing preference, you won’t know how quickly your users will receive updated IP addresses. Global Accelerator quickly updates your users with new information, even if their devices have old information saved. Updates take only a few seconds to be reflected, so application downtime is reduced.
4. **Improved performance**. Global Accelerator receives traffic from the edge location that is closest to your end-users. This traffic then travels through the fast and reliable AWS global network, which optimizes the path to your application that is running in an AWS Region. Global Accelerator chooses the optimal Region, based on the geography of end-users. This process helps reduce the time it takes for the first part of your application to load, and can improve performance.
5. **Easy manageability**. The IP addresses provided by Global Accelerator are fixed and provide a single-entry point to your applications. This lets you easily move your endpoints between Availability Zones or between AWS Regions, without having to update your DNS configuration or client-facing applications. 
6. **Fine-grained control**. Global Accelerator gives you the ability to control the amount of traffic that is sent to different regions. This is useful when you're conducting performance tests or making updates to your applications. Additionally, if your applications have to maintain a connection with a specific user, Global Accelerator allows you to direct all of their requests to the same endpoint. This provides you with detailed control over your applications.

### How is Amazon CloudFront different from AWS Global Accelerator?
Amazon CloudFront and AWS Global Accelerator are separate services that use the AWS global network and its edge locations around the world. Both services integrate with AWS Shield for DDoS protection.
#### AMAZON CLOUDFRONT
Amazon CloudFront speeds up the distribution of static and dynamic web content (HTTP objects). CloudFront caches content at edge locations that are close to end-users to provide a faster experience.

#### AWS GLOBAL ACCELERATOR
With AWS Global Accelerator, you create accelerators to improve the performance of your applications for local and global users. Global Accelerator doesn't cache content; instead it uses the AWS edge locations to receive end-user requests and then routes these requests to the closest AWS Region over the AWS global network.

### AWS Outposts
* Latency-sensitive workloads
* Data-residency requirements

Outposts are all about where businesses want to run their workloads. For example, a database specialist asks you, “Hey, we support a mission-critical database in our data center that must remain local. What options do we have?” The term “local” is the key here. 

Many businesses need their data to remain local because their workload is latency-sensitive. Or, these businesses need to meet data-residency requirements to store or process data in a specific geographical location. 

For example, government organizations must specify that certain data, such as taxpayers’ financial information, must be stored or processed in a specified location. Another example is related to financial services. US legislation, such as the Gramm-Leach-Bliley Act, also known as the Financial Modernization Act, requires financial institutions to explain how they keep, protect, and share customers' private information.

Outposts is a fully-managed service that provides businesses with the same hardware, software, security, and support that they can get from AWS, but in their own data center.

With Outposts, businesses can run some AWS services locally and also connect to a broad range of services available in the local AWS Region. Outposts support workloads and devices that require low latency access to on-premises systems, such as business applications for high-frequency trading or medical diagnostics.

Data sometimes needs to remain in a particular country, state, or municipality for regulatory, contractual, or information-security reasons. This is often the case with financial services, healthcare, oil and gas, and other highly-regulated industries. With Outposts, businesses can control where their workloads run and where their data is stored.

Finally, legacy, on-premises applications often have latency-sensitive system dependencies, making them difficult to migrate. Outposts allows businesses to segment migrations into smaller pieces on premises, maintaining latency-sensitive connectivity between application components until they are ready to migrate.

#### WITHOUT OUTPOSTS
To best understand AWS Outposts, consider this challenge: As you migrate applications to AWS, are there any applications that must remain on-premises?

These applications may need to generate near-real-time responses to end-user applications, or they may need to communicate with other on-premises systems or control on-site equipment. 

Examples include workloads running on factory floors for automated operations in manufacturing, real-time patient diagnosis or medical imaging, and content and media streaming. 

#### WITH OUTPOSTS
AWS on premises with Outposts

An Outposts offer AWS compute and storage capacity deployed at a customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region. 

You can create subnets on your Outpost and specify them when you create AWS resources, such as EC2 instances, Amazon Elastic Block Store (Amazon EBS) volumes, Amazon Elastic Container Service (Amazon ECS) clusters, and Amazon Relational Database Service (Amazon RDS) instances. 

Instances in Outpost subnets communicate with other instances in the AWS Region using private IP addresses, all within the same VPC. When you order Outpost capacity, you can choose from a variety of Outpost configurations. Each configuration provides a mix of EC2 instance types and EBS volumes.

#### Run AWS services locally
You can create many different resources on your Outpost to support low-latency workloads that must run in close proximity to on-premises data and applications.

### AWS Local Zones
A Local Zone is an extension of an AWS Region in geographic proximity to end-users. This is helpful when the Region that you want to use is a long distance from the data center or from the locations where the end-users need to run their applications.

For example, you may have a cloud migration team saying, “Hey, we need to run some low-latency applications within a geographic area where AWS doesn't currently have a Region. Do we have architectural solutions that are available here?” The answer is yes - Local Zones offer a type of AWS infrastructure deployment that places compute, storage, database, and other services closer to large population, industry, and IT centers.

Because they also have their own connection to the internet and support AWS Direct Connect, resources created in the Local Zone can serve local end-users with low-latency communications.

Unlike Outposts, which you deploy within your data center or a co-location of your choice, Local Zones are owned, managed, and operated by AWS. Local Zones eliminate the need for you to manage power, connectivity, and capacity by using the same set of APIs and tools that you are already using for an AWS Region. You can provision workloads on a Local Zone from your AWS Management Console, just as you would for Availability Zones and Regions today.

#### With and without Local Zones
#### WITHOUT LOCAL ZONES
Without Local Zones, end-user applications that require low latency may be excluded from the AWS Cloud. If the Regional data centers are too far from end users, the latency of running certain applications may be unacceptable.

#### WITH LOCAL ZONES
With Local Zones, your infrastructure and services are closer to users. Local Zones are an extension of an AWS Region, and they bring your infrastructure and compute, storage, database, and other services closer to end-users. They provide a high-bandwidth, secure connection between local workloads and workloads running in the AWS Region. 

### Summary
#### Regions, Availability Zones, and edge locations
* Regions are geographically isolated areas, where you can access the services needed to run your enterprise.
* Regions contain Availability Zones, which are one or more separated or isolated data centers with redundant power, ultra-low-latency networking, and connectivity. Availability Zones are located tens of miles apart from each other to protect against natural disasters.
* Edge locations run Amazon CloudFront to help get content closer to your customers, no matter where they are in the world. 

##### Reasons for using multiple Regions
* Disaster recovery and business continuity
* Decreased data latency for end-users
* Data sovereignty

##### Reasons for using multiple Availability Zones
* Make content highly available so that it has no single point of failure
* Increase resiliency to natural and man-made disasters

##### Benefits of edge Locations
* **Security**: All edge locations use AWS Shield standard to protect against attacks.
* **Performance**: AWS improves performance by giving access to global multi-service Points of Presence.
* **Ease-of-use**: AWS edge networking services can be set up in minutes within the AWS management console manually, with just a single click, or by following AWS SDKs.
* **Cost savings**: Using AWS edge locations reduces costs several ways (1) by limiting and consolidating traffic requests, (2) any cache-able data transferred to edge locations from an AWS resource incur no additional cost, (3) all AWS edge networking services are pay-as-you go without upfront costs or usage minimums.  

##### Benefits of using Amazon CloudFront edge locations
###### Security
Amazon CloudFront is a highly-secure CDN that provides both network and application level protection. Your traffic and applications benefit through a variety of built-in protections such as Amazon Shield standard. 

###### Higher performance
Amazon CloudFront improves performance by caching copies of content close to your users for faster content delivery. For files not cached at edge locations, CloudFront keep persistent connections with the original servers so that these files can be retrieved quickly. 

###### Cost effective
Amazon CloudFront helps you reduce costs with customizable, pay-as-you-go pricing options and free data transfer from AWS origin servers. CloudFront also reduces the number of requests that your origin server must respond to directly. This minimizes the need to scale your origin servers, which saves you even more money. 

###### Programmable
With edge compute features, you can easily run code across AWS locations globally, allowing you to personalize content and respond to your end-users with improved latency. For example, you can use CloudFront Functions to redirect people to the correct language version of your website, based on language preferences on their devices. 

##### Benefits of using AWS Global Accelerator edge locations
###### Instant regional failover
Global Accelerator will automatically check application health and route user traffic to healthy endpoints.

###### High availability
Accelerator gives you two unique IP addresses that are serviced by separate physical infrastructure. This means that if one IP address becomes unavailable, your users can still access your application through the other healthy IP address. This design increases the availbility of your application. 

###### No variability around clients that cache IP addresses
With Global Accelerator, there is no need to rely on the IP address caching settings of client devices, so changes can be updated immediately, reducing application downtime. 

###### Improved performance
An optimal AWS Region is chosen, based on the location of end-users, which reduces the time it takes for your application to load and improves performance. 

###### Easy manageability
The IP addresses provided by Global Accelerator are fixed and provide a single-entry point to your applications. This means that your applications remain accessible to your users, even if you move them to a different part of the world. This simplifies the process of managing your applications and help you avoid disruption in service. 

###### Fine-grained control
Global Accelerator gives you the ability to control the amount of traffic that is sent to different regions. This is useful when you're conducting performance tests or making updates to your applications. 

#### AWS Outposts
An AWS Outpost is a fully managed service that extends AWS infrastructure, services, APIs, and tools on-premises to decrease latency and address local data-processing needs.

#### AWS Local Zones
A Local Zone is an extension of an AWS Region in geographic proximity to the end-users. Unlike Outposts, which you deploy within your data center, Local Zones are owned, managed, and operated by AWS.

## AWS Service Domains and Services
### Compute
#### AMAZON EC2
Amazon Elastic Compute Cloud (Amazon EC2) is a virtual computing environment, allowing customers to use web service interfaces to launch instances with a variety of operating systems, load them with custom application environments, manage network access permissions, and run images using as many or few systems as needed.

#### AMAZON ECS
Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that enables customers to deploy, manage, and scale containerized applications. 

#### AMAZON LIGHTSAIL
Amazon Lightsail offers easy-to-use virtual private server (VPS) instances, containers, storage, databases, and more at a cost-effective monthly price. Lightsail can be used for things like launching simple web applications, creating custom websites, and building small business applications.

#### AWS LAMBDA
AWS Lambda enables customers to run code without provisioning or managing servers. They pay only for the compute time used. With Lambda, code can be run for virtually any type of application or backend service - all with no administration needed. Code is uploaded, and Lambda takes care of everything required to run and scale the code with high availability.

### Storage
#### AMAZON S3
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers scalability, data availability, security, and performance. It is used by customers of all sizes, and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, archives, Internet of Things devices, and big data analytics. Amazon S3 is designed for 99.999999999% durability, and it stores data for millions of applications for companies all around the world.

#### AMAZON S3 GLACIER
The Amazon S3 Glacier storage classes are built for data archiving, high performance, retrieval flexibility, and lowest cost archive storage in the cloud. All S3 Glacier storage classes provide virtually unlimited scalability and are designed for 99.999999999% of data durability.

#### AMAZON EBS
Amazon Elastic Block Store (Amazon EBS) is an easy-to-use, scalable, high-performance block-storage service designed for Amazon EC2. It can be used for things like big-data analytic engines and databases.

#### AMAZON EFS
Amazon Elastic File System (Amazon EFS) automatically grows and shrinks as a customer adds and removes files with no need for management or provisioning.

### Networking and content delivery
#### AMAZON VPC
Amazon Virtual Private Cloud (Amazon VPC) gives customers full control over a virtual networking environment, including resource placement, connectivity, and security. After setting up a VPC, resources such as EC2 instances are connected to it. Finally, communication is set up across accounts, Availability Zones, and Regions.

#### AMAZON CLOUDFRONT
Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds, all within a developer-friendly environment. CloudFront works with services such as Amazon Shield Standard for DDoS mitigation, Amazon S3, Amazon ELB, and Amazon EC2 as origins for applications.

#### ELB
Elastic Load Balancing (ELB) works as a traffic director. It automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones. 

### Database
#### AMAZON RDS
Amazon Relational Database Service (Amazon RDS) is a collection of managed services that make it simple to set up, operate, and scale databases in the cloud. Amazon RDS can be set up to use the following engines: Amazon Aurora with MySQL compatibility, Amazon Aurora with PostgreSQL compatibility, MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server. 

#### AMAZON DYNAMODB
Amazon DynamoDB is a NoSQL database that supports key-value and document data models. DynamoDB delivers single-digit millisecond performance at any scale.

It's a fully managed, multi-region, multi-master, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. DynamoDB can handle more than 10 trillion requests per day, and can support peaks of more than 20 million requests per second.

### Management and governance
#### AWS CLOUDTRAIL
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing for an AWS account. CloudTrail logs, continuously monitors, and retains account activity related to actions across a customer's AWS infrastructure. CloudTrail provides event history of AWS account activity, including actions taken through the Amazon Management Console, Amazon Software Development Kits, command-line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting.

#### AMAZON CLOUDWATCH
Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance. 

#### AWS CONFIG
AWS Config continually assesses, audits, and evaluates the configurations and relationships of AWS resources.

#### AWS AUDIT MANAGER
AWS Audit Manager helps customers map their compliance requirements to AWS usage data with pre-built and custom frameworks and automated evidence collection.

### Specialized AWS Services
### Artificial intelligence and machine learning
Machine learning is the science of developing algorithms and statistical models that computer systems use to perform tasks without explicit instructions, relying on patterns and inference instead. Computer systems use machine learning algorithms to process large quantities of historical data and identify data patterns. This allows them to predict outcomes more accurately from a given input data set. For example, data scientists could train a medical application to diagnose cancer from x-ray images by storing millions of scanned images and the corresponding diagnoses.

#### AMAZON SAGEMAKER
Amazon SageMaker provides developers and data scientists with the ability to build, train, and deploy machine learning models quickly. SageMaker is a fully-managed service that covers the entire machine learning workflow to label and prepare your data, choose an algorithm, train the model, tune and optimize it for deployment, make predictions, and take action.

#### AMAZON COMPREHEND
Amazon Comprehend is a natural-language processing service that uses machine learning to uncover valuable insights and connections in text.

##### Natural language processing
A brand of artificial intelligence computer science that studies and evolves the ability of computers to understand text and spoken words in a way that is similar to a human. 

#### AMAZON TRANSLATE
Amazon Translate is a text-translation service that uses advanced machine learning technologies to provide high-quality translation on demand.

### Data analytics
AWS provides the broadest selection of analytics services that fit all your data analytics needs and enables organizations of all sizes and industries to reinvent their business with data. AWS offers purpose-built services that provide the best price-performance, scalability, and at the lowest cost. These services include data movement, data storage, data lakes, big data analytics, log analytics, streaming analytics, business intelligence, and machine learning (ML).

##### Business intelligence
Business intelligence technology is used to help businesses make more data-driven decisions. It combines business analytics, data mining, data visualization, data tools and infrastructure, and general business best practices.

###### Semi-structured data
Semi-structured data has models that do not follow typical data models, such as tables, but still has tags or other markers that separate the data and create hierarchies. Examples of semi-structured data are emails, zipped files, and web pages.

###### Data lake
A data lake is a centralized repository that stores all structured and unstructured data in one place. 

#### AMAZON QUICKSIGHT
Amazon QuickSight is a cloud-scale business intelligence (BI) service that is used to deliver easy-to-understand insights. Amazon QuickSight connects to customer data in the cloud, and combines data from many different sources.

#### AMAZON REDSHIFT
Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. It helps companies to run complex analytic queries against petabytes of structured data.

Amazon Redshift uses SQL with hardware and machine learning designed by AWS to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes. 

#### AMAZON EMR
Amazon EMR (previously called Amazon Elastic MapReduce) is a managed cluster platform that simplifies running big data frameworks on AWS to process and analyze vast amounts of data.

### Application integration
Application integration on AWS is a suite of services that enable communication between decoupled components within micro-services, distributed systems, and serverless applications. You don’t need to refactor your entire architecture to benefit. Decoupling applications at any scale can reduce the impact of changes, making it easier to update and faster to release new features.

#### AMAZON SQS
Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Amazon SQS offers common constructs such as dead-letter queues and cost allocation tags. It provides a generic web services API that can be accessed using any programming language that the AWS SDK supports.

#### AMAZON SNS
Amazon Simple Notification Service (Amazon SNS) is a web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients. In Amazon SNS, there are two types of clients—publishers and subscribers—also referred to as producers and consumers.

Publishers communicate asynchronously with subscribers by producing and sending a message to a topic, which is a logical access point and communication channel. Subscribers (web servers, email addresses, Amazon SQS queues, Lambda functions) consume or receive the message or notification over one of the supported protocols (Amazon SQS, HTTP/S, email, SMS, AWS Lambda) when they are subscribed to the topic.

#### AMAZON EVENTBRIDGE
Amazon EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. Use it to route events from sources such as home-grown applications, AWS services, and third-party software to consumer applications across your organization. 

For example, Amazon S3 can send events to Amazon EventBridge whenever certain events happen in a bucket—a container for objects stored in Amazon S3. After EventBridge is enabled, all events below are sent to EventBridge. Customers can use rules with EventBridge to route events to additional targets. Examples of events are:
* Object created
* Object deleted
* Object restore initiated
* Object restore complete
* Object storage class changed

### Business applications
AWS business application services are meant to increase business agility, improve employee collaboration, and improve the customer experience. These applications can be used for things like improving contact-center performance, financial planning, and workforce development.

#### AMAZON CONNECT
Amazon Connect is an omnichannel cloud contact center that helps companies provide better customer service at a lower cost. You can set up a contact center in a few steps, add agents who are located anywhere, and start engaging with your customers. Amazon Connect provides a seamless experience across voice and chat for customers and agents. This includes one set of tools for skills-based routing, powerful real-time and historical analytics, and easy-to-use intuitive management tools—all with pay-as-you-go pricing.

#### AMAZON SES
Amazon Simple Email Service (Amazon SES) is a cloud email service provider that can integrate into any application for bulk email sending. It can send transactional or marketing emails, and customers pay only for what they use. Amazon SES also supports a variety of deployments including dedicated, shared, or owned IP addresses. Reports on sender statistics and a deliverability dashboard help businesses make every email count. 

##### Omnichannel/Multichannel
Omnichannel refers to when a business' in-person and online operations work together, for example, when you can buy a product online but return it in-person. 

Multichannel refers to when a business' in-person and online operations are separate, for example, when you buy a product online but cannot return it to a physical store in person. 

### End-user computing services
AWS End User Computing (EUC) services provide secure access to the applications and desktops the workforce needs to get their job done. With AWS EUC services, workers can be productive from any supported device while improving IT agility and organizational security. Resources can be scaled up or down on demand; providing teams with the resources they need, all without deploying and operating infrastructure.







## Features for Accessing AWS and AWS IAM
## Technology Support
## Assessment
