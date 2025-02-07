# Installing and Configuring a Web Framework

## Lab overview

This is the first lab in a series of labs that use Django. Django is a Python web framework that helps you avoid extra coding. It also helps you build scalable and maintainable websites. In this series of labs, you migrate the AnyCompany bicycle parts website you created in previous labs to run on the Django framework. Using Django provides a database storage layer for your web application. This makes it possible for you to store application data in a database and further enhance the AnyCompany bicycle parts website.

In this first Django lab, you install the Django web framework in a Python virtual environment. Then, you create a basic Django project with a Hello World web application running in it.

Objectives
By the end of this lab, you should be able to do the following:

Upgrade packages on Ubuntu, a Linux distribution.
Create a virtual Python environment.
Install Django using pip.
Create and configure a Django project.
Start the Django server and test access to it from the internet.
Create a Hello World Django application.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: Additional information or elaboration on a point.
 Task complete: A conclusion or summary point in the lab.
 Tip: A shortcut or recommended best practice.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made)
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

Image description: The diagram illustrates a person (you) using the AWS Cloud infrastructure. The person is accessing an AWS Cloud9 IDE which is hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance running Ubuntu as the guest operating system. A security group acts as a firewall to control access to the EC2 instance. For more information, refer to the following detailed diagram overview.

Detailed diagram overview
AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab.

Task 1: Upgrade operating system packages and create a Python virtual environment
In this task, you connect to the AWS Cloud9 IDE. You then run commands to verify and upgrade software libraries. You also create a Python virtual environment and activate it in a terminal.

Task 1.1: Connect to an EC2 instance and upgrade operating system packages
Connect to the AWS Cloud9 IDE and run commands to install software.

Copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab.

It connects you to the AWS Cloud9 integrated development environment (IDE).

 Command: To list the details about the guest operating system, in the AWS Cloud9 IDE, run the following command:


uname -a
 Expected output:


Linux ip-10-0-1-252 6.2.0-1017-aws #17~22.04.1-Ubuntu SMP Fri Nov 17 21:07:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
 Command: To list additional information about the operating system, run the following command:


cat /etc/os-release
 Expected output:


PRETTY_NAME="Ubuntu 22.04.3 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
Notice the lines ID=ubuntu and ID_LIKE=debian. Debian is another version of Linux. Ubuntu builds on Debian, which is a community-driven project. Ubuntu is developed and maintained by Canonical.

Ubuntu uses the Advanced Package Tool (APT) as its default package manager. This is in contrast to the Red Hat and CentOS Linux distributions, which use the Yellowdog Updater Modifier (YUM) as their package manager.

 Command: To learn about the APT package manager, enter the following command:


apt --help
 Expected output:


apt 2.4.11 (amd64)
Usage: apt [options] command

apt is a commandline package manager and provides commands for
searching and managing as well as querying information about packages.
It provides the same functionality as the specialized APT tools,
like apt-get and apt-cache, but enables options more suitable for
interactive use by default.

Most used commands:
list - list packages based on package names
search - search in package descriptions
show - show package details
install - install packages
reinstall - reinstall packages
remove - remove packages
autoremove - Remove automatically all unused packages
update - update list of available packages
upgrade - upgrade the system by installing/upgrading packages

...(truncated)
The output of the command gives you an introduction to what you can accomplish with APT.

The EC2 instance you are running was created from an Amazon Machine Image (AMI) that was created some time ago. The packages installed on the Ubuntu operating system embedded in the AMI might no longer be the latest versions.

 Command: To update any outdated packages, run the following command:


sudo apt upgrade -y
 Expected output:


Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
 Note: You might be prompted to restart any services that use outdated libraries. Press the Tab key to navigate to <Ok>, and then press Enter.

You return to the command prompt.

Task 1.2: Analyze the Python and pip settings
Verify the installed versions of Python and pip.

 Command: To verify the version of Python that is installed, run the following command:


python -V
 Expected output:


Python 3.10.12
The output should indicate a 3.x.x version of Python is installed. You might have a newer version than what is listed in this example.

 Command: To verify pip is installed and to list which version is installed, run the following command:


pip -V
 Expected output:


pip 24.0 from /usr/local/lib/python3.10/dist-packages/pip (python 3.10)
The output should indicate that pip is installed for the version of Python that is installed. Your version might be newer than what is listed in this example.

 Tip: The standard package manager for Python is pip. It works similar to Linux distributions that come with a package manager to manage the software you install on the operating system. You can use pip to manage Python packages that you install that are not distributed as part of the default Python installation.

Task 1.3: Create a Django project directory and a Python virtual environment
Create a directory for Django and change directories into it.

 Command: To create a new directory named django and then change directories into this directory, run the following command:


mkdir ~/environment/django
cd ~/environment/django
 Expected output: There is no expected output unless there is an error.

 Command: To create a virtual environment in the django directory and activate it, run the following command:


python -m venv .venv 
source .venv/bin/activate
 Note: Your command prompt now begins with (.venv), such as the following example:


(.venv) AWSLabsUser-xxxxx:~/environment/django $
 Tip: With Python virtual environments, you can create isolated Python environments. This is a helpful way to cleanly control which software libraries your project uses. You do not need to concern yourself with how your project-specific Python settings might impact other software installed on the operating system that might have different Python dependencies. For more information, see Creation of Virtual Environments in the Additional resources section.

 Note: Anytime you open a new command prompt and want to use the virtual environment, navigate to the django directory. Then, run the source .venv/bin/activate command to connect to it and use it.

To deactivate the virtual environment, run the deactivate command. However, keep the virtual environment activated in the current terminal window.

 Task complete: You successfully connected to the AWS Cloud9 IDE. You then ran commands to verify and upgrade software libraries. Finally, you created a Python virtual environment and activated it in a terminal.

Task 2: Install Django and create a project
In this task, you install Django using the pip install command. You then use the django-admin command-line utility to create a Django project.

Task 2.1: Install Django
Use the virtual environment to install Django.

 Command: To install Django in the virtual environment, run the following command:


pip install django
 Expected output:


Collecting django
  Downloading Django-5.0.3-py3-none-any.whl (8.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 18.7 MB/s eta 0:00:00
Collecting asgiref<4,>=3.7.0
  Downloading asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
 Downloading sqlparse-0.4.4-py3-none-any.whl (41 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.2/41.2 KB 3.5 MB/s eta 0:00:00
Collecting typing-extensions>=4
 Downloading typing_extensions-4.10.0-py3-none-any.whl (33 kB)
Installing collected packages: typing-extensions, sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-5.0.3 sqlparse-0.4.4 typing-extensions-4.10.0
 Note: If you receive an alert that a new version of pip is available, ignore it.

 Command: To verify the Django installation, run the following command:


python -m django --version
 Expected output:


5.0.3
The software version number should display. Your version might be newer than the version in this example.

Task 2.2: Create a project, analyze the settings, and start the Django server
Create a Django project and configure it.

 Command: To create a Django project, run the following command:


django-admin startproject bicycle_project .
 Note: Include the . at the end of the command to create the project in the current directory.

 Expected output: There is no expected output unless there is an error.

 Tip: The command you ran uses the django-admin command-line utility, which is useful for completing many tasks. For more information, see Django Documentation in the Additional resources section.

In the AWS Cloud9 file browser, expand django, and then expand bicycle_project.

Open settings.py.

Update the existing ALLOWED_HOSTS line to match the following:


ALLOWED_HOSTS = ['*']
By setting ALLOWED_HOSTS to any, which is represented by the *, you make the site accessible on any domain or host that you specify. For a production site, you would specify a specific host or set of hosts. However, for the purposes of this lab, you can use the any host setting.

Scroll to the MIDDLEWARE section of the file, and comment out the following line:


#'django.middleware.clickjacking.XFrameOptionsMiddleware',
 Note: By disabling this setting, you can display the Django end-user interface using the AWS Cloud9 Preview feature.

Save the changes.

In the settings.py file, observe the following additional settings:

INSTALLED_APPS: When you create a new application later in this lab, you need to update this list to include it.
DEBUG = True: For a production site, you would not want to leave DEBUG set to True. However, during development, it is helpful to have debugging turned on. This setting enables the display of detailed error pages to display. When there are issues with your Django file settings or your application code, you can use the detailed error pages with traceback to help fix the issues.
When you are done observing the file contents, close the settings.py file.

 Note: In the django directory, notice the file named manage.py. This file was created when you created the project. It is the Django command-line utility for administrative tasks. When you work with Django, you use manage.py often.

 Tip: You might notice manage.py invoked in one of two ways. You can run python manage.py migrate or you can run ./manage.py migrate. In either case, you should be in the directory that contains the manage.py file when you run the command. The two commands accomplish the same thing. For more information, see Django Documentation in the Additional resources section.

 Command: In the django directory, run the following migrate command:


python manage.py migrate
 Expected output:


Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
 Analysis: Django has the concept of migrations, which is a way to control when changes made to models are propagated to the schema of the database used by Django. You learn more about models later in this course. For now, know that the migrate command applies unapplied migrations. This is the first time you ran the migrate command after installing Django, so there were some migrations to apply.

To start the Django server, run the following command:


python manage.py runserver 0.0.0.0:8080
 Expected output:


Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 05, 2024 - 18:58:55
Django version 5.0.3, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
This command started a web server on port 8080 of the EC2 instance where the AWS Cloud9 IDE is running.

 Note: The web server only remains running while you keep the process active in the terminal. Leave this terminal as it is. Debug information might be written to this terminal’s output as you progress through the lab. It is a good place to look when you are troubleshooting.

Notice the following pop-up message that appears.

cloud9 help message

Image description: Image depicts a Cloud9 Help message that states, “Your code is running at [URL for the Cloud9 instance].”

AWS Cloud9 can proxy the web server that is running locally on TCP 8080 to make it available over TCP port 443, which is the default HTTPS port.

Choose the link in the Cloud9 Help pop-up message.

A new browser tab opens, and it displays the Django web interface.

initial django page

Image description: The image displays the default Django home page.

The Django web interface should be available at https://xxxxx.vfs.cloud9.us-west-2.amazonaws.com/, where xxxxx is a unique ID for your AWS Cloud9 instance.

 Note: Inbound port 443 does not need to be open in the EC2 instance’s security group inbound rules for you to access this URL. For more information, see Previewing Running Applications in the AWS Cloud9 Integrated Development Environment (IDE) in the Additional resources section.

You can also get to the same preview page by choosing Preview > Preview Running Application. In the preview panel, choose the pop out icon with the upward-pointing arrow in it to open the preview in a new browser tab.

Keep this browser tab open for the duration of this lab. You return to it later.

 Task complete: You successfully installed the Django framework on your Ubuntu instance (the AWS Cloud9 instance). You then created a project folder, started the Django web server, and tested your access to a Django webpage as an end user.

Task 3: Create a Django app and run Hello World
Now that you have a functioning Django server running, in this task, you create an app to run on it.

Task 3.1: Create a Django app
Create a Django app called bicycle_app.

In the AWS Cloud9 IDE, choose the plus sign icon next to the terminal where your Django runserver command is running, and then choose New Terminal.

 Command: In the new terminal, to navigate to the correct directory and activate the Python virtual environment, run the following commands:


cd ~/environment/django
source .venv/bin/activate
 Expected output: There is no expected output unless there is an error.

Verify that (.venv) is at the start of the command prompt.

To create an app called bicycle_app, run the following command:


python manage.py startapp bicycle_app
In the file browser, expand the new bicycle_app directory you created.

 Note: The directory contains a several .py files, including models.py and views.py.

Expand the bicycle_project directory, and then open the settings.py file in the file editor.

In the INSTALLED_APPS section of the settings.py file, add the bicycle_app to the bottom of the list as follows:


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bicycle_app',
]
Save the changes

Close the settings.py file.

Task 3.2: Configure a basic view and URL settings
Configure a basic view and URL settings by updating the views.py file, and create a new file called urls.py.

Update the bicycle_app/views.py file so that it contains the following lines:


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world from bicycle_app!")
Save the changes.

In the bicycle_app directory, create a new file named ‘urls.py’.

Copy the following code, and then paste it into the urls.py file:


from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
]
Save the changes.

Next, make the following updates to the django/bicycle_project/urls.py file:

 Note: There are two urls.py files. This is a different urls.py file from the one you edited in the previous step.

On the line that starts with from django.urls, update the line to also import include.

In the urlpatterns array, add an additional supported path as follows:

Add  path("", include("bicycle_app.urls")), to make the app available at http://<preview-url>. where <preview-url> is the URL where the Django server is running.

 Note: Because your site currently only has one app, it makes sense to map the base URL to display the app. That is what you have just done.

When done, the file should contain uncommented code as follows:


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("bicycle_app.urls")),
    path("admin/", admin.site.urls),
]
Task 3.3 Test the app
With the app created, in this task, you now test the app for functionality.

Return to the preview app browser tab and refresh the page.

The Hello world from bicycle_app! message you added to the views.py file displays.

hello world webpage

Image description: The image depicts a webpage displaying the message “Hello world from bicycle_app!”.

Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: You installed and configured Django, and you now have the most basic kind of app running on Django.

Django uses a Model-View-Template (MVT) design pattern. This Hello World app does not make use of models or templates, and its use of a view, which you defined in the views.py file, is basic. It returns a simple hard-coded HttpResponse to the requesting page. You learn more about models, views, and templates in the upcoming labs.

Conclusion
You have successfully done the following:

Upgraded packages on Ubuntu, a Linux distribution.
Created a virtual Python environment.
Installed Django using pip.
Created and configured a Django project.
Started the Django server and tested access to it from the internet.
Created a Hello World Django application.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
Creation of Virtual Environments
Django Documentation
Previewing Running Applications in the AWS Cloud9 Integrated Development Environment (IDE)
Django is property of the Django Software Foundation, and Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.