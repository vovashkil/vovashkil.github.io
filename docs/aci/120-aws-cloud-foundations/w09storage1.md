###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Storage 1
## Storage
### Pre-assessment
#### What are the three types of cloud storage? (Select THREE.)
The correct options are **Block storage**, **File storage**, and **Object storage**.

#### Which type of cloud storage is often used to store large amounts of unstructured data in buckets?
**Object storage** uses buckets to store large amounts of structured, unstructured, and semi-structured data.

#### What information is needed when retrieving files from file storage?
When using a file-based system, users must know **the exact path and location of the files** they need to work with or have a way to search the entire structure to find the files they need.

## Storage Fundamentals
### Storage
#### On-premises storage
On-premises storage means that your server is hosted within your organization's infrastructure and might be physically on-site. Your company controls, administers, and maintains the server. Data and other information are shared between computers through your local network. 

#### Cloud storage
With cloud storage, an outside service provider like AWS hosts your data on AWS hosted infrastructure. The cloud provider procures, installs, and maintains all hardware, software, and other supporting infrastructure in its data centers. You access these services and manage your account through the internet.

### Types of storage
Storage comes in three basic types: block storage, file storage, and object storage. These types of storage all have a particular use, and you will probably work with all three. 

#### Block storage
A block is a range of bytes or bits on a storage device. With block storage, files are divided into blocks and written to a physical drive. Each block is assigned a unique identifier and then written to the disk in the most efficient manner possible. Since blocks are assigned identifiers, they do not need to be stored in adjacent sections of the disk. They can be spread across multiple disks or environments. You can retrieve the individual blocks separately from the rest of the file, which makes block storage excellent for technology like relational databases.

With relational databases, you might only need to retrieve a single piece of a file, such as an inventory tracking number or one specific employee ID, instead of retrieving the entire inventory listing or whole employee repository.

Each block is assigned a unique identifier.

#### File storage
Historically, operating systems save data in hierarchical file systems organized in the form of directories, sub-directories and files, or folders, sub-folders, and files depending on the operating system.

For example, if you are troubleshooting an issue on a Linux distribution, you might need to look in /var/log or /etc/config. Inside of these directories, you need to identify which file to explore and open. When using a file-based system, you must know the exact path and location of the files you need to work with or have a way to search the entire structure to find the file you need.

File storage follows a hierarchical structure.

#### Object storage
Unlike the hierarchical structure used in file-based storage, object storage is a flat structure where the data, called an object, is located in a single repository known as a bucket. Objects can be organized to imitate a hierarchy by attaching key name prefixes and delimiters. Prefixes and delimiters help you group similar items to help visually organize and quickly retrieve your data. In the user interface, these prefixes give the appearance of a folder and sub-folder structure, but in reality, the storage is still a flat structure.

Object storage uses buckets for organizing storage.

### Choosing the right storage type
#### Define your requirements.
You must think about the workload requirements, security constraints, and performance expectations.

#### Review your storage options.
Depending on your workload, you might need more than one type of storage.

#### Design your storage strategy.
Choose a storage service and select the features you want to deploy.

### Cloud storage terminology
#### IOPS
I/O per second (IOPS) – the read/write I/O rate.

#### Latency
Time between I/O submission and completion, measured in milliseconds.

#### Throughput
The read/write transfer rate. Throughput = IOPS x I/O size.

### Cloud storage use cases
#### BLOCK STORAGE
**Enterprise applications**

Block storage provides highly available and highly durable storage to reliably run mission-critical applications on AWS.

The design of block storage provides versatile storage services with the following:
* Low latency and consistently high IOPS and throughput performance
* Capacity and performance scalability without workload disruption
* High availability

#### FILE STORAGE
**Content management**

A content management system (CMS) requires a common namespace and access to a file system hierarchy. Similar to web serving use cases, CMS environments typically have multiple servers that need access to the same set of files to serve up content. Since cloud file storage solutions adhere to the expected file system semantics, file naming conventions, and permissions that developers are accustomed to, storage of documents and other files can be integrated into existing CMS workflows.

#### OBJECT STORAGE
**Cloud-native applications**

Build fast, cost-effective, cloud-native applications by using object storage to store development and production data. The microservices that make up cloud-native applications share this data. With object storage, you can upload any amount of data and access it anywhere to deploy applications faster and reach more users. 

### Knowledge Check
#### Which cloud storage type uses a flat structure that stores data in a single repository?
**Object storage** is a flat structure that stores data, called objects, in a single repository, known as a bucket.

#### Which cloud storage type relies on key name prefixes and delimiters to imitate a hierarchical structure?
**Object storage** is a flat structure that relies on key name prefixes and delimiters to imitate a hierarchical structure.

#### Which of the following are considerations users must think about when defining cloud storage requirements (Select THREE)?
When defining storage requirements, users must think about **security constraints**, **workload requirements**, and **performance expectations**. The other options are incorrect because environmental controls, physical access requirements, and hardware maintenance are typically handled by the cloud provider.

### Summary
* Defining file, object, and block storage
* Describing file, object, and block storage
* Identifying when to use each type of storage

#### Types of cloud storage
There are three types of cloud storage. To review each type, choose the appropriate tab.

##### BLOCK STORAGE
A block is a range of bytes or bits on a storage device. With block storage, files are divided into blocks and written to a physical drive. Each block is assigned a unique identifier and then written to the disk in the most efficient manner possible.

##### FILE STORAGE
File storage stores data in hierarchical file systems organized in the form of directories, sub-directories and files, or folders, sub-folders, and files depending on the operating system.

When using a file-based system, you must know the exact path and location of the files you need to work with or have a way to search the entire structure to find the file you need.  

##### OBJECT STORAGE
Object storage is a flat structure where the data, called an object, is located in a single repository known as a bucket. Objects can be organized to imitate a hierarchy by attaching key name prefixes and delimiters. 

Prefixes and delimiters allow you to group similar items to help visually organize and easily retrieve your data. This process gives object storage the appearance of a folder and subfolder structure but in reality, the storage is still a flat structure.

#### Cloud storage use cases by type
##### Block storage
A use case that block storage is ideal for is enterprise applications. Block storage provides highly available and highly durable storage to reliably run mission-critical applications on AWS.

##### File storage
File storage is ideal for content management systems that require a common namespace and access to a file system hierarchy.

##### Object storage
Object storage is great for cloud-native applications. Object storage can store development and production data that the microservices that make up cloud-native applications can then share.

## AWS Cloud Storage Services
### Pre-assessment
#### A consultant is working with a potential client that is considering migrating to the cloud. The consultant wants to reinforce the positive aspects of migrating on-premises storage to the cloud. Which of the following are considered benefits of cloud storage that the consultant could use as examples (Select THREE)?
**Cost efficiency**, **scalability**, and **security** are all benefits that can be gained through the use of cloud storage.

#### Which storage service provides physically attached storage for an EC2 instance?
**Amazon EC2 instance store** provides temporary block-level storage for instances. This storage is located on disks that are physically attached to the host computer.

#### A company that maintains large quantities of unstructured data wishes to archive their data in the most cost-effective way possible. Which storage service would best fit their needs?
**Amazon S3** can be used to store nearly limitless amounts of unstructured data. By using Amazon S3 storage classes, the company can store their data cost-effectively based on their access needs.

### AWS Cloud Storage

### Benefits of cloud storage
Cloud storage provides you with a number of benefits. 

#### Cost efficient
Optimize storage costs based on how frequently and quickly data needs to be accessed.

#### Secure
In cloud storage, data is saved across multiple servers, providing for increased durability

#### Agile
Make resources available in minutes, not weeks.

#### Scalable
Cloud storage is scalable; it can grow and shrink as your workloads change.

#### Managed
Cloud storage is managed, so you don't have to worry about servers and can focus on your data and applications.

#### Backed up
Cloud storage can be backed up to multiple physical locations to protect against accidental deletion or data corruption.

### Amazon cloud storage services
AWS provides you with an array of cloud storage services that can be tailored to fit the needs of your organization. 

#### Amazon S3
Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. It is intentionally built with a minimal feature set that focuses on simplicity and robustness. You have access to the same highly scalable, reliable, fast, inexpensive data storage infrastructure that Amazon uses to run its own global network of websites. The service aims to maximize benefits of scale and to pass those benefits on to the you, the customer. 

#### Amazon EFS
Amazon EFS provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance. Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. 

Because Amazon EFS has a basic web services interface, you can create and configure file systems quickly. The service manages all the file storage infrastructure for you, meaning that you can avoid the complexity of deploying, patching, and maintaining complex file system configurations. 

With Amazon EFS, you pay only for the storage used by your file system, and there is no minimum fee or setup cost. Amazon EFS offers a range of storage classes designed for different use cases, including standard storage classes and one zone storage classes.

#### Amazon FSx
Amazon FSx makes it convenient and cost effective to launch, run, and scale feature-rich, high-performance file systems in the cloud. It supports a wide range of workloads with its reliability, security, scalability, and broad set of capabilities. Amazon FSx is built on the latest AWS compute, networking, and disk technologies to provide high performance and lower total cost of ownership. And as a fully managed service, it handles hardware provisioning, patching, and backups—freeing you up to focus on your applications, your end users, and your business.

Amazon FSx lets you choose between four widely used file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre. This choice is typically based on your familiarity with a given file system or by matching the file system's feature sets, performance profiles, and data management capabilities to the requirements of your workload.

##### FULLY FEATURED AND MANAGED
Amazon FSx assists you in providing broadly accessible and highly performant file storage for a wide variety of use cases. Thanks to its support of industry-standard protocols, Amazon FSx offers connectivity to Linux, Windows, and macOS users and applications. 

Amazon FSx also delivers sub-millisecond latencies and high throughput to meet the performance needs of your most demanding workloads. Amazon FSx combines the capabilities of widely used file systems with the simplicity of a fully managed AWS service to help you migrate legacy applications and build new applications quickly.

##### HIGHLY AVAILABLE AND PROTECTED
Amazon FSx ensures high availability by automatically replicating your data within or across AWS Availability Zones to protect it from component failure. Additionally, Amazon FSx continuously monitors for hardware failures, automatically replaces infrastructure components, or switches to a stand-by file server in the event of a failure.  

To meet your data protection requirements, Amazon FSx lets you replicate your file systems across AWS Regions and also integrates with AWS Backup for centralized backup management and additional levels of compliance. For enhanced security, Amazon FSx automatically encrypts your data at rest using AWS Key Management Service (AWS KMS) and also supports encryption of data in transit.

##### COST EFFECTIVE
Amazon FSx lets you optimize your price and performance to support a broad spectrum of use cases, from small user shares to the most demanding compute-intensive workloads. Amazon FSx offers SSD or HDD storage options and lets you provision and scale throughput performance independently from storage capacity.

You can choose from Single-AZ or Multi-AZ deployment options based on your high availability requirements. Amazon FSx file systems support a rich set of storage efficiency features, including data deduplication, compression, and usage quotas.

##### HYBRID
Amazon FSx helps you do more with your data. You can migrate and synchronize data from on premises to AWS and make it immediately available to a broad set of integrated AWS services. You can provide storage to global users by storing data in the cloud with low-latency local access provided by Amazon FSx File Gateway and NetApp ONTAP’s Global File Cache.

#### Amazon EBS
Amazon EBS provides block level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances. EBS volumes that are attached to an instance are exposed as storage volumes that persist independently from the life of the instance. You can create a file system on top of these volumes, or use them in any way you would use a block device (such as a hard drive). You can dynamically change the configuration of a volume attached to an instance.

#### Amazon S3 Glacier storage classes
The Amazon S3 Glacier storage classes are purpose-built for data archiving, providing you with the highest performance, most retrieval flexibility, and lowest cost archive storage in the cloud. All S3 Glacier storage classes provide virtually unlimited scalability and are designed for 99.999999999 percent (11 nines) of data durability. The S3 Glacier storage classes deliver options for the fastest access to your archive data and the lowest cost archive storage in the cloud.

#### Amazon EC2 instance store
An instance store provides temporary block-level storage for your instance. This storage is located on disks that are physically attached to the host computer. Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, and other temporary content, or for data that is replicated across a fleet of instances, such as a load-balanced pool of web servers. Amazon EC2 instance stores persist only as long as the life of the EC2 instance they are attached to.

An instance store consists of one or more instance store volumes exposed as block devices. The size of an instance store and the number of devices available varies by instance type.

### Knowledge Check
#### An administrator is tasked with explaining the benefits of cloud storage to their supervisor. Which of the following statements correctly describes the benefit of scalability?
Scalability is the ability of cloud storage to **shrink or grow as a workload changes**.

#### Which AWS cloud storage service attaches to an instance and is exposed as storage volumes that persist independently from the life of the instance?
**EBS volumes** that are attached to an instance are exposed as storage volumes that persist independently from the life of the instance.

#### Which of the following AWS services provides temporary block-level storage on disks that are physically attached to the host computer?
**Amazon EC2 instance store** provides temporary block-level storage for an instance. This storage is located on disks that are physically attached to the host computer.

### Summary
* Describing the benefits of cloud storage
* Describing the features and benefits of Amazon S3, Amazon EFS, and Amazon FSx
* Describing the features of Amazon EBS, Amazon S3 Glacier, and Amazon EC2 instance store

#### Benefits of cloud storage
Cloud storage provides you with a number of benefits.
* **Cost efficient** - optimize storage costs based on how frequently and quickly data needs to be accessed.
* **Secure** - in cloud storage, data is saved across multiple servers, providing for increased durability.
* **Agile** - make resources available in minutes, not weeks. 
* **Scalable** - cloud storage is scalable; it can grow and shrink as your workloads change.
* **Managed** - cloud storage is managed, so you don't have to worry about servers and can focus on your data and applications.
* **Backed up** - cloud storage can be backed up to multiple physical locations to protect against accidental deletion or data corruption.

#### Amazon cloud storage services
AWS provides you with an array of cloud storage services that can be tailored to fit the needs of your organization. To review the AWS cloud storage services discussed in this module, expand each of the following six categories.

##### Amazon S3
Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance.

##### Amazon EFS
Amazon Elastic File System (Amazon EFS) provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance.

##### Amazon FSx
Amazon FSx enables you to launch, run, and scale feature-rich, high-performance file systems in the cloud. Amazon FSx lets you choose between four widely-used file systems.

##### Amazon EBS
Amazon Elastic Block Store (Amazon EBS) provides block level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted block devices.

##### Amazon S3 Glacier storage classes
The Amazon S3 Glacier storage classes are purpose-built for data archiving, providing you with the highest performance, most retrieval flexibility, and the lowest cost archive storage in the cloud.

##### Amazon EC2 instance store
Amazon EC2 instance stores provide temporary block-level storage for instances. This storage is located on disks that are physically attached to the host computer and persists only as long as the computer it's attached to.

## Using AWS Storage Services for Data Migration
### Pre-assessment
#### Which AWS service is ideal for offline data transfers?
**AWS Snowball Edge** is ideal for offline transfers and use in environments with intermittent connectivity, as well as extremely remote locations.

#### Which of the following reasons should lead planners to consider retiring an application or workload rather than migrating it to the cloud?
Applications that have **no inbound connections for 90 days or more should be considered for retirement rather than migration**.

#### Which AWS service would be ideal to transfer petabytes (PBs) of data from an on-premises data center to the AWS Cloud?
**Snowmobilei** can transfer up to 100 PB of data from on premises to the AWS Cloud.

The other options are incorrect because of the following:
* **Snowcone** can provide storage of up to 14 TB, which will not meet the requirements for transfers measured in petabytes.
* **Transfer Family** uses common file protocols to transfer data to the cloud, which is not ideal for petabyte-sized data transfers.
* **DataSync** is capable of transferring hundreds of terabytes of data using internet connections but is not ideal for petabyte-sized data transfers.

### Migrating Data Into the Cloud
Data is a cornerstone of successful application deployments, analytics workflows, and machine learning innovations. When moving data to the cloud, you need to understand where you are moving it for different use cases, the types of data you are moving, and the network resources available, among other considerations. 

A cloud migration is the process of moving any workload or application into the cloud from the following:
* An on-premises environment
* A hosting facility
* Another cloud environment

### Storage migration
iWhether starting from traditional on-premises environments or cloud-native, the cloud migration process helps you achieve a variety of architectures. Your final state can include any combination of on-premises infrastructure, single or multiple public cloud environments, and even on-premises private cloud applications.

In the context of this module, the term application refers to the set of technical resources (application and infrastructure) that is being migrated to the AWS Cloud. Typically, these technical resources combine to constitute a business service or application, and they may be running on multiple systems. This course uses the terms workload and application interchangeably to refer to the combined set of resources that is being migrated to the AWS Cloud. 

This is not always the same as a business application as understood by the IT development teams or IT operations teams. For migration purposes, it is sometimes convenient to combine multiple business applications into a single workload in order to facilitate migration. At other times, it makes sense to split a complex business application into multiple workloads in order to migrate in multiple phases. 

The three-phase migration process is designed to help your organization approach a migration of tens, hundreds, or thousands of applications. While each phase is a common component of a successful migration, they are not discrete phases, but an iterative process. As you iterate and migrate more applications, you will be able to drive repeatability and predictability in processes and procedures, and find that the migration process accelerates.

#### Assess
At the start of your journey, you assess your organization’s current readiness for operating in the cloud. Most importantly, you want to identify the desired business outcomes and develop the business case for migration.

#### Mobilize
As part of the mobilize phase, you create a migration plan and refine your business case. You address gaps in your organization’s readiness that were uncovered in the assess phase, with a focus on building your baseline environment (the “landing zone”), driving operational readiness, and developing cloud skills.

A strong migration plan starts with a deeper understanding of the interdependencies between applications, and evaluates migration strategies to meet your business case objectives. One critical aspect of developing your migration strategy is to collect application portfolio data and rationalize applications using the seven common migration strategies: retire, retain, rehost, relocate, repurchase, re-platform, and refactor.

Not every decision in a migration can be automated, but there are AWS tools and services available to help you make easier and better decisions.

#### Migrate and Modernize
During the migrate and modernize phase, each application is designed, migrated, and validated.

AWS Migration Hub is the one destination for cloud migration and modernization, giving you the tools you need to accelerate and simplify your journey with AWS. Perhaps you’re making the case for cloud within your organization, or creating a data-driven inventory of existing IT assets. Maybe you’re planning, running, and tracking a portfolio of applications migrating to AWS. Or you might be modernizing applications already running on AWS. In all of these cases, Migration Hub can help with your cloud transformation journey.

Data is the cornerstone of successful cloud application deployments. AWS has the most options to get data to our cloud depending on the nature of the data and the application.

### Cloud migration strategies
A migration strategy is the approach used to migrate a workload into the AWS Cloud. There are seven migration strategies for moving applications to the cloud, known as the 7 Rs. 

#### Retire
This is the migration strategy for the applications that you want to decommission or archive. Retiring the application means that you can shut down the servers within that application stack. The following are common use cases for the retire strategy:
* There is no business value in retaining the application or moving it to cloud.
* You want to eliminate the cost of maintaining and hosting the application.
* You want to reduce the security risks of operating an application that uses an operating system version or components that are no longer supported.
* You might want to retire applications based on their performance. For example, you might want to retire applications that have an average CPU and memory usage below 5 percent, known as zombie applications. You might also choose to retire some applications that have an average CPU and memory usage between 5 and 20 percent over a period of 90 days, known as idle applications. You can use the utilization and performance data from your discovery tool to identify zombie and idle applications.
* There has been no inbound connection to the application for the last 90 days.

#### Retain
This is the migration strategy for applications that you want to keep in your source environment or applications that you are not ready to migrate. You might choose to migrate these applications in the future.

The following are common use cases for the retain strategy:
* **Security and compliance** – You might want to retain applications to remain in compliance with data residency requirements.
* **High risk** – You might decide to retain an application because it requires a detailed assessment and plan before migration.
* **Dependencies** – You might decide to retain an application if you need to migrate one or more other applications first.
* **Applications that are recently upgraded** – You might want to postpone migrating the application until the next technical refresh because you recently invested in upgrading your current system.
* **No business value to migrate** – There is no business value for migrating some applications to the cloud, such as those with only a few internal users.
* **Plans to migrate to software as a service (SaaS)** – You might choose retain an application until the SaaS version is released by the vendor. This is a common strategy for vendor-based applications.
* **Unresolved physical dependencies** – You might choose to retain an application that is dependent on specialized hardware that does not have a cloud equivalent, such as machines in a manufacturing plant.
* **Mainframe or mid-range applications and non-x86 Unix applications** – These applications require careful assessment and planning before migrating them to the cloud. Examples of mid-range applications include **IBM AS/400** and **Oracle Solaris**.
* **Performance** – You might want to retain applications based on their performance. For example, you might want to keep zombie or idle applications in your source environment.

#### Rehost
This strategy is also known as **lift and shift**. Using this strategy, you move your applications from your source environment to the AWS Cloud without making any changes to the application. For example, you migrate your application stack from on premises to the AWS Cloud.

With rehost, you can migrate a large number of machines from multiple source platforms (physical, virtual, or another cloud) to the AWS Cloud without worrying about compatibility, performance disruption, long cutover windows, or long-distance data replications.

Your application continues to serve users while the workloads are being migrated, which minimizes disruption and downtime. The downtime depends on your cutover strategy.

This strategy helps you to scale your applications without implementing any cloud optimizations that can save you time or money. Applications are more convenient to optimize or re-architect when they are already running in the cloud because it is faster to integrate to AWS services and manage your workloads.

#### Relocate
Using this strategy, you can transfer a large number of servers, comprising one or more applications, at a given time from an on-premises platform to a cloud version of the platform. You can also use the relocate strategy to move instances or objects to a different virtual private cloud (VPC), Region, or AWS account. For example, you can use this strategy to transfer servers in bulk from VMware software-defined data center to VMware Cloud on AWS, or you can transfer an Amazon Relational Database Service (Amazon RDS) DB instance to another VPC or AWS account.

The relocate strategy doesn’t require that you purchase new hardware, rewrite applications, or modify your existing operation. During relocation, the application continues to serve users, which minimizes disruption and downtime. Relocate is the quickest way to migrate and operate your workload in the cloud because it does not impact the overall architecture of your application.

#### Repurchase
This strategy is also known as **drop and shop**. You replace your application with a different version or product. The new application should provide more business value than the existing on-premises application, including features such as accessibility from anywhere, no infrastructure to maintain, and pay-as-you-go pricing models. Repurchasing the application typically reduces costs associated with maintenance, infrastructure, and licensing.

The following are common use cases for the repurchase migration strategy:
* **Moving from a traditional license to SaaS** – This removes the burden of managing and maintaining the infrastructure and helps reduce licensing issues.
* **Version upgrades or third-party equivalents** – By replacing your existing on-premises application with the vendor’s latest version or third-party equivalent in the cloud, you can use new features, integrate with cloud services, and scale the application.
* **Replacing a custom application** – You can avoid recoding and re-architecting a custom application by repurchasing a vendor-based SaaS or cloud-based application.

Before purchasing, you need to assess the application according to your business requirements, especially security and compliance.

After you purchase the new application, the following are the next steps:
* Training your team and users with the new system
* Migrating your data to the newly purchased application
* Integrating the application into your authentication services, such as Microsoft Active Directory, to centralize authentication
* Configuring networking to help secure communication between the purchased application, your users, and your infrastructure

Typically, the application vendor helps you with these activities for a smooth transition.

#### Replatform
This strategy is also known as **lift, tinker, and shift** or **lift and reshape**. Using this migration strategy, you move the application to the cloud, and you introduce some level of optimization to operate the application efficiently, reduce costs, or take advantage of cloud capabilities. For example, you might replatform a Microsoft SQL Server database to Amazon RDS for SQL Server.

Using this strategy, you might make a few or many changes to the application, depending on your business goals and your target platform.

The following are common use cases for the replatform migration strategy:
* You want to save time and reduce cost by moving to a fully managed service or serverless service in the AWS Cloud.
* You want to improve your security and compliance stance by upgrading your operating system to the latest version. By using End-of-Support Migration Program (EMP) for Windows Server, you can migrate your legacy Windows Server applications to the latest supported versions of Windows Server on AWS without any code changes. You can use this decision tree in the AWS EMP for Windows Server User Guide to help you determine your EMP workloads.
* You can reduce costs by using AWS Graviton processors, custom-built processors developed by AWS.
* You can reduce costs by moving from a Microsoft Windows operating system to a Linux operating system. You can port your .NET Framework applications to .NET Core, which can run on a Linux operating system. Porting Assistant for .NET is an analysis tool that helps you port your applications to Linux.
* You can improve performance by migrating virtual machines into containers, without making any code changes. You can modernize your .NET and Java applications into containerized applications by using the AWS App2Container migration tool.

The replatform strategy keeps your legacy application running without compromising security and compliance. Replatform reduces cost and improves performance by migrating to a managed or serverless service, moving virtual machines to containers, and avoiding licensing expenses.

#### Refactor or re-architect
Using this strategy, you move an application to the cloud and modify its architecture by taking full advantage of cloud-native features to improve agility, performance, and scalability. This is driven by strong business demand to scale, accelerate product and feature releases, and reduce costs.

The following are common use cases for the refactor migration strategy:
* The legacy mainframe application can no longer address the demand of the business because of its limitations or it is expensive to maintain.
* You have a monolith application that is already hindering efforts to deliver products quickly or address customer needs and demands.
* You have a legacy application that nobody knows how to maintain, or the source code is unavailable.
* The application is difficult to test, or test coverage is very low. This affects the quality and delivery of new application features and fixes. By redesigning the application for the cloud, you can increase the test coverage and integrate automated testing tools.
* For security and compliance reasons, when moving a database to the cloud, you might need to extract some tables (such as customer information or patient diagnosis tables) and retain those tables on premises. In this situation, you need to refactor your database to separate the tables that will be migrated from those that will be retained on premises.

### AWS Services for Data Migration
AWS offers a wide variety of services and partner tools to help you migrate your datasets, whether they are files, databases, machine images, block volumes, or even tape backups.

#### AWS DataSync
DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between storage systems and services. DataSync can copy data to and from S3 buckets, Amazon EFS file systems, Network File System file servers, Server Message Block file servers, and object storage systems, among others.

DataSync can provide you with the following benefits:
* DataSync helps you simplify and automate data movement by making it more convenient to move data over the network between storage systems and services. DataSync automates both the management of data-transfer processes and the infrastructure required for high performance and secure data transfer.
* DataSync transfers data securely by providing end-to-end security, including encryption and integrity validation, to help ensure that your data arrives securely, intact, and ready to use. DataSync accesses your AWS storage through built-in AWS security mechanisms, such as AWS Identity and Access Management (IAM) roles. It also supports VPC endpoints, giving you the option to transfer data without traversing the public internet and further increasing the security of data copied online.
* DataSync moves your data faster by transferring data rapidly over the network into AWS. DataSync uses a purpose-built network protocol and a parallel, multi-threaded architecture to accelerate your transfers. This approach speeds up migrations, recurring data-processing workflows for analytics and machine learning, and data-protection processes.
* DataSync can reduce your operational costs by moving data cost-effectively with the flat, per-gigabyte pricing of DataSync. You can save on script development and deployment and maintenance costs. You can also avoid the need for costly commercial transfer tools.

#### AWS Snow Family
Snow Family uses purpose-built devices to move petabytes of data offline. Snow Family devices have computing resources to collect and process data at the edge. Devices can support EC2 instances, AWS IoT Greengrass functions, and Kubernetes deployments on Amazon Elastic Kubernetes Services (Amazon EKS) anywhere.

All data moved to Snow Family devices is automatically encrypted with 256-bit encryption keys that are managed by AWS KMS. Encryption keys are never stored on the device, so your data stays secure during transit.

After the data migration job is complete and verified, AWS performs a software erasure of the device that follows the National Institute of Standards and Technology guidelines for media sanitization.

#### AWS Transfer Family
Transfer Family is a secure transfer service you can use to transfer files into and out of AWS storage services.

With Transfer Family, you get access to a file transfer protocol server in AWS without the need to run any server infrastructure. You can use this service to migrate your file transfer-based workflows to AWS while maintaining your end users' clients and configurations as is. You first associate your hostname with the server endpoint, then add your users and provision them with the right level of access. After you do this, your users' transfer requests are serviced directly out of your Transfer Family server endpoint.

AWS Transfer Family supports data transfers over SSH File Transfer Protocol version 3, FTP Secure, FTP, and Applicability Statement 2.

Transfer Family provides the following benefits:
* It is a fully managed service that scales in real time to meet your needs.
* You don't need to modify your applications or run any file transfer protocol infrastructure.
* With your data in durable Amazon S3 storage, you can use native AWS services for processing, analytics, reporting, auditing, and archival functions.
* With Amazon EFS as your data store, you get a fully managed elastic file system for use with AWS Cloud services and on-premises resources. Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. This helps eliminate the need to provision and manage capacity to accommodate growth.
* It has a fully managed, serverless file transfer workflow service that helps you set up, run, automate, and monitor processing of files uploaded using Transfer Family.
* There are no upfront costs, and you pay only for the use of the service.

#### Amazon S3 Transfer Acceleration
Amazon S3 Transfer Acceleration is a bucket-level feature that provides fast and secure file transfer over long distances between your client and an S3 bucket. Transfer Acceleration is designed to optimize transfer speeds from across the world into S3 buckets. Transfer Acceleration takes advantage of the globally distributed edge locations in Amazon CloudFront. As the data arrives at an edge location, the data is routed to Amazon S3 over an optimized network path.

When you use Transfer Acceleration, additional data transfer charges might apply.

**Transfer Acceleration is currently not supported for buckets in all Regions.**

### Data migration service use cases
#### DATASYNC
* **Data migration** – Move active datasets rapidly over the network into Amazon S3, Amazon EFS, FSx for Windows File Server, FSx for Lustre, or FSx for OpenZFS. DataSync includes automatic encryption and data integrity validation to help make sure that your data arrives securely, intact, and ready to use.
* **Archiving cold data** – Move cold data stored in on-premises storage directly to durable and secure long-term storage classes such as S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive. Doing so can free up on-premises storage capacity and shut down legacy systems.
* **Data protection** – Move data into any Amazon S3 storage class, choosing the most cost-effective storage class for your needs. You can also send data to Amazon EFS, FSx for Windows File Server, FSx for Lustre, or FSx for OpenZFS for a standby file system.
* **Data movement for timely in-cloud processing** – Move data in or out of AWS for processing. This approach can speed up critical hybrid cloud workflows across many industries. These include machine learning in the life sciences industry, video production in media and entertainment, big data analytics in financial services, and seismic research in the oil and gas industry.

#### SNOW FAMILY
You can use Snow Family services for data transfer and occasional pre-processing on location. Some large data transfer examples include cloud migration, disaster recovery, data center relocation, and remote data collection projects. These projects typically require you to migrate large amounts of data in the shortest and most cost-effective amount of time.

Some example use cases for AWS Snowcone and AWS Snowball Edge computing capabilities include Internet of Things sensor stream capture, on-the-fly media transcoding, image compression, aggregating metrics, and control signaling and alarming.

#### TRANSFER FAMILY
File transfer protocols are used in data exchange workflows across different industries, such as financial services, healthcare, advertising, and retail. Transfer Family simplifies the migration of file transfer workflows to AWS. Some common Transfer Family use cases using the various protocols are the following: 
* Data lakes in AWS for uploads from third parties, such as vendors and partners
* Subscription-based data distribution with your customers
* Data distribution
* Content management
* Workflows with compliance requirements that rely on having data protection and security features built into the protocol
* Integrations with enterprise resource planning and customer relationship management systems

### DataSync Service Overview
### Transferring large amounts of data
All organizations need to transfer data from one place to another, whether that need is occasional or frequent. Many organizations attempt do-it-yourself (DIY) data transfers to meet their needs. These DIY data transfers can be manageable with a few files and performed occasionally. However, the DIY solutions are not scalable solutions that can manage a data transfer involving hundreds, thousands, or millions of files. 

When you need to transfer more than a few files, be sure to ask enough questions about your needs and the needs of your organization before you decide on the best approach. 
* What transfer protocol should you use?
* Do you have enough compute and infrastructure resources to actually transfer the data?
* Are you going to compress the data in transfer?
* Do you need to preserve your storage system metadata?
* Do you need to be able to scale out the transfer?
* How are you going to handle security?
* How will you validate that all of your data got transferred properly? 

**DataSync** is an AWS managed service that simplifies, automates, and accelerates the copying of large amounts of data to and from AWS Cloud storage services. DataSync is used to transfer data between on-premises storage and the AWS Cloud and transfer data between AWS Cloud storage services. As a managed service, DataSync reduces your requirements to modify applications, develop scripts, or manage infrastructure to copy data between storage systems and services.

### What does DataSync do?
iDataSync supports data copy or synchronization tasks from a supported source storage system or service to a supported destination storage system or service. DataSync tasks support data transfers in only one direction. The following are a few features of DataSync:
* DataSync copies data between on-premises storage systems and AWS storage services in the AWS Cloud. On-premises storage systems include:
* Storage systems that support Network File System (NFS) and server message block (SMB) file system protocols. On-premises storage systems can include network-attached storage systems, file shares, and file servers.
* On-premises object storage systems that are Amazon S3 API compatible.
* Storage systems that use Hadoop Distributed File System (HDFS) storage protocol.
* DataSync is included with some Snow Family devices for data transfers from the devices to the AWS Cloud. DataSync is available when the devices are configured for local compute and storage jobs. Not all Snow Family devices include DataSync at this time.
* DataSync copies or synchronizes data between supported AWS storage services within the same Region or between Regions.
* You can use DataSync to copy between your in-cloud, self-managed NFS and SMB shares attached to your EC2 instances and supported AWS storage services.
* Supported AWS Cloud storage systems include Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, Amazon FSx for Lustre, and Amazon FSx for OpenZFS.

With DataSync features, you can implement robust data transfers from on premises to the AWS Cloud and within the AWS Cloud for select data storage services. DataSync solves and streamlines the data transfer challenges experienced by many organizations.

#### General features
##### Seamless data transfer
You can configure DataSync to perform seamless data copy transfers between on-premises NFS file shares, SMB file shares, on-premises Amazon S3 API compatible object storage, and HDFS data storage to AWS storage services. This can also be done between AWS storage services within the AWS Cloud. 

You can configure DataSync to perform one-time data transfers or automate ongoing transfers between storage systems. With the available task configuration options, you can create different data copy tasks to meet a wide range of use cases.

Each data transfer task provides a one-way transfer between the source storage location and the destination storage location. The transfer direction is established when you specify the source location and destination location when configuring your task.

DataSync removes many of the challenges you face when developing and managing scripts or deploying commercial data transfer tools. DataSync improves your productivity and reduces your management time.

##### Fully managed service
DataSync is a fully managed service in the AWS Cloud. As a managed service, AWS manages the AWS resources required to optimize the service performance and protect your data. 

DataSync transfers perform optimizations on how, when, and what data is sent over the network. Some of the DataSync service's optimizations include incremental transfers, in-line compression, and sparse-file detection. DataSync provides in-line data validation and encryption for data protection and security.

Because it is a fully managed service, you can use DataSync to focus on your business instead of spending time managing data transfers.

##### Security and compliance
To secure any data you transfer between your on-premises storage and the AWS Cloud or between AWS storage services, DataSync encrypts data in transit using TLS version 1.2. 

Each task performs integrity checks for all data in transit. Optionally, DataSync can perform integrity checks for data at rest. Integrity checks verify that your destination data matches your source data and validates data consistency.

AWS KMS integrates with AWS storage services to encrypt data at rest in AWS Cloud storage. For most services, you can use system-generated AWS managed encryption keys or customer managed keys that you provide. For data stored in Amazon S3, you can use server-side encryption keys managed by Amazon S3 (SSE-S3).

##### Native integration with AWS services
DataSync supports integration with AWS Cloud storage services such as Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, Amazon FSx for Lustre, and Amazon FSx for OpenZFS as a source and destination for copy tasks.

DataSync integrates natively with many other AWS services, helping you manage across your AWS Cloud environment. Some of the key services include the following:
* IAM provides access controls and security.
* Amazon CloudWatch provides activity monitoring and logging.
* AWS CloudTrail provides audit logging.
* DataSync uses the network connections provided by AWS Site-to-Site VPN, AWS Direct Connect, AWS PrivateLink, and AWS Transit Gateway to provide secure connectivity from on-premises storage systems to the AWS Cloud.
* DataSync can connect using private, public, and US Federal Information Processing Standards endpoints.

##### Cost-effective pricing
When using the DataSync service, you pay only for the amount of data that you copy on a flat per-gigabyte basis.

Your service costs are predictable with no additional costs for increasing and decreasing resources to meet your demand requirements. You have no additional services to start, stop, manage, or pay for.

For pricing information, refer to the [AWS DataSync Pricing](https://aws.amazon.com/datasync/pricing/) page on the AWS website.

Note: Additional storage, request, transfer, logging, and monitoring fees for other services apply.

##### Simple configuration and use
You can use the AWS Management Console, AWS Command Line Interface (AWS CLI), or DataSync API to configure and manage your DataSync tasks.

The console guides you through the configuration process. Using the console, you can create your source and destination locations, configure your copy tasks, and integrate DataSync with supported AWS services.

With DataSync configuration options, you can quickly customize your transfer task. DataSync options include the following:
* Data verification options – As DataSync transfers data, it always performs data integrity checks during the transfer. You can choose additional verification options to compare source and destination at the end of a transfer. 
* Ownership and permissions-related options – DataSync preserves metadata between storage systems that have similar metadata structures. Different options are used to configure metadata preservation depending on the storage system type. 
* File management and metadata options – You can configure DataSync tasks to copy file metadata, keep deleted files, and overwrite files in the destination. 
* Content filtering – When you transfer data from your source to your destination location, you can apply filters to transfer only a subset of the files in your source location. 
* Bandwidth throttling – You can configure a bandwidth limit for DataSync tasks. You can use all available bandwidth or set a bandwidth limit and schedule.
* Task scheduling – You can schedule a DataSync task to be run at a specific time. If you are using a single agent to run multiple tasks, you can queue those tasks. 

### Snow Family Overview
Snow Family helps customers that need to run operations in harsh, non-data center environments and in locations with inconsistent network connectivity. Snow Family consists of Snowcone, Snowball Edge, and AWS Snowmobile. Each of these devices is designed to meet the unique compute and capacity challenges required by different use cases. These services help physically transport up to exabytes of data into and out of AWS. AWS owns and manages Snow Family devices. The devices integrate with AWS security, monitoring, storage management, and compute capabilities. 

#### Snow Family options overview
Snow Family offers three classifications of data transfer and edge computing solutions to solve different levels of challenges:
* Snowcone, a small, rugged, portable, secure edge computing, storage, and data transfer device
* Snowball Edge, a rugged petabyte-scale data transport device with onboard storage and compute capabilities
* Snowmobile, a large truck to migrate or transport exabyte-scale datasets into and out of the AWS Cloud

#### Snowcone
Snowcone is the smallest member of the Snow Family edge computing and data transfer devices. Snowcone is portable, ruggedized, and secure. You can use Snowcone to collect, process, and move data to AWS. You can perform these operations offline by shipping the device to Amazon or online using DataSync.

Running applications in disconnected environments and connected edge locations can be challenging. This is because these locations often lack the space, power, and cooling needed for data center information technology (IT) equipment. 

Snowcone stores data securely in edge locations and can run edge computing workloads that use AWS IoT Greengrass or EC2 instances. Snowcone devices are small, so you can carry one in a backpack or fit it in tight spaces for Internet of Things (IoT), vehicular, or drone use cases.

#### Snowball Edge
Snowball Edge is a data migration and edge computing device that comes in two device options: Compute Optimized and Storage Optimized.

**Snowball Edge Storage Optimized** devices provide 24 virtual CPUs (vCPUs) of compute capacity, coupled with 80 terabytes of usable block or Amazon S3 compatible object storage. It is well-suited for local storage and large-scale data transfers. In addition, you can order Snowball Edge Storage Optimized devices for data transfer-only jobs, without compute capacity activated, at a reduced cost.

**Snowball Edge Compute Optimized** devices provide 52 vCPUs and 42 terabytes of usable block or object storage. They include an optional graphics processing unit (GPU) for use cases such as advanced machine learning and full motion video analysis in disconnected environments. 

Customers can use these two options for data collection, machine learning and processing, and storage in the following environments before shipping the device back to AWS:

Intermittent connectivity (such as manufacturing, industrial, and transportation)
Extremely remote locations (such as military or maritime operations) 
These devices can also be rack mounted and clustered together to build larger, temporary installations.

#### Snowmobile
Snowmobile moves up to 100 petabytes (PBs) of data in a 45-foot-long ruggedized shipping container pulled by a semi-trailer truck. Snowmobile is ideal for multi-petabyte or exabyte-scale data migrations. 

A Snowmobile arrives at the customer site and appears as a network-attached data store for secure, high-speed data transfer. After data is transferred to Snowmobile, it is driven back to a Region, and the data is uploaded into Amazon S3.

Snowmobile is tamper resistant, waterproof, and temperature controlled. It is made up of multiple layers of logical and physical security. For example, security includes encryption, fire suppression, dedicated security personnel, Global Positioning System tracking, alarm monitoring, 24/7 video surveillance, and an escort security vehicle during transit.

#### Snow Family comparison

| Description | Snowcone | Snowball Edge     | Snowball Edge     | Snowmobile |
|             |          | Storage Optimized | Compute Optimized |            |
| ----------- | -------- | ----------------- | ----------------- | ---------- |
| Usable Hard Disk Drive (HDD) Storage | 8 TB usable HDD | 80 TB usable HDD | N/A | Customized configurations up to 100 PB |
| Usable Solid-State Drive (SSD) Storage | 14 TB | 1 TB SSD | 28 TB | N/A |
| Usable Compute | 2 vCPUs | 40 vCPUs | 104 vCPUs | N/A |
| Usable Memory | 4 GB | 80 GB | 416 GB | N/A |
| Device size L x W x H | 227 x 148.6 x 82.65 millimeter (mm) | 548 x 320 x 501 mm | 548 x 320 x 501 mm | 45-foot shipping container |
| Device Weight | 4.5 pounds 2.1 kilograms (kg) | 49.7 pounds 22.54 kg | 49.7 pounds 22.54 kg | N/A |
| Storage Clustering | No | Yes 5–10 nodes | Yes 5–10 nodes | N/A |
| 256-bit Encryption | Yes, 256-bit | Yes, 256-bit | Yes, 256-bit | Yes, 256-bit |
| Health Insurance Portability and Accountability Act (HIPPA) Compliant | No | Yes, eligible | Yes, eligible | Yes, eligible |

#### [Snow Family](https://aws.amazon.com/snow/?nc2=h_ql_prod_mt_sno)

#### [Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/specifications.html)

### Transfer Family Overview
#### Sharing files
Organizations across every industry, vertical market, and organization type share critical files with their vendors, partners, and other organizations. In addition to the capability to transfer files, you need convenient access to the transferred files so that you can securely and cost-effectively process the data for a variety of use cases.

AWS has seen that 39 percent of business data that is uploaded to the cloud is used for file sharing purposes. These shared files are then supplied to downstream applications for further use and processing. Close integration with other services is critical to support machine learning, data analytics, and other application and workflow processes.

Transfer files securely and cost-effectively with the AWS Transfer Family.

#### What is Transfer Family?
Transfer Family offers you a managed file transfer (MFT) service used for transferring files over common file transfer protocols. Files are transferred directly into and out of AWS storage services. With Transfer Family related tools and resources, you can seamlessly migrate, automate, and monitor your file transfer workflows. 

With Transfer Family, you maintain existing client-side configurations for authentication, access, and firewalls. This means your existing transfer solution configurations, clients, and processes continue to operate for your customers, partners, and internal teams, or their applications.

#### Supported transfer protocol
Transfer Family currently supports these protocols to meet your transfer workflow requirements:
* **FTP**: Network protocol for transferring files without encryption over TCP/IP
* **FTP Secure (FTPS)**: File transfer protocol over TCP/IP with SSL/TLS encryption
* **SSH or Secure File Transfer Protocol (SFTP)**: File transfer protocol over SSH using industry standard strong encryption algorithms
* **Applicability Statement 2 (AS2)**: HTTPS-based protocol to transmit messages (especially Electronic Data Interchange messages) safely, cheaply, and quickly 

### Self-managed file transfer workload challenges
Organizations can use the technology platform MFT to reliably exchange electronic data between systems and people in a secure way to meet compliance needs. These data movements can be both internal and external to an enterprise and include various types, including sensitive, compliance-protected, or high-volume data.

Managing and maintaining these systems can be both time consuming and costly. Like many application and process workloads, MFT solutions vary from very limited use during the day or week to peak periods that can exceed the allocated resources for processing and support.

#### Challenges
* 24/7 operations and support
* High availability and on-demand scaling
* Maintenance for capacity and performance
* Patching and auditing for compliance
* End-user access provisioning
* Limited visibility into the exchanged data
* Dealing with bad actors, such distributed denial of service (DDoS) attacks and vulnerability scanners

MFT services have the same challenges as other self-managed services. Maintenance, operations, and systems and end-user support are required to support the systems and workflows on a 24/7 basis. 

### How Transfer Family works
As a managed service, the Transfer Family service incorporates features and services to minimize or alleviate most of the challenges with self-managed file transfer solutions. 

#### Secure data-in-transit encryption
Transfer Family uses secure transfer protocols to secure data in transit.

Transfer Family supports securing your data in transit between AWS and the client for all secure network transfer protocols. Each secure protocol manages the security between the client and the server. SFTP and FTPS use TLS, which is a cryptographic protocol designed to provide communications security over a computer network. 

With FTP, which does not encrypt the data in transit, Transfer Family permits the protocol over secure connectivity only. This helps to prevent any unauthorized or unintended bad actors from intercepting and reading data in transit.

#### Managed transfer servers
As part of the Transfer Family service, AWS manages the server instances (servers) without your intervention. As needed, AWS adds or removes resources to meet your workflow requirements. In addition, AWS manages updating and patching software and hardware to keep them current and operating securely and efficiently. All AWS managed services are designed for reliability and for high availability.

Transfer Family service is accessed using endpoints that you deploy in your account. An endpoint is the URL of the entry point for an AWS web service. Unlike standard AWS endpoints, Federal Information Processing Standard (FIPS) endpoints use a TLS software library that complies with FIPS 140-2. These endpoints might be required by enterprises that interact with the United States government. FIPS endpoints are available in selected Regions. 

Endpoints are deployed in Availability Zones (AZs) within a Region. You can deploy endpoints in up to three AZs per Region per server for high availability within a Region. Endpoints are deployed in an Amazon VPC. Additionally you can deploy SFTP using a public endpoint.

#### AWS storage services
Transfer Family uses two of the most popular AWS storage services to store your files. You can choose between **Amazon S3 for object-based storage** or **Amazon EFS for POSIX-compliant Network File System (NFS) storage**.

With the choice of AWS storage services, you can customize your file transfer solution to meet your use-case requirements. After your data is in your S3 buckets or EFS file systems, you can fully use the data with other applications or services in your AWS account.

#### Integration with other services
Transfer Family integrates with a variety of other services to create a complete managed file transfer solution to meet your workflow requirements. Some integration examples include the following:
* Integration with different identity and access management services such as Microsoft Active Directory (AD), Lightweight Directory Access Protocol (LDAP), and IAM
* Integration with CloudWatch to monitor service metrics, and integration with CloudTrail to log and audit service activity events
* Integration with Amazon Route 53 to manage Domain Name System (DNS) configuration from your AWS account and DNS services outside of AWS

### Transfer Family features
#### Seamless migration
The migration to Transfer Family is a seamless lift and shift off of existing datasets. You can seamlessly migrate your workflows by redirecting your DNS from on premises to the AWS Cloud.  

You can use your existing file transfer client configurations and workflows that are already built in place. The migration is transparent to both your internal and external clients.

#### Fully managed
AWS transparently operates and manages all of the compute, storage, and other infrastructure necessary to maintain high availability and performance for your endpoint. Your endpoint is designed to be available 24 hours a day, 7 days a week, 365 days a year. You get full redundancy across multiple AZs within a Region.

#### Secure and compliant
Transfer Family is both secure and compliant with secure transfer standards. Transfer Family supports FTPS, SFTP, and AS2 secure protocols and permits FTP only over secure connections.

Transfer Family helps you protect your business-to-business file exchanges with data encryption and scanning, audit trails, and compliance certifications including HIPAA, FedRAMP, and more.

#### Native integration
Transfer Family natively integrates with AWS services, including CloudWatch, CloudTrail, IAM, Amazon API Gateway, Route 53, Amazon S3, and Amazon EFS.

With your data in Amazon S3 or Amazon EFS storage, you can further integrate your workflows into other workflows that you implement in AWS.

#### Cost effective
Transfer Family is cost-effective. Many customers spend a lot of money to manage their managed transfer service on premises, either through their own DIY solutions or through commercial licenses.

With Transfer Family, you pay as you go for resources used instead of building out and maintaining servers, software, and infrastructure in advance.

#### Simple to use
An intuitive user interface and API makes it convenient for you to configure your SFTP, FTPS, FTP, or AS2 endpoint and set up client access. 

For internal and external users, the service supports commonly used protocols and scripting file transfers. Users don’t need to change their behavior to continue sharing data with you in the cloud.

#### Additional features and benefits
##### Elastic resources
Transfer Family can meet the needs of your dynamic workloads with elastic compute infrastructure. Built-in auto scaling means that you never need to worry about provisioning additional resources if your data loads grow over time. You don't need to worry if workloads spike during certain hours of the day or days of the month.

##### Multiple user authentication methods support
Transfer Family supports common user authentication systems, including Microsoft AD and LDAP. Alternatively, you can also choose to store and manage users’ credentials directly within the service. By connecting your existing identity provider to Transfer Family, you can be sure that your external users continue to have the correct, secure level of access to your data resources without disruption.

##### Fine-grained authorization
Authenticate and authorize individual line-of-business users with fine-grained access controls that level your operations, administration, and management workflows.

##### Data stored natively in AWS storage services
Store the files you exchange as objects in your S3 bucket or EFS file system so that you can extract business insights faster. The key piece that makes this exchange possible is that Transfer Family stores your data natively in Amazon S3 or Amazon EFS, while preserving relevant file metadata.

For example, when your files are stored in Amazon S3, you can use Amazon Translate to make process documents more tailored for international audiences. You can also use Amazon Comprehend to extract relationships and insights from text files, or you can use Amazon Athena to query CSV files to analyze historical data. Similarly with files in Amazon EFS, you can directly integrate your enterprise resource planning system to access these files on arrival from your business partners.

##### Familiar and comprehensive AWS management services
With Transfer Family, you can use IAM for security and identity management and CloudWatch for monitoring and events to start post-upload processing. You can use AWS KMS, Amazon S3 server-side encryption, or Customer Managed Keys with Amazon EFS to control encryption at rest.

Additionally, CloudTrail helps you meet compliance requirements with granular auditing of user and API activity.

##### Low-code workflow automation
Save time with low code, managed workflows that orchestrate common file processing steps and automatically detect data anomalies or errors. Transfer Family supports managed workflows for file processing of file transfers over SFTP, FTPS, and FTP. With managed workflows, you can create, automate, and monitor post-transfer file processing. 

Using this feature, you can securely and cost effectively meet your compliance requirements for business-to-business (B2B) file exchanges by coordinating all the necessary steps required for file processing. In addition, you benefit from end-to-end auditing and visibility.

### Knowledge Check
#### An organization has begun migrating their on-premises data to cloud storage. Their intent is to move the terabytes of data they have on premises to the cloud using internet connections. Which AWS Service would be the ideal solution for the organization to transfer their data?
**AWS DataSync.**

* AWS Snowmobile transfers physical media and does not use internet connections for migration.
* AWS Snowball uses a physical device rather than internet connections for migration.
* Amazon S3 Transfer Acceleration is a migration feature at the S3 bucket-level. There is not bucket-level data migration in this scenario

#### A network administrator is discussing viability of using AWS Transfer Family services for their organization's cloud migration with an AWS consultant. The network administrator wants to know which transfer protocols are supported by Transfer Family. Which protocols would be included in the consultant's response? (Select THREE.)
**FTP**, **FTPS**, **Applicability Statement 2 (AS2)**.

* Transfer Family does not currently support SSL and Trivial FTP (TFTP).

#### A large company has decided to begin migrating petabytes of data to the cloud. One requirement they have is that their data must be migrated using physical media instead of internet connections. Which AWS service can the organization use to transfer their data?
**AWS Snowmobile.**

* Snowmobile moves up to 100 petabytes (PBs) of data in a 45-foot-long ruggedized shipping container pulled by a semi-trailer truck, transferring the physical media instead of using internet connections.
* AWS DataSync, AWS Transfer Family, and Amazon S3 Transfer Acceleration use internet connections.

### Summary
* Describing the need for data migration into the cloud
* Describing the benefits of migrating data into the cloud
* Identifying cloud migration strategies
* Describing the features and benefits of Datasync, Snow Family, Transfer Family, and AWS S3 Transfer Acceleration
* Identifying use cases for AWS data migration services

#### Migrating data into the cloud
A cloud migration is the process of moving any workload or application into the cloud from:
* An on-premises environment
* A hosting facility
* Another cloud environment

The three-phase migration process is designed to help your organization approach a migration of applications. Each phase is an iterative process that contains a common component of a successful migration.

##### ASSESS
At the start of your journey, you assess your organization’s current readiness for operating in the cloud. Most importantly, you want to identify the desired business outcomes and develop the business case for migration.

##### MOBILIZE
Create a migration plan and refine your business case. Address gaps in your organization’s readiness that were uncovered in the assess phase, and focus on building your baseline environment (the “landing zone”), driving operational readiness, and developing cloud skills.

##### MIGRATE AND MODERNIZE
During the migrate and modernize phase, each application is designed, migrated, and validated. 

#### AWS services for data migration
AWS offers a wide variety of services and partner tools to help you migrate your data sets, whether they are files, databases, machine images, block volumes, or even tape backups. 

##### AWS DataSync
AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between storage systems and services. DataSync can copy data to and from Amazon S3 buckets and Amazon EFS file systems, as well as NFS file servers, SMB file servers, and object storage systems, among others.

##### AWS Snow Family
The AWS Snow Family uses purpose-built devices to move petabytes of data offline. Snow Family devices have computing resources to collect and process data at the edge. All data moved to AWS Snow Family devices is automatically encrypted with 256-bit encryption keys that are managed by the AWS Key Management Service (KMS).

##### AWS Transfer Family
AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services. Transfer Family provides access to a file transfer protocol-enabled server in AWS without the need to run any server infrastructure, enabling you to migrate file transfer-based workflows to AWS while maintaining end users' clients and configurations as is.

##### Amazon S3 Transfer Acceleration
Amazon S3 Transfer Acceleration is a bucket-level feature that enables fast, easy, and secure transfers of files over long distances between a client and an S3 bucket. It is designed to optimize transfer speeds from across the world into S3 buckets, taking advantage of the globally distributed edge locations in Amazon CloudFront. As the data arrives at an edge location, the data is routed to Amazon S3 over an optimized network path.

### Additional Resources
#### [Snow Family](https://aws.amazon.com/snow/?nc2=h_ql_prod_mt_sno)

#### [Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/specifications.html)

## Hybrid Cloud and Edge Storage
### Pre-assessment
#### Which statement accurately describes hybrid cloud storage?
**Hybrid cloud is an information technology (IT) infrastructure design that integrates an organization’s on-premises IT resources with a third-party cloud provider infrastructure and resources.**

Hybrid cloud infrastructure design does not function to integrate local storage with local servers.

#### Which statement accurately describes AWS Storage Gateway?
**Storage Gateway is an AWS service that facilitates hybrid cloud usage.**

The Storage Gateway service facilitates hybrid cloud storage use cases. It integrates with other AWS services for storage, backup, management, and security while still integrating with on-premises environments.

#### Which AWS Storage Gateway type supports data ingestion to data lakes in AWS?
**Amazon S3 File Gateway.**

Amazon S3 File Gateway supports data lakes, backups, and machine learning workflows. Users can store file data as objects in Amazon S3 cloud storage using file protocols such as Network File System and server message block. Objects written through Amazon S3 File Gateway can be directly accessed in Amazon S3.

### Benefits of Hybrid Cloud and Edge Storage
Hybrid cloud is an IT infrastructure design that integrates a company’s internal IT resources with third-party cloud provider infrastructures and services. With hybrid cloud, you can store your data and run your applications across multiple environments. Your hybrid cloud environment helps you provision, scale, and centrally manage your compute resources.

### Hybrid cloud with AWS
AWS offers a broad set of cloud computing services, ranging from IT infrastructure services to business web services. Examples include compute, storage, database, analytics, networking, mobile, developer tools, management tools, IoT, security, and enterprise applications. These cloud computing resources are used in workloads ranging from running existing enterprise applications to deploying and managing new applications.

Not all workloads are the same. Some workloads cannot quickly migrate to the cloud. Perhaps they need to work with large local datasets, share data with on-premises applications with single-digit-millisecond latency, or meet data residency requirements. In these use cases, constantly passing data to and from the cloud is too slow, too resource intensive, or not permitted. Hybrid cloud can be a useful alternative option for such workloads.

#### When to consider hybrid cloud
The following four use cases summarize several key situations for when to consider hybrid cloud:
* You have an existing application that must run on premises, that uses databases or files, or that must perform backups, and you want to use cloud resources and scalability.
* You need fast, local access to data, but you also want to take advantage of cloud compute and analytics engines.
* You have years worth of security and compliance requirements, supported by processes and procedures in disparate systems on premises. And you want to use cloud management and monitoring capabilities, ideally from a single pane of glass.
* You have many physical locations to manage with data and applications, and you want reliable connectivity and simplified maintenance.

#### What hybrid cloud can do for you
* Accelerate digital transformation by incorporating AWS infrastructure and services incrementally along your cloud journey.
* Improve IT and developer productivity by providing infrastructure, services, and tools that support their workflows and goals.
* Deliver differentiated services and experiences by using AWS services to create and deliver interactive and responsive operations faster.

#### Hybrid cloud storage
*Hybrid cloud storage* means that you can use your data on premises and store it durably in AWS Cloud storage services. You can access different data storage types such as files, volumes, and virtual tapes that are stored in the AWS Cloud.

Hybrid cloud storage in AWS means more than just extending your data center to the cloud. It means that you can benefit from unlimited storage, existing compliance certifications, multilayered security, and the endless possibilities provided by the AWS services.

With Storage Gateway, you can create hybrid cloud solutions and have on-premises data centers and applications use storage and services in the cloud. This way, you can take advantage of the durable low-cost storage, security, monitoring, and analytics services that AWS provides. 

#### Edge storage
The data that originates at the periphery of your network is susceptible to limited or no connectivity and issues because of increased latency. To address these issues, edge storage is placed as close as possible to the information that is generated in that network peripheral zone. Because of the nature of the locations they service, edge storage is often ruggedized, capable of withstanding environmental factors that wouldn't normally be found in a controlled environment like a data center. AWS has developed a number of services that are tailored to assist with your workload requirements.

Snow Family can be used to help your organization run operations in locations where lack of consistent network connectivity would normally be a limiting factor. Snowcone and Snowball Edge can help you access the storage and compute power of the AWS Cloud locally and cost effectively in places where connecting to the internet might not be an option.

##### Snowcone
Snowcone is a portable, rugged, and secure device for edge computing and data transfer. You can use a Snowcone device to collect, process, and move data to the AWS Cloud, either offline by shipping the device to AWS, or online by using DataSync.

Snowcone is available in two flavors:
* Snowcone – Snowcone has two vCPUs, 4 GB of memory, and 8 TB of HDD-based storage.
* Snowcone SSD – Snowcone SSD has two vCPUs, 4 GB of memory, and 14 TB of SSD-based storage.

With two CPUs and terabytes of storage, a Snowcone device can run edge computing workloads that use EC2 instances and store data securely.

##### Snowball Edge
Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities. Snowball Edge can do local processing and edge-computing workloads in addition to transferring data between your local environment and the AWS Cloud.

Each Snowball Edge device can transport data at speeds faster than the internet. This transport is done by shipping the data in the appliances through a regional carrier. The appliances are rugged, complete with e-ink shipping labels. Snowball Edge devices have three options for device configurations—Storage Optimized, Compute Optimized, and Compute Optimized with GPU.

### Hybrid Cloud Storage with Storage Gateway
### AWS Storage Gateway
The Storage Gateway service facilitates hybrid cloud storage use cases. It integrates with other AWS services for storage, backup, management, and security while still integrating with on-premises environments. 

Storage Gateway helps you store your on-premises data in the cloud, where you can take advantage of additional AWS Cloud services to help monitor and manage it:
* **Storage** – Connect to storage services such as Amazon S3, Amazon S3 Glacier Flexible Retrieval, Amazon S3 Glacier Deep Archive, Amazon FSx, AWS Backup, and Amazon EBS.
* **Management and monitoring** – Use the Storage Gateway management console to manage and monitor Storage Gateway and its associated resources. Also use other AWS services, such as the following:
 * IAM to secure access to the service and resources
 * AWS KMS for encrypting data
 * CloudTrail for logging account activity
 * CloudWatch for monitoring
 * Amazon EventBridge for monitoring alarms

#### Key features and benefits
With Storage Gateway, you can bring your data into AWS for processing in the cloud. You can also back up, archive, and tier your storage or add it to your on-premises environment to help you meet your business and regulatory compliance requirements.

#### Architecture and end-to-end data flow
Storage Gateway consists of **in-cloud** and **on-premises** components. The component that deploys on premises is called a Storage Gateway appliance.

##### On-premises environments that benefit from cloud storage
* Windows or Linux file server or user workstation
* Backup server
* Storage area network (SAN) system or network-attached storage (NAS) device that must be expanded

##### Standard protocols
With standard storage protocols, your on-premises environment can access cloud storage much like local storage is accessed. These include the following:
* NFS
* SMB
* Internet Small Computer Systems Interface (iSCSI)
* iSCSI virtual tape library (VTL)

##### Storage Gateway appliance
The local appliance connects to Storage Gateway in the cloud securely over the internet or private networking. It is deployed on premises with a local cache, providing low-latency access to frequently accessed data.

Deployment options include VMware, Microsoft Hyper-V, Linux Kernel-based Virtual Machine (KVM), an AWS managed hardware appliance, and Amazon EC2.

##### Secure and optimized uploads
Connect to AWS over the internet using HTTPS. 

You can also use Direct Connect for an even more secure and private connection.

You can use AWS virtual private network services for a private and dedicated network connection from your premises to the AWS Cloud.

##### Storage Gateway service
Storage Gateway is an AWS managed service that provides hybrid cloud solutions:
* It integrates your on-premises environments with AWS storage.
* Gateway types include Amazon S3 File Gateway, Amazon FSx File Gateway, Tape Gateway, and Volume Gateway.

##### Storage
With Storage Gateway, you can connect to and use cloud storage services such as Amazon S3, S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, Amazon EBS, FSx for Windows File Server, and AWS Backup.

##### Security, management, and monitoring
Storage Gateway integrates with other AWS services for security, management, and monitoring. 

This includes services such as AWS KMS, IAM, CloudTrail, and CloudWatch.

#### Storage protocols
Storage Gateway uses standard storage protocols, namely, NFS, SMB, iSCSI, or iSCSI VTL to connect your local production or backup applications to AWS Cloud storage. Its protocol conversion and device emulation make it possible for you to do the following:
* Access block data on volumes managed by Storage Gateway along with Amazon S3.
* Store files as native S3 objects or in fully managed cloud file shares with Amazon FSx for Windows File Server.
* Keep virtual tape backups online in a VTL backed by Amazon S3, or move the backups to a tape archive tier on S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive. 

#### Low-latency access to your data
The Storage Gateway appliance provides your applications with low-latency access to data by maintaining a cache of recently written or read data. Data is removed from the cache according a least recently used algorithm.

**As your applications write data to the AWS storage,** 
* the gateway first stores the data in the on-premises disks that are used for cache storage. 
* Then, the gateway uploads the data to AWS. 
* The cache store acts as the on-premises durable store for data. If your application requests data, the gateway first checks the cache storage for the data before checking AWS. 

#### Optimized data transfers
Storage Gateway uses optimization such as multi-part management, automatic buffering, and delta transfers. Data compression is applied for block and virtual tape data. The data transfers are optimized to reduce cost and the amount of data that is transferred into and out of AWS.

#### Security and compliance
Storage Gateway supports security features, access control, and security compliance certifications. Data is encrypted in transit and at rest. Your data at rest is encrypted by default using Amazon S3 server-side encryption (S3-SSE) keys. Alternatively, Storage Gateway integrates with AWS KMS, so you can choose to encrypt your data using customer managed encryption keys. By integrating with IAM, you manage and secure access to your data.

### Storage Gateway types
To support numerous hybrid cloud use cases, the Storage Gateway service provides four different types of gateways: Amazon S3 File Gateway, Amazon FSx File Gateway, Tape Gateway, and Volume Gateway. They seamlessly connect on-premises applications to cloud storage and cache data locally for low-latency access.

#### AMAZON S3 FILE GATEWAY
Amazon S3 File Gateway provides native file access to Amazon S3 for backups, archives, and ingest for data lakes.

Amazon S3 File Gateway presents a file-based interface to Amazon S3, which appears as a network file share. With it, you can store files that support your latency-sensitive applications and workloads that require local caching and file protocol access. Amazon S3 File Gateway moves your file data into an object format, which is highly durable and cost efficient.

#### AMAZON FSX FILE GATEWAY
Amazon FSx File Gateway provides native file access to Amazon FSx for on-premises group file shares and home directories.

Amazon FSx File Gateway optimizes on-premises access to Windows file shares on Amazon FSx, which helps you to access FSx for Windows File Server data with low latency and conserve shared bandwidth. A local cache of frequently used data that you can access is stored, which provides faster performance and reduced data transfer traffic. Amazon FSx File Gateway stores your data natively as files instead of as objects.

#### TAPE GATEWAY
Tape Gateway replaces physical tape infrastructure using Amazon S3 archive tiers for long-term retention.

Tape Gateway is a cloud-based VTL. It presents your backup application with a VTL interface consisting of a media changer and tape drives. You can create virtual tapes in your VTL using the Storage Gateway console. Your backup application can read data from or write data to virtual tapes by mounting them to virtual tape drives using the virtual media changer. 

Virtual tapes are discovered by your backup application using its standard media inventory procedure. Virtual tapes are available for immediate access and are backed by Amazon S3. You can also archive tapes. Archived tapes are stored in S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive.

#### VOLUME GATEWAY
Volume Gateway provides block storage volumes with snapshots, AWS Backup integration, and cloud recovery.

Volume Gateway provides an iSCSI target, with which you can create block storage volumes and mount them as iSCSI devices from your on-premises or Amazon EC2 application servers. The Volume Gateway runs in either a cached or stored mode:
* In the cached mode, your primary data is written to Amazon S3 while retaining your frequently accessed data locally in a cache for low-latency access.
* In the stored mode, your primary data is stored locally and your entire dataset is available for low-latency access while asynchronously backed up to AWS.

In either mode, you can take point-in-time copies of your volumes, which are stored as Amazon EBS snapshots in AWS. With this feature, you can make space-efficient versioned copies of your volumes for data protection, recovery, migration, and various other copy data needs.

### Choosing the right file gateway
Storage Gateway provides two gateway types for storing files that support your latency-sensitive applications and workloads that require local caching and file protocol access. If you want to move your file data into an object format that is highly durable and cost efficient, use Amazon S3 File Gateway. If you want to keep it stored natively as file data, use Amazon FSx File Gateway.

**Amazon S3 File Gateway** supports data lakes, backups, and ML workflows. You can store file data as objects in Amazon S3 cloud storage using file protocols such as NFS and SMB. Objects written through Amazon S3 File Gateway can be directly accessed in Amazon S3.

**Amazon FSx File Gateway** is a solution for replacing on-premises NAS, such as end-user home directories and departmental or group servers, with cloud storage. It facilitates user or team file shares and file-based application migration shares in FSx for Windows File Server, using the SMB protocol. Files written through FSx File Gateway can be directly accessed in FSx for Windows File Server.

### Solution deploys as a stateless gateway appliance
The gateway is straightforward to deploy and can use your existing virtual infrastructure and hypervisor investments. It can also be installed in your data center or remote offices as a hardware appliance. The gateway software running as a virtual machine (VM) or on the hardware appliance is stateless, so you can conveniently create and manage new instances of your gateway as your storage needs evolve.

The Storage Gateway deployment consists of two components: **a cloud component** and **an on-premises component** called **the gateway appliance**.

The gateway appliance that you use depends on the storage solution that you require and where you will be deploying the gateway appliance.

The gateway appliance will need to be hosted, use a local cache, and securely connect to the Storage Gateway service in the cloud for native data storage in AWS.

#### Host platform options
Deployment options include the following:
* Download, deploy, and activate the Storage Gateway VM image on any of the supported host platforms.
* Create an EC2 instance to deploy your gateway in the AWS Cloud.
* Order, deploy, and activate a Storage Gateway hardware appliance or in AWS as an Amazon EC2 instance.

Storage Gateway provides public, Amazon VPC, and FIPS service endpoints. This provides you with options to deploy and connect your gateway to Storage Gateway in a framework that best suits your networking and security needs. You can connect a gateway to the service either using public internet or through Direct Connect.

#### A quick look at Storage Gateway
Some of your applications may need to remain on premises for performance or compliance reasons, or they may simply be too complex to move completely into the cloud. 

While the cloud offers a large variety of services that can help modernize your IT infrastructure, you may also be considering a gradual transition to the cloud while still wanting to benefit from cloud capabilities in your data center. 

AWS Storage Gateway is a fast, simple way to get started with using the cloud from your data centers, remote offices, and edge locations. Storage Gateway is a hybrid cloud storage service that provides low-latency, on-premises access to virtually unlimited cloud storage. Your file, database, and backup applications can continue to run without changes. And once your data is safely and securely in AWS, it's available for all your current and future cloud initiatives since it can be easily accessed and processed by many other AWS services. 

In just minutes, you can be up and running in the cloud using AWS Storage Gateway. Using Storage Gateway, your on-premises applications can access data stored in the cloud via standard storage protocols, so there's no need to change application code. Storage Gateway works as a file share, as a virtual tape library, or as a block storage volume. Applications write data to the Amazon S3 File Gateway as files, which are stored in Amazon S3 as objects. Applications can also write data as files to the Amazon FSx File Gateway, which are stored in fully managed file shares in Amazon FSx for Windows File Server. The Tape Gateway presents a virtual tape library on your local network and is compatible with all major backup software. And the Volume Gateway attaches to your application servers as iSCSI block storage. No matter which type of gateway you're using, data is cached locally and moved to the cloud with optimized data transfers. 

Many Storage Gateway customers begin to use AWS by moving backups to the cloud, shifting on-premises storage to cloud-backed file shares, and ensuring low latency access for on-premises applications to access and process cloud data. It has never been easier to move to the cloud. And AWS Storage Gateway is a fast and powerful way to get started. To learn more about each Storage Gateway type and to see how customers just like you are leveraging secure, durable, and virtually unlimited cloud storage, visit the Storage Gateway website at [aws.amazon.com/storagegateway](https://aws.amazon.com/storagegateway/).

### Knowledge Check
#### A consultant is working with a non-governmental organization that spends a large amount of time operating in remote areas that have little to no network infrastructure. Which AWS service will allow them to collect, process, and transfer data to AWS?
* **AWS Snowcone**
* AWS Snowmobile
* AWS Transfer Family
* AWS DataSync

**Snowcone** can help users access the storage and compute power of the AWS Cloud locally and cost effectively in edge locations where connecting to the internet might not be an option.

The other options are incorrect because of the following: 
* Snowmobile is a solution for transporting large amounts of data (petabytes) using physical media.
* Transfer Family relies on network connectivity to transfer data.
* DataSync relies on network connectivity to transfer data.

#### Which statement about Amazon S3 File Gateway is true?
* Amazon S3 File Gateway provides a Small Computer Systems Interface (iSCSI) target for users to create block storage volumes and mount them as iSCSI devices.
* Amazon S3 File Gateway replaces physical tape infrastructure using Amazon S3 archive tiers.
* **Amazon S3 File Gateway presents a file-based interface to Amazon S3, which appears as a network file share.**
* Amazon S3 File Gateway is a solution for replacing on-premises network-attached storage (NAS) with cloud storage.

The other options are incorrect because of the following:
* Volume Gateway provides an iSCSI target for users to create block storage volumes and mount them as iSCSI devices.
* Tape Gateway replaces physical tape infrastructure using Amazon S3 archive tiers.
* Amazon FSx File Gateway is a solution for replacing on-premises NAS with cloud storage.

#### While reviewing their requirements for implementing AWS Storage Gateway, a company has determined that their solution will need to support data lakes on Amazon S3. Which type of Storage Gateway should they choose?
* Amazon FSx File Gateway
* **Amazon S3 File Gateway**
* Volume Gateway
* Tape Gateway

Amazon S3 File Gateway supports data lakes, backups, and machine learning workflows. Users can store file data as objects in Amazon S3 cloud storage using file protocols such as Network File System and server message block. Objects written through Amazon S3 File Gateway can be directly accessed in Amazon S3.

The other options are incorrect because of the following: 
* Amazon FSx File Gateway is a solution for replacing on-premises network-attached storage, such as end-user home directories and departmental or group servers, with cloud storage. 
* Volume Gateway does not function as a file gateway.
* Tape Gateway does not function as a file gateway

### Summary
* Defining and describing the need for hybrid cloud and edge storage
* Describing features and benefits of Storage Gateway
* Discussing how to use Storage Gateway and Snow Family for hybrid cloud and edge storage
* Describing how to use AWS at the edge (CloudFront)
* Describing how to use AWS for media storage

#### Hybrid cloud storage
Hybrid cloud enables you to benefit from nearly unlimited storage, existing compliance certifications, multilayered security, and the endless possibilities provided by the AWS services.

You can create hybrid cloud solutions that enable your on-premises data centers and applications to use storage and services in the cloud using Storage Gateway.

#### Edge storage
Edge storage allows you to address the data that originates at the periphery of your network where connectivity may be limited or non-existent. Edge storage devices are often ruggedized, capable of withstanding atypical environmental factors. Examples of edge storage include:
* AWS Snowcone
* AWS Snowball Edge

#### Storage Gateway
Storage Gateway is an AWS service that facilitates hybrid cloud storage use cases. It integrates with other AWS services for storage, backup, management, and security, while still integrating with on-premises environments. 

Storage Gateway provides four different types of gateways:
* **Amazon S3 File Gateway** - native file access to Amazon S3 for backups, archives, and ingest for data lakes.
* **Amazon FSx File Gateway** - native file access to Amazon FSx for on-premises group file shares and home directories.
* **Tape Gateway** - replaces physical tape infrastructure using Amazon S3 archive tiers for long-term retention.
* **Volume Gateway** - provides block storage volumes with snapshots, AWS Backup integration, and cloud recovery.

### Additional Resources
#### [Hybrid cloud with AWS](https://aws.amazon.com/hybrid/)

#### [Snowcone in Orbit](https://aws.amazon.com/blogs/aws/how-we-sent-an-aws-snowcone-into-orbit/)

## Working with Amazon S3
### Pre-assessment
#### Which type of storage is provided by Amazon S3?
* Block storage
* **Object storage**
* On-premises storage
* File storage

#### Which statement about Amazon S3 storage is true?
* **Data is stored in buckets, which are virtually unlimited in size.**
* Data is stored in buckets, each with a 100 TB limit.
* Data is stored in hierarchical folders.
* Data is stored in buckets, which can be in virtually unlimited amounts per account.

Amazon S3 bucket sized are virtually unlimited, eliminating the need to predetermine storage allocation like when creating storage volumes or partitions.

The other options are incorrect because of the following: 
* In Amazon S3, data is stored in buckets, which can be virtually unlimited in size.
* Amazon S3 does not use folders, and data is stored in a flat format rather than hierarchical.
* Amazon S3 buckets are limited to 100 per account, which can be expanded to up to 1,000 per account.

#### Which statements about bucket naming in Amazon S3 are true? (Select THREE.)
* **Bucket names must be unique across all of Amazon S3.**
* Bucket names cannot start with a lowercase letter or number.
* **Bucket names must be 3–63 characters long.**
* Bucket names can be formatted as an IP address (for example, 192.168.0.1).
* **Bucket names must start with a lowercase letter or number.**
* Bucket names must be unique only within each account.

**Bucket names must be unique across all of Amazon S3**, **Bucket names must be 3–63 characters long**, and **Bucket names must start with a lowercase letter or number**. 

The other response options are incorrect because of the following: 
* Bucket names must start with a lowercase letter or number.
* Bucket names cannot be formatted as an IP address.
* Bucket names must be unique

### Working with Amazon S3

### Object storage in Amazon S3
Object storage is a flat storage structure where objects are stored in buckets. Objects are any piece of data stored within a bucket. You can create a **pseudo folder structure** using **prefixes**. In Amazon S3 object storage, you can organize objects to imitate a hierarchy by using key name prefixes and delimiters. Prefixes and delimiters help you group similar items to visually organize and quickly retrieve your data. In the user interface, these prefixes give the appearance of a folder and subfolder structure, but in reality, the storage is still a flat structure. 

In the following image, you have a bucket called *getting-started-with-s3*. Inside the bucket, there is an object called *dolphins.jpg*. To organize and group the oceanography data for the external vendor, you created a logical hierarchy using the prefix ocean. Ocean looks like a subfolder, but this is only to help make the structure readable.

In reality, the key name of the dolphin object is a little longer, helping us locate the *ocean/dolphin.jpg* object. The object still sits in one single flat-storage structure.

```
https://getting-started-with-s3.s3-us-west-2.amazonaws.com/ocean/dolphins.jpg
```

### Bucket overview
Buckets are containers that hold objects. You can create up to 100 buckets in each AWS account by default. You can increase the bucket limit to a maximum of 1,000 buckets by submitting a service limit increase. Bucket sizes are virtually unlimited, so you don't need to allocate a predetermined bucket size the way you would when creating a storage volume or partition. 

An S3 bucket is a versatile storage option with the ability to host a static web site, retain version information about objects, and employ lifecycle management policies to balance version retention with bucket size and cost. 

### Bucket limitations
#### Bucket owner
Amazon S3 buckets are owned by the account that creates them and cannot be transferred to other accounts.

#### Bucket names
Bucket names are globally unique. There can be no duplicate names within the entire S3 infrastructure.

#### Bucket renaming
Once created, you cannot change a bucket name.

#### Permanent entities
Buckets are permanent storage entities and only removable when empty. Deleted bucket names become available for reuse by any account after 24 hours.

#### Object storage limits
Store unlimited objects in a single bucket, or across several buckets. Note that you can't create a bucket within another bucket (nesting buckets).

#### Bucket creation limits
You can create up to 100 buckets in each of your AWS accounts, and your account can be increased to a bucket limit of 1,000 buckets using a service limit increase request.

### Naming buckets
When naming buckets, carefully determine how you want to structure your bucket names and how they will function. Will you use them only for data storage or hosting a static website? Your bucket names matter to Amazon S3, and based on how you use the bucket, your bucket names and characters will vary. Bucket names are globally viewable and need to be DNS-compliant. 

Here are the rules to follow when naming your buckets. Bucket names must have the following characteristics:
* Be unique across all of Amazon S3
* Be 3–63 characters long
* Consist only of lowercase letters, numbers, dots (.), and hyphens (-)
* Start with a lowercase letter or number
* Not begin with xn-- (beginning February 2020)
* Not be formatted as an IP address (for example, 198.68.10.2)
* Use a dot (.) in the name only if the bucket's intended purpose is to host an Amazon S3 static website; otherwise do not use a dot (.) in the bucket name

### Object Overview
#### Amazon S3 Object Introduction
Amazon S3 is an object store that uses unique key-values to store as many objects as you want. You store these objects in one or more buckets, and each object can be up to 5 TB in size. 

An object consists of the following: Key, version ID, value, metadata, and access control information. The object key (or key name) uniquely identifies the object in a bucket. Object metadata is a set of name-value pairs. You can set object metadata at the time you upload it. After you upload the object, you cannot modify object metadata. The only way to modify object metadata is to make a copy of the object and set the metadata. 

#### What is an object?
An object is a file and any optional metadata that describes the file. To store a file in Amazon S3, you upload it to a bucket. When you upload a file as an object, you can set permissions on the object and any metadata.

#### What is a Key?
When you create an object, you specify the key name. The key name uniquely identifies the object in the bucket. It is the full path to the object in the bucket.

In Amazon S3, there is no hierarchy, as you would see in a file system. However, by using prefixes and delimiters in an object key name, the Amazon S3 console and the AWS SDKs can infer hierarchy and introduce the concept of folders. You do not get actual folders, what you get is a very long key name.

#### Version ID
Versioning is a means of keeping multiple variants of an object in the same bucket. You can use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket. You can easily recover from both unintended user actions and application failures. If Amazon S3 receives multiple write requests for the same object simultaneously; it stores all of the objects.

If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the object being stored. In one bucket, for example, you can have two objects with the same key, but different version IDs, such as the latest version of dolphins.jpg (version qNTCxBvI7p0pR39sw1sJhHyc59jx75HB) and the previous version of dolphins.jpg (version KWdgdZCncMiiPNs5LGHDz7zmf1QImseb).

#### Value
**Value (or size)** is the actual content that you are storing. An object value can be any sequence of bytes, meaning it can be the whole object or a range of bytes within an object that an application needs to retrieve. Objects can range in size from zero to 5 TB.

#### Metadata
This image shows three unique metadata values on the dolphins.jpg object.
For each object stored in a bucket, Amazon S3 maintains a set of system metadata. Amazon S3 processes this system metadata as needed. For example, Amazon S3 maintains object creation date and size metadata and uses this information as part of object management.

There are two categories of system metadata:
* Metadata such as object creation date is system controlled, where only Amazon S3 can modify the value.
* Other system metadata, such as the storage class configured for the object and whether the object has server-side encryption enabled, are examples of system metadata whose values you control.

#### Access control information
You can control access to the objects you store in Amazon S3. S3 supports both resource-based and user-based access controls. Access control lists (ACLs) and bucket policies are both examples of resource-based access control. 

### Organizing data using tags
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define to suit your company's requirements. Tags help you categorize your AWS resources or data in different ways. 

For example, you can define a set of tags for your objects that help you track project data or owner. Amazon S3 tags are key-value pairs and apply to a whole bucket or to individual objects to help with identification, searches, and data classification. Using tags for your objects helps you to effectively manage your storage and provide valuable insight on how your data is used. Newly created tags assigned to a bucket are not retroactively applied to its existing child objects. 

You can use two types of tags: bucket tags and object tags.

#### Bucket tags
One use case for bucket tags is to track storage costs by labeling your S3 buckets using cost allocation tags. A cost allocation tag is a key-value pair that you associate with an S3 bucket. After you activate cost allocation tags, AWS uses the tags to organize your resource costs on your cost allocation report. You can only use cost allocation tags on buckets and not on individual objects.

AWS provides two types of cost allocation tags: an AWS generated tag and user-defined tag. AWS defines, creates, and applies the AWS generated tag, createdBy, for you after an S3 CreateBucket event. You define, create, and apply user-defined tags to your S3 bucket. 

Once you have created and applied the user-defined tags, you can activate them by using the AWS Billing and Cost Management console for cost allocation tracking. Cost Allocation Tags appear on the console after enabling AWS Cost Explorer, AWS Budgets, AWS Cost and Usage reports, or legacy reports. 

After you activate the AWS services, they appear on your cost allocation report. You can then use the tags on your cost allocation report to track your AWS costs. 

Cost and Usage Reports are generated when using bucket tags.

#### Bucket tag set
Each S3 bucket has a tag set. A tag set contains all of the tags that are assigned to that bucket and can contain as many as 50 tags, or it can be empty.

Keys must be unique within a tag set, but values don't need to be unique. In the following image, the value ocean-life is listed twice in tag sets named project/ocean-life and topic/ocean-life. Because values don't need to be unique, these entries are fine. However, when attempting to add a second key called items, an error occurs because the key must be unique within the tag set.

Graphical interface for assigning keys and values to a bucket.

#### Object tags
Object tagging gives you a way to categorize and query your storage. You can add tags to an Amazon S3 object during the upload or after the upload. Each tag is a key-value pair that adheres to the following rules:
* An object can have up to 10 tags using unique keys.
* Tag keys can be up to 128 characters in length.
* Tag values can be up to 255 characters in length.
* Key and tag values are case sensitive.

#### Additional benefits
Adding tags to your objects offer benefits such as the following:
* Object tags provide fine-grained access control of permissions. For example, you can grant an IAM user permission to read-only objects with specific tags.
* Object tags provide fine-grained object lifecycle management in which you can specify a tag-based filter, in addition to a key name prefix, in a lifecycle rule.
* When using Amazon S3 analytics, you can configure filters to group objects together for analysis by object tags, key name prefix, or both prefix and tags.
* You can also customize CloudWatch metrics to display information by specific tag filters. 

### Region location
Amazon S3 is a globally viewable service. This means that in the console you do not need to specify a Region to view the buckets. Remember that when you initially create the bucket, you must choose a Region to indicate where you want the bucket data to reside. The Region you choose should be local to your users or consumers to optimize latency, minimize costs, and address regulatory requirements. 

For example, if your users reside in Europe, you will want to create buckets in one of the European Regions, such as Ireland, London, or Frankfurt, instead of in Asia or South America. This way the data is closer to your users and consumers, reducing latency and ensuring regulatory and country legal requirements.

#### Cross-Region Replication (CRR)
If you need data stored in multiple Regions, you can replicate your bucket to other Regions using CRR. With this, you can automatically copy objects from a bucket in one Region to a different bucket in another, separate Region. You can replicate the entire bucket, or you can use tags to replicate only the objects with the tags you choose.

#### Same-Region Replication (SRR)
Amazon S3 supports automatic and asynchronous replication of newly uploaded S3 objects to a destination bucket in the same Region. 

SRR makes another copy of S3 objects within the same Region, with the same redundancy as the destination storage class. This helps you to automatically aggregate logs from different S3 buckets for in-Region processing or configuring live replication between test and development environments. SRR helps you address data sovereignty and compliance requirements by keeping a copy of your objects in the same Region as the original.

### Amazon S3 Lifecycle Policies
Lifecycle management involves managing objects to ensure that they are stored cost effectively throughout their lifecycle, from data creation to retention. A lifecycle policy is a rule that moves objects between storage classes based on the object create date. With lifecycle management, objects automatically transition (move) to more economical storage classes as the content ages. Lifecycle management also helps you create rules to expire objects (delete them) based on the object’s age.

### Supported transitions
In an Amazon S3 Lifecycle configuration, you create rules to transition objects between storage classes for either cost management, retention requirements, or long-term compliance guidelines. These rules are configured based on your unique access patterns and business requirements. If you don't know the access patterns of your objects, or if your access patterns constantly change, your best option is to use the **S3 Intelligent-Tiering storage class**. This storage class is designed to optimize storage costs by automatically moving data to the most cost-effective access tier, based on access pattern, without manual intervention. 

Object data in a lifecycle policy can transition between storage classes in a downward, waterfall model. You can transition objects from the S3 Standard storage class to any other storage class but you cannot create a lifecycle rule that moves objects from any storage class back into to the S3 Standard storage class. 

* S3 Standard
* S3 Standard-IA
* S3 Intelligent-Tiering
* S3 One Zone-IA
* S3 Glacier Instant Retrieval
* S3 Glacier Flexible Retrieval
* S3 Glacier Deep Archive

### Object size constraints  
When using lifecycle policies to transition objects between storage classes, there are some considerations to remember when looking at the size of the objects. If the object is larger than 128 KB, there is a cost benefit for transitioning these larger objects from S3 Standard or S3 Standard-IA storage classes to the S3 Intelligent-Tiering. You also see cost benefits when moving large objects from S3 Standard storage class to the S3 Standard-IA or S3 One Zone-IA storage classes.

Amazon S3 **does not transition** objects between storage classes if they are **smaller than 128 KB** because it's not cost effective to do so.

#### Use cases
With S3 Lifecycle configuration rules, you can tell Amazon S3 to transition objects to less expensive storage classes or archive or delete them. How do you know which objects to consider moving? Here are a few of the primary reasons you might decide to implement lifecycle management:
* **Application logs**: If you upload periodic logs to a bucket, your application might need them for a week or a month. After that, you might want to delete them.
* **Limited time access**: Some documents are frequently accessed for a short period of time for specific projects or business needs and then infrequently accessed when the need is over. These files can be archived and then permanently deleted after their retention periods have expired. 
* **Archival**: Some companies import data to Amazon S3 primarily for archival purposes. For example, you might archive digital media, financial and healthcare records, raw genomics sequence data, long-term database backups, and data that must be retained for regulatory compliance.

#### Things to consider
##### Lifecycle configuration and versioning
You can add S3 Lifecycle configurations to both unversioned buckets and versioning-enabled buckets. 
You can define separate lifecycle rules for current and noncurrent object versions.

##### Object expiration
When an object reaches the end of its lifetime, Amazon S3 queues it for removal and removes it asynchronously. There might be a delay between the expiration date and the date at which Amazon S3 removes an object. You are not charged for storage time associated with an object that has expired. 

* **Versioning-enabled bucket**. If the current object version is not a delete marker, the lifecycle expiration action causes Amazon S3 to add a delete marker with a unique version ID. 
* **Versioning-suspended bucket**. In a versioning-suspended bucket, the expiration action causes Amazon S3 to create a delete marker with null as the version ID. This delete marker replaces any object version with a null version ID in the version hierarchy, which effectively deletes the object.
* For non-version-enabled buckets, when an object expires, the object is permanently deleted.

##### Minimums
It's not cost effective to transition objects smaller than 128 KB from S3 Standard and S3 Standard-IA to S3 Intelligent-Tiering.
Objects must remain for a minimum of 30 days in S3 Standard before they can transition to S3 Standard-IA and S3 One Zone-IA.
Objects in S3 Intelligent-Tiering, S3 Standard-IA, and S3 One Zone-IA storage are charged for a minimum storage duration of 30 days, and objects deleted before 30 days incur a pro-rated charge equal to the storage charge for the remaining days.

##### Configurations not supported
Lifecycle configuration on buckets with multi-factor authentication (MFA) is not supported.
Lifecycle actions are not captured by CloudTrail object-level logging. If logging is requried, you can use Amazon S3 Server access logs to capture S3 Lifecycle-related actions.
Your overall costs for Amazon S3 are comprised of cost for both storage and access. The lower storage classes charge less for storage, but more for access. Lifecycle policies are most effective when age and are accessed infrequently.

#### Multipart uploads
Multipart uploads accelerate the uploading of large objects by splitting them into parts that are then uploaded in parallel. You can upload these parts independently and in any order. If the transmission of any part fails, you can retransmit just that part without affecting other parts. Once uploaded, Amazon S3 assembles these parts and creates the object. 

##### WHEN TO USE
You should consider using multipart uploads if the following apply:
* Your object size is over 100 MB.
* You are uploading files over a network with inconsistent or erratic uptime.

To learn more about using multipart uploads, choose the following link: [Uploading and Copying Objects Using Multipart Upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

##### COST CONSIDERATIONS
If you initiate a multipart upload but the upload does not complete, the in-progress upload occupies storage space and incurs storage charges. After you initiate a multipart upload, Amazon S3 retains all the parts until you either complete or stop the upload. Throughout its lifetime, you are billed for all storage, bandwidth, and requests for this multipart upload and its associated parts. 

A Lifecycle rule can be configured to automatically remove incomplete uploads.

For more information about multipart upload pricing, choose the following link: [Multipart Upload and Pricing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html#mpuploadpricing) 

##### REMOVING INCOMPLETE UPLOADS
S3 Lifecycle policies:

In a lifecycle policy, you can use the *AbortIncompleteMultipartUpload* element to set a maximum number of  days for a multipart upload to remain in progress. If the upload doesn't complete within that specified number of days, it becomes eligible for a cancel operation. Amazon S3 stops the multipart upload and deletes the parts associated with the multipart upload.

See the *Delete expired delete markers or incomplete multipart uploads* section in the configuration.

#### Configuration elements example
##### Lifecycle rule name
This is the name of the individual Lifecycle rule.

An S3 Lifecycle configuration can have up to 1,000 rules.

##### Status
The Status value can be either Enabled or Disabled. If a rule is disabled, Amazon S3 doesn't perform any of the actions defined in the rule.

##### Scope of the rule
The Lifecycle rule can be run on an entire bucket or on a subset of objects based of Object tags or prefixes.

##### Prefix
This rule is run only on objects that contain the prefix  /logs. If you are not using prefixes to organize your data, you can run the rule on the entire bucket.

##### Transition rules
Objects with the prefix /logs will be move to the Standard-IA storage class 30 days after creation.

##### Second transition
The object will transition from Standard-IA and to S3 Glacier Flexible Retrieval 100 days after the object was created.

##### Lifecycle rule actions
In addition to moving objects, Lifecycle rules can be configured with a number of options, such as expiring current versions or permanently deleting old versions, and here the rule will delete expired delete markers and any incomplete multipart uploads so that you are not charged for the storage of expired or partial uploads.

### Amazon S3 Storage Classes
Amazon S3 offers a range of storage classes optimized for different use cases. Each storage class offers different minimum billable object size limits, storage duration, cost structure, lifecycle management, and retrieval times. Amazon S3 offers you eight different storage classes, so you can choose which class of storage best fits your use cases, your data access frequency, your regulatory compliance requirements, and numerous other considerations that are unique to your business requirements. You can optimize both the cost of the storage and the performance efficiency of your applications by choosing the correct storage class for your data.

#### Designed to fit data use requirements
Amazon S3 offers a range of storage classes designed for different data use cases. Each object gets assigned a storage class, and each bucket can hold objects that reside in different storage classes. You can move or change storage classes as your data needs or access patterns change. Some storage classes have minimum billable object size requirements and storage-time durations that must be met.

#### Before you choose
Before you decide on a storage class, take the time to analyze your workloads, data access patterns, service level agreements, and performance requirements to determine the correct storage class or storage classes for your data. 

Here are some questions to get you started:
* What are the application's data requirements for performance? What is your latency tolerance, or do you need millisecond latency?
* Is the data access pattern predictable or unpredictable? Is the data accessed every minute, every hour, or daily? Is it accessed only one week a year or is the access dependent on the project?
* Does the business or the data have compliance or long-term-storage requirements?
* What service levels are in place for your data access? Can users wait five hours for retrieval or does retrieval need to be faster?
* What is the data access pattern?

#### Storage class questions
##### Do I need to choose a storage class?
No, you don't need to choose a class; however, by default, Amazon S3 will store your data in the S3 Standard storage class. As you will discover later in this course, each storage class has its own cost and performance attributes. 

For example, imagine you're working with an external vendor on an oceanographic research project that collects terabytes of data daily on seawater quality, currents, temperatures, and marine life distribution. Your project runs for only three months, and then you analyze and process the data and publish the results. You plan to start the next step of the study in two years. You might not want terabytes of research data sitting untouched in the S3 Standard storage class for two years. The cost of infrequently accessed data (cold data) in the default storage class might be prohibitive for your business or department. 

Make sure you understand your data use cases. If you make the correct decision for storing your data, you will see both better performance and better cost savings.

##### Can I choose more than one storage class?
You can have as many storage classes for your data as you need, but each object can only be stored in one storage class as a time.

Data can have many requirements and demands made on it, whether it's a performance need, an application edict, a country or site specific requirement, or a legal or compliance process. Because of these ever-changing demands, Amazon has multiple storage classes to meet your needs. 

##### Which storage class will protect against data loss?
All of the Amazon S3 storage classes are designed to provide 99.999999999 percent of durability. This durability level corresponds to an average annual expected loss of 0.000000001 percent of objects. 

In addition, S3 Standard, S3 Standard-IA, and S3 Glacier storage classes are all designed to sustain data in the event of an entire Amazon S3 Availability Zone loss. As with any environment, the best practice is to have a backup and to put in place safeguards against malicious or accidental deletion. For Amazon S3 data, the best practices include secure access permissions, cross-Region replication, and versioning. 

#####What if I have encryption requirements?
Amazon S3 supports both server-side encryption and client-side encryption for data uploads. Amazon S3 offers flexible security features to block unauthorized users from accessing your data.

##### Can I use Amazon S3 if my data has regulatory or compliance requirements?
Amazon S3 maintains compliance programs, such as PCI-DSS, HIPAA/HITECH, FedRAMP, EU Data Protection Directive, and FISMA, to help you meet regulatory requirements. AWS also supports numerous auditing capabilities to monitor access requests to your Amazon S3 resources.

For additional details, see Compliance Validation for Amazon S3 at [https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-compliance.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-compliance.html).

##### Does the data permanently reside in the storage class I choose?
You do not need to choose just one storage class and stick to it. Data can also move between the storage classes based on access patterns and lifecycle management rules. An object that hasn't been accessed for a month can be moved to a more cost-effective storage class. If you need access to the object, it can be moved back to a more active storage class. Data is as mobile and dynamic in Amazon S3 as you are in your need to manage it.

#### Amazon S3 analytics – storage class analysis 
With storage class analysis, you can analyze storage access patterns and transition the right data to the right storage class. This feature observes data access patterns to to help you determine when to transition to storage classes more appropriate for less frequently accessed data. 

After storage class analysis observes the access patterns of a filtered set of data over a period of time, you can use the analysis results to help you improve your lifecycle policies. You can configure storage class analysis to analyze all the objects in a bucket. Or you can configure filters to group objects together for analysis by common prefix (that is, objects that have names that begin with a common string), object tags, or both prefix and tags. You will probably find that filtering by object groups is the best way to benefit from storage class analysis.

Storage class analysis provides storage usage visualizations in the Amazon S3 console that are updated daily. You can also export this daily usage data to an S3 bucket and view them in a spreadsheet application or with business intelligence tools, like **Amazon QuickSight**.

#### Coming up
Each of the storage classes focus on different attributes of access patterns, retention times, object lifecycle, and cost. 

### Storage Classes for Frequently Accessed Data
#### S3 Standard (general purpose)
S3 Standard is the default storage class for Amazon S3 and is automatically assigned to your objects if you do not choose a different storage class. S3 Standard is designed for performance-sensitive use cases, those that require millisecond access time, and your most frequently accessed data. This is the best storage class for a wide variety of use cases, including cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big data analytics.

#### Key features include the following:
* Low latency and high throughput performance
* Durability of 99.999999999 percent of objects across multiple Availability Zones
* Resiliency against events that impact an entire Availability Zone
* Availability of 99.99 percent over a given year
* Amazon S3 service level agreement for availability
* SSL support for data in transit and encryption of data at rest
* Amazon S3 lifecycle management for automatic migration of objects to other Amazon S3 storage classes

#### Object storage and retrieval limits
##### MINIMUM DURATION
S3 Standard has no data storage minimum or maximum duration. You can store an object in S3 Standard for one day, one year, or longer.

However, if you plan to store an object for a long period of time with infrequent access, consider choosing a less expensive storage tier. 

##### MINIMUM OBJECT SIZE
S3 Standard has no minimum size requirement.

##### RETRIEVAL TIMES
With S3 Standard, you can immediately retrieve your objects. S3 Standard provides low latency for object access.

#### Plan before you upload
If you are new to Amazon S3, or if you have started using it without a defined strategy, consider your future data state. Even the best administrator struggles if they upload TBs of data into Amazon S3 without clear details about the data, access patterns, retention policies, or if they need the objects to be immutable (unchanging).

Plan what you want to do with your data before you put it into the cloud. With this plan, you can  upload your data and set lifecycle rules; policies for retention, replication, and deletion; and procedures for archival and retrieval.

#### Pricing for storage
##### Storage-only pricing for **S3 Standard** (general purpose):

| Tier | Amount Stored | Price |
| -------------------- | ----------- | ------------- |
| Frequent Access Tier | Up to 50 TB | $0.023 per GB |
| Frequent Access Tier | 50–500 TB | $0.022 per GB |
| Frequent Access Tier | Over 500 TB | $0.021 per GB |

##### Requests and data retrieval pricing for **S3 Standard** (general purpose):

| PUT, COPY, POST, LIST Requests (Per 1,000 Requests) | GET, SELECT, and All Other Requests(Per 1,000 Requests) | Data Retrieval Requests | Per 1,000 Requests) | Data Retrievals (Per GB) |
| ------ | ------- | --- | --- |
| $0.005 | $0.0004 | n/a | n/a |

##### [Amazon S3 current pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4)

### Storage Classes for Infrequently Accessed Data
### S3 Standard-IA
iS3 Standard-IA is for data that you access less frequently but for which you require rapid access when you do need it. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard with a **lower per-GB** storage price than standard storage, but **higher per request** charges and retrieval fees. The charges for each request and retrieval for S3 Standard-IA are higher than S3 Standard. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and data stores for disaster recovery files. S3 Standard IA stores objects redundantly across multiple Availability Zones so that objects are resilient to the loss of an Availability Zone.

S3 Standard-IA is suitable for objects **larger than 128 KB** that you plan to store for **at least 30 days**. If an object is less than 128 KB, Amazon S3 charges you for 128 KB. If you delete an object before the end of the 30-day minimum storage duration period, you are charged for 30 days. 

#### Key features include the following:
* Same low latency and high throughput performance of S3 Standard
* Durability of 99.999999999 percent of objects across multiple Availability Zones
* Resiliency against events that impact an entire Availability Zone
* Data is resilient in the event of one entire Availability Zone destruction
* Availability of 99.9 percent over a given year
* Amazon S3 service level agreement for availability
* SSL support for data in transit and encryption of data at rest
* S3 Lifecycle management for automatic migration of objects to other Amazon S3 storage classes

### S3 One Zone-IA
S3 One Zone-IA is for data that you access less frequently but for which you require rapid access when you do need it. S3 One Zone IA stores the object data in only one Availability Zone. Because of this, the data is not resilient to the physical loss of the Availability Zone resulting from disasters, such as earthquakes and floods. The S3 One Zone-IA storage class is as durable as S3 Standard-IA, but it is less available and less resilient. Also, because the data resides in only a single Availability Zone, this storage class costs 20 percent less than S3 Standard-IA. 

S3 One Zone-IA is ideal for customers who want a lower-cost option for infrequently accessed data but who do not require the availability and resilience of S3 Standard or S3 Standard-IA. This storage class is a good choice for storing secondary backup copies of on-premises data, data you can quickly recreate, or storage you have already replicated in another Region using Amazon S3 cross-Region replication for compliance or disaster recovery purposes.

S3 One Zone-IA offers the same high durability, high throughput, and low latency of S3 Standard with a low per-GB storage price and per-GB retrieval fee. 

The S3 One Zone-IA storage class is also suitable for objects larger than 128 KB that you plan to store for at least 30 days. Just like S3 Standard-IA, objects smaller than 128 KB will be charged at the 128 KB size. Any object deleted before the 30-day minimum storage duration period will be charged for 30 full days.

#### Key features include the following:
* Same low latency and high throughput performance of S3 Standard
* Durability of 99.999999999 percent of objects in a single Availability Zone†
* Availability of 99.5 percent over a given year
* Amazon S3 service level agreement for availability
* SSL support for data in transit and encryption of data at rest
* S3 Lifecycle management for automatic migration of objects to other S3 storage classes

**Because S3 One Zone-IA stores data in a single Availability Zone, data stored in this storage class will be lost in the event of Availability Zone destruction.**

#### Storage and retrieval limits
##### MINIMUM DURATION
S3 Standard-IA and S3 One Zone-IA are both suitable for objects you plan to store for at least 30 days.

##### MINIMUM OBJECT SIZE
S3 Standard-IA and S3 One Zone-IA are both suitable for objects larger than 128 KB.

##### RETRIEVAL TIMES
There is no waiting to retrieve objects in S3 Standard-IA or S3 One Zone-IA. 

For the following transitions, Amazon S3 does not transition objects that are **smaller than 128 KB**:
* From the S3 Standard or S3 Standard-IA storage classes to S3 Intelligent-Tiering or S3 Glacier Instant Retrieval.
* From the S3 Standard storage class to S3 Standard-IA or S3 One Zone-IA.

#### Pricing information
The following chart does not include data retrieval, transfer, or management costs. Storage-only pricing for **S3 Standard-IA** and **S3 One Zone-IA**:

| Storage Class | Tier | Amount Stored | Price |
| -------------- | --------------------- | ------------------------------- | -------------- |
| S3 Standard-IA | Infrequently accessed | Total amount of storage a month | $0.0125 per GB |
| S3 One Zone-IA | Infrequently accessed | Total amount of storage a month | $0.01 per GB |

##### Requests and data retrieval pricing for **S3 Standard-IA** and  **S3 One Zone-IA**:

| Storage Class | PUT, COPY, POST, LIST Requests (Per 1,000 Requests) | GET, SELECT, and All Other Requests (Per 1,000 Requests) | Data Retrieval Requests Per 1,000 Requests) | Data Retrievals (Per GB) |
| -------------- | ----- | ------ | --- | ----- |
| S3 Standard-IA | $0.01 | $0.001 | n/a | $0.01 |
| S3 One Zone-IA | $0.01 | $0.01 | n/a | $0.01 |

#### [Amazon S3 current pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4)

### Storage Classes for Unknown or Changing Access Patterns
#### S3 Intelligent-Tiering
The S3 Intelligent-Tiering storage class optimizes storage costs by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead. It is the only cloud storage that delivers automatic cost savings by moving data on a granular object level between access tiers when access patterns change. This is the perfect storage class when you want to optimize storage costs for data that has unknown or changing access patterns. There are no retrieval fees for S3 Intelligent-Tiering. There is a small monthly object monitoring and automation fee because S3 Intelligent-Tiering monitors the access patterns and moves the objects automatically from one tier to another. Finally, there are retrieval fees for expedited archive retrieval and request charges.

#### How it works
S3 Intelligent-Tiering uses your data access patterns to automatically move data **between three access tiers**, with the option **to activate a fourth and fifth archive and deep archival tier**. The first tier is optimized for frequent access, the next lower-cost tier is optimized for infrequent access, and the Archive Instant Access Tier is an even lower-cost tier optimized for rarely accessed data. 
Additionally, there are two archive tiers that must be activated before using. Once activated, S3 Intelligent-Tiering moves data that has not been accessed for **90+ consecutive days** to the **Archive Access Tier**. This tier has the **same performance** as the **S3 Glacier Flexible Retrieval storage class**. The last optional tier, is the **Deep Archive Access Tier**. Once activated, objects that have not been accessed for **180 days** automatically move to this lowest cost tier. This tier has the same performance as the **S3 Glacier Deep Archive storage class**.

#### Access time
##### Milliseconds access (automatic)
* Frequent Access Tier
* Infrequent Access Tier
* Archive Instant Access Tier

##### Minutes to hours access (optional)
* Archive Access Tier
* Deep Archive Access Tier

Objects uploaded or transitioned to S3 Intelligent-Tiering are automatically stored in the Frequent Access Tier. S3 Intelligent-Tiering works by monitoring access patterns and then moving the objects that have not been accessed in 30 consecutive days to the Infrequent Access Tier. Once you have activated one or both of the archive access tiers, S3 Intelligent-Tiering will automatically move objects that haven’t been accessed for 90 consecutive days to the Archive Access Tier and then after 180 consecutive days of no access to the Deep Archive Access Tier. If the objects are accessed at a later date, S3 Intelligent-Tiering moves the objects back to the Frequent Access Tier. There are no retrieval fees, so you won’t see unexpected increases in storage bills when access patterns change. 

##### Key features include the following:
Only cloud storage that delivers automated cost savings
Monitors and optimizes costs at a granular object level
Moves objects between four access tiers for a small monthly monitoring and automation fee
Two low-latency access tiers for frequent and infrequent access and two new optional archive access tiers designed for access in minutes and hours
No operational overhead, no lifecycle fees, and no retrieval fees
Designed for 99.9 percent availability and 99.999999999 percent (11 nines) of durability 

#### Feature integration 
S3 Intelligent-Tiering works with all of the Amazon S3 features, such as object tagging, cross-region replication, and S3 Select. This is an Amazon S3 capability designed to pull out only the data you need from an object, which dramatically improves the performance and reduces the cost of applications that need to access data in Amazon S3. To manage S3-Intelligent-Tiering, you can use the Amazon S3 API or AWS CLI. You can also manage data through the console by putting objects directly into S3 Intelligent-Tiering or by using a S3 Lifecycle policy to move objects from S3 Standard or S3 Standard-IA to S3 Intelligent-Tiering. S3 Intelligent-Tiering is available today in all commercial Regions and AWS GovCloud (US). 

#### Archival tier activation
##### How do I activate S3 Intelligent-Tiering archive access tiers?
You can activate the Archive Access Tier and Deep Archive Access Tier by creating a bucket, prefix, or object tag level configuration using the Amazon S3 API, AWS CLI, or the console. You should only activate one or both of the archive access tiers if your objects can be accessed asynchronously by your application. 

##### Can I extend the time before objects are archived?
Yes. In the bucket, prefix, or object tag level configuration, you can extend the last access time for archiving objects in S3 Intelligent-Tiering. When activated, by default objects that haven't been accessed for a minimum of 90 consecutive days automatically move to the Archive Access Tier. Objects that haven't been accessed for a minimum of 180 consecutive days automatically move to the Deep Archive Access Tier. The default configuration for the consecutive days since last access before automatic archiving in S3 Intelligent-Tiering can be extended for up to 2 years. 

##### How do I identify in which tier my objects are located?
You can use Amazon S3 Inventory to report the access tier of objects stored in the S3 Intelligent-Tiering storage class. Amazon S3 Inventory provides CSV, Optimized Row Columnar, or Apache Parquet output files that list your objects and their corresponding metadata on a daily or weekly basis for an S3 bucket or a shared prefix. You can also make a HEAD request on your objects to report the S3 Intelligent-Tiering archive access tiers. 

#### Storage and retrieval limits
##### MINIMUM DURATION
S3 Intelligent-Tiering has no minimum storage duration.

##### MINIMUM OBJECT SIZE
S3 Intelligent-Tiering has no minimum billable object size, but objects smaller than 128 KB are not eligible for auto-tiering and will always be stored at the Frequent Access Tier rate.

##### RETRIEVAL TIMES
The retrieval time for moving the object back to the Frequent Access Tier depends on the tier from which the data is coming. The Frequent Access, Infrequent Access, and Archive Instant Access Tiers are designed for low latency and high throughput.

Retrieval times are 3–5 hours for objects in the Archive Access Tier and within 12 hours if the objects are in the Deep Archive Access Tier.

#### Fees
With S3 Intelligent-Tiering, you incur a small monthly monitoring and automation fee per object. There are no retrieval fees in S3 Intelligent-Tiering. With the addition of automatic data archiving, you can now further reduce your Amazon S3 storage costs when access patterns change without any analysis, operational overhead, or retrieval fees.

#### Use cases
With S3 Intelligent-Tiering storage, you can focus on your business needs while Amazon S3 monitors and reacts to your data access patterns. If you're unsure about the access frequency of an object or bucket, S3 Intelligent-Tiering might be a good choice. If you know without doubt that objects are not frequently accessed, your best option is to store those infrequently accessed objects in a class dedicated to infrequently accessed data from both a performance and cost-savings perspective.

Data lakes, big data analytics, and media applications are prime use cases for S3 Intelligent-Tiering because data in these instances is often used when first stored and then object access is reduced. When this happens, S3 Intelligent-Tiering can move that data down to less expensive storage tiers without administrator intervention, saving time and storage costs.

#### Pricing information
##### Storage-only pricing for **S3 Intelligent-Tiering**:

| Tier | Amount Stored | Price |
| ---- | ------------- | ----- |
| Frequent Access Tier | First 50 TB a month | $0.023 per GB |
| Frequent Access Tier | Next 450 TB per month | $0.022 per GB |
| Frequent Access Tier | Over 500 TB per month | $0.021 per GB |
| Infrequent Access Tier | All storage per month  | $0.0125 per GB |
| Archive Access Tier | All storage per month | $0.004 per GB  |
| Deep Archive Access Tier | All storage per month | $0.00099 per GB |

##### Requests, lifecycle transitions, and data retrieval pricing for **S3 Intelligent-Tiering**:

| PUT, COPY, POST, LIST Requests (Per 1,000 Requests) | GET, SELECT, and All Other Requests (Per 1,000 Requests) | Lifecycle Transition Requests Into (Per 1,000 Requests) | Data Retrieval Requests (Per 1,000 Requests) | Data Retrievals (Per GB) |
| ------ | ------- | ----- | --- | --- |
| $0.005 | $0.0004 | $0.01 | n/a | n/a |

##### [Amazon S3 current pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4)

### Storage Classes for Archiving Objects
The Amazon S3 Glacier storage classes are purpose-built for data archiving, providing you with the highest performance, most retrieval flexibility, and lowest cost archive storage in the cloud. The S3 Glacier storage classes provide three different archival storage classes optimized for different access patterns and storage durations.

#### S3 Glacier Instant Retrieval 
S3 Glacier Instant Retrieval is an archive storage class delivering the lowest cost storage for long-lived, rarely accessed data that requires retrieval in milliseconds. S3 Glacier Instant Retrieval delivers the fastest access to archive storage, with the same throughput and milliseconds access as the S3 Standard and S3 Standard-IA storage classes. This storage class also has 99.999999999 percent (11 nines) of data durability and 99.9 percent availability by redundantly storing data across multiple physically separated Availability Zones. This storage class is designed for rarely accessed data that still needs immediate access in performance-sensitive use cases like image hosting, online file-sharing applications, medical imaging and health records, news media assets, and genomics.

##### Key features include the following:
* Data retrieval in milliseconds with the same performance as S3 Standard
* Durability of 99.999999999 percent of objects across multiple Availability Zones
* Data is resilient in the event of one entire Availability Zone destruction
* Data availability of 99.9 percent in a given year
* 128 KB minimum object size storage charge
* SSL support for data in transit and encryption of data at rest
* S3 PUT API for direct uploads to S3 Glacier Instant Retrieval

Medical records, broadcasts, photographs can upload directly into S3 Instant Retrieval for long-term storage and use with data analytics tools. When the images are needed again, the access is instant, providing users with efficient access to their data and images.

##### Storage and retrieval limits for S3 Glacier Instant Retrieval
###### MINIMUM DURATION
S3 Glacier Instant Retrieval has a minimum storage duration requirement of 90 days. Any objects you delete before 90 days incur a pro-rated charge equal to the storage charge for the remaining days. In the US East (Northern Virginia) Region, you would be charged a pro-rated early deletion fee of $0.012 per gigabyte deleted within 3 months. This means that if you delete the data on day 30, you will be charged a pro-rated fee of $0.008 for the remaining 60 days. If the data was deleted on day 60, you would be charged a $0.004 fee for the remaining 30 days. **Fees are for example purposes and subject to change**

###### MINIMUM OBJECT SIZE
S3 Glacier Instant Retrieval has a minimum billable object storage size requirement of 128 KB. Objects smaller than 128 KB can be stored, but you are charged for 128 KB of storage.

###### RETRIEVAL TIMES
S3 Glacier Instant Retrieval provides millisecond object retrieval.

#### S3 Glacier Flexible Retrieval
S3 Glacier Flexible Retrieval delivers a low-cost storage solution for archive data that is accessed 1–2 times per year. S3 Glacier Flexible Retrieval retrieves data asynchronously, meaning that after you have requested the data, you must wait for the data to restore. This storage class offers flexible retrieval times from minutes to hours based on your data and cost requirements. For archive data that does not require immediate access, S3 Glacier Flexible Retrieval provides free bulk retrievals. It is an ideal solution for backup, disaster recovery, offsite data storage needs, and for when some data occasionally needs to be retrieved in minutes and you don’t want to worry about costs. S3 Glacier Flexible Retrieval is designed for 99.999999999 percent (11 nines) of data durability and 99.99 percent availability. 

Data stored in the S3 Glacier storage class has a minimum storage duration period of 90 days. Deleting data from S3 Glacier Flexible Retrieval is free if the archive being deleted has been stored for 3 months or longer. If an archive is deleted within 3 months of being uploaded, you will be charged an early deletion fee. In the US East (Northern Virginia) Region, you would be charged a pro-rated early deletion fee of $0.012 per gigabyte deleted within 3 months. So if you deleted 1 GB of data 1 month after uploading it, you would be charged a $0.008 early deletion fee. If instead you deleted 1 GB after 2 months, you would be charged a $0.004 early deletion fee. 

##### Key features include the following:
* Durability of 99.999999999 percent of objects across multiple Availability Zones
* Data is resilient in the event of one entire Availability Zone destruction
* SSL support for data in transit and encryption of data at rest
* Low-cost design is ideal for long-term archive
* Up to 10 percent lower cost (than S3 Glacier Instant Retrieval)
* Configurable retrieval times, from minutes to hours
* No minimum billable object size. S3 Glacier Flexible Retrieval requires 40 KB of additional metadata for each archived object, which will be added to the object size for billing purposes
* S3 PUT API for direct uploads to S3 Glacier Flexible Retrieval, and S3 Lifecycle management for automatic migration of objects

##### Storage and retrieval limits for S3 Glacier Flexible Retrieval
###### MINIMUM DURATION
S3 Glacier Flexible Retrieval has a minimum duration requirement of 90 days. Any objects you delete before 90 days incur a pro-rated charge equal to the storage charge for the remaining days.

###### MINIMUM OBJECT SIZE
S3 Glacier Flexible Retrieval has a minimum billable object storage size requirement of 40 KB. Objects smaller than 40 KB can be stored, but you will be charged for 40 KB of storage.

###### RETRIEVAL TIMES
S3 Glacier provides three retrieval options to fit your needs:
* Expedited (1–5 mins)
* Standard (3–5 hours)
* Bulk (5–12 hours) free

Expedited retrievals typically return data in 1–5 minutes and are great for active archive use cases. Standard retrievals typically complete in 3–5 hours and work well for less time-sensitive needs like backup data, media editing, or long-term analytics. Bulk retrievals are the lowest cost retrieval option, returning large amounts of data within 5–12 hours.

#### S3 Glacier Deep Archive
S3 Glacier Deep Archive is the lowest cost storage class in Amazon S3 and supports long-term retention and digital preservation for data that might be accessed once or twice a year. It is designed for highly regulated industries, such as the financial services, healthcare, and public sectors, that retain datasets for 7–10 years or longer to meet regulatory compliance requirements. S3 Glacier Deep Archive can also be used for backup and disaster recovery use cases and is a cost-effective and manageable alternative to magnetic tape systems, whether they are on-premises libraries or off-premises services. 

Data stored in the S3 Glacier Deep Archive storage class has a minimum storage duration period of 180 days. Objects deleted, overwritten, or transitioned to a different storage class before the 180-day minimum incur a pro-rated charge from the time of deletion to the 180-day minimum.

All objects stored in S3 Glacier Deep Archive are replicated and stored across at least three geographically dispersed Availability Zones, with 99.999999999 percent of durability protection and a default retrieval time of 12 hours.

##### Key features include the following:
* Durability of 99.999999999 percent of objects across multiple Availability Zones
* Lowest cost storage class designed for long-term retention of data that will be retained for 7–10 years
* Ideal alternative to magnetic tape libraries
* Retrieval time within 12 hours
* No minimum billable object size. S3 Glacier Deep Archive requires 40 KB of additional metadata for each archived object, which will be added to the object size for billing purposes
* S3 PUT API for direct uploads to S3 Glacier Deep Archive, and S3 Lifecycle management for automatic migration of objects

##### Storage and retrieval limits for Amazon S3 Glacier Deep Archive
###### MINIMUM DURATION
S3 Glacier Deep Archive has a minimum duration requirement of 180 days of storage. Any objects you delete before 180 days incur a pro-rated charge equal to the storage charge for the remaining days.

###### MINIMUM OBJECT SIZE
S3 Glacier Deep Archive has a minimum billable object storage size requirement of 40 KB. Objects smaller than 40 KB can be stored, but you will be charged for 40 KB of storage.

###### RETRIEVAL TIMES
S3 Glacier Deep Archive has retrieval times within 12 hours.

#### Monitoring and compliance
The S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes offer sophisticated integration with CloudTrail to log, monitor, and retain storage API call activities for auditing and supports three different forms of encryption. 

These storage classes also support security standards and compliance certifications. These include SEC Rule 17a-4, Payment Card Industry Data Security Standard, HIPAA, Health Information Technology for Economic and Clinical Health, FedRAMP, EU General Data Protection Regulation, and Federal Information Security Management Act. Amazon S3 Object Lock permits write once read many storage capabilities, helping satisfy compliance requirements for virtually every regulatory agency around the globe.

#### Pricing information
The following chart does not include data retrieval, transfer, or management costs.

Storage-only pricing for the three Amazon S3 Glacier storage classes:

| Storage Class | Storage Class | Amount Stored | Price |
| ------------- | ------------- | ------------- | ----- |
| S3 Glacier Instant Retrieval | For long-lived archive data accessed once a quarter with instant retrieval in milliseconds  | Total amount of storage per month | $0.004 per GB |
| S3 Glacier Flexible Retrieval | For long-term backups and archives with retrieval options from 1 minute to 12 hours  | Total amount of storage per month | $0.0036 per GB |
| S3 Glacier Deep Archive | For long-term data archiving that is accessed once or twice in a year and can be restored within 12–48 hours  | Total amount of storage per month | $0.00099 per GB |

|        | PUT, COPY, POST, LIST requests (per 1,000 requests) | GET, SELECT, and all other requests (per 1,000 requests) | Data Retrieval Requests (per 1,000 requests) | Data retrievals (per GB) |
| ----------------| --- | --- | --- | --- |
| Archive Instant | N/A | N/A | N/A | N/A |
| Archive Access, Standard | N/A | N/A | N/A | N/A |
| Archive Access, Bulk | N/A | N/A | N/A | N/A |
| Archive Access, Expedited | N/A | N/A | $10.00 | $0.03 |
| Deep Archive Access, Standard | N/A | N/A | N/A | N/A |
| Deep Archive Access, Bulk | N/A | N/A | N/A | N/A |

*Prices are current as of March 2023 and are subject to change without notice. Pricing varies by Region.

##### [Amazon S3 current pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4)

### Knowledge Check
#### What happens to users’ data if they are using S3 One Zone-IA and there is an Amazon S3 service outage in the Availability Zone? 
* Nothing happens. Amazon S3 offers 11 nines of durability.
* Users can access their data in another Availability Zone.
* The data is replicated to another AWS Region for recovery.
* **Without the Availability Zone, users cannot access their data until the service is restored in the Availability Zone.**

Because S3 One Zone-IA stores data in a single Availability Zone, data stored in this storage class will be lost in the event of Availability Zone destruction.

The other options are incorrect because S3 One Zone-IA stores data in a single Availability Zone. Data stored in this storage class will be lost in the event of Availability Zone destruction.

#### Which of the following access patterns works best with S3 Intelligent-Tiering? (Choose TWO.) 
* **Unknown access patterns**
* **Unpredictable access patterns**
* Daily access data patterns
* Yearly data access patterns
* Long-term storage access patterns

**Unknown access patterns** and **Unpredictable access patterns**. 

S3 Intelligent-Tiering is the ideal storage class for long-lived data with access patterns that are unknown or unpredictable.

The other options are incorrect because they have predictable access patterns that can be directly addressed by other storage classes.

#### Which scenario would restrict Amazon S3 lifecycle policies from moving objects between storage classes?
* An object is larger than 128 GB.
* **An object is smaller than 128 KB.**
* An object is less than 30 days old.
* An object is more than 30 days old.

Amazon S3 does not move objects between storage classes if they are **smaller than 128 KB** because it is not cost-effective to do so.

The other response options are incorrect because of the following: 
* Objects larger than 128 GB can be moved between storage classes.
* Lifecycle policies can be set to move objects of any age.

### Summary
* Discussing when to choose Amazon S3 and the consistency and Region implications
* Explaining how to set up a bucket and upload files
* Explaining the use of object URLs, file URLs, hosted URLs, and S3 ARNs
* Discussing how to secure an S3 bucket
* Describing how to manage Amazon S3 objects using tagging
* Identifying Amazon S3 storage classes
* Discussing how to use Amazon S3 storage classes for lifecycle management
* Describing how to use Amazon S3 access points and multi-Region access points

#### Object storage in Amazon S3
In Amazon S3 object storage, you can organize objects to imitate a hierarchy by using key name prefixes and delimiters. Prefixes and delimiters allow you to group similar items to help visually organize and easily retrieve your data. In the user interface, these prefixes give the appearance of a folder/ subfolder structure but in reality, the storage is still a flat structure. 

Buckets are containers that hold objects. You can create up to 100 buckets in each AWS account by default. You can increase the bucket limit to a maximum of 1,000 buckets by submitting a service limit increase. Bucket sizes are virtually unlimited so you don't have to allocate a predetermined bucket size the way you would when creating a storage volume or partition.

Bucket names must have the following characterist:
* Be unique across all of Amazon S3
* Be between 3-63 characters long
* Consist only of lowercase letters, numbers, dots (.), and hyphens (-)
* Start with a lowercase letter or number
* Not begin with xn-- (beginning February 2020)
* Not be formatted as an IP address. (i.e. 198.68.10.2)
* Use a dot (.) in the name only if the bucket's intended purpose is to host an Amazon S3 static website; otherwise do not use a dot (.) in the bucket name

#### Region locations
Amazon S3 is a globally viewable service. The region you choose should be local to your users or consumers to optimize latency, minimize costs, or to address regulatory requirements.

#### Cross-Region Replication (CRR)
If your data needs to be stored in multiple regions, your buckets can be replicated to other Regions using Cross-Region Replication. This enables you to automatically copy objects from a  bucket in one region to different bucket in a another, separate region

#### Same-Region Replication (SRR)
SRR makes another copy of S3 objects within the same AWS Region, with the same redundancy as the destination storage class. SRR helps you address data sovereignty and compliance requirements by keeping a copy of your objects in the same AWS Region as the original.

#### Storage classes for frequently accessed data
##### Amazon S3 Standard (general purpose)
Amazon S3 Standard is the default storage class for Amazon S3 and is automatically assigned to your objects if you do not choose a different storage class. It is designed for performance-sensitive use cases, those that require millisecond access time, and for your most frequently accessed data.

#### Storage classes for infrequently accessed data
##### Amazon S3 Standard-Infrequent Access 
Amazon S3 Standard-Infrequent Access (S3 Standard-IA) is for data that you access less frequently, but for which you require rapid access when you do need it. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard, with a lower per-GB storage price and per-GB retrieval. 

##### Amazon S3 One Zone-Infrequent Access 
Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) is for data that you access less frequently, but for which you rapid access when you do need it. S3 One Zone IA stores the object data in only one Availability Zone, which enables rapid access while sacrificing the resiliency of storing data across multiple Availability Zones.

#### Storage Classes for Unknown or Changing Access Patterns
##### Amazon S3 Intelligent-Tiering
The S3 Intelligent-Tiering storage class optimizes storage costs by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead. It is the only cloud storage that delivers automatic cost savings by moving data on a granular object level between access tiers when access patterns change.

#### Storage Classes for Archiving Objects
##### Amazon S3 Glacier Instant Retrieval 
S3 Glacier Instant Retrieval is an archive storage class delivering the lowest-cost storage for long-lived, rarely accessed data, that requires retrieval in milliseconds. S3 Glacier Instant Retrieval delivers the fastest access to archive storage, with the same throughput and milliseconds access as the S3 Standard and S3 Standard-IA storage classes.

##### Amazon S3 Glacier Flexible Retrieval (S3 Glacier)
S3 Glacier Flexible Retrieval delivers a low-cost storage solution for archive data that is accessed 1-2 times per year. S3 Glacier Flexible Retrieval retrieves data asynchronously, meaning that once you have requested the data you must wait for the data to restore. 

##### Amazon S3 Glacier Deep Archive (S3 Glacier Deep Archive)
S3 Glacier Deep Archive is the lowest-cost storage class in Amazon S3 and supports long-term retention and digital preservation for data that may be accessed once or twice in a year. S3 Glacier Deep Archive can also be used for backup and disaster recovery use cases, and is a cost-effective and easy-to-manage alternative to magnetic tape systems, whether they are on-premises libraries or off-premises services. 

### Additional Resources
#### [Using a prefix and delimiter](https://docs.aws.amazon.com/AmazonS3/latest/dev/ListingKeysHierarchy.html)

#### [Additional information](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html)

#### [Amazon S3 analytics](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html)

## Amazon EBS
### Pre-assessment
#### What is one of the common uses of Amazon Elastic Block Store (Amazon EBS)?
* Amazon EBS is used for temporary storage that last only for the duration of an EC2 instance.
* Amazon EBS is used for large-scale storage of unstructured data.
* Amazon EBS is used for caching frequently accessed data close to the user.
* **Amazon EBS is used for storage for database-style applications.**

**Amazon EBS is used for storage for database-style applications.**

The other options are incorrect because of the following: 
* EBS volumes persist independently from the life of an EC2 instance. 
* Amazon S3 is used for large-scale storage of unstructured data. Amazon EBS is used primarily for structured data.
* Edge storage is used for caching frequently accessed data close to the user.

#### What type of storage provides temporary, block-level storage for Amazon EC2?
* **Instance storage**
* Amazon Elastic Block Store (Amazon EBS) storage
* Snapshots
* Amazon S3

**Instance storage provides temporary, block-level storage for Amazon EC2.**

The other options are incorrect because of the following:
* Amazon EBS storage persists independent of EC2 instances.
* Snapshots are incremental copies of data stored in EBS volumes.
* Amazon S3 provides object storage, not block-level storage.

#### What are some of the benefits of using Amazon Elastic Block Store (Amazon EBS)? (Select TWO.)
* **EBS volumes are persistent.**
* EBS volumes are maintained on a single server.
* Amazon EBS limits volumes to being attached to a single instance.
* EBS volumes last only as long as the EC2 instance they are attached to.
* **EBS volumes are elastic.**

**EBS volumes are persistent** and **EBS volumes are elastic**.

The other options are incorrect because of the following: 
* EBS volume data is replicated across multiple servers in an Availability Zone.
* Customers can activate Multi-Attach on an EBS Provisioned IOPS io1 or io2 volume, enabling a single EBS volume to be concurrently attached to up to 16 Nitro-based EC2 instances within the same Availability Zone.
* EBS volumes persist independent of the EC2 instance they are attached to.

### Amazon Elastic Block Store
Amazon EBS is a user-friendly, high-performance block storage service designed for use with Amazon EC2 for both throughput and transaction-intensive workloads at any scale. 

AWS recommends Amazon EBS for data that must be quickly accessible and requires long-term persistence. EBS volumes are particularly well suited for use as the primary storage for file systems, databases, or any applications that require fine granular updates and access to raw, unformatted, block-level storage. 

Amazon EBS is well suited to both database-style applications that rely on random reads and writes and to throughput-intensive applications that perform long, sequential reads and writes. EBS volumes behave like raw, unformatted block devices. You can mount these block devices as EBS volumes on your EC2 instances. EBS volumes that are attached to an EC2 instance are exposed as raw block storage volumes that persist independently from the life of the instance. You can create a file system on top of these volumes or use them in any way you would use a block device (such as a hard drive). Finally, you can dynamically change the configuration of a volume attached to an EC2 instance, unlike traditional disk drives that come in fixed sizes.

You can choose from six different EBS volume types to balance optimal price and performance. You can achieve single-digit millisecond latency for high-performance database workloads such as SAP HANA or gigabyte-per-second throughput for large, sequential workloads such as Apache Hadoop. You can change EBS volume types, tune performance, or increase volume size without disrupting your critical applications. Amazon EBS provides you cost-effective block storage when you need it.

Designed for mission-critical systems, EBS volumes are replicated within an Availability Zone and can scale to petabytes of data. Also, you can use EBS snapshots with automated lifecycle policies to back up your volumes in Amazon S3 while ensuring geographic protection of your data and business continuity.

With Amazon EBS, you pay for only the **storage and resources that you provision**.

### AWS block storage portfolio
The AWS block storage portfolio consists of two types of block storage services—instance storage and Amazon EBS—and an integrated snapshot service.

#### INSTANCE STORAGE
Instance storage is temporary block-level storage attached to host hardware that is ideal for storing information that frequently changes or is replicated across multiple instances. Instance storage units are called instance stores and are directly associated with an Amazon EC2 instance. Instance stores are also called EC2 instance stores.

An instance store is non-persistent and is terminated when the associated EC2 instance is terminated. Instance stores resemble Amazon EBS storage in initial configuration options. However, they functionally most closely resemble a direct attached disk drive. The available storage type is directly tied to the EC2 instance type.

#### AMAZON EBS STORAGE
Amazon EBS is a block storage service designed for use with Amazon EC2. Amazon EBS scales to support virtually any workload and any volume size. EBS volumes attach to your EC2 instances and can be moved from one EC2 instance to a different EC2 instance.

EBS volumes are persistent, which means they persist independently from the life of your EC2 instance. If an EC2 instance goes down, your volume and, most importantly, your data on that volume remain available to attach to a different EC2 instance.

#### SNAPSHOTS
Snapshots are incremental, point-in-time copies of your data stored on your EBS volumes. You can use snapshots to restore new volumes, expand the size of a volume, or move volumes across Availability Zones. 

Snapshots let you geographically protect your data and achieve business continuity. You can use Amazon Data Lifecycle Manager to automate snapshot management without any additional overhead or cost.

### Amazon EBS Features and Benefits
### Amazon EBS foundation
Amazon EBS is built on a service foundation to deliver block storage to meet your operational requirements. The core elements include performance, ease of use, reliability, scalability, security, and cost effectiveness.

#### Performance for any workload
The different EBS volume types deliver the right performance for your most demanding workloads.

SSD and HDD backed volumes provide strong price to performance rations suitable for most workloads.

For even higher storage performance per instance, use multiple volumes together.

#### Convenience
Creating, using, and protecting volumes is convenient using the console and the AWS APIs. 

Elastic Volumes capability lets you increase storage, tune performance up and down, and change volume types without any disruption to your workloads. 

You can use Amazon Data Lifecycle Manager for automated snapshot management based on your needs.

#### High reliability
The Amazon EBS architecture is built for mission-critical applications. EBS volumes are designed to protect against failures by replicating within the Availability Zone, offering 99.999 percent durability for io2 volume types, with all other volume types providing 99.8–99.9 percent durability. All volume types  provide an annual failure rate of 0.1–0.2 percent.

#### Virtually unlimited scale
Amazon EBS was launched in 2008 to provide persistent block storage for EC2 instances. Today millions of customers use Amazon EBS to store exabytes of data.

The scalability lets you build applications that require as little as a single gigabyte of storage up to virtually unlimited scale.

#### Secure
Amazon EBS was designed with security as the number one priority. Amazon EBS includes advanced key management and volume encryption features. 

Amazon EBS includes the ability to encrypt newly created EBS volumes by default with a single setting in your account. All data in newly created EBS volumes will be encrypted automatically. 

#### Cost-effective
Amazon EBS provides different options to keep costs as low as possible for your specific workload. There are four different volume types to choose from to balance optimal price and performance. 

You pay for only the storage you use without long-term contracts or complex licensing agreements. 

Backups using EBS snapshots are incremental and save on storage costs by not duplicating data.

### Amazon EBS features and benefits
#### Persistent
Amazon EBS volumes are durable and persistent by default. Your EBS volume survives even if your EC2 instance is terminated. Your data is preserved for your future use and persists until you decide to delete it. 

EBS volumes are managed independently from the Amazon EC2 instances to which they are attached. You can detach an existing EBS volume from an EC2 instance and reattach it to a different EC2 instance. This provides you the ability to change EC2 instance types to meet your performance requirements and optimize your Amazon EC2 costs. It also means that spot instances can be stopped or terminated without losing your data.

#### Built-in encryption
Amazon EBS encryption offers seamless encryption of EBS data volumes, boot volumes, and snapshots, eliminating the need to build and manage a secure key management infrastructure.

Amazon EBS encryption provides data-at-rest security by encrypting your data volumes, boot volumes, and snapshots using AWS managed keys or keys that you create and manage using AWS KMS. You can also configure your profile so that encryption is activated by default for all newly created EBS volumes.  

The encryption occurs on the servers that host EC2 instances, providing data-in-transit encryption of your data as it moves between EC2 instances and EBS data and boot volumes.

With your data encrypted in transit and at rest, you are protected from unauthorized access to your data.

#### High availability and high durability
EBS volumes are designed to be highly available, reliable, and durable at no additional charge to you. EBS volume data is replicated across multiple servers in an Availability Zone to prevent the loss of data from the failure of any single component. 

Amazon EBS offers a higher durability io2 volume that is designed to provide 99.999 percent durability with an annual failure rate (AFR) of 0.001 percent, where failure refers to a complete or partial loss of the volume. For example, if you have 100,000 EBS io2 volumes running for 1 year, you should expect only one io2 volume to experience a failure. This makes io2 ideal for business-critical applications such as SAP HANA, Oracle, Microsoft SQL Server, and IBM DB2 that will benefit from higher uptime. The io2 volumes are 2,000 times more reliable than typical commodity disk drives, which fail with an AFR of 2–4 percent. 

All other EBS volumes are designed to provide 99.8–99.9 percent durability with an AFR of 0.1–0.2 percent. Amazon EBS also supports a snapshot feature, which is a good way to take point-in-time backups of your data. 

#### Multiple volume type options
Amazon EBS provides multiple volume types so that you can optimize storage performance and cost for a broad range of applications. These volume types are divided into two major categories: SSD-backed storage for transactional workloads, such as databases, virtual desktops, and boot volumes, and HDD-backed storage for throughput-intensive workloads, such as MapReduce and log processing. 

SSD-based volumes include two levels to meet your application requirements:
* General Purpose SSD volumes (gp3 and gp2) balance price and performance for transactional applications, including virtual desktops, test and development environments, and interactive gaming applications.
* Provisioned IOPS SSD volumes are the highest performance EBS volumes (io2, io2 Block Express, and io1) for your most demanding transactional applications, including SAP HANA, Microsoft SQL Server, and IBM DB2.

HDD-based volumes include Throughput Optimized HDD (st1) for frequently accessed, throughput-intensive workloads and the lowest cost Cold HDD (sc1) for less frequently accessed data.

You can choose the volume type that best meets your application and use-case requirements. You can change from one volume type to another.

#### Elastic Volumes
Elastic Volumes is a feature that helps you quickly adapt your volumes as the needs of your applications change. The Elastic Volumes feature empowers you to dynamically increase capacity, tune performance, and change the type of any new or existing current generation volume with no downtime or performance impact. You can quickly right-size your deployment and adapt to performance changes.

You can create a volume with the capacity and performance needed today, knowing that you have the ability to modify your volume configuration in the future. Elastic Volumes can save you hours of planning cycles.

By using CloudWatch with AWS Lambda, you can automate volume changes to meet the changing needs of your applications.

The Elastic Volumes feature makes it quicker to adapt your resources to changing application demands, giving you confidence that you can make modifications in the future as your business needs change.

#### Multi-Attach
Customers can activate Multi-Attach on an EBS Provisioned IOPS io2 or io1 volume. Multi-Attach permits a single EBS volume to be concurrently attached to up to 16 Nitro-based EC2 instances within the same Availability Zone.

Multi-Attach helps you achieve higher application availability for applications that manage storage consistency from multiple writers. Each attached instance has full read and write permission to the shared volume. Applications using Multi-Attach need to provide I/O fencing for storage consistency. There is no additional fee to turn on Multi-Attach.

#### Volume monitoring
Performance metrics, such as bandwidth, throughput, latency, and average queue length, are available through the console. Using these metrics, provided by CloudWatch, you can monitor the performance of your volumes to make sure that you are providing enough performance for your applications without paying for resources you don't need.

#### Snapshots
Amazon EBS provides the ability to save point-in-time snapshots of your volumes to Amazon S3. EBS snapshots are stored incrementally. Only the blocks that have changed after your last snapshot are saved, and you are billed only for the changed blocks. 

When you delete a snapshot, you remove only the data not needed by any other snapshot. All active snapshots contain all the information needed to restore the volume to the instant at which that snapshot was taken. The time to restore changed data to the working volume is the same for all snapshots.

Snapshots can be used to instantiate multiple new volumes, expand the size of a volume, or move volumes across Availability Zones. When a new volume is created, you can choose to create it based on an existing EBS snapshot. In that scenario, the new volume begins as an exact replica of the snapshot.

##### Key snapshot feature capabilities include the following:
* Direct read access of EBS snapshots
* Ability to create EBS snapshots from any block storage
* Immediate access to EBS volume data
* Instant full performance on EBS volumes restored from snapshots using Fast Snapshot Restore (FSR)
 * Additional hourly charge for FSR
* Ability to resize EBS volumes
* Ability to share EBS snapshots
* Ability to copy EBS snapshots across Regions

#### Backups
AWS Backup supports backing up your EBS volumes. AWS Backup helps you to centralize and automate data protection across AWS services. AWS Backup offers a cost-effective, fully managed, policy-based service that further simplifies data protection at scale. 

AWS Backup also helps you support your regulatory compliance obligations and meet your business continuity goals. Together with AWS Organizations, AWS Backup helps you centrally deploy data protection (backup) policies to configure, manage, and govern your backup activity across your organization’s AWS accounts and resources. 

AWS Backup supports many AWS services, including 
* EC2 instances,
* EBS volumes, 
* Amazon RDS databases (including Amazon Aurora clusters), 
* Amazon DynamoDB tables, 
* Amazon EFS, 
* FSx for Lustre, 
* FSx for Windows File Server, 
* and Storage Gateway volumes. 

### Amazon EBS Volume Types
Having an understanding of the different EBS volume types is critical when you are designing storage for your applications and workloads. In this section, you will learn more about EBS volume types, including minimum and maximum volume sizes; baseline, burst, and maximum performance; and ways to increase performance for the volume type.

### Types of EBS Volumes
Amazon EBS provides the following volume types: General Purpose SSD, Provisioned IOPS SSD, Throughput Optimized HDD, Cold HDD, and Magnetic (standard). They differ in performance characteristics and cost, which lets you to tailor your storage performance and cost to the needs of your applications. 

* Your account has a limit on the number of EBS volumes that you can use and the total storage available to you. You can request an increase in your limits if required.
* You can attach multiple EBS volumes to a single instance. The volume and instance must be in the same Availability Zone.
* Depending on the EBS volume type and EC2 instance types, you can use multi-attach to mount a volume to multiple instances at the same time.

### General Purpose SSDs
General Purpose SSD-backed volumes provide a balance of price and performance. AWS recommends these for most workloads. The current General Purpose SSD offering includes gp2 and gp3 volume types. 

#### gp2 General Purpose SSD volumes
gp2 General Purpose SSD volumes offer cost-effective storage that is ideal for a broad range of workloads. These volumes deliver single-digit millisecond latencies and the ability for smaller volumes to burst to 3,000 IOPS for extended periods of time. gp2 volume performance scales with the volume size.

* Baseline performance scales linearly at 3 IOPS per gibibyte (GiB) of volume size.
* Performance ranges from a minimum of 100 IOPS at 33.33 GiB and below to a maximum of 16,000 IOPS at 5,334 GiB and above.
* gp2 volumes are designed to deliver their provisioned performance 99 percent of the time.
* gp2 volume size can range from 1 GiB to 16 tebibyte (TiB).
* A flat-rate pricing model is based on the provisioned volume size.

#### gp2 I/O burst credits and burst performance
gp2 volume performance is tied to volume size, which determines the baseline performance level of the volume and how quickly it accumulates I/O or burst credits. I/O credits represent the available bandwidth that your gp2 volume can use to burst large amounts of I/O when more than the baseline performance is needed. 

* Larger volumes have higher baseline performance levels and accumulate I/O credits faster.
* The more credits your volume has for I/O, the more time it can burst beyond its baseline performance level and the better it performs when more performance is needed.
* Each volume receives an initial I/O credit balance of 5.4 million I/O credits, which is enough to sustain the maximum burst performance of 3,000 IOPS for at least 30 minutes. This initial credit balance is designed to provide a fast initial boot cycle for boot volumes and to provide a good bootstrapping experience for other applications.
* gp2 volumes earn I/O credits at the baseline performance rate of 3 IOPS per GiB of provisioned volume size.
* When your volume uses fewer I/O credits than it earns in a second, unused I/O credits are added to the I/O credit balance.
* When your volume requires more than the baseline performance I/O level, it draws on I/O credits in the credit balance to burst to the required performance level up to a maximum of 3,000 IOPS.
* When the baseline performance of a volume is higher than maximum burst performance, I/O credits are never spent.

#### gp3 General Purpose SSD volumes
gp3 General Purpose SSD volumes offer cost-effective storage that is ideal for a broad range of workloads. gp3 volumes deliver a consistent baseline rate of 3,000 IOPS and 125 megabytes per second (MBps) of throughput included with the price of storage. With gp3, you scale IOPS and throughput independent from the volume size.

* gp3 consistent baseline performance of 3,000 IOPS and 125 MBps throughput is included with the price of storage.
* You can independently provision additional performance up to a total of 16,000 IOPS and 1,000 MBps throughput for an additional cost.
 * The maximum ratio of provisioned IOPS to provisioned volume size is 500 IOPS per GiB.
  * 32 GiB or larger volume size: 500 IOPS/GiB x 32 GiB = 16,000 IOPS
 * The maximum ratio of provisioned throughput to provisioned IOPS is 0.25 MBps per provisioned IOPS.
  * 8 GiB or larger volume size with 4,000 provisioned IOPS or higher: 4,000 IOPS x 0.25 MBps/IOPS = 1,000 MBps
* There is flat-rate pricing for provisioned volume size and a tiered pricing model for provisioned IOPS and throughput.

#### General Purpose SSD comparison

| Description | gp3 Volumes | gp2 Volumes |
| ----------- | ----------- | ----------- |
| Durability | 99.8–99.9% durability (0.1–0.2% AFR) | 99.8–99.9% durability (0.1–0.2% AFR) |
| Volume size | 1 GiB–16 TiB | 1 GiB–16 TiB |
| Minimum/maximum IOPS at 16 kibibyte (KiB) I/O | 16,000 | 16,000 |
| Maximum throughput per volume | 1,000 MBps | 250 MBps* |
| Boot volume | Supported | Supported |
| Multi-attached volumes  | Not supported | Not supported |
 
*The throughput limit is 128–250 mebibytes per second (MiBps), depending on the volume size.

* Volumes smaller than or equal to 170 GiB deliver a maximum throughput of 128 MiBps.
* Volumes larger than 170 GiB but smaller than 334 GiB deliver a maximum throughput of 250 MiBps if burst credits are available. 
* Volumes larger than or equal to 334 GiB deliver 250 MiBps regardless of burst credits. 

### Provisioned IOPS SSDs
Provisioned IOPS SSD-backed volumes provide high performance for mission-critical, low-latency, or high-throughput workloads. Provisioned IOPS SSD volumes are designed to meet the needs of I/O-intensive workloads, particularly database workloads, that are sensitive to storage performance and consistency. AWS recommends these for most of your demanding workloads.

The current Provisioned IOPS SSD offering includes io1 and io2 volume types. io2 offers performance for I/O-intensive applications and databases, while io2 Block Express can be used for high-performance, business-critical applications and databases.

#### io1 and io2 Provisioned IOPS SSD volume differences
##### Durability
* io1 volumes are designed to provide 99.8–99.9 percent volume durability with an AFR no higher than 0.2 percent, which translates to a maximum of two volume failures per 1,000 running volumes over a 1-year period.
* io2/io2 Block Express volumes are designed to provide 99.999 percent volume durability with an AFR no higher than 0.001 percent, which translates to a single volume failure per 100,000 running volumes over a 1-year period. 

##### Available EC2 instance types
* Provisioned IOPS SSD io1 volumes are available for all EC2 instance types.
* Provisioned IOPS SSD io2 volumes are available for all EC2 instance types.

##### Maximum ratio of provisioned IOPS to requested volume size
* The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1 for io1 volumes and 500:1 for io2 volumes.
 * For example, a 100-GiB io1 volume can be provisioned with up to 5,000 IOPS, while a 100-GiB io2 volume can be provisioned with up to 50,000 IOPS.
* On a supported instance type, io1 volumes require a 10 times greater volume size for provisioning up to the 64,000 IOPS maximum.
 * io1 volume of 1,280 GiB or greater for maximum IOPS (50 × 1,280 GiB = 64,000 IOPS).
 * io2 volume of 128 GiB or greater for maximum IOPS (500 × 128 GiB = 64,000 IOPS).

#### Provisioned IOPS SSD comparison

| Description | io1 | io2 | io2 Block Express |
| ----------- | --- | --- | ----------------- |
| Durability | 99.8–99.9% durability (0.1–0.2% AFR)  | 99.999% durability (0.001% AFR) | 99.999% durability (0.001% AFR) |
| Volume size | 4 GiB–16 TiB | 4 GiB–16 TiB | 4 GiB–64 TiB |
| Minimum/maximum IOPS at 16 KiB I/O | 100–64,000 | 64,000* | 256,000 |
| Maximum throughput per volume | 1,000 MBps | 1,000 MBps* | 4,000 MBps |

**Maximum IOPS and throughput are guaranteed only on instances built on the Nitro System and provisioned with more than 32,000 IOPS. Other instances guarantee up to 32,000 IOPS and 500 MBps. **

### HDD-backed volumes
The HDD-backed volumes that Amazon EBS provides fall into two categories: st1 Throughput Optimized HDD volumes and sc1 Cold HDD volumes.

#### Throughput Optimized HDD
Throughput Optimized HDD provides low-cost HDDs designed for frequently accessed, throughput-intensive workloads. Throughput Optimized HDD (st1) volumes provide low-cost magnetic storage that defines performance in terms of throughput instead of IOPS. st1 volumes are designed to support frequently accessed data. This volume type is optimized for workloads involving large, sequential I/O. AWS recommends that you use gp3 General Purpose SSD volumes for workloads performing small, random I/O.

This volume type is a good fit for large, sequential workloads such as Amazon EMR; data warehouses; log processing; and extract, transform, and load (ETL) workloads.

* Maximum IOPS is based on 1 MB I/O size, with a baseline throughput of 40 MBps per TB of volume size for st1 volumes. 
* Sustained throughput performance ranges from 5 MBps at 125 GiB to a maximum of 500 MBps at 12,775 GiB and above.
* Baseline burst performance scales from 40 MBps per tebibyte to 500 MBps.
* st1 volumes are designed to deliver their expected throughput performance 99 percent of the time.
* st1 volume size can range from 125 GiB to 16 TiB.

##### st1 throughput credits and burst performance
st1 volume performance is tied to volume size, which determines the baseline throughput of your volume and how quickly it accumulates throughput burst credits. Throughput burst credits represent the available bandwidth that your st1 volume can use to burst large amounts of throughput when more than the baseline performance is needed. 

* Larger volumes have higher baseline performance levels and accumulate burst throughput credits faster.
* The more credits your volume has, the more time it can burst beyond its baseline performance level and the better it performs when more performance is needed.
* For a 1-TiB st1 volume, burst throughput is limited to 250 MBps. Larger volumes scale these limits linearly with throughput capped at a maximum of 500 MBps. 
* The bucket fills with credits at 40 MBps, and it can hold up to 1 TiB of credits.
* When your volume uses fewer burst credits than it earns in a second, unused burst credits are added to the throughput credit balance.
* When your volume requires more than the baseline throughput performance level, it draws on burst credits in the credit balance to burst to the required performance level.
* When the baseline performance of a volume is higher than maximum burst performance, I/O credits are never spent.

#### Cold HDD
Cold HDD provides the lowest cost HDD design for less frequently accessed workloads. Use cases include throughput-oriented storage for data that is infrequently accessed and scenarios where the lowest storage cost is important.

* Maximum IOPS is based on 1 MB I/O size, with a baseline throughput of 12 MBps per terabyte of volume size for sc1 volumes. 
* Sustained throughput performance ranges from 1.5 MBps at 125 GiB to a maximum of 192 MBps at 16,384 GiB.
* Baseline burst performance scales from 12 MBps per tebibyte to 250 MBps.
* sc1 volumes are designed to deliver their expected throughput performance 99 percent of the time.
* sc1 volume size can range from 125 GiB to 16 TiB.

##### sc1 throughput credits and burst performance
sc1 volume performance is tied to volume size, which determines the baseline throughput of your volume and how quickly it accumulates throughput burst credits. sc1 throughput credit and burst performance behave the same as st1 volumes although at a lower scale.

* Larger volumes have higher baseline performance levels and accumulate burst throughput credits faster.
* The more credits your volume has, the more time it can burst beyond its baseline performance level and the better it performs when more performance is needed.
* For a 1-TiB st1 volume, burst throughput is limited to 80 MBps. Larger volumes scale these limits linearly, with throughput capped at a maximum of 250 MBps.
* The bucket fills with credits at 12 MBps, and it can hold up to 1 TiB of credits.

#### HDD volume comparison

| Description | Throughput Optimized HDD | Cold HDD |
| ----------- | ------------------------ | -------- |
| Durability | 99.8–99.9% durability (0.1–0.2% AFR) | 99.8–99.9% durability (0.1–0.2% AFR)  |
| Volume size | 125 GiB–16 TiB | 125 GiB–16 TiB |
| Minimum/maximum throughput at 1 MB I/O | 5–500 MBps | 2–192 MBps |
| Maximum burst throughput per volume | 500 MBps | 250 MBps |
| Boot volume | Not supported | Not supported |
| Multi-attached volumes | Not supported | Not supported |

### Choosing the Correct Amazon EBS Volume Type
Choosing the correct EBS volume type to use for your workload can seem like an overwhelming task as you first begin configuring volumes for your workloads. AWS has simplified your challenge by making it possible to change volume types and performance characteristics. You can be assured that you can later modify the EBS volume type that you initially selected to meet your workflow requirements.

### Preparing to make your decision
Understanding your workload characteristics can help simplify the selection process of your EBS volume types for your workload. You can take some preliminary actions to help provide the information that you require for your decision.

#### Existing on-premises workloads
To prepare to move your on-premises workloads to the AWS Cloud, AWS recommends that you collect as much information about the workloads as you can:

* Storage configuration information is helpful to plan your EBS volume use. How many volumes are used? What storage media are they stored on? What are the volume sizes?
* Volume performance statistics assist in understanding your current volume performance requirements. Are any volumes experiencing 100 percent utilization? Are any volumes creating performance bottlenecks? What are the IOPS? What are the volume throughput requirements?
* Understanding your current and future expected workload utilization or consumption helps you to plan for your current needs and future growth. How many overall clients access the workload at a time? What is your expected client growth rate? How will future application releases impact your performance requirements?

#### New AWS Cloud native workloads
Answering questions for new workloads involves a different type of planning. You don't always have the information available, so what steps can you take to assist your decision-making process? The following are a few options:
* You can create a test or dev environment to try out the applications using different EBS volume types to measure performance requirements.
* You can evaluate similar workloads as guidance for your new workload.
* Use what is expected from your planning process. What is the expected demand? How many expected clients will there be? What is the underlying application or database? The application or database often provides insights into volume configuration and performance requirements.
* Use monitoring tools available in AWS to monitor and optimize your EBS volumes for performance and costs on a regular schedule.

### Select volume type for workload characteristics
Your volume type decision is made at the individual volume level. You can connect multiple EBS volume types to your EC2 instance. 

With EBS Elastic Volumes, you can make changes as needed to optimize your EBS volumes. EBS Elastic Volumes let you change the volume type, dynamically increase the volume size, and modify performance characteristics. For gp3 and io2 volumes types, you can dynamically change the provisioned IOPS or provisioned throughput performance settings for your volume.

AWS encourages you to use actual test results and your actual performance data to optimize your EBS volume types for price and performance.

#### Workload characteristics questions
* Is your workload more IOPS-intensive or throughput-intensive? If your workload is IOPS-intensive, start with the SSD volume types and review the performance characteristics. If your workload is more throughput-intensive, you can start with HDD volume types to see if their performance can meet your requirements.
* Do the workload requirements exceed the maximum performance characteristics for a selected EBS volume type? If yes, eliminate the volume type from consideration for that volume. Review characteristics for the next higher performing EBS volume type.
* What is the application's latency sensitivity? If it is very low and sub-millisecond to single-digit millisecond latency is needed, io2 Provisioned IOPS might be required. If single-digit to low two-digit latency is tolerable, gp3 General Purpose SSD might be the correct choice. If your workload is not latency sensitive, HDD volume types can be the most cost-effective choice.
* Do you prefer to optimize for price or performance? When comparing the EBS volume types, multiple volumes types can satisfy the requirements. Compare the EBS volume configurations required. Which configuration is more cost effective? Does a configuration offer additional desirable performance characteristics? Is there a trade-off and what is the value to your workload?

### AWS Compute Optimizer for EBS volumes
Once your EBS volumes are in operation, you can monitor them and verify that your volumes are providing optimal performance and cost effectiveness using Compute Optimizer.

Compute Optimizer is a service that analyzes the configuration and utilization metrics of your AWS resources. It reports if your resources are optimized and generates optimization recommendations to reduce the cost and improve the performance of your workloads. 

Compute Optimizer also provides graphs showing recent utilization metric data and projected utilization for recommendations. You can use this information to evaluate which recommendation provides the best price-performance trade-off. 

The analysis and visualization of your usage patterns can help you decide when to move or resize your running resources and still meet your performance and capacity requirements.

Compute Optimizer generates recommendations for EC2 instances, EC2 Auto Scaling groups, EBS volumes, and Lambda functions.

For Compute Optimizer to generate recommendations for these resources, they must meet a specific set of requirements and must have accumulated sufficient metric data.

You must opt in to have Compute Optimizer analyze your AWS resources. The service supports standalone AWS accounts, member accounts of an organization, and the management account of an organization.

After you opt in, Compute Optimizer begins analyzing the specifications and the utilization metrics of your resources from CloudWatch. The Compute Optimizer dashboard displays the optimization findings for your resources.

### Amazon EBS Snapshots
Amazon EBS snapshots creates backup copies of your data in your EBS volumes. Snapshots are stored in a protected part of Amazon S3 as part of the managed service. Storing snapshots on Amazon S3 protects your data with 11 nines of durability and provides you regional access and availability.

### Amazon EBS snapshots overview
Using Amazon EBS snapshots, you can back up the data on your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshot copies. Snapshots are incremental copies of the data, which means that only the blocks on your EBS volumes that have changed after your most recent snapshot are saved. Incremental snapshots minimize the time required to create the snapshot and saves on storage costs by not duplicating previously saved data. Collectively, the volume snapshots contain all of the information for that point in time that is needed to restore your data to a new EBS volume.

When you create a new EBS volume based on a snapshot, the new volume begins as an exact replica of the original volume that was used to create the snapshot. Your data is loaded into the new replicated volume in the background. You can begin to use your new volume immediately while the EBS volume data loads. If you access data that hasn't been loaded yet, the volume immediately downloads the requested data from Amazon S3. Amazon EBS snapshots then continues loading the remainder of the volume's data in the background.

Amazon EBS fast snapshot restore (FSR) lets you create a volume from a snapshot that is fully initialized at creation. FSR eliminates the latency of I/O operations on a block when it is accessed for the first time. Volumes that are created using FSR instantly deliver all of their provisioned performance. FSR must turned on for specific snapshots in specific Availability Zones, and it must be explicitly activated for each snapshot.

When you delete a snapshot, only the data unique to that snapshot is removed. Any information contained in that snapshot that is required by other snapshots remains available and is not deleted.

Snapshot events are tracked through CloudWatch events. An event is generated each time you create a single snapshot or multiple snapshots, copy a snapshot, or share a snapshot. 

With snapshots, you can create backup copies of critical workloads, such as a large database or a file system that spans across multiple EBS volumes. Multi-volume snapshots let you take exact point-in-time, data-coordinated, and crash-consistent snapshots across multiple EBS volumes attached to an EC2 instance.

#### HOW INCREMENTAL SNAPSHOTS WORK
Incremental snapshots provide the point-in-time current state for your EBS volumes. Incremental snapshots use pointers to reference previous data that remains current in the incremental snapshot. Only the current data is retained in each incremental snapshot. 

An initial point-in-time snapshot is created containing all of the data within your EBS volume.
For each incremental snapshot after that, the following occurs:
All new data is copied to the new incremental snapshot.
Previously existing and unchanged data is not copied to the incremental snapshot. The new snapshot references the previously existing unchanged data. Any previously existing data that has been changed or deleted is not included in the new incremental snapshot.
Any saved snapshot contains all of the data or references necessary to restore to that point in time.

#### AVAILABLE SNAPSHOT ACTIONS
Snapshots provide you the capabilities to manage your snapshots manually or by using an automated process. The following options are available: 
* **Create snapshots** – You can create manual snapshots or create snapshot schedules. Snapshots occur asynchronously; the point-in-time snapshot is created immediately, but the status of the snapshot is pending until the snapshot is complete. The snapshot is complete when all modified blocks are transferred to Amazon S3. 
* **Delete snapshots** – You can delete any snapshot whether it is a full or incremental snapshot. When you delete a snapshot, only the data that is referenced exclusively by that snapshot is removed. Unique data is only deleted if all of the snapshots that reference it are deleted.
* **Copy a snapshot** – You can copy a completed snapshot within the same Region or from one Region to another. The snapshot copy receives an ID that is different from the ID of the original snapshot.
* **View snapshot information** – You can view detailed information about your snapshot using the describe-snapshots AWS CLI command or Get-EC2Snapshot command using AWS Tools for PowerShell. You can filter the results based on various fields including tags, specific volume, date ranges, and snapshot owner.
* **Share a snapshot** – By modifying the permissions of a snapshot, you can share it with other AWS accounts that you specify. Authorized users can use the shared snapshots as the basis for creating their own EBS volumes. Shared snapshot copies can be modified by the authorized user; however, your original snapshot remains unaffected.

### Copy and share snapshots
A snapshot is constrained to the Region where it was created. After you create a snapshot of an EBS volume, you can use it to create new volumes in the same Region. You can also copy snapshots across Regions, making it possible to use multiple Regions for geographical expansion, data center migration, and disaster recovery. You can copy any accessible snapshot that has a completed status.

You can share a snapshot across AWS accounts by modifying its access permissions. You can also make copies of snapshots that have been shared with you.

### Encryption support
Snapshots fully support Amazon EBS encryption. To modify volume encryption, you must own the volume or have access to it. Snapshot encryption follows a set of prescribed rules to provide a predictable experience:
* Snapshots of encrypted volumes are automatically encrypted.
* Volumes created from encrypted snapshots are automatically encrypted.
* Volumes created from an unencrypted snapshot can be encrypted during the creation process.
* When you copy an unencrypted snapshot, you can encrypt it during the copy process.
* When you copy an encrypted snapshot, you can re-encrypt it with a different encryption key during the copy process.
* The first snapshot taken of an encrypted volume that was created from an unencrypted snapshot is always a full snapshot.
* The first snapshot taken of a re-encrypted volume that has a different encryption key from the source snapshot is always a full snapshot.

**A new full snapshot copies all of the data in your EBS volume, which results in additional storage costs and can result in additional delay.**

### Amazon Data Lifecycle Manager
You can use Amazon Data Lifecycle Manager to automate the creation, retention, and deletion of snapshots that you use to back up your EBS volumes and Amazon EBS-backed Amazon Machine Images (AMIs). 

Amazon Data Lifecycle Manager uses a combination of elements to automate the lifecycle management process:
* EBS snapshots are one of the primary resource and lifecycle policy types for Amazon Data Lifecycle Manager. 
* Amazon EBS-backed AMIs provide the information that's required to launch an EC2 instance. Amazon EBS-backed AMIs are also primary resources and lifecycle policy types for Amazon Data Lifecycle Manager.
* Target resource tags are used to identify the resources to back up. Tags are customizable metadata that you assign to your AWS resources, including EC2 instances, EBS volumes, and snapshots.
* Amazon Data Lifecycle Manager tags are specific tags applied to all snapshots and AMIs created by a lifecycle policy. These tags distinguish them from snapshots and AMIs created by any other means. You can also specify custom tags to be applied to snapshots and AMIs on creation.
* Lifecycle policies are created using core policy settings to define the automated policy action and behavior.
* Policy schedules determine when and how often the lifecycle policy is ran.

#### LIFECYCLE POLICIES
Lifecycle policy consists of these core settings:
* **Policy type** – Defines the type of resources that the policy can manage. Amazon Data Lifecycle Manager supports two types of lifecycle policies:
 * **Snapshot lifecycle policy** – Used to automate the lifecycle of EBS snapshots. These policies can target EBS volumes and instances.
  * **Cross-account copy event policy** – Used to automate the copying of snapshots across accounts. This policy type should be used with an EBS snapshot policy that shares snapshots across accounts.
 * **EBS-backed AMI lifecycle policy** – Used to automate the lifecycle of EBS-backed AMIs. These policies can target instances only.
* **Resource type** – Defines the type of resources that are targeted by the policy. **Snapshot lifecycle policies** can target **instances** or **volumes**. Use *VOLUME* to create snapshots of individual volumes, or use *INSTANCE* to create multi-volume snapshots of all of the volumes that are attached to an instance. **AMI lifecycle policies** can target **instances only**. One AMI is created that includes snapshots of all of the volumes that are attached to the target instance.
* **Target tags** – Specifies the tags that must be assigned to an EBS volume or an EC2 instance for it to be targeted by the policy.
* **Schedules** – The start times and intervals for creating snapshots or AMIs. The first snapshot or AMI creation operation starts within one hour after the specified start time. Subsequent snapshot or AMI creation operations start within one hour of their scheduled time. 
* **Retention** – Specifies how snapshots or AMIs are to be retained. You can retain snapshots or AMIs based on their total count (count-based) or their age (age-based). 
 * For snapshot policies, when the retention threshold is reached, the oldest snapshot is deleted.
 * For AMI policies, when the retention threshold is reached, the oldest AMI is deregistered and its backing snapshots are deleted.

Amazon Data Lifecycle Manager quotas are the following:
* You can create up to 100 lifecycle policies for each Region.
* You can add up to 45 tags for each resource.

#### POLICY SCHEDULES
Policy schedules define when snapshots or AMIs are created by the policy. Policies can have up to **four** schedules — **one mandatory** schedule and **up to three optional** schedules. 

Adding multiple schedules to a single policy lets you create snapshots or AMIs at different frequencies using the same policy. For example, you can create a **single policy** that creates **daily**, **weekly**, **monthly**, and **yearly** snapshots. This eliminates the need to manage multiple policies. 

For each schedule, you can define the frequency, fast snapshot restore settings (*fsnapshot lifecycle policies only*), cross-Region copy rules, and tags. The tags that are assigned to a schedule are automatically assigned to the snapshots or AMIs that are created when the schedule is activated. In addition, Amazon Data Lifecycle Manager automatically assigns a system-generated tag based on the schedule's frequency to each snapshot or AMI.

Each schedule is activated individually based on its frequency. If multiple schedules are activated at the same time, Amazon Data Lifecycle Manager creates only one snapshot or AMI and applies the retention settings of the schedule that has the highest retention period. The tags of all of the activated schedules are applied to the snapshot or AMI.

### Amazon EBS Architecture
Amazon EBS architecture is built to deliver block storage performance for Amazon EC2. You can use the same connectivity and access methods that you use to reach your EC2 instances to reach your EBS volumes. For example, you can connect using the Internet, a VPN, PrivateLink, or Direct Connect. You can access the service using AWS APIs, the AWS CLI, or the console. As you build your applications, you use a combination of the architectures to deliver the resources you need for your workloads.

#### Basic architecture
The basic Amazon EBS architecture consists of EBS volumes attached to an EC2 instance:
* You can have multiple EBS volumes and different EBS volume types attached to the same instance.
* The EC2 instance and the attached EBS volumes reside in a single Availability Zone. You cannot attach EBS volumes to EC2 instances in a different Availability Zone.
* You can create Amazon EBS snapshots for each of your EBS volumes. The snapshots are stored in an AWS managed S3 bucket within the same Region where your EBS volume resides.
* Access to the EC2 instances and the EBS volumes is controlled using IAM. Users, groups, and roles must have permissions to access the EC2 instance and the EBS volumes.
* You can use any connectivity method to access your resources in your VPC in the Region.  

#### Advanced architecture – Multi-Attach
Amazon EBS Multi-Attach architecture consists of multiple EC2 instances connected to a single EBS volume:
* Multi-Attach is only supported with provisioned IOPS SSD (io1, io2, and io2 Block Express) EBS volume types.
* The EC2 instances and the attached EBS volumes reside in a single Availability Zone. You cannot attach EBS volumes to EC2 instances in a different Availability Zone.
* Amazon EBS does not manage data consistency for multiple writers. Your application or operating system environment must manage data consistency operations.
* You can create EBS snapshots for your Multi-Attach EBS volume. The snapshots are stored in an AWS managed S3 bucket within the same Region where your EBS volume resides.
* Access to the EC2 instances and the EBS volumes is controlled using IAM. Users, groups, and roles must have permissions to access the EC2 instance and the EBS volumes.
* You can use any connectivity method to access your resources in your VPC in the Region.  

#### Advanced architecture – striped volumes
Amazon EBS architecture consists of multiple EBS volumes in a striped redundant array of independent disks (RAID) type configuration. The striped configuration uses a RAID 0 style process to increase the volume size and increase performance for the combined EBS volumes:
* In a striped configuration, the volumes operate as a single EBS volume. 
* A striped EBS volume attaches to a single EC2 instance.
* RAID systems are configured using the operating system of the EC2 instance.
* The EC2 instances and the attached EBS volume reside in a single Availability Zone. You cannot attach EBS volumes to EC2 instances in a different Availability Zone.
* You can create EBS snapshots for your striped EBS volume. The snapshots are stored in an AWS managed S3 bucket within the same Region where your EBS volume resides.
* Access to the EC2 instances and the EBS volumes is controlled using IAM. Users, groups, and roles must have permissions to access the EC2 instance and the EBS volumes.
* You can use any connectivity method to access your resources in your VPC in the Region.

### Knowledge Check
#### What are incremental, point-in-time copies of data stored in Amazon Elastic Block Store (Amazon EBS) volumes known as?
* **Snapshots**
* Instances
* Tags
* Snippets

**Snapshots.** 

The other options are incorrect because of the following: 
* Instances are Amazon EC2 servers. 
* Tags are keywords used for management of data.
* Snippets are pieces of code.

#### A company is working with a consultant in planning to migrate their database workload to the cloud. The database being migrated is I/O-intensive and sensitive to storage performance and consistency. Which Amazon Elastic Block Store (Amazon EBS) volumes would best fit their needs?
* Volumes backed by gp2 General Purpose SSDs
* **Volumes backed by io2 Provisioned IOPS SSDs**
* Volumes backed by gp3 General Purpose SSDs
* Volumes backed by st1 Throughput Optimized HDDs

**io2 Provisioned IOPS SSD volumes** are designed to meet the needs of I/O-intensive workloads, particularly database workloads, that are sensitive to storage performance and consistency. 

The other options are incorrect because of the following:
* gp2 and gp3 General Purpose SSDs are adequate for general use, but they are not optimal for I/O-intensive databases.
* st1 Throughput Optimized HDD-backed volumes are best suited as storage volumes for large, sequential workloads such as Amazon EMR or log processing. HDD-backed volumes are not ideal for database workloads.

#### How are the resources to be backed up in a snapshot identified when using Amazon Data Lifecycle Manager?
* Amazon Data Lifecycle Manager tags
* Encryption keys
* **Target resource tags**
* Retention policies

**Target resource tags** are used to identify the resources to back up. Tags are customizable metadata that users assign to their AWS resources, including EC2 instances, Amazon Elastic Block Store (Amazon EBS) volumes, and snapshots.

The other options are incorrect because of the following: 
* Amazon Data Lifecycle Manager tags are tags that are applied to all snapshots and Amazon Machine Images created by a lifecycle policy. 
* Encryption keys are used to encrypt and decrypt snapshots, not to identify resources.
* Retention policies apply to the snapshot as a whole and determine how long they are retained.

### Summary
* Describing the features and benefits of Amazon EBS
* Identifying Amazon EBS volume types and their performance characteristics
* Identifying the benefits of using Amazon EBS and Amazon EBS optimized instances
* Discussing how to choose between the different types of Amazon EBS instances
* Discussing the use and benefits of Amazon EBS snapshots
* Discussing Amazon EBS lifecycle events

#### Amazon EBS
Amazon EBS is an easy-to-use, high performance, block storage service designed for use with Amazon EC2 for both throughput and transaction-intensive workloads at any scale. Amazon EBS is well suited to both database-style applications that rely on random reads and writes, and to throughput-intensive applications that perform long, sequential reads and writes. 

EBS volumes behave like raw, unformatted block devices. You can mount these block devices as EBS volumes on your EC2 instances. EBS volumes that are attached to an EC2 instance are exposed as raw block storage volumes that persist independently from the life of the instance. 

The AWS block storage portfolio consists of two types of block storage services—instance storage and Amazon EBS—and an integrated snapshot service.

##### Instance store
Instance storage is temporary block-level storage attached to host hardware that is ideal for storing information that frequently changes or is replicated across multiple instances. 

##### Amazon EBS storage
Amazon EBS is a block storage service designed for use with Amazon EC2.  Amazon EBS scales to support virtually any workload and any volume size.

##### Snapshots
Snapshots are incremental, point-in-time copies of your data stored on your EBS volumes. You can use snapshots to restore new volumes, expand the size of a volume, or move volumes across Availability Zones. 

#### Amazon EBS volume types
Amazon EBS provides the following volume types: General Purpose SSD, Provisioned IOPS SSD, Throughput Optimized HDD, Cold HDD, and Magnetic (standard). They differ in performance characteristics and cost, which lets you to tailor your storage performance and cost to the needs of your applications. 

* General Purpose SSD-backed volumes provide a balance of price and performance. AWS recommends these for most workloads. The current General Purpose SSD offering includes gp2 and gp3 volume types.
* Provisioned IOPS SSD-backed volumes provide high performance for mission-critical, low-latency, or high-throughput workloads. The current Provisioned IOPS SSD offering includes io1 and io2 volume types.
* The HDD-backed volumes that Amazon EBS provides fall into two categories: st1 Throughput Optimized HDD volumes and sc1 Cold HDD volumes.
* Magnetic (standard) volumes are not recommended and are generally only used to provide backward compatibility. 

#### Amazon EBS Snapshots
Amazon EBS Snapshots creates backup copies of your data in your EBS volumes. Snapshots are stored in a protected part of Amazon S3 as part of the managed service. You can back up the data on your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshot copies. EBS Snapshots fully support EBS encryption.

### Additional Resources
#### [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)

#### [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html)

## Amazon EFS
### Pre-assessment
#### Which throughput mode is the default for Amazon Elastic File System (Amazon EFS) and is recommended for most workloads?
* Provisioned throughput
* **Elastic throughput**
* General purpose
* Max I/O

**Elastic throughput.**

The other options are incorrect because of the following: 
* Provisioned throughput is recommended for workloads requiring higher throughput-to-storage ratios.
* General purpose and Max I/O are performance modes, not throughput modes.

#### Amazon Elastic File System (Amazon EFS) offers two storage classes, each with their own subtypes. What are those storage classes? (Choose TWO.)
* General Purpose
* Elastic Throughput
* **Standard**
* **One Zone**
* Max I/O

**Standard** and **One Zone**.

The other options are incorrect because General Purpose, Elastic Throughput, and Max I/O are performance and throughput modes.

#### Which of these options are features and benefits provided by Amazon Elastic File System (Amazon EFS)? (Choose TWO.)
* **Serverless**
* Server-based
* Direct-attached
* **Fully managed**
* Rigidity

**Serverless** and **Fully managed**.

The other options are incorrect because of the following: 
* Amazon EFS is a serverless service. 
* When used with Amazon EC2, Amazon EFS does not work as direct-attached storage.
* A major benefit of Amazon EFS is its scalability.

### Amazon EFS Features and Benefits
### Amazon EFS overview
Amazon EFS provides a practical, cloud-native, serverless shared file system that is optimized for cost and performance.

We launched Amazon EFS back in 2016 to give customers a user-friendly, set-and-forget, fully managed, cloud-native file system. You can get up and running in seconds with just a few clicks and have petabyte-scale elastic storage that’s uncomplicated to use. Amazon EFS provides the capabilities and integrations you need to confidently run business-critical applications requiring shared file storage in the cloud.

Let's look at the features and benefits of Amazon EFS:
* Fully managed shared file system
* Scalable storage and performance
* High availability and durability
* Security
* Cost optimization

**Amazon EFS is a shared set-and-forget file system that is convenient and serverless and opens up new possibilities.**

#### Fully managed shared file system
Amazon EFS is serverless, so you don’t need to provision or manage any infrastructure or capacity. 

Amazon EFS file systems can be shared with up to tens of thousands of concurrent clients, no matter the type. These can be traditional EC2 instances. They can be containers running in one of your self-managed clusters. They can be containers running in one of the AWS container services—Amazon Elastic Container Service (Amazon ECS), Amazon EKS, or AWS Fargate. Or they can be in a serverless function running in Lambda.

##### Mountable shared file storage
With Amazon EFS, you can create a file system, mount the file system on your EC2 instances, and then read and write data with multiple clients in your account.

##### File sharing across AWS services
Amazon EFS file systems can be shared with traditional EC2 instances or containers running in one of the AWS container services—Amazon ECS, Amazon EKS, or Fargate. Or they can be in a serverless function running in Lambda.

##### Amazon SageMaker
You can also use Amazon EFS with the AWS machine learning platform SageMaker.

##### Direct Connect and AWS VPN
You can access your Amazon EFS file systems on premises with Direct Connect and AWS VPN.

#### Scalable storage and performance
Amazon EFS provides a scalable elastic file system for use with AWS Cloud services and on-premises resources. A file system can grow to store petabytes of data.

As a managed service, the appropriate storage size is allocated so that you don’t need to worry about administration tasks. Amazon EFS automatically scales capacity out or in to meet your changing storage demands. This scalability means that you avoid overprovisioning storage, and you pay only for storage that you use.

With Amazon EFS, your performance can scale along with your capacity. Your performance can scale to up to tens of gigabytes per second of throughput and over 500,000 IOPS.

##### PERFORMANCE MODES
For every Amazon EFS file system, you will need to choose between one of two performance modes.

**General Purpose** is the default performance mode and is best suited for most workloads. We recommend the General Purpose performance mode for the majority of your Amazon EFS file systems. General Purpose is ideal for latency-sensitive use cases, like web serving environments, content management systems, home directories, and general file serving. If you don't choose a performance mode when you create your file system, Amazon EFS selects the General Purpose mode for you by default.

The **Max I/O** performance mode is recommended for workloads that must scale to higher levels of aggregate throughput and IOPS. This scaling is done with a tradeoff of slightly higher latencies for file metadata operations. Highly parallelized applications and workloads, such as big data analytics, media processing, and genomic analysis, can often benefit from this mode.

##### THROUGHPUT MODES
For every Amazon EFS file system, you can also choose from one of three throughput modes.

**Elastic Throughput** is the default throughput mode when you have spiky or unpredictable workloads and performance requirements that are difficult to forecast or when your application drives throughput at an average-to-peak ratio of 5 percent or less.

**Bursting Throughput** is recommended for workloads that require performance to scale with the amount of data stored in the file system. The larger the file system, the better your performance will be.

**Provisioned Throughput** is recommended for workloads requiring higher throughput-to-storage ratios. It provides higher levels of aggregate throughput for smaller file systems. With Provisioned Throughput mode, you can instantly provision the throughput of your file system (in MiBps) independent of the amount of data stored.

#### High availability and durability
Amazon EFS is highly available and designed to be highly durable. It offers a 99.99 percent availability service-level agreement and is designed for 11 nines of data durability.

##### Availabilty Zones
To achieve availability and durability, all files and directories are redundantly stored within and across multiple Availability Zones. This means that when you write data to Amazon EFS, the write isn’t acknowledged until that data is written across three Availability Zones. Amazon EFS file systems can withstand the full loss of a single Availability Zone while still providing the same quality of service in the other Availability Zones.

##### AWS Backup
For additional data protection, backup services are provided for your Amazon EFS file systems through close integration with AWS Backup. This will also protect data by storing it across multiple Availability Zones. This service is a completely independent software stack. So it provides you diversity in the physical infrastructure and software implementation of your data availability strategy.

#### Security
With Amazon EFS, you control access to your files in multiple ways. 

You can control what network resources have access to your file systems using Amazon VPC routing and security group firewall rules. You can further control user and application access to your file systems using IAM policies and Amazon EFS Access Points. 

##### POSIX PERMISSIONS
You can use Portable Operating System Interface (POSIX)-compliant user-level and group-level permissions to control client access permissions to your file syste

##### AMAZON VPC SECURITY GROUPS
You can restrict access over the network with Amazon VPC security groups. Security groups determine which IP addresses have network visibility to an Amazon EFS endpoint.

##### IAM ROLES
You can create IAM roles to control both the creation and administration of your Amazon EFS file system, in addition to client permissions. For example, you can create an IAM role in your account that has specific permissions for the creation, deletion, or modification of file systems. Then you can grant them to the users in your AWS account. 

Additionally, you can use roles to control client access to your data. NFS clients can identify themselves using an IAM role when connecting to an Amazon EFS file system. When a client connects to a file system through a role, Amazon EFS evaluates the AWS account permissions associated with the role and grants access to data accordingly. When you use IAM authorization for NFS clients, client connections and IAM authorization decisions are logged to CloudTrail for an additional layer of observability.

##### AWS KMS
To protect data at rest, use AWS KMS to manage the keys to encrypt the data that resides in the file system. To encrypt data in transit, you can turn on TLS when you mount the file system.

#### Cost optimization
With Amazon EFS, you pay only for the storage used by your file system, and there is no minimum fee or setup cost. The cost of EFS storage is determined according to the Amazon EFS storage class and the lifecycle management policy you select. By default, newly created EFS file systems use intelligent tiering, automatically cost optimizing the data stored by moving it to the lowest cost tier of storage or optimizing for performance based on how frequently the file is being accessed. The available storage classes include the following:

##### Standard
Amazon EFS Standard and Amazon EFS Standard-Infrequent Access (EFS Standard-IA) offer multi-AZ resilience and the highest levels of durability and availability.

##### One Zone
Amazon EFS One Zone and Amazon EFS One Zone-Infrequent Access (EFS One Zone-IA) offer customers the choice of additional savings by choosing to save their data in a single Availability Zone. Amazon EFS One Zone not only offers lower cost but also provides lower latencies because data replication occurs within a single Availability Zone.

###### Lifecycle management
Lifecycle management monitors your workload and file access patterns. It automatically saves you money by moving files that you’re not accessing frequently from EFS Standard into the lower cost EFS Standard-IA. There’s a generally accepted industry estimate that 80 percent of data isn’t accessed frequently. We actually analyzed our own usage data that we’ve gathered over the past 4.5 years of operation and validated this estimate. 

###### Cost savings
Consider that 80-20 rule, where 20 percent of your files are actively used and the other 80 percent are not. With built-in cost optimization, your effective price is just $0.08 per gigabyte per month for EFS Standard and $0.043 for EFS One Zone.

###### EFS Intelligent-Tiering
EFS Intelligent-Tiering lifecycle management monitors the access patterns of your file system. It moves files that have not been accessed for the duration of the lifecycle policy from EFS Standard or EFS One Zone to EFS Standard-IA or EFS One Zone-IA. This depends on whether your file system uses EFS Standard or EFS One Zone storage classes. If the file is accessed again, it is moved back to EFS Standard or EFS One Zone storage classes.

###### Effective storage price
With Amazon EFS, your effective storage price is just $0.08 per gigabyte per month. The price assumes that you take advantage of Amazon EFS data lifecycle policies. If you do a total cost of ownership analysis, comparing this to running your own file system storage infrastructure, you will find that Amazon EFS is 90 percent more cost effective than doing it yourself.

### Amazon EFS Storage Classes
Amazon EFS offers a range of storage classes designed for different use cases. These include EFS Standard, EFS Standard-IA, EFS One Zone, and EFS One Zone-IA.

#### Before you choose
Choosing a storage class for Amazon EFS is similar to the process you learned about for Amazon S3. Before you decide on a storage class, take the time to analyze your workloads, data access patterns, service-level agreements, and performance requirements to determine the correct storage class or storage classes for your data. 

Here are some questions to get you started:
* What are the application's data requirements for performance? What is your latency tolerance, or do you need millisecond latency?
* Is the data access pattern predictable or unpredictable? Is the data accessed every minute, every hour, daily? Is it accessed only one week a year, or is the access dependent on the project?
* What is the data access pattern?

#### EFS Standard and EFS Standard-IA storage classes
EFS Standard and EFS Standard-IA storage classes are regional storage classes that are designed to provide continuous availability to data, even when one or more Availability Zones in a Region are unavailable. They offer the highest levels of availability and durability by storing file system data and metadata redundantly across multiple geographically separated Availability Zones within a Region.

The EFS Standard storage class is used for frequently accessed files. It is the storage class to which customer data is initially written for Standard storage classes.

The EFS Standard-IA storage class reduces storage costs for files that are not accessed every day. It does this without sacrificing the high availability, high durability, elasticity, and POSIX file system access that Amazon EFS provides. EFS Standard-IA storage is recommended when you need your full dataset to be readily accessible and want to automatically save on storage costs for files that are less frequently accessed. Examples include keeping files accessible to satisfy audit requirements, performing historical analysis, or performing backup and recovery. EFS Standard-IA storage is compatible with all Amazon EFS features and is available in all Regions where Amazon EFS is available.

#### EFS One Zone and EFS One Zone-IA storage classes
EFS One Zone and EFS One Zone-IA storage classes are designed to provide continuous availability to data within a single Availability Zone. The EFS One Zone storage classes store file system data and metadata redundantly within a single Availability Zone in a Region. Because they store data in a single Availability Zone, data that is stored in these storage classes might be lost in the event of a disaster or other fault that affects all copies of the data within the Availability Zone or in the event of Availability Zone destruction.

For added data protection, Amazon EFS automatically backs up file systems using EFS One Zone storage classes with AWS Backup. You can restore file system backups to any operational Availability Zone within a Region, or you can restore them to a different Region. Amazon EFS file system backups that are created and managed using AWS Backup are replicated to three Availability Zones and are designed for durability.

EFS One Zone Standard is used for frequently accessed files. It is the storage class to which customer data is initially written for One Zone storage classes.

The EFS One Zone-IA storage class reduces storage costs for files that are not accessed every day. EFS One Zone-IA storage is recommended when you need your full dataset to be readily accessible and want to automatically save on storage costs for files that are less frequently accessed. EFS One Zone-IA storage is compatible with all Amazon EFS features and is available in most of the Regions where Amazon EFS is available.

#### Comparing Amazon EFS storage classes
This table offers a quick comparison of Amazon EFS storage classes, providing you with use cases, durability, availability, and other considerations.

| Storage class | Designed for | Durability (designed for) | Availability | Availability Zones | Other Considerations |
| ------------- | ------------ | ------------------------- | ------------ | ------------------ | -------------------- |
| EFS Standard | Frequently accessed data requiring the highest durability and availability. | 99.999999999% (11 9s) | 99.99% | >=3 | None |
| EFS Standard-Infrequent Access (IA) | Long lived, infrequently accessed data requiring the highest durability and availability. | 99.999999999% (11 9s) | 99.99% | >=3 | Per GB retrieval fees apply |
| EFS One Zone | Frequently accessed data that doesn't require highest levels of durability and availability. | 99.999999999% (11 9s) | 99.90% | 1 | Not resilient to the loss of the Availability Zone. |
| EFS One Zone-IA | Long lived, infrequently accessed data that doesn't require highest levels of durability and availability. | 99.999999999% (11 9s) | 99.90% | 1 | Not resilient to the loss of the Availability Zone. Per GB retrieval fees apply. |

### Knowledge Check
#### Which **performance mode** is recommended for workloads that must scale to higher levels of aggregate throughput and IOPS?
* Provisioned Throughput
* General Purpose
* Bursting Throughput
* **Max I/O**

The **Max I/O** performance mode is recommended for workloads that must scale to higher levels of aggregate throughput and IOPS.

The other options are incorrect because of the following: 
* Provisioned Throughput is a throughput mode that is recommended for workloads requiring higher throughput-to-storage ratios.
* General Purpose performance mode is the default performance mode for Amazon Elastic File System (Amazon EFS), but Max I/O scales more efficiently.
* Bursting Throughput is the default throughput mode that is recommended for most workloads.

#### A customer requires an Amazon Elastic File System (Amazon EFS) storage class that provides a service-level agreement of 99.99 percent availability. Which storage class would meet that requirement?
* EFS One Zone or EFS One Zone-IA
* **EFS Standard or EFS Standard-IA**
* Elastic Throughput
* Max I/O

**EFS Standard** or **EFS Standard-IA** guarantee an availability of 99.99 percent.

The other options are incorrect because of the following: 
* EFS One Zone or EFS One Zone-IA provide 99.90 percent availability.
* Elastic Throughput and Max I/O are throughput and performance modes.

#### A consultant is working with a client that has spiky and unpredictable workloads that have been difficult to accurately forecast. Which Amazon Elastic File System (Amazon EFS) throughput mode would be most suitable for the customer’s needs?
* Bursting Throughput
* Provisioned Throughput
* Max I/O
* **Elastic Throughput**

**Elastic Throughput** is the default throughput mode when there are spiky or unpredictable workloads and performance requirements that are difficult to forecast or when an application drives throughput at an average-to-peak ratio of 5 percent or less.

The other options are incorrect because of the following: 
* Bursting Throughput is recommended for workloads that require performance to scale with the amount of data stored on the file system. 
* Provisioned Throughput is recommended for workloads requiring higher throughput-to-storage ratios.
* Max I/O is a performance mode that is recommended for workloads that must scale to higher levels of aggregate throughput and IOPS.

### Summary
* Describing the features and benefits of Amazon EFS
* Describing the Amazon EFS storage classes and their uses

#### Features and benefits of Amazon EFS
Amazon EFS provides a practical, cloud-native, serverless shared file system that is optimized for cost and performance.

Features and benefits of Amazon EFS include:
* Fully managed shared file system
* Scalable storage and performance
* High availability and durability
* Security
* Cost optimization

#### Amazon EFS storage classes
Amazon EFS offers a range of storage classes designed for different use cases, including:
* Amazon EFS Standard
* Amazon EFS Standard-IA
* Amazon EFS One Zone
* Amazon EFS One Zone-IA

### Additional Resources
#### [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

#### [Amazon EFS storage classes](https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html)

## Assessment
### 1. What type of storage is the most likely to be used as the primary storage for a relational database?
* **Block storage**
* Archival storage
* File storage
* Object storage

Relational databases may only need to retrieve a single piece of a file, such as an inventory tracking number or employee ID. **Block storage** enables you to retrieve individual blocks of a file rather than the entire file.

The other options are incorrect because of the following:
* File storage is used when files are shared across devices. Block storage offers lower latency for applications like databases.
* Relational databases use a file system for storage and typically use block storage for backups.
* Archival storage is used by databases for backups and compliance, but not as primary storage.

### 2. How is storage throughput defined?
* **The rate at which data can be written into and read from storage system.**
* The number of input and output requests per second that a storage system can support.
* The amount of data that can be stored in a storage system before errors are generated.
* The amount of time to complete read and write requests.

**Throughput is the read/write transfer rate, determined by IOPS x I/O size.**

The other options are incorrect because of the following:
* The amount of time to complete requests is called latency, not throughput.
* The number of inputs and outputs per second (IOPS) is a part of storage throughput. The other part is the size of the data of each request.
* Throughput is a measure of rate, not the amount of data stored.

### 3. A company is preparing to migrate a workload to the AWS cloud. Which of the following steps are necessary to ensure that they choose the right storage type? (Select THREE.)
* Select AWS Support Plan tier
* **Design storage strategy**
* Review capital expenditure requirements
* **Define the workload requirements**
* **Review storage options**
* Review AWS Config recommendations

The steps for choosing the right storage type are **define requirements**, **review your storage options**, and **design your storage strategy**.

The other options are incorrect because of the following:
* Capital expenditure is reduced or eliminated when migrating to any cloud storage option.
* AWS Config does not make recommendations for storage options.
* The Support plan does not directly impact storage decisions.

### 4. When you configure a new Amazon FSx environment, what file systems can you choose? (Select THREE.)
* EXT3
* **Lustre**
* **OpenZFS**
* EXT4
* **NetApp ONTAP**
* Unix File system

When building your Amazon FSx environment, you can choose between four widely-used files systems: **NetApp ONTAP**, **OpenZFS**, Windows File Server, and **Lustre**.

The other options are incorrect because EXT3, EXT4, and Unix filesystems are not supported on FSx.

### 5. A consultant is working with a company that is preparing to migrate their on-premises file system to fully managed storage in the AWS cloud. The on-premises file system uses Netapp ONTAP, and they do not want to modify application code or change how data is managed. Which AWS cloud storage service meets the requirements?
* Amazon EBS
* Amazon S3
* Amazon EC2 instance store
* **Amazon FSx**

**Amazon FSx** lets you choose between four widely used file systems, including Netapp ONTAP. This allows the applications to continue to access the file system without application code or
management

The other options are incorrect because of the following:
* S3 does not offer the full features of the Netapp filesystem.
* EBS is block storage that could be used to host the file system, but this would be self-managed.
* Instance store is ephemeral storage, and is not used for durable storage use cases.

### 6. A student is using an Amazon EC2 instance confiqured with instance store volumes and an Amazon EBS volume attached. After terminating the EC2 instance, and reattaching the EBS volume to a new EC2 instance, the student has found that the data they saved is no longer available. What could be the cause of this data loss?
* The EC2 instance was terminated before the first snapshot completed.
* The EBS volume was automatically wiped when the instance was terminated.
* The new EC2 instance is in a different Availability Zone than the original instance.
* **The data was written to an instance store volume.**

**Data written to the Amazon EC2 instance store persists only as long as the EC2 instance.**

The other options are incorrect because of the following:
* EBS volumes are not automatically wiped, but there is a configurable option to automatically delete them when the instance terminates.
* Snapshots are not involved, since the same EBS volume is being reused.
* It isn't possible to attach the same EBS volume to an instance in a different AZ.

### 7. A company's networking team is planning an upcoming migration using AWS Transfer Family, and they need to know which transfer protocols can be used. The company requires end-to-end encryption of the data during the transfer. What secure transfer protocols are supported by AWS Transfer Family? (Select THREE.)
* **Applicability Statement 2 (AS2)**
* **File Transfer Protocol Secure (FTPS)**
* Hypertext Transfer Protocol (HTTP)
* Trivial File Transfer Protocol (TFTP)
* **Secure File Transfer Protocol (SFTP)**
* Server Message Block (SMB)

AWS Transfer Family supports **FTPS**, **SFTP**, and **AS2** protocols, as well as File Transfer Protocol (FTP).

The other options are incorrect because of the following:
* SMB is not a supported protocol.
* TFTP and HTTP are not supported and do not provide encryption.

### 8. What AWS data migration service completes a migration job with a full erasure of the device that follows the National Institute of Standards and Technology (NIST) guidelines?
* Amazon S3 Transfer Acceleration
* AWS DataSync
* **AWS Snow Family**
* AWS Transfer Family

**AWS Snow Family** uses purpose-built devices to transfer data offline. AWS performs a full erasure of the device that follows the National Institute of Standards and Technology guidelines for media sanitization.

The other options are incorrect because of the following:
* DataSync transfers your data over a network. It doesn't retain a local copy.
* Transfer Family is typically for ongoing transfer of data into and out of the AWS cloud. It does not automatically wipe the storage.
* S3 Transfer Acceleration transfers your data over a network. It doesn't retain a local copy.

### 9. A consultant is working with an organization that conducts maritime research in remote sectors of the Atlantic Ocean. These areas have minimal satellite coverage, which limits network connectivity. The organization needs the ability to collect and process sensor data before shipping it to AWS. What data storage solution meets the requirements?
* AWS Transfer Family
* AWS DataSync
* **AWS Snowball Edge**
* AWS Snowmobile

**AWS Snowball Edge** is purpose-built for extremely remote locations that have little to no connectivity. AWS Snowball Edge can be used for data collection, machine learning and processing, and storage.

The other options are incorrect because of the followinq:
* Snowmobile does not provide compute capability to process the data and is not for shipboard use.
* DataSync requires a network connection to operate.
* Transfer requires a network connection to operate.

### 10. A large company is planning to migrate their data storage to the AWS cloud. What are the phases of a large migration process? (Select THREE.)
* Discover
* **Assess**
* Deploy
* **Mobilize**
* **Migrate and Modernize**
* Provision

AWS defines the three-phase migration process as: **Assess**, **Mobilize**, and **Migrate and Modernize**.

The other options are incorrect because of the following:
* Backup and Restore is one possible migration strategy, but it is part of Migrate and Modernize.
* Deploy is part of Migrate and Modernize.
* Lift and Shift is part of Migrate and Modernize.
* Account provisioning is done as part of the Mobilize phase.

### 11. What cloud migration strategy is also known as lift and shift?
* Refactor
* **Rehost**
* Repurchase
* Retain

The **Rehost** strategy is also known as lift and shift. Using this strategy, you move your applications from your source environment to the AWS cloud without making any changes to the application.

The other options are incorrect because of the following:
* Repurchase is used when you are purchasing an SaaS product to replace an application.
* Retain is the strategy for applications you will not migrate.
* Refactor is used when you modify your application architecture to use cloud-based services.

### 12. While planning for a cloud migration, a company discovers that there has not been an inbound connection to one of their applications in 90 days. What migration strategy would be preferred in this situation?
* **Retire**
* Replatform
* Rehost
* Repurchase

**Retire** is the strategy that best applies. ldle applications are often discovered during a migration. These should be retired to avoid paying to host an unused application and its associated storage.

The other options are incorrect because of the following:
* Rehost is used when migrating an application as-is.
* Repurchase is used when you are purchasing an SaaS product to replace application.
* Replatform is used when you optimize your application to leverage the cloud.

### 13. A company wants to migrate to a hybrid storage solution but doesn't want to have to modify their existing applications. Which storage network protocols are part of the standard set supported by AWS Storage Gateway? (Select THREE.)
* Fibre Channel over Ethernet (FCOE)
* **Network File System (NFS)**
* **Server Message Block (SMB)**
* Fibre Channel (FC)
* InfiniBand
* **Internet Small Computer Systems Interface (iSCSI)**

AWS Storage Gateway supports **NFS**, **SMB**, and **iSCSI** storage protocols.

The other options are incorrect because of the following:
* Fibre Channel isa storage protocol that usually uses fiber optic links connected to SAN storage and is not supported by Storage Gateway.
* InfiniBand is typically used for High Performance Computing, which is not a use case for Storage Gateway, and not supported.
* Similar to Fibre Channel, but uses an Ethernet network. Also not supported by Storage Gateway.

### 14. A company's applications need low-latency access to frequently used data. Which deployment options for Storage Gateway will provide the LOWEST latency? (Select TWO.)
* Deploy Storage Gateway on an Amazon EC2 instance in the AWS cloud.
* **Deploy a Storage Gateway VM image locally on any supported host platform.**
* Deploy a Storage Gateway container image on Amazon ECS.
* Deploy a Storage Gateway docker container image as an AWS Lambda function.
* **Deploy a Storage Gateway hardware appliance.**

Storage Gateway can be configured to locally cache frequently accessed data running in the data center as a **VM** or **hardware appliance**.

The other options are incorrect because deploying Storage Gateway in the cloud means the data will not be cached locally.

### 15. Which factors would make a company consider a hybrid cloud rather than a full cloud migration? (Select TWO.)
* Requirements to store data with high durability.
* Requirements to store data with high availability.
* Requirements to encrypt data at rest.
* **Compliance requirements for data residency.**
* **On-premises applications with single-millisecond latency requirements.**

Use cases for hybrid cloud include **security and compliance requirements for data residency**, and the need **for on-premises application to have single-digit millisecond access to data**.

The other options are incorrect because of the following:
* Durability of data typically is typically far better on the cloud than on-premises.
* Encryption is built in to AWS storage services.
* Most AWWS storage services are highly available by default.

### 16. A company that offers object storage for their customers has reached the limit of 100 buckets in their AWS account. How can they continue to create more buckets?
* Configure the buckets to use S3 One Zone-IA for the storage class.
* Log in to the account as the root user and create the additional buckets.
* **Visit the Service Quotas console and request that the limit to be increased.**
* Confiqure buckets in multiple AWS Regions.

Amazon S3 has a maximum bucket limit of 100 per account, but this can be increased to a **maximum of 1,000 per account with a service limit increase request**.

The other options are incorrect because of the following:
* The limit is per account, which represents the total number of buckets in all Regions.
* The root does not have privileges to exceed service limits.
* One zone storage classes do not allow more buckets to be created.

### 17. Which Amazon S3 storage class delivers the lowest cost storage for long-lived, rarely accessed data that requires retrieval in milliseconds?
* S3 Glacier Deep Archive
* S3 Standard-IA
* S3 Glacier Flexible Retrieval
* **S3 Glacier Instant Retrieval**

**S3 Glacier Instant Retrieval** is an archive storage class that delivers the lowest cost storage for long-lived, rarely accessed data that requires retrieval in milliseconds.

The other options are incorrect because of the following:
* S3 Glacier Instant Retrieval is 5x less costly than Standard-IA.
* S3 Glacier Flexible Retrieval has a minimum retrieval time of one minute.
* S3 Glacier Deep Archive has a minimum retrieval time of 12 hours.

### 18. AnyCompany (anycompany.com) is using Amazon S3 as their storage solution. An administrator has been asked to create a new bucket for a project, with the requested bucket name of any_company_planning. However, the bucket creation failed. What is a cause of the error?
* The bucket name must contain both letters and numbers.
* The bucket name must use the company's unique domain name.
* **The bucket name cannot contain underscores.**
* The bucket name must contain both lowercase and uppercase letters.

Bucket names must consist of **only lowercase letters, numbers, dots, and hyphens**.

The other options are incorrect because of the following:
* Bucket names cannot contain uppercase letters.
* Bucket names can contain the company's domain name, but it's not required.
* Numbers are not required in bucket names.

### 19. What are some common use cases for bucket tags?
* To store encryption keys.
* To classify the confidentiality level of objects.
* **To allocate storage costs to specific projects.**
* To categorize objects.

**Cost allocation** is a primary use case for bucket tags. These can be viewed in AWS Cost Explore, AWS Budgets, and AWS Cost and Usage reports.

The other options are incorrect because of the following:
* Object tags are used for categorizing objects.
* Object tags are used for data classification of objects.
* Encryption keys are never stored in tags, since they are visible as plain text.

### 20. In preparation for a new project, a Project Manager (PM) for AnyBank has just created an Amazon S3 bucket, and migrated 100 terabytes of data to the Amazon S3 Standard storage class. They also decommissioned the on-premises storage system. The project has just been put on hold for three months, and the data will not be accessed during this time. How can the PM minimize the storage costs, while the project is on hold, without lowering the durability?
* Configure AWS Storage Gateway in the bucket Region, and immediately copy the data to the
storage.
* Immediately move the data to Amazon EBS Cold HDD volumes.
* Wait 30 days and move the objects to the Amazon S3 Standard-lA storage class.
* **Immediately move the objects to the Amazon S3 Glacier Deep Archive storage class.**

The PM can save costs by immediately moving the objects to Amazon S3 Glacier Deep Archive.

The other options are incorrect because of the following:
* Using HDD volumes will lower the durability to 99.8%.
* There is no reason to wait 30 days, since the Standard storage class does not have a minimum duration. Standard-IA is about half the cost of Standard, but since the objects don't need be accessed for three months, Glacier Deep Archive is the best option.
* The costs for Storage Gateway will be greater than the costs for directly storing the data in S3.

### 21. A company needs to share business-critical data across multiple EC2 instances. What requirements need to be met for a single EBS volume to be attached to multiple instances? (Select THREE.)
* The EBS volume type must be General Purpose SSD (gp2 or gp3) volumes.
* The instances must be running on the same host machine.
* The instances must all be the sanme type and size.
* **The EBS Volume type must be Provisioned IOPS SSD (io1 or io2) volumes.**
* **The instances must be in the same Availability Zone.**
* **The instances must be built on the Nitro System.**

Multi-Attach supports a single EBS volume to be concurrently attached to up to 16 **Nitro-based EC2 instances** within the **same Availability Zone**. The EBS volume **must use Provisioned IOPS SSD (io1 and io2) volumes**.

The other options are incorrect because of the following:
* General purpose EBS volumes do not support Multi-Attach.
* The instances can be on different hosts.
* The instances can be different types and sizes.

### 22. To save storage costs, a Systems Administrator deleted some of the Amazon EBS snapshots associated with a volume storing critical financial data. A Cloud Application Developer then tries to create a new volume using the latest snapshot for the financial data volume. What financial data will be available on the new EBS volume?
* **All of the data that was on the volume at the time of the latest snapshot.**
* None of the data will be available on the new volume.
* Only the data that was not saved in the deleted snapshots.
* Only the data contained on the oldest remaining snapshot.

When snapshots are deleted, only the data that isn't needed to restore the remaining snapshots is deleted. **All of the data from the snapshot will be available.**

The other options are incorrect because of the following:
* Data needed to restore the remaining snapshots will not be deleted.
* Any remaining snapshot can be restored, and it will contain all of the data at that point in time.

### 23. What is the primary advantage of configuring multiple EBS volumes as a striped RAIDO array?
* Increased availability of the data.
* **Increased storage throughput and IOPS.**
* Reduced boot time of the operating system
* Increased durability of the data.

With RAID 0, I/O is distributed across the volumes in a stripe. If you add a volume, you get the straight **addition of throughput and IOPS**.

The other options are incorrect because of the following:
* Since the data is not replicated across the volumes, there is no increase in durability or availability.
* Booting from a RAID volume is not recommended, due to not being able to boot your system if one device fails. Since the boot loader typically runs on only one device in the array, and the RAID controller adds an additional step to the boot process, boot time is likely to increase.

### 24. A consultant is working with a biotech company that specializes in genomic analysis.  They are migrating their highly parallelized workload to Amazon EFS, and the consultant is tasked with recommending the correct configurations for their new deployment. Which Amazon EFS performance mode is best suited for this workload?
* Bursting Throughput
* General Purpose
* Elastic Throughput
* **Max I/0**

The **Max I/O** performance mode is recommended for highly parallelized applications and workloads.

The other options are incorrect because of the following:
* General Purpose performance is ideal for latency-sensitive use cases. It is not as efficient as Max I/O in scaling to higher levels of aggregate throughput and IOPS that is needed by highly parallelized workloads.
* Elastic Throughput focuses on providing adequate throughput for spiky and unpredictable workloads. It is only available for file systems configured with the General Purpose performance mode.
* Bursting Throughput focuses on providing adequate throughput for workloads that scale with the amount of data stored in the file system, but because bursting is based on a credit system, it cannot ensure consistent performance.

### 25. A user is writing data to their Amazon EFS file system using the EFS Standard storage class. At what point is the write acknowledged by Amazon EFS?
* After the data has been written to at least one Availability Zone.
* After the data has been written to AWS Backup.
* **After the data has been written across three Availability Zones.**
* Immediately after the write request is received.

When data is written to Amazon EFS using the EFS Standard storage class, the write isn't acknowledged **until the data is written across three Availability Zones**, providing for redundancy and high availability.

The other options are incorrect because of the following:
* When data is written to Amazon EFS using the EFS Standard storage class, the write isn't acknowledged until the data is written across three Availability Zones, providing for redundancy and high availability.
