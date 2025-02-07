# Creating Data Models in a Web Framework

## Lab overview

This is the second in a series of labs that have you working with Django, a Python web framework that helps you avoid extra coding and helps you build websites that are scalable and maintainable. In the first Django lab, you installed the Django web framework in a Python virtual environment and then created a basic Django project with a hello world web app running in it.

In this lab, you create models in Django to support storing product information and order information in the database used by Django.

Objectives
By the end of this lab, you should be able to do the following:

Configure Django to use the MySQL database.
Use Python to create Django models for a web app.
Use a sql client to confirm a database table and table entries.
Use the Django interactive shell and the Django loaddata command to create test data in the database.
Confirm that you can display model data on a webpage.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Task complete: A conclusion or summary point in the lab.
 Tip: A shortcut or recommended best practice.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
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
The following diagram shows the basic architecture of the lab environment. The resources depicted in the diagram already exist in your Amazon Web Services (AWS) account when you start the lab.

AWS Architecture diagram showing the initial state of the lab environment

Image description: The diagram illustrates a person (you) using the AWS Cloud infrastructure. The person is accessing an AWS Cloud9 IDE which is hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance running Ubuntu as the guest operating system. A security group acts as a firewall to control access to the EC2 instance. For more information, refer to the following detailed diagram overview.

Detailed diagram overview
AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Run the script to configure the development environment
In this first task, you run a script that installs the Django framework on your Ubuntu linux instance and gets your environment to match the end state of the previous lab.

Task 1.1: Connect to the IDE and run the setup script
Copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab. It connects you to the AWS Cloud9 IDE.

 Command: In the AWS Cloud9 IDE terminal window, run the following command:


./setup.sh
 Analysis: The shell script completes configurations on the Amazon EC2 instance on which your AWS Cloud9 IDE is installed. The configurations replicate the steps that you completed in the previous lab: installing a Python virtual environment, installing Django, creating the bicycle_project Django project, and creating the bicycle_app Django app.

 Note: If you receive a prompt asking which services should be restarted, use your Tab key to select Ok and press the Enter key so that the script continues running.

If the script ran successfully, the final output should look like this:

 Expected output:


(truncated)...

from . import views
urlpatterns = [
    path("", views.index, name="index"),
]
 Command: To start the Django web server, run the following commands:


cd ~/environment/django
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8080
 Expected output:


Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 07, 2024 - 22:10:13
Django version 5.0.2, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
 Note: The web server only remains running while you keep the process active in the terminal. Leave this terminal as it is. Note that debug information might by written to this terminal’s output as you progress through the lab. It is a good place to look if and when you are troubleshooting issues.

 Troubleshooting tip: Only if the web server stops responding and has to be started again, you could do the following:

Run cd ~/environment/django.
Run python manage.py runserver 0.0.0.0:8080 to start it as a new Linux process.
If you receive a message that another process is using the same port, you can run sudo lsof -i :8080 to find the process ID (PID) that is using it.
Then use sudo kill pid, where pid is the process number from the previous command result, to stop the process.
Then try python manage.py runserver 0.0.0.0:8080 again to start the server.
Task 1.2: Confirm that the app is running
Choose the link in the Cloud9 Help dialog that appeared.

A new browser tab opens and it displays the Django web interface.

You should see the Hello world from bicycle_app! message.

Hello world webpage.

Image description: Image shows a webpage with text reading, “Hello world from bicycle_app!”.

 Note: You can also get to the same preview page by choosing Preview > Preview Running Application, and then in the preview panel choose the pop-out icon with the upward-pointing arrow in it to open the preview in a new browser tab.

Keep this browser tab open for the duration of this lab. You return it it later.

You might recall from the previous lab that the message displaying comes from the bicycle_app/views.py file.

The following diagram illustrates the currently configured logic. Here is an explanation of each labeled step:

Step 1: Your browser makes a request to load the URL where the app is available.
Step 2: The Django project settings indicate that the bicycle_project’s URLs file should be consulted for routing details.
Step 3: The bicycle_project’s URLs file indicates that if the requested URL is “” (meaning the base URL), the bicycle_app URL file should be consulted.
Step 4: The bicycle_app URL file indicates that the views file’s index function should be consulted.
Step 5: The views file’s index function contains very basic logic. It simply returns an HttpResponse with the hardcoded message Hello world from bicycle_app!.
flowchart

Image description: Image depicts the logic as explained before the image.

Recall however that Django uses a Model View Template architecture. You might have noticed that so far your app is only using a view and is not using models or templates.

In this lab and the two that follow, you extend this basic configuration to make use of models and templates.

The design that you have then looks more like the following diagram. Here is an explanation of each labeled step:

Step 1: Your browser makes a request to load the URL.
Step 2: The same URL logic described in detail in the previous diagram still occurs.
Step 3: The Python functions defined in the views.py file control the application logic.
Step 4: The view logic typically runs a SQL query using the included model to look up data or modify or insert data. A dataset from the database is returned to the view.
Step 5: The view logic typically loads an HTML template and then injects data from the dataset into it.
Step 6: Finally, the view logic returns the response, which might render the same page to display data from the dataset, or the view logic might redirect the user to a different webpage that makes use of a different template to display dataset results.
Model-view-template data flow.

Image description: Image depicts the logic using six steps, as explained before the image.

 Task complete: You successfully ran a script that installs the Django framework on your Ubuntu linux instance and got your environment to match the end state of the previous lab.

Okay! Now that you have an idea what type of solution this lab and the next two labs are driving towards, it’s time to start implementing the details. Start by creating the models, which are used to create the database tables needed to support the bicycle shop web app.

Task 2: Configure Django to use MySQL
In this task, you configure Django to use MySQL.

Task 2.1: Activate the Python virtual environment in the terminal
Start by activating the Python virtual environment.

In the AWS Cloud9 IDE, choose the plus icon next to the terminal where your Django runserver command is running, and choose New Terminal.

A new terminal opens.

 Command: In the new terminal, run these commands:


cd ~/environment/django
source .venv/bin/activate
 Expected output:


(.venv)
The terminal prompt should now display (.venv).

Task 2.2: Start MySQL and install needed connector software
By default, Django uses sqlite as the database in which to store data. In this task, you configure Django to use MySQL instead. Doing so is consistent with the [dev prod parity](https://us-west-2-tcprod.s3.us-west-2.amazonaws.com/courses/SPL-PW-300-DVF307/v1.0.3.prod-3a1f0138/instructions/en_us/dev prod parity) principle of the Twelve-Factor App principles. Because in a later lab, you migrate the database used by Django from the MySQL running locally on this EC2 instance to instead run on Amazon Relational Database Service (Amazon RDS) for MySQL.

 Command: To start the MySQL database that is already installed on the EC2 instance, run the following commands:


sudo systemctl start mysql ; sudo systemctl status mysql
 Expected output:


● mysql.service - MySQL Community Server
  Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
  Active: active (running) since Wed 2024-02-07 21:18:30 UTC; 1h 1min ago
Main PID: 608 (mysqld)
  Status: "Server is operational"
   Tasks: 37 (limit: 4598)
  Memory: 427.2M
     CPU: 26.051s
  CGroup: /system.slice/mysql.service
          └─608 /usr/sbin/mysqld

Feb 07 21:18:25 ip-10-0-1-124 systemd[1]: Starting MySQL Community Server...
Feb 07 21:18:30 ip-10-0-1-124 systemd[1]: Started MySQL Community Server.
The output should show that the mysql.service is now Active: active (running).

To install the software dependencies that are needed so that Django can connect to MySQL, run the following commands.

 Command: To update libraries on the Ubuntu OS, run this command:


sudo apt-get update
 Expected output:


(truncated)...
Get:18 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [838 kB]
Get:19 http://security.ubuntu.com/ubuntu jammy-security/universe Translation-en [160 kB]
Fetched 8825 kB in 2s (3727 kB/s)                            
Reading package lists... Done
(.venv) AWSLabsUser-v4Rqi3TSz8G6iypboXM8eN:~/environment/django $
 Command: To install additional software on the Ubuntu OS, run this command:


sudo NEEDRESTART_MODE=a apt-get install -y python3-dev default-libmysqlclient-dev python3-mysqldb
 Expected output:


...
Running kernel seems to be up-to-date.
No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
 Command: Finally, to use pip to install additional Python libraries needed to configure the connection between Django and MySQL, run this command.


pip install pymysql pillow cryptography
 Expected output:


Collecting pymysql
  Downloading PyMySQL-1.1.0-py3-none-any.whl (44 kB)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.8/44.8 KB 1.4 MB/s eta 0:00:00
Collecting pillow
  Downloading pillow-10.2.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.5 MB)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 42.6 MB/s eta 0:00:00
Collecting cryptography
  Downloading cryptography-42.0.2-cp39-abi3-manylinux_2_28_x86_64.whl (4.7 MB)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 87.6 MB/s eta 0:00:00
Collecting cffi>=1.12
  Downloading cffi-1.16.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (443 kB)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 443.9/443.9 KB 56.2 MB/s eta 0:00:00
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 KB 19.9 MB/s eta 0:00:00
Installing collected packages: pymysql, pycparser, pillow, cffi, cryptography
Successfully installed cffi-1.16.0 cryptography-42.0.2 pillow-10.2.0 pycparser-2.21 pymysql-1.1.0
 Command: To update the Django installation to use the pymysql library that you just installed, run the following two commands:


echo "import pymysql" >> /home/ubuntu/environment/django/bicycle_project/__init__.py
echo "pymysql.install_as_MySQLdb()" >> /home/ubuntu/environment/django/bicycle_project/__init__.py
 Expected output:

None, unless there is an error.

Task 2.3: Configure MySQL users and permissions
In this task, you set up the Django user and grant permissions.

 Command: Set the MySQL root user password:


sudo mysqladmin -u root password 'AciDb2034'
 Expected output:


mysqladmin: [Warning] Using a password on the command line interface can be insecure.
Warning: Since password will be sent to server in plain text, use ssl connection to ensure password safety.
 Command: Connect as root to MySQL:


sudo mysql -u root -p
When prompted, enter the following password:


AciDb2034
 Expected output:


Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.35-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
You should now see that you are at a mysql> prompt.

 Command: Create a database named bicycles and a database user named django.


CREATE DATABASE bicycles CHARACTER SET utf8;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'djangoAciDb2034';
GRANT ALL PRIVILEGES ON bicycles.* To 'django'@'localhost';
 Expected output:


mysql> CREATE DATABASE bicycles CHARACTER SET utf8;
Query OK, 1 row affected, 1 warning (0.01 sec)

mysql> CREATE USER 'django'@'localhost' IDENTIFIED BY 'djangoAciDb2034';
Query OK, 0 rows affected (0.02 sec)

mysql> GRANT ALL PRIVILEGES ON bicycles.* To 'django'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql>
 Command: Exit the the mysql client to return to a terminal prompt.


exit;
 Expected output:


Bye
 Command: Create a file to store the Django MySQL user credentials that you can use for connections. To do this, run these commands:


echo '[client]' | sudo tee -a /etc/mysql/config.cnf
echo 'user = "django"' | sudo tee -a /etc/mysql/config.cnf
echo 'password = "djangoAciDb2034"' | sudo tee -a /etc/mysql/config.cnf
echo 'host = "localhost"' | sudo tee -a /etc/mysql/config.cnf
 Expected output:


(.venv) AWSLabsUser-v4Rqi3TSz8G6iypboXM8eN:~/environment/django $ echo '[client]' | sudo tee -a /etc/mysql/config.cnf
[client]
(.venv) AWSLabsUser-v4Rqi3TSz8G6iypboXM8eN:~/environment/django $ echo 'user = "django"' | sudo tee -a /etc/mysql/config.cnf
user = "django"
(.venv) AWSLabsUser-v4Rqi3TSz8G6iypboXM8eN:~/environment/django $ echo 'password = "djangoAciDb2034"' | sudo tee -a /etc/mysql/config.cnf
password = "djangoAciDb2034"
(.venv) AWSLabsUser-v4Rqi3TSz8G6iypboXM8eN:~/environment/django $ echo 'host = "localhost"' | sudo tee -a /etc/mysql/config.cnf
host = "localhost"
Task 2.4: Configure Django to use MySQL as the database
Open the django > bicycle_project > settings.py file in the file editor and locate the following lines:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Replace those lines with the following lines:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bicycles',
        'USER': 'django',
        'PASSWORD': 'djangoAciDb2034',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
 Command: Run the Django migrate command.


cd /home/ubuntu/environment/django
python manage.py migrate
 Expected output: Verify that the last part of the output looks similar to the following:


...
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
To confirm that there are no errors, return to the terminal window where you left the web server running.

 Expected output: You should see output similar to the following.


...
System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project might not work properly until you apply the migrations for app(s): admin, auth, contenttypes,  sessions.
Run 'python manage.py migrate' to apply them.
January 12, 2024 - 01:01:37
Django version 5.0.1, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
If you see errors, try pressing Ctrl+C on your keyboard, and then run python manage.py runserver 0.0.0.0:8080 again to restart the server.

 Task complete: You successfully configured Django to use MySQL.

Task 3: Create models and insert test data
In this task, you create Django models (that are used to create database tables) to support the AnyCompany bicycle parts website. You might recall from previous labs that the bicycle parts website contains a listing of products as shown in the following image. The table that displays these products is already wrapped in an HTML form element that contains input elements for each product.

 Tip: You can find the HTML source code for this page in the AWS Cloud9 file browser at www > html > index.html if you want to review it.

Products table.

Image description: Image shows the bicycle parts website Products section. It is a listing of product images, descriptions, prices, and quantity wrapped in an HTML form element that contains input elements for each product.

Task 3.1: Create models to support the web app
Create three models to support the bicycle store app.

Open bicycle_app > models.py in the file editor.

Add the following below the from django.db import models line:


from django.utils import timezone
Add the following below the #Create your models here. line:


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_group = models.IntegerField()
    image_url = models.ImageField(max_length=255)

class Order(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date_time = models.DateTimeField(default=timezone.now)

class Order_Item(models.Model):
    order_number = models.ForeignKey("Order", on_delete=models.CASCADE)
    product_id = models.IntegerField(null=True)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
 Note: This code defines the structure of tables that get created in the MySQL database used by Django.

Save the change to models.py.

Return to the second terminal window (the one not running the web server).

Confirm that the prompt starts with (.venv).

 Note: If it does not, run these commands:


cd ~/environment/django
source .venv/bin/activate
 Command: Create database tables from the Django models.


cd ~/environment/django/
python manage.py makemigrations bicycle_app
python manage.py migrate
 Expected output:


Migrations for 'bicycle_app':
bicycle_app/migrations/0001_initial.py
  - Create model Order
  - Create model Product
  - Create model Order_Item
(.venv) AWSLabsUser-v4Rqi3TSz8G6iypboXM8eN:~/environment/django $ python  manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, bicycle_app, contenttypes, sessions
Running migrations:
  Applying bicycle_app.0001_initial... OK
Task 3.2 Confirm that tables were created in MySQL
 Command: Connect to the MySQL database using the mysql client. This time you use the Django user that you just created and that you just configured Django to use in the settings.py file.


mysql --defaults-extra-file=/etc/mysql/config.cnf
 Note: The command references the config.cnf file that you created earlier, which contains the login credentials for the Django user.

 Expected output:


Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 19
Server version: 8.0.35-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
You should now see a mysql> prompt, indicating that you are connected to the database.

Observe how three tables created from your models now exist in the database.

 Command: At the SQL prompt, run the following commands:


show databases;
use bicycles;
show tables;
 Expected output:


Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------------------+
| Tables_in_bicycles         |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| bicycle_app_order          |
| bicycle_app_order_item     |
| bicycle_app_product        |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
13 rows in set (0.00 sec)
 Analysis: The first command showed all the databases that your MySQL installation contains. The second command told your MySQL client to use the bicycle database. The third command told MySQL to list the tables in the bicycles database.

The output shows that tables named bicycle_app_order, bicycle_app_order_item, and bicycle_app_product now exist. They were created when you ran the migration commands. Those commands used the table schema details that you defined in models.py and created the tables.

 Command: Describe the structure of the product table:


describe bicycle_app_product;
 Expected output:


+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | bigint       | NO   | PRI | NULL    | auto_increment |
| product_name  | varchar(255) | NO   |     | NULL    |                |
| description   | varchar(255) | NO   |     | NULL    |                |
| price         | decimal(8,2) | NO   |     | NULL    |                |
| product_group | int          | NO   |     | NULL    |                |
| image_url     | varchar(255) | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
6 rows in set (0.01 sec)
 Note: See how the fields and types match the specifications defined in models.py. However, Django also created an id field in the table. As explained in the Django models documentation, if your model does not specify a primary key, Django automatically creates one for you. Therefore, you find that all three of the tables you just created also now contain an id field as the primary key.

 Command: Try to select some data from the product table:


select * from bicycle_app_product;
 Expected output:


Empty set (0.00 sec)
The output indicates Empty set, meaning that the database table currently contains no rows of data. That is expected at this point in the lab.

 Command: Exit the MySQL client.


exit;
 Expected output:


Bye
You are returned to the (.venv) command prompt.

Task 3.3: Use the Django shell to create two rows of test data
Create test data using the Django shell.

 Command: Use the following command to connect to the Django shell:


python manage.py shell
 Expected output:


Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
You should now see a '>>>` interactive Python prompt. Django provides this Python REPL (Read-Eval-Print Loop) interface as a useful tool. You can use it to run Python code for your Django projects interactively. A key feature is that it can connect to the database used by Django.

 Command: At the >>> prompt, run commands to import the Product table and then list all objects in the table.


from bicycle_app.models import Product
Product.objects.all()
 Expected output:


Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bicycle_app.models import Product
>>> Product.objects.all()
<QuerySet []>
>>>
Notice that there are currently no objects in the Product table, as indicated by the <QuerySet []> response.

 Analysis: Running Product.objects.all() in the REPL provided you the same information as running select * from bicycle_app_product; in the SQL client.

 Command: Next, run the following code to define two records that can be inserted as rows in the Product table.


prod1 = Product(product_name='cassette', description='some description', price = '50.00', product_group='1', image_url='/var/www/html/images/cassette.jpeg')
prod2 = Product(product_name='crankset', description='some description', price = '215.00', product_group='1', image_url='/var/www/html/images/crank-arm.jpeg')
 Expected output:

None, unless there is an error.

 Command: Save the rows to the database.


prod1.save()
prod2.save()
 Expected output:

None, unless there is an error.

Now run the command to see the objects in the Products table again.


Product.objects.all()
 Expected output:


<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>
The response indicates that the QuerySet Product object now contains two Product objects.

 Command: To view the actual object data, run this command:


Product.objects.all().values()
 Expected output:


<QuerySet [{'id': 1, 'product_name': 'cassette', 'description': 'some description', 'price': Decimal('50.00'), 'product_group': 1, 'image_url': '/var/www/html/images/cassette.jpeg'}, {'id': 2, 'product_name': 'crankset', 'description': 'some description', 'price': Decimal('215.00'), 'product_group': 1, 'image_url': '/var/www/html/images/crank-arm.jpeg'}]>
That returns the details for both objects. Notice how although you did not specify an ID, when creating these rows, they still receive id values, based on the order in which you created them.

What if you wanted to return just the object that has an id value of 1?

 Command: Then you could run this command:


Product.objects.filter(id=1).values()
 Expected output:


<QuerySet [{'id': 1, 'product_name': 'cassette', 'description': 'some description', 'price': Decimal('50.00'), 'product_group': 1, 'image_url': '/var/www/html/images/cassette.jpeg'}]>
 Analysis: If you were trying to retrieve the same data in a SQL client, you would run select * from bicycle_app_product where id='1';. The fact that you can access (retrieve, insert, modify, delete) database table data using Python code proves useful when you define application logic in the view.py file in the next task in this lab.

 Command: Run the following command to return to the command prompt.


exit()
 Expected output:

None, unless there is an error.

 Task complete: You have successfully created models and inserted test data.

Task 4: Pull model data into a view and use a template
In this task, you update the view so that it pulls in data from the Products database table.

Task 4.1: Update the view
Update the views.py script to change the logic used in the view code.

Update bicycle_app > views.py to match this:


from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader

def index(request):
    #return HttpResponse("Hello world from bicycle_app!")
    product_item = Product.objects.all()
    context = {'product_item': product_item}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
Be sure to save the changes.

 Analysis: Notice the changes that you just made to the view code logic.

The code now imports the Product model that you defined in models.py a moment ago.
It also defines an object named product_item. It is created by running the same Product.objects.all() command that you ran in the shell utility to confirm that rows exist in the database. Therefore, this object now contains those rows of data.
A context set is created and then returned as part of the HttpResponse. You are able to reference this context set in the template.
The code also references a template that does not yet exist and then uses that template to render the response. You create the template next.
Task 4.2: Create a basic template
Create a directory named templates in the bicycle_app directory.

Create a new file named index.html in the templates directory.

Add the following HTML code to the index.html template to print some data from the HttpResponse that is now being sent to it:


<!DOCTYPE html>
<html>
  <body>
   <h1>Hello from bicycle_app</h1>
   <ul>
        {% for product in product_item %}
        <li>{{ product.product_name }}</li>
        {% endfor %}
   </ul>
 </body>
</html>
Save the changes.

 Analysis: You likely notice the line <li>{{ product.product_name }}</li> in the HTML code and the for loop that it appears in. These lines of code are an example of using the Django template language. They reference the context that was passed to the template in the HttpResponse from the view. If this does not make much sense yet, don’t worry. The Django template language is explored in detail in the upcoming labs.

Task 4.3: Test
Verify that the data from the model—and thus from the database—is now appearing on your webpage.

If you reload your webpage, it should now look like this.

Data from model.

Image description: Image shows a webpage with a message of “Hello from bicycle_app” in bold text with a bulleted list of two items reading “cassette” and “crankset”.

 Troubleshooting tip: If the webpage returns an error, make sure that you did save the index.html file and that you did save the changes to views.py, then try reloading the page again. If that still does not resolve the issue, try stopping and then restarting the runserver process. To do this:

Select the terminal where the runserver process is active.
Press Ctrl+C to stop the server.
The terminal returns to the (.venv) prompt. Use the arrow up key on your keyboard to reload the python manage.py runserver 0.0.0.0:8080 command (or manually type it in again). And then press Enter to start the runserver process again.
The terminal displays the usual message indicating that the server is again running.
On the webpage, notice that there are two line items displaying, even though you only have a single <li> element defined. The for loop must be working. Because two rows of data were found in the product table, there are two rows of data displaying on the webpage.

To view the following challenge, expand this section.

Challenge
Can you also get the price to display in the webpage?

You should accomplish this without hardcoding the actual prices into the HTML (although you can hardcode the $ sign). Instead, retrieve the price from the database.

If you do it correctly, it should look like this:

Data from model.

Image description: Image shows a webpage with a message of “Hello from bicycle_app” in bold text with a bulleted list of two items reading “cassette $50.00” and “crankset $215.00”.

Did you get the same result?

If you need help, choose here to see the necessary change to the index.html code.
The contents of the line item element should now look like this. The dollar sign is hardcoded.


<li>{{ product.product_name }} ${{ product.price }}</li>
Task 4.4: Use the loaddata tool to add more data
Earlier in this lab, you used the Django shell to add two rows of data to the Products database table. In this task, you use the Django loaddata tool to add more products.

In the AWS Cloud9 file editor, open the products.json file, which is located in the main /home/ubuntu/environment folder. It displays towards the bottom of the environment file browser panel.

 Analysis: Notice that there are 12 products defined in JSON format, including the two products that you inserted earlier. For each product, values are provided that match what the database table expects.

 Command: To delete the existing rows of data in the product table, run the following commands in the terminal:


mysql --defaults-extra-file=/etc/mysql/config.cnf -e "use bicycles; delete from bicycle_app_product;"
 Expected output:

None, unless there is an error.

 Command: To load the JSON formatted data into the Products table, run the following command:


python manage.py loaddata /home/ubuntu/environment/products.json
 Expected output:


Installed 12 object(s) from 1 fixture(s)
The output of the command should indicate success.

 Tip: You can read details about the loaddata command in the Django documentation.

Return to the Django webpage and reload it.

You should now see all 12 products listed, along with their corresponding prices.

Full line item data displaying.

Image description: Image shows a webpage with a message of “Hello from bicycle_app” in bold text with a bulleted list of 12 bicycle-related items.

You have now accomplished a simple implementation of the Model-View-Template (MVT) web application architecture that powers the Django framework! Take a moment to bask in the glory! :-)

There are many moving parts, but when you understand the concept you can readily extend it to more complex webpages than this simple one that you just created.

Recall this diagram shown earlier in the lab. Maybe the concept is starting to make more sense now that you have practiced implementing it.

Model-view-template data flow.

Image description: Image depicts the logic using six steps. For a detailed explanation, expand the following section.

Detailed diagram explanation
Step 1: Your browser makes a request to load the URL.
Step 2: The same URL logic described in detail in the previous diagram still occurs.
Step 3: The Python functions defined in the views.py file control the application logic.
Step 4: The view logic typically runs a SQL query using the included model to look up data or modify or insert data. A dataset from the database is returned to the view.
Step 5: The view logic typically loads an HTML template and then injects data from the dataset into it.
Step 6: Finally, the view logic returns the response, which might render the same page to display data from the dataset, or the view logic might redirect the user to a different webpage that makes use of a different template to display dataset results.
Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: You have successfully pulled model data into a view and used a template.

To recap:

You inserted data into a database table.

You then configured Django to pull that data into the webpage.

Now that you have all the MVT pieces working, it is fairly straightforward to build out the rest of the bicycle supplies webpage on Django. The result you soon achieve might look almost exactly like the webpage that you built from scratch without using a framework. But it is much more scalable, extendable, and maintainable. Let’s get started doing that in the next lab!

Conclusion
You have successfully done the following:

Configured Django to use the MySQL database.
Used Python to create Django models for a web app.
Used a sql client to confirm a database table and table entries.
Used the Django interactive shell and the Django loaddata command to create test data in the database.
Confirmed that you can display model data on a webpage.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

Django is property of the Django Software Foundation, and Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.