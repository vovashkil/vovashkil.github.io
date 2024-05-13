###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Compute 1
## Compute as a Service
### Virtual machines
Virtual machines are virtual computers that run within another physical computer.

The main service to run virtual machines on AWS is Amazon EC2, which you will learn about in this module.

### Containers
A container is a standardized unit that packages your code and its dependencies. Instead of virtualizing an entire machine including the operating system and the physical hardware, containers virtualize only the software layer.

AWS services for container technology include Amazon ECS,  Amazon ECR, Amazon EKS, and AWS Fargate.

### Serverless
If you want to deploy your workloads and applications without having to manage resources, you can do that on AWS with serverless compute services such as AWS Lambda or Fargate.

## Amazon EC2
EC2 instances give you a lot of flexibility and control in the cloud, and you can configure them to meet your needs. You can provision one or many instances easily. And at the end of the billing cycle, you only pay for what you use, either per second or per hour depending on the type of the instance. When you no longer need an instance, you can terminate or stop the instance and you will stop incurring charges.

Not all servers are the same and you are probably looking to run a specific type of operating system on your EC2 instance. AWS supports a range of operating systems, including Linux, macOS, Ubuntu, Windows, and more. To select the operating system for your server, you must choose an Amazon Machine Image, or an AMI. The AMI contains information about how you want your instance to be configured, including the operating system, possible applications to be pre-installed on that instance upon launch, and other configurations. You can launch one or many instances from a single AMI, which would create multiple instances that all have the same configurations. Some AMIs are provided by AWS, whereas others are provided by the community and can be found using the AWS Marketplace. Or you can build your own custom AMIs as needed. For example, Amazon Linux 2 is the AMI we selected when we launched our employee directory application. This AMI is provided by AWS, and it is essentially a pre-built EC2 optimized Linux image that has long-term support provided by AWS.

Beyond the properties determined by the AMI, you can also configure the instance type and size, which correspond to the amount of compute, memory, and network capabilities available per instance. Different applications have different hardware requirements, and choosing the instance type for your application gives you the ability to pick the hardware that it runs on. It's also really nice that you have a wide variety of choices as it's hard to achieve that same level of variety with on-premises resources.

 

The instance types you can choose from are grouped for use cases like compute optimized, memory optimized, storage optimized instances, and more. There is a list of instance types that you can find in the AWS documentation, and you can expect this page to be updated regularly as new instance types are released. For example, the G instance family are optimized for graphics-intensive applications, which will work best for use cases such as 3D visualizations or video encoding, whereas the M5 general purpose EC2 instance family provides a balance of resources and are great for applications that use these resources in equal proportions, like web servers, our employee directory application example, or code repositories.

When you are launching an EC2 instance, you will see something like this when selecting an instance type and size. The t3 or a1 is the instance type that determines the blend of hardware capabilities. Then the dot, then the size, like small, medium, large. It goes down to nano and up to many, many, extra-large sizes. The great thing about this type of selection existing right at your fingertips is that you are no longer locked into hardware decisions upfront. You can choose an initial EC2 instance type, evaluate its performance for your specific use case, and then later change to a different type that is better suited for the application. EC2 is also resizable with a few clicks in the console or can be done programmatically through an API call. All of these configurations being available to you via API enables you to embrace change over time easily as your workloads mature and change.

So, ok, virtual machines are cool and totally not new. So how exactly does this impact your business? Well, the important thing is this: the flexible and low-cost nature of EC2 instances as well as the ease of provisioning servers allows for programmers and businesses to innovate more quickly by spinning up servers for a short amount of time to run experiments and find optimal configurations for your applications. EC2 offers a wide variety of hardware options to choose from, so you can optimize for your solutions by selecting the right EC2 instance type for your application. And then you can optimize even further by right sizing the resource or selecting an instance size that is appropriate for your application and not over-provisioning like is often done on premises. This type of optimization is hard to achieve on your own because with traditional on-premises deployments, you are working with hardware constraints that simply don't exist in the same way with the cloud. The ability to adapt to changes and choose really specific configurations for your virtual machines all through a couple of API calls is very powerful. And EC2 is really just the beginning of the story.

### EC2 instance types
#### INSTANCE TYPES
* An instance type is the combination of virtual hardware components, such as virtual CPU (vCPU) and memory, that make up the instance.
* Instance types are grouped together into instance families. Each instance family is optimized for specific types of use cases. You will learn more about instance families later.
* Instance families have subfamilies, which are grouped according to the combination of processer and storage used.

#### INSTANCE ARCHITECTURE
Amazon EC2 offers you the option to run Intel, AMD, and ARM (Graviton) architectures.

Here are some examples of how the different architectures are named:
* Intel – c5, m5, r5
* AMD – c5a, m5a, t3a
* AWS Graviton – c6g, m6g

Different instance types might use the same or different CPU architecture. Different architectures can have different CPU-to-memory ratios.

Depending on your workload and cost considerations, using AMD or Graviton instances, based on the ARM architecture, can offer significant benefits.

#### INSTANCE GENERATION
Newer generations offer new or improved features and cost-savings opportunities.

Here are some examples:
* AWS Nitro System – Better performance and price with enhanced security
* Enhanced networking – Significant additional network and throughput to the storage volumes for Amazon Elastic Block Store (Amazon EBS)
* New architectures – ARM-based instances or sometimes newer Intel and AMD CPU generations*
*Multiple CPU generations can exist within a single instance generation.

#### OPERATING SYSTEMS
AMIs are available for Linux, Windows, and macOS:
* Amazon Linux 2 or Amazon Linux 2023 are Amazon Linux-based optimized implementations. Other Linux implementations such as Ubuntu, Redhat, SUSE Linux, and Debian are available.
* Windows is available through Windows Server 2016, 2019, or 2022.
* MacOS is available for developing, building, testing, and signing applications for Apple devices:
 * EC2 x86 Mac instances (mac1.metal) are built on 2018 Mac mini hardware powered by 3.2 GHz Intel eighth generation (Coffee Lake) Core i7 processors. 
 * EC2 M1 Mac instances (mac2.metal) are built on 2020 Mac mini hardware powered by Apple Silicon M1 processors.

### Instance families
The AWS instances are currently categorized into five distinct families. 

#### General purpose
General purpose instances provide a balance of compute, memory, and networking resources and can be used for a wide range of workloads.

Use cases: These instances are ideal for applications that use these resources in equal proportions, such as web servers and code repositories.

Burstable instance options: Many workloads are not busy all the time and do not require sustained CPU performance. Using a large instance for these low-to-moderate workloads leads to waste and unnecessary cost. 

For these workloads you can take advantage of the low-cost burstable general purpose instances, which are the T family instances. A burst is when the activity on the instance exceeds normal operation for a short period—for example, when the workload temporarily spikes. The T instance family provides a baseline CPU performance with the ability to burst above the baseline at any time for as long as required. The T instances offer a balance of compute, memory, and network resources. They provide you with the most cost-effective way to run a broad spectrum of general purpose applications that have a low-to-moderate CPU usage. 

Example of general purpose instances are M6a, M6g, M6gd, M6i, M6id, M6idn, M6in, M7g, T4g

Mac is available only as general purpose instances.

#### Compute optimized
Compute optimized instances are ideal for compute-bound applications that benefit from high-performance processors. Instances belonging to this family are well suited for compute-intensive operations.

Use cases include the following:
* Batch processing workloads
* Media transcoding
* High-performance web servers
* High performance computing (HPC)
* Scientific modeling
* Dedicated gaming servers and ad server engines
* Machine learning (ML) inference

Examples of general purpose instances are C6a, C6g, C6gd, C6gn, C6i, C6id, C6in, C7g, and Hpc6a.

#### Memory optimized
Memory optimized instances are designed to deliver fast performance for workloads that process large datasets in memory.

Use cases include the following:
* High-performance relational (MySQL) and NoSQL (MongoDB, Cassandra) databases
* Distributed web scale cache stores that provide in-memory caching of key-value type data (Memcached and Redis)
* In-memory databases using optimized data storage formats and analytics for business intelligence (for example, SAP HANA)
* Applications performing real-time processing of big unstructured data (financial services, Hadoop and Spark clusters)
* HPC and electronic design automation applications

Examples are Hpc6id, R6a, R6g, R6gd, R6i, R6id, R6idn, R6in, R7g, X2gd, X2idn, and X2iedn.

#### Storage optimized
Storage optimized instances are designed for workloads that require high, sequential read and write access to very large datasets on local storage. They are optimized to deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to applications.

Use cases include the following:
* Massive parallel processing data warehouses
* MapReduce and Hadoop distributed computing
* Log or data processing applications
* NoSQL databases
* Cache for in-memory databases (for example, Redis)
* Data warehousing applications
* Distributed file systems

Examples are I4i, Im4gn, Is4gen, D2, D3, and H1.

#### Accelerated computing
Accelerated computing instances use hardware accelerators, or coprocessors, to perform some functions more efficiently than is possible in software running on CPUs. Examples of such functions include floating point number calculations, graphics processing, and data pattern matching. Accelerated computing instances facilitate more parallelism for higher throughput on compute-intensive workloads.

If you require high processing capability, you will benefit from using accelerated computing instances, which provide access to hardware-based compute accelerators such as graphics processing units, field-programmable gate arrays, or AWS Inferentia.

Use cases include the following:
* Video rendering
* Video processing
* Analytics (big data)
* Artificial intelligence and ML
* Examples are G5g, Trn1, F1, G3, VT1, P3, and P4.

### Instance sizing
EC2 instances are sized based on the combined hardware resources consumed by that instance type. This means the size is the total configured capacity of vCPU, memory, storage, and networking. The sizes range from nano to upwards of 32xlarge, with a nano-sized instance using the least amount of hardware resources and the 32xlarge instance using the most amount of hardware resources (128 vCPU and 1,024 gibibyte (GiB) memory). 

Let's take a quick look at a size comparison chart to help you understand how the allocated hardware corresponds to the instance size. For the general-purpose T instance family, the vCPU allocation remains the same, but the memory doubles with each larger size. Review the following chart to understand the way the instance memory increments. 

Instance Family		Instance Size	vCPU	Memory (GiB)
General purpose 	t4g.nano	2	0.5
General purpose         t4g.micro	2	1
General purpose		t4g.small	2	2
General purpose		t4g.medium	2	4
General purpose		t4g.large	2	8

### Instance family growth
Different instance families grow based on the resource for which the family is optimized. The following table shows the compute optimized growth and how it focuses on vCPU resources and the memory optimized growth and how it focuses on the memory resources. Review the following chart to understand the way different instance families increment vCPU and memory. 

Instance Family	Instance Size	vCPU	Memory (GiB)
Compute optimized	c5.xlarge	4	8
Compute optimized	c5.2xlarge	8	16
Compute optimized	c5.4xlarge	16	32
Memory optimized	r5.xlarge	4	32
Memory optimized	r5.2xlarge	8	64
Memory optimized	r5.4xlarge	16	128

### Deconstructing instance type names
The first position in the instance type indicates the instance family. In this example, the "c" tells us that this instance type is from the "compute optimized family".

The second position indicates the instance generation. In this example the instance generation is "5". 

The remaining letters before the period indicate additional capabilities. Here we see an "n", before the period, indicating that the instance is also network optimized.

After the period is the instance size, there is either a number followed by a size, such as 9xlarge in this example, or the word  "metal", indicating a bare metal instance.

### EC2 instance families
#### c5 instances are the fifth generation of compute optimized instances.

Model	vCPU	Memory	Instance Storage (GB)	Network Bandwith (Gbps)	EBS Bandwidth (Mbps)
c5.large	2	4	EBS-Only	Up to 10	Up to 4,750
c5.xlarge	4	5	EBS-Only	Up to 10	Up to 4,750
c5.24xlarge	96	192	EBS-Only	25	19,000
c5d.xlarge	4	8	1 x 100 NVMe SSD	Up to 10	Up to 4,750

### EC2 instance tenancy
A tenant is an entity that occupies space, whether that space is a rented apartment in a building you own or an instance occupying resources on AWS infrastructure. With Amazon EC2, tenancy defines how the EC2 instances are distributed across the physical hardware. Tenancy choices also have an effect on pricing. These are the three available tenancy options:
* Shared tenancy (default),
* Dedicated Host,
* and Dedicated Instance.

#### SHARED TENANCY
Shared tenancy is the default tenancy for EC2 instances. Shared tenancy means that when you launch your instance, the instance is created on an AWS server that you share with many other different AWS customer accounts. Your instance is isolated and secured from the other user's instances, but you are all sharing the same underlying hardware. 

Shared tenancy is the most economical choice and can support Spot Instances and burstable instance types. Shared tenancy doesn’t support instances that use the Bring Your Own License (BYOL) model.

#### DEDICATED HOST
An Amazon EC2 Dedicated Host is a physical server where all the instance capacity is fully dedicated to your use. With Dedicated Hosts, you can use your existing per-socket, per-core, or per-virtual machine (VM) software licenses, including Windows Server, Microsoft SQL Server, SUSE, and Linux Enterprise Server. The following are a few reasons why you might you choose a Dedicated Host: 
* For compliance, security, or licensing reasons, some organizations must run their instances on dedicated servers. With Dedicated Hosts, you rent a physical server that is solely dedicated to your instances.
* Dedicated Hosts provide visibility and the option to control how you place the instances on your physical server. This facilitates instance deployment using specific location configurations that address corporate compliance and regulatory requirements.
* Dedicated Hosts also give you control and visibility into the underlying hardware of the host. By using Dedicated Hosts, you can use the BYOL model. There is no additional charge for software usage if you choose to bring your own licenses.
* You can also use Windows Server Amazon Machine Images (AMIs) provided by Amazon to run the latest versions of Windows Server on Dedicated Hosts. This is common for scenarios where you have existing SQL Server licenses eligible to run on Dedicated Hosts but need Windows Server to run the SQL Server workload.

Windows Server AMIs provided by Amazon are supported on current generation instance types only.

#### DEDICATED INSTANCE
Dedicated Instances are EC2 instances that run on hardware that's dedicated to a single customer. Dedicated Instances can share hardware with other instances from the same AWS account that are not Dedicated Instances. For example, you have two Dedicated Instances that need to run on hardware allocated to your account. You then launch two additional regular instances that can be run on any hardware. But because you have hardware dedicated to your account, you can place these two additional regular instances on that Dedicated Instance hardware. 

Dedicated Instances and Dedicated Hosts can both be used to launch EC2 instances onto physical servers that are dedicated for your use. An important difference between a Dedicated Host and a Dedicated Instance is that a Dedicated Host gives you additional visibility and control over how instances are placed on a physical server. And you have greater visibility into the hardware that the instance is running on.

With a Dedicated Instance, only instances owned by you can run on the hardware, but you have no visibility into the underlying hardware or control of instance placement. Dedicated Instance pricing has two components: an hourly per-instance usage fee and a dedicated fee for each AWS Region. (You pay this once per hour regardless of how many Dedicated Instances you're running.)

### Amazon EC2 pricing
#### On-Demand Instances
With On-Demand Instances, you pay for compute capacity by the hour or by the second depending on which instances you run. No longer-term commitments or upfront payments are needed. You can increase or decrease your compute capacity depending on the demands of your application and only pay the specified rates for the instance you use.

On-Demand Instances are recommended for the following:
* Users who prefer the low cost and flexibility of Amazon EC2 without any upfront payment or long-term commitment
* Applications with short-term, irregular, or unpredictable workloads that cannot be interrupted
* Applications being developed or tested on Amazon EC2 for the first time

Sample use cases for On-Demand Instances include developing and testing applications and running applications that have unpredictable usage patterns. On-Demand Instances are not recommended for workloads that last a year or longer because these workloads can experience greater cost savings using Reserved Instances.

#### Reserved Instances
Reserved Instances (RIs) are a billing discount applied to the use of On-Demand Instances in your account. You can purchase Standard RIs and Convertible RIs for a 1-year term or a 3-year term. You realize greater cost savings with the 3-year option.

There are two types of RIs to choose from:
* Standard RIs: These provide the most significant discount (up to 72 percent off On-Demand) and are best suited for steady-state usage.
* Convertible RIs: These provide a discount (up to 66 percent off On-Demand) and the capability to change instance families, operating system types, and tenancies while benefitting from RI pricing. Like Standard RIs, Convertible RIs are best suited for steady-state usage.

RIs are recommended for the following:
* Steady-state loads and long-running systems
* Core components with minimal high peaks and valleys of usage

At the end of an RI term, you can continue using the EC2 instance without interruption. However, you are charged On-Demand rates until you do one of the following:
* Terminate the instance.
* Purchase a new RI that matches the instance attributes (instance type, Region, tenancy, and platform).

#### Spot Instances
With Spot Instances, you can request spare Amazon EC2 computing capacity for up to 90 percent off the On-Demand price.

Spot Instances are recommended for the following:
* Applications that have flexible start and end times and can tolerate interruptions
* Applications that you want to run or test only when the compute prices are in your price range
* Applications that are a lower priority in your environment
* Users with urgent computing needs for large amounts of additional capacity at a price they determine

Suppose that you have a background processing job that can start and stop as needed (such as the data processing job for a customer survey). You want to start and stop the processing job without affecting the overall operations of your business. If you make a Spot request and Amazon EC2 capacity is available, your Spot Instance launches. However, if you make a Spot request and Amazon EC2 capacity is unavailable, the request is not successful until capacity becomes available. The unavailable capacity might delay the launch of your background processing job.

After you have launched a Spot Instance, your instance might be interrupted for three reasons:
* Capacity: Amazon EC2 can interrupt your Spot Instance when it needs it back.
* Price: The Spot price is higher than your maximum price.
* Constraints: If your Spot request includes a constraint such as a launch group or an Availability Zone group, the Spot Instances are terminated as a group when the constraint can no longer be met.

This might not pose any issues for your background processing job. However, in the earlier example of developing and testing applications, you would probably want to avoid unexpected interruptions. Therefore, choose a different EC2 instance type that is ideal for those tasks.

### Saving Plans
As an alternative to reserved instances, AWS offers three types of Savings Plans:
* Compute Savings Plans apply to usage across Amazon EC2, Lambda, and Fargate.
* EC2 Instance Savings Plans apply to Amazon EC2 usage.
* Amazon SageMaker Savings Plans apply to SageMaker usage.

With EC2 Instance Savings Plans, you can reduce your compute costs by committing to a consistent amount of compute usage for a 1-year term or a 3-year term. This term commitment results in savings of up to 72 percent over On-Demand costs for the EC2 instance Savings Plans.

Any usage up to the commitment is charged at the discounted plan rate (for example, $10 an hour). Any usage beyond the commitment is charged at regular On-Demand rates.

### Dedicated Hosts
You can also pay for Dedicated Hosts, which provide EC2 instance capacity on physical servers dedicated for your use. Dedicated Hosts can help you reduce costs by letting you use your existing server-bound software licenses, including Windows Server, SQL Server, and SUSE Linux Enterprise Server (subject to your license terms). They can also help you meet compliance requirements.

Dedicated Hosts can be purchased in the following ways:
* On-Demand (hourly)
* As a reservation for up to 70 percent off the On-Demand price
* Use Savings Plans to lower your spend on Dedicated Hosts

Dedicated Hosts are recommended for the following:
* Workloads that require server-bound software licenses
* Security and regulatory compliance where your workload cannot share hardware with other tenants

The majority of EC2 instances run on hardware known as the AWS Nitro System. The AWS Nitro System is built specifically to run instances in the most optimal fashion possible. The AWS Nitro System is a combination of dedicated hardware and a lightweight hypervisor for faster innovation and enhanced security.

### Flexibility in the cloud
Choosing the right instance for a job is very important. However, if you choose an instance that isn't right for the workload or for the cost associated with it, you can try other instance types. You can find a better fit. 

Moving from one instance to another is often done to improve performance and lower cost. Building and terminating an instance is a very fast process. You don't have the overhead of building and managing the hardware. So you have the flexibility to test different instance configurations, sizes, and settings against your workload to find the one that is the right fit.

**AWS Compute Optimizer** and **AWS Cost Explorer** provide optimal EC2 instance recommendations for your workloads. Both tools use the same ML engine to analyze historical use metrics. 

## Amazon EC2 Storage
Amazon EC2 provides you with flexible, cost-effective, and user-friendly data storage options for    your instances. Each option has a unique combination of performance and durability. These storage options can be used independently or in combination to suit your requirements. 

AWS storage services are grouped into three categories: file storage, block storage, and object storage. In file storage, data is stored as files in a hierarchy. In block storage, data is stored in fixed-size blocks. And in object storage, data is stored as objects in buckets.

The following diagram shows how EC2 instances can connect to different AWS services using different storage options:
* Block storage by connecting to instance stores or Amazon EBS volumes
* File storage by connecting to Amazon Elastic File System (Amazon EFS) or Amazon FSx
* Object storage by connecting to Amazon Simple Storage Service (Amazon S3)

### Amazon EC2 instance storage
Instance storage provides temporary, block-level storage for instances. The data on an instance store volume persists only during the life of the associated instance.

### Amazon EBS
Amazon EBS provides durable, block-level storage volumes that you can attach to a running instance.

### Amazon EFS
Amazon EFS provides scalable file storage for use with Amazon EC2.

### Amazon S3
Amazon S3 provides access to reliable and inexpensive data storage infrastructure. Amazon EC2 uses Amazon S3 to store EBS snapshots and instance store-backed AMIs.

You can also decide to store data and retrieve data from within Amazon EC2 at any time.

### Amazon FSx
The Amazon FSx family of services makes it convenient to launch, run, and scale shared storage powered by popular commercial and open-source file systems.

## Block device storage with AWS
A block device is a storage device that moves data in sequences of bytes or bits (blocks). These devices support random access and generally use buffered I/O.

 Examples include hard disks, CD-ROM drives, and flash drives. A block device can be physically attached to a computer or accessed remotely as if it were physically attached to the computer. The unique characteristics of block storage make it the preferred option for transactional, mission-critical, and I/O-intensive applications.

Amazon EC2 supports two types of block devices:
* Instance store volumes (virtual devices whose underlying hardware is physically attached to the host computer for the instance)
* EBS volumes (remote storage devices)

### Amazon EC2 instance store
An instance store provides temporary block-level storage for your instance. This storage is located on disks that are physically attached to the host computer. This ties the lifecycle of the data to the lifecycle of the EC2 instance. 

Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, and other temporary content. It can also be used to store temporary data that you replicate across a fleet of instances, such as a load-balanced pool of web servers.

An instance store consists of one or more instance store volumes exposed as block devices. The size of an instance store and the number of devices available varies by instance type.

#### Instance store lifecycle
You can specify instance store volumes for an instance only when you launch it. You can't detach an instance store volume from one instance and attach it to a different instance.

The data in an instance store persists only during the lifetime of its associated instance. If an instance reboots (intentionally or unintentionally), data in the instance store persists. However, data in the instance store is lost under any of the following circumstances:
* The underlying disk drive fails
* The instance stops
* The instance hibernates
* The instance terminates

Therefore, do not rely on instance store for valuable, long-term data. Instead, use more durable data storage, such as Amazon S3, Amazon EBS, or Amazon EFS.

When you stop, hibernate, or terminate an instance, every block of storage in the instance store is reset. Therefore, your data cannot be accessed through the instance store of another instance.

If you change the instance type, an instance store will not be attached to the new instance type. 

### Amazon EBS
Amazon EBS provides block-level storage volumes you can attach to and detach from an EC2 instance. EBS volumes have the following features:
* Detachable: You can detach an EBS volume from one EC2 instance and attach it to another EC2 instance in the same Availability Zone to access the data on it.
* Distinct: The EBS volume is separate from the EC2 instance. That means that if an accident occurs and the EC2 instance goes down, you still have your data on your external drive.
* One-to-one connection: Most EBS volumes can only be connected with one computer at a time. Most EBS volumes have a one-to-one relationship with EC2 instances, so they cannot be shared by or attached to multiple instances at one time.

You can scale your EBS volumes either by increasing the volume size to a maximum of 64 tebibytes (TiB) or by attaching multiple EBS volumes to your EC2 instances.

#### Amazon EBS use cases
EBS volumes are particularly well suited for use as the primary storage for file systems, databases, or any applications that require fine, granular updates and access to raw, unformatted, block-level storage. Volumes are commonly used in the following scenarios. 

##### Operating systems
Boot and root volumes can be used to store an operating system. The root device for an instance launched from an AMI is typically an EBS volume. These are commonly called EBS-backed AMIs.

##### Databases
EBS volumes can be used as a storage layer for databases running on Amazon EC2 that will scale with your performance needs and provide consistent and low-latency performance. 

##### Enterprise applications
Amazon EBS provides high availability and high durability block storage to run business-critical applications. 

##### Big data analytics engines
Amazon EBS offers data persistence, dynamic performance adjustments, and the ability to detach and reattach volumes, so you can resize clusters for big data analytics.

#### EBS volume types
EBS volumes are organized into two main categories: SSDs and hard disk drives (HDDs). SSDs are used for transactional workloads with frequent read/write operations with small I/O size. HDDs are used for large streaming workloads that need high throughput performance. 

#### EBS snapshots
You can make are incremental backups of your data using EBS snapshots. Snapshots only save the blocks on the volume that have changed after your most recent snapshot. For example, if you have 10 GB of data on a volume and only 2 GB of data have been modified since your last snapshot, only the 2 GB that have been changed are written to Amazon S3.

When you take a snapshot of any of your EBS volumes, the backups are stored redundantly in multiple Availability Zones using Amazon S3. This aspect of storing the backup in Amazon S3 is handled by AWS, so you won’t need to interact with Amazon S3 to work with your EBS snapshots. You manage them in the Amazon EBS console, which is part of the Amazon EC2 console.

#### Amazon EBS benefits
##### High availability
When you create an EBS volume, it is automatically replicated in its Availability Zone to prevent data loss from single points of failure.

##### Storage persistance
Storage persists even when your instance doesn’t.

##### Data encryption
When activated by the user, all EBS volumes support encryption.

##### Flexibility
EBS volumes support on-the-fly changes. Modify volume type, volume size, and I/O operations per second (IOPS) capacity without stopping your instance. 

##### Backups
Amazon EBS provides the ability to create backups of any EBS volume.

### File storage
Cloud file storage is a method for storing data in the cloud that provides servers and applications access to data through shared file systems. This compatibility makes cloud file storage ideal for workloads that rely on shared file systems and provides simple integration without code changes.

There are many file storage solutions that exist, ranging from a single node file server on a compute instance using block storage as the underpinnings with no scalability or few redundancies to protect the data, to a do-it-yourself clustered solution, to a fully-managed solution. The following content introduces some of the storage services provided by AWS for use with Linux.

#### Amazon EFS
Amazon EFS provides scalable file storage for use with Amazon EC2. You can use an EFS file system as a common data source for workloads and applications running on multiple instances. 

Amazon EFS is a file system that automatically grows and shrinks as you add and remove files. There is no need for provisioning or managing storage capacity and performance. Amazon EFS can be used with AWS compute services and on-premises resources. 

With the Amazon EFS web interface, you can create and configure file systems quickly without any minimum fee or setup cost. You pay only for the storage used, and you can choose from a range of storage classes designed to fit your use case.

#### Amazon FSx
The Amazon FSx family of services makes it convenient to launch, run, and scale shared storage powered by popular commercial and open-source file systems. You can use the new launch instance wizard to automatically attach the following types of Amazon FSx file systems to your Amazon EC2 instances at launch:
* Amazon FSx for NetApp ONTAP provides fully managed shared storage in the AWS Cloud with the popular data access and management capabilities of NetApp ONTAP.
* Amazon FSx for OpenZFS provides fully managed, cost-effective shared storage powered by the popular OpenZFS file system.

### Object Storage
Object storage is built for the cloud and delivers virtually unlimited scalability, high durability, and cost effectiveness. 

Objects, much like files, are treated as a single, distinct unit of data when stored. However, unlike file storage, these objects are stored in a bucket using a flat structure, meaning there are no folders, directories, or complex hierarchies. Each object contains a unique identifier. This identifier, along with any additional metadata, is bundled with the data and stored.

### Amazon S3
Amazon S3 is an object storage service. Object storage stores data in a flat structure. An object is a file combined with metadata. You can store as many of these objects as you want. All the characteristics of object storage are also characteristics of Amazon S3. 
Amazon EC2 uses Amazon S3 for storing AMIs and to to store snapshots (backup copies) of the data volumes.

Given the benefits of Amazon S3 for storage, you might also decide to use this service to store files and datasets for use with EC2 instances. There are several ways to move data to and from Amazon S3 to your instances:
* The wget utility is an HTTP and FTP client installed by default in most distributions that you can use to download public objects from Amazon S3.
* The AWS Command Line Interface (AWS CLI) can be used with the aws s3 cp command.
* The Amazon S3 API can also be used.

### Choosing the right storage solution
Choosing the right storage solution is important so that your application matches the cost, availability, and speed that you expect your application to have.

#### Amazon EC2 instance store
Instance store is ephemeral block storage. This is preconfigured storage that exists on the same physical server that hosts the EC2 instance and cannot be detached from Amazon EC2. You can think of it as a built-in drive for your EC2 instance.

Instance store is generally well suited for temporary storage of information that is constantly changing, such as buffers, caches, and scratch data. It is not meant for data that is persistent or long lasting. If you need persistent, long-term block storage that can be detached from Amazon EC2 and provide you more management flexibility, such as increasing volume size or creating snapshots, you should use Amazon EBS.

#### Amazon EBS
Amazon EBS is meant for data that changes frequently and must persist through instance stops, terminations, or hardware failures. Amazon EBS has two types of volumes: SSD-backed volumes and HDD-backed volumes.

The performance of SSD-backed volumes depends on the IOPS and is ideal for transactional workloads, such as databases and boot volumes.

The performance of HDD-backed volumes depends on megabytes per second (MBps) and is ideal for throughput-intensive workloads, such as big data, data warehouses, log processing, and sequential data I/O.

Here are a few important features of Amazon EBS that you need to know when comparing it to other services:
* It is block storage.
* You pay for what you provision (you must provision storage in advance).
* EBS volumes are replicated across multiple servers in a single Availability Zone.
* Most EBS volumes can only be attached to a single EC2 instance at a time.

#### Amazon S3
If your data doesn’t change often, Amazon S3 might be a cost-effective and scalable storage solution for you. Amazon S3 is ideal for storing static web content and media, backups and archiving, and data for analytics. It can also host entire static websites with custom domain names.

Here are a few important features of Amazon S3 to know about when comparing it to other services:
* It is object storage.
* You pay for what you use (you don’t need to provision storage in advance).
* Amazon S3 replicates your objects across multiple Availability Zones in a Region.
* Amazon S3 is not storage attached to compute.

#### Amazon EFS
Amazon EFS provides highly optimized file storage for a broad range of workloads and applications. It is the only cloud-native shared file system with fully automatic lifecycle management. Amazon EFS file systems can automatically scale from gigabytes to petabytes of data without needing to provision storage. Tens, hundreds, or even thousands of compute instances can access an Amazon EFS file system at the same time.

Amazon EFS Standard storage classes are ideal for workloads that require the highest levels of durability and availability. EFS One Zone storage classes are ideal for workloads such as development, build, and staging environments.

Here are a few important features of Amazon EFS to know about when comparing it to other services:
* It is file storage.
* Amazon EFS is elastic and automatically scales up or down as you add or remove files. And you pay only for what you use.
* Amazon EFS is highly available and designed to be highly durable. All files and directories are redundantly stored within and across multiple Availability Zones.
* Amazon EFS offers native lifecycle management of your files and a range of storage classes to choose from.

#### Amazon FSx
Amazon FSx provides native compatibility with third-party file systems. You can choose from FSx for NetApp ONTAP, FSx for OpenZFS, FSx for Windows File Server, and FSx for Lustre. With Amazon FSx, you don't need to worry about managing file servers and storage. This is because Amazon FSx automates time-consuming administration tasks, such as hardware provisioning, software configuration, patching, and backups. This frees you up to focus on your applications, end users, and business.

Amazon FSx file systems offer feature sets, performance profiles, and data management capabilities that support a wide variety of use cases and workloads. Examples include machine learning, analytics, HPC applications, and media and entertainment.

## Storage best practices
To ensure the maximum benefit from Amazon EC2, we recommend that you perform the following best practices:
* Understand the implications of the root device type for data persistence, backup, and recovery.
* Use separate EBS volumes for the operating system versus your data. Ensure that the volume with your data persists after instance termination.
* Use the instance store available for your instance to store temporary data. Remember that the data stored in instance store is deleted when you stop, hibernate, or terminate your instance.
* Encrypt EBS volumes and snapshots for security.

## Amazon Machine Images
An Amazon Machine Image, or AMI is a template that contains software configuration—for example, an operating system, applications, or tools. You use the AMI and the information contained within it to launch an instance. You must specify an AMI when you launch an instance because it contains all the necessary information and files required to build and launch the instance. If you don't specify an AMI, you cannot launch an instance because it will not have any operating system or software to interface with.

Because the AMI is a configuration template, you can use a single AMI to launch multiple instances. Or you can choose to launch a variety of different instances using different AMIs that contain unique configuration options. 

Amazon EC2 supports AMIs that use the Linux, Windows, or macOS operating systems. An AMI includes the following pieces. 

### WINDOWS OPERATING SYSTEMS
You are probably familiar with the Windows Operating system. It is a graphical user interface (GUI) based, proprietary operating system developed by Microsoft. There are a variety of versions of Windows operating systems available as public AMIs. 

When you launch an instance from a Windows AMI, the root device for the Windows instance is  an EBS volume. Windows AMIs do not support instance store for the root device.

### MAC OPERATING SYSTEMS (MACOS)
EC2 Mac instances are ideal for developing, building, testing, and signing applications for Apple devices, such as iPhone, iPad, iPod, Mac, Apple Watch, and Apple TV. You can connect to your EC2 Mac instance using SSH or Apple Remote Desktop. EC2 Mac instances natively support the macOS operating system:
* EC2 x86 Mac instances (mac1.metal) are built on 2018 Mac mini hardware powered by 3.2 GHz Intel eighth-generation (Coffee Lake) Core i7 processors.
* EC2 M1 Mac instances (mac2.metal) are built on 2020 Mac mini hardware powered by Apple Silicon M1 processors.

### LINUX OPERATING SYSTEMS
Just like Windows and MacOS, Linux is an operating system. In fact, it's one of the most popular on the planet. For example, Android, is powered by the Linux operating system. AWS supports Linux AMIs that include packages for convenient integration with AWS services, such as the AWS CLI, Amazon EC2 API and AMI tools, the Boto library for Python, and the Elastic Load Balancing tools.

When launching a Linux-based instance, remember that only the following instance types support an instance store volume as the root device for a Linux AMI: C3, D2, G2, I2, M3, and R3.

## Getting an operating system onto your instance
EC2 instances are virtual machines running in the AWS Cloud. How is a server built in the cloud? You can't insert a USB, DVD or any physical media to launch an instance, so how do you build instances in the cloud?

A virtual machine is made up of code and configuration files that comprise its operating system, which is operating on hardware owned by the cloud provider. Instead of physical media, you use an AMI that is either instance store backed or Amazon EBS backed to build instances. The operating system software will be located on storage that the system identifies as the root device. When you launch an instance, the root device volume contains the image used to boot the instance. 

## How an AMI can be backed
* When AWS introduced Amazon EC2, all AMIs were backed by Amazon EC2 instance store. This means the root device for an instance launched from an AMI was an instance store volume created from a template stored in Amazon S3.
* After AWS introduced Amazon EBS, we introduced AMIs that are backed by Amazon EBS. This means that the root device for an instance launched from an AMI is an Amazon EBS volume created from an EBS snapshot.

You can choose between AMIs backed by Amazon EC2 instance store and AMIs backed by Amazon EBS. We recommend that you use AMIs backed by Amazon EBS because they launch faster and use persistent storage.

### Instance stores
You can specify instance store volumes for an instance only when you launch it. You can't detach an instance store volume from one instance and attach it to a different instance. When using an instance store for a root device, consider the following:
* The root device is temporary.
* It is slower to boot.
* You only pay when the instance is running.
* Logs and other data disappear when the instance is stopped.

### Amazon EBS
Amazon EBS provides block-level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances. EBS volumes that are attached to an instance are exposed as storage volumes that persist independently from the life of the instance. You can create a file system on top of these volumes or use them in any way you would use a block device (such as a hard drive). 

When using Amazon EB for a root device, consider the following:
* The root device is persistent.
* It is faster to boot.
* It is more costly than an instance store backed instance. 
* Logs are persistent.

## Boot mode
When a computer boots, the first software that it runs is responsible for initializing the platform and providing an interface for the operating system to perform platform-specific operations. The AMI boot mode parameter signals to Amazon EC2 which boot mode to use when launching an instance. 

In Amazon EC2, two variants of the boot mode software are supported.

### UEFI
Unified Extensible Firmware Interface (UEFI): Graviton instance types run UEFI by default.

This is a newer boot mode than Legacy BIOS. When you launch an instance where the boot mode is set to UEFI, a key-value store for variables is created. The store can be used by UEFI and the instance operating system for storing UEFI variables.

UEFI variables are used by the boot loader and the operating system to configure early system startup. Because of the UEFI variables, the operating system can manage certain settings of the boot process, like the boot order or the keys for UEFI Secure Boot.

You can only access UEFI variables from within an instance. Anyone who can connect to an instance, and potentially any software running on the instance, can read the variables. You should never store sensitive data, such as passwords or personally identifiable information, in the UEFI variable store.

UEFI Secure Boot builds on the long-standing secure boot process of Amazon EC2 and provides additional defense-in-depth that helps customers secure software from threats that persist across reboots. It ensures that the instance only boots software that is signed with cryptographic keys. The keys are stored in the key database of the UEFI non-volatile variable store. UEFI Secure Boot prevents unauthorized modification of the instance boot flow.

### LEGACY BIOS
Legacy BIOS: Intel and AMD instance types run on Legacy BIOS by default.

Legacy BIOS is the original way of booting a system using the BIOS firmware. Older versions of the Windows operating system can only use Legacy BIOS where newer versions can support both Legacy BIOS or UEFI. 

It's important to verify which boot mode your AMI operating system can support.


The AMI boot mode parameter is optional. For AMIs with no boot mode parameter, the instances launched from these AMIs use the default value of the instance type—UEFI on Graviton and Legacy BIOS on all Intel and AMD instance types.

## Relationship between AMIs and EC2 instances
EC2 instances are live instantiations of what is defined in an AMI, much like a cake is a live instantiation of a cake recipe. If you are familiar with software development, you can also see this kind of relationship between a class and an object.

A class is something you model and define, while an object is something you interact with. Here, the AMI is how you model and define your instance, while the EC2 instance is the entity you interact with where you can install your web server and serve your content to users.

When you launch a new instance, AWS allocates a VM that runs on a hypervisor. Then, the AMI you selected is copied to the root device volume, which contains the image used to boot the volume. As a result, you get a server that you can connect to and install packages and additional software on.

One advantage of using AMIs is that they are reusable. You might choose a Linux-based AMI and configure the HTTP server, application packages, and additional software you need to run your application. If you want to create a second EC2 instance with the same configurations, you can go through the entire instance creation and configuration process to match your settings to the first instance. Or, you can create an AMI from your running instance and use the AMI to start a new instance. That way, your new instance would have the same configurations as your current instance because the configurations set in the AMIs are the same.

### Find AMIs
You can select an AMI from the following categories:
* Quick Start AMIs, which are created by AWS to help you get started quickly
* AWS Marketplace AMIs, which provide popular open source and commercial software from third-party vendors
* My AMIs, which are created from your EC2 instances
* Community AMIs, which are provided by the AWS user community
* Build your own custom image with EC2 Image Builder

Each AMI in the AWS Management Console has an AMI ID, which is prefixed by “ami-”, followed by a random hash of numbers and letters. The IDs are unique to each Region.

### EC2 Image Builder
EC2 Image Builder simplifies the building, testing, and deployment of VM and container images for use on AWS or on premises. It can significantly reduce the effort of keeping images up to date and secure by providing a basic graphical interface, built-in automation, and AWS provided security settings.

With Image Builder, there are no manual steps for updating an image nor do you need to build your own automation pipeline. When software updates become available, Image Builder automatically produces a new image without requiring users to manually initiate image builds. Image Builder is offered at no cost, integrates with AWS Organizations, and can share AMIs across accounts based on your existing AMI sharing mechanisms.

### Shared and public AMIs 
A shared AMI is an AMI that was built and made available for others to use. One of the best ways to get started with Amazon EC2 is to use a shared AMI that already has the operating system and software components you need. You can then add your own additional content to the instance. With your finalized instance, you can create a new AMI. When you have an AMI built, you can share it publicly or internally within your AWS accounts or Organizations.

Because AWS can't vouch for the integrity or security of all publicly shared AMIs, you use a shared public AMI at your own risk. Always treat shared AMIs as you would any foreign code that you might consider deploying in your own data center and perform the appropriate due diligence. It's a good idea to get an AMI from a trusted source. Public images owned by Amazon have an aliased owner, which appears as "amazon" in the account field so that you can easily find AMIs from Amazon. Only Amazon can alias their AMIs, so this is not something other users can do.

#### Considerations before publicly sharing an AMI 
Consider the following details when sharing AMIs with the public. 

##### Regional resources
AMIs are a Regional resource. When you search for a shared AMI (public or private), you must search for it from the same Region from which it is shared. 

To make an AMI available in a different Region, copy the AMI to the Region and then share it.

##### AMIs that cannot be public
If your AMI includes one of the following components, you can't make it public (but you can share the AMI with specific AWS accounts):
* Encrypted volumes
* Snapshots of encrypted volumes
* Product codes

A unique product code is assigned to your product when you create it in AWS Marketplace.

##### Sensitive
Avoid exposing sensitive data. To avoid exposing sensitive data when you share an AMI, read the security considerations in the guidelines for shared Linux AMIs and follow the recommended actions. 

##### Deprecation
By default, the deprecation date of all public AMIs is set to 2 years from the AMI creation date automatically. You can choose to set the deprecation date to be sooner than 2 years. 

To cancel the deprecation date or to move the deprecation to a later date, you must make the AMI private by only sharing it with specific AWS accounts.

##### Billing
You are not billed when your AMI is used by other AWS accounts to launch instances. The accounts that launch instances using the AMI are billed for the instances that they launch.

### Launch permissions
The owner of an AMI determines its availability by specifying launch permissions. Launch permissions fall into the following three categories:
* **Public**: The owner of the AMI grants launch permissions to all AWS accounts.
* **Explicit**: The owner of the AMI grants launch permissions to specific AWS accounts, organizations, or organizational units. 
* **Implicit**: The owner of the AMI has launch permissions for the AMI they own.

## Amazon EC2 Lifecycle
### Instance states
An operating system goes through a variety of phases, or states, during both the power-on cycle and then afterward when it is powered-on but in a different state, such as sleeping or hibernating.

In addition to the states that occur within an operating system, the Amazon EC2 instance itself also goes through a variety of states. 

One of the main reasons why EC2 provides so much value is the fact that you can provision new EC2 instances on demand, and just as easily, you can get rid of instances that you no longer need. In most cases, you only get charged for instances that are currently running. EC2 allows you to stop and start instances at will, which enables you to treat your fleet of EC2 instances as elastic, scaling them in or out. Then at the end of the billing cycle, you only pay for what you use. We are building up to the idea of scaling your fleet of EC2 instances in and out to serve demand. But before we get there, it's important to understand some of the more basic things about EC2. Let's talk about the EC2 instance lifecycle.

An Amazon EC2 instance transitions through different states from the moment you launch it through to its termination. You launch an EC2 instance from an AMI, and as you learned in a previous lesson, once the EC2 instance is launched, it enters a pending state. This state is essentially your VM booting up. Once the instance is ready for use, it enters the running state. In the running state, you will be charged for the EC2 instance.

From running, you have a couple of different options. You can reboot the instance, which is similar to rebooting, say, your laptop. It turns off, then it turns back on again. Pretty straightforward. You can also choose to stop your instance. It will enter a stopping phase, then enter the stopped phase. Stopping an instance is like powering down your laptop. You can always turn it back on and it will go through its usual boot sequence, moving through the pending state and back to the running state.

The other option, which is similar to stop, is to stop-hibernate your instance. This also enters the stopping phase and then the stopped phase. You can compare this to how you lock your laptop and shut the lid, but when you open it back up, everything is still in place where you left it. No boot sequences required. You are back up and running after a couple of seconds of the computer waking up. Since the state of the machine was written to memory when you stopped it, the state of the machine can be drawn from memory and put back into place. Then, you're back up and running.

Now, the last option depicted here is the terminate option. When you terminate an instance, it enters the shutting down phase then the terminated phase. Terminating an EC2 instance is like taking your laptop out for a long boat ride off the coast and throwing it into the ocean, getting rid of it forever. It's now lost in the great blue sea. There is no hope of finding your laptop on an island, shipwrecked one day, having been saved after spelling SOS in the sand. Anyways, I hope you had any data or state stored on that instance backed up because once you terminate an instance, it's gone. That being said, there is a feature called termination protection that you can enable if you're worried about instances being terminated accidentally. You also will learn about persistent storage and EC2 in future lessons, so don't fret. We will show you ways you can make sure your data sticks around, even if the EC2 instance doesn't.

So that is the EC2 instance lifecycle. It's definitely a good idea to remember how all of this works if you plan on using EC2 to host your applications. And don't think of terminating instances as a bad thing. If your EC2 instances is having technical trouble for one reason or another, maybe it needs an update or a patch, instead of logging into the instance to fix it or install software, you can launch a new one with the new changes in its place and then you could terminate the old instance, having a new instance take that place. You of course can do in place updates as well, but just know that you have the option to decide how to handle these sorts of tasks. You can launch or terminate EC2 instances to meet demand. So as demand for your application increases, you can launch more instances and as it decreases, you can terminate instances. This keeps your EC2 instance fleet in line with demand. So again, terminating an instance isn't a bad thing and shouldn't be feared.

Now, let's discuss the cost aspect of this. You only get charged for an EC2 instance if you're in the running state or if you are in the stopping state when preparing to hibernate. This means that you can stop instances when they aren't in use, say if you have applications that are only used during the work week. Run them when your employees are clocked in and then stop them when they aren't. Remember, you can always start from a stop state, allowing them to resume working when necessary.

### Instance states in detail
* **Running**: This state means the instance is active and ready to use. You are billed when an instance is in the running state.
* **Stopping**: The instance is preparing to be stopped.
* **Stopped**: This state means the instance is shut down. Although you are not billed for the instance in this state, you are billed for any data storage on EBS volumes associated to the instance. For Linux, Windows, Windows with SQL Enterprise, Windows with SQL Standard, and Windows with SQL Web Instances, each time you start an instance from a stopped state, you will be billed for a minimum of 1 minute of use. However after the first minute that the instance is running, you are only billed for the seconds you use. Other types of instances are charged by the hour.
* **Shutting down**: This state indicates that the instance is preparing to be terminated. You are not billed when an instance is in this state.
* **Terminated**: This state means that an instance has been permanently deleted. A terminated instance cannot be started or connected to. You do not incur charges after the instance goes into the stopping state, in preparation for termination.
* **Hibernate**: Hibernation saves the contents from the instance memory (RAM) to your EBS root volume. Amazon EC2 persists the instance's EBS root volume and any attached EBS data volumes. You're not charged for instance usage for a hibernated instance when it is in the stopped state or for data transfer when the contents of the RAM are transferred to the EBS root volume. You are charged for storage of any EBS volumes, including storage for the RAM contents. 

#### Pending
A pending state means that an instance is preparing to go into the running state. This state occurs at the first launch of an instance or any time the instance is stopped and restarted. There is no billing for usage in this state.

#### Stopping
The instance is preparing to stop or stop-hibernate. You are billed if the instance is in the stopping state while transitioning to hibernate.

#### Hibernate
When you hibernate an instance, Amazon EC2 signals the operating system to perform hibernation (suspend to disk). Hibernation saves the contents from the instance memory (RAM) to your EBS root volume. Amazon EC2 persists the instance EBS root volume and any attached EBS data volumes. When you start your instance, the following events occur:
* The EBS root volume is restored to its previous state.
* The RAM contents are reloaded.
* The processes that were previously running on the instance are resumed.
* Previously attached data volumes are reattached and the instance retains its instance ID.

#### Reboot (scheduled)
AWS can schedule events, such as a reboot, for your instances. An instance reboot is equivalent to an operating system reboot. Usually, it takes only a few minutes to reboot your instance. When you reboot an instance, it keeps its public DNS name (IPv4), private and public IPv4 address, IPv6 address (if applicable), and any data on its instance store volumes.

Rebooting an instance doesn't start a new instance billing period (with a minimum 1-minute charge), unlike stopping and starting your instance.

An instance reboot might be done for required maintenance, such as to apply updates that require a reboot. No action is required on your part when a reboot is scheduled. It's recommend that you wait for the reboot to occur within its scheduled window. 

#### Retire
An instance is scheduled to be retired when AWS detects irreparable failure of the underlying hardware that hosts the instance. When an instance reaches its scheduled retirement date, it is stopped or terminated by AWS.

If your instance root device is an EBS volume, the instance is stopped, and you can start it again at any time. Starting the stopped instance migrates it to new hardware.

If your instance root device is an instance store volume, the instance is terminated and cannot be used again.


**You cannot stop, start, or hibernate an instance store-backed instance**.


## Amazon EC2 Scaling
### Elasticity and scaling
**Elasticity** means that the infrastructure can expand and contract when capacity needs change. You can acquire resources when you need them and release resources when you don't. Scaling is a technique that is used to achieve elasticity. **Scaling** is the ability to increase or decrease the compute capacity of your application.

#### ELASTICITY
With elasticity, you can do the following:
* Increase the number of web servers when traffic to your application spikes.
* Lower the write capacity on your database when traffic decreases.
* Handle the day-to-day fluctuation of demand throughout for your architecture.

Imagine a website that might see a sudden increase in traffic, such as an e-commerce website during a sales event. Elastic infrastructure adds servers to avoid the site from becoming temporarily unavailable. The traffic might drop to normal levels after the event, or it might increase again during holiday seasons.

#### SCALING
Scaling has two types:
* **Horizontal scaling** is where you add or remove resources. For example, you might need to add more hard drives to a storage array or add more servers to support an application. Adding resources is called scaling out, and shutting down resources is called scaling in. Horizontal scaling is a good way to build internet-scale applications that take advantage of the elasticity of cloud computing.
* **Vertical scaling** is where you increase or decrease the specifications of an individual resource. For example, you can upgrade a server so that it has a larger hard drive or a faster CPU. With Amazon EC2, you can stop an instance. You can then resize it to an instance type that has more RAM, CPU, I/O, or networking capabilities. Vertical scaling can eventually reach a limit, and it isn't always a cost-efficient or highly available approach. However, it's basic to implement and can be sufficient for many use cases, especially in the short term.

### Amazon EC2 Auto Scaling
Amazon EC2 Auto Scaling helps you to have the right number of EC2 instances. The service automatically adds or removes EC2 instances according to policies that you define, schedule, and monitor.

#### Better fault tolerance
Amazon EC2 Auto Scaling can detect when an instance is unhealthy, terminate it, and launch an instance to replace it. You can also configure Amazon EC2 Auto Scaling to use multiple Availability Zones. If one Availability Zone becomes unavailable, Amazon EC2 Auto Scaling can launch instances in another one to compensate.

#### Better availability
Amazon EC2 Auto Scaling helps to ensure that your application has the right amount of capacity to handle the current traffic demand. When using several Availability Zones, the service attempts to distribute instances evenly among the Availability Zones that are activated for your Auto Scaling group.

#### Better cost management
You pay for the EC2 instances that you use. Therefore, you save money by launching instances when they are needed and terminating them when they're not.

Amazon EC2 Auto Scaling is key to building highly available architectures. You will learn more about high availability later in this module.

Amazon EC2 Auto Scaling also integrates with Elastic Load Balancing (ELB) to better distribute incoming traffic across the instances.

### Auto Scaling groups
Amazon EC2 Auto Scaling works with Auto Scaling groups, which are collections of EC2 instances. For each Auto Scaling group, you specify the minimum, maximum, and necessary capacities of the group.
* **Minimum capacity**: The number of EC2 instances will never go below this size.
* **Maximum capacity**: The number of EC2 instances will never go above this size.
* **Desired capacity**: Amazon EC2 Auto Scaling ensures that the group has this many instances.

Initially, you set the desired capacity to tell the Auto Scaling group how many instances you want to run at a particular time. The number of instances that are currently running might be different from the desired value until Amazon EC2 Auto Scaling instantiates or deletes them.

### Scaling policies
You can use scaling policies to increase or decrease the number of instances in your group dynamically to meet changing conditions. Amazon EC2 Auto Scaling provides several ways for you to scale your Auto Scaling group.

#### FIXED INSTANCES
By accurately setting the minimum, maximum, and desired capacities, you define a fixed number of instances that are needed. After you have created your Auto Scaling group, the group starts by launching enough instances to meet its desired capacity. Amazon EC2 Auto Scaling performs a periodic health check on running instances within an Auto Scaling group, and terminates or launches instances accordingly.

#### MANUAL SCALING
Manual scaling is the most basic way to scale your resources. With manual scaling, you specify only the change in the maximum, minimum, or desired capacity of your Auto Scaling group. Manually scaling your group can be useful when automatic scaling is not needed or when you need to hold capacity at a fixed number of instances.

#### SCHEDULED SCALING
Scaling by schedule means that scaling actions are performed automatically as a function of time and date. To use scheduled scaling, you create scheduled actions. When you create a scheduled action, you specify when the scaling activity should occur, and the new minimum and maximum sizes for the scaling action.
   
For example, you can configure a schedule for Amazon EC2 Auto Scaling to increase capacity on Wednesday and decrease capacity on Friday.

#### SCALE BASED ON DEMAND
A more advanced way to scale your resources uses dynamic scaling. You can define a scaling policy that dynamically resizes your Auto Scaling group to meet changes in demand. A dynamic scaling policy instructs Amazon EC2 Auto Scaling to track a specific CloudWatch metric. The policy defines which action to take when the associated CloudWatch alarm is activated. The metrics that cause an alarm to change state are an aggregation of metrics that are coming from all instances in the Auto Scaling group.

Multiple ways are available to scale on demand:
* **Simple scaling**: Increase or decrease the current capacity of the group based on a single scaling adjustment.
* **Step scaling**: Increase or decrease the current capacity of the group based on a set of scaling adjustments. These scaling adjustments, which are known as step adjustments, vary based on the size of the alarm breach.
* **Target tracking scaling**: Increase or decrease the current capacity of the group based on a target value for a specific metric. Target tracking is similar to the way that your thermostat maintains the temperature of your home. You select a temperature, and the thermostat does the rest.

#### PREDICTIVE SCALING
Predictive scaling uses machine learning to predict capacity requirements based on historical data from CloudWatch that monitors your EC2 instances.

Predictive scaling can help you scale faster by launching capacity in advance of a forecasted load, compared to using only dynamic scaling, which is reactive in nature.

### Lifecycle hooks
With lifecycle hooks, an Auto Scaling group can be aware of events in the Auto Scaling instance lifecycle. The group then performs a custom action when the corresponding lifecycle event occurs. The instance enters a wait state until the action is completed or the timeout period ends (1 hour by default).

For example, the group might install packages when a scale-out event occurs to make sure that the new EC2 instance is fully ready to work. Or the group might send a notification when a scale-in event occurs.

### Purchasing options
When you configure an Auto Scaling group, you can specify several EC2 instance types to help lower costs:
* Spot Instances have discounted prices.
* Reserved Instances or Saving Plans provide discounted prices compared to On-Demand Instances.

You can specify how much of the desired capacity should be fulfilled with On-Demand Instances and Spot Instances.

You can launch and automatically scale a fleet of On-Demand Instances and Spot Instances within a single Auto Scaling group.

For On-Demand Instances, you can also prioritize instance types that can benefit from Savings Plans or Reserved Instance discount pricing.

For Spot Instances, you can prioritize fewer interruptions.  In this case, Amazon EC2 Auto Scaling requests Spot Instances from the pool with optimal capacity for the number of instances that are launching. Or you can prioritize lower prices, in which case Amazon EC2 Auto Scaling allocates Spot Instances from pools with the lowest price.

## Launching an EC2 Instance
### Launching an instance
The most common ways to launch an instance are through the console, AWS CLI, and AWS SDKs. If you want to build a more granular, consistent, repeatable, and modifiable environment, you can use services such as AWS CloudFormation to build infrastructure as code.

#### Launching an EC2 instance using AWS Management Console.
To start, log into the console and choose EC2. On the EC2 page, choose Launch instance.

Enter a name for your instance and then choose an Amazon Machine Image or AMI.

The AMI contains an operating system and the software of your choice. AMIs can be a simple image that installs a Linux distribution, such as Amazon Linux 2023 or Ubuntu. AMIs can also be more complex, and might include specialized tools. The AWS Marketplace offers many types of AMIs that have various operating systems and specialized software, tools, and features. You can also create your own AMI from an EC2 instance after you install the software you need. For this example, we'll select Amazon Linux 2023. Next, choose an instance type to configure the EC2 instance. A key is needed for a secure connection when you're using tools such as PuTTY or OpenSSH. Configure the network and storage settings, and then choose Launch instance. When the instance is launched, it appears on the Instances dashboard. Notice that the instance is in a Pending state. When the status changes to Running, the EC2 instance is available. You can access the instance using its public IP address. 

To connect to your instance, click Connect. Now, there are four options for connecting to the instance. The first is the EC2 Instance Connect, which connects directly through the browser. Choose Connect, and a new window opens. You can interact with your instance through a CLI shell. The second way to connect is through the SSH client option. Here, we'll connect using OpenSSH on Windows. Keep in mind that you can also generate a key to connect via the PuTTY client on Windows. Session Manager is an option to connect using the AWS Systems Manager Service. The EC2 serial console option offers access to the serial port for the instance, which you can use to troubleshoot issues. To launch an instance using a template you have created, go to the Instances dashboard and choose Launch instance from template. You can create launch templates using the Launch Templates menu.

And you can store common launch parameters such as AMI ID, instance type, and network settings. This means you won't have to specify them every time you launch an instance. 

#### Launching an EC2 instance through the AWS Command Line Interface or AWS CLI.
Just enter this command in a shell. This command creates an EC2 instance using the Amazon Linux 2023 AMI ID and the key pair that we created before. The command displays details about the instance in the shell. To verify that the instance that you launched from the CLI is being created, navigate to the Instances dashboard. Note that the instance is in a Running state. Now, we will shut it down. 

#### Launching an EC2 instance by using the AWS SDK API.
It is available in several languages, including Python, PHP, Java, and Go. In this example, we will use the SDK for JavaScript. Here, you can see the JavaScript code in AWS Cloud9, which is a cloud-based integrated development environment or IDE. Here, you can see the EC2 instance created by the JavaScript code is in a running state. We have completed your introduction to the most common ways to launch an EC2 instance by using the AWS Management console, the AWS CLI, or an AWS SDK.

### Launching an instance using the console
There are four ways to launch an instance from the Amazon EC2 dashboard.
#### Launch wizard
**You can launch an instance using the new launch instance wizard**.

This is the fastest way to get started. Except for the key pair, the launch instance wizard provides default values for all of the parameters. You can accept any or all of the defaults or configure an instance by specifying your own values for each parameter. The parameters are grouped in the launch instance wizard. The wizard walks you through deploying an EC2 instance.

When using the default settings, you must provide five required pieces of information for the instance to launch successfully:
* **Name of the instance**: This is a useful moniker to remember the purpose or function of the instance.
* **Application and operating system AMI**: This is the image operating system type that you want to launch. This can be any supported version of Linux, Windows, or macOS.
* **Instance type**: This is the instance family and hardware specifications that you require.
* **Key pair**: This is a combination of a public key that is used to encrypt data and a private key that is used to decrypt data.
* **Security group rule**: This controls the traffic and ports that can go into and out of your instances.

#### Launch template
**You can launch an instance from a launch template**.

A launch template contains the configuration information to launch an instance and helps you to use the same template to launch multiple instances with the same settings.

For example, a launch template can contain the AMI ID, instance type, and network settings that you typically use to launch instances.

#### Exisiting instance
**You can launch an instance using parameters from an existing instance**.

The Amazon EC2 console provides a launch wizard option that can help you use a current instance as a base for launching other instances. This option automatically populates the Amazon EC2 launch wizard with certain configuration details from the selected instance.

#### AWS Marketplace
**You can launch an AWS Marketplace instance**.

The AWS Marketplace is a curated digital catalog that you can use to find, buy, deploy, and manage third-party software, data, and services. AMIs are available for purchase that come with preinstalled software configurations for a wide range of technologies.

### Launching an instance using AWS CLI or AWS SDKs
You can use AWS CLI or the AWS SDKs to launch instances from an AMI or from a launch template and list and terminate Amazon EC2 instances.

## Connecting to an EC2 Instance
### Key pairs
A key pair, consisting of a public key and a private key, is a set of security credentials used to prove your identity when connecting to an EC2 instance. Amazon EC2 stores the public key on your instance, and you store the private key.

With the private key, you can securely connect to you instance by using SSH (Secure Shell) for Linux or Remote Desktop Protocol for Windows instances.

Anyone who possesses your private key can connect to your instances, so it's important that you store your private key in a secure place.

When you launch an instance, you are prompted for a key pair. If you plan to connect to the instance using SSH, you must specify a key pair. You can choose an existing key pair or create a new one. When your instance boots for the first time, the public key that you specified at launch is placed on your Linux instance in an entry within ~/.ssh/authorized_keys. When you connect to your Linux instance using SSH, you must specify the private key that corresponds to the public key. 

Because Amazon EC2 doesn't keep a copy of your private key, there is no way to recover a private key if you lose it. 

When you create an instance, you can either provide your own key pair or let the wizard launcher create it for you.

### Connection options
AWS provides several options to connect to your EC2 instances that vary according to your local computer operating system and the operating systems the AMIs are using.

#### Connecting to a Linux AMI
#### Linux or macOS
To connect to a Linux EC2 instance from a Linux or macOS operating system, you can use the following:
* An SSH client
* The EC2 instance connect feature available on the the console
* AWS Systems Manager

#### Windows
To connect to a Linux EC2 instance from a Windows operating system, you can use the following:
* The OpenSSH Client 
* PuTTY
* Systems Manager

##### SSH client
To connect to your instance through SSH, you need an SSH client installed on your computer, such as OpenSSH on Linux or macOS or OpenSSH for Windows. If you are a Windows user, you can also use PuTTY, a free SSH client with a graphical user interface. The recommended option for Windows is OpenSSH for Windows.

You connect to your instance using the public IPv4 or IPv6 address or the DNS name. To ensure the connection is secure, you must also provide the private key that you created or passed to the EC2 instance at creation time.

Since the SSH connection goes through port 22, you must make sure that the security group of your instance has an inbound rule that allows connections on port 22 from your computer. This rule is added by default if you selected the option create security group on the EC2 launch wizard.

##### EC2 Instance Connect
You can use EC2 Instance Connect to connect to your instances using the Amazon EC2 console, the EC2 Instance Connect CLI, or the SSH client of your choice. (Unlike normal a SSH client connection, the key is used only once during the first connection.) All connection requests using EC2 Instance Connect are logged to AWS CloudTrail so that you can audit connection requests.

Connections on port 22 from your computer or domain must be allowed on the security group attached to your EC2 instance.

##### Systems Manager Session Manager
Systems Manager is the operations hub for your AWS applications and resources and a secure end-to-end management solution for hybrid cloud environments that helps you create secure operations at scale.

Session Manager is a fully managed Systems Manager capability. With Session Manager, you can use either an interactive, one-click, browser-based shell or AWS CLI to connect to your EC2 instances and manage them. Connecting through Session Manager requires the Systems Manager Agent to be installed on your instance.

#### Connecting to a Windows AMI
##### RDP client
You can connect to your Windows instance using a Remote Desktop Protocol (RDP) client from your computer:
* The default RDP client on Windows
* Microsoft Remote Desktop App on macOS
* Remmina on Linux

Ensure that the security group associated with your instance allows incoming RDP traffic (port 3389) from your IP address.

##### Fleet Manager
You can use Fleet Manager, a capability of Systems Manager, to connect to Windows instances using RDP and display up to four Windows instances on the same page in the console. You can connect to the first instance in the Fleet Manager Remote Desktop directly from the instances page in the Amazon EC2 console.

##### Session Manager
Session Manager is a fully managed Systems Manager capability for managing your EC2 instances through an interactive, one-click, browser-based shell or through AWS CLI. You can use Session Manager to start a session with an instance in your account. After the session is started, you can run PowerShell commands as you would for any other connection type.

## Management, Maintenance, and Operations
### Remote management options
With the console, you can manage infrastructure on AWS, such as EC2 instances. However, managing the underlying operating system, software, services, or artifacts on an instance must still be performed. So, how is this done? That can depend on the type of operating system or software and the type of interactions that are needed.

**Once you have launched your instances, you will need a way to manage, maintain, and securely operate them. That is where Systems Manager comes in**.

### Systems Manager
Systems Manager is a secure end-to-end management solution for hybrid cloud environments. It simplifies resource and application management and shortens the time taken to detect and resolve operational problems. It also helps you operate and manage your AWS infrastructure securely at scale. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations that it detects.

With Systems Manager, you can group resources, like EC2 instances or Amazon Relational Database Service (Amazon RDS) databases, and view operational data for monitoring and troubleshooting, or take action on your groups of resources.

You first create group of resources that you want to monitor or take actions on. You can then visualize data about these resources and take actions such as install a patch on a fleet of EC2 instances.

Systems Manager is agent-based, which makes it possible for the service to update, manage, and configure software that runs on edge devices, on-premises servers, and VMs in addition to your EC2 instances.

#### Systems Manager
Systems Manager helps you safely manage and operate your resources at scale.

#### Group resources
Create groups of resources across different AWS services, such as applications or different layers of an application stack.

#### Visualize data
View aggregated operational data by resource group.

#### Take action
Respond to insights and automate operational actions across resources groups.

#### Actions
* **Operations management** helps manage AWS resources. 
* **Applications management** helps manage applications running in AWS.
* **Change management** helps takes actions on or make changes  to AWS resources in a safe and auditable manner.
* **Node management** helps manage EC2 instances, on-premises servers, and VMs in hybrid environments as well as other types of AWS resources.

**Systems Manager is a collection of capabilities to help you manage your applications and infrastructure running in the AWS Cloud. 

It helps you to shorten time to detect problems, take advantage of automation, improve visibility and control, manage hybrid environments, and maintain security and compliance**.

### Node management
Systems Manager provides various capabilities for accessing, managing, and configuring your managed nodes. A managed node is any machine configured for Systems Manager. 

In the following example, notice how you can use the service to remotely manage EC2 instances, ECS clusters, EKS clusters, Internet of Things (IoT) devices, on-premises services, and VMs, including VMs in other cloud environments. 

#### Patch Manager
Patch Manager automates the process of patching managed nodes with both security-related and other types of updates. Patch Manager provides options to scan your managed nodes and report compliance on a schedule, install available patches on a schedule, and patch or scan targets on demand whenever you need to.

#### State Manager
State Manager is a secure and scalable configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define.

#### Automation
Automation simplifies common maintenance and deployment tasks of EC2 instances and other AWS resources. Automation can simplify common information technology tasks, such as changing the state of one or more nodes (using an approval automation) and managing node states according to a schedule.

#### Session Manager
With Session Manager, you can establish secure connections to your EC2 instances, edge devices, and on-premises servers and VMs.

Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.

#### Run Command
Using Run Command, you can remotely and securely manage the configuration of your managed nodes. You can automate common administrative tasks and perform one-time configuration changes at scale. Administrators use Run Command to install or boostrap applications, build a deployment pipeline, and capture log files when an instance is removed from an Auto Scaling group. They also use it to join instances to a Windows domain.

### Setup and use AWS Systems Manager Session manager
Welcome to an Introduction to AWS Systems Manager Session Manager. Session Manager is a fully managed AWS Systems Manager capability. This video will demonstrate how to set up an AWS Systems Manager and the EC2 instances you need to use Session Manager. To use Session Manager, you need to complete the following prerequisites. First, you'll need to configure permissions. By default, Systems Manager does not have permission to perform actions on your instances. You can set permissions at the account level by using an AWS Identity and Access Management or IAM role. Or, you can provide permissions at the instance level by using an instance profile. Second, you will need to install the Systems Manager Agent, or SSM Agent, on all mount systems and instances. For an EC2 instance, you can select an Amazon machine image or AMI that has the SSM Agent installed by default. Last, the security group of your EC2 instance must allow HTTPS port 443 outbound traffic to the required EC2 and SSM Agent endpoints. First, let's configure the permissions. From the roles page on the IAM dashboard, choose Create Role. For the Trusted Entity type, choose AWS service. In the Use case section, choose EC2. Next you'll add permissions. Search for and choose the AWS managed role called Amazon SSM Managed Instance call. This allows Systems Manager to perform actions on your EC2 instances. Next, name the Role SSM instance profile and then choose Create Role. Now you can use the EC2 instance dashboard to launch an EC2 instance that uses the Amazon Linux 2 HVM AMI, and this is pre-configured with the SSM Agent.

When you launch the instance, you can create a new key pair if you do not have one. Next, you can create a new security group for the instance. By default, the security group will allow outbound access for all traffic. System Manager requires outbound access for port 443 only, so you can restrict access to the required SSM endpoints on port 443 for enhanced security. In Advanced details for IAM Instance Profile, choose SSM Instance Profile. Then, choose Launch Instance. Now you can open Systems Manager. On the Quick Setup page, choose the Library tab and then choose Create to configure the host management options for AWS Systems Manager. You can customize the host configuration management options, but for this example, the default options for updating the Systems Management Agent inventory instance and scanning for missing patch remains selected. For Targets, choose Current Region. For the Choose how you want to Target in Instances Option, choose Manual, which allows you to choose the EC2 instances that you previously launched. When you are done customizing options, choose Create. Next, wait for the quick setup configuration deployment. The quick setup post management configuration will begin deploying to your account. This process might take several minutes to complete. After the status changes to Success, you can continue. Once your host management configuration is successfully updated, you can use Session Manager to connect securely to the EC2 instance. From the Node Management section of the left-navigation menu choose Session manager. On the specified target page, choose Start session. You can see the EC2 instance that was launched and configured with the host management. Choose the instance, and then choose Start session. This opens a secure session of the instance with the EC2 host.

### AWS Systems Manager Parameter Store
Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, AMI IDs, and license codes as parameter values. You can store values as plain text or encrypted data. You can reference Systems Manager parameters in your scripts, commands, Systems Manager documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter. 

Instead of storing data in config files or including them in your source code, you can use Parameter Store to reference this information in your applications or scripts. Configuration information that can be kept in Parameter Store include passwords, keys, license codes, and database strings.

Some of the benefits of Parameter Store include the following:
* Hierarchical structure
* Support for encryption
* Support for label versioning and roll-back
* Support for AWS Identity and Access Management (IAM) users and roles
* Change notification 

In Parameter Store, you can tag and organize your data into hierarchies, helping you manage parameters. For example, you can use the same parameter name, license, with a different hierarchical path, dev/OS/license or prod/OS/license, to store values for either the development (identified as dev) or production environment (identified as prod).

Parameter Store integrates with IAM to control parameter access and with AWS Key Management Service (AWS KMS) to encrypt and decrypt stored information.

#### Request
The application sends a parameter request, either a PUT request to store or a GET request to retrieve, to Parameter Store.  The application can be the following:
* An on-premises server
* An AWS service such as Amazon EC2, Amazon ECS, Lambda, etc...
* A Systems Manager capability such as Run Command, Automation, or State Manager

#### Permission
Parameter Store accesses IAM for permissions to retrieve and decrypt the parameter or encrypt and PUT the parameter depending on the request.

#### Encryption and decryption
Parameter Store sends an encrypt or decrypt request to AWS KMS.

In the second case, AWS KMS returns the decrypted value.

During transmission, the plaintext data is protected by TLS.

#### Response
For a GET parameter request, Parameter Store returns the plaintext parameter value in the response.

### Parameter example
In the following example, a parameter has been created to store a license key. Notice that the hierarchy of the path for this parameter is /prod/OS/license. This path can be defined by the user and is fairly intuitive; it suggests that this license key is for the organization's production environment and for an operating system. 

This organization can use a different path to store license keys for systems in the development environment, such as /dev/OS/license.

```
{
    "Parameters":
        {
            "Name": "/prod/OS/license",
            "Type": "String",
            "LastModifiedDate": "2022-01-02T16:00:02.303000-04:00",
            "LastModifiedUser": "arn:aws:iam::example-user",
            "Value": “EXAMPLE-LICENSE-KEY-1234",
            "Version": 1,
            "Labels": [],
            "Tier": "Standard",
            "Policies": []
        }
}
```

## Summary
### Amazon EC2 basics
AWS Cloud computing options deliver secure, reliable, high-performance, and cost-effective compute infrastructure to meet demanding business needs.

You pay only for the compute time you use when an instance is running, not when it is stopped or terminated.

### EC2 types and names
The AWS instances are currently categorized into five distinct families: general purpose, compute optimized, memory optimized, accelerated computing, and storage optimized.

EC2 instances are sized based on the combined hardware resources consumed by that instance type, such as vCPU, memory, storage, and networking.

Instances are named based on a combination of the instance family, generation, and size. They can also indicate additional capabilities, such as specific processor type or optimized networking performance.

### Pricing models
Amazon EC2 offer different pricing models that can help you cut costs.

#### On-Demand Instances
With On-Demand Instances, you pay for compute capacity by the hour or by the second, depending on which instances you run.

#### Saving Plans
Savings Plans are a flexible pricing model offering lower prices compared to On-Demand pricing in exchange for a specific usage commitment (measured in dollars per hour) for a 1-year or 3-year period.

#### Reserved Instances
Reserved Instances (RIs) are a billing discount applied to the use of On-Demand Instances in your account. You can purchase Standard RIs and Convertible RIs for a 1-year or 3-year term. You realize greater cost savings with the 3-year option.

#### Spot Instances
With Amazon EC2 Spot Instances, you can request spare Amazon EC2 computing capacity for up to 90 percent off the On-Demand price.

#### Dedicated Hosts
A Dedicated Host is a physical Amazon EC2 server dedicated for your use. Dedicated Hosts can help you reduce costs by letting you use your existing server-bound software licenses, including Windows Server, SQL Server, and SUSE Linux Enterprise Server (subject to your license terms). They can also help you meet compliance requirements.

#### Dedicated Instances
You can use Dedicated Hosts and Dedicated Instances to launch EC2 instances on physical servers that are dedicated for your use. With Dedicated Instances, all of your instances reside on one single host that is allocated to your AWS account so that no other AWS accounts can place instances on this host.

### Storage options
Amazon EC2 provides you with flexible, cost-effective, and user-friendly data storage options for    your instances. AWS storage services are grouped into three categories: file storage, block storage, and object storage.

#### Block storage
In block storage, data is stored in fixed-size blocks. Amazon EBS provides block-level storage volumes you can attach to and detach from an Amazon EC2 instance. An instance store provides temporary block-level storage.

#### File storage
In file storage, data is stored as files in a hierarchy. Amazon EFS provides scalable file storage for use with Amazon EC2.

#### Object storage
In object storage, data is stored as objects in buckets. Amazon EC2 uses Amazon S3 for storing AMIs and to store snapshots (backup copies) of the data volumes.

### AMIs
An AMI is a template that contains software configuration—for example, an operating system, applications, or tools. 

You must specify an AMI when you launch an instance because it contains all the necessary information and files required to build and launch the instance.

### Amazon EC2 lifecycle
An Amazon EC2 instance transitions through different states from the moment you launch it through to its termination.

### Amazon EC2 Auto Scaling
Amazon EC2 Auto Scaling helps you to have the right number of EC2 instances. The service automatically adds or removes EC2 instances according to policies that you define, schedule, and monitor. It helps you achieve better fault tolerance, availability, and cost management.

### Connecting to an EC2 instance
### Connecting to a Linux AMI
#### Linux or macOS
To connect to a Linux EC2 instance from a Linux or macOS operating system, you can use the following:
* An SSH client
* The EC2 Instance connect feature available in the console
* System Manager

#### Windows
To connect to a Linux EC2 instance from a Windows operating system, you can use the following:
* The OpenSSH client 
* PuTTY
* System Manager

### Connecting to a Windows AMI
#### RDP client
You can connect to your Windows instance using a Remote Desktop Protocol (RDP) client from your computer in the following ways:
* The default RDP client on windows
* Microsoft Remote Desktop App on macOS
* Remmina on Linux

Ensure that the security group associated with your instance allows incoming RDP traffic (port 3389) from your IP address.

#### Fleet Manager
You can use Fleet Manager, a capability of Systems Manager, to connect to Windows instances using RDP and display up to four Windows instances on the same page in the console. You can connect to the first instance in the Fleet Manager Remote Desktop directly from the instances page in the Amazon EC2 console.

#### Session Manager
Session Manager is a fully managed Systems Manager capability for managing your EC2 instances through an interactive, one-click, browser-based shell or through the AWS CLI. You can use Session Manager to start a session with an instance in your account. After the session is started, you can run PowerShell commands as you would for any other connection type.

### Management, maintenance, and operations
Once you have launched your instances, you will need a way to manage, maintain, and securely operate them. That is where Systems Manager comes in.

## Additional Resources
### [Amazon EC2i](https://aws.amazon.com/ec2/)

### [Amazon EC2 documentation](https://docs.aws.amazon.com/ec2/index.html)

### [Tutorials](https://aws.amazon.com/ec2/getting-started/)

### [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

## Containers on AWS
### Container Technology
A container is a standardized unit. In the physical world, a container is a standardized unit of storage. While this had a lasting impact on the shipping industry, the concept also had impacts on the world of computing. Let's take a look at how containers in the physical world and in computing have changed things.

Not so long ago, getting physical objects from point A to point B was a challenge. Objects can be oddly shaped—some secure, some not. You often had to load objects by hand into whatever vessel was carrying them. You wouldn't know how much cargo a vessel could take until all the cargo was loaded. The transport of objects was slow, inefficient, and costly.

Standardization of containers began in the eighteenth century and continued for the next 200 years until 1958, when Malcom McLean and Keith Tentlinger patented the current international shipping container.

Standardized containers improve cargo handling on ships. They also provide a consistent, predictable unit of storage that can be easily transferred to truck or rail transportation. By focusing on containers instead of individual pieces of cargo, we improved efficiency, increased productivity, and reduced costs for consumers. This is a great example of using abstraction to increase agility.

#### A container in computing
A container is a standardized unit that packages your code and its dependencies. This package is designed to run reliably on any supported platform because the container creates its own independent environment. With containers, workloads can be carried from one place to another, such as from development to production or from on premises to the cloud. In the same way that abstraction helped to increase agility in the physical world of shipping containers, abstraction helps to remove difficulties and inconsistencies in the virtual world. In the past, it was difficult to consistently and efficiently deliver physical cargo before shipping containers. Similarly, in the virtual world, it is difficult to consistently and efficiently deliver applications with bare-metal servers. Let's explore a couple considerations surrounding the use of bare-metal servers and VMs:
* **Bare-metal servers**: A bare-metal server runs a standalone operating system with one or more applications that use the libraries installed on top of the operating system. The maximum capacity is fixed; to scale, you must buy and configure additional servers.
* **VM**: Virtually every application can now consistently run on a VM. The downside to VMs is that the virtualization layer is heavy. Each VM has its own operating system instead of one that supports all VMs. This causes higher use of the host CPU and RAM, reducing efficiency and performance. Having an individual operating system for each VM also means more patching, more updates, and more space being taken up on the physical host. There's also significant redundancy: you've installed potentially the same operating system four times and potentially the same library three times.

Because containers isolate software from the other layers, their code runs identically across different environments—from development and staging all the way to production. Containers are lightweight, efficient, and fast.

#### Bare-metal servers
A bare-metal server runs a standalone operating system with one or many applications by using libraries installed on top of the operating system.

#### VMs
You can increase agility by putting a virtualization platform over the operating system. Now, you have isolated applications and their libraries with their own full operating system within a VM.

#### Containers
Virtual Machines virtualize a whole server, including the hardware, whereas the containers only virtualize the software layer.

You can deliver consistency and efficiency with containers. The containerization platform lets containers share a machine’s operating system kernel and exposes the underlying operating system file system. Sharing a machine’s operating system kernel allows for shared libraries but can permit individual libraries as necessary.

A container is a standardized unit of software designed to run quickly and reliably, on any computing environment that is running the containerization platform.

Containers are a form of virtualization that is implemented at the operating-system level.

They are lightweight, standalone packages that include everything needed to run an application, such as code, runtime system tools, system libraries, and settings.
A single server can host several containers, and all of these containers will share the underlying host and OS kernel. The containers may be services that are part of a larger enterprise application, or, they may be separate applications running in their own isolated environments.
How do containers differ from other forms of virtualization?

With bare metal servers, the architectural layers, including the infrastructure and application software layers, are built on top of the physical infrastructure.

For example, you install an operating system on top of your server hardware, you install shared libraries on top of that operating system, and then you install your applications, which use those libraries.

The problem with this architecture is that it is inefficient. Your hardware costs are the same, whether you're running at 0% utilization or 100% utilization.

All your applications are fighting for the same resources, and you have to keep the versions of your libraries in sync with all of the applications.

For example, if one application requires an updated version of a library that is incompatible with other applications running on that host, you may run into problems.
You can increase agility by putting a virtualization platform over the operating system.

With this model, applications and their libraries are isolated on their own operating system within a virtual machine or VM.

This improves utilization because you can add more VMs to run on top of the existing hardware, which can greatly reduce your physical footprint.

The downside of VMs is that the virtualization layer can be heavy. In this example, there are three operating systems on the host instead of one. This means three times more patching, more updates, and significantly more space used on the physical host.

And, installing the same operating system and libraries three times can be a waste of resources and storage space.
We can do better, which is where containers come in.

Containers are lightweight, efficient and fast. They can be built, started, and stopped faster than virtual machines, which allows for better utilization of the underlying hardware.

The container runtime shares the operating system's kernel, so you can create container images using file-system layers. You can share libraries when needed, or you can have isolated libraries for your applications.

Containers are standardized, which means they run the same code in any environment, from development and staging, all the way to production. The benefit of this is that the applications that you deploy and run in containers are agile and highly portable.

The most popular technology for containers today is Docker, which is a technology used by AWS services.

It is a lightweight container-virtualization platform that provides tools for creating, storing, managing, and running containers. It’s easy to integrate with automated build, test, and deployment pipelines.
Docker offers portability, and the ability to package an application with all of its dependencies in a single, read-only object.

You can run different application versions with different dependencies and different libraries simultaneously. This leads to much faster development and deployment cycles, and better resource utilization and efficiency.

These are the types of capabilities that developers want, and it all comes back to agility.

Much of the work behind containers comes from the concept of a container image. An image is a read-only template with instructions for creating a container.

A container runs as an instance of a container image. Once you create a container image, it can go anywhere that Docker is supported.

An image is usually based on another image, with some customization. For example, you may build an image that is based on the Ubuntu Linux image in the registry.

However, it installs a web server and your application, in addition to the essential configuration details to make your application run.

You can use images that were created by others and published to a public registry such as Docker Hub. Or, you can use images published to a private registry that that you can create using a service like Amazon Elastic Container Registry or Amazon ECR.

You can also create your own images and publish them to these registries.

#### Containerization platforms
Containerization platforms make containers highly portable. They are software solutions you can use to manage containerized applications. Generally, they provide capabilities like automation, orchestration, security, and customization for a container architecture. The following are a few different types of container platforms:
* Container engines
* Container orchestrators
* Managed container services

#### Container engine example: Docker
Docker is an example of a popular container engine that provides a container runtime environment and helps you to create containers, manage container images, and perform basic operations.

Docker is a software platform you can use to build, test, and deploy applications quickly. Docker packages software into containers that have everything the software needs to run, including libraries, system tools, code, and runtime.

**Running Docker on AWS provides developers a highly reliable, low-cost way to build, ship, and run distributed applications**.

#### Container orchestrator example: Kubernetes
Kubernetes is open-source software you can use to deploy and manage containerized applications at scale. Kubernetes works by managing a cluster of compute instances and scheduling containers to run on the cluster based on the available compute resources and the resource requirements of each container. Containers are run in logical groupings called pods, and you can run and scale one or many containers together as a pod.

**AWS makes it convenient to run Kubernetes. You can choose to manage Kubernetes infrastructure yourself with Amazon EC2 or get an automatically provisioned, managed Kubernetes control plane with Amazon EKS**.

### Container Images
A container image is a static file with executable code that can create a container on a computing system. A container image is immutable. This means it cannot be changed, so it can be deployed consistently in any environment. It is a core component of a containerized architecture.

#### Container image example: Dockerfile
When using the Docker containerization platform as your runtime, container images are composed in what is called a Dockerfile. A Dockerfile is a read-only template with instructions for creating a container image.

##### Dockerfile
Each line or layer of the Dockerfile contains an instruction and then the arguments that the instruction uses. An instruction can specify the image on which to base your custom image, run certain executables, expose ports, and more. You can create custom images, or you can use images that were created by others and published to a public or private image registry.

##### Container image
An image is usually based on another image, with some customization. To build a container image, the Dockerfile instructions are followed line by line.

Consider the container image itself as immutable, which means that it should not be changed outside of the build process. Represent all changes in the Dockerfile as a build step, and produce a new image. You can store container images in image registries for later use. 

#### Building a Docker image
To build your own image, create a Dockerfile by using a basic syntax to define how to create the image and run it.

##### FROM instruction
Every Dockerfile starts with the FROM instruction. It might be from another existing image, such as CentOS 7 in this example, or from a specific application image, such as OPENJDK or NGINX. You can also use FROM scratch, which is a reserved, minimal image that returns an empty filesystem.

##### RUN instruction
The RUN instruction here updates the operating system and installs the Apache HTTP server. The RUN instruction runs any commands in a new layer on top of the current image and commits the results. This results in a new image that is used for the next layer in the Dockerfile.

##### EXPOSE instruction
The EXPOSE instruction documents what network port to listen to at runtime. Here, the instruction is for port 80.

##### COPY instruction
The COPY instruction copies files from the client file system and specifies their location in the container image file system. In this example, it copies your shell script for your application.

The ADD instruction is similar to the COPY instruction. However, you can also use it to access a URL or extract a tar file.

##### RUN instruction
This second RUN instruction gives the shell script executable permissions.

##### CMD instruction
The CMD instruction defines what command the container should start when run. The instruction might be a shell script, as in this example, a shell built-in, or a call to an interpreted language runtime, such as Python or Node.js. A Dockerfile can have only one CMD instruction.

In addition to the five instructions in this example, other keywords are available in a Dockerfile, such as the following:
* LABEL for image metadata
* ENV for setting environment variables
* USER for setting users on the image
* WORKDIR for setting the working directory for relative paths throughout the rest of the Dockerfile

If you change the Dockerfile and rebuild the image, the layer you changed and all the following layers are rebuilt. This is part of what makes container images lightweight, small, and fast in comparison to other virtualization technologies.

Most images are built on top of base images that are minimal OS distributions such as Centos, Redhat, or Alpine images for Linux containers or Microsoft Nano Server or Windows images for Windows containers.

#### A running container is an instance of an image
Think of container images as more permanent, unchangeable objects. Think of containers as ephemeral or temporary objects. You can have multiple running containers derived from the same container image. Containers can be disposed of and new containers can be instantiated from the container image.

### Container Services on AWS
AWS container services offer a broad choice of services to run your containers. You have options whether you need full control over the installation, configuration, and management of your compute environment or you want to explore more managed options.

EC2 is great for all sorts of different use cases from running basic web servers to running high performance computing clusters. That being said though EC2 is incredibly flexible, reliable and scalable depending on your use case, you might be looking at alternatives for your compute capacity. For example, let's say you are looking for a way to run containers at scale on AWS. 

Containers can provide you with efficiency and portability in this context. I am specifically referring to containers like docker containers or containers that use the container run time. If you aren't sure what containers are, please review the readings on containers. Containers are portable because everything an application needs to run, including the application code, dependencies and configuration are all packaged up together as one executable, which is the container itself. Since everything is self contained, it means that you can expect your containers to behave the same way across different environments like development Q A and Production. 

AWS offers container services like Amazon Elastic Container Service, otherwise known as ECS or Amazon Elastic Kubernetes Service, otherwise known as EKS. Both of these services are container orchestration tools. When you use containers on AWS, you need processes to start stop, restart, and monitor containers running across, not just one EC2 instance, but a number of them together called a cluster. The process of doing these tasks is called container orchestration and turns out it's really hard to do on your own. If you have a few containers, it's not so bad. But once you get to hundreds or thousands of containers you are managing, it can be quite complex. 

Orchestration tools were created to help you run and manage containers. ECS is designed to help you run your containerized applications at scale without the hassle of managing your own container orchestration software. EKS does essentially the same thing but uses different tooling with different features. We aren't going to go too much into this now, however, I did include a link to more learning resources around containerized applications on AWS in the readings following this video. 

The way you can interact with these container services is you manage the containers running on a cluster through the orchestration tools. API and then the orchestration tool carries out the management tasks. You can automate scaling of your cluster, hosting your containers as well as automate scaling of the containers themselves. Containers have a shorter boot up time when compared to virtual machines. So if you need super fast response to increasing demand, then containers might be the service for you personally. 

I think the portability aspect that containers give are my favorite benefit of containerized applications. So you can choose to host containers on top of a cluster of EC2 instances as your hosting options, either for ECS or EKS. However, what if you were looking for an alternative to hosting your containers? Because you either don't need access to the underlying OS or you don't want to manage those EC2 instances. Well, you can use a compute platform called AWS Fargate which handles most of the underlying details for you. Fargate is a serverless compute platform for ECS and EKS and we'll talk more about what serverless is coming up next.

### Amazon ECS
Amazon ECS is a managed container service. It is used to deploy, run, and manage containerized applications.

Amazon ECS can run containers on clusters of EC2 instances and on the Fargate serverless compute engine. You can also run containers on customer-owned hosts outside of Regions.

Amazon ECS manages the complete lifecycle of containers. This includes scheduling containers on compute, allocating resources, upgrading containers, and auto scaling containers to meet increased demand. To comprehensively address all the needs of containerized applications, Amazon ECS seamlessly integrates with several AWS services. These include ELB, Amazon CloudWatch, and IAM.

The following are common use cases for Amazon ECS: microservices, websites, video rendering services, and machine learning.

**Amazon ECS comprehensively addresses challenges associated with managing containerized applications at scale**.

#### Benefits of Amazon ECS
##### Fully managed control plane
Amazon ECS is a fully managed container service, and customers don’t need to worry about managing any middleware software.

##### Fargate serverless compute engine integration
Amazon ECS has seamless integration with Fargate, the serverless compute engine. When customers use Amazon ECS with Fargate, they don’t need to manage any container hosts. Additionally, with Fargate, each containerized task runs in its own dedicated VM, which provides enhanced isolation and security by design.

##### Native integrations with valuable AWS services or capabilities
Amazon ECS has native integrations with AWS services and capabilities, such as the following:
* ELB
* CloudWatch
* AWS Cloud Map
* AWS Secrets Manager
* Parameter Store, a capability of Systems Manager
* AWS CodeDeploy
* Amazon ECR

By using Amazon ECS native integrations, containerized applications can take advantage of these AWS services or capabilities.

##### Proven performance and scale
Amazon ECS has a proven track record of running large-scale, mission-critical applications for customers across all industries.

##### Powerful simplicity
The powerful simplicity of Amazon ECS means that you can grow from a single Docker container to managing your entire enterprise application portfolio. Run and scale your container workloads across Availability Zones, in the cloud, and on premises without the complexity of managing a control plane or nodes.

##### No charge
Amazon ECS is a no-charge service. Customers pay only for the resources and other services that are used to run the containers.

#### Basic technical concepts of Amazon ECS

#### Launching a container with Amazon ECS
##### Clusters
An ECS cluster is a logical grouping of tasks or services that are run on infrastructure that is registered to the cluster. You can use clusters to isolate your applications. This way, they don't use the same underlying infrastructure. An ECS cluster is a logical grouping of tasks or services. When your tasks run on Fargate, your cluster resources are also managed by Fargate.

##### Containers and images
To deploy applications on Amazon ECS, your application components must be configured to run in containers. A container is a standardized unit of software that holds everything that your software application requires to run. This includes relevant code, runtime, system tools, and system libraries. Containers are created from a read-only template called an image.

##### Task definitions
A task definition is a text file that describes one or more containers that form your application. It's in JSON format. You can use it to describe up to 10 containers. The task definition functions as a blueprint for your application. It specifies the various parameters for it. For example, you can use it to specify parameters for the operating system, which containers to use, which ports to open for your application, and the data volumes to use with the containers in the task. The specific parameters available for your task definition depend on the needs of your specific application.

Your entire application stack doesn't need to be in a single task definition. In fact, it is  recommended to span your application across multiple task definitions. You can do this by combining related containers into their own task definitions, each representing a single component.

##### Tasks
A task is the instantiation of a task definition inside a cluster. After you create a task definition for your application in Amazon ECS, you can specify the number of tasks to run on your cluster. You can run a standalone task, or you can run a task as part of a service.

##### Services
You can use an ECS service to run and maintain your desired number of tasks simultaneously in an ECS cluster. Here's how it works: If any of your tasks fail or stop for any reason, the Amazon ECS service scheduler launches another instance based on your task definition. It does this to replace it and thereby maintain your desired number of tasks in the service.

#### Launching a container with Amazon ECS
To launch containers on supporting compute services with Amazon ECS, you can configure various options. After you create and configure your containers, you can use Amazon ECS to manage them. It scales your application and manages your containers for availability.

##### EC2 instances
For customers who want to manage or customize the underlying compute environment and host operating system, an ECS cluster can manage EC2 instances, provided they are running the Amazon ECS container agent and has been registered into the cluster.

The agent sends information about the current running tasks and resource utilization of your containers to Amazon ECS. It starts and stops tasks whenever it receives a request from Amazon ECS. 

The Amazon ECS container agent is included in the Amazon ECS optimized AMIs, but you can also install it on any EC2 instance that supports the Amazon ECS specification. Amazon EC2 offers the widest choice of instance types, including processor, storage, and networking.

##### Fargate
Fargate is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of EC2 instances. This is suited to customers who do not want to worry about managing servers, handling capacity planning, or figuring out how to isolate container workloads for security.

When you run your tasks and services with the Fargate launch type, you package your application in containers, specify the CPU and memory requirements, define networking and IAM policies, and launch the application. Each Fargate task has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources.

##### Hybrid, on-premises, and edge deployments
The following are additional options for running containers with compute services through Amazon ECS:

Amazon ECS Anywhere helps customers launch containers on their self-managed compute outside of AWS.
AWS Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience. 
AWS Wavelength provides an ultra-low latency mobile edge computing suited to 5G applications, interactive and immersive experiences, and connected vehicles.

#### How can Amazon ECS be used to architect a cloud solution?
Developers are modernizing applications by deconstructing monolithic architectures and migrating application components into container–based, service-oriented, and microservices architectures. Modern applications help improve scalability, reliability, and development efficiency because smaller, more focused teams can own the services.

In the following diagram of a multi-AZ architecture, an ECS Cluster manages EC2 instances located in two public subnets in two Availability Zones. In each Availability Zone, containers run EC2 instances inside tasks. The Application Load Balancer distributes traffic evenly to the different tasks.

##### ECS cluster
These are a logical grouping of tasks and services. An ECS cluster can use Amazon EC2, Fargate, or customer-owned hosts to run tasks (containers).

##### Task definition
A task definition is a text file that describes one or more containers that form your application. The task definition functions as a blueprint for your application. You can also specify parameters for it depending on the needs of your specific application.

##### Tasks
These are the smallest activation unit. A task can have one or more containers. A task is the instantiation of a task definition within a cluster. After you have created a task definition for your application within Amazon ECS, you can specify the number of tasks that will run on your cluster.

##### Container
A container is a standardized unit of software that holds everything that your software application requires to run. This includes relevant code, runtime, system tools, and system libraries. Containers are created from a read-only template called an image.

##### Amazon ECS Auto Scaling
Amazon ECS can manage the scaling of EC2 instances registered to your cluster through Amazon ECS Auto Scaling.

##### Application Load Balancer
Your Amazon ECS service can optionally be configured to use ELB to distribute traffic evenly across the tasks in your service.

#### Deploying an application to run on Amazon ECS
Welcome to this demonstration on creating an Amazon Elastic Container Service, Amazon ECS, Cluster. In this video, you'll learn how to create, configure, and delete an Amazon ECS cluster. From the a AWS Management Console, search for ECS in the Services search bar, and then choose Elastic Container Service. Now, from the Clusters panel, choose Create Cluster to begin the create cluster wizard. First, choose the EC2 Linux + Networking template to create an ECS cluster that consists of EC2 Linux instances to run containers. Choose Next step to begin configuring the cluster. Next, enter a name for the cluster. In this example, we will use ECSCluster. Choose an instance size for the EC2 instance type, and then choose the number of instances. Here we will choose one instance and then leave the default value for the Root EBS Volume. Next, we'll set up networking for the cluster. For the VPC, we will leave it as Create a new VPC, but in the future, you can use the drop-down menu to select an existing VPC. In the CIDR block text box, enter the CIDR block to use with the VPC. Use a private IP range here, such as the one shown. Then enter two subnets with the CIDR block you specified to use for container networking. Subnet 1 and 2 are populated in this demo. Note that network address translation will be set up in a later demonstration to provide access to the internet. Now that we have configured the cluster, choose Create. When the cluster resources components are provisioned, choose View Cluster. After a few minutes, the cluster has an Active status.

Now let's create a task definition for Amazon ECS. From the Amazon ECS panel, choose Task Definitions, and then choose Create New Task Definition. Choose the EC2 launch type to run tasks, and then choose Next step. Next, enter a name for the task definition. In this example, we will use MyTaskDefinition. Selecting a task role is optional. You can use task Role to grant permissions for a specific role in this task definition, such as accessing an S3 bucket. For the Network mode attribute, leave the default setting. This setting is the same as selecting bridge networking, which also appears in the dropdown menu. You can consult the EC2 user guide to learn about different networking modes. You can find a link to the user guide in the Learn more section of this course. Now, you can continue the configuration steps. Task execution role is the permission used by the ECS agent for activities, such as fetching an image from Amazon Elastic Container Registry or sending logs to Amazon CloudWatch. Note that ECS automatically creates ECS task execution role in your account, if you don't already have it configured. In the task size section, you can specify the task memory and number of CPU units needed for the task. All containers in the task will share the specified resources, and this is the maximum amount that can be used. We will use two gigabytes for Task memory and one virtual CPU for Task CPU. To create the container that will be used for this task, choose Add container. Next, enter a name for the container, and provide a URL to the image. Because bridge networking is used for this task definition, we can map a port from the container to the host. The NGINX container in this demo will serve traffic on port 80, which is mapped the same port on the container host. All other options on this page can be left as default values. To see the container definition, choose Add. Notice that the container we defined is listed under Container definitions. You can leave the remaining settings at their default values. To create the task definition, choose Create. Next, we will start a new task using the newly created task definition. Choose Actions, and then choose Run Task. For Launch type, choose EC2. Choose the name of the ECS cluster from the dropdown list, and then choose the number of tasks you want to run. Leave the remaining options as the default values and then choose Run Task. On the clusters page, notice the container cluster created is listed. Choose refresh to confirm that the first task is running. For more details, choose the running task. On the Tasks panel, expand the container name to see more details. Choose the public IP address under external link so you can reach the task container at port 80 through your web browser. Recall that we map port 80 of the NGINX container to port 80 on the host. The default webpage configured for NGINX container appears in the web browser. Next, we will configure load balancing. From the Amazon EC2 console, choose Load Balancers, and then choose Create Load Balancer. Next, in the Application Load Balancer panel, choose Create. Now we will set the basic configuration for the application load balancer. Enter a unique load balance name. For this demonstration, we will use myALB. Leave the other options set to the default values. From the Network mapping section, choose VPC created in the previous demonstration or the VPC you previously selected. Choose the two mapped Availability Zones, and then choose one subnet within each. Next, under Security groups, remove the default security group by choosing the X. Choose the security group name that begins with EC2ContainerService. From the Listeners and routing section, choose Create target group. This is where the task or container endpoints will be registered by ECS when they're created. Now, in the Specified group details panel, select a target type of instances, then enter a target group name in the text box. Leave the remaining configurations at their default values, and choose Next. Now, under registered targets, we will associate the container host instance to the target group. We haven't created any services or associated any tasks yet, so choose Include as Pending below. Then, choose Create target group to continue. Now, on the target group's page, the banner at the top of the panel shows the target group has been successfully created. It can now be associated with the load balancer being configured. Next, return to the Load balancer creation webpage tab. In the Listeners and routing section, refresh the list of target groups. Then, select the target group you created from the dropdown list. Next, review the configurations in the Summary section. The remaining configurations can be left at their default values. To finish creating the application load balancer, choose Create load balancer. Notice that a banner shows that the load balancer was successfully created. Choose View load balancer to continue. Return to the EC2 Dashboard, and under the Description tab in the Basic Configuration section, note the DNS name of the load balancer. You can open this in a new browser tab. Note the after we create the service, you'll see NGINX page as the URL. You can press the icon to the right of the DNS URL to copy it, then paste it into the text editor. Another option might be to write it down. This name will be used at the end of the demo to test the setup. Next, we will create a load balanced ECS service. Return to the Amazon ECS console, and then select Task Definitions from the left panel to see the task definition that you created in the previous demonstration. Select the task. Then from the Actions dropdown menu, choose Create Service. On the Create Service panel, for Launch type, choose EC2, enter a service name and choose the number of tasks you want to run. Review the default values for the other settings, and then choose Next step.

Now, for the load balancer type, choose Application Load balancer. Then choose the load balancer name that we created earlier from the dropdown list. Then choose the container name from the dropdown menu, and choose Add to load balancer. ECS will manage the registration and deregistration to the load balancer after the container is created. Next, choose HTTP port 80 from the production listener port dropdown menu. From the dropdown menu, for Target group name, choose the target group that we created during the load balancer setup. Choose Next step to continue. For Set Auto Scaling, confirm that Service Auto Scaling is set to Do not adjust service desired count. Choose Next step to continue. Review the service settings, and then choose Create service. Now, you'll see the details of the various components being provisioned. When the service creation process is complete, choose View Service. Finally, paste the load balancer's DNS name, copied earlier, into the address bar your web browser to view the page delivered by the ECS service. This completes the demo for creating and configuring an ECS cluster.

Because we don't need the resources anymore, it's time to delete them. From the Amazon EC2 console, choose Load Balancers. Select the load balancer you created, and then from the Actions dropdown menu, choose Delete. Next, confirm the deletion by choosing Yes, Delete. Now, from the EC2 dashboard, choose Target groups. Select the target group that we created. From the Actions dropdown menu, choose Delete. Next, confirm the deletion by choosing Yes, Delete. Then, in the Amazon EC2 console, set the cluster we previously created and choose Delete cluster. Confirm the deletion by entering the phrase, delete me, into the text box. Next, choose Delete. It might take several minutes to delete the cluster. You can monitor the progress in this pop-up panel.

#### What to remember about Amazon ECS?
To comprehensively address all the needs of containerized applications, Amazon ECS seamlessly integrates with several AWS services. These include ELB, CloudWatch, and IAM, just to name a few. 

##### SECRETS MANAGER
Use Secrets Manager for storing sensitive data in your container. The service helps you quickly rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

##### CONFIGURATION AUDITS
Use AWS Config and CloudTrail to audit your container configurations. 

AWS Config helps you assess, audit, and evaluate configurations of your AWS resources. CloudTrail also helps you set up governance, compliance, and operational and risk auditing of your AWS account.

##### MONITORING
CloudWatch provides you with data and actionable insights to monitor your applications by collecting logs, metrics, and events. You can use CloudWatch to detect anomalous behavior in your environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep your applications running smoothly.

##### LOGGING
AWS provides a Fluent Bit image with plugins for both CloudWatch Logs and Amazon Kinesis Data Firehose. This container image provides the capability to route logs to CloudWatch and Kinesis Data Firehose destinations. Destinations include Amazon S3, Amazon OpenSearch Service, and Amazon Redshift.

### Amazon ECR
AWS offers a secure container registry with Amazon ECR. It is integrated with Amazon ECS and Amazon EKS, which means you can easily store and run container images for applications with either orchestrator. All you need to do is specify the Amazon ECR repository in your task or pod definition for Amazon ECS or Amazon EKS to retrieve the appropriate images for your applications

You can use your preferred command-line interface to push, pull, and manage Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts.

#### Registry functions
A container registry has two core functions: pushing containers (uploading them to the registry) and pulling containers (downloading them from the registry). 

Pushing a container is part of application development. A developer writes application code and packages it as a container, which is called building a container image. The developer then pushes the image to the registry. 

After an image is in the registry, it can be pulled to be run by your applications. This image pull is often managed by container orchestrators, which are services that automate much of the operational effort associated with running containerized applications.

#### Highly available
Because container registries are the central point from which container images are pulled, they play a key role in the availability of applications. If an application needs to scale up to meet increased demand, it will need to pull a certain number of container images to start new tasks or pods. However, if the registry storing the images isn’t able to scale up to fulfill the image pulls, the application won’t be able to scale up to meet demand. Amazon ECR is highly available and scales to meet your demands without any provisioning on your end. It can effectively support applications where availability and scalability are important.

#### Security and access control
Amazon ECR uses IAM to control and monitor who and what (for example, EC2 instances) can access your container images. Through IAM, you can define policies to allow users in the same AWS account or other accounts to access your container images in private repositories. You can further refine these policies by specifying different permissions for different users and roles, such as push only, pull only, or full administrator access. For example, a running web application might be allowed to pull images from its specified repository but no other repositories and not be allowed to push images to any repository. Amazon ECR also provides you with container image vulnerability scanning, with a no-cost option (using Clair) and an enhanced option powered by Amazon Inspector Classic.

#### Encryption
You can transfer your container images to and from Amazon ECR through HTTPS. Your images are also automatically encrypted at rest using Amazon S3 server-side encryption. Amazon ECR also lets you choose your own key managed by AWS KMS to encrypt images at rest.

#### Team and public collaboration
Amazon ECR supports defining and organizing repositories (such as folders in the registry) using name spaces, which you can use to group similar repositories. For example, if both team 1 and team 2 need development and production environments, you can create dev/team1, prod/team1, dev/team2, and prod/team2.

You can control which actions another user can perform on your repository through resource-level policies. Then, you can share your repositories with different users and AWS accounts. You can also efficiently share your container artifacts with anyone in the world by storing them in a public repository to be found on the Amazon ECR website.

### What else should be remembered about Amazon ECR?
#### INTEGRATING AMAZON ECR
Remember that Amazon ECR is rarely used by itself but in conjunction with a container orchestrator like Amazon ECS or Amazon EKS. Amazon ECR is also integrated with continuous integration and delivery (CI/CD) tools, such as AWS CodePipeline, to help customers automate deploying code changes. Integrating Amazon ECR with other tools typically happens when building a cloud solution and building workflows to automate deployments.

#### SECURING SDLC
Customers developing containerized applications typically build containers iteratively, which means they build on top of an existing container in their registry. Registries are involved earlier in the software development lifecycle (SDLC) than container orchestrators like Amazon ECS and Amazon EKS. This means that registries play a key role in securing the SDLC, and many organizations are working to shift left to secure applications earlier in the development process to reduce risk.

#### VALIDATION
Instead of validating the security of a container image only before it is deployed into production, a shift left would begin the validation process when the first container is built and pushed to a development repository. Amazon ECR offers features like integration with IAM, encryption at rest, and vulnerability scanning to help you secure your SDLC.

### Using Amazon ECR with docker
In thiis example we first install a docker client on an Amazon Linux 2023 EC2 instance. We will then retrieve a container image that contains a MySQL Server on top of an Ubuntu distribution from an Amazon ECR public registry, instantiate and run a container, and connect to the database it hosts.

#### Install Docker client
On a Amazon Linux 2023, we install a Docker client:
* dnf install docker: Install the client.
* docker images: Verifies the Docker command works by listing the container images on the local host. Here, there is no image yet.
* docker container ls: List all the containers. There is no container yet on this EC2 instance.

#### Browse the Amazon ECR public repository
Navigate to https://gallery.ecr.aws(opens in a new tab) and look for a MySQL container. We select docker/library/mysql.

#### Copy the image URL
We select mysql 5.7.41 and copy the following image name: public.ecr.aws/docker/library/mysql:5.7.41

#### Run the container
We can now run the container using the Docker run command with the following options:
* -d: Runs as a background task.
* -name: The name of our choice for the container.
* -p: Maps the port 3306 of the container to the port 30306 of our host. 3306 is the default port to access a MySQL instance. The mapping will let us connect through the port 30306 or our local host.
* -e MYSQL_ROOT_PASSWORD: Sets the password for the root user.
We then verify the container is running with the command docker container ls that lists the running containers.

The run command pulls the image from the repository before creating and running the container. You can also pull the container first by using the Docker pull command.

#### Connect to the MySQL instance that runs in the container
We can now connect to our MySQL instance that is hosted in the container using the mysql command:
* -u: We connect using the root user.
* -p: The password is the one we previously passed to the Docker run command.
* -h: The ip is 127.0.0.1, the local host, because the container is running locally on our EC2 instance.
* -P: The port is 30306 that we previously mapped to the port 3306 of the container.

Password: MyS3cr3t

#### Summary
In this example, we connected to an Amazon ECR public registry that is available to anyone. When you create your own images, you can publish them to an Amazon ECR public registry for anyone to use or to an Amazon ECR private registry for private usage. An Amazon ECR private registry is provided to each AWS account; you can create one or more repositories in your registry and store images in them.

### Amazon EKS
### Kubernetes
Kubernetes is an open-source container orchestration platform supported by a strong and vibrant community. The Cloud Native Computing Foundation, a subsidiary of the Linux Foundation, maintains Kubernetes, one of the most popular projects on GitHub.

**AWS actively works with the Kubernetes community, including making contributions to the Kubernetes code base that helps Amazon EKS users take advantage of AWS services and features.**

Kubernetes supports multiple cloud providers in addition to on-premises servers. The Kubernetes API can be thought of as a single extensible layer that can be used to abstract resources both within AWS and on premises. When using Kubernetes on AWS, you can take advantage of the scale, performance, and breadth of features of the AWS offerings. You can do this while still using the same familiar Kubernetes API for deploying containers on premises. Kubernetes also uses a declarative format for setup automation. This reduces the time and cost for new developers joining projects. 

### Amazon EKS
Amazon EKS is a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications. 

In addition to managing the control plane, Amazon EKS can manage elements of the data plane (worker nodes), if you choose. Amazon EKS is tightly integrated with other AWS services, such as Application Load Balancers for load distribution, IAM for role-based access control, and Amazon Virtual Private Cloud (Amazon VPC) for pod networking.

#### Running the Kubernetes control plane
##### Amazon EKS
Amazon EKS automatically detects and replaces unhealthy control plane nodes, which removes a significant operational burden for running Kubernetes. This capability helps you focus on building your applications instead of managing AWS infrastructure.

##### API server
When you create a new cluster, Amazon EKS creates an endpoint for the managed Kubernetes API server that you use to communicate with your cluster (using Kubernetes management tools such as kubectl). This control plane must have at least two API servers.

##### etcd
Etcd is a strongly consistent, distributed key-value store that provides a reliable way to store data for distributed systems. Amazon EKS operates etcd clusters.

##### Worker nodes
A Kubernetes node is a machine that runs containerized applications. Each node has the following components:
* **Container runtime**: Software that's responsible for running the containers.
* **Kubelet**: This makes sure that containers are healthy and running within their associated pod.
* **Kube-proxy**: This maintains network rules for communication to your pods.

### Summary
#### Containers
A container is a standardized unit that packages your code and its dependencies. This package is designed to run reliably on any supported platform because the container creates its own independent environment. Docker is a famous containerization platform.

#### Container hosting options
##### EC2
An ECS cluster infrastructure capacity can be provided by EC2 instances that you manage. Using Amazon EC2 as your host can offer you more control over your infrastructure.

##### Fargate
Fargate is a serverless, pay-as-you-go compute engine that takes care of the infrastructure that your containers run on.

#### Container orchestration options
##### Amazon ECS
Amazon ECS is a fully managed container orchestration service that helps you deploy, manage, and scale containerized applications.

##### Amazon EKS
Amazon EKS is a managed container service used to scale Kubernetes applications in the cloud or on premises.

### Additional Resources
#### [Guides and tutorials about containers](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&amp;getting-started-all.sort-order=desc&amp;awsf.getting-started-category=category%23containers&amp;awsf.getting-started-content-type=*all)

#### [Amazon ECS](https://aws.amazon.com/ecs/)

#### [Amazon ECS documentation](https://docs.aws.amazon.com/ecs/index.html)

#### [Amazon ECS FAQs](https://aws.amazon.com/ecs/faqs/)

#### [Amazon ECS Best Practices Guide](https://docs.aws.amazon.com/pdfs/AmazonECS/latest/bestpracticesguide/bestpracticesguide.pdf)

#### [Amazon ECS PHP simple demo app](https://github.com/aws-samples/ecs-demo-php-simple-app) 

#### [Amazon EKS](https://aws.amazon.com/eks/)

#### [Amazon EKS Documentation](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)

#### [Amazon ECS compared to Amazon EKS}(https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/)

#### [Amazon ECR](https://aws.amazon.com/ecr/)

#### [Amazon ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)

#### [Amazon ECR Public Gallery](https://gallery.ecr.aws/)
Each repository you create in your public registry is available publicly in the Amazon ECR Public Gallery. 

## Serverless Computing on AWS
If you run your code on Amazon EC2, AWS is responsible for the physical hardware, and you are responsible for the logical controls, such as guest operating system, security and patching, networking, security, and scaling.

If you run your code in containers on Amazon ECS and Amazon EKS, AWS is responsible for more of the container management, such as deploying containers across EC2 instances and managing the container cluster. However, when running Amazon ECS and Amazon EKS on Amazon EC2, you are still responsible for maintaining the underlying EC2 instances.

If you want to deploy your workloads and applications without having to manage any EC2 instances, you can do that on AWS with serverless compute.

### Introduction: Serverless Computing on AWS
Every definition of serverless mentions the following four aspects:
* No servers to provision or manage
* Scales with usage
* No paying for idle resources
* Built-in availability and fault tolerance

With serverless, you can spend time on the things that differentiate your application instead of spending time on ensuring availability, scaling, and managing servers.

### Lambda
AWS Lambda is one of these serverless compute options you have available to you on AWS. Lambda allows you to package and upload your code to the Lambda service, creating what's called a Lambda function. Once you create a Lambda function, it isn't always running all of the time. 

Instead, Lambda functions run in response to triggers. You can configure a trigger for when you want your function to run, and from there, the Lambda service waits for the trigger. 

#### Common examples of triggers for Lambda functions
* an HTTP request
* an upload of a file to the storage service Amazon S3
* events originating from other AWS services
* in-app activity from mobile devices

When the trigger is detected, the code is automatically run in a managed environment, an environment you do not need to worry too much about because it is automatically scalable, highly available, and all of the maintenance of the environment itself is done by AWS. You do, however, get to choose the language your Lambda function is coded in, the amount of memory and CPU your function is allocated in the environment, its permissions, dependencies, and many other aspects of how the function runs. If you have one or 1000 incoming triggers, AWS Lambda will scale your function to meet demand, each in its own isolated environment. Lambda is currently designed to run code that has a runtime of under **15 minutes**. So this isn't for long-running processes like deep learning or batch jobs. You wouldn't host something like a WordPress site on AWS Lambda.

It's more suited for quick processing like a web backend for handling requests or a backend report processing service. One of the best things about Lambda is that you aren't billed for code that isn't running. You only get billed for the resources that you use down to 100 millisecond intervals. 

#### Lambda demo
Let's create a Lambda function that resizes images uploaded into the employee directory application to be a uniform thumbnail size. It makes sense to create this sort of logic with the Lambda function. You don't need an application to be running 24/7 on EC2 to resize photos uploaded to the application. You really only need the resize logic to run when a new photo is uploaded. So here's our diagram for the app. What I want to do is add this. When a new photo is uploaded to Amazon S3, it triggers a Lambda function that resizes the image and uploads it to the same S3 bucket, but to a different location than where the original image is stored.

Let's go ahead and build this out. You can see that I'm already in the AWS management console, and I'm going to go ahead and click, "Create function." From here, you have a couple of choices of how you want to create this function. We are going to author this one from scratch, and I already have the code written and downloaded to my local machine. So we're going to author from scratch. We'll name this, "Resize photo," and then we get to select the runtime, and that's basically the language that you've coded your function to be. So for us, we coded this in Python, so I'm going to select the Python runtime, and then I'm also going to expand this permission section here, and I'm going to use an existing IAM role for this code.

The Python code that we wrote is using the AWS SDK to make API calls to S3. Therefore, those API calls must be signed and authenticated as we discussed in earlier lessons. So, in order for this code to gain access to the temporary credentials needed to sign the request, we are going to associate an IAM role with the appropriate S3 permissions to this Lambda function. So I'm going to go ahead and select the existing role, which is called, "AWS Lambda, S3 access," and then I'll click, "Create function." At this point, we are now seeing the designer view, and I'm going to add a trigger for this Lambda function. I will select a trigger, and you can see here, as I scroll down, all of the different triggers that are available for Lambda. There are quite a bit, and there are also partner event sources powered by a service called Amazon Event Bridge, but I'm going to go ahead and select S3.

Then I will select the employee photos bucket, which is the bucket that our app is using. And then I will use the prefix, "Employee pic," because I know that that is the prefix where the function is uploading the images. And then I will scroll down and I'm going to acknowledge this recursive invocation piece here, and this is essentially just letting us know that if I were to have this Lambda function read from the Employee pic prefix, which is what triggered the event, and then process the image and upload it to the same spot, it would trigger another Lambda function run, and that would just go on forever. So you want to make sure that you are using a different place for the output than you are for the input. So I'm going to go ahead and click, "Add." And now I will scroll down and we are going to add the source code. So if you have source code with no dependencies, you can just type it right in here, which is really nice for experimentation.

But for us, we're using some outside dependencies for resizing the image in Python. So I'm going to upload a zip file from my local machine. Then I'm going to click, "Save." Then I'm going to scroll down and change this Lambda handler. Go ahead and check out the class notes if you want to learn more about Lambda handlers and how this works. I'm just changing this so that it's referring to my actual file, and then I'll click save. And now what I want to do is test this through the Employee Directory application. So I'm going to add a new employee. We'll name this Alana, location's USA, role is Cloud Technologist. She is a Mac user, and then we will upload her photo and click, "Save." So now it's been saved. I want to then test to see if this worked. So I'm going to click monitoring here.

And then I want to view the logs and CloudWatch Logs. So CloudWatch Logs is where the output goes from your Lambda function. I'm going to scroll down and click on the latest log stream, which is just the latest collection of log files from the Lambda function, and we can see that we did get the image resized output here. So I know that this code ran in response to the incoming event from S3. And that's it. That's how you create an AWS Lambda function at a high level. You could host the entire Employee Directory applications backend on Lambda with some refactoring, but I think I'm going to save that for a later conversation. 

#### Run code on Lambda
**With Lambda, you can run code without provisioning or managing servers or containers.**

Lambda is an ideal compute service for application scenarios that need to scale up rapidly and scale down to zero when not in demand, such as backend services, data processing, real-time stream processing, file processing, IoT backends, and web applications backends.

Lambda requires zero administration from the user. You upload your source code, and Lambda takes care of everything required to run and scale your code with high availability. There are no servers to manage, bringing you continuous scaling with subsecond metering and consistent performance.

#### Example: file processing
Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. You can call Lambda from over 200 AWS services and software as a service (SaaS) applications, and only pay for what you use.

##### Photo
A photo is taken and sent to an S3 bucket.

##### Event notification
The Amazon S3 new object created event is sent to Lambda.

##### Lambda
The Lambda function retrieves the source S3 bucket name and the key name of the uploaded object from the event parameter that it receives. It processes the image using its functions. The Lambda function can import and use an image processing library for instance.

##### New images
New images in various formats are output by the Lambda functions. They can be uploaded to another S3 bucket.

#### Use cases
##### Process data at scale
Run code at the capacity you need, as you need it. Scale to match your data volume automatically and create custom events.

##### Run interactive web and mobile backends
Combine Lambda with other AWS services to create secure, stable, and scalable online experiences. 

##### Gain powerful ML insights
Preprocess data before feeding it to your ML model. With Amazon EFS access, Lambda handles infrastructure management and provisioning to simplify scaling.

##### Create event-driven applications
Build event-driven functions for communication between decoupled services. Reduce costs by running applications during times of peak demand without crashing or over-provisioning resources.

#### Lambda core concepts
##### Function
A function is a resource that you can invoke to run your code in Lambda. A function has code to process the events that you pass into the function or that other AWS services send to the function.

You can invoke Lambda functions directly using the Lambda console, a function URL HTTP(S) endpoint, the Lambda API, an AWS SDK, AWS CLI, and AWS toolkits. You can also configure other AWS services to invoke your function in response to events or external requests or on a schedule. For example, Amazon S3 can invoke your function when an object is created in an S3 bucket, or Amazon EventBridge (CloudWatch Events) can invoke your function on a schedule. You can also configure Lambda to read items from a stream or a queue and invoke your function to process them.

When you create the Lambda function, it can be authored in several ways: 
* You can create the code from scratch.
* You can use a blueprint that AWS provides. For instance, the Get S3 Object blueprint provides code and configuration to fetch an object from an S3 bucket.
* You can use a container image to deploy and code and libraries into the Lambda runtime.

##### Lambda function handler
The Lambda function handler is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method. When the handler exits or returns a response, it becomes available to handle another event.

The Lambda function handler name specified at the time you create a Lambda function is derived from the following:
* Name of the file in which the Lambda handler function is located
* Name of the Python handler function

A function handler can be any name. If the runtime is Python, the default on the Lambda console is lambda_function.lambda_handler. This name reflects the function name as lambda_handler, and the file where the handler code is stored, for instance lambda_function.py. Other runtimes will have other naming conventions. If you choose a different name for your function handler on the Lambda console, you must update the name on the runtime settings pane.

##### Trigger
A trigger is a resource or configuration that invokes a Lambda function. Triggers include  AWS services that you can configure to invoke a function and event source mappings. An event source mapping is a resource in Lambda that reads items from a stream or queue and invokes a function.

##### Event
An event is a JSON-formatted document that contains data for a Lambda function to process. The runtime converts the event to an object and passes it to your function code. The JSON structure varies depending on the service that generates it and the event type, but they all contain the data that the function needs to process the event.

Lambda converts the event document into an object and passes it to your function handler.

##### Runtime
The runtime provides a language-specific environment that runs in an execution environment. The runtime relays invocation events, context information, and responses between Lambda and the function. You can use runtimes that Lambda provides or build your own. If you package your code as a .zip file archive, you must configure your function to use a runtime that matches your programming language. For a container image, you include the runtime when you build the image.

Various runtimes are available for the most used programming languages such as Python, Java, Node.js, and Go.

##### Deployment package
You deploy your Lambda function code using a deployment package. Lambda supports two types of deployment packages:
* A .zip file archive – This contains your function code and its dependencies. Lambda provides the operating system and runtime for your function.
* A container image – A container image includes the base operating system, the runtime, Lambda extensions, your application code, and its dependencies. 

##### Layer
A Lambda layer is a .zip file archive that can contain additional code or other content. A layer can contain libraries, a custom runtime, data, and configuration files.

Layers provide a convenient way to package libraries and other dependencies that you can use with your Lambda functions. Using layers reduces the size of uploaded deployment archives and makes it faster to deploy your code. Layers also promote code sharing and separation of responsibilities so that you can iterate faster on writing business logic.

#### How it works
##### Direct invocation
You can invoke Lambda functions directly using the Lambda console, a function URL HTTP(S) endpoint, the Lambda API, an AWS SDK, AWS CLI, and AWS toolkits. You can also configure other AWS services to invoke your function in response to events or external requests.

When you invoke a function, you can choose to invoke it synchronously or asynchronously.

##### Event
The events are data structured in JSON format. The JSON structure varies depending on the service that generates it and the event type, but they all contain the data that the function needs to process the event.

##### Lambda polling
For services that generate a queue or data stream, you set up an event source mapping in Lambda to have Lambda poll the queue or a data stream.

##### Event source mapping
An event source mapping is a Lambda resource that reads from an event source and invokes a Lambda function. You can use event source mappings to process items from a stream or queue in services that don't invoke Lambda functions directly. 

##### Lambda function
Lambda converts the event document into an object and passes it to your Lambda handler.

### Fargate
Fargate is a service that provisions serverless compute resources to run Amazon ECS and Amazon EKS containers. Fargate helps you to focus on building your applications when you let Fargate provision and manage the infrastructure required.

Fargate scales and manages the infrastructure, allowing developers to work on what they do best—application development. It achieves this by allocating the right amount of compute, eliminating the need to choose and handle EC2 instances, cluster capacity, and scaling. Fargate supports both Amazon ECS and Amazon EKS architecture and provides workload isolation and improved security by design.

Fargate abstracts the EC2 instance so that you’re not required to manage it. However, with Fargate, you can use all the same Amazon ECS primitive types, APIs, and AWS integrations. It natively integrates with IAM and Amazon VPC. Having native integration with Amazon VPC allows you to launch Fargate containers inside your network and control connectivity to your applications.

### Summary
#### Serverless
With serverless, you can spend time on the things that differentiate your application instead of spending time on ensuring availability, scaling, and managing servers.

#### AWS serverless services
##### Lambda functions
With Lambda, you can run code without provisioning or managing servers or containers. You can run code for virtually any type of application or backend service, including data processing, real-time stream processing, ML, WebSockets, IoT backends, mobile backends, and web apps, like your corporate directory app.

##### Fargate
Fargate is a service that provisions serverless compute resources to run Amazon ECS and Amazon EKS containers. Fargate helps you to focus on building your applications when you let Fargate provision and manage the infrastructure required.

### dditional Resources
#### [Serverless computing](https://serverlessland.com/)

#### [Serverless resources](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&amp;cards-all.sort-order=desc&amp;awsf.content-type=*all&amp;awsf.methodology=*all&amp;awsf.tech-category=tech-category%23serverless&amp;awsf.industries=*all&amp;awsf.business-category=*all)

#### [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

#### [Run a serverless "Hello, world"](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/)

#### [Fargate documentation](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)

## Module Summary
### Let's review AWS compute services
At this point, you've covered a few different AWS compute services. The services covered so far can handle a wide variety of use cases. So, how do you know when to use each one? To figure that out, I think it's time to play a game. Welcome to the 'Which AWS Compute Service Should I Choose for my Use Case?' Game Show. We're your hosts, and you are the contestant.

We will present three different use cases that require compute on AWS, and it's up to you to choose the right service for the use case. You'll have five seconds to answer each question. Ready?

I'm ready and I hope you are too. So, let's do it. First question is up. Consider a scenario where you are a developer who is tasked with creating a new feature for a web application being hosted on EC2. The web application is an online store, and right now, all of the items being sold in the store are loaded into a database manually behind the scenes. By manually, I mean there is a person who adds each row into a database for each new item to be sold in the store.

This process takes a long time and isn't very scalable, and on top of that, it's also prone to error. You are tasked with automating this process of getting new item information loaded into the inventory database. The goal is to have a person upload an inventory spreadsheet into Amazon S3, the object storage service, then have a process automatically load the data into the inventory database. What compute service would you use to host the processing logic to load the items from the file into the database? You have five seconds on the clock.

All right, let's discuss how you could have answered this question. You could have decided to use Amazon EC2 here. You could spin up a new instance specifically for this process and write some code that pulls the location of the spreadsheet for a new upload every so often. Updating the database when it finds a new file, that would work. But before I make my answer final here, I have a question. How often does new inventory get added to the database? New inventory gets updated one time per quarter.

Good to know. So, it's not very often, which means this process would only run once a quarter and that does change my answer. Here's why. Amazon EC2 charges per second or per hour. So, if I have an instance running all the time to serve a request that happens once per quarter, that seems like a lost opportunity to optimize for cost. I would be spending money on a resource I rarely use. It certainly would work, but maybe not the best fit for this use case. I could automate the process of starting and stopping the instance when needed, but instead, what about using AWS Lambda?

Bingo. AWS Lambda is the correct answer for this one. There are a few reasons. First of all, to address your concern on cost, AWS Lambda only charges you for the compute you consume when the code is actually running. And the code is run in response to triggers or a direct invocation. So, here's my suggestion. You know that the goal is to have someone upload an inventory document to S3, which should kick off the process of updating the database. You also learned that AWS Lambda has triggers that run your Lambda functions code. AWS Lambda integrates with many AWS services to act as triggers and Amazon S3 is one of them. So, my suggestion would be to create an AWS Lambda function, configure a PutEvent as the trigger from Amazon S3, then when the inventory is uploaded to Amazon S3, it will trigger the Lambda function to run and the code in the function will parse the inventory document and add each item into the database.

Time for the next question. Let's say you have an application currently hosted in your on-premises data center which needs to be migrated to AWS. It's currently running on Linux servers in the data center, and you want to minimize the amount of refactoring needed to migrate to AWS. It's important that this workload is elastic and can support varying demand. What compute option would you choose? Five seconds on the clock.

Time's up. Now I'll go over the answer. Considering the fact that minimizing refactoring is an important aspect of this workload, I would architect a solution using Amazon EC2 as the compute service. EC2 instances can be launched from Linux-based AMIs and the application could be hosted on the EC2 instance the same way it would be hosted on a Linux server on-premises. Amazon EC2 also has the ability to scale in or out based on demand. So, I think EC2 is the best service for this one.

That is correct. So, if you answered "EC2" at home, good work. Before we move on to the final question, let's dive into this answer a little more. Morgan, can you explain the thought process behind eliminating the other compute services we covered as answers to this question?

Sure thing. So, AWS Lambda could work, but you can't just upload the same code you would've run on an Amazon EC2 instance into a Lambda function. There would be a decent amount of refactoring in order to take advantage of that service. Same idea with any of the AWS container services, like ECS or EKS. Again, you'd have some amount of rework required to migrate to using containers. Therefore, Amazon EC2 is the best option for this migration. Now, time for one final use case, and this one is for all the marbles.

Imagine a scenario where you are planning to write a brand new application using micro-services or a service-oriented design, and you want to architect the application where it can scale up or down quickly, and you want to lower the risk of deploying new changes to production. Which AWS compute service would you use?  Five seconds.

Okay. Time's up. The answer for this use case is AWS container services like Amazon ECS or Amazon EKS.

Correct. The answer is either ECS or EKS for this one. Because using containers makes it easier to support microservices or service-oriented designs. Containers boot up quickly, so scaling is quicker than with EC2 instances, and the use of containers helps with code portability. Meaning, if I write the code on my laptop and I run it in a container, then I test it in QA, in a container, I can then expect that the same container would behave the same way once deployed to production, thus reducing the risk of any issues that might occur because of environmental issues.

All right, there you have it. Different use cases for a few of the AWS compute services. Make sure you read up on AWS's other compute offerings and make informed decisions when architecting your solutions. You'll find there are a lot of options.

Remembering that these services exist to best suit different use cases helps. Don't try to use the same compute service for all of your use cases. Instead, pick the right one for the job and consider reevaluating choices for existing workloads, as AWS continues to release new services and improve offerings.

# Assessment
## What is an Amazon ECS cluster?
**A group of tasks**.

The other options are incorrect because of the following:
* An Amazon ECS cluster is a logical grouping of tasks hosted on AWS Fargate, Amazon EC2 instances, or external instances. One cluster can contain a mix of tasks hosted on different compute services. Tasks define the underlying infrastructure used to run containers. Amazon ECS does not manage container images; it pulls images from a registry, such as Amazon ECR to instantiate containers.
