# Deploying a Web App on AWS Elastic Beanstalk

## Lab overview

In the previous few labs in this course, you built a web application hosted on the Django web framework for AnyCompany bicycle parts. You installed and configured Django, defined Django models, views, and templates, and you configured the Django administration console for your web application.

You start this lab with that same solution, where the web application is hosted on the AWS Cloud9 instance that you used to configure it. The database backend used by the web application is an installation of MySQL. It resides on the same Amazon Elastic Compute Cloud (Amazon EC2) instance with the AWS Cloud9 integrated development environment (IDE) running on it. The graphics files (JPEG and PNG) used in the web application are hosted locally on the AWS Cloud9 instance.

In this lab, you update how the web application is hosted so that it runs on an architecture that is more scalable and resilient than running it on a single EC2 instance. You migrate the application to run on AWS Elastic Beanstalk, which provides many benefits, including scalability, monitoring, and versioning. You migrate the Django data storage to Amazon Relational Database Service (Amazon RDS). You also migrate the web application graphics to be hosted on Amazon Simple Storage Service (Amazon S3). This improves the reliability and availability of your data.

Objectives
By the end of this lab, you should be able to do the following:

Create an S3 bucket with cross-origin resource sharing (CORS) configured.
Use the AWS Command Line Interface (AWS CLI) to upload objects to an S3 bucket.
Configure Django to use Amazon S3 as a storage location.
Configure an Amazon RDS database to support a Django application.
Configure Django to use Amazon Relational Database Service (Amazon RDS) for MySQL.
Install the Elastic Beanstalk command line interface (CLI) and configure a Django application for deployment.
Use the Elastic Beanstalk CLI to create an environment and an application.
Update the Django application source and deploy the update to Elastic Beanstalk.
Roll back an Elastic Beanstalk application update.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: Additional information or elaboration on a point.
 Task complete: A conclusion or summary point in the lab.
 Tip: A shortcut or recommended best practice.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
Prerequisites
 Caution: This lab requires the use of Chrome internet browser. Using a different browser may prevent viewing the web application website.

Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Lab environment
The following diagram depicts the basic architecture of the lab environment. The resources depicted in the diagram already exist in your Amazon Web Services (AWS) account when you start the lab.

AWS Architecture diagram showing the initial state of the lab environment

Image description: The diagram illustrates that a website developer is working in an AWS Cloud environment using an AWS Cloud9 IDE that has the Django web framework installed. It runs a web application and hosts a MySQL database and graphics. This IDE runs in a public subnet of a virtual private cloud (VPC). The AWS account also includes a private subnet with an Amazon RDS instance running inside a DBSecurityGroup. For more information, refer to the following detailed diagram overview.

Detailed diagram description
The following is a description of the components and how they’re connected:

AWS Cloud: The overall environment is encapsulated in the AWS Cloud, which is the broader context where all the components reside.

Lab VPC: In the AWS Cloud, there is a virtual private cloud (VPC) designated as Lab VPC. This is like a virtual network in the AWS environment that is isolated from other virtual networks.

Public subnet: Inside the Lab VPC, there’s a public subnet. This subnet is accessible from the internet. A subnet is a range of IP addresses in the VPC.

Security group: In the public subnet, there’s a security group. It acts as a virtual firewall controlling the traffic to the EC2 instance.

EC2 instance: Inside the security group, there’s an EC2 instance. This is a virtual server in AWS where applications can run. The EC2 instance is depicted with the EC2 instance group icon. Inside this instance, two key components are mentioned:

AWS Cloud9 IDE: This is an IDE provided by AWS. In this diagram, it’s part of the EC2 instance. This indicates that the AWS Cloud9 IDE is being used for development directly in the EC2 instance.

Ubuntu guest operating system: This indicates that the EC2 instance is running the Ubuntu guest operating system.

You (website developer): On the left side of the diagram, there’s an icon of a person with the label You (website developer). This symbolizes the developer who interacts with the AWS Cloud9 IDE.

By the end of the lab, you configure the architecture depicted in this diagram.

end of lab account architecture

Image description: The diagram illustrates how everything that existed in the account at the start of the lab is still there. However, there is also an Elastic Beanstalk environment running in the public subnet. The application hosts an Elastic Beanstalk environment that has a single EC2 instance running in it. The EC2 instance hosts the Django web application code. The application communicates with the Amazon RDS instance that hosts the Django application data and a new S3 bucket that hosts the graphics files. For more information, refer to the following detailed diagram overview.

Detailed diagram description
The following is a description of the components and how they’re connected:

A rectangle represents the Lab VPC, which is a virtual network dedicated to your AWS account. In this virtual private cloud (VPC), there are two distinct sections.

The left side of the VPC is labeled Public subnet. There’s an outline of the Elastic Beanstalk app, indicating that it’s publicly accessible. Inside this app, there is a nested structure as follows:

At the core of the Elastic Beanstalk app, there is an Amazon EC2 instance, which is a virtual server in the AWS Cloud.

The EC2 instance has Django framework installed and Django web application code, implying that the server is set up to run a Django web application.

There is layer around the EC2 instance called DBSecurityGroup. It acts as a firewall governing access to the EC2 instance.

Next, there’s an Elastic Beanstalk environment layer, indicating that the Elastic Beanstalk application is deployed on the EC2 instance.

On the right, there is a Private subnet. Inside it, there’s another rectangle labeled DBSecurityGroup. It is similar to the one in the public subnet, indicating this is also a firewall-controlled area. Inside the DBSecurityGroup, there is an Amazon RDS for MySQL instance with application data, which is a managed relational database service that holds the application data.

There’s a line connecting the Elastic Beanstalk environment and the Amazon RDS for MySQL instance. The line represents the network communication that is allowed between the EC2 instance and the MySQL database. It is regulated by the security groups.

Additionally, outside the VPC, there are the following three elements:

To the left of the AWS Cloud, there’s an icon representing You (web application developer) with an arrow pointing to the AWS Cloud9 service. This indicates that you, as the developer, use AWS Cloud9, a cloud-based IDE, to interact with AWS services.

Outside the AWS Cloud and below the Lab VPC, there’s a representation of Web application users. This indicates that users from the internet interact with your web application.

In the bottom right of the AWS Cloud, there’s an S3 bucket with graphics files. This indicates that the web application uses a separate storage service (Amazon S3) to store and serve graphics files.

Lines connecting the elements indicate the flow of interaction and communication between the developer, AWS Cloud9 IDE, the web application environment, the database, and end users. The overall layout conveys a typical web application architecture with separate environments for customer-facing application components and private data storage with specific security measures in place.

AWS services used in this lab
The following AWS services are used in this lab:

AWS Cloud9
Amazon EC2
Elastic Beanstalk
Amazon RDS
Amazon S3
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Run the script to configure the development environment
In this task, you run a script that installs the Django framework on your Linux instance. You complete other steps, so your environment matches the end state of the previous lab.

Task 1.1: Connect to the IDE and run the setup script
Start by running a script, starting the web server, and adding product data to the database.

To open the AWS Cloud9 environment, copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab.

It connects you to the AWS Cloud9 IDE.

 Command: In the AWS Cloud9 IDE terminal window, run the following command:


./setup.sh
Analysis: The shell script completes configurations on the EC2 instance where your AWS Cloud9 IDE is installed. The configuration replicates the steps you completed in the previous labs. It installs a Python virtual environment and Django. It also creates the bicycle_project Django project and the bicycle_app Django app.

 Important: If you receive a prompt asking which services to restart, press Tab to navigate to OK, and then press Enter so the script continues to run.

 Expected output: The following output is truncated:


************************
**** EXAMPLE OUTPUT ****
************************
...
restore bicycles database
delete product table contents
reset auto_increment on product table
create the django user
 Command: To activate the Python virtual environment and start the Django web server, run the following commands:


cd ~/environment/django
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8080
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 15, 2024 - 17:08:52
Django version 5.0.1, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
 Important: The web server remains running only while you keep the process active in the terminal. Leave this terminal as it is. Debug and log information is written to this terminal’s output as you progress through the lab.

To add product data to the product table, open a second terminal window in AWS Cloud9.

 Command: In the new terminal, run the following command:


cd ~/environment/django
source .venv/bin/activate
python manage.py loaddata /home/ubuntu/environment/products.json
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Installed 12 object(s) from 1 fixture(s)
(.venv)
Task 1.2: Confirm the application is running
Confirm that your Django environment matches the environment you achieved by the end of the previous lab.

Return to the terminal where the runserver process is running, and then choose the link in the Cloud9 Help dialog box in the bottom-right corner.

 Important: To navigate to the preview page at any time, choose Preview, and then choose Preview Running Application. In the preview panel, choose the pop-out icon to open the preview in a new browser tab.

Completed website screen capture

Image description: The image depicts the Products page of the AnyCompany bicycle parts website. It contains a form with a list of 12 bicycle products, including descriptions, prices, and quantities, and a Submit button.

The lab environment now matches the environment you created at the end of the previous lab.

Optionally, test submitting an order. Review the order history and the order details to confirm the functionality of the site. You can also optionally test logging in to the Django administration site. To access the site, add /admin/ to the end of the base amazonaws.com URL. Try logging in as ProductManager1 with the password Manager2024! or admin with the password djangoSecret764.

Keep this browser tab open because you return to it later.

 Task complete: In this task, you successfully ran a script to install the Django framework on your Linux instance. You also updated database entries, so your lab environment matches the end state of the previous lab.

Task 2: Migrate the product images to Amazon S3
In this task, you migrate the images in the product listings on the website to be hosted in an S3 bucket. You then configure the Django web application to securely retrieve the images from the bucket.

Task 2.1: Create an S3 bucket with CORS configured
Create a bucket where you store the static images, and then configure cross-origin resource sharing (CORS) on it.

Navigate to the Amazon S3 console.

Choose Create bucket.

On the Create bucket page, configure the following:

For AWS Region, choose US West (Oregon) us-west-2.

For Bucket type, choose General purpose.

For Bucket name, enter bicycle-project-us-west-2-ACCOUNT_ID, and replace ACCOUNT_ID with AccountID value listed to the left of these instructions.

Leave all other default settings, and then choose Create bucket at the bottom of the page.

The following Amazon S3 status message appears: Successfully created bucket bicycle-project-us-west-2-ACCOUNT_ID.

Choose the link for the bicycle-project-us-west-2-ACCOUNT_ID bucket you just created.

In the Permissions tab, scroll to the Cross-origin resource sharing (CORS) section, and then choose Edit.

Copy the following JSON, and paste it into the editor:


[
 {
   "AllowedOrigins": ["http://*.elasticbeanstalk.com", "http://127.0.0. 1", "http://localhost"],
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
    "MaxAgeSeconds": 9000,
    "ExposeHeaders": ["x-amz-server-side-encryption"]
 }
]
Choose Save changes .

 Analysis: With CORS, a web application loaded in one domain can communicate with resources stored in another domain. By configuring CORS, your application can load the image files that are hosted in the S3 bucket.

When your application is hosted on the elasticbeanstalk.com domain later in this lab, the http://.elasticbeanstalk.com* entry allows the graphics stored on Amazon S3 to be loaded. Currently, your application is running on AWS Cloud9, which is perceived as a localhost, or 127.0.0.1, domain from the perspective of the preview application functionality.

 Refer to Using Cross-Origin Resource Sharing (CORS) in the Additional resources section for more information.

In the Properties tab of the S3 bucket, the bucket implements server-side encryption with Amazon S3 managed keys (SSE-S3), which is the default encryption configuration for S3 buckets. The CORS configuration also exposes this in the headers.

 Refer to Common Response Headers in the Additional resources section for more information.

Task 2.2: Upload files to the bucket
Add the images needed for the AnyCompany bicycle parts web application to the bucket.

Navigate to the AWS Cloud9 IDE, and then open the second terminal window.

 Command: To copy the files to the bucket, run the following command:


aws s3 cp /home/ubuntu/environment/django/bicycle_app/static s3://bicycle-project-us-west-2-ACCOUNT_ID --recursive --include "*.jpeg"
 Note: Replace ACCOUNT_ID with your account ID so the bucket name in the command matches your bucket name.

 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

upload: bicycle_app/static/css/main.css to s3://bicycle-project-us-west-2-111111111111/css/main.css
upload: bicycle_app/static/logo-white.png to s3://bicycle-project-us-west-2-111111111111/logo-white.png
upload: bicycle_app/static/bell.jpeg to s3://bicycle-project-us-west-2-111111111111/bell.jpeg
upload: bicycle_app/static/brake-disk.jpeg to s3://bicycle-project-us-west-2-111111111111/brake-disk.jpeg
upload: bicycle_app/static/chain.jpeg to s3://bicycle-project-us-west-2-111111111111/chain.jpeg
upload: bicycle_app/static/crank-arm.jpeg to s3://bicycle-project-us-west-2-111111111111/crank-arm.jpeg
upload: bicycle_app/static/cassette.jpeg to s3://bicycle-project-us-west-2-111111111111/cassette.jpeg
upload: bicycle_app/static/inner-tube.jpeg to s3://bicycle-project-us-west-2-111111111111/inner-tube.jpeg
upload: bicycle_app/static/map.jpeg to s3://bicycle-project-us-west-2-111111111111/map.jpeg
upload: bicycle_app/static/logo-black.png to s3://bicycle-project-us-west-2-111111111111/logo-black.png
upload: bicycle_app/static/rear-light.jpeg to s3://bicycle-project-us-west-2-111111111111/rear-light.jpeg
upload: bicycle_app/static/pedals.jpeg to s3://bicycle-project-us-west-2-111111111111/pedals.jpeg
upload: bicycle_app/static/specialist.png to s3://bicycle-project-us-west-2-111111111111/specialist.png
upload: bicycle_app/static/hydraulic-brake.jpeg to s3://bicycle-project-us-west-2-111111111111/hydraulic-brake.jpeg
upload: bicycle_app/static/biking-outdoors.jpeg to s3://bicycle-project-us-west-2-111111111111/biking-outdoors.jpeg
upload: bicycle_app/static/sports-glasses.jpeg to s3://bicycle-project-us-west-2-111111111111/sports-glasses.jpeg
upload: bicycle_app/static/seat.jpeg to s3://bicycle-project-us-west-2-111111111111/seat.jpeg
upload: bicycle_app/static/gear-shifter.jpeg to s3://bicycle-project-us-west-2-111111111111/gear-shifter.jpeg
upload: bicycle_app/static/wheel.jpeg to s3://bicycle-project-us-west-2-111111111111/wheel.jpeg
upload: bicycle_app/static/repair.jpeg to s3://bicycle-project-us-west-2-111111111111/repair.jpeg
In the Amazon S3 console, choose the Objects tab on the bucket page.

To refresh the listing, choose the refresh icon .

The images for your web application are listed.

Task 2.3: Configure Django to use Amazon S3
Install additional software and configure the Django project to use Amazon S3.

Navigate to the AWS Cloud9 IDE, and then open the second terminal window.

Verify that you are in the django directory and that the prompt starts with .venv, indicating that your virtual environment is active.

 Command: To install the additional software that is needed, run the following commands:


pip install --upgrade pip
pip install "pyyaml<5.4"
pip install django-storages boto3
pip list --local
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

Package           Version
----------------- -------
asgiref           3.7.2
boto3             1.34.38
botocore          1.34.38
cffi              1.16.0
cryptography      42.0.1
Django            5.0.1
django-storages   1.14.2
jmespath          1.0.1
pillow            10.2.0
pip               24.0
pycparser         2.21
PyMySQL           1.1.0
python-dateutil   2.8.2
PyYAML            5.3.1
s3transfer        0.10.0
setuptools        59.6.0
six               1.16.0
sqlparse          0.4.4
typing_extensions 4.9.0
urllib3           2.0.7
 Analysis: The django-storages library provides Django a way to connect to Amazon S3 and other storage backends. Boto3 is the AWS SDK for Python (Boto3). The pip list command generates a list of all the software installed in the Python environment, such as this list of expected output.

 Note: You might notice different software versions in your list.

In the file editor, open bicycle_project/settings.py, and then make the following updates:

Under from pathlib import Path, enter the following line:


import os
At the end of the INSTALLED_APPS list, enter the following line:


'storages',
Under STATIC_URL = ‘static/’, enter the following line:


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
At the end of the file, enter the following lines:


AWS_STORAGE_BUCKET_NAME = 'bicycle-project-us-west-2-ACCOUNT_ID'
AWS_S3_REGION_NAME = 'us-west-2'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
 Important: Replace ACCOUNT_ID with your account ID so the bucket name matches your bucket name.

Save the changes.

Verify that no errors display in the runserver terminal output.

 Command: Return to the second terminal window, and run the following command:


python manage.py collectstatic
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

146 static files copied to '/home/ubuntu/environment/django/static'.
(.venv)
When the command runs, it creates a new static directory in the django directory.

 Analysis: The new static directory contains copies of the files in the bicycle_app/static directory and static files used by the Django administration console. If you had more than one application in your Django project, static files to support those additional applications would be collected as well. Collecting the static files into a single directory is useful for deploying Django to Elastic Beanstalk later in this lab.

In the file editor, open bicycle_app/templates/products.html, and then locate the following line:


<img src="static/{{ i.image_url.url }}" width="100" />
Remove static/ from the source as follows:


<img src="{{ i.image_url.url }}" width="100" />
Save the change.

Task 2.4: Confirm Django web application access to S3 objects
Confirm that the web application still displays the product graphics even though the location of the graphics moved from AWS Cloud9 to Amazon S3.

Refresh the main AnyCompany bicycle parts webpage with the products table that you opened previously.

The product images should still display correctly.

To observe the page source of the website, open the context menu for the website, and then choose View page source.

Locate the table element that is contained in the form element. Notice that the source of the images is now the S3 bucket. The image elements are in the format <img src=“https://bicycle-project-us-west-2-ACCOUNT_ID.s3.amazonaws.com/…”.

 Analysis: The images are now pulled from Amazon S3 when the page loads. Notice how each image source includes a Signature and x-amz-security-token with an expiration timestamp. This provides a layer of security so that not just anyone or any website can load these images. To test this layer of security, return to the Amazon S3 console. Choose the link for one of the objects, and then choose the link for the Object URL. You receive an *Access Denied error because your request does not include the security token.

 Task complete: In this task, you successfully uploaded the product images to Amazon S3 and configured the Django web application to securely retrieve the images from the S3 bucket.

Task 3: Update Django to use Amazon RDS
In this task, you configure Django to use Amazon RDS for MySQL to store model data instead of the MySQL database running on the AWS Cloud9 instance.

Task 3.1: Analyze the Amazon RDS database created for you
Start by analyzing the Amazon RDS database instance that was created previously for you.

Navigate to the Amazon RDS console, and in the left navigation pane, choose Databases.

Choose the link for the django-db database instance.

Analyze the following database details:

In the Summary section, notice that the instance uses the MySQL Community engine.

In the Connectivity & security tab, locate Endpoint. This is how MySQL clients can connect to the database over the network.

 Note: The endpoint in the Amazon RDS console is the same as the RDSEndpoint value listed to the left of these instructions.

The database uses port 3306, which is the standard MySQL TCP port.

The database is running in one of the private subnets in the Lab VPC. This is the same VPC where your AWS Cloud9 instance runs in a public subnet.

 Tip: This is not a multi-AZ deployment. However, Amazon RDS requires you to specify at least two subnets when the instance in launched so you can convert the deployment to multi-AZ later if needed.

The database is using a VPC security group named DBSecurityGroup.
Task 3.2: Configure the Amazon RDS security group
Configure the Amazon RDS security group to allow connections from the AWS Cloud9 instance and from the security group used to host the Django deployment on Elastic Beanstalk.

Choose the link for DBSecurityGroup (sg-…).

In the Security group ID column, choose the link for the security group.

In the Inbound rules section, choose Edit inbound rules .

Choose Add rule.

Configure the following:

For Type, choose MYSQL/Aurora.
For Port range, enter 3306.
For Source, choose Custom.
In the search box to the right of Source, enter sg-, and then choose the existing aws-cloud-9… security group.
Choose Add rule, and then configure the following:

For Type, choose MYSQL/Aurora.
For Port range, enter 3306.
For Source, choose Custom.
In the search box to the right of Source, enter sg-, and then choose the existing ebSecurityGroup… security group.
Choose Save rules.

The following message appears at the top of the page: Inbound security group rules successfully modified on security group….

 Note: The first rule allows the AWS Cloud9 instance to communicate with the Amazon RDS database. The second rule allows EC2 instances managed by Elastic Beanstalk, which you configure later in this lab, to also communicate with the database.

Task 3.3: Access Amazon RDS from the AWS Cloud9 instance
Establish an MySQL client connection from the AWS Cloud9 instance to the Amazon RDS database.

Navigate to the AWS Cloud9 IDE, and then open the second terminal.

 Command: To install Nmap, enter the following command:


sudo apt install -y nmap
 Expected output: The following output is truncated.


******************************
**** This is OUTPUT ONLY. ****
******************************

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
    libblas3 liblinear4 lua-lpeg nmap-common
Suggested packages:
    liblinear-tools liblinear-dev ncat ndiff zenmap
The following NEW packages will be installed:
    libblas3 liblinear4 lua-lpeg nmap nmap-common
0 upgraded, 5 newly installed, 0 to remove and 7 not upgraded.
...
No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.

Broadcast message from root@ip-10-0-1-14 (Thu 2024-02-15 18:50:01 UTC):

The system shutdown has been cancelled
(.venv)
 Note: Nmap is a commonly used utility that can tell you if the ports of remote servers are accessible over the network.

 Command: To test if port 3306 of the Amazon RDS database is accessible from the AWS Cloud9 instance, run the following command:


nmap -Pn RDS_ENDPOINT
 Note: Replace RDS_ENDPOINT with the RDSEndpoint value listed to the left of these instructions.

 Expected output: Notice that the port is accessible.


************************
**** EXAMPLE OUTPUT ****
************************

Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-15 18:54 UTC
Nmap scan report for django-db.csxchc99am0m.us-west-2.rds.amazonaws.com (10.0.3.206)
Host is up (0.00087s latency).
rDNS record for 10.0.3.206: ip-10-0-3-206.us-west-2.compute.internal
Not shown: 999 filtered ports
PORT     STATE SERVICE
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 4.25 seconds
(.venv)
 Command: To connect the Amazon RDS database, enter the following command:


mysql -h RDS_ENDPOINT -P 3306 -u root -p
 Note: Replace RDS_ENDPOINT with the RDSEndpoint value listed to the left of these instructions.

When prompted for a password, enter the DBPassword value listed to the left of these instructions.

 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 50
Server version: 8.0.35 Source distribution

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input     statement.

mysql>
Task 3.4: Configure the Amazon RDS database
Analyze the current configuration in Amazon RDS, and then create a Django user in the database.

 Command: To discover which databases and tables exist in the bicycles database, run the following SQL queries:


show databases;
use bicycles; 
show tables;
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

+--------------------+
| Database           |
+--------------------+
| bicycles           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use bicycles; 
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql>
The bicycles database exists, but there are currently no tables in it.

 Command: To create the Django user, grant the Django user permission on the bicycles database, and then exit the SQL client, run the following commands:


CREATE USER 'django'@'%' IDENTIFIED BY 'djangoAciDb2034';
GRANT ALL PRIVILEGES ON bicycles.* To 'django'@'%';
exit;
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

mysql> CREATE USER 'django'@'%' IDENTIFIED BY 'djangoAciDb2034';
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON bicycles.* To 'django'@'%';
Query OK, 0 rows affected (0.01 sec)

mysql> exit;
Bye
(.venv)
Task 3.5: Configure Django to use Amazon RDS
Configure Django to use the Amazon RDS database instance that you configured to support your web application.

In the file editor, open bicycle_project/settings.py.

To update the database settings to point to the Amazon RDS database instead of the local MySQL database, do the following:

Update the HOST line so that it points to the RDS_ENDPOINT.

Add an OPTIONS section. Setting the sql_mode is highly recommended and helps to avoid a warning later when you run the migrate command.

 Refer to Django documentation in the Additional resources section for more information.

The database settings should be as follows:


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bicycles',
            'USER': 'django',
            'PASSWORD': 'djangoAciDb2034',
            'HOST':'RDS_ENDPOINT',
            'PORT':'3306',
            'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
       }
    }
 Important: Replace RDS_ENDPOINT so that it matches your RDS database endpoint

Save the changes.

In the AWS Cloud9 IDE, open the second terminal window where you exited the SQL client.

 Command: To run the migration and load data into the database, run the following commands:


cd ~/environment/django
python manage.py migrate
 Expected output: The output should indicate success.


************************
**** EXAMPLE OUTPUT ****
************************
...
Applying auth.0012_alter_user_first_name_max_length... OK
Applying bicycle_app.0001_initial... OK
Applying sessions.0001_initial... OK'
 Note: You can ignore the WARNINGS messages in the output.

 Command: To load the product data and some test data for orders into the Amazon RDS database tables, run the following command:


python manage.py loaddata /home/ubuntu/environment/products.json
python manage.py loaddata /home/ubuntu/environment/orders.json
python manage.py loaddata /home/ubuntu/environment/order_details.json
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Installed 12 object(s) from 1 fixture(s)
Installed 1 object(s) from 1 fixture(s)
Installed 2 object(s) from 1 fixture(s)
(.venv)
 Command: To create the Django administrator login in the Amazon RDS database, run the following command:


python manage.py createsuperuser
When prompted, enter the same values you used to create this user in MySQL on the AWS Cloud9 instance as follows:

For Username, enter admin.
For Email address, press Enter.
For Password, enter djangoSecret764.
For Password (again), enter djangoSecret764.
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Username (leave blank to use 'ubuntu'): admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
 Command: To create the Product Managers group and ProductManager1 user, run the following command:


python manage.py shell
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
 Command: After connecting to the shell, run the following commands:


from django.contrib.auth.models import User
user = User.objects.create_user("ProductManager1", "", "Manager2024!")
user.is_staff=True 
user.save()

from django.contrib.auth.models import Group
group = Group.objects.create(name = 'Product Managers')
user.groups.add(group)  

from django.contrib.auth.models import Permission
id = Permission.objects.filter(codename="change_product").values()[0] ['id']
group.permissions.add(id)
id = Permission.objects.filter(codename="delete_product").values()[0] ['id']
group.permissions.add(id)
id = Permission.objects.filter(codename="view_product").values()[0]['id']
group.permissions.add(id)
id = Permission.objects.filter(codename="add_product").values()[0]['id']
group.permissions.add(id)
group.save()
exit()
 Note: The commands recreate the settings you configured in the previous lab. Specifically, they create a ProductManager1 user and a Product Managers group. They also add the user to the group and assign permissions to manage the orders table to members of the Product Managers group.

 Expected output: There is no expected output unless there is an error.

Task 3.6: Confirm Django web application access to Amazon RDS data
Complete the task by turning off the MySQL database running on the AWS Cloud9 instance. Confirm that the web application still functions after it is connected to the Amazon RDS database.

 Command: To turn off the MySQL server service on Ubuntu, run the following command:


sudo service mysql stop
 Expected output: There is no expected output unless there is an error.

 Note: Although turning off the local MySQL database is not necessary, it acts as a proof point that Django is no longer using it.

To confirm the web application still displays orders and order details, go to the website and do the following:

Choose Order history.

The test order that was defined in orders.json and loaded into the Amazon RDS database displays.

Choose the link for Order details.

The order details display.

You know this data comes from Amazon RDS because you configured Django to use Amazon RDS in the settings.py file. You also stopped the local MySQL service, so the previously used database is not available.

Optionally, to confirm the web application is functioning as expected, place additional orders using the website.

Open the Django administration UI by loading the AWS Cloud9 Preview URL (which is in the format https://...vfs.cloud9.us-west-2.amazonaws.com) and adding /admin to the end of it.

To open the Django administration UI, load the AWS Cloud9 preview URL, which is in the format https://…vfs.cloud9.us-west-2.amazonaws.com, and add /admin to the end of it.

Enter the credentials you defined as follows:

Username: ProductManager1

Password: Manager2024!

You should successfully log in. The screen displays that you only have access to the Products model data, which is expected when you log in as this user.

Choose LOG OUT.

 Task complete: In this task, you successfully configured Django to use Amazon RDS for MySQL as the database backend.

Task 4: Deploy to Elastic Beanstalk
In this task, you migrate the Django hosting environment from the AWS Cloud9 instance to run on Elastic Beanstalk. You test the functionality of the site, observe how the deployment is configured, and deploy an update to the application.

Task 4.1: Install and configure the software needed to package the Django application
Install an HTTP server and capture a listing of software that Elastic Beanstalk needs to install.

In the AWS Cloud9 IDE, open the second terminal window where the runserver process is not running.

Confirm that your terminal prompt starts with (.venv) and that you are in the django directory.

 Command: To install Python HTTP software, run the following command:


pip install gunicorn
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Collecting gunicorn
  Downloading gunicorn-21.2.0-py3-none-any.whl.metadata (4.1 kB)
Collecting packaging (from gunicorn)
  Downloading packaging-23.2-py3-none-any.whl.metadata (3.2 kB)
Downloading gunicorn-21.2.0-py3-none-any.whl (80 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.2/80.2 kB 3.0 MB/s eta 0:00:00
Downloading packaging-23.2-py3-none-any.whl (53 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.0/53.0 kB 6.1 MB/s eta 0:00:00
Installing collected packages: packaging, gunicorn
Successfully installed gunicorn-21.2.0 packaging-23.2
(.venv)
 Note: Gunicorn is a Python Web Server Gateway Interface (WSGI) HTTP server that can host Django applications. In the AWS Cloud9 IDE, you use the built-in preview feature. However, when you migrate your Django application to Elastic Beanstalk, it needs to run on a WSGI HTTP server.

 Refer to Gunicorn in the Additional resources section for more information.

 Command: To create a requirements.txt file for Elastic Beanstalk, run the following command:


pip freeze > /home/ubuntu/environment/django/requirements.txt
 Expected output: There is no expected output unless there is an error.

 Command: To list the contents of the file that was created, run the following command:


cat requirements.txt
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************
asgiref==3.7.2
boto3==1.34.38
botocore==1.34.38
cffi==1.16.0
cryptography==42.0.1
Django==5.0.1
django-storages==1.14.2
gunicorn==21.2.0
jmespath==1.0.1
packaging==23.2
pillow==10.2.0
pycparser==2.21
PyMySQL==1.1.0
python-dateutil==2.8.2
PyYAML==5.3.1
s3transfer==0.10.0
six==1.16.0
sqlparse==0.4.4
typing_extensions==4.9.0
urllib3==2.0.7
 Analysis: The pip freeze command lists all the packages that are installed in your Python virtual environment. By piping the output of the command to a file, you have a resource that lists the software Elastic Beanstalk needs to install on the EC2 instances where it deploys the Django application.

Task 4.2: Configure settings and install the Elastic Beanstalk CLI
Configure the settings Elastic Beanstalk needs, and then install the Elastic Beanstalk CLI.

In the AWS Cloud9 file editor, open django/bicycle_project/settings.py.

Add http://*.elasticbeanstalk.com as an allowed origin in the existing CSRF_TRUSTED_ORIGINS list.

The line should now be as follows:


CSRF_TRUSTED_ORIGINS = ['https://*.amazonaws.com', 'http://127.0.0.1', 'http://localhost', 'http://*.elasticbeanstalk.com']
Save the changes.

 Command: To create a new directory with an empty file in it, in the terminal window, run the following command:


mkdir /home/ubuntu/environment/django/.ebextensions
touch /home/ubuntu/environment/django/.ebextensions/django.config
 Expected output: There is no expected output unless there is an error.

In the AWS Cloud9 file browser, choose the settings icon in the top-right corner of the left navigation pane, and then choose Show Hidden Files.

Expand the django/.ebextensions directory contents, and then open django.config in the file editor.

Copy the following code, and then paste it into the file:


    option_settings:
    aws:elasticbeanstalk:container:python:
        WSGIPath: bicycle_project.wsgi:application
    aws:elasticbeanstalk:environment:proxy:staticfiles:
        /static: static
    aws:autoscaling:launchconfiguration:
        DisableIMDSv1: true
 Analysis: The WSGIPath value specifies the location of the WSGI script that Elastic Beanstalk uses to start your bicycle_app application. Notice that the configuration indicates the location of the static files to Elastic Beanstalk.

Save the changes.

 Command: To install the Elastic Beanstalk CLI into your Python virtual environment, run the following command in the terminal window:


pip install awsebcli
 Note: If an error message related to the version of botocore appears in the output, ignore it. The error message is followed by a success message.

 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************
...
Installing collected packages: wcwidth, termcolor, cement, urllib3, semantic-version, pathspec, idna, colorama, charset-normalizer, certifi, blessed, requests, botocore, awsebcli
Attempting uninstall: urllib3
  Found existing installation: urllib3 2.0.7
  Uninstalling urllib3-2.0.7:
    Successfully uninstalled urllib3-2.0.7
Attempting uninstall: botocore
  Found existing installation: botocore 1.34.43
  Uninstalling botocore-1.34.43:
    Successfully uninstalled botocore-1.34.43
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
boto3 1.34.43 requires botocore<1.35.0,>=1.34.43, but you have botocore 1.31.85 which is incompatible.
s3transfer 0.10.0 requires botocore<2.0a.0,>=1.33.2, but you have botocore 1.31.85 which is incompatible.
Successfully installed awsebcli-3.20.10 blessed-1.20.0 botocore-1.31.85 cement-2.8.2 certifi-2024.2.2 charset-normalizer-3.3.2 colorama-0.4.3 idna-3.6 pathspec-0.10.1 requests-2.31.0 semantic-version-2.8.5 termcolor-1.1.0 urllib3-1.26.18 wcwidth-0.1.9
(.venv)
Task 4.3: Initialize the Elastic Beanstalk environment and application
Initialize the Django configuration as an Elastic Beanstalk application that is ready to be deployed.

 Command: To initialize your repository, use the following eb init command:


eb init --region us-west-2 --platform python-3.11 bicycle-project-ebapp
The following message should appear: Application bicycle-project-ebapp has been created.

 Note: In the file browser, notice that a new directory named .elasticbeanstalk was created in the django directory.

 Command: To create an .ebignore file with a line in it so that Elastic Beanstalk does not include your Python virtual environment in the deployment environment, run the following command:


touch .ebignore
echo ".venv" >> .ebignore
 Expected output: There is no expected output unless there is an error.

Task 4.4: Create the Elastic Beanstalk environment
Run the command to create the Elastic Beanstalk environment and deploy the bicycle app as an Elastic Beanstalk application in that environment.

Set values for the needed variables in your terminal session.

 Command: To set the VPC ID, enter the following command:


vpcId="VPC_ID"
 Note: Replace VPC_ID with the VpcId value listed to the left of these instructions.

 Expected output: There is no expected output unless there is an error.

To set the subnet ID, enter the following command:


subnetId="SUBNET_ID"
 Note: Replace SUBNET_ID the PublicSubnetId value listed to the left of these instructions.

 Expected output: There is no expected output unless there is an error.

 Command: To set the ID for the security group that Elastic Beanstalk should use, enter the following command:


ebSecGroupId="SG_ID"
 Note: Replace SG_ID the EbSgId listed to the left of these instructions.

 Expected output: There is no expected output unless there is an error.

 Command: To confirm the variable values are set properly, run the following command:


echo "vpcId= "$vpcId
echo "subnetId= "$subnetId
echo "ebSecGroupId= "$ebSecGroupId
 Expected output: The output from each command should indicate that the values are set properly.

 Command: To create an Elastic Beanstalk environment and deploy an application to it, run the following eb create Elastic Beanstalk CLI command:


eb create bicycle-project-env --single --instance_type t3.micro --instance_profile ebInstanceProfile --service-role ebInstanceRole --vpc.id $vpcId --vpc.ec2subnets $subnetId --vpc.securitygroups $ebSecGroupId --region us-west-2
 Note: The command specifies to create a single EC2 instance of type t3.micro. The command also references an AWS Identity and Access Management (IAM) instance profile named ebInstanceProfile. It contains an IAM role named ebInstanceRole that has the permissions needed to deploy the Elastic Beanstalk application. These resources were previously created for you in the AWS account. The command also uses the three variables that you set in your terminal session to specify the VPC, subnet, and security group. They are used to deploy the EC2 instance that runs the Django application.

The output of the command should indicate success.

 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Creating application version archive "app-240220_220818619859".
Uploading: [##################################################] 100% Done...
Environment details for: bicycle-project-env
  Application name: bicycle-project-ebapp
  Region: us-west-2
  Deployed Version: app-240220_220818619859
  Environment ID: e-pdztiyhesk
  Platform: arn:aws:elasticbeanstalk:us-west-2::platform/Python 3.11 running on 64bit Amazon Linux 2023/4.0.8
  Tier: WebServer-Standard-1.0
  CNAME: UNKNOWN
  Updated: 2024-02-20 22:08:29.163000+00:00
Printing Status:
2024-02-20 22:08:28    INFO    createEnvironment is starting.
2024-02-20 22:08:29    INFO    Using elasticbeanstalk-us-west-2-111111111111 as Amazon S3 storage bucket for environment data.
2024-02-20 22:08:57    INFO    Created security group named: sg-058bd9df6a7217a32
2024-02-20 22:09:13    INFO    Created EIP: 44.226.110.136
2024-02-20 22:09:44    INFO    Waiting for EC2 instances to launch. This may take a few minutes.
2024-02-20 22:10:41    INFO    Instance deployment successfully generated a 'Procfile'.
2024-02-20 22:10:46    INFO    Instance deployment completed successfully.
2024-02-20 22:11:00    INFO    Application available at bicycle-project-env.eba-xi98atua.us-west-2.elasticbeanstalk.com.
2024-02-20 22:11:01    INFO    Successfully launched environment: bicycle-project-env
Troubleshooting Tips

If you encounter any errors, you can create a new Elastic Beanstalk environment with a different name. For example, change bicycle-project-env to bicycle-project-env2 in the command you just ran and run it again.
To make an update to the application code deployed to Elastic Beanstalk without changing the Elastic Beanstalk environment settings, run the command eb deploy --region us-west-2 bicycle-project-env. This will deploy your application updates to the existing Elastic Beanstalk environment.
Task 4.5: Test and make observations
Confirm that the web application is working as intended for end users when hosted on Elastic Beanstalk. Confirm that you can access the Django administration UI.

 Command: When the terminal returns you to a prompt, enter the following command to get the status:


eb status bicycle-project-env
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Environment details for: bicycle-project-env
  Application name: bicycle-project-ebapp
  Region: us-west-2
  Deployed Version: app-240220_220818619859
  Environment ID: e-pdztiyhesk
  Platform: arn:aws:elasticbeanstalk:us-west-2::platform/Python 3.11 running     on 64bit Amazon Linux 2023/4.0.8
  Tier: WebServer-Standard-1.0
  CNAME: bicycle-project-env.eba-xi98atua.us-west-2.elasticbeanstalk.com
  Updated: 2024-02-20 22:11:01.233000+00:00
  Status: Ready
  Health: Green
(.venv)
 Note: The response includes a CNAME value, which is the URL you can use to test the application.

Navigate to the Elastic Beanstalk console.

In the left navigation pane, choose Environments.

Choose the link for bicycle-project-env.

The Health should indicate Ok.

The domain URL is displayed in the format http://bicycle-project-env.UNIQUE-VALUE.us-west-2.elasticbeanstalk.com.

Choose the domain link.

The AnyCompany bicycle parts website displays. It should appear the same as it did when it was hosted on AWS Cloud9.

The functionality to place an order, view order history, and view order details should also work as intended.

To access the Django administration UI, add /admin to the end of the URL. For user, enter admin. For password, enter djangoSecret764.
 Tip: Alternatively, you can log in with the user ProductManager1 and password Manager2024!.

The Django administration UI should display, and you should have access to the model data.

Navigate to the browser tab with the Elastic Beanstalk console.

In the Platform panel, notice that the environment uses Python 3.11.

In the Events tab, notice that it provides the same output that you received after you ran the eb create command that created this environment.

Choose the Logs tab.

On the Request logs menu, choose Last 100 lines.

Choose the Download link.

A new browser tab opens and displays the output from different logs, including the /var/log/eb-engine.log.

Task 4.6: Connect to the EC2 instance that Elastic Beanstalk manages
Connect to the EC2 instance that Elastic Beanstalk manages to make observations about how your application is now hosted.

Navigate to the EC2 console, and in the left navigation pane, choose Instances.

Choose the link for the bicycle-project-env instance.

Choose Connect.

For Connect to instance, choose the Session Manager tab.

Choose Connect.

 Command: In the terminal that appears, run the following command:


sudo tail -100 /var/log/eb-engine.log
 Note: This is the log file that the eb-engine.log content was pulled from when you chose Download from the Logs tab.

 Command: To install the tree utility, which is helpful for browsing directory contents, run the following command:


sudo yum install -y tree
 Expected output: The following output is truncated.


******************************
**** This is OUTPUT ONLY. ****
******************************

Installed:
tree-1.8.0-6.amzn2023.0.2.x86_64

Complete!
 Command: To observe where the application is installed, run the following command:


tree /var/app/current/bicycle_app
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************
/var/app/current/bicycle_app
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   ├── 0001_initial.py
│   ├── __init__.py
│   └── __pycache__
│       ├── 0001_initial.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── models.py
├── __pycache__
│   ├── admin.cpython-310.pyc
│   ├── admin.cpython-311.pyc
│   ├── apps.cpython-310.pyc
│   ├── apps.cpython-311.pyc
│   ├── __init__.cpython-310.pyc
│   ├── __init__.cpython-311.pyc
│   ├── models.cpython-310.pyc
│   ├── models.cpython-311.pyc
│   ├── urls.cpython-310.pyc
│   ├── urls.cpython-311.pyc
│   ├── views.cpython-310.pyc
│   └── views.cpython-311.pyc
├── static
│   ├── bell.jpeg
│   ├── biking-outdoors.jpeg
│   ├── brake-disk.jpeg
│   ├── cassette.jpeg
│   ├── chain.jpeg
│   ├── crank-arm.jpeg
│   ├── css
│   │   └── main.css
│   ├── gear-shifter.jpeg
│   ├── hydraulic-brake.jpeg
│   ├── inner-tube.jpeg
│   ├── logo-black.png
│   ├── logo-white.png
│   ├── map.jpeg
│   ├── pedals.jpeg
│   ├── rear-light.jpeg
│   ├── repair.jpeg
│   ├── seat.jpeg
│   ├── specialist.png
│   ├── sports-glasses.jpeg
│   └── wheel.jpeg
├── templates
│   ├── favicon.ico
│   ├── index.html
│   ├── order_history.html
│   ├── order_result.html
│   ├── products.html
│   └── test_form.html
├── tests.py
├── urls.py
└── views.py
6 directories, 49 files
This is the location where your application code was deployed. If you make further adjustments to your codebase in the AWS Cloud9 instance, use the eb deploy --region us-west-2 bicycle-project-env command to update the application. This will update the code accordingly.

Task 4.7: Modify the source code and deploy the updated application
Experience how you can make a modification to the application source code that is on the AWS Cloud9 instance. Deploy an updated version of the application to Elastic Beanstalk.

Make an update to your codebase and redeploy.

In the AWS Cloud9 IDE, open bicycle_app/static/css/main.css in the file editor.

Locate the following lines:


.nav-menu a:hover {
    background-color: darkblue;
}

h2 {
background-color: darkblue;
Change both occurences of darkblue to darkgreen.

Save the changes.

 Command: To collect the change to the static folder, in the AWS Cloud9 terminal, run the following command:


python manage.py collectstatic
When prompted about whether you want to overwrite existing files, if you are sure, enter yes.

 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

You have requested to collect static files at the destination    location as specified in your settings:
/home/ubuntu/environment/django/static
This will overwrite existing files!
Are you sure you want to do this?
Type 'yes' to continue, or 'no' to cancel: yes
1 static file copied to '/home/ubuntu/environment/django/    static', 145 unmodified.
Deploy a new version of the app.

 Command: To deploy the update, run the following command:


eb deploy --region us-west-2 bicycle-project-env --label 1.0.1   --message 'new look'
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Creating application version archive "1.0.1".
Uploading: [##################################################]      100% Done...
2024-02-20 22:26:06    INFO    Environment update is     starting.      
2024-02-20 22:26:12    INFO    Deploying new version to instance     (s).
2024-02-20 22:26:19    INFO    Instance deployment successfully      generated a 'Procfile'.
2024-02-20 22:26:28    INFO    Instance deployment completed     successfully.
2024-02-20 22:26:34    INFO    New application version was   deployed to         running EC2 instances.
2024-02-20 22:26:35    INFO    Environment update completed      successfully.
 Note: The command applies a version and a message to the deployment.

Wait until the updated deployment completes and you are returned to the command prompt. This time, you are only updating the application, not deploying an entire Elastic Beanstalk environment. The eb deploy command should complete faster than the eb create command did previously.

Reload the website on the Elastic Beanstalk domain, which is in the format http://bicycle-project-env.eba-xxxxx.us-west-2. elasticbeanstalk.com/.

Did you notice that the update was applied?

In the Elastic Beanstalk console, in the left navigation pane, choose Applications.

Choose bicycle-project-ebapp.

Choose Application versions.

 Note: The version label and description you provided have been recorded. This helps you keep track of your application versions.

Elastic Beanstalk Application version listing for the bicyble-project-ebapp application

Image description: The images depicts the bicycle-project-ebapp and the application versions currently available.

Optional: You can roll back to the previous application version.

Select the application version which has a label of EB-CLI deploy under the Description column.

On the Actions menu, choose Deploy.

Select the bicycle-project-env environment to deploy to.

Choose Deploy.

Optionally, observe the environment events as the redeploy of the previous version occurs.

After the deployment update completes, reload the webpage to ensure that the latest change was reverted.

Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: In this task, you successfully migrated the Django hosting environment from the AWS Cloud9 instance to run on Elastic Beanstalk. You also tested the functionality of the site, observed how the deployment is configured, and deployed an update to the application.

Conclusion
You have successfully done the following:

Created an S3 bucket with CORS configured.
Used the AWS CLI to upload objects to an S3 bucket.
Configured Django to use Amazon S3 as a storage location.
Configured an Amazon RDS database to support a Django application.
Configured Django to use Amazon RDS for MySQL.
Installed the Elastic Beanstalk CLI and configured a Django application for deployment.
Used the Elastic Beanstalk CLI to create an environment and an application.
Updated the Django application source and deployed the update to Elastic Beanstalk.
Rolled back an Elastic Beanstalk application update.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
Using Cross-Origin Resource Sharing (CORS)
Common Response Headers
Django Documentation
Gunicorn
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

Django is property of the Django Software Foundation, and Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.