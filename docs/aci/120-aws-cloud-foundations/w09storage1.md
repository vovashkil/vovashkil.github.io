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

