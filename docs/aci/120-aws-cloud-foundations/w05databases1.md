###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Databases 1
A database is a logically organized collection of information, designed in such a way that the information within can be accessed for later use by a computer program. Databases give access to the data while keeping the integrity of the data in a secure environment. 

## Foundational Database Concepts
### Data models and structures
A data model is the logical structure of a database and determines the rules for how information can be organized and used. The data model you choose is influenced by the structure of your data. 

### Data source types
#### STRUCTURED
Structured data is often organized to support transactional and analytical applications. Structured data is most commonly stored in relational databases but can also be stored in nonrelational databases. This data source type is valuable because you can gain insight into overarching trends by efficiently running powerful data queries and analysis.

#### SEMI-STRUCTURED
Semi-structured data can be just as predictable and organized as structured data. The difference is that semi-structured data is flexible and can be updated without the requirement to change the schema for every single record in a table. You can use semi-structured data to capture any data in any structure as data evolves and changes over time. Semi-structured data is often stored in nonrelational stores.

Examples of semi-structured data include XML, email, and JSON. The following example is JSON.

#### UNSTRUCTURED
**Unstructured** data is not organized in any distinguishable or predefined manner. Common stores for unstructured data are nonrelational key-value databases. Unstructured data is full of irrelevant information, which means data needs to first be processed to perform any kind of meaningful analysis.

Examples of data considered to be unstructured are text messages, word processing documents, videos, photos, and other images. These files are not organized other than being placed into a file system, object store, or another repository such as a data lake.

### Database terms
#### SCHEMA
A database schema is the blueprint of the database. The schema outlines the relationships within the database and the constraints of the database.

Databases can use a fixed schema for structured data, or a use schema-less approach for semi-structured or unstructured data.
* A schema-less database manages information without the need for a blueprint.
* Semi-structured data does not follow the format of a tabular data model or relational databases because it does not have a fixed schema.

#### READ/WRITE
Reading and writing to a database is just what it sounds like.
* When you complete actions that read from the database, you are accessing data for a particular purpose.
* When you complete actions that write to the database, you are putting new data into the database or changing data that is already existing.

Knowing if your workload will have more read operations or write operations will help you to design a database that is optimized for speed and efficiency.

### Online Transaction Processing (OLTP) and Online Analytical Processing (OLAP)
There are two primary models for data processing that use a relational database management system, or RDBMS—online transaction processing and online analytical processing. 

#### Online transaction processing (OLTP)
These systems are optimized to support high volumes of update, insert, and delete operations. 

To optimize transactional efficiency, OLTP database table schemas use normalization, a process that reduces data redundancy and improves overall data integrity. The data is distributed over a number of tables and might require highly complex join operations when queried. A great example of an OLTP system is a bank automated teller machine, or ATM, network in which many customers access their bank accounts and update the balances.

#### Online analytical processing (OLAP)
These analytical systems are optimized for querying, extracting, and combining large sets of aggregated historical data from OLTPs. With OLAP databases, users can view different summaries of multidimensional data. Unlike OLTP transactional queries, which generally are run frequently and respond in milliseconds, OLAP transactions can take minutes or hours and are run less frequently. 

Using OLAP, you can extract information from large datasets and analyze it for decision-making. An example of an OLAP system is a data warehouse. Business intelligence tools are typically used to query a data warehouse and create user-friendly views, such as reports, dashboards, charts, and graphs.

Beyond their functional differences, OLTP and OLAP systems differ in the way they are architected. OLTP systems are designed for operational workloads, whereas OLAP systems are designed for business insights. 

### Data indexing
You navigate a relational database using structured query language (SQL). Tables should be indexed to allow a query to quickly find the data needed to produce a result. Indexes can also help control the way data is physically stored on disk. They physically group records into a predictable order based on the key values within the table. This plays a huge part in the speed and efficiency of queries.

In a table with 12,000 rows, without an index, the query must scan 12,000 rows to find orders placed on a specified date. When the table is indexed by OrderDate, for example, the query seeks the range of orders placed only on the specified date. In the case here, the query would be faster because it is only searching the 50 rows in the range.

### SQL
SQL is the standard language for accessing and working with relational databases. Using SQL queries, you can do the following:
* Run queries against a database.
* Retrieve data from a database.
* Insert records in a database.
* Update records in a database.
* Delete records from a database.
* Create new databases.
* Create new tables in a database.

You can enter SQL commands into your relational database engine to return data from the database.

### DBMS
A database management system (DBMS) is a method of accessing, interacting, and manipulating a database, normally through software or similar tools. Examples of database management systems would include Amazon Relational Database Service (Amazon RDS), Amazon Redshift, and Amazon DynamoDB.

### Database controls
To ensure the security, concurrency, and integrity of your database and database management system, it is important to implement the appropriate controls. These controls include limiting access according to the principle of least privilege, and a data recovery solution in the event of accidental data loss or corruption.

#### Security controls
There are numerous best practices available to guide you in implementing the appropriate security controls for your databases and database management systems. A good place to start is the AWS Well-Architected security pillar. Best practices for the implementation of administrative controls, detective controls, and preventative controls can be found within the documentation. 

Security of the cloud is the responsibility of AWS. AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. Your level of responsibility for security in the cloud will depend on the AWS service that you use. This can include factors such as data classification, organizational requirements, and applicable laws and regulations.

#### Database concurrency and integrity controls
Database concurrency and integrity depends on transactional compliance. Transactions are groups of statements or operations that take place in a database. Issues arise when two sessions try to change the same record or item at the same time. Transactional compliance includes methods like ACID and BASE for maintaining consistency and integrity in a database.

##### ACID COMPLIANCE
Atomicity, consistency, isolation, and durability (ACID) compliance is used in a structured database. One goal of an ACID compliant database is to return the most recent version of all data. It also must ensure that data entered into the system meets all assigned rules and constraints at all times.
* **Atomicity**: When completing a transaction, atomicity ensures that your transactions either completely succeed or completely fail.
* **Consistency**: Consistency ensures that all transactions provide valid data to the database. Consistency also ensures that data updates are not made available until all synchronous replicas have been updated as well.
* **Isolation**: Isolation ensures that one transaction cannot interfere with another concurrent transaction.
* **Durability**: Data durability is making sure your changes actually stick.

##### BASE COMPLIANCE
BASE compliance is used in a structured or semi-structured database. BASE supports data integrity in nonrelational databases. 
* **Basically available (BA)**: Basically available means that one instance can receive a change request and make that change available immediately. In an ACID system, the change does not become available until all instances are consistent. Consistency in a BASE model is traded for availability.
* **Soft state**: In a BASE system, there are allowances for partial consistency across distributed instances. For this reason, BASE systems are considered to be in a soft state, also known as a changeable state. In an ACID system, the database is considered to be in a hard state because users cannot access data that is not fully consistent.
* **Eventually consistent**: This reinforces the other letters in the acronym. The data will be eventually consistent. In other words, a change will eventually be made to every copy. However, the data will be available in whatever state it is during the propagation of the change. 

#### Recovery controls
Databases can be backed up in multiple ways, including the use of automatic backups and database snapshots. We will use Amazon RDS for this example.
* **Automatic backups**: When you create an Amazon RDS database, automatic backups are enabled by default. Amazon RDS will back up the entire database and transaction logs by creating a storage volume snapshot of your database instance. You can also configure the backup retention period, which is the number of days that backups are kept. Finally, you can restore your database instance to any specific time during the backup retention period, which creates a new database instance. 
* **Database snapshots**: You can take manual database snapshots of your database instance if you want to keep your automated backups for longer than 35 days. Snapshots are saved in Amazon Simple Storage Service (Amazon S3) and are available until you delete them. 

### Additional Resources
#### [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

#### [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

## Database Paradigms
### Database Paradigms
In general, databases fall into two main categories; relational and nonrelational. Relational databases are best for structured data. Nonrelational databases are best for unstructured and semi-structured data.

### Relational database basics
A relational database is a collection of data records organized as a set of tables with rows and columns. Each row holds information about a record, and the columns contain attributes of the data. For example, in an employee database a record row for an employee might include attribute columns for employee number, last name, first name, and department. The values for the employee's attributes would be shown in the record's row.

Each row has an identifier column or group of identifier columns that uniquely distinguish the record from other records. The value in the identifier column is called a primary key. Other tables can reference a primary key. A record in another table that references a primary key is called a foreign key.

### Example: Relational database
Let's review an example of a relational database for cloud computing courses that an employee might be required to take. For this example, assume that the course curriculum for employees has three tables.
* The first table contains the course listings.
* The second table contains the list of course books.
* The third table contains the list of course instructors.

When an employee requests course information, they receive the course title from the Course table. In this example, the course title, **Getting Started with Databases**, is found in the Course table. The course book name from the Books table is Introduction to Databases. Finally, the instructor's name, Mary Major, is found in the Instructors table. The three tables are related by the Course_ID, which is the primary key for the Course table, and it appears in all three tables as a foreign key. 

Relational databases have maintained their popularity because they are easy to use, have data integrity controls and accuracy, use a common shared query language, and are excellent at reducing redundancy and overall data storage.

### AWS relational databases
#### Amazon Relational Database Service (Amazon RDS)
Amazon RDS provides cost-efficient and resizable capacity while automating time-consuming administration tasks including hardware provisioning, database setup, patching, and backups.

#### Amazon Aurora
Amazon Aurora is a MySQL-compatible and PostgreSQL-compatible relational database engine that combines the speed and availability of high-end commercial databases with the simplicity and cost-eﬀectiveness of open-source databases.

#### Amazon Redshift
Amazon Redshift is a fully managed data warehouse environment that uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes.

### Nonrelational Databases
A nonrelational database stores data in unstructured ways using one of many storage models, including key-value pairs, documents, and graphs. Nonrelational schemas are dynamic. A row does not have to contain data for each column. Nonrelational databases scale out horizontally, and they can work with structured and semi-structured data.

Nonrelational databases have continued to grow in popularity because they were designed to overcome the limitations of relational databases for handling the demands of variable structured data. Nonrelational databases are purpose-built for specific data models and have flexible schemas for building modern applications. Nonrelational databases are widely recognized for their flexibility, scalability, high performance, and highly functional APIs.

### Use case: Customer experience management
A good example of a use case for nonrelational databases is providing a personalized customer experience. Each customer has different preferences, desires, and habits. Customers expect a consistent personalized experience every time they interact with an application.

A nonrelational database can keep track of customer data, respond in near real time, and can handle all types of data from a variety of sources to seamlessly capture and integrate new data. Nonrelational databases are great for solving problems that cannot be solved with relational databases. 

### Types of nonrelational databases
AWS has many nonrelational databases available for you to choose from. The type of nonrelational database you choose will depend on the data that you are working with. 

#### Key-value databases
A key-value database is a type of nonrelational database that uses a simple key-value method to store data. A key-value database stores data as a collection of key-value pairs in which a key serves as a unique identifier. Both keys and values can be anything, ranging from simple objects to complex compound objects. Key-value databases are highly partitionable and allow horizontal scaling at scales that other types of databases cannot achieve. For example, Amazon DynamoDB allocates additional partitions to a table if an existing partition fills to capacity and more storage space is required.

##### AWS key-value database solution
###### Amazon DynamoDB
DynamoDB is a fully managed key-value and document database. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools.

#### Wide-column databases
A wide-column database is a type of NoSQL database that stores data across flexible columns. The names and format of the columns can vary across rows. It is designed to be scalable, with fast queries for a particular value in a column. It differs from relational databases that store data in fixed rows and tables.

Wide-column databases are mainly used for analytical and query-intensive environments, such as data mining, business intelligence, data warehouses, and decision support.

##### AWS wide-column database solution
###### Amazon Keyspaces
Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra–compatible database service. 

#### Document databases
A document database is a type of nonrelational database that is designed to store and query data as JSON-like documents. Document databases make it easier for developers to store and query data in a database by using the same document-model format they use in their application code. The flexible, semi-structured, and hierarchical nature of documents and document databases allows them to evolve with applications’ needs. 

The document model works well with use cases such as catalogs, user profiles, and content management systems where each document is unique and evolves over time. Document databases enable flexible indexing, powerful ad hoc queries, and analytics over collections of documents.

##### AWS document database solution
###### Amazon DocumentDB
Amazon DocumentDB is a fast, scalable, highly available document database service that supports MongoDB workloads. Data in Amazon DocumentDB is stored as JSON-like documents and maps naturally to how data is modeled in applications.

#### Graph databases
Graph databases are purpose-built to store and navigate relationships. Relationships are first-class citizens in graph databases, and most of the value of graph databases is derived from these relationships. Graph databases use nodes to store data entities and edges to store relationships between entities. An edge always has a start node, end node, type, and direction, and an edge can describe parent-child relationships, actions, ownership, and the like. There is no limit to the number and kind of relationships a node can have.

A graph in a graph database can be traversed along specific edge types or across the entire graph. In graph databases, traversing the joins or relationships is very fast because the relationships between nodes are not calculated at query times but are persisted in the database. Graph databases have advantages for use cases such as social networking, recommendation engines, and fraud detection, when you need to create relationships between data and quickly query these relationships.

##### AWS graph database solution
###### Amazon Neptune
Neptune is a fully managed graph database service. Neptune makes it easy to build and run applications that store billions of relationships and query the graph with millisecond latency.

#### Search-engine databases
A search-engine database is a type of nonrelational database that is dedicated to the search of data content. Search-engine databases use indexes to categorize the similar characteristics among data and facilitate search capability. Search-engine databases are optimized for dealing with data that might be long, semi-structured, or unstructured, and they typically offer specialized methods such as full-text search, complex search expressions, and ranking of search results.

##### AWS search-engine database solution
###### Amazon OpenSearch Service
OpenSearch Service is a managed service that makes it easy to deploy, operate, and scale OpenSearch Service clusters in the AWS Cloud.

#### In-memory databases
In-memory databases are purpose-built databases that rely primarily on memory for data storage, in contrast to databases that store data on disk or SSDs. In-memory data stores are designed to provide minimal response times by eliminating the need to access disks. Because all data is stored and managed exclusively in main memory, in-memory databases risk losing data upon a process or server failure. In-memory databases can persist data on disks by storing each operation in a log or by taking snapshots.

In-memory databases are ideal for applications that require microsecond response times or have large spikes in traffic such as gaming leaderboards, session stores, and real-time analytics.

##### AWS in-memory database solution
###### Amazon ElastiCache
ElastiCache is a fully managed, in-memory data store and cache that provides scalability to maintain sub-millisecond response times with fluctuating application demands. 

###### Amazon MemoryDB for Redis
MemoryDB for Redis is a durable, in-memory database service that delivers ultra-fast performance. It is purpose-built for modern applications with microservices architectures.

#### Time series databases
Time series databases are optimized for storing and analyzing time-stamped or time series data. Time series data is measurements or events that are tracked, monitored, collected, or aggregated over time. Time series databases are excellent for measuring change over time. 

##### AWS time series database solution
###### Amazon Timestream
Timestream is a fast, scalable, and serverless time series database service that makes it easier to store and analyze trillions of events each day. Timestream automatically scales up or down to adjust capacity and performance.

#### Ledger databases
Ledger databases provide a centralized and trusted authority to maintain a scalable, immutable, and cryptographically verifiable record of transactions for every application. They are used for systems of record, supply chain, registrations, and banking transactions.

##### AWS ledger database solution
###### Amazon QLDB
Amazon Quantum Ledger Database (Amazon QLDB) is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log owned by a central trusted authority. 

### Knowledge Check
#### A consultant is working with a city’s department of transportation. The department wants to aggregate the large amount of data from their traffic sensors to determine road usage patterns and changes over time. 

Which AWS database solution could the consultant suggest that would best fit their needs?

**Amazon Timestream** is a fast, scalable, and serverless time-series database service that makes it easier to store and analyze trillions of events per day. Amazon Timestream automatically scales up or down to adjust capacity and performance.

The other options are incorrect because of the following: 
* Amazon ElastiCache relies primarily on in-memory storage, which would not be ideal for the task described.
* AWS QLDB provides cryptographically verifiable transaction logs, which would not be ideal for the task described. 
* Amazon OpenSearch Service is a search-engine database and is not ideal for aggregating traffic data and analyzing it.

### Summary
#### Relational databases
A relational database is a collection of data records organized as a set of tables with rows and columns. Each row holds information about a record, and the columns contain attributes of the data.

Relational databases are still the most popular and most used database category due to their ease of use, data integrity controls and accuracy, common shared query language, and excellence at reducing redundancy and overall data storage.

##### AWS relational databases
AWS has a number of relational database services to choose from. 
* **Amazon RDS** - a cost-efficient and resizable database that automates time-consuming administration tasks.
* **Amazon Aurora** - a MySQL and PostgreSQL compatible relational database engine that combines the speed and availability of high-end commercial databases with the simplicity and cost-eﬀectiveness of open source databases.
* **Amazon Redshift** - a fully managed data warehouse environment that uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes.

#### Nonrelational databases
Designed to overcome the limitations of relational databases, non-relational continue to grow in popularity. Nonrelational databases store data in unstructured ways using one of many storage models, including key-value pairs, documents and graphs. Nonrelational schemas are dynamic. A row does not have to contain data for each column. Nonrelational databases scale out horizontally, and they can work with unstructured and semistructured data.

##### AWS non-relational databases
AWS has a number of relational database services to choose from based on data type and needs. 
* **Amazon DynamoDB** - a fully managed key-value and document database. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools.
* **Amazon Keyspaces** - Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra–compatible wide-column database service. 
* **Amazon DocumentDB** - a fast, scalable, highly available document database services that supports MongoDB workloads. Data in Amazon DocumentDB is stored as JSON-like documents and maps naturally to how data is modeled in applications.
* **Amazon Neptune** - a fully managed graph database service. Neptune enables the building and running of applications that store billions of relationships and query the graph with millisecond latency.
* **Amazon OpenSearch Service** - a managed search-engine database service that enables the deployment, operation, and scaling of OpenSearch clusters in the AWS Cloud.
* **Amazon ElastiCache** - a fully managed, in-memory data store and cache that provides scalability to maintain sub-millisecond response times with fluctuation application demands. 
* **Amazon MemoryDB for Redis** - a durable, in-memory database service that delivers ultra-fast performance. It is purpose-built for modern applications with microservices architectures.
* **Amazon Timestream** - a fast, scalable, and serverless time-series database service that the storage and analysis of trillions of events per day. Amazon Timestream automatically scales up or down to adjust capacity and performance.
* **AWS Quantum Ledger Database** - a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log owned by a central trusted authority. 

### Additional Resources
#### [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

#### [Amazon Keyspaces](https://aws.amazon.com/keyspaces/)

#### [Amazon DocumentDB](https://aws.amazon.com/documentdb/)

#### [Amazon Neptune](https://aws.amazon.com/neptune/)

#### [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)

#### [Amazon ElastiCache](https://aws.amazon.com/elasticache/)

#### [Amazon Timestream](https://aws.amazon.com/timestream/)

#### [Amazon Quantum Ledger Database](https://aws.amazon.com/qldb/)

#### [Amazon RDS](https://aws.amazon.com/rds/)

#### [Amazon Aurora](https://aws.amazon.com/rds/aurora/)

#### [Amazon Redshift](https://aws.amazon.com/redshift/)

## Amazon Relational Database Service (Amazon RDS)
### Pre-assessment
#### What are two purchasing options for Amazon RDS database compute resources? (Select TWO.)
The correct options are **On-demand** and **Reserved**. 

The other options are incorrect because of the following: 
* General purpose and provisioned are database storage types.
* Multi-AZ is an Amazon RDS deployment method.

#### What is the maximum retention period for DB instance backups in Amazon RDS?
After you create a DB instance, you can modify the backup retention period. You can set the backup retention period to 0–35 days.

The other options are incorrect because the backup retention period can only be set between 0 and 35 days.

#### Which statement about Amazon RDS Multi-AZ deployments is true?
**One or more secondary standby DB instances is automatically provisioned in a different Availability Zone.**

The other options are incorrect because of the following:
* Your primary DB instance cannot be split into separate Availability Zones.
* Although multi-Region replicas are possible, one or more secondary DB instance is not automatically provisioned in different AWS Regions.
* Your primary DB instance cannot be split into separate AWS Regions.

### Amazon RDS
Amazon RDS is an AWS core database service. Amazon RDS is a fully managed database solution that supports multiple database engines to suit the needs of most relational database use cases. Amazon RDS makes it easy to go from project conception to deployment. There's no need to provision infrastructure or to install and maintain database software. 

#### Amazon RDS storage autoscaling
You can scale your database's compute and storage resources, which can minimize downtime. Amazon RDS storage autoscaling automatically scales storage capacity in response to database workloads. Previously, you had to manually provision storage capacity based on anticipated application demands. Under-provisioning could result in application downtime, and over-provisioning could result in under-utilized resources and higher costs. With Amazon RDS Storage you can set your desired maximum storage limit, and RDS takes care of the rest.

#### Highly reliable, highly available
Amazon RDS runs on the same highly reliable infrastructure used by all other AWS services. When you provision a Multi-AZ DB instance, Amazon RDS synchronously replicates the data to a standby instance in a different Availability Zone. Amazon RDS has many other features that enhance reliability for critical production databases, including automated backups, database snapshots, and automatic host replacement.

#### Cost-effective
Amazon RDS is cost-effective because you can optimize your costs based on your needs and pay for only what you use. Costs are based on the compute resources used to run the DB instance, database storage, and the data transferred in and out of Amazon RDS.

Amazon RDS database compute resources has two purchasing options: 
* On-demand DB instances, which are pay-as-you-go
* Reserved instances, which offer low prices with a 1–3-year commitment

Amazon RDS database storage resources have several purchasing options depending on the needs of your workload. You pay for the gigabyte storage each month.

#### Secure
With Amazon RDS, you run your DB instances in a virtual private cloud (VPC). This gives you the ability to isolate your DB instances and connect to your existing IT infrastructure. RDS also offers encryption server-side encryption for data at rest and in transit. 

### Amazon RDS at a glance
#### AWS Regions, Availability Zones, and Local Zones
You can run your DB instance in several Availability Zones, an option called a Multi-AZ deployment. When you choose this option, Amazon automatically provisions and maintains one or more secondary standby DB instances in a different Availability Zone. Your primary DB instance is replicated across Availability Zones to each secondary DB instance. This approach helps provide data redundancy and failover support, eliminate I/O freezes, and minimize latency spikes during system backups. In a Multi-AZ DB clusters deployment, the secondary DB instances can also serve read traffic. 

Local Zones are extensions of AWS Regions that are geographically close to users. You can extend any VPC from the parent AWS Region into Local Zones. To do so, create a new subnet and assign it to the AWS Local Zone. When you create a subnet in a Local Zone, your VPC is extended to that Local Zone. The subnet in the Local Zone operates the same as other subnets in your VPC.

When you create a DB instance, you can choose a subnet in a Local Zone. Local Zones have their own connections to the internet and support AWS Direct Connect. Thus, resources created in a Local Zone can serve local users with very low-latency communications.g

### Multi-AZ deployments
Amazon RDS Multi-AZ deployments provide enhanced availability and durability for DB instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB instance, Amazon RDS synchronously replicates your data to a standby instance in a different Availability Zone. Multi-AZ deployments are done with either one standby or two readable standbys.

Amazon RDS is a collection of managed services that makes it simple to setup, operate, and scale databases.

It removes resource-intensive database administrative tasks without requiring you to provision infrastructure or maintain software.

Amazon RDS Multi-AZ ensures high availability and enhances durability.

Amazon RDS offers you two Multi-AZ deployment options.
1. RDS Multi-AZ with one standby enables you to automatically create a primary database instance and synchronously replicate your data onto a secondary instance in a different availability zone. Automating failover without manual intervention.
2. RDS Multi-AZ with two readable standbys lets you deploy your database workload across three availability zones. Both options provide zero data loss. 

The two readable standby option also allows you to create read-only and read-write endpoints for improved performance and scalability.

Compared to one standby, you can achieve up to 2x improved write latency as well as additional read capacity.

One standby offers failover as quick as 60 seconds.

Whereas two readable standbys typically allow you to failover in under 35 seconds.

#### Multi-AZ with one standby
In an Amazon RDS Multi-AZ deployment, Amazon RDS automatically creates a primary database (DB) instance and synchronously replicates the data to an instance in a different Availability Zone. When it detects a failure, Amazon RDS automatically fails over to a standby instance without manual intervention.
1. Create and connect to your Amazon RDS instance.
2. Highly available, durable relational databases deployed across two availability zones.
3. Amazon RDS deploys two database instances in different AZs with 2nd instance in standby.
4. When there is a new write it is sent to an Amazon EBS volume attached to the primary.
5. The write is then written to the standby DB instance.
6. The transaction is acknowledged.
7. The transaction is committed.

#### Multi-AZ with two readable standbys
You can deploy highly available and durable MySQL or PostgreSQL databases in three Availability Zones using Amazon RDS Multi-AZ with two readable standbys. This can provide you with automatic failovers in typically under 35 seconds, up to two times faster transaction commit latency compared to Amazon RDS Multi-AZ with one standby, additional read capacity, and a robust compute instance option. 
1. Connect your Amazon RDS workloads to your writer and reader endpoints.
2. Highly available, durable relational databases deployed across three Availability Zones.
3. Once acknowledged from any reader, it commits the transaction.
4. Logs are first written to SSD storage on the writer.
5. Data is moved asynchronously to Amazon EBS for durability. Serves reads from memory cache or from Amazon EBS back to your reader endpoint.

#### Amazon RDS read replicas
Amazon RDS read replicas provide enhanced performance and durability for Amazon RDS DB instances. They make it easy to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads. You can create one or more replicas of a given source DB instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput. Read replicas can also be promoted when needed to become standalone DB instances. Read replicas are available in Amazon RDS for MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server in addition to Amazon Aurora.

With read replicas, application servers can read and write to the primary server. Asynchronous replication is used to maintain concurrency with the read replica, which can also be used in a read only state by application servers to increase aggregate read throughput.

#### Comparing Multi-AZ deployments and read replicas
Amazon RDS read replicas complement Multi-AZ deployments. Although both features maintain a second copy of your data, there are differences between the two. The following table identifies these differences.

|             | Multi-AZ deployments | Read replicas |
| ----------- | -------------------- | ------------- |
| Purpose | Main purpose is high availability | Main purpose is scalability |
| Replication | Synchronous replication | Asynchronous replication |
| Instance Availability | Only the primary instance is active | All read replicas are accessible and can be used for read scaling |
| Backups | Automated backups are taken from standby | No backups are configured by default |
| Regions and Availability Zones | Always span at least two Availability Zones within a single Region | Can be within an Availability Zone, Cross-AZ, or Cross-Region |
| Upgrades | Database engine version upgrades happen on primary | Database engine version upgrades are independent from source instances |
| Failover/promotion | Failover to standby when a problem is detected | Can be manually promoted to a standalone instance |

When data is written to the primary DB instance, Aurora synchronously replicates the data across Availability Zones to six storage nodes associated with your cluster volume.

#### Amazon RDS backups
You can back up your databases in multiple ways, including using automatic backups and database snapshots.

##### AUTOMATIC BACKUPS
When you create an Amazon RDS database, automatic backups are enabled by default. Amazon RDS will back up the entire database and transaction logs by creating a storage volume snapshot of your DB instance. It is recommended that you schedule the 30-minute backup window to a time when the database has minimum activity to avoid latency issues. You can also configure the backup retention period up to 35 days, which is the number of days that backups are kept. You can restore your DB instance to any specific time during the backup retention period, which creates a new DB instance.

##### DATABASE SNAPSHOTS
You can take manual database snapshots of your database instance if you want to keep your automated backups for longer than 35 days. Snapshots are saved in Amazon Simple Storage Service (Amazon S3) and are available until you delete them.

##### BACKUP RETENTION PERIOD
You can set the backup retention period when you create a database instance. When creating a DB instance using the Amazon RDS API or the command line interface (CLI), the default backup retention period is 1 day. When creating a database using the AWS Management Console, the default backup retention period is 7 days. 

After you create a DB instance, you can modify the backup retention period. You can set the backup retention period to 0–35 days. Setting the backup retention period to 0 disables automated backups.

##### BACKUP STORAGE
Your Amazon RDS backup storage for each AWS Region is composed of the automated backups and manual DB snapshots for that Region. Total backup storage space equals the sum of the storage for all backups in that Region. Moving a DB snapshot to another Region increases the backup storage in the destination Region. Backups are stored in Amazon S3.

#### AWS Backup
You can also use AWS Backup to manage backups of Amazon RDS DB instances. The AWS Backup service provides a centralized backup console that offers backup scheduling, retention management, and backup monitoring. Backups managed by AWS Backup are counted as manual backups.

#### Point-in-time restores
You can restore your DB instance to any specific time during the backup retention period by creating a new DB instance. To restore your DB instance, you can use the AWS Management Console or the CLI.

To determine the latest restorable time for a DB instance, use the AWS Management Console or the CLI to look at the value returned in the LatestRestorableTime field for the DB instance. The latest restorable time for a DB instance is typically within 5 minutes of the current time.  

## Pricing Considerations
Amazon RDS pricing is determined by a number of factors: instance type, storage options, RDS engine, RDS deployments, and data transfers.

### Pricing by instance type
When determining pricing by instance type, AWS divides Amazon RDS instances into two subcategories—on-demand instances and reserved instances.

#### ON-DEMAND INSTANCES
With on-demand instances, you pay for compute capacity per hour your DB instance runs. DB instances are billed based on the class of the DB instance, and there are no long-term commitments.

On-demand instances are ideal for the following:
* Users that prefer low cost and flexibility without any upfront payment or long-term commitment
* Applications with short-term, spiky, or unpredictable workloads that cannot be interrupted
* Applications being developed or tested on RDS for the first time

#### RESERVED INSTANCES
With reserved instances, you can reserve a DB instance for a one-year or three-year term. Reserved instances receive a significant discount compared to on-demand instances. RDS provides three reserved instance payment options—no upfront, partial upfront, all upfront—so you can balance the amount you pay upfront with your effective hourly price.  

Reserved instances are ideal for the following:
* Users with long-term, steady state workloads
* Mission critical applications that run on Multi-AZ database deployments for high availability and data durability

### Cost based on engine type
Amazon RDS provides a selection of instance types optimized to fit different relational database use cases. Specific pricing is available for databases using the following services:
* Amazon Aurora
* Amazon RDS for MySQL
* Amazon RDS for PostgreSQL
* Amazon RDS for MariaDB
* Amazon RDS for Oracle
* Amazon RDS for SQL Server

### Cost based on storage options
The storage options you select will also affect the pricing of your Amazon RDS DB instances. Storage options are divided into two categories—general purpose (SSD) storage and provisioned IOPS (SSD) storage. General purpose storage provides cost-effective storage for most workloads. If your workloads are I/O-intensive, require low I/O latency, and have consistent I/O throughput, then provisioned IOPS storage would likely benefit you.

### Cost based on RDS deployments
You have a number of deployment options for Amazon RDS including on-premises environments using Amazon RDS on AWS Outposts, using Amazon RDS Custom for privileged access to the underlying database environment and operating system for applications like Oracle E-Business Suite, or running Amazon RDS Proxy.

### Data transfer costs
Data transfers can also incur additional costs. For example, data transferred between an Amazon Elastic Compute Cloud (Amazon EC2) instance and Amazon RDS DB instance in different Availability Zones of the same Region have no data transfer charge for traffic in or out of the RDS DB instance. You are only charged for the data transfer in or out of the Amazon EC2 instance and standard EC2 regional data transfer charges apply.

#### [Amazon RDS pricing](ihttps://aws.amazon.com/rds/pricing/)

### Amazon Aurora
Aurora is a MySQL-compatible and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open-source databases.

Aurora is up to **five times** faster than standard MySQL databases and **three times** faster than standard PostgreSQL databases. It provides the security, availability, and reliability of commercial databases at one-tenth the cost. Aurora is fully managed by Amazon RDS, which automates time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.

#### Amazon Aurora Serverless
Amazon Aurora Serverless is an on-demand, autoscaling configuration for Amazon Aurora. It automatically starts up, shuts down, and scales capacity up or down based on your application's needs. You can run your database on AWS without managing database capacity.

Manually managing database capacity can take up valuable time and can lead to inefficient use of database resources. With Aurora Serverless, you create a database, specify the desired database capacity range, and connect your applications. You pay on a per-second basis for the database capacity that you use when the database is active and migrate between standard and serverless configurations with a few steps in the Amazon RDS console.

#### AURORA SERVERLESS V1
Amazon Aurora Serverless v1 is a simple, cost-effective option for infrequent, intermittent, or unpredictable workloads. Benefits using Aurora Serverless v1 include the following:
* **Simple**: Provisioning and managing database capacity are automated.
* **Scalable**: Compute and memory can scale as needed without disrupting connectivity.
* **Cost-effective**: Pay only for resources consumed on a per-second basis. 
* **Highly available**: It is built on the robust architecture of AWS.
Limitations of Aurora Serverless v1 include, but are not limited to the following:
* Support is limited for some features and services.
* Connections to an Aurora Serverless v1 DB cluster are closed automatically if held open for longer than one day.
* You can't export Aurora Serverless v1 snapshots to Amazon S3 buckets.

#### AURORA SERVERLESS V2
Aurora Serverless v2 is an on-demand, autoscaling configuration for Amazon Aurora. Aurora Serverless v2 helps to automate the processes of monitoring the workload and adjusting the capacity for your databases.

This type of automation is especially valuable for multi-tenant databases, distributed databases, development and test systems, and other environments with highly variable and unpredictable workloads. Benefits of Aurora Serverless v2 include the following: 
* *Simple**: It removes the complexity of provisioning and managing database capacity.
* **Scalable**: It scale instantly to hundreds of thousands of transactions in a fraction of a second.
* **Available**: It is supported by the full breadth of Aurora features.
* **Cost-effective**: You can provision and pay only for the resources you need.
* **Transparent**: Database capacity is instantly scalable without disruption.
* **Durable:** It protects against data loss using the distributed, fault-tolerant, self-healing Aurora storage with six-way replication.

AWS recommends the use of Serverless V2 for all new Amazon Aurora deployments.

#### High availability
The Amazon Aurora architecture involves separation of storage and compute. Aurora includes some high availability features that apply to the data in your DB cluster. The data remains safe even if some or all of the DB instances in the cluster become unavailable. Other high availability features apply to the DB instances. These features help to make sure that one or more DB instances are ready to handle database requests from your application.

Aurora stores copies of the data in a DB cluster across multiple Availability Zones in a single AWS Region. Aurora stores these copies regardless of whether the instances in the DB cluster span multiple Availability Zones.

#### Use case: Public source data ingestion architecture
Many applications rely on data from public sources to meet the needs of their users. Suppose your database needs to gather public weather information. For this use, this architecture is one way to accomplish the task. 

##### Public data source
Public data is everywhere. Using it to enhance the abilities of your applications and analysis can be the difference between having a functional app and having one that is a huge success.

In this architecture, data is being gathered from a website containing a public weather data source.

##### Kinesis Data Firehose
Kinesis Data Firehose is a service that can capture, transform, and load streaming data into an S3 bucket. The result is called a data stream.

In this architecture, Kinesis Data Firehose gathers data from the weather website and sends it on to am AWS Lambda function.

##### Lambda
With Lambda you can run code called functions without provisioning or managing servers.

In this architecture, the Lambda function takes the data from the data stream and transforms it into a consistent format before storing it in an S3 bucket.

##### Amazon S3
Amazon S3 is a data repository.

In this architecture, Amazon S3 holds the data gathered by the Lambda function.

##### AWS DMS
AWS Database Migration Service (AWS DMS) migrates data from one source into an AWS database service.

In this architecture, AWS DMS takes the data from the S3 bucket, transforms it, and loads it into an Aurora table within the designated database.

##### Aurora
In this architecture, Aurora can now take the data from the table created by AWS DMS and use it to enrich the other data generated and used by applications accessing the database.

#### Use case: Log analytics architecture
Knowing how your databases are being used and their health is an important part of maintaining well-running systems. Aurora regularly generates logs on activities of users and the database. You can analyze these logs to ensure that users are getting the responses they require, and the database is running optimally. For this use case, this architecture is one option for creating a log analytics system. 

##### Aurora
Aurora is the database system.

In this architecture, users access the database through an application. Logging the activity of the application can help you to determine if it is running properly and meeting the needs of your users.

##### Amazon CloudWatch
CloudWatch is a monitoring and management service that provides you with the data and actionable insights to monitor and understand what is going on in your applications.

In this architecture, CloudWatch gathers the log files containing the activities of users and basic database operations. You can also export these logs to Amazon S3.

##### Amazon OpenSearch Service
Amazon OpenSearch is a fully managed service that helps you securely ingest data from any source and search, analyze, and visualize the data in real time. 

In this architecture, Amazon OpenSearch gathers data from the CloudWatch logs, catalogs it, and makes it available for analysis and visualization.

##### Amazon QuickSight
QuickSight is a fast, cloud-powered business intelligence service that facilitates delivering insights to everyone in your organization.

In this architecture, QuickSight can visualize data contained within Amazon OpenSearch. That data reflects usage of the Aurora database.

##### Amazon S3
An Amazon S3 bucket is a storage location for many types of data.

In this architecture, you can store the log files from CloudWatch indefinitely for future analysis and to meet retention requirements.

##### Athena
Athena is an interactive query service that facilitates analyzing data in Amazon S3 using standard SQL. 

In this architecture, you can use Athena to query the archived log files.

### Knowledge Check
#### What can you implement to isolate your Amazon RDS instance and connect it to your existing IT infrastructure?
You can run your Amazon RDS database in a virtual private cloud to isolate your database instances and connect to your existing IT infrastructure.

The other options are incorrect because of the following: 
* Multi-AZ deployments are used to enhance availability and durability, but they do not specifically provide isolation and connection to existing IT infrastructure.
* Read replicas are used to enhance scalability, but they do not specifically provide isolation and connection to existing IT infrastructure.
* Encryption at rest provides additional data security, but it does not assist with the described task.

#### What are multiple distinct locations within an AWS Region?
Each AWS Region contains multiple distinct locations called Availability Zones.

The other options are incorrect because of the following:
* Edge locations are the areas at the periphery of your network.
* Security groups are used to control the traffic that is allowed to reach and leave AWS resources, they are not distinct locations within an AWS Region.
* Local Zones are extensions of an AWS Region that is geographically close to users.

#### Which Amazon RDS availability measure can be promoted to a standalone instance?
**Read replicas** can be manually promoted when needed to become a standalone DB instance.

The other options are incorrect because of the following:
* Multi-AZ with one standby provides failover to standby when issues are detected.
* Multi-AZ with two readable standbys provides failover to standby when issues are detected.
* Database snapshots are a form of backup that must be restored, not promoted.

### Summary
#### Amazon RDS
Amazon RDS is a fully managed database solution that supports multiple database engines to suit the needs of most relational database use cases. Features and benefits of Amazon RDS include:
* Amazon RDS storage autoscaling
* Highly reliable, highly available infrastructure
* Cost-effective
* Secure

#### AWS Regions, Availability Zones, and Local Zones
Amazon cloud computing resources are housed in highly available data center facilities in different areas of the world. Each data center location is called an AWS Region. Each AWS Region contains multiple distinct locations called Availability Zones that are engineered to be isolated from failures in other Availability Zones. By launching instances in separate Availability Zones, you can protect your applications from the failure of a single location.

DB instances can be run in several Availability Zones, referred to as a Multi-AZ deployment. When using the Multi-AZ option, Amazon automatically provisions and maintains one or more secondary standby DB instances in a different Availability Zone.

Local Zones are extensions of AWS Regions that are geographically close to users. You can extend any VPC from the parent AWS Region into Local Zones.

#### Multi-AZ deployments
Multi-AZ deployments are done with either one standby or two readable standbys. In an Amazon RDS Multi-AZ deployment, Amazon RDS automatically creates a primary database (DB) instance and synchronously replicates the data to an instance in a different AZ. When it detects a failure, Amazon RDS automatically fails over to a standby instance without manual intervention. This is referred to as a Multi-AZ deployment with one standby.

In a Multi-AZ deployment with two readable standbys, a database is deployed in three separate AZs, providing for rapid automatic failovers and faster transaction commit latency. 

#### Read replicas
Amazon RDS read replicas provide enhanced performance and durability for Amazon RDS DB instances. You can create one or more replicas of a given source DB Instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput. Read replicas can also be promoted when needed to become standalone DB instances. 

#### Amazon RDS backups
You can back up your databases in multiple ways, including using automatic backups and database snapshots.

##### AUTOMATIC BACKUPS
Automatic backups are enabled by default when you create an Amazon RDS database. Amazon RDS will back up the entire database and transaction logs by creating a storage volume snapshot of your database instance. Backups can be retained up to 35 days.

##### DATABASE SNAPSHOTS
You can take manual database snapshots of your database instance if you want to keep your automated backups for longer than 35 days. Snapshots are saved in Amazon S3, and are available until you delete them.

#### Amazon RDS pricing
##### On-demand instances
With on-demand instances, you pay for compute capacity per hour your DB instance runs. DB instances are billed based on the class of the DB instance, and there are no long-term commitments. 

##### Reserved instances
With reserved instances, you can reserve a DB instance for a one- or three-year term. Reserved instances receive a significant discount compared to on-demand instances. RDS provides three reserved instance payment options - No Upfront, Partial Upfront, All Upfront - enabling you to balance the amount you pay upfront with your effective hourly price.  

##### Cost based on engine type
Amazon RDS provides a selection of instance types optimized to fit different relational database use cases.

##### Cost based on storage options
The storage options you select will also affect the pricing of your Amazon RDS DB instances. Storage options are divided into two categories – General Purpose (SSD) storage and Provisioned IOPS (SSD) storage.

##### Cost based on RDS deployments
You have a number of deployment options for Amazon RDS including on-premises environments using Amazon RDS on Outposts, using Amazon RDS Custom for privileged access to underlying database for applications like Oracle E-Business Suite, or running Amazon RDS Proxy.

###### Data transfer costs
Data transfers can also incur additional costs. Review the most current Amazon RDS pricing information to learn more about transfer costs.

#### Amazon Aurora
Aurora is a MySQL- and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open-source databases.

##### Amazon Aurora Serverless
Amazon Aurora Serverless is an on-demand, autoscaling configuration for Amazon Aurora. It automatically starts up, shuts down, and scales capacity up or down based on your application's needs, enabling you to run your database without managing database capacity.

### Additional Resources
#### [Amazon RDS](https://aws.amazon.com/rds/)

#### [Amazon RDS developer resources](https://aws.amazon.com/rds/resources/)

#### [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)

#### [AWS Backup](https://aws.amazon.com/backup/)

#### [Amazon Aurora](https://aws.amazon.com/rds/aurora/)

#### [Amazon Aurora resources](https://aws.amazon.com/rds/aurora/resources/)

## Using Amazon RDS
### Using Amazon RDS pre-assessment
#### Which type of database is also called a self-managed database?
**Unmanaged databasesi**, also referred to as self-managed databases, are databases that are run on premises or on virtual machines (VMs) in a cloud environment. 

The other options are incorrect because of the following: 
* General purpose and provisioned are types of database storage.
* Managed databases are managed by a cloud provider, not self-managed.

#### Which of the following are responsibilities of AWS under the shared responsibility model when databases are hosted on Amazon EC2? (Select TWO.)
The correct options are **OS installation**, **server maintenance**, and power, HVAC, network.

The other options are incorrect because scaling and OS patches are customer responsibilities under the shared responsibility model.

#### Which creation method uses best-practice configurations by default when creating an Amazon RDS database?
The correct option is **Easy create**.

The other options are incorrect because of the following:
* With standard create, you set all the configuration options yourself.
* Express create and basic create are not database creation methods.

### Database Management Methods
#### Unmanaged and managed databases
Databases that are hosted in cloud environments commonly fall within two categories. Those two categories, managed databases and unmanaged databases, are very different approaches to database management.

#### Unmanaged databases
Unmanaged databases, also referred to as self-managed databases, are databases that are run on premises or on virtual machines (VMs) in a cloud environment. Users have full control over both the VMs and the related database infrastructure.

For on-premises databases, the customer is responsible for managing all database aspects. This includes managing all security backups, database tuning, and replication. The customer makes all decisions about capacity as well.

##### On-premises databases
For on-premises databases, the customer is responsible for managing all database aspects. This includes managing all security backups, operating system (OS) patches, database tuning, and replication. The customer makes all decisions about capacity.

Customer Responsibility:
* Power, HVAC, network
* Rack and stack
* Server maintenance
* OS installation
* OS patches
* DB software installs
* DB software patches
* DB backups
* High availability
* Scaling
* Application optimization

##### Hosted on Amazon EC2
Unmanaged databases can be deployed in an Amazon Elastic Compute Cloud (Amazon EC2) instance. When databases are hosted on Amazon EC2, AWS is responsible for the physical hardware, while the customer is responsible for all of the database management, including database software installation, patching, backups, availability, and scaling.

##### AWS responsibility:
* Power, HVAC, network
* Rack and stack
* Server maintenance
* OS installation

###### Customer Responsibility:
* OS patches
* DB software installs
* DB software patches
* DB backups
* High availability
* Scaling
* Application optimization

#### Managed databases
A managed database is a cloud computing service in which a cloud service provider is paid to manage the underlying infrastructure. This is accomplished while providing the you with access to the database itself. 

##### AWS managed
AWS purpose-built databases are fully managed. The customer is only responsible for the optimization of the application. AWS is responsible for managing everything else so you can focus on your application.

##### AWS responsibility:
* Power, HVAC, network
* Rack and stack
* Server maintenance
* OS installation
* OS patches
* DB software installs
* DB software patches
* DB backups
* High availability
* Scaling

###### Customer Responsibility:
* Application optimization

### Relational databases on Amazon EC2
Running your relational database on Amazon EC2 instances comes with tradeoffs. The installation, configuration, and management of the EC2 instance, network infrastructure, database software, and more are all your responsibility. Though there is an increased administrative burden for you and your organization, this database option provides you with the most flexibility and control over your database assets. 

#### Tradeoffs if opt for using Amazon EC2 for your relational database rather than Amazon RDS.
|              | Database on Amazon EC2 | Amazon RDS database |
| ------------ | ---------------------- | ------------------- |
| Administration | You have complete control of the installed DB software, including configuration, management, maintenance, and security. | AWS automates management, maintenance, and security of your database. |
| Scalability | You are responsible for configuring your architecture to be scalable. | Amazon RDS uses Amazon scaling tools for vertical and horizontal scaling, both which can be done rapidly. |
| Performance | To monitor your database performance, third-party monitoring tools will be required. | Amazon RDS integrates with Amazon CloudWatch to provide you with insights about the performance of your database. |
| Availability | Configuration for high availability is your responsibility. | High availability is built-in with Amazon RDS. |
| Backups | Backups will need to be manually configured and monitored by you. | Backups with Amazon RDS can be automated and can be monitored using AWS CloudWatch. |

### Getting Started with Amazon RDS
#### The Amazon RDS workflow
Now that you have an understanding of database basics, let's take a look at the Amazon RDS workflow. It starts with establishing your database engine, in this example MySQL. Each database engine has its own unique characteristics and features.

Then you choose the VPC in which to launch the database. Two database subnet groups are required even in single DB instance mode. Next, create the Amazon RDS instance. Then, connect your application to your Amazon RDS database.

Now you can work with and monitor the database to maintain overall performance. Keep this workflow in mind as you go through the Amazon RDS setup.

#### Amazon RDS key decision points
Before setting up a database using Amazon Relational Database Service, or Amazon RDS, there are some key decisions to consider. You need to understand the workload and the DB instance and network needs.

##### Virtual private cloud (VPC)
First, your DB instances will need to run in a virtual private cloud, or VPC, with subnets and a security group. The VPC must have at least two subnets in different Availability Zones. The security group must be configured to allow connections from the applications or services to the DB instance.

##### Type of database engine
The next consideration is the type of database engine you want to run. Each database engine has its own unique characteristics, features, and costs. Choose the engine that best matches your needs and is compatible with the applications that need to use it. 

##### Instance class and storage
Another important consideration is the DB instance class, which consists of both the instance type and size. The class determines the amount of memory, computational capacity, and the maximum bandwidth for storage and network performance. 

##### Database authentication
Finally, you need to choose from three options for database authentication, which determines how you will maintain the user permissions and access to your database. The most common is password authentication, where you create users and passwords in the database. Amazon RDS also provides an option to use AWS Identity and Access Management, or IAM, for database authentication. This uses an authentication token instead of a password. The third type of database authentication uses Kerberos, which is an authentication protocol built into Microsoft Active Directory.

#### Amazon RDS DB creation
To begin, navigate to the Amazon RDS console. Choose Databases, then choose Create database. The first choice is the database creation method. When creating a database in the Amazon RDS console there are two options: standard create and easy create. For this example, we will be using the standard create option to look at the customizable settings before launching the DB instance.

##### Creation method: standard or easy
When you use **standard create** you specify more configuration options, including availability, security, backups, and maintenance.

With **easy create**, you specify only the database **engine type**, **instance size**, and **instance identifier**. Easy create uses the default settings for the other configuration options.

Next, choose the database engine. Amazon RDS supports most relational database engines, including Oracle and Microsoft SQL Server. Open-source engines include PostgreSQL, MySQL, and Amazon Aurora.

##### Engine option

###### Templates
In the templates section, there are three choices—production, dev/test, and free tier.
* Production uses defaults for high availability and fast, consistent performance.
* Dev/Test is intended for development use outside of the production environment.
* Free tier is intended for developing new applications, testing existing applications, or gaining hand-on experience with Amazon RDS.

###### Availability and durability
* Multi-AZ DB cluster
* Multi-AZ DB instance
* Single DB instance

###### Settings
Next, review the Amazon RDS settings. The DB cluster or instance identifier must be unique across all the database clusters or instances that are owned by your AWS account in the Region. Login credentials are required for the primary user. If you are using AWS Secrets Manager, it can be used to manage the Amazon RDS credentials, though some RDS features aren't supported. 

###### Instance configuration
In the Instance configuration section, you will select the database instance class. There are two choices—standard classes and memory optimized classes.
* Standard classes are used for general purpose instances.
* Memory optimized classes are used for memory-intensive applications.

###### Choosing storage for your Amazon RDS database
For data and log storage for most database engines, Amazon Relational Database Service, or Amazon RDS, DB instances use Amazon Elastic Block Store, or Amazon EBS, volumes. Amazon RDS automatically stripes the data across multiple Amazon EBS volumes to optimize performance.

There are three storage types available for use with Amazon RDS: 
* general purpose SSD, 
* provisioned IOPS SSD, 
* and magnetic. 

Each storage type has its own benefits and limitations that you will need to take into consideration. 

###### IOPS
IOPS is a unit of measure representing input/output operations per second for a storage device. If you try to drive more input/output operations to a device than it can handle, the operations get queued, which increases input/output latency.

###### Kibibyte, mebibyte, gibibyte, and tebibyte
The term megabyte represents 1,000,000 bytes, whereas a mebibyte represents 1,048,000 bytes.

##### General purpose SSD storage offers cost-effective storage for Amazon RDS
This storage can be used effectively for a broad range of workloads that aren’t sensitive to latency, such as development and test environments. Amazon RDS offers two types of general purpose SSD storage: gp2 and gp3.

**Gp2 storage** is sufficient when your applications don’t need high storage performance. The baseline I/O performance for gp2 storage is 3 IOPS for each gibibyte of storage volume size, with a minimum of 100 IOPS. Because the IOPS increase with volume size, larger volumes offer better baseline performance. Gp2 volumes that are less than 1 TiB can also burst their performance to 3,000 IOPS for a limited period of time. 

**With gp3 storage**, you can customize storage performance independently of storage capacity. Storage performance refers to the combination of IOPS and storage throughput, which refers to the amount of data being read or written per second. In gp3 volumes, the baseline storage performance is 3,000 IOPS and 125 MiBps of storage throughput, regardless of volume size. When you need more performance, you can provision the IOPS or throughput you need without increasing the storage capacity. 

##### Provisioned IOPS storage
Provisioned IOPS storage is used for I/O-intensive production applications that require fast, predictable, and consistent I/O performance. Provisioned IOPS storage is optimized for online transaction processing, or OLTP, workloads that need consistent performance for the short, rapid transactions they are used for. 

##### Magnetic storage
Magnetic storage is typically used for backward compatibility and is not recommended for any new storage needs. There are several limitations to magnetic storage that are not present with general purpose SSD or provisioned IOPS SSD.


To recap, there are three types of storage provided by Amazon RDS. General purpose SSD volumes provide cost-effective storage that supports a broad range of workloads. Provisioned IOPS storage is use for I/O-intensive database workloads that require consistent low I/O latency. Finally, magnetic storage is used for backward compatibility and is not recommended for new storage needs.

#### Connectivity and Scaling
##### Connectivity
After you have selected the appropriate storage for your Amazon RDS database, you will need to determine the configuration for network access to your DB. Your database must be used within a VPC. The list of existing VPCs will include only those with a corresponding DB subnet group. 

**After the database has been created, it is not possible to change the VPC.**

After you have chosen the VPC you will be using, you will need to select the database subnet group. The database subnet group defines which subnets and IP ranges that the database cluster can use in the selected VPC. Amazon RDS requires two subnets in two different Availability Zones to provide for high availability. 

##### Scaling your RDS instance
After your database has been configured and fully operational, you might find that the needs of your database change over time. Your database can grow in size beyond your initial expectations, or you might find that your database needs additional capability to support reads operations or connections. These are cases where scaling can help you adjust your database to best fit your needs.

###### Vertical scaling
Vertical scaling is the act of adding additional capacity to your database. You can scale your RDS by changing its instance type, which can be used to adjust CPU, memory, storage, and networking capacity. Each instance type includes several sizes for you to scale your database to the requirements of your target workload.

The following lists a few things to consider prior to scaling up your RDS instance:
* Licensing needs to be in place if you are using a commercial database engine such as Oracle.
* Database instance class support varies by database engine and AWS Region.
* Determine whether you want the change to occur immediately, or if you prefer to wait until a planned maintenance window.
* Storage and instance type are not linked. If you find that you have a predictable workload and simply need more storage space or better storage throughput, you can modify your DB instance to simply increase storage or storage performance. These changes will not cause any down time for your database. 
* If your workload is unpredictable, consider managing your storage capacity by enabling Amazon RDS storage autoscaling.

###### [Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling)

###### Horizontal scaling
If you find that scaling your database requirements goes beyond what can be achieved with a single instance, horizontal scaling might be the choice for you. Horizontal scaling involves adding additional instances to support your workload. An advantage of horizontally scaling in Amazon RDS is that AWS handles the infrastructure management, provisioning, and configuration of additional nodes. 

The type of horizontal scaling you need to perform will be based on your workload requirements. If additional performance for read operations is what you need, then read replicas can be used horizontally scale your database. If support for additional connections is what you need, then Amazon RDS Proxy can provide the needed support for hundreds of thousands of connections.

###### [Amazon RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Overview)

###### [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/)

### Knowledge Check
#### A consultant is working with a company that wants to migrate their relational database to the cloud. The company wants to maintain as much control of their database as possible and is willing to conduct the required upkeep.
When databases are **hosted on Amazon EC2**, AWS is responsible for the physical hardware, and the customer is responsible for all the database management, including installation, patching, backups, availability, and scaling.

The other options are incorrect because of the following: 
* A database built using Amazon RDS is managed by AWS.
* Amazon DynamoDB is not a relational database service.
* The company’s requirements can be met by hosting their database on Amazon EC2.

#### A consultant is working with a company interested in migrating their relational database to the AWS Cloud. The company wants to know what responsibility they would have if they chose to host their database on Amazon RDS.
With a database deployment using Amazon RDS, the customer is responsible for **application optimization** under the shared responsibility model.

The other options are incorrect because of the following:
* Database software installation, database software patches, and server maintenance are the responsibility of AWS under the shared responsibility model.

#### A database administrator has discovered that their growing database is nearing the limits of their current storage capacity, but their workload has remained predictable. The database is consistently in use, so avoidance of downtime is preferred.
If you find that you have a predictable workload and simply need more storage space or better storage throughput, you can modify your DB instance to simply **increase storage** or storage performance.

The other options are incorrect because of the following:
* Vertically scaling instance type can modify both storage and performance but can incur downtime.
* Horizontally scaling instances is an unnecessary action when only storage needs to be modified.
* Amazon RDS storage autoscaling is generally only necessary when your workload is unpredictable.

### Summary
#### Unmanaged and managed databases
Databases that are hosted in cloud environments commonly fall within two categories, unmanaged and managed. Unmanaged databases are run on-premises or on VMs in a cloud environment. Users have full control over both the VMs and the related database infrastructure.

When unmanaged databases are run on-premises, the customer is responsible for managing all aspects of the database, up to and including the power, HVAC, and network. Unmanaged databases that are deployed in an Amazon EC2 instance shifts the responsibility of tasks like OS installation, server maintenance, and power to AWS, but the customer is still responsible for the majority of DB management tasks.

Managed databases are services that are managed by a cloud service provider. The cloud service provider manages the underlying infrastructure, while the user or customer is responsible only for the optimization of the DB application.

#### Getting started with Amazon RDS
Before setting up a database using Amazon Relational Database Service, or Amazon RDS, there are some key decisions to consider. 
* DB instances will need to run in a virtual private cloud, or VPC, with subnets and a security group. The VPC must have at least two subnets in different Availability Zones. The security group must be configured to allow connections from the applications or services to the DB instance.
* The type of database engine you want to run; each database engine has its own unique characteristics, features, and costs. Choose the engine that best matches your needs and is compatible with the applications that need to use it. 
* The DB instance class, which consists of both the instance type and size. The class determines the amount of memory, computational capacity, and the maximum bandwidth for storage and network performance.
* Database authentication, which determines how you will maintain the user permissions and access to your database.

#### Scaling
Your database may grow in size beyond your initial expectations or you may find that your database needs additional capability to support reads operations or connections. These are cases where scaling can help you adjust your database to best fit your needs. You can scale your database in two ways, vertically and horizontally.
* Vertical scaling is the act of adding additional capacity to your database. You can scale your RDS by changing its instance type, which can be used to adjust CPU, memory, storage, and networking capacity.
* Horizontal scaling involves adding additional instances to support your workload. The type of horizontal scaling you will need to perform will be based on your workload requirements. 

## Migrating to an Amazon Managed RDS
### Pre-assessment
#### Which type of the following migrates a database from one database engine to another?
The correct option is **Heterogenous**.

The other options are incorrect because of the following: 
* A homogenous database migration is the migration from an on-premises engine to the same engine in the cloud.
* Asynchronous and synchronous are not types of database migrations.

#### What important database component requires conversion first when completing a database migration from one relational database engine type to another relational database engine type?
The correct option is **Schema**.

The other options are incorrect because server OS, database storage, and database memory do not need to go through a specific conversion process.

#### How are the source databases and target databases in database migrations are commonly referred to?
The correct option is **Endpoints**.

The other options are incorrect because of gateways, destination points, and migration points aren’t common elements of the database migration lexicon.

### Migrating Your Database to AWS
### Database migration
Today’s applications come with unique challenges, such as large data volumes, complex data types and business logic, and proprietary vendor features. Migrating these workloads to the cloud is a goal for many AWS customers. Cloud migration can reduce costs by providing easier automation and elasticity while lowering license costs with less vendor lock-in. Migration can also help modernize data infrastructure with cloud-only features like the Amazon Aurora storage engine. 

#### Common reasons to migrate a database
##### Database modernization
Moving data from legacy database engines to modern database engines, enabling business agility to compete in the digital age.

##### Dtabase migration
 Moving data from one platform to another, in the context of enterprise applications.

##### Database replication
Frequently copying data electronically from a database in one computer or server to a database in another to share the same level of information with all users.

#### Benefits of migrating a database with AWS
With the mature technology of relational databases, you can routinely manage high levels of availability with on-premises servers. Although NoSQL databases are newer, we can usually maintain high availability on premises; however, any database downtime can severely impact both application downtime and a company's ability to serve its customers in a timely manner.

AWS database technologies, such as Amazon RDS and Amazon DynamoDB, provide low-cost, scalable, and highly available database solutions that are simple to set up and use. For many companies, migrating their databases to the cloud (particularly if switching to a different engine) would lower downtime and cost compared to on-premises servers.

##### Simple to use
AWS DMS is easy to use. You do not need to install drivers or applications, and it typically does not require changes to the source database.

##### Minimal downtime
AWS DMS helps you migrate your databases to AWS with virtually no downtime.

##### Supports widely used database engines
AWS DMS can migrate your data to and from most widely used commercial and open-source database engines. 

##### Low cost
AWS DMS is a low-cost service. You only pay for the compute resources used during the migration process, any additional log storage, and data transfer if not in the same AWS Region.

##### Fast and easy to set up
You can set up a migration task within minutes in the AWS Management Console to define parameters used by AWS DMS to run the migration.

##### Reliable
AWS DMS is highly resilient and self-healing. It continually monitors source and target databases, network connectivity, and the replication instance.

#### Migrating your database to AWS
AWS DMS and AWS SCT can help you migrate your databases to or from AWS quickly and securely. Using AWS DMS, your source database remains fully operational during migration, minimizing downtime to applications that rely on the database.

You can migrate to the same database engine, known as a homogenous database migration, or switch database engines to modernize your database platform. Switching from one database type to another during migration is called a heterogenous database migration. You can also replicate data to sync source and target databases.

##### For example:
You can migrate from an on-premises Oracle instance to an Amazon RDS for Oracle instance.

A homogenous database migration from an on-premises Oracle database to an Amazon RDS for Oracle database.

##### Or...
You can migrate an Oracle instance, either on premises or in the cloud, to a PostgreSQL database like Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL.

A heterogenous database migration from an on-premises Oracle database to an Amazon Aurora Database. The AWS SCT is first used to convert the existing database schema and prepare it for the transition facilitated by AWS DMS.

### Migration tools
#### AWS DMS
At its most basic level, AWS DMS is a server in the AWS Cloud that runs replication software. You create a source and target connection to tell AWS DMS where to extract from and load to. Then you schedule a task that runs on this server to move your data.

AWS DMS creates the tables and associated primary keys if they don't exist on the target. You can create the target tables manually, if you prefer. Or you can use AWS SCT to create some or all of the target tables, indexes, views, triggers, and so on.

#### AWS SCT (AWS SCT as an AWS DMS task)
If you want to switch database engines, AWS SCT can convert your existing database schema to the target platform. This includes tables, indexes, views, and stored procedures, plus your application code. If the schema from your source database can't be converted automatically, AWS SCT provides guidance about how you can create equivalent schema in your target database engine.

### Managing a migration project
How do AWS DMS and AWS SCT fit into your migration project? Customers typically structure a migration into 12 distinct steps. Not all of the steps apply to every migration project—your particular use case will dictate which steps apply based on characteristics of your application, database, infrastructure, available resources, and skill sets.

### Using AWS DMS to Migrate Data
#### The data migration process
Data migration is the process of moving data records from the source to the target. It is the activity that most people think of when they hear database migration.

Data migration can be challenging if you are dealing with large data volumes and have to keep the source and target systems in sync until you can cut over your applications to the target system.

If your database also contains complex data types like large objects (LOBs) or spatial data, then you will need to consider how best to migrate those data values to the target. Lastly, if you’re changing the type of your target database, then you will have to translate most (if not all) data values to conform to the target system requirements.

#### Reasons to use AWS DMS to migrate
You can use AWS DMS to modernize your database to a cloud-ready, open-source engine, migrate it to the same engine but on the cloud, or replicate it for additional availability.

##### Database modernization 
The movement of data from legacy database engines to modern ones. An enterprise's ability to compete in the digital age rests on business agility.

##### Database migration 
In the context of enterprise applications, moving your data from one platform to another.

##### Database replication 
The ongoing copying of information from one database to another so that both databases share the same level of information.

#### What AWS DMS is
AWS DMS is a cloud service that makes it easy to migrate relational databases, data warehouses, NoSQL databases, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud or between combinations of cloud and on-premises setups. 

#### How AWS DMS works
AWS DMS is a web service that helps you migrate data from a source data store to a target data store, as long as either the source or target databases reside within AWS. These two data stores are called **endpoints**. You can migrate between source and target endpoints that use the same database engine, such as from an on-premises PostgreSQL database to an Amazon RDS for PostgreSQL database.

You can also migrate between source and target endpoints that use different database engines, such as from an Oracle database to a PostgreSQL database. The only **requirement to use AWS DMS** is that **one endpoint is on an AWS service**. **You cannot use AWS DMS to migrate from an on-premises database to another on-premises database**.

AWS DMS will migrate your data records to the same database engine, or you can modernize your database to use a cloud-native or open-source engine. You can use AWS DMS to perform a one-time copy of the source data to the target. You can also use AWS DMS to keep your source and target **syncedi** by migrating ongoing transactions as they occur on the source.

If you are migrating to a new target database, you can continue replicating until you are ready to switch over your applications. If your use case requires ongoing data replication, then you can use AWS DMS to keep a source and target in sync indefinitely.

#### How AWS DMS moves your data
AWS DMS moves your data in one of three ways: 
* full-load migration,
* ongoing replication,
* or a combination of those. 

During a full-load migration, where existing data from the source is moved to the target, AWS DMS loads data from tables on the source data store to tables on the target data store.

AWS DMS also supports ongoing replication, known as **change data capture (CDC)**, which keeps your target in sync with a transactionally active source. AWS DMS can combine these two types of data transfer by using an initial full load, followed by ongoing replication.

#### Monitoring progress
A migration task runs on a replication instance, which is an Amazon EC2 instance that has been configured with the AWS DMS software. The task migrates the data between your source and target endpoints. You can see the progress of the task in the console and review detailed task logs if needed.

#### Verifying migration success
For relational migrations, AWS DMS can validate the migrated data, so you can be confident that the source and target databases match. **Data validation** is **an option** that you can choose to add to your replication task. Data validation tracks the progress of the migration and incrementally validates new data as it is written to the target. 

#### Next steps
Migrating your schema and data are the two most important things for database migration. However, other important steps include testing, switching over your production systems, and documentation.

### Using AWS SCT to Convert Data
#### Assessing migration
Planning is key to the success of any migration process. You need to understand the scope of work required based on your database schema, data volumes, data types, resources, and stakeholders. And you need integrated tools that support the project plan and automate the migration as much as possible.

#### Migrating to another database engine
Different relational database engines have different features, so you can choose the engine to best take advantage of them. Open-source databases are comparable to commercial ones, but offer lower licensing costs, which can motivate you to move.

Changing database technologies, such as going from Oracle to Amazon DynamoDB, can greatly improve performance and cost for some applications.

AWS SCT can assist you in the migration process by cataloging the physical and logical components of the existing system. If you are performing a heterogeneous migration from one database engine to another, AWS SCT will evaluate how much effort is needed to migrate to one or more popular open-source engines. It will provide a detailed report about each engine, and you can choose the best target for your particular use case.

#### Database object conversion
Taking on a heterogenous database migration will require you to convert your database objects from the source engine to the target engine. This includes converting your tables, indexes, constraints, foreign keys, triggers, and stored procedures. It doesn’t include migrating the actual data records in your database.

#### How AWS SCT functions
AWS SCT will convert your source-object definitions to the target engine’s formats. Then, when you’re ready to build the database schema, it will apply them to the target engine.

When you’re performing a heterogeneous migration, your target database might be missing features that are available in your source database. If AWS SCT can’t convert an object, it flags it for manual intervention, along with a color-coded level of effort needed to resolve. Later in this topic, you will see an AWS SCT assessment report for converting an Oracle database to Amazon Aurora with PostgreSQL compatibility.

#### Assessing the complexity of a migration with AWS SCT
The assessment report shows you what AWS SCT 
* can convert automatically,
* which objects need manual remediation,
* and which objects require significant remediation. 

##### Levels of effort are color coded as 
* green,
* gray,
* orange, 
* and red in the summary report.

Simple actions usually require less than an hour, medium actions can be completed in 1–4 hours, and complex actions would typically take over 4 hours. You can use this information to develop level-of-effort estimates across different lines of responsibility like database administrators (DBAs), application developers, test engineers, and business stakeholders.

#### Database storage objects with conversion actions
In the following example assessment report, the task involves converting an Oracle database to an Amazon Aurora PostgreSQL-compatible edition database. The assessment report gives you a quick overview of how many of your database objects have been converted automatically and how many require manual intervention. It also includes an assessment of the difficulty of each manual intervention.

##### Red – significant actions
Red bars represent the number of objects requiring significant manual efforts. Although AWS SCT can help you migrate tables and indexes, and even some stored procedures and triggers, complex stored procedures are not always automated and might require substantial effort.

In this particular example, 1 out of 10 indexes will require significant effort.

##### Gray – simple actions
Gray items are not automatically converted, but the interventions they require are fairly simple. In this example, 2 out of the 19 tables require simple manual intervention.

#### Database code objects with conversion actions
AWS SCT not only helps you convert tables and indexes: it can also assist you in converting code objects such as stored procedures and functions, database packages, and views and triggers. AWS SCT will translate code written in the native language of the source database into equivalent code in the target database language.

For example, AWS SCT will convert an Oracle stored procedure written in PL/SQL into an equivalent PL/pgSQL procedure for a PostgreSQL target. If AWS SCT detects any issues that require manual intervention, it will highlight the offending code that needs attention.

##### Convert code
AWS SCT will help you convert not just the tables, but also code objects like triggers and stored procedures.

For any objects that can't be converted, it will show you the level of effort you need to apply to migrate these objects.

##### Gray items
Gray items require simple actions. In this example, 17 percent (1 out of 6) of stored procedures would need to be somewhat modified.

##### Orange items
Orange items require medium complexity actions. In this example, half of the functions require these kinds of actions.

#### Detailed recommendations
AWS SCT will also provide you with a detailed list of migration objects that require manual intervention. The details will include which features are not supported by your target database and recommendations about how to translate. You can also export a version of this report as a spreadsheet, so you can track which tasks are complete.

##### Item details
The detailed report contains useful details for any item. It includes a numeric code (for easy searching), pointers to reference materials, and recommended actions.

##### Estimated complexity
For each item, you see an estimated complexity. This roughly indicates the level of effort required.

##### See for yourself: [a sample assessment report in AWS SCT](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1715558400/mt2jKlqz8cV1BOSBT__Bhg/tincan/914789_1711995597_o_1hqde6qcm4i41nma1gfnqa2ohmb_zip/assets/sampleReport.pdf) 

#### AWS SCT report
AWS SCT also provides a granular view of the report to use as a remediation checklist. Responsible developers, DBAs, and others can use this view to verify that corrective action has been taken on cited objects and that remediation is complete.

### Getting help with heterogenous database migrations
Sometimes, you will find that a feature in your source database does not have an exact match in the target database that AWS SCT can translate to. In these cases, you will need to recode the objects using design patterns based on the target engine’s capabilities.

To help with this process, AWS provides migration playbooks that contain design patterns for the most popular source and target combinations. For example, the Oracle to Aurora PostgreSQL migration playbook is 317 pages and contains information about 60 design patterns that are fully, partially, or not supported by the target.

The Database Migration Playbooks are a series of guides focused on best practices for creating successful blueprints for heterogeneous database migration. The playbooks complement existing automated and semiautomated database migration solutions and tools from Amazon, including AWS SCT and AWS DMS.

* AWS Schema Conversion Tool (object migration)
* AWS Database Migration Service (data migration)
* Database Migration Playbook (reference guide)

### Knowledge Check
#### Which database types can be migrated to Amazon RDS without schema conversion using AWS Database Migration Service (AWS DMS)? (Select THREE.)
The correct options are 
* **relational databases**, 
* **data warehouses**, 
* and **NoSQL databases**.

The AWS Database Migration Service can be used to migrate structured databases such as relational databases, data warehouses, and NoSQL databases.

The other options are incorrect because of the following: 
* Nonrelational databases require schema conversion to migrate to Amazon RDS.
* Microsoft SQL databases require schema conversion to migrate to Amazon RDS.
* Data lakes are object storage and cannot be migrated to Amazon RDS.

#### A consultant is working with a customer that is preparing a hybrid cloud environment. The customer is using AWS Database Migration Service (AWS DMS) to migrate their relational database to Amazon RDS. The customer is impressed with the capabilities of AWS DMS and asks if it is possible to use it to migrate their existing on-premises relational database to one of their newer on-premises virtual machines.
The correct option is **AWS DMS can only migrate databases where either the source or target resides in AWS**.

The other options are incorrect because AWS DMS can only migrate databases where either the source or target resides in AWS; it cannot migrate data between two on-premises databases.

#### What is the purpose of an AWS Database Migration Playbook?
The correct option is **Providing design patterns for the most popular heterogenous migration combinations**.

AWS provides migration playbooks that contain design patterns for the most popular source and target combinations.

### Summary
#### Migrating your database to AWS
Cloud migration can reduce costs by providing easier automation and elasticity while lowering license costs with less vendor lock-in. Migration can also help modernize data infrastructure with cloud-only features like the Amazon Aurora storage engine. Some common reasons to migrate a database to the cloud are:
* Database modernization
* Database migration from one platform to another
* Database replication

AWS provides several tools to enable you in your database migration. Using AWS Database Migration Service, you can perform homogenous database migrations while keeping your source database fully operational. This minimizes your overall downtime for applications that may rely on the database.

The AWS Schema Conversion Tool can assist you in conducting heterogenous database migrations. Heterogenous migrations require a conversion of the database schema, which can be accomplished using AWS SCT. 

## Assessment
### What process is used in OLTP databases to reduce data redundancy and improve overall data integrity?
**Normalization**.

The other options are incorrect because of the following:
* Atomicity is an ACID compliance measure that ensures transactions either completely succeed pr completely fail.
* Soft state is a BASE compliance component, not a process used by OLTP databases.
* Isolation is an ACID compliance measure that ensures that one transaction cannot interfere with another concurrent transaction.

### What type of data follows a predefined relational data model, and is typically stored in a relational database?
**Structured** data is most commonly stored in relational databases.

The other options are incorrect because of the following:
* Unstructured data is typically stored in non-relational databases.
* Semi-structured data is typically stored in non-relational databases.
* Meta-tagged data is a form of semi-structured data, which is typically stored in non-relational databases.

### What trade-off is made when a database is BASE compliant?
**Consistency is traded for availability**.
BASE compliance is used in a structured or semi-structured database. Data changes are made immediately available, and are eventually consistent. This means replicas may return different results until replication is completed.

The other options are incorrect because of the following:
* Security is never sacrified.
* Consistency is sacrified for availability. Reliability is not traded off.
* Availability is prioritized in a BASE-compliant database.

### A gaming company needs a database that support microsecond response times for the leaderboard for their very popular online game. What yupe of database will meet the requirements?
**In-memory**.

In-memory databases are ideal for applications that require miscosecond response times or have large spikes in traffic, such as gaming leaderboards, session stores, and real-time analytucs. Data resides in-memory, rather than on disks.

The other options are incorrect because they store data on disks, and because of the following:
* A document database is optimized for querying data in JSON-like docyments.
* Wide-column databases are mainly used for analytical and query-intensive environments, which do not require miscosecond response times.
* Time series databases are typically used for measuring changes over time, not for real-time analytics.

### A manufacturing company needs to analyze historical sales data to plan for the production and distribution of their products over the next year. The company sells through multiple channels, and needs to combine large sets of structured and semistructured data for the analysis. What AWS database service provides a fully managed environment for querying the data across multiple sources?
**Amazon Redshift** is a fully managed warehouse environment that uses SQL to analyze structured and semi-structured data across data warehouses. operational databases, and data lakes.

The other options are incorrect because of the following:
* Amazon Neptune, Amazon DynamoDB, and Amazon Timestream are non-relational database services, not data warehouse services.

#### When configuring an Amazon RDS database instance, what elements are determined by the instance class selection? (Select TWO.)
The instance class determines the amount of memory, computational capacity, and maximum bandwidth for storage and network performance. For production databases, memory optimized instances are typically recommended.

The other options are incorrect because of the following:
* Authentication type is not determined by instance class.
* The database engine may influence the decision on the instance class, but it is not determined by the instance class.
* Storage type is separately configured and determined by the storage class.
