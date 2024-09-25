
```
UTC-7:00 (Local): September 04, 2024, 18:12:00 UTC-7:00
Region (Oregon): September 04, 2024, 17:12:00 UTC-8:00

dbinstance-backup.c5gs02ku8aqr.us-west-2.rds.amazonaws.com

sudo sed -i 's/<DBEndpoint>/<dbinstance-backup-Endpoint>/g' /var/www/inc/dbinfo.inc

sudo sed -i 's/labstack-ac55160b-ccd2-4313-95a6-33d826-dbinstance-1dxzltrnfjyq.c5gs02ku8aqr.us-west-2.rds.amazonaws.com/dbinstance-backup.c5gs02ku8aqr.us-west-2.rds.amazonaws.com/g' /var/www/inc/dbinfo.inc
```

Restoring an Amazon RDS DB instance
© 2024 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

Note: Do not include any personal, identifying, or confidential information into the lab environment. Information entered may be visible to others.

Corrections, feedback, or other questions? Contact us at AWS Training and Certification.

Lab Overview
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity for databases in the cloud. Hosting a database on Amazon EC2 allows for a high degree of customization and control over the database and its environment. Amazon EC2 facilitates manual database management including managing replication, failover, monitoring, notifications, and backups. Amazon Web Services (AWS) managed database solutions, such as Amazon Relational Database Service (Amazon RDS), provide fully automated solutions for all these tasks.

Amazon RDS allows you to configure synchronous replication with just a few clicks. In the event of a failure, Amazon RDS automatically fails over to a secondary server in 60-120 seconds. Using a DNS endpoint prevents any complicated routing, IP reassignment, or DNS propagation delays. Understanding how an automatic failover affects your applications is vital to successful implementation of this service.

Automated Backups: Turned on by default, the automated backup feature of Amazon RDS enables point-in-time recovery for your DB Instance. Amazon RDS will backup your database and transaction logs and store both for a user-specified retention period. This allows you to restore your DB Instance to any second during your retention period, up to the last five minutes. Your automatic backup retention period can be configured to up to thirty five day

Objectives
By the end of this lab, you will be able to do the following:

Connect to a precreated Amazon RDS for MySQL instance.
Delete a precreated database from the RDS for MySQL instance.
Recover an RDS for MySQL instance from an automated backup using the restore-in-time feature.
Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Additional information: Where to find more information.
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
 File contents: A code block that displays the contents of a script or file you need to run that has been pre-created for you.
 Knowledge check: An opportunity to check your knowledge and test what you have learned.
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Security: An opportunity to incorporate security best practices.
 Refresh: A time when you might need to refresh a web browser page or list to show new information.
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal.
 Hint: A hint to a question or challenge.
 Answer: An answer to a question or challenge.
 Group effort: A time when you must work together with another student to complete a task.
Lab environment
An Amazon EC2 instance has been provisioned for use in this lab. This instance will also act as a WebServer which hosts a simple database application. The EC2 instance is configured to communicate with the database instance located in a private subnet via port 3306. The initialization of an RDS DB instance can take a while. For this reason, a pre-configured RDS for MySQL instance has been created. This will allow you to continue with the lab without having to wait.

'Architecture diagram'

Image description: The preceding diagram depicts the data flow from an external user to an internet gateway, to a web server in a public subnet, to a database server in a separate private subnet.

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
Task 1: Test the pre-created Web-application
In this task, you get to test a simple pre-created Web-application.

Copy the WebsiteURL value from the list to the left of these instructions, and then paste it into a new web browser tab.

 Below is the expected output:

'Web application page'

Image description: The preceding diagram depicts the web application page. It consists of a table with two columns – Name and Address – which can be used to create a record.

In the web-page, you can now enter any name and address of an individual to create a list of record. For example, you can enter the following details to create a record.

Name: Aws and Address: Seattle
After you enter Name and Address detail, click on Add Data to add each entry.

 Note: Do not close this tab as you will be using it in the upcoming tasks.

Task 2: Connect to your RDS for instance
In this task, you connect to your RDS for MySQL database instance. This instance was created for you using CloudFormation when you started the lab.

Copy the InstanceSessionURL value from the list to the left of these instructions, and then paste it into a new web browser tab.

 Copy edit: Copy the following code into a text editor and replace the <DBEndpoint> placeholder value with the value of your RDS DB instance endpoint (DBEndpoint) that you see to the left of these instructions.


mysql -h <DBEndpoint> -P 3306 -u dbadmin -p
 The new command should look similar to this:


mysql -h labstack-jaysinp-uhwcccq4irp42fswqzw-auroracluster-ivg0sneibtts.cluster-cc6lhhxxp5pj.us-west-2.rds.amazonaws.com -P 3306 -u dbadmin -p
Paste the updated command from the text editor into the command line. Press Enter to run the code.

 Command: When prompted for a password, enter lab-password

 Note: The entered password will not be visible.

 Expected output:


Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 22
Server version: 8.0.35 Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]>
Now you are logged in to the MySQL console. You should see the mysql> prompt.

 Command: Enter the following query to observe all the databases present in the RDS for MySQL instance.


SHOW DATABASES;
 Copy and paste will sometimes result in command errors. If a command does not work, try manually typing it in the prompt.

 Expected output:


+--------------------+
| Database           |
+--------------------+
| addressdb          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
 Command: Enter the following query to delete addressdb database which stores the data for the web-application you tested in previous task.


DROP DATABASE addressdb;
 Copy and paste will sometimes result in command errors. If a command does not work, try manually typing it in the prompt.

 Expected output:


Query OK, 1 row affected (0.01 sec)
As the database is now deleted, go to the browser tab which has the web-application running and refresh this page.

 Expected output:

'Web application page broken'

Image description: The preceding diagram depicts the web-application page has been broken resulting in two errors, “Error creating table.” and “Error adding employee data"

 Command: Return to the EC2 InstanceSessionURL browser tab and enter the following to exit out of the database.


exit;
 Expected output:


Bye
sh-4.2$
 Congratulations! You have now successfully connected to your RDS for MySQL instance and deleted a database.

Task 3: Using Automated backup to restore RDS for MySQL database
In this task, you restore your RDS for MySQL database instance using the restore-in-time feature. This will help you recover the broken web-application.

At the top of the AWS Management Console, in the search bar, search for and choose RDS.

In the left navigation pane, choose Automated backups.

In the list of Current Region backups, choose the DB instance or cluster with dbinstance in the name. This redirects you to the summary page.

In the summary page, note the Earliest restorable time & Latest restorable time

 Note: The Earliest restorable time specifies how far back within the backup retention period that you can restore your cluster volume. The Latest restorable time for a DB cluster is the most recent point at which you can restore your DB cluster, typically within 5 minutes of the current time.

In the Backups & restore section, choose the Earliest restorable time. Keep the date and hour unchanged and round the minute value up to the next integer. For example, June 8, 17:51:08 would be rounded up to June 8, 17:52:00.

 Copy edit: Copy and paste this rounded up time to a local text editor as it will be used to restore your database in the upcoming steps.

 Consider: In a production environment, ideally you would restore database to the latest time and date just before the database was corrupted. The automated backups are taken every 5 minutes, so there will be a list of backups available to choose from.

Choose Actions and select Restore to point in time. This redirects you to configuration page.

Configure the backup database using the following settings:

Restore time: Choose Custom date and time.

The chosen date and time must be after Earliest restorable time and before the Latest restorable time for the DB instance. To restore your database, use the date and time you rounded up in the earlier step 17.
 Note: Times are shown in your local time zone, which is indicated by an offset from Coordinated Universal Time (UTC). For example, UTC-5 is Eastern Standard Time/Central Daylight Time.

Settings

DB instance identifier: Enter dbinstance-backup
Availability and durability: Choose Single DB instance

Scroll down, Choose  Additional configuration, and configure:

Database options
Initial database name: Enter addressdb
 Note: This is the same database which we deleted in the earlier task.
Keep all the other configurations to default and Choose Restore to point in time

 Note: You are taken to the Amazon RDS console. Here you can monitor the progress of your new database instances. The new Amazon RDS instance takes about 10-15 minutes to create.

After about 10-15 minutes, choose refresh  button to review the status of the database. Move to the next task once the status is shown as Available

 Additional information: While you wait for the database to become available, you can read through Amazon RDS Backup for more details.

When the database is available to use, choose dbinstance-backup. This will re-direct you to the Summary page.

 Copy edit: In the Connectivity & security section,  copy the Endpoint value to your local text editor.

Return to the EC2 InstanceSessionURL browser tab. If the session is timed out, refresh the page.

 Copy edit: Copy the following command into your text editor.


sudo sed -i 's/<DBEndpoint>/<dbinstance-backup-Endpoint>/g' /var/www/inc/dbinfo.inc
Replace <DBEndpoint> with the value of your RDS DB instance endpoint that you can see to the left of these instructions. Replace <dbinstance-backup-Endpoint> with the value of your RDS dbinstance-backup endpoint that you saved to a text editor in the previous step.

You have now successfully updated the database endpoint.
To replace the database endpoint in a configuration file dbinfo.inc, paste the updated command into the command line and press Enter, thereby pointing to the newly created database.

Return to the WebsiteURL browser tab and refresh the page. You can observe now that the web application has been restored to the original state and the error message encountered earlier has been fixed.

 Congratulations! You have successfully restored database from an earlier backup which was automatically created by the RDS service, thereby restoring the web-application to normal state.

Conclusion
 Congratulations! You now have successfully:

Connected to a pre-created RDS for MySQL instance.
Deleted a pre-created database from RDS for MySQL instance.
Recovered an RDS for MySQL instance from an Automated backup using the restore-in-time feature.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
For more information about how to use Amazon RDS, see Amazon RDS User Guide.
For more information about how to use Amazon RDS, see Amazon RDS for MySQL
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.