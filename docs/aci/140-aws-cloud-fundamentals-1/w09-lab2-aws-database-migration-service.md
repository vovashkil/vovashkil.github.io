Introduction to AWS DMS
SPL-PW-100-CLF132-1 - Version 1.0.2

© 2024 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

Note: Do not include any personal, identifying, or confidential information into the lab environment. Information entered may be visible to others.

Corrections, feedback, or other questions? Contact us at AWS Training and Certification.

Lab overview
This lab provides you with a basic understanding of AWS Database Migration Service (AWS DMS). In this lab you migrate data from a MySQL database running on an Amazon Elastic Compute Cloud (Amazon EC2) instance to an Aurora DBDB instance.

Objectives
By the end of this lab, you will be able to do the following:

Connect to a pre-created Aurora DB instance.
Migrate data from your MySQL server to your Aurora DB instance.
Verify that your migration was successful.
Duration
This lab will require 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run.
 Note: A hint, tip, or important guidance.
 Additional information: Where to find more information.
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
AWS Database Migration Service
AWS Database Migration Service helps you migrate databases to AWS easily and securely. With AWS Database Migration Service, the source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. The AWS Database Migration Service can migrate your data to and from the most widely used commercial and open-source databases. The service supports homogenous migrations such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle to Amazon Aurora or Microsoft SQL Server to MySQL.

Amazon Aurora
Amazon Aurora is a fully managed, MySQL-compatible relational database engine that combines the speed and availability of high-end commercial databases with the simplicity and cost-effectiveness of open source databases. Amazon Aurora provides up to five times better performance than MySQL with the security, availability, and reliability of a commercial database at one tenth the cost.

Amazon Elastic Compute Cloud (Amazon EC2)
Amazon EC2 is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.

Amazon RDS
Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, freeing you up to focus on your applications and business. Amazon RDS provides you with six familiar database engines to choose from, including Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL and MariaDB.

Start lab
To launch the lab, at the top of the page, choose Start lab.
 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console.
You are automatically signed in to the AWS Management Console in a new web browser tab.

 WARNING: Do not change the Region unless instructed.

Common sign-in errors
Error: You must first sign out


If you see the message, You must first log out before logging into a different AWS account:

Choose the click here link.
Close your Amazon Web Services Sign In web browser tab and return to your initial lab page.
Choose Open Console again.
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Task 1: Connect to your Aurora DB instance
In this task, you connect to your Aurora DB instance. This instance was created for you using CloudFormation when you started the lab. Aurora will be used as your target for migration.

Copy the CommandHostSessionUrl value from the list to the left of these instructions, and then paste it into a new web browser tab.

 Copy edit: Copy the following code into a text editor and replace <ClusterEndpoint> with the value of your ClusterEndpoint that you see to the left of these instructions.


mysql -h <ClusterEndpoint> -P 3306 -u admin -p
 Command: In the command line for Session Manager, a capability of AWS Systems Manager, paste the updated command from the text editor. Press Enter to run the code.
 The copied value should look similar to this:


mysql -h labstack-jaysinp-uhwcccq4irp42fswqzw-auroracluster-ivg0sneibtts.cluster-cc6lhhxxp5pj.us-west-2.rds.amazonaws.com -P 3306 -u admin -p
 Command: When prompted for a password, enter admin123
 Note: the entered password will not be visible.

 Expected output:


Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 57
Server version: 5.7.12 MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]>
Now you are logged in to the MySQL console. You should see the mysql> prompt.

 Command: Enter the following query to verify that no data exists in your Aurora instance.

Select * from menu.Products;
 Copy and paste will sometimes result in command errors. If a command does not work, try manually typing it in the prompt.

 You should receive a message showing that menu.Products does not exist.

 Expected output:


ERROR 1049 (42000): Unknown database 'menu'
 Note: The above error shows that the database called menu does not exist in Aurora Database instance.

 Congratulations! You have now successfully connected to your Aurora database.

Task 2: Migrate your source MySQL database to your Aurora instance using AWS Database Migration Service
In this task, you use the AWS Database Migration Service to migrate your mydb database running on your MySQL instance to your Aurora instance.

Task 2.1: Create your replication subnet group
At the top of the AWS Management Console, in the search bar, search for and choose Database Migration Service.

In the left navigation pane, choose Subnet groups.

Choose Create subnet group and then configure:

Name: replicationsubnetgroup
Description: Subnet group for DMS instance
VPC: Lab-VPC.
Add subnets: Select each Private subnet.
Choose Create subnet group .
Task 2.2: Create your replication instance
The first step in migrating data using AWS Database Migration Service is to create a replication instance. An AWS DMS replication instance runs on an Amazon EC2 instance. A replication instance provides high availability and failover support using a Multi-AZ deployment.

AWS DMS uses a replication instance that connects to the source data store, reads the source data, and formats the data for consumption by the target data store. A replication instance also loads the data into the target data store. Most of this processing happens in memory; however, large transactions might require some buffering on a disk. Cached transactions and log files are also written to a disk.

In the left navigation pane, choose Replication instances.

Choose Create replication instance and then configure:

Name: Enter replicationInstance.
Description: Enter replicationInstance.
Instance class: Choose dms.t3.micro.
High Availability: Choose Dev or test workload (Single-AZ).
Virtual private cloud (VPC) for IPv4: Choose Lab-VPC.
Replication subnet group: replicationsubnetgroup
Public accessible: Clear the check box.
Choose Create replication instance .

Wait for the status of your replication instance to display Available.

This will take 5-10 minutes.

Task 2.3: Create your source endpoint
An endpoint provides connection, data store type, and location information about your data store. AWS Database Migration Service uses this information to connect to a data store and migrate data from a source endpoint to a target endpoint. You can specify additional connection attributes for an endpoint by using extra connection attributes. These attributes can control logging, file size, and other parameters; for more information about extra connection attributes, see the documentation section for your data store.

In the left navigation pane, choose Endpoints.

Choose Create endpoint and then configure:

 Source endpoint
Endpoint identifier: MySQL
Source engine: MariaDB
Access to endpoint database:  Provide access information manually
Server name: Paste the value of EC2PrivateIP located to the left of these instructions
Port: 3306
User name: dbuser
Password: admin123
Expand  Test endpoint connection (optional), then configure:
VPC: Lab-VPC
Choose Run test
 You may have to wait a few minutes for your replication instance to become active.

Once your test is successful, choose Create endpoint .
Task 2.4: Create your target endpoint to your Aurora instance
At the top of the screen, choose Create endpoint and then configure:
Select  Target endpoint
Check  Select RDS DB instance
For RDS Instance, select the RDS DB instance that appears.
In the Endpoint configuration section, configure:
Endpoint identifier: aurora
Access to endpoint database:  Provide access information manually
User name: admin
Password: admin123
Expand  Test endpoint connection, then configure:
VPC: Lab-VPC
Choose Run test
Once your test is successful, choose Create endpoint .
Task 2.5: Create a database migration task
An AWS Database Migration Service (AWS DMS) task is where all the work happens. You use tasks to migrate data from the source endpoint to the target endpoint, and the task processing is done on the replication instance. You specify what tables and schemas to use for your migration and any special processing, such as logging requirements, control table data, and error handling.

In the left navigation pane, choose Database migration tasks.

Choose Create task and then configure:

Task identifier: MySQL-Aurora
Replication instance: Select your replication instance
Source database endpoint: mysql
Target database endpoint: aurora
Migration type: Migrate existing data
Under Table mappings, choose Add new selection rule and then configure:
Schema: Enter a schema
Source name: menu
 Table mapping uses several types of rules to specify the data source, source schema, data, and any transformations that should occur during the task. You can use table mapping to specify individual tables in a database to migrate and the schema to use for the migration. In addition, you can use filters to specify what data from a given table column you want replicated and you can use transformations to modify the data written to the target database.

In Premigration assessment section, uncheck the Turn on premigration assessment box.

Choose Create task .

Wait for the Status of your task to change from Creating to  Load complete.

Choose the link for your mysql-aurora task.

Choose the Table statistics tab.

 This shows the table statistics for your database migration task. You should see that table Products has a value of 3 for Total rows.

Return to the EC2 SessionManager browser tab. If the session is timed out, refresh the page.

 Command: In the System Manager session command line, paste the updated command that you saved in the text editor in task 1 into the command line and press Enter to run the code.

 The copied value should look similar to this:


mysql -h labstack-jaysinp-uhwcccq4irp42fswqzw-auroracluster-ivg0sneibtts.cluster-cc6lhhxxp5pj.us-west-2.rds.amazonaws.com -P 3306 -u admin -p
 Command: When prompted for a password, enter admin123
 Note: the entered password will not be visible.

 Command: Enter the following query to verify that the database now exists in your Aurora instance.

Select * from menu.Products;
 Copy and paste will sometimes result in command errors. If a command does not work, try manually typing it in the prompt.

 You will see that your menu database has been migrated to your Aurora instance.

 Expected output:


+-----------+---------------+--------------+
| ProductId | ProductFlavor | ProductPrice |
+-----------+---------------+--------------+
|         1 | Vanilla       |         4.99 |
|         2 | Chocolate     |         4.99 |
|         3 | Strawberry    |         4.99 |
+-----------+---------------+--------------+
3 rows in set (0.000 sec)
 Congratulations! You have now successfully used the AWS Database Migration Service to migrate data from your source MySQL server to your target Aurora instance.

End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Conclusion
 Congratulations! You have now successfully:

Connected to a pre-created Aurora DBinstance
Migrated data from your MySQL server to your Aurora instance
Verified that your migration was successful
Additional Resources
AWS Database Migration Service Documentation
Working with AWS DMS Tasks
Working with an AWS DMS replication instance
Using table mapping to specify task settings
Connect using Remote Desktop
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

