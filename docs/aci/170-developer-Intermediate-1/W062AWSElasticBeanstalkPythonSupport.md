# Week 6: AWS Elastic Beanstalk Python Support

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Review of Elastic Beanstalk

### Pre-assessment

#### What is AWS Elastic Beanstalk?

* A service for deploying and scaling web applications

Wrong answers:

* A database service for structured data
* A machine learning service for predictions
* A storage service for files and objects

#### AWS Elastic Beanstalk supports all of the following programming languages, except one. Which is the programming language that is not supported?

* C/C++

Wrong answers:

* Python
* Java
* Node.js

##### Explanation

* The most common web development languages and frameworks are supported by AWS Elastic Beanstalk, such as Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.

* C/C++ is not supported on Elastic Beanstalk, although, C/C++ could be deployed inside Docker containers that you create.

#### How does AWS Elastic Beanstalk simplify the deployment of applications?

* By automatically handling details like resource provisioning, load balancing, scaling, and application health monitoring

Wrong answers:

* By providing a graphical interface to manually configure underlying resources
* By letting you write infrastructure as code to define resources
* By giving you root access to Amazon EC2 instances running the application

## Benefits and Concepts of Elastic Beanstalk

### Elastic Beanstalk

AWS Elastic Beanstalk is a service that provides an environment to deploy, scale, and manage applications on AWS. With Elastic Beanstalk, developers can quickly upload applications and services without worrying about the infrastructure that runs those applications. Elastic Beanstalk automatically scales compute resources, balances loads, and monitors application health.

To use Elastic Beanstalk, you create an application and package it in a source bundle. You then upload the bundle to Elastic Beanstalk and provide some information about the application. Elastic Beanstalk automatically launches an environment and creates and configures the AWS resources needed to run your code. After your environment is launched, you can then manage your environment and deploy new application versions.

By handling infrastructure provisioning, application version deployment, capacity provisioning, load balancing, scaling, and application health monitoring, Elastic Beanstalk reduces management complexity and operational costs for developers. This lets developers focus on writing code rather than managing infrastructure. Elastic Beanstalk supports a variety of programming languages, including Python, Java, .NET, Node.js, PHP, Ruby, Go, and Docker. It also integrates with developer tools such as AWS CodePipeline to support continuous deployment.

#### [AWS Elastic Beanstalk Features](https://aws.amazon.com/elasticbeanstalk/details/)

### Key benefits

* **Quick deployment**: Get Python applications up and running quickly without manually setting up servers or infrastructure. Just upload code, and Elastic Beanstalk handles deployment.
* **Auto scaling**: Elastic Beanstalk scales Python application instances up and down to meet demand. This handles spikes in traffic without intervention.
* **Multiple environments**: Create different environments like development, test, and production for application lifecycle management.
* **Code focus**: Focus on writing code rather than infrastructure. Elastic Beanstalk handles all the servers, load balancing, and monitoring.
* **Pricing**: There is no additional charge for Elastic Beanstalk. You only pay for the underlying AWS resources that your application consumes.

### Typical use cases

Elastic Beanstalk is commonly used for web applications, API backends, and simple queue or batch processing tasks.

Typical use cases include the following:

* Quickly deploy Python web applications without managing the underlying infrastructure.
* Host Python Web Server Gateway Interface (WSGI) and Flask applications. Elastic Beanstalk provides preconfigured Python platforms that support popular Python web frameworks.
* Deploy machine learning models and Python data-processing scripts as web services with very little configuration.
* Select Elastic Beanstalk as the deployment destination of continuous integration and continuous delivery (CI/CD) pipeline builds. AWS CodePipeline supports Elastic Beanstalk and a deployment action.

Elastic Beanstalk boosts developer productivity by reducing time spent on infrastructure management.

### Concepts

Your application needs several compute, storage, and networking resources. Elastic Beanstalk makes it possible for you to manage these resources by grouping them as environments. To learn more about key Elastic Beanstalk concepts, expand each of the following categories.

#### Application

An Elastic Beanstalk **application** is a logical collection of Elastic Beanstalk components, including environments, versions, and environment configurations. In Elastic Beanstalk, an application is conceptually similar to a folder.

#### Application version

In Elastic Beanstalk, an **application version** refers to a specific, labeled iteration of deployable code for a web application. An application version points to an Amazon Simple Storage Service (Amazon S3) object that contains the deployable code, such as a Java WAR file. An application version is part of an application.

Applications can have many versions, and each application version is unique.

#### Environment

An **environment** is a collection of AWS resources running an application version. Each environment runs only one application version at a time. However, you can run the same application version or different application versions in many environments simultaneously.

#### Environment tier

The **environment tier** designates the type of application that the environment runs, and determines what resources Elastic Beanstalk provisions to support it. For example, an application that serves HTTP requests runs in a web server environment tier.

There are two types of environment tiers:

* **Web server environment**: Run a website, web application, or web API that serves HTTP requests.
* **Worker environment**: Run a worker application that processes long-running workloads on-demand or performs tasks on a schedule.

#### Environment configuration

An **environment configuration** identifies a collection of parameters and settings that define how an environment and its associated resources behave. When you update an environment’s configuration settings, Elastic Beanstalk automatically applies the changes to existing resources or deletes and deploys new resources (depending on the type of change).

#### Saved configuration

A **saved configuration** is a template that you can use as a starting point for creating unique environment configurations.

#### Platform

A **platform** is a combination of an operating system, programming language runtime, web server, application server, and Elastic Beanstalk components. You design and target your web application to a platform.

To work with Elastic Beanstalk, you have to pick an **AWS Region**, like **us-east-2**. You start by creating an application as a placeholder. You need to give it a name, like **pets-app**. When you have an application, you need at least one **environment**. For instance, two environments exist, called **pets-env-blue** and **pets-env-green**. Each environment has its own **configuration** and **platform**. Each environment also points to a specific **application version**. If **pets-env-blue** is your production environment, you can use **pets-env-green** for testing. You can upgrade both the platform and the application version to perform some testing before using it as your new production environment. Next time, **pets-env-blue** becomes the test environment. This is called blue-green deployment, and it is fully supported by Elastic Beanstalk.

## Elastic Beanstalk Web Server Environment Architecture

### Web server environment

A **web server environment** tier is made of components including a load balancer and several Amazon Elastic Compute Cloud (Amazon EC2) instances.

As you create a new web server environment, Elastic Beanstalk provisions networking, compute, and security resources for you.

An **Application Load Balancer (ALB)** from the Elastic Load Balancing (ELB) service routes all the incoming HTTP requests. Clients do not call the load balancer's URL directly, as in **abcd-1234.us-west-2.elb.amazonaws.com**. Instead, Elastic Beanstalk registers a Canonical Name Record (CNAME) in DNS. That record maps one domain name to the load balancer's URL. It acts as an alias record, so clients can call, for instance, **pets-app.elasticbeanstalk.com**. Note that you can reconfigure the CNAME to point to a different ALB in a different environment, which allows blue-green deployments.

The load balancer routes the requests to an Amazon EC2 Auto Scaling group. The group includes instances whose quantity dynamically grows and shrinks based on the traffic load. Adding and removing servers is called horizontal scaling.

Each **EC2 instance** is provisioned by Elastic Beanstalk with a predefined **platform** based on the environment configuration. A stack of software is available for a certain type of web application to run. It can support a particular Python version, for instance.

Each **EC2 instance** has an Elastic Beanstalk process running. It is called a **host manager**. It acts as an agent running commands locally. The Elastic Beanstalk service acts as a controller and calls the local host manager to deploy a new version of an application on that EC2 instance. The host manager is also called to patch the platform. In addition, the host manager has an important role related to monitoring and reporting. It aggregates events and metrics, monitors the application logs for critical errors, monitors the application server part of the platform, and rotates and exports logs to Amazon S3.

### Security

The EC2 instances' network interfaces are protected by a firewall called a **security group**. By default, Elastic Beanstalk allows inbound HTTP traffic in the security group. This is exactly what is needed for an HTTP request routed by the load balancer to arrive at one of the instances and be handled by your web application. This default configuration is appropriate when your load balancer terminates HTTPS. Externally, the connection between the clients and the load balancer is secure. Internally, the connection between the load balancer and the instance is not encrypted. Instead, end-to-end encryption requires the use of configuration files to modify the software running on the instances and to modify the security group to allow secure connections. In that case, the instances would terminate HTTPS.

Your application can make use of other AWS services. Using such APIs requires credentials. The provisioned instances have an instance profile with an **AWS Identity and Access Management (IAM) role**. A role lists the policies to perform actions against the different AWS services.

An IAM role defines what actions are allowed and denied from these instances.

### Persistent storage

Amazon EC2 instances are managed by Elastic Beanstalk. They are instantiated and terminated automatically. It means that whatever your application is storing on the local file system will be lost when the instance disappears. Application data and application logs must be stored externally to Elastic Beanstalk to make them persistent.

Your application can make use of several storage and database services. But for such integration to work properly, extra policies are required in the IAM role attached to the instances.

An Elastic Beanstalk application can make use of an external AWS service to persist data. Amazon S3, Amazon EFS, Amazon CloudWatch, Amazon DynamoDB and Amazon RDS can be integrated.

The integration between your Elastic Beanstalk application and AWS services can be applied at different levels.

* **Built-in Amazon S3 integration** – You can configure your Elastic Beanstalk environment to enable application log rotation and to publish logs automatically to Amazon S3 after they are rotated. This is performed by the **host manager**. The bucket name is preprovisioned and is called **elasticbeanstalk-<region>-<account-id>**.
* **Built-in Amazon CloudWatch integration** – Elastic Beanstalk installs a **CloudWatch log agent** with the default configuration settings on each instance that it creates. You can enable instance log streaming to Amazon CloudWatch Logs. From CloudWatch, subscription filters can be created to stream logs to AWS Lambda or Amazon Kinesis.
* **Elastic Beanstalk resource creation** – Configuration files under the **.ebextensions** folder of your project are used to declare extra AWS resources that must be created automatically when an environment is created. You can declare an Amazon DynamoDB table and an Amazon Elastic File System (Amazon EFS) file system. For the latter, the file system is automatically mounted to the EC2 instances. Note that these extra resources are not tied to your environment's lifecycle. They are not deleted when you terminate your environment because they might contain important customer data.
* **AWS SDK for Python** – Your application can programmatically use the Software Development Kit (SDK) to make calls to the AWS service APIs. Any service can be called, so the possibilities are endless.
* **Framework integration** – Instead of directly coding with the SDK, your application could be based on a framework that has built-in support for some AWS services. For instance, Django allows you to store application media files on Amazon S3 through configuration. This is an easier approach in terms of integration and maintenance.

## Using Elastic Beanstalk with the CLI

### CLI purpose and usage

Elastic Beanstalk provides a command line interface (EB CLI) to create, manage, and monitor environments. The EB CLI integrates with Git to support version control and deployment of applications. To use the EB CLI, first install it on your local machine, and then initialize the EB CLI to integrate it with your AWS account.

After initialization, you can create environments, deploy applications, manage environments, and monitor logs right from the CLI. For example, you can use commands like eb init, eb create, and eb deploy to manage environments. With the EB CLI, you can work with Elastic Beanstalk from your local terminal.

Key benefits are version control integration and streamlined environment management without switching between the CLI and console.

#### [Using the Elastic Beanstalk Command Line Interface](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)

### Installation

The Elastic Beanstalk dedicated CLI can be installed into your IDE with the following command. You install a Python package called **awsebcli**. Installing this package makes the **eb** command available in your terminal.

```bash
pip install awsebcli
```

All **eb** commands should be run in the top-level directory of the Python project (the parent directory of the **.ebextensions** folder). This identifies which application you are deploying to Elastic Beanstalk.

### Common CLI commands and options

The EB CLI provides commands for creating, configuring, and monitoring Elastic Beanstalk environments.

Some common commands include the following.

* **eb init** - Initializes your directory with Elastic Beanstalk. This sets up your environment for creating new applications and environments.
* **eb create** - Creates a new environment and deploys an application version to it. You specify options like AWS Region, environment name, solution stack, and instance type.
* **eb status** - Shows health and status information about your environment. This allows you to monitor your environment.
* **eb deploy** - Deploys your application source bundle to the environment. This updates the environment with your latest code.
* **eb config** - Modifies an environment's configuration settings. For example, you can adjust auto scaling, swap solution stacks, or update environment variables.
* **eb terminate** - Terminates and deletes a running environment. Use this to permanently delete an environment and terminate associated resources.

### Knowledge Check

#### How does AWS Elastic Beanstalk simplify application version management over time?

* By allowing you to roll back to previous versions

Wrong answers:

* By maintaining multiple environments for each version
* By automatically incrementing version numbers
* By storing application artifacts in Amazon S3

#### Which tool can you use to deploy a Python application to AWS Elastic Beanstalk from the command line?

* EB CLI

Wrong answers:

* AWS CloudFormation
* AWS CodeDeploy
* AWS CodePipeline

#### Which AWS services can you use along with AWS Elastic Beanstalk?

* Amazon RDS 

Wrong answers:

* AWS Lambda
* Amazon SageMaker
* AWS Fargate

Amazon RDS can be used as a relational database service and integrates with AWS Elastic Beanstalk.

#### A Django application is about to be deployed on AWS Elastic Beanstalk. Which CLI command can be used to setup a new environment and install the current application version to it?

* eb create

Wrong answers:

* eb deploy
* eb init
* eb status

### Summary

You learned about the key concepts and benefits of using AWS Elastic Beanstalk to deploy and manage web applications. Key topics included deploying and managing applications without worrying about the infrastructure. This module also covered automatically scaling application resources based on demand, and Elastic Beanstalk support for popular programming platforms such as Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.

You learned about the Elastic Beanstalk Command Line Interface (EB CLI), and common eb commands for operations like creating environments, deploying code, monitoring environments, and terminating environments. 

With Elastic Beanstalk, you can focus more on coding applications and less on managing servers. Continue to the next topic to learn about deploying Python applications with Elastic Beanstalk.

## Elastic Beanstalk Python Platform and Tools

### Pre-assessment

#### A Python application deployed in Elastic Beanstalk is using the AWS SDK to read from an Amazon DynamoDB table. Which mechanism is used to allow this action?

* Attach the corresponding IAM policy to the EC2 instance profile

Wrong answers:

* Add an outbound rule to the Elastic Beanstalk security group
* Use an IAM user and password in the code
* Configure the Amazon DynamoDB table

For the code to work, the EC2 instances running the Python application need to have an instance profile with an IAM role. That role must include an IAM policy that allows the read action on the Amazon DynamoDB table resource.

#### Which Python platform versions are supported by AWS Elastic Beanstalk?

* A list of specific Python platform versions

Wrong answers:

* All existing Python platform versions
* Only Python 3.9
* Only Python 3.11

For more information, visit the [Python-based supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.python).

#### Which file do you include in your Python application source bundle to specify application dependencies installed by AWS Elastic Beanstalk?

* requirements.txt

Wrong answers:

* config.yml
* .ebextensions
* setup.py

The requirements.txt file lists the Python dependencies for your application that Elastic Beanstalk will install when building the applications environment.

## Using Elastic Beanstalk with the SDK for Python

You can use the AWS SDK for Python (Boto3) in your Python application to call AWS services, such as Amazon DynamoDB and Amazon S3. You programmatically access these services through a client interface instead of making direct calls to service endpoints. In this section, you will focus on how to use the SDK in Elastic Beanstalk.

### Python packages

The SDK for Python includes two key Python packages:

* **Boto3** – This package implements the SDK for Python itself as **programming interface**s. This is what you are coding against in your application. It allows you to create or retrieve objects like an Amazon Simple Notification Service (Amazon SNS) queue, a DynamoDB table, or an Amazon S3 bucket.
* **Botocore** – This is the library that provides the low-level functionality shared between the SDK for Python and the AWS Command Line Interface (AWS CLI) to access AWS services. This is a hidden dependency that you do not use directly.

To use Boto3, you first need to install it and its dependencies.

```bash
pip install boto3
```

### Boto3 programming interfaces

With Boto3, as a Python developer you can write software that makes use of AWS services for messaging, storage, data analytics, artificial intelligence, and much more. You can access the service API from two interfaces.

* **Client interface** – This is a low-level interface to AWS whose methods map close to one-to-one with service APIs. As a consequence, all service operations are supported by the client interface. As illustrated in the following snippet, you can access a specific object-oriented API through the **client()** method when boto3 is imported. The function requires the name of the service and optionally the AWS Region. Clients are generally thread safe. The client interface can be used for all AWS services supported by Boto3.

```python
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')
sf = boto3.client('stepfunctions')
rek = boto3.client('rekognition')
```

* **Resource interface** – This is an object-oriented interface to AWS services. It gives you a higher-level abstraction than the low-level calls made by service clients. Only a few key AWS services support the resource interface, including Amazon EC2, Amazon S3, DynamoDB, IAM, Lambda, Amazon Simple Queue Service (Amazon SQS), and Amazon SNS. To use resources, you invoke the **resource()** method after boto3 is imported. You must pass in a service name. Note that the SDK for Python team does not intend to add new features to the resource interface. The client interface has to be used for new AWS services.

```python
import boto3

s3 = boto3.resource('s3')
sns = boto3.resource('sns')
ddb = boto3.resource('dynamodb')
ec2 = boto3.resource('ec2')
```

### Boto3 on Elastic Beanstalk

Your Python application has to be deployed to an Elastic Beanstalk environment, together with its dependencies, including Boto3. It runs on one or more Amazon EC2 instances.

For instance, your application is running and using the SDK to get an item from an Amazon DynamoDB table. An IAM role allows the Amazon EC2 instance to perform such action.

The application Python code imports **boto3**, loads the resource interface for DynamoDB, and gets the Pets table object before invoking the database to get the pet with name Buddy. It then prints the owner of that pet.

```python
import boto3
ddb = boto3.resource('dynamodb')
table = ddb.Table('Pets')
response = table.get_item(Key={'Name': 'Buddy'})
item = response['Item']
print(f"Owner: {item['Owner']}")
```

For the code to work, the Amazon EC2 instance must have an instance profile mapped to an IAM role that includes a policy allowing the **dynamodb:GetItem** action on the Pets table resource.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "dynamodb:GetItem",
      "Resource": "arn:aws:dynamodb:us-west-2:123456789:table/Pets"
    }
  ]
}
```

## Using Web Application Frameworks for Elastic Beanstalk

Python web frameworks Django and Flask are both supported by Elastic Beanstalk.

### Definition of a web application framework

A web application framework is a software framework that helps developers build and deploy web applications. Frameworks provide reusable code libraries, templates, file structures, and tools that abstract lower-level details so that developers can focus on the business logic and presentation layers of an application. Some common Python web frameworks that work with Elastic Beanstalk include Django, Flask, Pyramid, Bottle, and Web2py.

These frameworks help structure Python web applications by handling request routing, sessions, templating, and access to databases. Using a framework can speed up web application development and deployment on Elastic Beanstalk.

### The Django web application framework

Django is a high-level Python web framework that supports rapid development of secure and maintainable websites. Django includes an object-relational mapper, a customizable admin interface, and support for common web development tasks like authentication, routing, sessions, and templating.

Key features of Django include the following:

* Separated business logic, data, and presentation layers for cleaner code
* Object-relational mapper (ORM) that maps Python classes to database tables to abstract database access
* Auto-generated admin panels for managing content
* Built-in security features
* Protection from cross-site scripting, SQL injection, and cross-site request forgery

Django aligns with AWS best practices as a proven, scalable framework. Its component-based architecture also aids high availability.

#### [Deploying a Django Application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

#### Django benefits

Using Elastic Beanstalk to host Django applications provides the following benefits:

* Elastic Beanstalk supports deployment of Django applications out of the box. It automatically handles Django application configuration and infrastructure provisioning. Developers can focus on writing application code rather than managing servers.
* It provides auto scaling to match application traffic demands. Additional instances are launched to maintain performance during traffic spikes.
* It deploys application updates through the Elastic Beanstalk CLI or the AWS Management Console. New application versions can be uploaded without downtime.
* It monitors application and infrastructure health. Alerts notify you if resources fail or behave unexpectedly.
* You save on costs because you only pay for the AWS resources needed to run your application. Resources can scale down when not in use.

By handling infrastructure and deployment tasks, Elastic Beanstalk lets developers concentrate on building Django features and business logic. The service scales smoothly in response to demand.

### The Flask web application framework

The Flask framework provides libraries and tools to simplify building lightweight web applications in Python. Some key features of Flask include its simple core with extensions available for added functionality, integrated development server and debugger, RESTful request dispatching, and template engine support.

With Flask, developers can get started with minimal setup and build web applications, backends, and services on AWS with languages and frameworks like Python.

#### [Deploying a Flask Application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)

#### Flask benefits

Using Flask provides several benefits when you deploy Python applications on Elastic Beanstalk:

* **Rapid deployment**: Flask's simplicity makes it fast and efficient to deploy on Elastic Beanstalk. This enables rapid iterations.
* **Flexibility**: Flask's modular design offers flexibility to create stateless Python applications to best use Elastic Beanstalk's auto scaling and load balancing.
* **Productivity**: Flask abstracts away web complexities like handling requests and routing to let you focus on business logic for faster development.
* **Community support**: As an open-source project, Flask has great community support for resolving issues when you are running applications on Elastic Beanstalk.

## Using Web Server Gateway Interface Servers for Elastic Beanstalk

Web servers do not natively speak Python, and Python is not compiled. Therefore, there is a need for an interface between the application and the web server. This Python interface has been standardized and several implementations exist. **Web Server Gateway Interface (WSGI)** is one of the main standards, and it is suitable for **regular synchronous web applications**, where requests are handled one at a time. Example WSGI servers include Gunicorn and gWSGI.

### Production architecture

A typical deployment of a web application is the following. A WSGI server is needed, which is implemented by Gunicorn for instance. In front, Apache HTTP server can serve static files, and handle client connections and proxy requests to WSGI. In this example, a Django application serves the HTTP requests.

Http client < - > Apache HTTP Server < - > gunicorn WSGI Server < - > django application

#### For more information, see [How to deploy Django](https://docs.djangoproject.com/en/stable/howto/deployment/) on the Django website.

### Web Server Gateway Interface

Web Server Gateway Interface (WSGI) is a Python standard for web applications on a production server. It connects web server and Python web application code. Elastic Beanstalk uses WSGI to run Python applications on its servers.

Using WSGI, Elastic Beanstalk connects a web server to a Python application. The interface enables Elastic Beanstalk to perform load balancing, health checks, and scaling. WSGI also simplifies the deployment of a Python application.

Elastic Beanstalk configures WSGI automatically, so developers can focus on writing application code rather than server code.

#### Green Unicorn (Gunicorn)

Green Unicorn (Gunicorn) is a Python WSGI HTTP server for Unix. By default, Elastic Beanstalk uses Gunicorn to serve Python applications. Gunicorn supports multiple worker processes for handling requests and supporting concurrency and parallelism. This improves application performance under load.

#### procfile

A procfile is a text file that is provided in the application's deployment zip file. The procfile specifies process types and commands for an application running on Elastic Beanstalk, and it allows you to declare required processes that should be launched when your application starts. Typically, a procfile declares a single process type named **web**, which launches the command to start your web application.

For example, the following procfile tells Elastic Beanstalk to launch Gunicorn as the WSGI server. At the end of the line is **application**, which is pointing the server to the application code in **application.py**.

```config
web: gunicorn --bind 127.0.0.1:8000 --workers=1 --threads=15 application
```

For Python applications, this command often invokes the Flask, Django, or custom application script. Additional worker or background processes can also be specified. Specifying process types and commands in a procfile gives you full control over how your application is launched.

## Using Reverse Proxy Servers with Elastic Beanstalk

AWS Elastic Beanstalk uses a proxy server to handle HTTP requests to your Python application.

### Reverse proxy server

A reverse proxy server is a type of proxy server that sits in front of web servers and forwards client requests to those web servers. They act as an intermediary between clients and web servers, receiving requests from clients and forwarding them to the appropriate servers. This hides the existence and characteristics of the origin servers.

Reverse proxy servers can provide additional layers of security, caching, compression, and SSL certificate management to application servers behind the proxy. This offloads work from the application servers. Requests can also be distributed across multiple origin servers, providing load balancing and failover capabilities. This helps handle more traffic and improves availability.

#### [Serving Content Using a Fully Managed Reverse Proxy Architecture in AWS](https://aws.amazon.com/blogs/architecture/serving-content-using-fully-managed-reverse-proxy-architecture/)

### Nginx

Nginx (pronounced "engine-x") is a high-performance web server and reverse proxy for handling web traffic. Nginx serves static files very efficiently and can also act as a reverse proxy to application servers such as WSGI or Gunicorn to handle dynamic requests. By default, Elastic Beanstalk uses Nginx to handle requests to Python applications deployed on the platform.

Nginx listens for requests and serves static files directly. Dynamic requests are proxied to the WSGI server running the Python application. This setup permits to handle static content and dynamic content separately. This improves performance and efficiency.

Http client < - > NGINX Proxy Server < - > gunicorn WSGI Server < - > django application

### Apache HTTP server

An Apache HTTP server is open-source software that enables a computer to act as a web server. It receives requests through the HTTP or HTTPS protocols and serves web pages or applications in response. The Apache HTTP server is the most popular web server software, used by over 50 percent of active websites.

When you deploy a web application on Elastic Beanstalk, it can automatically handle provisioning an Apache HTTP server to host your application code. Elastic Beanstalk configures the Apache server with optimal settings for running Python applications. This makes it possible to handle requests efficiently and serve your web application's dynamic content and static files.

Although Nginx is the default reverse proxy server deployed, you have the option to choose between Nginx or Apache during the deployment configuration.

The option to choose the proxy server is in the **Platform software** section of the create application deployment process within the Elastic Beanstalk console.

Http client < - > Apache HTTP Server < - > gunicorn WSGI Server < - > django application

## Using the Pipenv Packaging Tool for Elastic Beanstalk

### Introduction to Pipenv

Pipenv is a packaging tool for Python that helps manage virtual environments and dependencies when you are building Python applications. Pipenv creates a Pipfile and Pipfile.lock to track which packages and versions are installed in an application's virtual environment. When deploying a Python application to Elastic Beanstalk, a **requirements.txt** file is needed to install the application's dependencies.

Pipenv can generate a **requirements.txt** file from the **Pipfile.lock**, ensuring consistency between development and production environments. Pipenv integrates virtualenv and pip to create isolated Python environments for each project. It resolves dependencies and installs dependent packages automatically. Using Pipenv ensures replicable builds and enables deploying the same artifacts across environments.

### Benefits of using Pipenv with Elastic Beanstalk

Using Pipenv solves common dependency problems when you are deploying Python applications, such as locking dependency versions, ensuring replicable builds, and preventing bugs from new releases. It manages a separate virtual environment for each project to avoid conflicts between application dependencies. It also integrates with pip to install dependencies from PyPI.

By handling these dependency and environment issues, Pipenv streamlines deploying Python applications on Elastic Beanstalk.

For example, if a Python application has to communicate with a MySQL database, the **mysqlclient** dependency must be installed. Elastic Beanstalk can do this from a **requirements.txt** file that contains a list of the dependencies and versions that must be installed.

#### [Create an Application Source Bundle](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html)

### Knowledge Check

#### What can you use to run custom commands that configure the AWS Elastic Beanstalk environment?

* .ebextensions

Wrong answers:

* .ebignore
* .elasticbeanstalk
* requirements.txt

The **.ebextensions** folder contains YAML or JSON scripts that run commands to customize the Elastic Beanstalk environment.

#### Which service can you use to monitor metrics and set alarms for an AWS Elastic Beanstalk environment?

* Amazon CloudWatch

Wrong answers:

* AWS CloudTrail
* AWS X-Ray
* AWS CodeDeploy

CloudWatch provides metrics and alarms for Elastic Beanstalk instances and environments.

#### How can a developer access the AWS SDK for Python in code?

* import boto3

Wrong answers:

* import botocore
* import sdk
* import aws

AWS SDK for Python (Boto3) can be imported in a Python file using **import boto3**. It gives access to the client interface and the resource interface.

### Summary

Elastic Beanstalk provides a Python platform that developers can use to deploy and scale Python web applications. This platform supports popular Python web frameworks like Django and Flask, making it straightforward to get started with writing web applications in Python. Behind the scenes, Elastic Beanstalk handles provisioning of AWS resources like EC2 instances and load balancers, so the developer can focus on their code.

AWS SDK for Python provides an API for interacting programmatically with AWS services like Elastic Beanstalk. Developers can write scripts using AWS SDK for Python to deploy their applications, manage environments, and automate administrative tasks.

AWS SDK for Python also integrates nicely with Python web frameworks like Django and Flask. Elastic Beanstalk configures the Python platform with tools optimized for running Python web applications. For WSGI servers, it uses Gunicorn, which is designed for high performance production environments. For dependency and environment management, it includes Pipenv, which locks down dependencies and creates isolated virtual environments.

Proxy servers like Nginx and Apache efficiently handle routing requests and serving static assets. The Python platform, and included tools, make Elastic Beanstalk a convenient way to get Python web applications deployed and running on AWS.
